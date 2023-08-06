
import logging
import asyncio

from lxml import etree as et

log = logging.getLogger(__name__)


class Vmix8099ClientProtocol(asyncio.Protocol):
    def __init__(self, eventloop, input):
        self.transport = None
        self.loop = eventloop
        self.xml = et.fromstring("<vmix/>")
        self.xmllength = 0
        self.xmlstr = ''
        self.input = input
        self._inProgress = '' # Set to type of MESSAGE if running into second TCP datagram (normally XML types as everything else is small)

    def connection_made(self, transport):
        self.transport = transport

        self.transport.write('SUBSCRIBE ACTS\r\n'.encode())
        self.transport.write('SUBSCRIBE TALLY\r\n'.encode())
        self.transport.write('XML\r\n'.encode())
        self.input.registerCallBacks(self.update_field) # connect to the input file reader once connected to vMix

    def data_received(self, byteData):
        BLOCK_ENDING = '\r\n'
        strBuffer = byteData.decode()

        log.debug(f'Data received: {strBuffer}')
        # Prcess string Buffer until none left
        while len(strBuffer) > 0:
            if strBuffer.startswith('VERSION'):
                data, _, strBuffer = strBuffer.partition(BLOCK_ENDING)
                # buffer = buffer.encode() # back to bytes
                log.debug(f'VMIX VERSION :{data}')
                continue
            if strBuffer.startswith('XML') or self._inProgress=='XML':
                xml, self._inProgress, strBuffer = vmixXMLdecoder.vmixXMLdecode(strBuffer)
                if len(xml.getchildren()) > 0:
                    self.xml = xml
                continue

            # if buffer.decode().startswith('ACTS OK '):
            #     data, _, buffer = buffer.decode().partition(BLOCK_ENDING)
            #     log.debug(f'ACTS: {data}')
            #     continue

            # if buffer.decode().startswith('TALLY OK '):
            #     data, _, buffer = buffer.decode().partition('\r\n')
            #     log.debug(f'TALLY: {data}')
            #     continue

            # if buffer.decode().startswith('SUBSCRIBE OK '):
            #     data, _, buffer = buffer.decode().partition('\r\n')
            #     log.debug(f'SUBSCRIBE: {data}')
            #     continue

            if strBuffer.startswith('FUNCTION OK '):
                data, _, strBuffer = strBuffer.partition(BLOCK_ENDING)
                # buffer = buffer.encode() # back to bytes
                log.debug(f'FUNCTION OK :{data}')
                continue

            if self._inProgress == '':
                data, _, strBuffer = strBuffer.partition(BLOCK_ENDING)
                log.warning(f'DATA:{data}| UNKOWN: Not sure... discard')
                continue
            


    # async def update_visable(self, field_name, value):
    #     log.debug(f'UPDATE_VISABLE: {field_name}, {value}')
    #     # for field in self.xml.xpath(f'.//image[starts-with(@name,"{field_name}.")]'):
    #     for field in self.xml.xpath(f'.//image[@name="{field_name}.Source"]'):
    #         input_number = field.getparent().attrib.get('number')
    #         if value.strip() == '':
    #             function_str = f'FUNCTION SetImageVisibleOff Input={input_number}&SelectedValue={field_name}.Source\r\n'
    #         else:
    #             function_str = f'FUNCTION SetImageVisibleOn Input={input_number}&SelectedValue={field_name}.Source\r\n'
    #             # await self.update_field(field_name, value)
    #         print(function_str)
    #         self.transport.write(function_str.encode())
            
    async def update_field(self, field_name, value):
        ''' Field_name is the TCSldXXX or Bowl0 etc
        ### TODO - use self.xml to determine if we actually need to send the update
        Or does this matter loadwise?
        Need to ensure we have an upto date xml though!'''

        log.debug(f'update_field| field_name:{field_name}| value:{value}')
        
        # print(f'Print: UPDATE_FIELD: {field_name} {value}')

        # Support for legacy titles with legacy field naming:
        for field in self.xml.xpath(f'.//text[@name="{field_name}"]'):
        
                input_number = field.getparent().attrib.get('number')
                valueStrip = value.strip()
                function_str = f'FUNCTION SetText Input={input_number}&SelectedName={field_name}&Value={valueStrip}\r\n'

                log.info(f'UPDATE_FIELD| Found a legacy match in vmix input {input_number} {field_name}, setting to {valueStrip}')
                print(function_str)
                self.transport.write(function_str.encode())

        fieldNameList = [
            # field_name,
            field_name[5:] + ' ',
            field_name[5:] + '.',
        ]
        for name in fieldNameList:
            for field in self.xml.xpath(f'.//text[starts-with(@name, "{name}")]'):
                
                vmixname = field.attrib.get('name')
                input_number = field.getparent().attrib.get('number')
                valueStrip = value.strip()
                function_str = f'FUNCTION SetText Input={input_number}&SelectedName={vmixname}&Value={valueStrip}\r\n'

                log.info(f'UPDATE_FIELD| Found a match in vmix input {input_number} {vmixname} for {name} setting to {valueStrip}')
                print(function_str)
                self.transport.write(function_str.encode())
        
    def connection_lost(self, exc):
        log.critical('The server closed the connection')
        # print('Stop the event loop')
        # self.loop.stop()


class vmixXMLdecoder():
    ''' # TODO - Make into a proper vMix_XML_Handler 
    ie receivers parent substites a handler and then you always ask the handler for xml and don't have a local xml back in the client 
    '''
    _xmllength = 0
    _xmlstr = '<vmix/>'

    @property
    def xml(self):
        return et.fromstring(self._xmlstr)

    @classmethod
    def vmixXMLdecode(cls, buffer):
        ''' return self.xml, inProgress, buffer
        buffer of xml data '''
        log.debug(f'vmixXMLdecode| str:{buffer}| _xmllength:{cls._xmllength}| _xmlstr:{cls._xmlstr}')
        if buffer.startswith('XML'):
            cls._xmlstr = ''
            inProgress = 'XML'

            data, _, buffer = buffer.partition('\r\n')

            xmllength = data.rpartition('XML ')[2]
            cls._xmllength = int(xmllength) #- len(xmllength)
            log.info(f'_xmllength:{cls._xmllength}|len(buffer):{len(buffer)}')

        log.debug(f'str:{buffer}| len(buffer):{len(buffer)}| _xmllength:{cls._xmllength}| _xmlstr:{cls._xmlstr}')
        
        if len(buffer) == 0:
            # TODO Should still have a valid xml to return here!
            xml = et.fromstring('<vmix/>')
            return xml, inProgress, buffer

        if len(buffer) < cls._xmllength:
            # Not enounch in the buffer so set inProgress and return
            cls._xmlstr += buffer
            cls._xmllength -= len(buffer)
            inProgress = 'XML'
            
            # TODO Should still have a valid xml to return here!
            xml = et.fromstring('<vmix/>')
            return xml, inProgress, ''

        if len(buffer) >= cls._xmllength:
            # greater or equal so return what is left of the buffer
            cls._xmlstr += buffer[:cls._xmllength]
            buffer = buffer[cls._xmllength:]
            
            xml = et.fromstring(cls._xmlstr)
            # No longer in progress
            inProgress = ''
            return xml, inProgress, buffer


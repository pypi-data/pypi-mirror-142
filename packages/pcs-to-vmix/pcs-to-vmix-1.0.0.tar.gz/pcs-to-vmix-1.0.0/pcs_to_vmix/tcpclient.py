import logging
import asyncio
import os
from time import sleep
from lxml import etree as et


class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, loop, input):
        self.transport = None
        self.loop = loop
        self.xml = et.Element("vmix")
        self.xmllength = 0
        self.xmlstr = ''
        self.input = input

    def connection_made(self, transport):
        self.transport = transport
        # transport.write(self.message.encode())
        # print('Data sent: {!r}'.format(self.message))
        self.transport.write('SUBSCRIBE ACTS\r\n'.encode())
        self.transport.write('SUBSCRIBE TALLY\r\n'.encode())
        self.transport.write('XML\r\n'.encode())
        self.input.start(loop, transport, self.update_field, self.update_visable) # connect to the input file reader once connected to vMix

    def data_received(self, data):
        log.debug(f'Data received: {data.decode()}')
        buffer = data.decode()
        while len(buffer) > 0:
            if self.xmllength > 0:
                data, _, buffer = buffer.partition('\r\n')
                self.xmlstr += data
                self.xmllength = self.xmllength - len(data)
                print(f'xmllength = {self.xmllength}')
            if self.xmllength <= 2:
                if self.xmlstr != '':
                    print('HAVE ALL THE XML')
                    try:
                        self.xml = et.fromstring(self.xmlstr)
                    except TypeError as ex:
                        log.criticil(f'Error with XML received: {ex}')

                self.xmllength = 0
                self.xmlstr = ''

            data, _, buffer = buffer.partition('\r\n')
            if data.startswith('VERSION'):
                log.debug(f'Connection response...')
                # self.transport.write('SUBSCRIBE ACTS\r\n'.encode())
            elif data.startswith('XML'):
                # data, _, buffer = buffer.partition('\r\n')
                self.xmllength = int(data.rpartition('XML ')[2])
            elif data.startswith('ACTS OK '):
                # data, _, buffer = buffer.partition('\r\n')
                log.debug(f'ACTS: {data}')
            elif data.startswith('TALLY OK '):
                # data, _, buffer = buffer.partition('\r\n')
                log.debug(f'TALLY: {data}')
            elif data.startswith('SUBSCRIBE OK '):
                # data, _, buffer = buffer.partition('\r\n')
                log.debug(f'SUBSCRIBE: {data}')
            elif data.startswith('FUNCTION OK '):
                # data, _, buffer = buffer.partition('\r\n')
                log.debug(f'FUNCTION: {data}')
            else:
                # data, _, buffer = buffer.partition('\r\n')
                log.info(f'UNKOWN: Not sure... throw away until next {data}\\r\\n')

    async def update_visable(self, field_name, value):
        log.debug(f'UPDATE_VISABLE: {field_name}, {value}')
        # for field in self.xml.xpath(f'.//image[starts-with(@name,"{field_name}.")]'):
        for field in self.xml.xpath(f'.//image[@name="{field_name}.Source"]'):
            input_number = field.getparent().attrib.get('number')
            if value.strip() == '':
                function_str = f'FUNCTION SetImageVisibleOff Input={input_number}&SelectedValue={field_name}.Source\r\n'
            else:
                function_str = f'FUNCTION SetImageVisibleOn Input={input_number}&SelectedValue={field_name}.Source\r\n'
                # await self.update_field(field_name, value)
            print(function_str)
            self.transport.write(function_str.encode())
            
    async def update_field(self, field_name, value):
        log.debug(f'UPDATE_FIELD: {field_name} {value}')
        # print(f'Print: UPDATE_FIELD: {field_name} {value}')
        for field in self.xml.xpath(f'.//text[@name="{field_name}"]'):
            # field_name = f'TCSld{field_no}'
            input_number = field.getparent().attrib.get('number')
            
            function_str = f'FUNCTION SetText Input={input_number}&SelectedName={field_name}&Value={value.strip()}\r\n'
            print(function_str)
            self.transport.write(function_str.encode())
            
        # for field in self.xml.xpath(f'.//text[@name="TCSld{field_no}.Text"]'):
        #     input_number = field.getparent().attrib.get('number')
        #     field_name = f'TCSld{field_no}.Text'
        #     print(field)
        #     self.transport.write(f'FUNCTION SetText Input={input_number}&SelectedName={field_name}&Value={value.strip()}\r\n'.encode())
        
    def connection_lost(self, exc):
        log.info('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()


async def read_file(filename):
        log.info(f'NEED TO PROCESS {filename}')
        scoredata = et.parse(filename).getroot()
        return scoredata


class Input():
    def start(self, loop, transport, cb_update_field, cb_update_visability):
        self.loop = loop
        self.transport = transport
        self.cb_update_field = cb_update_field
        self.cb_update_visability = cb_update_visability
        self.loop.create_task(self.watch_for_file_change())

    async def watch_for_file_change(coro, interval=1):
        # coro.transport is the above transport.
        filename = "S:\\_Scoreboards\\Output\\nvplay-scoreboard1.xml"
        print('Start wait')
        await asyncio.sleep(10 * interval) 
        print('Finsih wait')
        file_datetime = 0
        while True:
            if not os.path.exists(filename):
                log.debug(f'DOES NOT EXIST: {filename} ')
                file_datetime = 0
            else:
                new_file_datetime = os.path.getmtime(filename)
                log.debug(f'mtime {new_file_datetime}')
                if  new_file_datetime != file_datetime:
                    file_datetime = new_file_datetime
                    # Ensure upto date XML in vMIX connection
                    coro.transport.write('XML\r\n'.encode())
                    
                    scoredata = await read_file(filename)
                    # Process file
                    # Process Fields in file with matching fields in title graphics
                    for item in scoredata.xpath('//Field'):
                        await coro.cb_update_field(f'TCSld{item.attrib.get("no")}',item.text)
                        await coro.cb_update_field(f'TCSld{item.attrib.get("no")}.Text',item.text) # GT Titles
                        await coro.cb_update_visability(f'TCSvis{item.attrib.get("no")}',item.text) # Any non empty string after strip() will make visable.
                        if item.attrib.get('no') == '610':
                            await coro.cb_update_field('Bowl0',item.text)
                        if item.attrib.get('no') == '611':
                            await coro.cb_update_field('Bowl1',item.text)
                        if item.attrib.get('no') == '612':
                            await coro.cb_update_field('Bowl2',item.text)
                        if item.attrib.get('no') == '613':
                            await coro.cb_update_field('Bowl3',item.text)
                        if item.attrib.get('no') == '614':
                            await coro.cb_update_field('Bowl4',item.text)
                        if item.attrib.get('no') == '615':
                            await coro.cb_update_field('Bowl5',item.text)
                        if item.attrib.get('no') == '616':
                            await coro.cb_update_field('Bowl6',item.text)
                        if item.attrib.get('no') == '617':
                            await coro.cb_update_field('Bowl7',item.text)
                        if item.attrib.get('no') == '618':
                            await coro.cb_update_field('Bowl8',item.text)
                        if item.attrib.get('no') == '482':
                            if item.text.strip() != '':
                                await coro.cb_update_field('TCSBrace482',f'({item.text})')
                            else:
                                await coro.cb_update_field('TCSBrace482',f'')
                        if item.attrib.get('no') == '492':
                            if item.text.strip() != '':
                                await coro.cb_update_field('TCSBrace492',f'({item.text})')
                            else:
                                await coro.cb_update_field('TCSBrace492',f'')
                        if item.attrib.get('no') == '457':
                            overball = item.text.partition('.')[2]
                            await coro.cb_update_field('TCSOverBall',f'.{overball}')
                    # Bowl0 -> Bowl6
                    # Cricket logic here to work these out and update the fields
                    

            await asyncio.sleep(interval) 



log = logging.getLogger("")
formatter = logging.Formatter("%(asctime)s %(levelname)s " +
                                "[%(module)s:%(lineno)d] %(message)s")
# setup console logging
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

ch.setFormatter(formatter)
log.addHandler(ch)

loop = asyncio.get_event_loop()
# message = 'Hello World!\r\n'
# e = EchoClientProtocol('jjjjj',loop)
# loop.create_connection(EchoClientProtocol, '127.0.0.1', 8099)
input = Input()

coro = loop.create_connection(lambda: EchoClientProtocol(loop, input),
                              '127.0.0.1', 8099)

loop.run_until_complete(coro)
loop.run_forever()
loop.close()
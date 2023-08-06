
# import asyncio
# from vmix import Vmix

# async def tcp_echo_client(message):
#     reader, writer = await asyncio.open_connection(
#         '127.0.0.1', 8099)

#     print(f'Send: {message!r}')
#     writer.write(message.encode())
#     await writer.drain()

#     data = await reader.read(100)
#     print(f'Received: {data.decode()!r}')

#     print('Close the connection')
#     writer.close()
#     await writer.wait_closed()

import asyncio
import os
import logging
from vmix import Vmix

log = logging.getLogger(__name__)

clients = {}  # task -> (reader, writer)


def make_connection(host, port, v):

    task = asyncio.Task(handle_client(host, port, v))

    clients[task] = (host, port)

    def client_done(task):
        del clients[task]
        log.info("Client Task Finished")
        if len(clients) == 0:
            log.info("clients is empty, stopping loop.")
            loop = asyncio.get_event_loop()
            loop.stop()

    log.info("New Client Task")
    
    task.add_done_callback(client_done)


# @asyncio.coroutine
async def handle_client(host, port, v):
    log.info("Connecting to %s %d", host, port)
    client_reader, client_writer = asyncio.open_connection(host, port)
    log.info("Connected to %s %d", host, port)
    try:
        # looking for a hello
        # give client a chance to respond, timeout after 10 seconds
        data = asyncio.wait_for(client_reader.readline(), timeout=10.0)

        if data is None:
            log.warning("Expected VERSION OK from vMIX, received None")
            return

        sdata = data.decode().rstrip().upper()
        log.info("Received %s", sdata)
        if not sdata.startswith('VERSION OK'):
            log.warning("Expected VERSION OK from vMIX - received '%s'", sdata)
            return
        _, _, version = sdata.rpartition('OK ')
        # v.version = version

        # send back a WORLD
        client_writer.write("XML\r\n".encode())

        # wait for a READY
        data = asyncio.wait_for(client_reader.readline(), timeout=10.0)

        if data is None:
            log.warning("Expected READY, received None")
            return

        sdata = data.decode().rstrip().upper()
        if sdata.startswith('XML'):
            # process incoming XML
            log.debug(f'XML Header received')
            length = int(sdata.rpartition('XML ')[2])
            xmlraw = asyncio.wait_for(client_reader.readline(), timeout=10.0)
            print(f'LENGTH: {length} {len(xmlraw)}')
            if length != len(xmlraw):
                log.error(f'xmlraw length not equal to what vMIX told us!!')
            # will this always get ALL the XML??
            print(xmlraw)
        elif sdata.startswith('FUNCTION'):
            if sdata != 'FUNCTION OK Completed':
                log.error(f'FUNCTION not OK! {sdata}')
        elif sdata.starswith('TALLY'):
            log.info(f'TALLY: {sdata}')
            pass
        elif sdata.startswith('ACTS'):
            log.info(f'ACTS: {sdata}')
            pass
        elif sdata.startswith('SUBSCRIBE'):
            log.info(f'SUBSCRIBE: {sdata}')
            pass
        else:
            log.error(f'UNKNOW Data returned from vMIX {sdata}')


        # data = yield from asyncio.wait_for(client_reader.readline(),
        #                                     timeout=10.0)
        # echostrings = ['one', 'two', 'three', 'four', 'five', 'six']

        # for echostring in echostrings:
        #     # send each string and get a reply, it should be an echo back
        #     client_writer.write(("%s\n" % echostring).encode())
        #     
        #     if data is None:
        #         log.warning("Echo received None")
        #         return

        #     sdata = data.decode().rstrip()
        #     log.info(sdata)

        # # send BYE to disconnect gracefully
        # client_writer.write("BYE\n".encode())

        # # receive BYE confirmation
        # data = yield from asyncio.wait_for(client_reader.readline(),
        #                                    timeout=10.0)

        sdata = data.decode().rstrip().upper()
        log.info("Received '%s'" % sdata)
    finally:
        log.info("Disconnecting from %s %d", host, port)
        client_writer.close()
        log.info("Disconnected from %s %d", host, port)


# Python program to find MD5 hash value of a file
import hashlib
def get_md5(filename):
    # filename = input("Enter the file name: ")
    md5_hash = hashlib.md5()
    with open(filename,"rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()


async def read_file(filename):
    log.info(f'Need to read {filename}')
    
    return

# @asyncio.coroutine
async def watch_for_file_change(filename, interval=1):
    file_datetime = 0
    while True:
        if not os.path.exists(filename):
            log.debug(f'DOES NOT EXIST: {filename} ')
            file_datetime = 0
        else:
            new_file_datetime = os.path.getmtime(filename)
            log.info(f'mtime {new_file_datetime}')
            if  new_file_datetime != file_datetime:
                file_datetime = new_file_datetime
                
                # await asyncio.get_event_loop().run_until_complete(read_file(filename))
                await read_file(filename)
        await asyncio.sleep(interval)    

class VmixClientProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.xml = ''
        self.loop = loop

    def connection_made(self, transport):
        transport.write('SUBSCRIBE ACTS'.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        # self.loop.stop()

# loop = asyncio.get_event_loop()
# message = 'Hello World!'
# coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
#                               '127.0.0.1', 8888)
# loop.run_until_complete(coro)
# loop.run_forever()
# loop.close()


def main():
    log.info("MAIN begin")
    loop = asyncio.get_event_loop()
    # for x in range(200):
    v = Vmix()
    # loop.create_task()
    coro = loop.create_connection(lambda: VmixClientProtocol(loop), '127.0.0.1', 8099)
    loop.run_until_complete(coro)
    # loop.run_until_complete(watch_for_file_change('./data/input.xml'))
    
    # make_connection('localhost', 8099, v)
    # watch_pcs('./data/scores.xml', v.consume_pcs)
    
    loop.run_forever()
    log.info("MAIN end")

if __name__ == '__main__':
    log = logging.getLogger("")
    formatter = logging.Formatter("%(asctime)s %(levelname)s " +
                                  "[%(module)s:%(lineno)d] %(message)s")
    # setup console logging
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(formatter)
    log.addHandler(ch)
    main()



# if __name__=="__main__":
#     print('The entry point for it all!')


#     v = Vmix('con')

    


#     asyncio.run(tcp_echo_client('Hello World!'))
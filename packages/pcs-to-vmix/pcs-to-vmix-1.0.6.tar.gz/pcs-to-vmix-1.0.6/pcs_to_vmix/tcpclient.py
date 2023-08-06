#!/usr/env python3


import logging
import asyncio
import os
import argparse

from time import sleep

from lxml import etree as et

from pcs_to_vmix.version import VERSION
from pcs_to_vmix.vmix import Vmix8099ClientProtocol

log = logging.getLogger(__name__)


class PCSScoreboardFileWatcher():
    _signal_kv = [] # call these functions with item:value
    def __init__(self, filename, interval=1) -> None:
        self.interval = interval
        self.filename = filename
        log.info(f'filename:{filename}| PCS Filewatcher creeted...')

    def registerCallBacks(self, cb_kv):
        ''' PCS Only know a value has become smoething 
        I can have cricket logic but should have no down stream logic!'''
        self._signal_kv.append(cb_kv)

    async def watch_for_file_change(self):
        # It seems a lot of file change watching systems don't work on network drives
        # Therefore we need to just poll
        filename = self.filename
        interval = self.interval
        log.info(f'filename:{filename}| PCS Filewatcher async routine...')
        # Think i needed at some point this wait for vMix to be online
        print('Start wait')
        await asyncio.sleep(2 * interval) 
        print('Finsih wait')
        file_datetime = 0
        while True:
            # And while loop waits...
            log.debug(f'filename:{filename}| PCS Filewatcher loop...')
            await asyncio.sleep(interval) 
            if not os.path.exists(filename):
                log.error(f'DOES NOT EXIST: {filename} ')
                file_datetime = 0
            else:
                new_file_datetime = os.path.getmtime(filename)
                log.debug(f'mtime {new_file_datetime}')
                if  new_file_datetime != file_datetime:
                    file_datetime = new_file_datetime

                    # Not for PCS class to worry about
                    # # Ensure upto date XML in vMIX connection
                    self.scoredata = et.parse(filename).getroot() # read_file(filename)
                    await self.processUpdatedInput()

    async def processUpdatedInput(self):
        # Process file
        # Process Fields in file with matching fields in title graphics
        for item in self.scoredata.xpath('//Field'):
            attrib_no = item.attrib.get("no")
            for cb in self._signal_kv:
                await cb(f'TCSld{attrib_no}', item.text)

                if 610 <= int(attrib_no) <= 618:
                    await cb(f'Bowl{attrib_no[-1]}', item.text)

                if attrib_no  == '482':
                    if item.text.strip() != '':
                        await cb('TCSBrace482',f'({item.text})')
                    else:
                        await cb('TCSBrace482',f'')

                if attrib_no == '492':
                    if item.text.strip() != '':
                        await cb('TCSBrace492',f'({item.text})')
                    else:
                        await cb('TCSBrace492',f'')

                if item.attrib.get('no') == '457':
                    overball = item.text.partition('.')[2]
                    await cb('TCSOverBall',f'.{overball}')


def main():
    log = logging.getLogger("")
    formatter = logging.Formatter("%(asctime)s %(levelname)s " +
                                    "[%(module)s:%(lineno)d] %(message)s")
    # setup console logging
    log.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    ch.setFormatter(formatter)
    log.addHandler(ch)
    # from ..setup import setup
    log.info(f'VERSION:{VERSION} | Info log message')
    log.warning(f'VERSION:{VERSION} | Warning log message')


    my_parser = argparse.ArgumentParser(description=''''Conect Play Cricket Scorer to vMIX''')
    # Add the arguments
    my_parser.add_argument('--path',
                        action='store',
                        type=str,
                        default='c:/vmix/livedata.xml',
                        help='PCS Scorboard Output file - see README.md for how to configure PCS')

    my_parser.add_argument('--vmixip',
                        action='store',
                        type=str,
                        default='127.0.0.1',
                        help='vMix IP')

    my_parser.add_argument('--vmixport',
                        action = 'store',
                        type = int,
                        default = 8099,
                        help='vMix port')
    # Execute the parse_args() method
    args = my_parser.parse_args()

    # pcs_data_file = "S:\\_Scoreboards\\Output\\nvplay-scoreboard1.xml"

    loop = asyncio.get_event_loop()

    input = PCSScoreboardFileWatcher(args.path)

    coro = loop.create_connection(lambda: Vmix8099ClientProtocol(loop, input),
                                args.vmixip, args.vmixport)
    
    loop.create_task(input.watch_for_file_change())
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()


if __name__=="__main__":
    main()
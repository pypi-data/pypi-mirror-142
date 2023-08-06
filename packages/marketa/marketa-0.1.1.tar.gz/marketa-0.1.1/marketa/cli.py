#!/usr/bin/env python3

"""Marketa command line interface
Usage:
    marketa (status | watch <symbol> | unwatch <symbol> | pull | clean | monitor | install | uninstall)
    marketa -h|--help
    marketa -v|--version
Commands:
    status              reports it's current configuration status
    watch <symbol>      adds symbol to a watchlist
    unwatch <symbol>    removes symbol from watchlist
    pull                gets latest historical data for symbols in watchlist refreshing local caches
    clean               removes cached data
    monitor             runs marketa in 'monitor' service mode, getting regular updates for watchlist symbols
    install             installs, enables and starts marketa 'monitor' mode as a systemd service
    uninstall           uninstalls marketa systemd service
Options:
    -h --help           show this screen
    -v --version        show version
"""

import os, sys, subprocess
from time import sleep
from pathlib import Path

from docopt import docopt
from exitstatus import ExitStatus
from datetime import datetime
import humanize
from marketa.shared.utils import hookup_tqdm
from marketa.shared.exceptions import MarketaException
from marketa import get_facade
mk = get_facade()


def pull():
    print('pulling data for symbols in the watchlist ...')
    mk.pull()
    print('data for symbols in watchlist was succesfully updated')


def watch(symbol:str):
    if mk.is_watching(symbol):
        raise MarketaException(f'symbol "{symbol}" is already in the watchlist')

    mk.watch(symbol)
    print(f'symbol "{symbol}" added to the watchlist')


def unwatch(symbol:str):
    if not mk.is_watching(symbol):
        raise MarketaException(f'symbol "{symbol}" is not in the watchlist')

    mk.unwatch(symbol)
    print(f'symbol "{symbol}" removed from the watchlist')


def monitor():
    try:
        while True:
            print('marketa is running in monitor mode!', flush=True)
            sleep(5)
        
    except BaseException as e:
        print(f'unexpected error: {e}')
        raise e


src = Path(__file__).parent.joinpath('marketa.service')
dst = '/etc/systemd/system/marketa.service'

def install():
    print('installing service ...')
    subprocess.check_call(f'sudo cp {src} {dst}', shell=True)
    subprocess.check_call('sudo systemctl daemon-reload', shell=True)
    subprocess.check_call('sudo systemctl enable marketa', shell=True)
    print('starting service ...')
    subprocess.check_call('sudo systemctl start marketa', shell=True)
    subprocess.check_call('systemctl status marketa', shell=True)
    print('service installed successfully and running')

    
def uninstall():
    print('stopping service ...')
    subprocess.check_call('sudo systemctl stop marketa', shell=True)
    subprocess.check_call('sudo systemctl disable marketa', shell=True)
    subprocess.check_call(f'sudo rm {dst}', shell=True)
    subprocess.check_call('sudo systemctl daemon-reload', shell=True)
    print('service uninstalled successfully')


def status():
    s = mk.get_state()
    watchlist = s['watchlists']['default']
    result = f'watching {len(watchlist)} symbols: '
    result+= ', '.join(watchlist)
    result+='\n'
    result+=' data last updated: '
    if 'data_updated_on' in s.keys():
        result += humanize.naturaltime(datetime.now() - s['data_updated_on'])
    else:
        result+='never'
    
    print(result)


def clean():
    mk.clear_caches()
    print('cache cleaned succesfully')


if __name__ == '__main__':
    try:
        arguments = docopt(str(__doc__), version='0.1.0') # semver MAJOR.MINOR.PATCH
        hookup_tqdm() # enable tqdm progress bar

        if arguments['pull']:
            pull()
        elif arguments['clean']:
            clean()
        elif arguments['watch']:
            watch(arguments['<symbol>'][0])
        elif arguments['unwatch']:
            unwatch(arguments['<symbol>'][0])
        elif arguments['status']:
            status()
        elif arguments['monitor']:
            monitor()
        elif arguments['install']:
            install()
        elif arguments['uninstall']:
            uninstall()
        else:
            print('invalid arguments specified')

    except MarketaException as e:
        print(f'error: {e}')
        sys.exit(ExitStatus.failure)

    except Exception as e:
        print(f'unexpected error: {e}')
        raise e
        sys.exit(ExitStatus.failure)

    sys.exit(ExitStatus.success)

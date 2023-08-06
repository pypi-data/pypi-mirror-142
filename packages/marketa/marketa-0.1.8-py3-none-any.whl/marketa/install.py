import subprocess
from pathlib import Path
from marketa.shared.constants import systemd_service_path
from marketa.shared.utils import is_root, is_systemd_installed, is_systemd_service_running, file_replace_string
from marketa.shared.exceptions import MarketaException


def install():
    print('installing marketa ...')
    if not is_root():
        raise MarketaException('error: you must use sudo to install marketa systemd service')
    if not is_systemd_installed():
        raise MarketaException('error: systemd is not installed on this machine')
    if is_systemd_service_running('marketa'):
        raise MarketaException('error: marketa service is already installed on this machine')

    print('configuring systemd service ...')
    template_path = Path(__file__).parent.joinpath('template.service')
    path = Path(systemd_service_path)
    cli_path = Path(__file__).parent.joinpath('cli.py')
    file_replace_string(template_path, path, old_string='<path>', new_string=str(cli_path))
    subprocess.check_call('systemctl daemon-reload', shell=True)
    subprocess.check_call('systemctl enable marketa', shell=True)

    print('starting service ...')
    subprocess.check_call('systemctl start marketa', shell=True)
    subprocess.check_call('systemctl status marketa', shell=True)
    print('marketa systemd service started')

    print('marketa installed successfully')

    
def uninstall():
    print('uninstalling marketa ...')

    if not is_root():
        raise MarketaException('error: you must use sudo to uninstall marketa systemd service')
    if not is_systemd_installed():
        raise MarketaException('error: systemd is not installed on this machine')
    
    print('stopping service ...')
    subprocess.check_call('systemctl stop marketa', shell=True)

    print('uninstalling service ...')
    subprocess.check_call('systemctl disable marketa', shell=True)
    subprocess.check_call(f'rm {systemd_service_path}', shell=True)
    subprocess.check_call('systemctl daemon-reload', shell=True)

    print('marketa uninstalled successfully')

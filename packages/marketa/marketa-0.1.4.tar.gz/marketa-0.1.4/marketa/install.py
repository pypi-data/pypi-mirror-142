import subprocess
from pathlib import Path
from marketa.shared.constants import systemd_service_path
from marketa.shared.utils import is_root


def install():
    print('installing marketa ...')

    cli_path = Path(__file__).parent.joinpath('cli.py')
    subprocess.check_call(f'chmod +x {cli_path}', shell=True)
    if is_root():
        target_path = Path('/usr/local/bin')
    else:
        target_path = Path.home().joinpath('.local/bin').resolve()
    print(f'registering mk soft link in {target_path}')
    subprocess.check_call(f'rm -f mk', shell=True, cwd=target_path)
    subprocess.check_call(f'ln -s {cli_path} mk', shell=True, cwd=target_path)

    if is_root():
        print('configuring systemd service ...')
        path = Path(__file__).parent.joinpath('marketa.service')
        inplace_change(path, old_string='<path>', new_string=str(cli_path))
        subprocess.check_call(f'sudo cp {path} {systemd_service_path}', shell=True)
        subprocess.check_call('sudo systemctl daemon-reload', shell=True)
        subprocess.check_call('sudo systemctl enable marketa', shell=True)

        print('starting service ...')
        subprocess.check_call('sudo systemctl start marketa', shell=True)
        subprocess.check_call('systemctl status marketa', shell=True)
        print('marketa systemd service started')

    print('marketa installed successfully')

    
def uninstall():
    print('stopping service ...')

    subprocess.check_call('sudo systemctl stop marketa', shell=True)
    subprocess.check_call('sudo systemctl disable marketa', shell=True)
    subprocess.check_call(f'sudo rm {systemd_service_path}', shell=True)
    subprocess.check_call('sudo systemctl daemon-reload', shell=True)

    print('service uninstalled successfully')


def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            raise Exception('"{old_string}" not found in {filename}.'.format(**locals()))

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)

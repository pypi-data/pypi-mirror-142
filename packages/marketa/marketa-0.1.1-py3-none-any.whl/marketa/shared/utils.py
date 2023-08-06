import pathlib, os
import string, random


def check_internet(host="8.8.8.8", port=53, timeout=3) -> bool:
    """
    tests if there is internet connection available
    taken from https://stackoverflow.com/questions/3764291/how-can-i-see-if-theres-an-available-and-active-network-connection-in-python
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    import socket
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        #print(ex)
        return False


def get_cache_folder_path():
    return pathlib.Path(os.environ.get('XDG_STATE_HOME') 
        or pathlib.Path.home().joinpath('.local', 'state')).joinpath('marketa', 'cache').resolve()


chars = string.ascii_letters + string.octdigits
def random_string_generator(str_size, allowed_chars = chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


def hookup_tqdm():
    import sys, marketa.shared.taskeeper as taskeeper, tqdm
    mod = sys.modules[__name__]
    # hookup tdqm with taskeeper
    def task_start(steps: int):
        mod.pbar = tqdm.tqdm(total = steps)
    taskeeper.on_start_callback = task_start
    def step_start(name: str):
        mod.pbar.set_description(name)
    taskeeper.on_step_start_callback = step_start
    def step_finish():
        mod.pbar.update()
    taskeeper.on_step_finish_callback = step_finish
    def task_finish(info: str):
        mod.pbar.set_description(info)
        mod.pbar.close()
    taskeeper.on_finish_callback = task_finish

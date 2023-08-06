import os
import pdb

from mitmdump import DumpMaster, Options
from mitmproxy.optmanager import _Option
from typing import Union

from .lib.root_dir import RootDir

PROXY_URL_FILENAME = 'proxy_url'
INTERCEPT_HANDLER_FILENAME = 'intercept_handler.py'

def run(**kwargs):
    __create_proxy_url_file(kwargs.get('listen_host'), kwargs.get('listen_port'))

    fixed_options = {
        'flow_detail': 1,
        'scripts': __get_intercept_handler_path(),
        'upstream_cert': False,
    }

    opts = Options(**{**kwargs, **fixed_options})
    __set_connection_strategy(opts, 'lazy')

    m = DumpMaster(opts)
    m.run()

def get_proxy_url() -> Union[str, None]:
    path = __proxy_url_abs_path()
    if not os.path.exists(path):
        return None

    with open(path) as f:
        return f.read()

def filter_options(options):
    # Filter out non-mitmproxy options
    options['listen_host'] = options['proxy_host']
    options['listen_port'] = options['proxy_port']

    del options['headless']
    del options['log_level']
    del options['proxy_host']
    del options['proxy_port']
    del options['ui_host']
    del options['ui_port']
    del options['api_url']
    del options['test_script']

def __get_intercept_handler_path():
    cwd = os.path.dirname(os.path.realpath(__file__))
    script = os.path.join(cwd, INTERCEPT_HANDLER_FILENAME)
    return script
##
#
# Equivalent of:
# mitmdump connection_strategy={strategy}
#
def __set_connection_strategy(opts, strategy):
    extra_options = {
        'dumper_filter': f"connection_strategy={strategy}",
        'readfile_filter': f"connection_strategy={strategy}",
        'save_stream_filter': f"connection_strategy={strategy}",
    }
    for k, v in extra_options.items():
        opts._options[k] = _Option(k, str, v, '', None)
    opts.update(**extra_options)

def __proxy_url_abs_path():
    tmp_dir_path = RootDir.instance().tmp_dir
    return os.path.join(tmp_dir_path, PROXY_URL_FILENAME)

def __create_proxy_url_file(host, port):
    file_path = __proxy_url_abs_path()
    tmp_dir_path = os.path.dirname(file_path)
    if not os.path.exists(tmp_dir_path):
        os.mkdir(tmp_dir_path)

    with open(file_path, 'w') as f:
        f.write(f"http://{host}:{port}")

def __remove_proxy_url_file():
    file_path = __proxy_url_abs_path()
    if os.path.exists(file_path):
        os.remove(file_path)

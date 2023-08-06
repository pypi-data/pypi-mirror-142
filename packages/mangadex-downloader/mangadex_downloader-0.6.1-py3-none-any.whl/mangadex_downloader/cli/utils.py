import logging
import signal
import sys

from ..network import Net
from ..downloader import _cleanup_jobs
from ..errors import NotLoggedIn

log = logging.getLogger(__name__)

def setup_logging(name_module, verbose=False):
    log = logging.getLogger(name_module)
    handler = logging.StreamHandler()
    fmt = logging.Formatter('[%(levelname)s] %(message)s')
    handler.setFormatter(fmt)
    log.addHandler(handler)
    if verbose:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
    return log

def setup_proxy(proxy=None, from_env=False):
    if proxy and from_env:
        log.warning('--proxy and --proxy-env options are present, --proxy option will be ignored')

    if from_env:
        log.debug("Using proxy from environments")

    if proxy:
        log.debug('Setting up proxy from --proxy option')
        Net.set_proxy(proxy)

def _keyboard_interrupt_handler(*args):
    print("Cleaning up...")
    # Downloader are not cleaned up
    for job in _cleanup_jobs:
        job()

    # Unfinished jobs in pdf converting
    from ..format.pdf import _cleanup_jobs as pdf_cleanup

    for job in pdf_cleanup:
        job()

    # Logging out
    try:
        Net.requests.logout()
    except NotLoggedIn:
        pass

    print("Action interrupted by user", file=sys.stdout)
    sys.exit(0)

def register_keyboardinterrupt_handler():
    # CTRL+C is pressed
    signal.signal(signal.SIGINT, _keyboard_interrupt_handler)

    # CTRL+D (in Unix) is pressed or taskkill without force (in Windows)
    signal.signal(signal.SIGTERM, _keyboard_interrupt_handler)

def close_network_object():
    log.info("Cleaning up...")
    log.debug("Closing netwok object")
    Net.close()
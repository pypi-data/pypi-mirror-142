"""A library that provides a Python interface to the INTELLIHUB APIs."""

__author__ = 'INTELLIHUB'
__email__ = 'connect@spotflock.com'
__copyright__ = 'Copyright (c) 2019-2020 The Spotflock Technologies LLC'
__version__ = '1.4.1'
__url__ = 'https://github.com/Spotflock/intellihub-sdk-python'
__download_url__ = ''
__description__ = 'A Python wrapper around the INTELLIHUB API'

from .core import IntellihubAiClient

import json
import requests
import warnings

def custom_formatwarning(msg, *args, **kwargs):
    # ignore everything except the message
    return str(msg) + '\n'

try:
    url = f"https://pypi.org/pypi/intellihub/json"
    data = json.loads(requests.get(url).text)
    latest_version = data['info']['version']
    installed_version = __version__
    if str(installed_version) != str(latest_version):
        warnings.filterwarnings('ignore', '.*do not.*')
        warnings.formatwarning = custom_formatwarning
        warnings.warn(f'New version of intellihub ({latest_version}) available, you are still using older ({installed_version}) version of the intellihub, Please update using "pip install intellihub=={latest_version}"', FutureWarning)
except:
    pass

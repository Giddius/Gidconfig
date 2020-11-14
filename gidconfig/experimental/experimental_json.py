# region [Imports]

# * Standard Library Imports -->
import gc
import os
import re
import sys
import json
import lzma
import time
import queue
import logging
import platform
import subprocess
from enum import Enum, Flag, auto
from time import sleep
from pprint import pprint, pformat
from typing import Union
from datetime import tzinfo, datetime, timezone, timedelta
from functools import wraps, lru_cache, singledispatch, total_ordering, partial
from contextlib import contextmanager
from collections import Counter, ChainMap, deque, namedtuple, defaultdict
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# * Third Party Imports -->
# import requests
# import pyperclip
# import matplotlib.pyplot as plt
# from bs4 import BeautifulSoup
# from dotenv import load_dotenv
# from github import Github, GithubException
# from jinja2 import BaseLoader, Environment
# from natsort import natsorted
# from fuzzywuzzy import fuzz, process

# * PyQt5 Imports -->

# * Gid Imports -->
import gidlogger as glog
from gidconfig.utility.functions import pathmaker, loadjson, writejson

from gidconfig.experimental.experimental_abstract import GidAttConfigAbstract
# endregion[Imports]

__updated__ = '2020-11-14 01:43:00'

# region [AppUserData]

# endregion [AppUserData]

# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion[Logging]

# region [Constants]

# endregion[Constants]


class GidAttConfigJson(GidAttConfigAbstract):
    def __init__(self, config_file):
        super().__init__(config_file)

    def load(self):
        _config_dict = loadjson(self.config_file)
        for section, value in _config_dict.items():
            setattr(self, section, value)
            self.added_attributes.append(section)
            setattr(self, 'set_' + section, partial(self._edit_dict_attribute, section))
            self.added_attributes.append('set_' + section)


# region[Main_Exec]

if __name__ == '__main__':
    pass

# endregion[Main_Exec]

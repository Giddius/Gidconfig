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
from abc import ABC, abstractmethod

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


# endregion[Imports]

__updated__ = '2020-11-14 01:40:20'

# region [AppUserData]

# endregion [AppUserData]

# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion[Logging]

# region [Constants]

# endregion[Constants]


class GidAttConfigAbstract(ABC):
    def __init__(self, config_file):
        self.config_file = config_file
        self.timedelta_template = "{negative}days: {days}, hours: {hours}, minutes: {minutes}, seconds: {seconds}"
        self.timedelta_regex = re.compile(r"^days:\s*?(?P<days>\d*?),\s*?hours:\s*?(?P<hours>\d*?),\s*?minutes:\s*?(?P<minutes>\d*?),\s*?seconds:\s*?(?P<seconds>\d*?)$")
        self.typus_data = {}
        self.added_attributes = []

    @abstractmethod
    def load(self):
        ...

    @abstractmethod
    def save(self):
        ...

    @abstractmethod
    def new_section(self, section_name, **options):
        ...

    @abstractmethod
    def _edit_dict_attribute(self, section, **kwargs):
        ...

    # region[Main_Exec]


if __name__ == '__main__':
    pass

# endregion[Main_Exec]

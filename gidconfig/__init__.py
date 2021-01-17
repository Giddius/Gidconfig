"""
Configuration provider package, that exposes the section as attribute and also automatically keeps the config file and object in sync.
Through the Factory/Strategy the config objects are singletons as long as they point to the same file.
"""

__version__ = '0.1.7'

from .standard import *
from .data import *


def last_updated(as_datetime=False):
    import os
    import re
    from datetime import datetime
    from functools import partial
    collected_times = []
    this_file_dir = os.path.abspath(os.path.dirname(__file__))
    last_updated_regex = re.compile(r"(?P<updatetime>(?<=__updated__ \= ').*(?='))")
    for dirname, folderlist, filelist in os.walk(this_file_dir):
        for file in filelist:
            if file.endswith('.py'):
                with open(os.path.join(dirname, file), 'r') as pyfile:
                    regex_result = last_updated_regex.search(pyfile.read())
                    if regex_result:
                        collected_times.append(regex_result.groupdict()['updatetime'])

    collected_times = list(map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), collected_times))
    latest_time = max(collected_times)
    if as_datetime is True:
        return latest_time
    return latest_time.strftime("%Y-%m-%d %H:%M:%S")

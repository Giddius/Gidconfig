# region [Imports]

# * Standard Library Imports -->
import os

# import pyperclip
# import re
# import shutil
# import sys
# import time

# *GID Imports -->
from gidconfig.utility.functions import pathmaker, writeit


# * Gid Imports -->

import gidlogger as glog

# endregion [Imports]

# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion [Logging]

# region [Constants]


# endregion [Constants]


# region [Paths]

def appdata_folder():
    return pathmaker(os.getenv('APPDATA'))

# endregion [Paths]


# region [Functions_1]

def make_user_app_folder(in_app_name):
    _path = pathmaker(appdata_folder(), in_app_name)
    if os.path.exists(_path) is False:
        os.makedirs(_path)
    return _path
# endregion [Functions_1]


# region [Functions_2]

def create_configs(app_name, solid='default', user='default', database='default'):
    _path = make_user_app_folder(app_name)
    _solidcfg = solid_config_string_std if solid == 'default' else solid
    _usercfg = user_config_string_std if user == 'default' else user
    _databasecfg = database_config_string_std if database == 'default' else database


# endregion [Functions_2]


# region [Main_Exec]
if __name__ == '__main__':
    pass


# endregion [Main_Exec]

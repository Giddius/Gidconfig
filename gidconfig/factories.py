# region [Imports]

# * Standard Library Imports -->
import os

# * Gid Imports -->
import gidlogger as glog
from gidconfig.data.enums import Cfg
from gidconfig.classes import ConfigHandler

# endregion [Imports]

__updated__ = '2020-11-14 14:55:14'

# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion [Logging]

# region [Factories]


class ConfigRental:
    UCFG = None
    SCFG = None
    DCFG = None
    appdata = None

    @classmethod
    def set_appdata(cls, appdata_object):
        cls.appdata = appdata_object

    @classmethod
    def get_config(cls, variant: Cfg, cfg_folder=None):
        if cls.appdata is None and cfg_folder is None:
            raise FileExistsError('appdata has not been set')
        _folder = cls.appdata['config'] if cfg_folder is None else cfg_folder

        if variant == Cfg.User:
            if cls.UCFG is None:
                cls.UCFG = ConfigHandler(os.path.join(_folder, 'user_config.ini').replace('\\', '/'), inline_comment_prefixes='#')
            return cls.UCFG
        elif variant == Cfg.Solid:
            if cls.SCFG is None:
                cls.SCFG = ConfigHandler(os.path.join(_folder, 'solid_config.ini').replace('\\', '/'), inline_comment_prefixes='#')
            return cls.SCFG
        elif variant == Cfg.Database:
            if cls.DCFG is None:
                cls.DCFG = ConfigHandler(os.path.join(_folder, 'db_config.ini').replace('\\', '/'), inline_comment_prefixes='#')
            return cls.DCFG
        else:
            raise KeyError('unable to rent out Config of type ' + str(variant) + ' and location ' + str(_folder))


# endregion [Factories]


# region [Main_Exec]
if __name__ == '__main__':
    pass


# endregion [Main_Exec]

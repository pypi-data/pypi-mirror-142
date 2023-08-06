import inspect
import os
import sys
from pathlib import Path

try:
    __MAINPATH__ = Path(inspect.getfile(sys.modules.get("__main__"))).parent
    conf_name = "maxoptics.conf"
    if os.path.exists(__MAINPATH__ / conf_name):
        __CONFIGPATH__ = __MAINPATH__ / conf_name
    elif os.path.exists(__MAINPATH__.parent / conf_name):
        __CONFIGPATH__ = __MAINPATH__.parent / conf_name
    elif os.path.exists(__MAINPATH__.parent.parent / conf_name):
        __CONFIGPATH__ = __MAINPATH__.parent.parent / conf_name
    else:
        ind = list(sys.modules.keys()).index("maxoptics")
        secondary_path = Path(inspect.getfile(list(sys.modules.values())[ind - 1]))
        if os.path.exists(secondary_path.parent / conf_name):
            __CONFIGPATH__ = secondary_path.parent / conf_name
        elif os.path.exists(secondary_path.parent.parent / conf_name):
            __CONFIGPATH__ = secondary_path.parent.parent / conf_name
        elif os.path.exists(secondary_path.parent.parent.parent / conf_name):
            __CONFIGPATH__ = secondary_path.parent.parent.parent / conf_name
        else:
            __CONFIGPATH__ = ''

except AttributeError:
    print("Warning: No __main__ modules found, using the default configuration")
    __CONFIGPATH__ = ""
    __MAINPATH__ = Path(".")

except TypeError:
    print("Warning: No __main__ modules found, using the default configuration")
    __CONFIGPATH__ = ""
    __MAINPATH__ = Path(".")

# Version Number
__VERSION__ = "0.5.5"


class MosLibrary:
    def __new__(cls, **kws):
        from .sdk import MaxOptics

        cls.mos_instance = MaxOptics(**kws)
        return cls.mos_instance

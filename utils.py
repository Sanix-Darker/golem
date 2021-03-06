#
# A list of usefull functions and methods
# utils.py
#

from pygolem import *


def generate_app(_path, _type, _name="golem_app", stxt=None, INSERT=None):
    if _type.lower() == "py":
        if stxt is not None:
            pyg = PyGolem(_path, _name, stxt, INSERT)
            pyg.generate_app()
        else:
            pyg = PyGolem(_path, _name)
            pyg.generate_app()
    else:
        print("[+] This language is not handle by Golem")

from .. import __version__

import sys
import importlib

__module__ = sys.modules[__name__]

def execute(kwargs):
    command = kwargs.pop('command')

    if command is None:
        raise TypeError('not command')
        
    importlib.__import__('.'.join((__package__, command)) , fromlist=('execute'))
    getattr(__module__, command).execute(**kwargs)

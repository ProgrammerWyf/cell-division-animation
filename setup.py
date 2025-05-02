# coding=utf-8
from distutils.core import setup
import py2exe

INCLUDE = ['pygame']

options = {
    "py2exe":{ 'compressed' : 1,
        'optimize' : 2,
        'bundle_files' : 1,
        'includes':INCLUDE,
        'dll_excludes' : ['MSVCR100.dll']}
}

setup(
    options= options,
    description='植物细胞有丝分裂模型',
    zipfile = None,
    console = [{"script":'multiply.py'}]
)
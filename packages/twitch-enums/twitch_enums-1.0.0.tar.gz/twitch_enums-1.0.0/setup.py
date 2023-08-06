try: from setuptools import setup
except: from distutils.core import setup

from re import search, sub, I

modules = ['twitch_enums_extensions', 'twitch_enums']

version = sub(r'\'|__version__|=', '', search(r'__version__.*=.*', open('./twitch_enums.py', 'r+', encoding='utf-8').read(), I).group()).strip()
author = sub(r'\'|__author__|=', '', search(r'__author__.*=.*', open('./twitch_enums.py', 'r+', encoding='utf-8').read(), I).group()).strip()

setup(
    name='twitch_enums',
    version=version,
    author=author,
    maintainer=author,
    py_modules=modules,
    description='Unofficial twitch api enums. (Scopes, Apis)'
)
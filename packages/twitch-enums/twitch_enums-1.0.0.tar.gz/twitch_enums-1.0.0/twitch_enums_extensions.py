from __future__ import generators

from enum import Enum as _Enum
from functools import cache as _cache
from typing import NamedTuple as _NamedTuple

class API(_NamedTuple):
    url: str
    method: str

class Enum(_Enum):
    '''A base enum class for twitch api enums.'''
    @classmethod
    @property
    @_cache
    def as_list(cls):
        yield from [k.value for k in cls]

    @classmethod
    @property
    @_cache
    def as_dict(cls):
        return {k.name: k.value for k in cls}

broadcast_url = 'rtmp://{}/app/{}/{}?{}'
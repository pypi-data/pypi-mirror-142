"""
@author axiner
@version v1.0.0
@created 2022/3/12 22:40
@abstract
@description
@history
"""
import typing as t


class Config(dict):

    def __init__(self, defaults: t.Optional[dict] = None) -> None:
        dict.__init__(self, defaults or {})

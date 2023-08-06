"""
@author axiner
@version v1.0.0
@created 2022/1/25 19:22
@abstract
@description
@history
"""
from pathlib import Path

from xrpa.base import BaseRobot


class Robot(BaseRobot):
    """robot"""

    _ = Path().absolute()
    defaults = {
        'indir': _.joinpath('indir'),
        'outdir': _.joinpath('outdir'),
    }

    def __init__(self):
        super().__init__()
        self.defaults['indir'].mkdir(parents=True, exist_ok=True)
        self.defaults['outdir'].mkdir(parents=True, exist_ok=True)

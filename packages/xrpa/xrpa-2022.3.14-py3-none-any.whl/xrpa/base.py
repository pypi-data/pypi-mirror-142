"""
@author axiner
@version v1.0.0
@created 2022/1/25 19:22
@abstract
@description
@history
"""
import sys
import time
import typing as t

from xrpa.config import Config


class BaseRobot:
    config: Config
    processes: dict = {}
    defaults: dict

    def __init__(self):
        self.config = Config(self.defaults)

    def run(self):
        processes = self.__sort_processes()
        for index, process in processes:
            for i, item in enumerate(process, 1):
                sys.stdout.write(f"[process-{index}-{i}]: start executing.....\n")
                item['call']()
                time.sleep(item['sleep'])

    def rule(self, index: int = 0, sleep: t.Union[int, float] = 0):
        def decorator(func: t.Callable):
            self.processes.setdefault(index, []).append({'call': func, 'sleep': sleep})
            return func
        return decorator

    def __sort_processes(self):
        return sorted(self.processes.items(), key=lambda item: item[0])

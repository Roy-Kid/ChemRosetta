# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-11-21
# version: 0.0.1

from dataclasses import dataclass

class Command:
    
    commands = []
    
    def __new__(cls, *args,**kwargs):
        ins = super().__new__(cls)
        cls.commands.append(ins)
        return ins
    
    @classmethod
    def reset(cls):
        cls.commands = []
    
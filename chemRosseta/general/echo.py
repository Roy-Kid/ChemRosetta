# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-11-21
# version: 0.0.1

from chemRosseta.command import Command

class echo(Command):
    
    def __init__(self, kwarg) -> None:
        super().__init__()
        self.echoinfo = kwarg
        
    def toLAMMPS(self):
        return f'echo\t{self.echoinfo}'
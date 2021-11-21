# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-11-21
# version: 0.0.1

from typing import Literal
from .command import Command

class System:
    
    def __init__(self, systemType: Literal['MD', 'QM']) -> None:
        
        self.Command = Command
        self.systemType = systemType
        
    def write(self, filename, format: Literal['LAMMPS']):
        
        write_command = f'to{format}'
        
        with open(filename, 'w') as f:
            for command in self.Command.commands:
                line = getattr(command, write_command)()
                f.write(line)
                
    @property
    def ncommand(self):
        return len(self.Command.commands)
    
    @property
    def commands(self):
        return self.Command.commands
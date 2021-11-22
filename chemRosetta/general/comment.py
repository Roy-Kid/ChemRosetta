# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-11-21
# version: 0.0.1

from chemRosetta.command import Command, dataclass

@dataclass
class comment(Command):
    
    comment: str
        
    def toLAMMPS(self):
        return '# ' + self.comment
    
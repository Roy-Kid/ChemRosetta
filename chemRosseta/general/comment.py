# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-11-21
# version: 0.0.1

from chemRosseta.command import Command

class comment(Command):
    
    def __init__(self, comment) -> None:
        super().__init__()
        self.comment = comment
        
    def toLAMMPS(self):
        return '# ' + self.comment
    
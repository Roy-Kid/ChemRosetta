
    
from chemRosetta.command import Command, dataclass

@dataclass
class neighborlist(Command):

    skin: float
    skinStyle: str
    delay: int = 10
    freq: int = 1000
    check: bool = True
    capacity: int = 1000

    def toLAMMPS(self):
        c1 = f'neighbor {self.skin} {self.skinStyle}'
        c2 = f'neigh_modify  delay {self.delay} check {self.check}'
        return '\n'.join([c1, c2])
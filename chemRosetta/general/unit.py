from chemRosetta.command import Command
from dataclasses import dataclass

@dataclass
class unit(Command):

    unit: str

    def toLAMMPS(self):
        return f'units\t{self.unit.lower()}'
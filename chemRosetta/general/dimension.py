from chemRosetta.command import Command, dataclass

@dataclass
class dimension(Command):

    dimension: int

    def toLAMMPS(self):
        return f'dimension {self.dimension}'
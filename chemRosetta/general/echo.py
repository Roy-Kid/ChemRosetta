from chemRosetta.command import Command, dataclass

@dataclass
class echo(Command):

    kwarg: str

    def toLAMMPS(self):
        return f'echo\t{self.kwarg}'
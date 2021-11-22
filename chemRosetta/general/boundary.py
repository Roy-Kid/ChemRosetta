from chemRosetta.command import Command, dataclass

@dataclass
class boundary(Command):

    x: str
    y: str
    z: str
    
    def toLAMMPS(self):
        return f'boundary {self.x} {self.y} {self.z}'
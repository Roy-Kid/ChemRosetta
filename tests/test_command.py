from dataclasses import dataclass
from chemRosetta.command import Command
from chemRosetta import *

def test_command():
    system = System('MD')
    cmd = Command()
    assert len(cmd.commands) == 1
    cmd = Command()
    assert len(cmd.commands) == 2
    
def test_inherit():
    
    @dataclass
    class testCommand(Command):
        key: int
        
    t1 = testCommand(1)
    assert t1.key
    
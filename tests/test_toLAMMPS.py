from chemRosetta import *
from chemRosetta.general import *

fname = 'pe.input'

system = System(systemType='MD')
comment(fname)
unit('LJ')
dimension(3)
boundary('p', 'p', 'p')
neighborlist(skin=0.2, skinStyle='bin', delay=10, freq=1000, check=True, capacity=1000)

system.write(fname, 'LAMMPS')
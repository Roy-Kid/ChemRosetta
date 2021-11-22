# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-11-21
# version: 0.0.1

import pytest
from chemRosetta import *
from chemRosetta.general import *
# from chemRosetta.general import comment


def test_lammps():
    
    comment('1 charge and N dipoles')
    echo('both')
    unit('lj')
    # dimension('3')
    # boundary('p', 'p', 'p')
    # neighbor(0.2, 'bin')
    # neighbor_modify('delay' '1' 'one' '10000')
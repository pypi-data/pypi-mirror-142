#!/usr/bin/env python3
#------------------------------------------------------------------------------#
#  fortnet-ase: Interfacing Fortnet with the Atomic Simulation Environment     #
#  Copyright (C) 2021 - 2022  T. W. van der Heide                              #
#                                                                              #
#  See the LICENSE file for terms of usage and distribution.                   #
#------------------------------------------------------------------------------#


'''Dummy regression test to set up CI workflow.'''


import pytest


_TOLERANCE = 1.0e-10


def test_dummy():
    '''Dummy regression test to set up CI workflow.'''

    assert True


if __name__ == '__main__':
    pytest.main()

#------------------------------------------------------------------------------#
#  fortnet-ase: Interfacing Fortnet with the Atomic Simulation Environment     #
#  Copyright (C) 2021 - 2022  T. W. van der Heide                              #
#                                                                              #
#  See the LICENSE file for terms of usage and distribution.                   #
#------------------------------------------------------------------------------#


'''
This module defines a FileIOCalculator for the Behler-Parrinello-Neural-Network
implementation Fortnet, therefore interfacing it with the ASE Python package.

https://github.com/vanderhe/fortnet
'''


import os
import h5py
import hsd
import numpy as np
from ase.calculators.calculator import FileIOCalculator
from fortformat import Fnetdata, Fnetout
from .common import FortnetAseError


# conversion factors
# (according to prog/fortnet/lib_dftbp/constants.F90)
BOHR_AA = 0.529177249
AA_BOHR = 1.0 / BOHR_AA
HARTREE_EV = 27.2113845
EV_HARTREE = 1.0 / HARTREE_EV

ELEMENTSYMBOL = ['h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne',
                 'na', 'mg', 'al', 'si', 'p ', 's ', 'cl', 'ar', 'k', 'ca',
                 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 'cu', 'zn',
                 'ga', 'ge', 'as', 'se', 'br', 'kr', 'rb', 'sr', 'y', 'zr',
                 'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn',
                 'sb', 'te', 'i', 'xe', 'cs', 'ba', 'la', 'ce', 'pr', 'nd',
                 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb',
                 'lu', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg',
                 'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr', 'ra', 'ac', 'th',
                 'pa', 'u', 'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm',
                 'md', 'no', 'lr', 'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds',
                 'rg', 'cn', 'nh', 'fl', 'mc', 'lv', 'ts', 'og']

FNETDATA = 'fnetdata.hdf5'
FNETOUT = 'fnetout.hdf5'

def hsd_from_file(fname):
    '''Deserializes HSD file into nested Python dictionaries.

    Args:

        fname (str): name of HSD file to read

    Returns:

        inp (dict): HSD input as nested dictionaries

    '''

    inp = hsd.load(fname)

    return inp


def hsd_to_file(inp, fname):
    '''Dumps Python dictionary to HSD format and disk.

    Args:

        inp (dict): dictionary representation of an HSD input
        fname (str): name of HSD file to write

    '''

    hsd.dump(inp, fname)


def get_fortnet_input(netstat, finitediffdelta, forces):
    '''Generates a suitable Python dictionary for a prediction run of Fortnet.

    Args:

        netstat (str): path to the netstat file to initialize network from
        finiteDiffDelta (float): coordinate shift to calculate central
            finite differences (unit: Angstrom)
        forces (bool): true, if forces shall be calculated by Fortnet

    Returns:

        fnetinp (dict): Fortnet compatible input as nested dictionaries

    '''

    fnetinp = {}

    fnetinp['Options'] = {}
    fnetinp['Options']['Mode'] = 'predict'
    fnetinp['Options']['ReadNetStats'] = 'Yes'
    fnetinp['Options']['WriteIterationTrajectory'] = 'No'

    fnetinp['Data'] = {}
    fnetinp['Data']['Dataset'] = FNETDATA
    fnetinp['Data']['NetstatFile'] = netstat

    if forces:
        fnetinp['Analysis'] = {}
        fnetinp['Analysis']['Forces'] = {}
        # analytical forces are the default
        if finitediffdelta is None:
            fnetinp['Analysis']['Forces']['Analytical'] = {}
        else:
            fnetinp['Analysis']['Forces']['FiniteDifferences'] = {}
            if finitediffdelta <= 0.0:
                msg = 'Error while processing finite difference delta ' + \
                    str(finitediffdelta) + '. Must be positive.'
                raise FortnetAseError(msg)
            fnetinp['Analysis']['Forces']['FiniteDifferences']['Delta'] = \
                finitediffdelta

    return fnetinp


def _check_bpnn_configuration(fname, tforces):
    '''Checks a given Netstat file for compliance with ASE's expectations.

    Args:

        fname (str): path to the netstat file
        tforces (bool): true, if force analysis is requested

    '''

    with h5py.File(fname, 'r') as netstatfile:
        netstat = netstatfile['netstat']
        # currently only the BPNN topology is allowed
        if 'netstat/bpnn' in netstatfile:
            bpnn = netstat['bpnn']
        else:
            msg = "Error while reading netstat file '" + fname + \
                "'. No network group/information present."
            raise FortnetAseError(msg)

        # read number of system-wide targets
        nglobaltargets = bpnn.attrs.get('nglobaltargets')
        if len(nglobaltargets) == 1:
            nglobaltargets = nglobaltargets[0]
        else:
            msg = "Error while reading netstat file '" + self._fname + \
                "'. Unrecognized number of global targets obtained."
            raise FortnetAseError(msg)

        # read number of atomic targets
        natomictargets = bpnn.attrs.get('natomictargets')
        if len(natomictargets) == 1:
            natomictargets = natomictargets[0]
        else:
            msg = "Error while reading netstat file '" + self._fname + \
                "'. Unrecognized number of atomic targets obtained."
            raise FortnetAseError(msg)

        if nglobaltargets != 1 or natomictargets != 0:
            msg = "Error while reading netstat file '" + fname + \
                "'. Only networks trained on a single global property" + \
                " are supported."
            raise FortnetAseError(msg)

        atomicnumbers = np.sort(np.array(bpnn['atomicnumbers'], dtype=int))

        for atnum in atomicnumbers:
            element = ELEMENTSYMBOL[atnum - 1]
            subnet = bpnn[element + '-subnetwork']
            topology = np.array(subnet['topology'], dtype=int)

            if topology[-1] != 1:
                msg = "Error while reading netstat file '" + fname + \
                    "'. Only networks trained on a single global property" + \
                    " are supported."
                raise FortnetAseError(msg)

        # inquire structural ACSF mappings
        if 'netstat/mapping' not in netstatfile and tforces:
            msg = "Error while reading netstat file '" + fname + \
                "'. Calculation of forces is only supported in combination" + \
                " with ACSF input features."
            raise FortnetAseError(msg)

        # inquire external atomic input features
        if 'netstat/external' in netstatfile and tforces:
            msg = "Error while reading netstat file '" + fname + \
                "'. Calculation of forces is only supported for purely ACSF" + \
                " based input features."
            raise FortnetAseError(msg)


class Fortnet(FileIOCalculator):
    '''ASE file-IO calculator for Fortnet.'''

    if 'FORTNET_COMMAND' in os.environ:
        command = os.environ['FORTNET_COMMAND'] + ' > PREFIX.out'
    else:
        command = 'fnet > PREFIX.out'

    implemented_properties = ('energy', 'forces')
    discard_results_on_any_change = True


    def __init__(self, label='fortnet', atoms=None, restart='fortnet.hdf5',
                 **kwargs):
        '''Initializes a Fortnet file-IO calculator object.

        Args:

            label (str): prefix used for the main output file <label>.out
                (default: fortnet)
            atoms (list): list of ASE atoms objects, containing the geometries
                of the prediction dataset to be used
            binary (str): path to executable Fortnet binary (default: ./fnet)
            netstat (str): path to the netstat file to initialize network from
            finitediffdelta (float): coordinate shift to calculate central
                finite differences (unit: Angstrom)
            forces (bool): true, if forces shall be calculated by Fortnet

        '''

        self.atoms = None
        self.atoms_input = None
        self.do_forces = False
        self.outfilename = 'fortnet.out'

        # determine coordinate shift for finite differences
        if 'finitediffdelta' in kwargs:
            # expect coordinate shift in ASE units, i.e. Angstrom
            self._finitediffdelta = kwargs['finitediffdelta'] * AA_BOHR
        else:
            # runs analytical force calculation if self.do_forces is true
            self._finitediffdelta = None

        if os.path.isfile(restart):
            self._netstat = restart
        else:
            msg = "Specified Fortnet netstat file at '" + \
                os.path.join(os.getcwd(), restart) + "' is not present."
            raise FortnetAseError(msg)

        FileIOCalculator.__init__(self, restart=restart, label=label,
                                  atoms=atoms, **kwargs)


    def _get_fortnet_input(self):
        '''Generates a suitable Python dictionary for a prediction run.

        Returns:

            inp (dict): Fortnet compatible input as nested dictionaries

        '''

        inp = get_fortnet_input(self._netstat, self._finitediffdelta,
                                self.do_forces)

        return inp


    def check_state(self, atoms):
        '''Checks the current state of the FileIOCalculator.'''

        system_changes = FileIOCalculator.check_state(self, atoms)
        # Ignore unit cell for molecules:
        if not atoms.pbc.any() and 'cell' in system_changes:
            system_changes.remove('cell')

        return system_changes


    def write_input(self, atoms, properties=None, system_changes=None):
        '''Generates and writes a Fortnet compatible HSD input to disk.'''

        if properties is not None:
            if 'forces' in properties:
                self.do_forces = True

        _check_bpnn_configuration(self._netstat, self.do_forces)

        FileIOCalculator.write_input(self, atoms, properties, system_changes)

        # generate HSD input and dump to disk
        inp = self._get_fortnet_input()
        hsd_to_file(inp, 'fortnet_in.hsd')

        # generate minimal dataset and dump to disk
        if atoms is not None and not isinstance(atoms, list):
            fnetdata = Fnetdata(atoms=[atoms])
        else:
            fnetdata = Fnetdata(atoms=atoms)
        fnetdata.dump(FNETDATA)

        # self.atoms is none until results are read out,
        # then it is set to the ones at writing input
        self.atoms_input = atoms
        self.atoms = None


    def read_results(self):
        '''All results are read from the fnetout.hdf5 file.
           It will be destroyed after it is read to avoid
           reading it once again after some runtime error.
        '''

        self.atoms = self.atoms_input

        # read energy from fnetdata.hdf5 output
        self.results['energy'] = read_energy()

        # read forces from fnetdata.hdf5 output
        if self.do_forces:
            self.results['forces'] = read_forces(self.do_forces)

        os.remove(os.path.join(self.directory, FNETOUT))


def read_energy():
    '''Read energy from fnetout.hdf5 output.'''

    fnetout = Fnetout(FNETOUT)
    # assume a single system-wide energy prediction
    # further assume that the target unit was a.u.
    energy = fnetout.globalpredictions[0, 0] * HARTREE_EV

    return energy


def read_forces(tforces):
    '''Read forces from fnetout.hdf5 output.

    Args:

        tforces (bool): true, if forces are expected to be present

    '''

    fnetout = Fnetout(FNETOUT)

    if tforces and not fnetout.tforces:
        msg = 'Error while reading ' + FNETOUT + ' file. Forces ' + \
            'requested by the calculator but not present in output.'
        raise FortnetAseError(msg)

    if tforces:
        # assume a single datapoint and training target
        # further assume that the target unit was a.u.
        forces = fnetout.forces[0][0] * HARTREE_EV / BOHR_AA
    else:
        forces = None

    return forces

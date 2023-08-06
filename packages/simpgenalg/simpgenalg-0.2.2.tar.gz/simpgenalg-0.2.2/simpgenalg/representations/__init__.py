#__name__ = 'simpgenalg.representations'

from .vector import vectorRepresentation
from .binary import binaryRepresentation
from .proportional import proportionalRepresentation

representations_dct = {'vector':vectorRepresentation,\
                       'binary':binaryRepresentation,\
                       'proportional':proportionalRepresentation}

import attr
from attr.validators import instance_of
import numpy as np
from scipy import constants
from hgc_tpg.plotting.plot_rate import Parameters as RatePlotParameters

# Default constants used to rescale rate values
nbunches = 2808.
c_light = constants.c*1.e-3 # km/s
lhc_length = 27. # km
rate2kHz = nbunches*c_light/lhc_length*1.e-3

@attr.s
class RateParameters(object):
    input_file = attr.ib(validator=instance_of(str), default='ntuple.root')
    input_tree = attr.ib(validator=instance_of(str), default='hgcalTriggerNtuplizer/HGCalTriggerNtuple')
    thresholds = attr.ib(validator=instance_of(np.ndarray), default=np.arange(5., 100., 1.))
    scale_factor = attr.ib(validator=instance_of(float), default=rate2kHz)
    plot_params = attr.ib(validator=instance_of(RatePlotParameters), default=RatePlotParameters())

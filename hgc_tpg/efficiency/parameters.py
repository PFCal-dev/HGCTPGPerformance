import attr
from attr.validators import instance_of
from hgc_tpg.plotting.plot_efficiency import Parameters as EfficiencyPlotParameters


@attr.s
class TurnonParameters(object):
    input_file = attr.ib(validator=instance_of(str), default='ntuple.root')
    input_tree = attr.ib(validator=instance_of(str), default='hgcalTriggerNtuplizer/HGCalTriggerNtuple')
    threshold = attr.ib(validator=instance_of(float), default=30.)
    plot_params = attr.ib(validator=instance_of(EfficiencyPlotParameters), default=EfficiencyPlotParameters())

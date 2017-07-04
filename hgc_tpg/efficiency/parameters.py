import attr
from attr.validators import instance_of
from hgc_tpg.plotting.plot_efficiency import Parameters as EfficiencyPlotParameters
from hgc_tpg.utilities.tree import GenSelection, PositionMatching


@attr.s
class TurnonParameters(object):
    input_file = attr.ib(validator=instance_of(str), default='ntuple.root')
    input_tree = attr.ib(validator=instance_of(str), default='hgcalTriggerNtuplizer/HGCalTriggerNtuple')
    reference_pt = attr.ib(validator=instance_of(str), default='gen_pt')
    l1_pt = attr.ib(validator=instance_of(str), default='l1_pt')
    reference_selection = attr.ib(default=GenSelection())
    matching = attr.ib(default=PositionMatching())
    threshold = attr.ib(validator=instance_of(float), default=30.)
    plot_params = attr.ib(validator=instance_of(EfficiencyPlotParameters), default=EfficiencyPlotParameters())


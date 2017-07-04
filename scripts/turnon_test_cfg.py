import ROOT
from hgc_tpg.efficiency.parameters import TurnonParameters
from hgc_tpg.plotting.plot_efficiency import Parameters as EfficiencyPlotParameters
from hgc_tpg.utilities.tree import GenSelection, PositionMatching
from hgc_tpg.utilities.matching import match_etaphi


# Plotting parameters and style
plot_params = EfficiencyPlotParameters(
                name='turnon_Zee',
                xmin=10.,
                xmax=60.,
                ymin=0.,
                ymax=1.1,
                xtitle='p_{T}^{gen} [GeV]',
                ytitle='Efficiency',
                efficiency_markerstyle='circle',
                efficiency_markersize=1.2,
                efficiency_markercolor=ROOT.kBlack,
                legend_x1=0.70,
                legend_y1=0.76,
                legend_x2=0.70,
                legend_y2=0.76,
                legendtext_size=0.035,
                legendtext_font=42,
                )

# Variables names and cuts used to select reference objects
selection = GenSelection(
                gen_pt='gen_pt',
                gen_eta='gen_eta',
                gen_id='gen_id',
                gen_status='gen_status',
                eta_min=1.7,
                eta_max=2.8,
                pt_min=15.,
                id=11,
                status=1
                )

# Variables names and function used for L1-gen matching
matching = PositionMatching(
                ref_position=('gen_eta', 'gen_phi'),
                l1_position=('cl3d_eta', 'cl3d_phi'),
                l1_pt='cl3d_pt' ,
                matching_function=match_etaphi
                )

# General turnon parameters
parameters = TurnonParameters(
                input_file='/afs/cern.ch/user/j/jsauvan/workspace/public/HGCAL/eg_trees/RelValZEE_14/ZEE_PU140_0/ntuple_*.root',
                input_tree='hgcalTriggerNtuplizer/HGCalTriggerNtuple',
                reference_pt='gen_pt',
                l1_pt='cl3d_pt',
                reference_selection=selection,
                matching=matching,
                threshold=30.,
                plot_params=plot_params
                )


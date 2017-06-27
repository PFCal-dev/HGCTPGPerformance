import ROOT
from hgc_tpg.efficiency.parameters import TurnonParameters
from hgc_tpg.plotting.plot_efficiency import Parameters as EfficiencyPlotParameters


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

# General turnon parameters
parameters = TurnonParameters(
                input_file='/afs/cern.ch/user/j/jsauvan/workspace/public/HGCAL/eg_trees/RelValZEE_14/ZEE_PU140_0/ntuple_*.root',
                input_tree='hgcalTriggerNtuplizer/HGCalTriggerNtuple',
                threshold=30.,
                plot_params=plot_params
                )


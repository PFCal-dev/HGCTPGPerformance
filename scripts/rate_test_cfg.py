import ROOT
import numpy as np
from hgc_tpg.rate.parameters import RateParameters, rate2kHz
from hgc_tpg.plotting.plot_rate import Parameters as RatePlotParameters


# Plotting parameters and style
plot_params = RatePlotParameters(
        name='rate_200PU',
        xmin=5.,
        xmax=100.,
        ymin=1.,
        ymax=40000.,
        xtitle='Threshold [GeV]',
        ytitle='Rate [kHz]',
        fill_color=ROOT.kBlack,
        fill_style='solid'
        )

# General rate parameters
parameters = RateParameters(
                input_file='/home/llr/cms/sauvan/DATA/HGCAL/Ntuples/rate_study/SingleNeutrino/NuGun_PU200_L1T/170628/ntuple*.root',
                input_tree='hgcalTriggerNtuplizer/HGCalTriggerNtuple',
                thresholds=np.arange(5.,100., 1.),
                scale_factor=rate2kHz,
                plot_params=plot_params
                )



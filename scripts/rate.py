#! /usr/bin/env python
import numpy as np
import ROOT
from rootpy.plotting.style import set_style
from hgc_tpg.utilities.tree import read
from hgc_tpg.rate.rate import rate

from hgc_tpg.plotting.styles import style_rate
from hgc_tpg.plotting import plot_rate

thresholds = np.arange(5., 100., 1.)

nbunches = 2808.
c_light = 299792.458
lhc_length = 27.

# Plotting parameters and style
set_style(style_rate)
params = plot_rate.Parameters(
        name='rate',
        xmin=5.,
        xmax=100.,
        ymin=1.,
        ymax=40000.,
        xtitle='Threshold [GeV]',
        ytitle='Rate [kHz]',
        fill_color=ROOT.kBlack,
        fill_style='solid'
        )

def main(input_file, output_file):
    l1_data = read(input_file, 'hgcalTriggerNtuplizer/HGCalTriggerNtuple')
    output = ROOT.TFile.Open(output_file, 'recreate')
    rates = rate(l1_data['cl3d_pt'], thresholds, total_events=l1_data.shape[0])
    rates.Scale(nbunches*c_light/lhc_length*1.e-3)
    plot_rate.plot(params, rates)
    output = ROOT.TFile.Open(output_file, 'recreate')
    rates.Write()
    output.Close()

if __name__=='__main__':
    import sys
    import optparse

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--input', dest='input_file', help='Input file')
    parser.add_option('--output', dest='output_file', help='Output file')
    (opt, args) = parser.parse_args()
    if not opt.input_file :
        parser.print_help()
        print 'Error: Missing input file name'
        sys.exit(1)
    if not opt.output_file :
        parser.print_help()
        print 'Error: Missing output file name'
        sys.exit(1)
    main(opt.input_file, opt.output_file)



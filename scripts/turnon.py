#! /usr/bin/env python
import numpy as np
import ROOT
from rootpy.plotting.style import set_style
from hgc_tpg.utilities.tree import read_and_match
from hgc_tpg.efficiency.efficiency import turnon

from hgc_tpg.plotting.styles import style_turnon
from hgc_tpg.plotting import plot_turnons


# Plotting parameters and style
set_style(style_turnon)
params = plot_turnons.Parameters(
        name='turnon_Zee',
        xmin=10.,
        xmax=60.,
        ymin=0.,
        ymax=1.1,
        xtitle='p_{T}^{gen} [GeV]',
        ytitle='Efficiency',
        turnon_markerstyle='circle',
        turnon_markersize=1.2,
        turnon_markercolor=ROOT.kBlack,
        legend_x1=0.70,
        legend_y1=0.76,
        legend_x2=0.70,
        legend_y2=0.76,
        legendtext_size=0.035,
        legendtext_font=42,
        )


def main(input_file, output_file):
    ref_pt, l1_pt = read_and_match(input_file, 'hgcalTriggerNtuplizer/HGCalTriggerNtuple')
    efficiency = turnon(ref_pt, l1_pt, threshold=30)
    plot_turnons.plot(params, efficiency)
    output = ROOT.TFile.Open(output_file, 'recreate')
    efficiency.Write()
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


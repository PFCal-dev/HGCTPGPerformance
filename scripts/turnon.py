#! /usr/bin/env python
import numpy as np
import ROOT
from hgc_tpg.utilities.tree import read_and_match
from hgc_tpg.efficiency.efficiency import turnon

def main(input_file, output_file):
    ref_pt, l1_pt = read_and_match(input_file, 'hgcalTriggerNtuplizer/HGCalTriggerNtuple')
    efficiency = turnon(ref_pt, l1_pt, threshold=30)
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


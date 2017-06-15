#! /usr/bin/env python
import numpy as np
import ROOT
from hgc_tpg.utilities.matching import match_etaphi
from hgc_tpg.efficiency.efficiency import turnon

def main(input_file, output_file):
    input_tree = ROOT.TChain('hgcalTriggerNtuplizer/HGCalTriggerNtuple')
    input_tree.Add(input_file)
    nentries = input_tree.GetEntries()
    ref_pt = []
    l1_pt = []
    for entry in xrange(nentries):
        if nentries<100 or entry%(nentries/100)==0:
            print 'Event {0}/{1}'.format(entry,nentries)
        input_tree.GetEntry(entry)
        gen_eta = np.array(input_tree.gen_eta)
        gen_phi = np.array(input_tree.gen_phi)
        gen_pt = np.array(input_tree.gen_pt)
        gen_id = np.array(input_tree.gen_id)
        gen_status = np.array(input_tree.gen_status)
        cl3d_eta = np.array(input_tree.cl3d_eta)
        cl3d_phi = np.array(input_tree.cl3d_phi)
        cl3d_pt = np.array(input_tree.cl3d_pt)
        gen_selection = np.logical_and.reduce((np.abs(gen_eta)>1.7, np.abs(gen_eta)<2.8, gen_pt>15, np.abs(gen_id)==11, gen_status==1))
        if np.count_nonzero(gen_selection)>0:
            gen_etaphi = np.column_stack((gen_eta,gen_phi))[gen_selection]
            matched = match_etaphi(gen_etaphi, np.column_stack((cl3d_eta,cl3d_phi)), cl3d_pt)
            for gen,l1 in matched.items():
                ref_pt.append(gen_pt[gen_selection][gen])
                l1_pt.append(cl3d_pt[l1])
    matched_data = np.column_stack((ref_pt,l1_pt))
    efficiency = turnon(np.array(ref_pt), np.array(l1_pt), threshold=30)
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


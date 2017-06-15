import numpy as np
import ROOT
from hgc_tpg.utilities.matching import match_etaphi

# FIXME: temporary function
# Need better and more generic way to read the trees
def read_and_match(input_file, tree_name):
    input_tree = ROOT.TChain(tree_name)
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
    return np.array(ref_pt), np.array(l1_pt)

import attr
from attr.validators import instance_of
import numpy as np
import ROOT
from root_numpy import root2array
from hgc_tpg.utilities.matching import match_etaphi


@attr.s
class Branches(object):
    l1_pt = attr.ib(validator=instance_of(str), default='cl3d_pt')
    l1_eta = attr.ib(validator=instance_of(str), default='cl3d_eta')
    l1_phi = attr.ib(validator=instance_of(str), default='cl3d_phi')
    ref_pt = attr.ib(validator=instance_of(str), default='gen_pt')
    ref_eta = attr.ib(validator=instance_of(str), default='gen_eta')
    ref_phi = attr.ib(validator=instance_of(str), default='gen_phi')
    ref_id = attr.ib(validator=instance_of(str), default='gen_id')
    ref_status = attr.ib(validator=instance_of(str), default='gen_status')

    def l1(self):
        return [self.l1_pt, self.l1_eta, self.l1_phi]

    def ref(self):
        return [self.ref_pt, self.ref_eta, self.ref_phi, self.ref_id, self.ref_status]


@attr.s
class Selection(object):
    eta_min = attr.ib(validator=instance_of(float), default=1.7)
    eta_max = attr.ib(validator=instance_of(float), default=2.8)
    pt_min = attr.ib(validator=instance_of(float), default=15.)
    gen_id = attr.ib(validator=instance_of(int), default=11)
    gen_status = attr.ib(validator=instance_of(int), default=1)


def read_and_match(input_file, tree_name, branches=None, selection=None):
    if selection==None:
        selection = Selection()
    if branches==None:
        branches = Branches()
    branch_names = branches.l1() + branches.ref()
    events = root2array(input_file, tree_name, branches=branch_names)
    selected_ref_pt = []
    matched_l1_pt = []
    for event in events:
        ref_eta = event[branches.ref_eta]
        ref_phi = event[branches.ref_phi]
        ref_pt = event[branches.ref_pt]
        ref_id = event[branches.ref_id]
        ref_status = event[branches.ref_status]
        l1_eta = event[branches.l1_eta]
        l1_phi = event[branches.l1_phi]
        l1_pt = event[branches.l1_pt]
        ref_selection = np.logical_and.reduce((
            np.abs(ref_eta)>selection.eta_min,
            np.abs(ref_eta)<selection.eta_max,
            ref_pt>selection.pt_min,
            np.abs(ref_id)==selection.gen_id,
            ref_status==selection.gen_status
            ))
        if np.count_nonzero(ref_selection)>0:
            ref_etaphi = np.column_stack((ref_eta,ref_phi))[ref_selection]
            matched = match_etaphi(ref_etaphi, np.column_stack((l1_eta,l1_phi)), l1_pt)
            for ref,l1 in matched.items():
                selected_ref_pt.append(ref_pt[ref_selection][ref])
                matched_l1_pt.append(l1_pt[l1])
    return np.array(selected_ref_pt), np.array(matched_l1_pt)


def read(input_file, tree_name, branches=None):
    if branches==None:
        branches = Branches()
    branch_names = branches.l1()
    return root2array(input_file, tree_name, branches=branch_names)

import attr
from attr.validators import instance_of
import numpy as np
import ROOT
from root_numpy import root2array
from hgc_tpg.utilities.matching import match_etaphi


@attr.s
class GenSelection(object):
    # variable names
    gen_pt = attr.ib(validator=instance_of(str), default='gen_pt')
    gen_eta = attr.ib(validator=instance_of(str), default='gen_eta')
    gen_id = attr.ib(validator=instance_of(str), default='gen_id')
    gen_status = attr.ib(validator=instance_of(str), default='gen_status')
    # Cuts
    eta_min = attr.ib(validator=instance_of(float), default=1.7)
    eta_max = attr.ib(validator=instance_of(float), default=2.8)
    pt_min = attr.ib(validator=instance_of(float), default=15.)
    id = attr.ib(validator=instance_of(int), default=11)
    status = attr.ib(validator=instance_of(int), default=1)

    def branch_list(self):
        return [self.gen_pt, self.gen_eta, self.gen_id, self.gen_status]

    def __call__(self, event):
        gen_eta = event[self.gen_eta]
        gen_pt = event[self.gen_pt]
        gen_id = event[self.gen_id]
        gen_status = event[self.gen_status]
        return np.logical_and.reduce((
            np.abs(gen_eta)>self.eta_min,
            np.abs(gen_eta)<self.eta_max,
            gen_pt>self.pt_min,
            np.abs(gen_id)==self.id,
            gen_status==self.status
            ))

@attr.s
class PositionMatching(object):
    ref_position = attr.ib(validator=instance_of(tuple), default=('gen_eta', 'gen_phi'))
    l1_position = attr.ib(validator=instance_of(tuple), default=('cl3d_eta', 'cl3d_phi'))
    l1_pt = attr.ib(validator=instance_of(str), default='cl3d_pt')
    matching_function = attr.ib(default=match_etaphi)

    def branch_list(self):
        return list(self.ref_position) + list(self.l1_position) + [self.l1_pt]

    def __call__(self, event, ref_selection):
        ref_pos =  np.column_stack((event[name] for name in self.ref_position))[ref_selection]
        l1_pos =  np.column_stack((event[name] for name in self.l1_position))
        l1_pt = event[self.l1_pt]
        return self.matching_function(ref_pos, l1_pos, l1_pt)


def read_and_match(input_file, tree_name,
        ref_variables=['gen_pt'],
        l1_variables=['cl3d_pt'],
        selection=GenSelection(),
        matching=PositionMatching()
        ):
    branch_names = list(set(ref_variables + l1_variables + selection.branch_list() + matching.branch_list()))
    events = root2array(input_file, tree_name, branches=branch_names)
    # prepare dictionary storing the output variables of matched objects
    ref_output = {key:[] for key in ref_variables}
    l1_output = {key:[] for key in l1_variables}
    for event in events:
        # Retrieve indices of selected reference objects
        selected = selection(event)
        if np.count_nonzero(selected)>0:
            # matched L1 objects to reference objects
            matched = matching(event, selected)
            for ref,l1 in matched.items():
                for branch,values in ref_output.items():
                    values.append(event[branch][selected][ref])
                for branch,values in l1_output.items():
                    values.append(event[branch][l1])
    nvars = len(ref_output)+len(l1_output)
    output = np.core.records.fromarrays(
            np.array([ref_output[name] for name in ref_variables]+[l1_output[name] for name in l1_variables]), 
            names=ref_variables+l1_variables,
            formats=['f4']*nvars
            )
    return output


def read(input_file, tree_name, variables=['cl3d_pt', 'cl3d_eta', 'cl3d_phi']):
    return root2array(input_file, tree_name, branches=variables)

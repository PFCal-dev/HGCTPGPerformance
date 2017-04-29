# test of a python analyzer that produce response plots #
# Luca Mastrolorenzo - 25-04-2017 #
# The class provide a function that create an output file and store pt,eta,phi response #

import ROOT
import hgc_tpg.utilities.functions as f
import numpy as np

class resolution :
    
    def __init__(self, input_file, output_file, conf) :
        self.inputNtuple = ROOT.TFile.Open(input_file)
        self.outputFile = output_file
        self.chain = self.inputNtuple.Get("hgcalTriggerNtuplizer/HGCalTriggerNtuple")
        self.cfg = conf

    # function that produce the response plot - looking to dR-match between gen-C3d #
    # keep the highest-pt C3d in the cone as L1-candidate #
    def plotResponse(self) :

        # definition of the output file and histogram to store in it
        output = ROOT.TFile(self.outputFile+".root","RECREATE")
        h_resoPt = ROOT.TH1D("resoPt","Pt response",100, 0, 2)
        h_resoEta = ROOT.TH1D("resoEta","Eta response",100, -0.15, 0.15);
        h_resoPhi = ROOT.TH1D("resoPhi","Phi response",100, -0.15, 0.15);
        h_L1PtvsTrue2D = ROOT.TH2D("h_L1PtvsTrue2D","h_L1PtvsTrue2D",200, 0, 200, 201, -1, 200);

        self.chain.Print()
    
        # loop over the ttree ntries
        for ientry, entry in enumerate(self.chain):
            gen_pt_ = np.array(entry.gen_pt) # for vectors
            gen_eta_ = np.array(entry.gen_eta)
            gen_phi_ = np.array(entry.gen_phi)
            gen_energy_ = np.array(entry.gen_energy)
            gen_status_ = np.array(entry.gen_status)
            gen_id_ = np.array(entry.gen_id)        
            c3d_pt_ = np.array(entry.cl3d_pt)
            c3d_eta_ = np.array(entry.cl3d_eta)
            c3d_phi_ = np.array(entry.cl3d_phi)
            c3d_energy_ = np.array(entry.cl3d_energy)
            
            # select the good C3d
            goodC3d_idx = []
            for i_c3d in range(len(c3d_pt_)) :
                if ( abs( c3d_eta_[i_c3d] ) > self.cfg.minEta_C3d and  abs( c3d_eta_[i_c3d] ) < self.cfg.maxEta_C3d 
                     and c3d_pt_[i_c3d] > self.cfg.minPt_C3d ) :
                    goodC3d_idx.append(i_c3d)
                    
            # loop over the gen particle and apply basic selection at MC-truth level
            for i_gen in range(len(gen_pt_)) :
                if ( abs( gen_eta_[i_gen] ) > self.cfg.minEta_gen and abs( gen_eta_[i_gen] ) < self.cfg.maxEta_gen 
                     and gen_pt_[i_gen] > self.cfg.minPt_gen and abs( gen_id_[i_gen] ) == self.cfg.particle_type 
                     and gen_status_[i_gen] == self.cfg.particle_status ) :
                    
                    hasMatched = False
                    pt_cand = -1.
                    eta_cand = -100.
                    phi_cand = -100.

                    # loop over the good 3D-cluster
                    for i in range(len(goodC3d_idx)) :
                         i_c3d = goodC3d_idx[i]   
                         dR = f.deltaR( gen_eta_[i_gen], c3d_eta_[i_c3d], gen_phi_[i_gen], c3d_phi_[i_c3d])                
                         if dR<0.5 :
                             hasMatched = True
                             if c3d_pt_[i_c3d] > pt_cand :
                                 pt_cand = c3d_pt_[i_c3d]
                                 eta_cand = c3d_eta_[i_c3d]
                                 phi_cand = c3d_phi_[i_c3d]                                                      
                                 
                    # fill the response histograms    
                    if hasMatched : 
                        print gen_pt_[i_gen], pt_cand
                        h_L1PtvsTrue2D.Fill(gen_pt_[i_gen], pt_cand)
                    elif not hasMatched :
                        print gen_pt_[i_gen], -1
                        h_L1PtvsTrue2D.Fill(gen_pt_[i_gen], -1)
                    
                    h_resoPt.Fill( pt_cand / gen_pt_[i_gen] )
                    h_resoEta.Fill( eta_cand - gen_eta_[i_gen] )
                    h_resoPhi.Fill( phi_cand - gen_phi_[i_gen] )

        # write histograms into output file
        h_resoPt.Write()
        h_resoEta.Write()
        h_resoPhi.Write()
        h_L1PtvsTrue2D.Write()

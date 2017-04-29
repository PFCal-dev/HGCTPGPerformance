

class parameters : 
    
    def __init__(self) :

        #define acceptance of the reconstructed clusters
        self.minEta_C3d = float(1.47)
        self.maxEta_C3d = float(3.0)
        self.minPt_C3d = float(7.0) # in GeV
        
        #define acceptance, type and status of the gen-particle
        self.minEta_gen = float(1.47)
        self.maxEta_gen = float(3.0)
        self.minPt_gen = float(7.0) # in GeV
        self.particle_type = int(11)
        self.particle_status = int(1)
        

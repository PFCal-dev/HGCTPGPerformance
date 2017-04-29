import math as m 

def deltaPhi( phi1, phi2) :    
    dPhi = phi1-phi2
    pi = m.acos(-1.0)
    if dPhi <= -pi : 
        dPhi += 2.0*pi
    elif dPhi > pi : 
        dPhi-=2.0*pi;           
    return dPhi
    
def deltaEta( eta1, eta2) :
    dEta = eta1-eta2
    return dEta

def deltaR( eta1, eta2, phi1, phi2) :
    dEta = deltaEta(eta1, eta2)
    dPhi = deltaPhi(phi1, phi2)
    return m.sqrt(dEta*dEta+dPhi*dPhi)

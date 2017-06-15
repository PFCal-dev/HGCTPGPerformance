import numpy as np
from rootpy.plotting import Hist, Graph
from root_numpy import fill_hist

turnon_binning_default = [-20,-10,-7,-5,-4,-3,-2,-1,0,1,2,3,4,5,7,10,15,20,30]
def turnon(ref_pt, l1_pt, threshold, bins=None):
    if bins==None:
        print 'WARNING: Turnon binning not specified. Default binning will be used:'
        bins = np.array(turnon_binning_default)+threshold
        bins = bins[bins>=0]
        print bins
    return efficiency_graph(
            np.vectorize(lambda pt:pt>threshold), # selection cut to be applied
            np.array(l1_pt), 
            np.array(ref_pt),
            bins
            )



def efficiency_graph(selection_function, selection_inputs, xs, bins=None, error=0.01):
    selection = selection_function(selection_inputs)
    if bins is None: # Automatic binning
        # Compute the number of bins such that the error on the efficiency is equal to 'error' in each bin
        # The calculation is based on binomial errors and assumes that the efficiency is flat (that the distributions of all and selected events are the same)
        k = float(np.count_nonzero(selection))
        n = float(len(selection))
        percentiles = [0.,100.]
        if k>0: 
            nbins = (error*n)**2/k / (1-k/n)
            print nbins
            # Compute the bin bounaries with the same number of events in all bins
            percentiles = np.arange(0., 100., 100./nbins)
            percentiles[-1] = 100.
        bins = np.unique(np.percentile(xs, percentiles))
    # Fill histograms of selected and all events and compute efficiency
    histo_pass = Hist(bins)
    histo_total = Hist(bins)
    fill_hist(histo_pass, xs, selection)
    fill_hist(histo_total, xs)
    efficiency = Graph()
    efficiency.Divide(histo_pass, histo_total)
    return efficiency

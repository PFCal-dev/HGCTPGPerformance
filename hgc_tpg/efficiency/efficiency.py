import numpy as np
from rootpy.plotting import Hist, Graph
from root_numpy import fill_hist

turnon_binning_default = [-30,-20,-10,-7,-5,-4,-3,-2,-1,0,1,2,3,4,5,7,10,15,20,30]
def turnon(ref_pt, l1_pt, threshold, selection_function=None, selection_inputs=None, bins=None):
    if bins==None:
        print 'WARNING: Turnon binning not specified. Default binning will be used:'
        bins = np.array(turnon_binning_default)+threshold
        bins = bins[bins>=0]
        print bins
    # If no selection only apply pt threshold
    pass_function = np.vectorize(lambda pt:pt>threshold) # pass threshold
    inputs = l1_pt
    # If additional selection (e.g. object identification)
    # combine pt threshold and selection
    if selection_function!=None:
        pass_function = lambda (pt,sel_inputs):np.logical_and(\
                np.vectorize(lambda x:x>threshold)(pt),\
                selection_function(sel_inputs)\
                )
        inputs = (l1_pt, selection_inputs)
    return efficiency_graph(
            selection_function=pass_function,
            selection_inputs=inputs,
            xs=ref_pt,
            bins=bins
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

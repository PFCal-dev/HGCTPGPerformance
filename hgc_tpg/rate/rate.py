from copy import deepcopy as copy
import numpy as np
from rootpy.plotting import Hist, Graph
from root_numpy import fill_hist, array2hist


def pass_threshold(et, thresholds):
    # Make sure the et thresholds are sorted
    thresholds_sorted = np.sort(np.unique(thresholds))
    pass_thresholds = np.zeros(len(thresholds_sorted))
    for event in et:
        if len(event)==0: continue
        et_max = np.max(event)
        pass_threshold = thresholds_sorted < et_max
        pass_thresholds += pass_threshold
    return np.column_stack((thresholds_sorted, pass_thresholds))


def rate(et, thresholds, total_events):
    pass_thresholds = pass_threshold(et, thresholds)
    # fill pass and total numbers of events
    bins = (pass_thresholds[:-1,0] + pass_thresholds[1:,0])/2.
    bins = np.append([-bins[0]+2.*pass_thresholds[0,0]], bins)
    bins = np.append(bins, [2.*pass_thresholds[-1,0] - bins[-1]])
    histo_pass = Hist(bins)
    histo_total = Hist(bins)
    for b,n in zip(histo_pass[1:-1], pass_thresholds[:,1]):
        b.value = n
        b.error = np.sqrt(n)
    for b in histo_total[1:-1]:
        b.value = total_events
        b.error = np.sqrt(total_events)
    rates = Graph()
    rates.Divide(histo_pass, histo_total)
    return rates



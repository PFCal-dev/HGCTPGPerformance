#! /usr/bin/env python
import numpy as np
import ROOT
from rootpy.plotting.style import set_style
from hgc_tpg.utilities.tree import read
from hgc_tpg.rate.rate import rate

from hgc_tpg.plotting.styles import style_rate
from hgc_tpg.plotting import plot_rate 


def main(parameters):
    set_style(style_rate)
    l1_data = read(parameters.input_file, parameters.input_tree)
    rates = rate(l1_data['cl3d_pt'], parameters.thresholds, total_events=l1_data.shape[0])
    rates.Scale(parameters.scale_factor)
    plot_rate.plot(parameters.plot_params, rates)

if __name__=='__main__':
    import sys
    import os
    import optparse
    import importlib
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--cfg', dest='parameter_file', help='Python file containing the definition of parameters ', default='pars.py')
    (opt, args) = parser.parse_args()
    current_dir = os.getcwd();
    sys.path.append(current_dir)
    # Remove the extension of the python file before module loading
    if opt.parameter_file[-3:]=='.py': opt.parameter_file = opt.parameter_file[:-3]
    parameters = importlib.import_module(opt.parameter_file).parameters
    main(parameters)



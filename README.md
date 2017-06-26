# HGCAL TPG performance utilities
This is a Python package used to produce various performance plots for the HGCAL trigger prmitive generation studies.

## Installation
First clone the package:
```bash
git clone git@github.com:PFCal-dev/HGCTPGPerformance.git HGCTPGPerformance
```

This package depends on several python packages, listed in `requirements.txt`:
* `attrs`
* `scipy`
* `numpy`
* `pandas`
* `root-numpy`
* `rootpy`

In general it is better to encapsulate these packages inside a virtual environment (using for instance `virtualenvwrapper`).

On SLC6 lxplus, the default versions of python and ROOT are antique, so a couple of setup commands are needed to have a working environment. The following script should be sourced each time to setup Python, ROOT, and the virtual environment (**outside a CMSSW environment**).
```bash
source init_env_lxplus.sh
```
The first time it is called, it will install everything so it might take some time (in particular with the installation of root-numpy). Then, once everything is already installed it will just activate the virtual environment.

If it worked correctly the terminal prompt should be prefixed with `(hgc_tpg)`, meaning that you are inside the virtual environment. To leave the virtual environment, just type `deactivate`.

On machines other than lxplus, the same thing can be done, just the Python and ROOT setup at the beginning of the script would need to be modified.

## Usage
The package code is located in `hgc_tpg`. It is divided in sub-directories corresponding to different performance studies:
* `resolution`: study of energy and position resolutions
* `efficiency`: study of efficiencies (including turn-ons)
* `rate`: study of trigger rates
* `bandwidth`: study of the bandwidth between layers of the TPG system
* `utilities`: general utility functions
* `plotting`: plotting functions and style definitions

This code is used from scripts located in the `scripts` directory. The scripts currently available are:
* `runResolution.py`: energy and position resolution plots
* `turnon.py`: turnon plot
* `rate.py`: rate plot



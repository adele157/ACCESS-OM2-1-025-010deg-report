#!/usr/bin/env python

# Centralised code to set model and experiment names.

# This is just an initial stab at it. More functionality is planned:
# https://github.com/OceansAus/ACCESS-OM2-1-025-010deg-report/issues/6

# load this with
#     import sys, os
#     sys.path.append(os.path.join(os.getcwd(), '..'))  # so we can import ../exptdata
#     import exptdata
# in figures/subdir/your_notebook.ipynb

from collections import OrderedDict
import os

basedir = '/g/data3/hh5/tmp/cosima/'

# Model data sources. 
# More experiments (or variables each experiment) can be added here if needed.
# locals().update(exptdata.exptdict['1deg']) will define all variables for the '1deg' experiment (dangerous!).
# exptdir = exptdata.expdict[expkey]['exptdir'] etc is safer.
# desc is a short descriptor for use in figure titles.
# Uses OrderedDict so that iteration on exptdict will be in this order.
exptdict = OrderedDict([
    ('1deg',   {'model':'access-om2',     'expt':'1deg_jra55_ryf8485_kds50_may',    'desc': 'ACCESS-OM2 (1 degree), RYF8485 forcing',        'filesPerYear': 1}),
    ('025deg', {'model':'access-om2-025', 'expt':'025deg_jra55v13_ryf8485_spinup_A','desc': 'ACCESS-OM2-025 (0.25 degree), RYF8485 forcing', 'filesPerYear': 4}),
    ('01deg',  {'model':'access-om2-01',  'expt':'01deg_jra55v13_ryf8485_spinup6',  'desc': 'ACCESS-OM2-01 (0.1 degree), RYF8485 forcing',   'filesPerYear': 12})
])

# Now add expdirs programmatically where they don't already exist.
# This allows expdir to be overridden by specifying it above if needed.
for k in exptdict.keys():
    if not('exptdir' in exptdict[k]):
        exptdict[k]['exptdir'] = os.path.join(os.path.join(
            basedir, 
            exptdict[k]['model']),
            exptdict[k]['expt' ])


# Lists of models, experiments dirs and descriptors in consistent order

models    = [exptdict[k]['model']   for k in exptdict.keys()]

expts     = [exptdict[k]['expt']    for k in exptdict.keys()]

exptdirs  = [exptdict[k]['exptdir'] for k in exptdict.keys()]

descs     = [exptdict[k]['desc']    for k in exptdict.keys()]


def model_expt_exptdir_desc(keyname):
    """
    Return (model, expt, exptdir, desc) strings for keyname in exptdict.keys()
    
    Examples:
    
    (model, expt, exptdir, desc) = model_expt_exptdir_desc('1deg')
    
    for k in exptdict.keys():
        (model, expt, exptdir, desc) = model_expt_exptdir_desc(k)
    
    """
    return (exptdict[keyname]['model'],
            exptdict[keyname]['expt'],
            exptdict[keyname]['exptdir'],
            exptdict[keyname]['desc'])

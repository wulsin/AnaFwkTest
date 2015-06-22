#!/usr/bin/env python


# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *

# specify which config file to pass to cmsRun
config_file = "dibosonConfig_cfg.py"

# choose luminosity used for MC normalization
intLumi = 19000

# create list of datasets to process
datasets = [
#    'JetHt2012BCD_Skim',  
    'RSGravitonZZ2000',  
    'QCD1800',  
]

InputCondorArguments = {}


labels['JetHt2012BCD_Skim'] = "JetHt 2012BCD"  
types ['JetHt2012BCD_Skim'] = "data"  

labels['RSGravitonZZ2000'] = "RS G #rightarrow ZZ (M = 2 TeV)"  
types ['RSGravitonZZ2000'] = "signalMC"  
colors['RSGravitonZZ2000'] = 600  

labels['QCD1800'] = "QCD (p_{T}>1800)"  
types ['QCD1800'] = "bgMC"  
colors['QCD1800'] = 791  





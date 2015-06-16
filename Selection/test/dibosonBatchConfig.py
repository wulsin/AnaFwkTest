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
    'JetHt2012BCD_Skim',  
]

InputCondorArguments = {}


labels['JetHt2012BCD_Skim'] = "JetHt 2012BCD"  
types ['JetHt2012BCD_Skim'] = "data"  





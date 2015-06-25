#!/usr/bin/env python

# Creates a list of all files in DAS for the given datasets.  
# Remember before running this script to execute:  voms-proxy-init -voms cms 

import os

datasets = ['/HT/biliu-Run2012A-22Jan2013-SubjetFilter-v1-c0c59fd273be4482a26f67f0b1acaccb/USER', 
            '/JetHT/biliu-Run2012B-22Jan2013-SubjetFilter-v1-c0c59fd273be4482a26f67f0b1acaccb/USER', 
            '/JetHT/biliu-Run2012C-22Jan2013-SubjetFilter-v1-c0c59fd273be4482a26f67f0b1acaccb/USER', 
            '/JetHT/biliu-Run2012D-22Jan2013-SubjetFilter-v1-c0c59fd273be4482a26f67f0b1acaccb/USER',
            ]

cmd = 'das_client.py --limit 0 --query="file instance=prod/phys03 dataset='  # remember to add closing "
myfiles = ""
for i in range(0, len(datasets)):
    myfiles += os.popen(cmd + datasets[i] + '"').read()  # use popen instead of command-line redirect to log file, because sometimes the python script continues before the das_client query has finished
    print ".", 


listname = "AAAFileListData"
outfile = open(listname, 'w') 
outfile.write(myfiles)  
outfile.close()  

num = os.popen('cat ' + listname + ' | wc ').read().split()[0]  

print "Wrote", num, "files to", listname  




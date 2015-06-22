#!/usr/bin/env python
intLumi = 19800

###################
# 'color' options #
###################
## 'black'
## 'red'  
## 'green'
## 'purple'
## 'blue'  
## 'yellow'
## default: cycle through list


####################
# 'marker' options #
####################
## 'circle'
## 'square'
## 'triangle'
## default: 'circle'

####################
#  'fill' options  #
####################
## 'solid'
## 'hollow'
## default: 'solid'

 
input_sources = [
    { 'condor_dir' : '20150618_SigVsBkgd', 
      'dataset' : 'histQCD',
      'channel' : 'SkimChannel',
      'color'   : 'blue', 
      'legend_entry' : 'QCD (p_{T}>1800)',
    },
    { 'condor_dir' : '20150618_SigVsBkgd',  
      'dataset' : 'histRSGraviton2000',
      'channel' : 'SkimChannel',
      'legend_entry' : 'RS G #rightarrow ZZ (M = 2 TeV)',
    },
]

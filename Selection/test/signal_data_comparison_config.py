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
    { 'condor_dir' : 'JUNE18_DibosonComparisonPlots',
      'dataset' : 'JetHt2012Partial',
      'channel' : 'SkimChannel',
      'legend_entry' : 'data',
    },
    { 'condor_dir' : 'JUNE18_DibosonComparisonPlots',
      'dataset' : 'histRSGraviton2000',
      'channel' : 'SkimChannel',
      'legend_entry' : 'RS G #rightarrow ZZ (M = 2 TeV)',
    },
]

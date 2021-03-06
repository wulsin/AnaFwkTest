import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# input source when running interactively
# ---------------------------------------
# argument can be a ROOT file, directory, or dataset name*
# *registered dataset names are listed in 'datasets' in:
#    https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Configuration/python/configurationOptions.py

# sample direcotory
# From /JetHT/Run2012D-22Jan2013-v1/AOD dataset:  
#set_input(process, "/mnt/hadoop/se/store/user/kkotov/BN_JetHT_Run2012D-22Jan2013-v1_AOD_0/")


# sample ROOT file
#set_input(process, "/home/hart/subjetFilter.root")  
#set_input(process, "root://cmsxrootd.fnal.gov//store/user/ahart/JetHT/SubjetFilter-v1/150605_174426/0000/subjetFilter_new_1.root")
#set_input(process, "/data/users/bing/condor/DiBosonSkimJune15/JetHtBCD/SkimChannel/skim_0.root")  
set_input(process, "/home/wulsin/dibosonResonance/ntuples/CMSSW_5_3_28_patch1/src/AnaFwkTest/Producers/test/patTuple_PATandPF2PAT_RSGravitonToZZ_kMpl01_M-2000.root")  

# sample dataset nickname
#set_input(process, "DYToTauTau_20")
#set_input(process, "DYToMuMu_20")

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
#    input = cms.untracked.int32 (1000)
    input = cms.untracked.int32 (-1)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
collections = cms.PSet (
    basicjets       =  cms.InputTag  ('leadingFatPatJet', 'leadingFat'),
    beamspots       =  cms.InputTag  ('offlineBeamSpot',             ''),
    electrons       =  cms.InputTag  ('selectedPatElectronsPFlow',   ''),
    jets            =  cms.InputTag  ('selectedPatJetsPFlowFilter',  ''),
    mets            =  cms.InputTag  ('patMETsPFlow',                ''),
    muons           =  cms.InputTag  ('selectedPatMuonsPFlow',       ''),
    photons         =  cms.InputTag  ('selectedPatPhotons',          ''),
    primaryvertexs  =  cms.InputTag  ('offlinePrimaryVertices',      ''),
    #taus            =  cms.InputTag  ('selectedPatTaus',             ''),
    triggers        =  cms.InputTag  ('TriggerResults',              '',   'HLT'),
)

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
#variableProducers.append("AnaFwkTestEventVariableProducer")
variableProducers.append("AnaFwkTestSubjetVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from AnaFwkTest.Selection.DibosonSelections import *
from AnaFwkTest.Selection.MyProtoEventSelections import *

channels = []
channels.append(skimChannel)
channels.append(preselectionChannel)
# channels.append(lowMassChannel)
# channels.append(WWChannel)
# channels.append(WZChannel)
channels.append(ZZChannel)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from AnaFwkTest.Selection.DibosonHistogramDefinitions import *

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, channels, cms.VPSet (MyBasicJetHistograms, MyMetHistograms, BasicjetBasicjetHistograms, MyEventVarHistograms), collections, variableProducers, True)

# uncomment to produce a full python configuration log file
outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")



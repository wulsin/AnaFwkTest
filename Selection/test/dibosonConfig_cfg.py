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
#set_input(process, "/home/hart/diboson/CMSSW_5_3_28_patch1/src/subjetFilter.root")  
set_input(process, "root://cmsxrootd.fnal.gov//store/user/ahart/JetHT/SubjetFilter-v1/150605_174426/0000/subjetFilter_new_1.root")

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
    beamspots       =  cms.InputTag  ('offlineBeamSpot','', 'RECO'),
    bxlumis         =  cms.InputTag  (''),
    electrons       =  cms.InputTag  ('gsfElectrons', ''),
    events          =  cms.InputTag  (''),
    genjets         =  cms.InputTag  (''),
#    jets            =  cms.InputTag  ('ak5PFJets'),
    jets            =  cms.InputTag  ('caSubjetFilterPFJets', ""),
#    basicjets       =  cms.InputTag  ('caSubjetFilterPFJets', "fat"),
    basicjets       =  cms.InputTag  ('leadingFat', "leadingFat"),
    mcparticles     =  cms.InputTag  (''),
    mets            =  cms.InputTag  ('pfMet', ''),
    muons           =  cms.InputTag  ('muons'),
    photons         =  cms.InputTag  ('photons'),
    primaryvertexs  =  cms.InputTag  ('offlinePrimaryVertices'),
    secMuons        =  cms.InputTag  ('muonsFromCosmics'),
    stops           =  cms.InputTag  (''),
    superclusters   =  cms.InputTag  (''),
    taus            =  cms.InputTag  ('hpsPFTauProducer'),
    tracks          =  cms.InputTag  ('generalTracks'),
    triggers        =  cms.InputTag  ("TriggerResults","","HLT"),   
    trigobjs        =  cms.InputTag  (''),
)

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
variableProducers.append("AnaFwkTestEventVariableProducer")
variableProducers.append("AnaFwkTestSubjetVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from AnaFwkTest.Selection.DibosonSelections import *
from AnaFwkTest.Selection.MyProtoEventSelections import *

channels = []
channels.append(skimChannel)
channels.append(preselectionChannel)
channels.append(lowMassChannel)
channels.append(WWChannel)
channels.append(WZChannel)
channels.append(ZZChannel)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from AnaFwkTest.Selection.MyProtoHistogramDefinitions import *

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, channels, cms.VPSet (MyBasicJetHistograms, MyMetHistograms, BasicjetBasicjetHistograms, MyEventVarHistograms), collections, variableProducers, False)

# uncomment to produce a full python configuration log file
outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")



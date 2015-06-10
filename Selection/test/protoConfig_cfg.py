##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##### THIS FILE IS FOR TESTING ONLY
##### DO DEVELOPMENT INSTEAD IN dibosonConfig_cfg.py  
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################




















































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
set_input(process, "/home/hart/diboson/CMSSW_5_3_28_patch1/src/subjetFilter.root")  

# sample dataset nickname
#set_input(process, "DYToTauTau_20")
#set_input(process, "DYToMuMu_20")

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
collections = cms.PSet (
    bxlumis         =  cms.InputTag  (''),
    electrons       =  cms.InputTag  ('gsfElectrons', '','RECO'),
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
    beamspots       =  cms.InputTag  ('offlineBeamSpot',          '',      'RECO'),
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

from AnaFwkTest.Selection.MyProtoEventSelections import *

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from AnaFwkTest.Selection.MyProtoHistogramDefinitions import *
from OSUT3Analysis.Configuration.histogramDefinitions import *

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, [channelWZ], cms.VPSet (histograms, MyElectronHistograms, MyBasicJetHistograms, MyMetHistograms, BasicjetBasicjetHistograms, MyEventVarHistograms), collections, variableProducers, False)

# uncomment to produce a full python configuration log file
outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")



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
 
#load JEC and standard services
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('JetMETCorrections.Configuration.CorrectedJetProducersDefault_cff')
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
process.load('JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff')
process.load('JetMETCorrections.Configuration.CorrectedJetProducersAllAlgos_cff')
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
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
 
# sample dataset nickname
#set_input(process, "DYToTauTau_20")
#set_input(process, "DYToMuMu_20")
 
#We need a secondary file to access needed collections. <double> "fixedGridRhoFastjetAll"
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cmsxrootd.fnal.gov//store/user/ahart/JetHT/SubjetFilter-v1/150605_174523/0000/subjetFilter_new_1.root'),
    secondaryFileNames = cms.untracked.vstring('root://cmsxrootd.fnal.gov//store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10001/06AEE514-5996-E211-BD63-90E6BA19A23C.root'),
)
 
# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)
 
# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
#    input = cms.untracked.int32 (1000)
    input = cms.untracked.int32 (-1)
)
 
#Get the JetCorrectionREcord from the local db file.
process.GlobalTag.globaltag = "PHYS14_25_V2::All"
 
from CondCore.DBCommon.CondDBSetup_cfi import *
process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
           connect = cms.string('sqlite_file:CSA14_V4_DATA.db'),
           toGet =  cms.VPSet(
              cms.PSet(record = cms.string("JetCorrectionsRecord"),
              tag = cms.string("JetCorrectorParametersCollection_CSA14_V4_DATA_AK10PF"),
              label=cms.untracked.string("AK10PF")),
              cms.PSet(record = cms.string("JetCorrectionsRecord"),
              tag = cms.string("JetCorrectorParametersCollection_CSA14_V4_DATA_AK3PF"),
              label=cms.untracked.string("AK3PF")),
        )
       )
process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")
 
#We can define multiple jet energy corrections to various jet collections.
 
#Apply ak10PF corrections to fatjet.
process.correctedFatJet = cms.EDProducer("BasicJetCorrectionProducer",
    src = cms.InputTag("leadingFat","leadingFat","SJF" ),
    correctors = cms.vstring('ak10PFL1FastjetL2L3')
)
 
#Apply ak3PF corrections to filterjet and subjet.
process.correctedSubJet = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag('caSubjetFilterPFJets', 'sub','SJF'),
    correctors = cms.vstring('ak3PFL1FastjetL2L3')
)
process.correctedFilterJet = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag('caSubjetFilterPFJets', 'filter','SJF'),
    correctors = cms.vstring('ak3PFL1FastjetL2L3')
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
    #jets            =  cms.InputTag  ('caSubjetFilterPFJets', 'sub'),  # subjets 
    jets            =  cms.InputTag  ('correctedFilterJet'),  # change the input tag of filterJet to the corrected one. 
    #basicjets       =  cms.InputTag  ('leadingFat', "leadingFat"),     # leading 2 fat jets
    basicjets       =  cms.InputTag  ('correctedFatJet'),     # change the input tag of fatJet to the corrected one.
    mcparticles     =  cms.InputTag  (''),
    mets            =  cms.InputTag  ('pfMet', ''),
    muons           =  cms.InputTag  ('muons'),
    photons         =  cms.InputTag  ('photons'),
    primaryvertexs  =  cms.InputTag  ('offlinePrimaryVertices'),
    secMuons        =  cms.InputTag  (''),
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
#variableProducers.append("AnaFwkTestEventVariableProducer")
variableProducers.append("AnaFwkTestSubjetVariableProducer")
 
################################################################################
##### Import the channels to be run ############################################
################################################################################
 
from AnaFwkTest.Selection.DibosonSelections import *
from AnaFwkTest.Selection.MyProtoEventSelections import *
 
channels = []
channels.append(skimChannel)
#channels.append(preselectionChannel)
# channels.append(lowMassChannel)
# channels.append(WWChannel)
# channels.append(WZChannel)
# channels.append(ZZChannel)
 
################################################################################
##### Import the histograms to be plotted ######################################
################################################################################
 
from AnaFwkTest.Selection.DibosonHistogramDefinitions import *
 
################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################
 
add_channels (process, channels, cms.VPSet (MyBasicJetHistograms, MyMetHistograms, BasicjetBasicjetHistograms, MyEventVarHistograms), collections, variableProducers)
 
#Define a JEC path to run at the very beginning.
process.JetEnergyCorrectionPath = cms.Path(process.correctedFatJet + process.correctedFilterJet + process.correctedSubJet)
 
#Insert the JEC to the very beginning of the scheduler. 
process.schedule.insert(0,process.JetEnergyCorrectionPath)
# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
 
#process.Tracer = cms.Service("Tracer")
                                                 

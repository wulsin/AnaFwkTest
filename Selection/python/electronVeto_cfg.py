import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('OSUAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring (
   #'root://cmsxrootd.fnal.gov//store/data/Run2012B/MuEG/AOD/20Nov2012-v2/00000/D4591785-E034-E211-B631-003048FF9AA6.root',
   'root://cmsxrootd.fnal.gov//store/mc/Spring14dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/PU_S14_POSTLS170_V6-v1/00000/0A82699D-29C7-E311-90C1-00266CF3338C.root',
  )
)

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (500)
)


###########################################################
##### Set up the analyzer #####
###########################################################

miniAOD_collections = cms.PSet (
  electrons       =  cms.InputTag  ('gedGsfElectrons', '',             'RECO'),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',                    ''),
  mcparticles     =  cms.InputTag  ('slimmedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('slimmedMuons',                   ''),
  photons         =  cms.InputTag  ('slimmedPhotons',                 ''),
  primaryvertexs  =  cms.InputTag  ('offlineSlimmedPrimaryVertices',  ''),
  beamspots       =  cms.InputTag  ('offlineBeamSpot',          '',      'RECO'),
  superclusters   =  cms.InputTag  ('reducedEgamma',                  'reducedSuperClusters'),
  taus            =  cms.InputTag  ('slimmedTaus',                    ''),
  triggers        =  cms.InputTag  ('TriggerResults',                 '',  'HLT'),
  trigobjs        =  cms.InputTag  ('selectedPatTrigger',             ''),
)


electronId = cms.PSet(
    name = cms.string("ElectronId"),
    #triggers = cms.vstring('HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL'), 
    triggers = cms.vstring(""),
    cuts = cms.VPSet (
      # ELECTRON ID
      cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string(" ( \
              abs(superCluster.eta) <= 1.479 & abs(deltaEtaSuperClusterTrackAtVtx) < 0.007 & \
              abs(deltaPhiSuperClusterTrackAtVtx) < 0.8 & \
              sigmaIetaIeta < 0.01 & \
              hadronicOverEm < 0.15  & \
              abs(1/et - 1/pt ) > -1 & \
              isGap < 1 ) | \
              (abs(superCluster.eta) > 1.479 & abs(superCluster.eta) < 2.5 & abs(deltaEtaSuperClusterTrackAtVtx) < 0.01 & \
              abs(deltaPhiSuperClusterTrackAtVtx) < 0.7  & \
              sigmaIetaIeta < 0.03 & \
              hadronicOverEm > -1  & \
              abs(1/et - 1/pt ) > -1 & \
              isGap < 1)"),
        numberRequired = cms.string(">= 0"),
        alias = cms.string("electron Id")
      ),
      # ELECTRON ISOLATION
      cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("                \
              (pfIso_.sumChargedHadronPt \
              + max(0.0,                            \
              pfIso_.sumNeutralHadronEt                    \
              + pfIso_.sumPhotonEt                        \
              - 0.5*pfIso_.sumPUPt))                        \
              /pt < 0.10"),
        numberRequired = cms.string(">= 0"),
        alias = cms.string("electron dBeta isolation < 0.1")
      ),
      # ELECTRON DXY
      cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs(((electron.gsfTrack.vx - beamspot.x0)*electron.gsfTrack.py + (electron.gsfTrack.vy - beamspot.y0)*electron.gsfTrack.px)/electron.gsfTrack.pt)  < 0.02"),
        numberRequired = cms.string(">= 0"),
        alias = cms.string("electron dxy(beamspot)")
      ),
      # ELECTRON DZ
      cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((electron.gsfTrack.vz - beamspot.z0) - ((electron.gsfTrack.vx - beamspot.x0)*electron.gsfTrack.px +  (electron.gsfTrack.vy - beamspot.y0)*electron.gsfTrack.py)/electron.gsfTrack.pt*electron.gsfTrack.pz/electron.gsfTrack.pt)  < 5"),
        numberRequired = cms.string("== 0"),
        alias = cms.string("electron dz(beamspot)")
      ),
   )
)

add_channels  (process,  [electronId],  cms.VPSet  (),  miniAOD_collections,[],False)

from Configuration.DataProcessing.Utils import addMonitoring
process = addMonitoring (process)

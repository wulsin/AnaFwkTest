import FWCore.ParameterSet.Config as cms


#!
#! PROCESS
#!
process = cms.Process("SJF")



#!
#! INPUT
#!
fileNames = cms.untracked.vstring([
    'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/00052B35-3F45-E211-8FD8-0025905964C4.root',
    'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/000CA4B4-D644-E211-9F0B-002618943900.root',
    'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/0011FC38-9545-E211-B798-003048FFD736.root',
    'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/0024836B-CE44-E211-9BE4-0026189438FD.root',
    'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/00461E22-0545-E211-B6AB-00261894393D.root',

    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/00474B99-2093-E211-AB43-E0CB4E19F98A.root',
    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/0068D6F2-3492-E211-84DA-E0CB4E29C4F3.root',
    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/006D4231-3E93-E211-B1E3-E0CB4E19F9BC.root',
    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/00753808-8491-E211-B38B-E0CB4E19F973.root',
    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/00DBAC18-A792-E211-A44E-20CF305616E2.root',
    ])

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))
process.source = cms.Source("PoolSource", fileNames = fileNames)


#!
#! SERVICES
#!
process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring('cout'),
    cout         = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
)


#!
#! JET RECONSTRUCTION
#!
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'FT_R_53_V18::All', '')

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
#process.load('RecoJets.Configuration.GenJetParticles_cff')
#process.load('RecoJets.JetProducers.caSubjetFilterGenJets_cfi')
#process.load('RecoJets.JetProducers.caSubjetFilterCaloJets_cfi')
process.load('RecoJets.JetProducers.caSubjetFilterPFJets_cfi')

process.caSubjetFilterPFJets.massDropCut = 1.0
process.caSubjetFilterPFJets.asymmCut = 0.2

process.leadingFat = cms.EDProducer("LeadingFat",
    fats = cms.InputTag ("caSubjetFilterPFJets", "fat")
)

process.AODoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring ([
      'drop *',
      'keep *_*_*_SIM',
      'keep recoBeamSpot_*_*_*',
      'keep *edmTriggerResults_*_*_*',
      'keep recoGsfElectrons_*_*_*',
      'keep recoPFJets_*_*_*',
      'keep recoPFMETs_*_*_*',
      'keep recoMuons_*_*_*',
      'keep recoPhotons_*_*_*',
      'keep recoVertexs_*_*_*',
      'keep recoPFTaus_*_*_*',
      'keep recoTracks_*_*_*',
      'keep *_*_*_SJF',
    ]),
    fileName = cms.untracked.string('subjetFilter_new.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AOD')
    )
)

#!
#! RUN
#!
process.run = cms.Path(
#    process.genParticlesForJets*
#    process.caSubjetFilterGenJets*
#    process.caSubjetFilterCaloJets*
    process.caSubjetFilterPFJets*
    process.leadingFat
    )

process.AODoutput_step = cms.EndPath(process.AODoutput)

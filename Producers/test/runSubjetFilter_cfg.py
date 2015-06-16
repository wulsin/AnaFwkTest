import FWCore.ParameterSet.Config as cms


#!
#! PROCESS
#!
process = cms.Process("SJF")


#!
#! INPUT
#!
fileNames = cms.untracked.vstring([
    # Quasi-signal sample:  
    # 'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/00052B35-3F45-E211-8FD8-0025905964C4.root',
    # 'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/000CA4B4-D644-E211-9F0B-002618943900.root',
    # 'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/0011FC38-9545-E211-B798-003048FFD736.root',
    # 'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/0024836B-CE44-E211-9BE4-0026189438FD.root',
    # 'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/ZJetsFullyHadronic_Ht100_Pt50_Pt30_deta22_Mqq200_8TeV-madgraph/AODSIM/PU_S10_START53_V7C-v1/10000/00461E22-0545-E211-B6AB-00261894393D.root',

    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/00474B99-2093-E211-AB43-E0CB4E19F98A.root',
    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/0068D6F2-3492-E211-84DA-E0CB4E29C4F3.root',
    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/006D4231-3E93-E211-B1E3-E0CB4E19F9BC.root',
    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/00753808-8491-E211-B38B-E0CB4E19F973.root',
    #'root://cmsxrootd.fnal.gov///store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/00DBAC18-A792-E211-A44E-20CF305616E2.root',

# Signal sample:  
    'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/RSGravitonToZZ_kMpl01_M-2000_TuneZ2star_8TeV-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/2EF4E83B-37F8-E111-A41C-E41F13181A88.root', 
    'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/RSGravitonToZZ_kMpl01_M-2000_TuneZ2star_8TeV-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3A1443B3-39F8-E111-BE04-00215E221680.root', 
    'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/RSGravitonToZZ_kMpl01_M-2000_TuneZ2star_8TeV-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/72A83B17-3EF8-E111-BA45-00215E93F080.root', 
    'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/RSGravitonToZZ_kMpl01_M-2000_TuneZ2star_8TeV-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/A891748B-35F8-E111-9E77-00215E93D738.root', 

# QCD MC sample:  (only 4 sample files given here; full list for this dataset is given in AAAFileListQCD_Pt1800
    # 'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/QCD_Pt-1800_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/02533972-471A-E211-883B-00266CFFA768.root', 
    # 'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/QCD_Pt-1800_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/02A5AA68-471A-E211-A1BC-00266CFFA704.root', 
    # 'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/QCD_Pt-1800_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/0C8BD5B5-251A-E211-8418-003048CEFFE4.root', 
    # 'root://cmsxrootd.fnal.gov///store/mc/Summer12_DR53X/QCD_Pt-1800_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/0E0DE4EB-521A-E211-BD90-00266CFFA090.root', 

    ])

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))
process.source = cms.Source("PoolSource", fileNames = fileNames)


#!
#! SERVICES
#!
process.load ('FWCore.MessageService.MessageLogger_cfi')
# process.MessageLogger = cms.Service("MessageLogger",
#     destinations = cms.untracked.vstring('cout', 'cerr'),
#     cout         = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
# )
process.MessageLogger.cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
process.MessageLogger.cerr.FwkReport.reportEvery = 1



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

from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SubjetFilter_2012A_v1'
config.General.workArea = 'crab'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runSubjetFilterAndPAT_cfg.py'
config.JobType.inputFiles = ["CSA14_V4_DATA.db"]

config.Data.inputDataset = '/HT/Run2012A-22Jan2013-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 30
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt'
config.Data.outLFNDirBase = '/store/user/ahart' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.publishDataName = 'Run2012A-22Jan2013-SubjetFilter-v1'

config.Site.storageSite = 'T2_US_Purdue'

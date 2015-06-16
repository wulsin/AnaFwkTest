import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
import re
import py_compile

py_compile.compile('dibosonConfigWithJEC_cfg.py')
py_compile.compile('datasetInfo_JetHt2012BCD_cfg.py')

exec("import dibosonConfigWithJEC_cfg as pset")
exec("from datasetInfo_JetHt2012BCD_cfg import parentDic")


pset.process.SkimChannelPoolOutputModule.fileName = cms.untracked.string('/data/users/bing/condor/DiBosonSkimJune15/JetHtBCD/SkimChannel/skim_'+ str (osusub.jobNumber)+ '.root')

fileName = pset.process.TFileService.fileName
fileName = fileName.pythonValue ()
fileName = fileName[1:(len (fileName) - 1)]
fileName = re.sub (r'^(.*)\.([^\.]*)$', r'\1_' + str (osusub.jobNumber) + r'.\2', fileName)
pset.process.TFileService.fileName = fileName

pset.process.source.secondaryFileNames= cms.untracked.vstring()

for file in osusub.runList:
    secondaryFileList = parentDic[file] 
    for secondaryFile in secondaryFileList:
        pset.process.source.secondaryFileNames.append(secondaryFile)

pset.process.SkimChannelPoolOutputModule.outputCommands.append('keep *_caSubjetFilterPFJets_*_*')
pset.process.SkimChannelPoolOutputModule.outputCommands.append('keep *_correctedSubJet__*')
pset.process.SkimChannelPoolOutputModule.outputCommands.append('keep *_leadingFat_leadingFat_*')

pset.process.source.fileNames = cms.untracked.vstring (osusub.runList)
pset.process.maxEvents.input = cms.untracked.int32 (-1)
process = pset.process

import FWCore.ParameterSet.Config as cms
import copy
from AnaFwkTest.Selection.CommonUtils import *  
from AnaFwkTest.Selection.CutDefinitions import *  



##########################################################################
#############################  Skim Channel  #############################
##########################################################################

# trigger, met cut, lepton vetos, basic jet cuts

skimChannel = cms.PSet(
    name = cms.string("SkimChannel"),
    triggers = singleJetTrigger,
    cuts = copy.deepcopy(skimSelection)
)

##########################################################################
#########################  Preselection Channel  #########################
##########################################################################

# skim selection + more jet selections + dijet selections
# (all cuts except W and Z mass window cuts)

preselectionChannel = cms.PSet(
    name = cms.string("PreselectionChannel"),
    triggers = singleJetTrigger,
    cuts = copy.deepcopy(preselection)
)

##########################################################################
#########################  Mass Sideband Channel  ########################
##########################################################################

# preselection + jet masses both between 40 and 60 GeV

lowMassChannel = cms.PSet(
    name = cms.string("LowMassChannel"),
    triggers = singleJetTrigger,
    cuts = copy.deepcopy(preselection)
)

jetLeadingLowMassCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMax - 50 ) < 10"),
    numberRequired = cms.string(">= 1"),
)

jetSubleadingLowMassCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMin - 50 ) < 10"),
    numberRequired = cms.string(">= 1"),
)

lowMassChannel.cuts.append(jetLeadingLowMassCut)
lowMassChannel.cuts.append(jetSubleadingLowMassCut)

##########################################################################
##############################  WZ Channel  ##############################
##########################################################################

# preselection + one W-tagged jet and one Z-tagged jet 

WZChannel = cms.PSet(
    name = cms.string("WZChannel"),
    triggers = singleJetTrigger,
    cuts = copy.deepcopy(preselection)
)

jetZMassCut_WZ = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMax - " + str(massZ) + " ) < 13"),
    numberRequired = cms.string(">= 1"),
)
jetWMassCut_WZ = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMin - " + str(massW) + " ) < 13"),
    numberRequired = cms.string(">= 1"),
)

WZChannel.cuts.append(jetZMassCut_WZ)
WZChannel.cuts.append(jetWMassCut_WZ)

##########################################################################
##############################  WW Channel  ##############################
##########################################################################

# preselection + two W-tagged jets

WWChannel = cms.PSet(
    name = cms.string("WWChannel"),
    triggers = singleJetTrigger,
    cuts = copy.deepcopy(preselection)
)

jetZMassCut_WW = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMax - " + str(massW) + " ) < 13"),
    numberRequired = cms.string(">= 1"),
)
jetWMassCut_WW = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMin - " + str(massW) + " ) < 13"),
    numberRequired = cms.string(">= 1"),
)

WWChannel.cuts.append(jetZMassCut_WW)
WWChannel.cuts.append(jetWMassCut_WW)

##########################################################################
##############################  ZZ Channel  ##############################
##########################################################################

# preselection + two Z-tagged jets

ZZChannel = cms.PSet(
    name = cms.string("ZZChannel"),
    triggers = singleJetTrigger,
    cuts = copy.deepcopy(preselection)
)

jetZMassCut_ZZ = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMax - " + str(massZ) + " ) < 13"),
    numberRequired = cms.string(">= 1"),
)
jetWMassCut_ZZ = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMin - " + str(massZ) + " ) < 13"),
    numberRequired = cms.string(">= 1"),
)

ZZChannel.cuts.append(jetZMassCut_ZZ)
ZZChannel.cuts.append(jetWMassCut_ZZ)

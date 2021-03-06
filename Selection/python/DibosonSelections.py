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
    triggers = jetHtTrigger,  
    cuts = copy.deepcopy(skimSelection)
)

##########################################################################
#########################  Preselection Channel  #########################
##########################################################################

# skim selection + more jet selections + dijet selections
# (all cuts except W and Z mass window cuts)

preselectionChannel = cms.PSet(
    name = cms.string("PreselectionChannel"),
    triggers = jetHtTrigger,
    cuts = copy.deepcopy(preselection)
)

##########################################################################
#########################  ATLAS Mass Sideband Channel  ##################
##########################################################################

# preselection + jet masses both between 40 and 60 GeV

lowMassChannel = cms.PSet(
    name = cms.string("LowMassChannel"),
    triggers = jetHtTrigger,
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
######################  Extended Mass Sideband Channel  ##################
##########################################################################

# preselection + jet masses both in range of 40-60 GeV or >120 GeV

extendedMassChannel = cms.PSet(
    name = cms.string("ExtendedMassChannel"),
    triggers = jetHtTrigger,
    cuts = copy.deepcopy(preselection)
)

jetLeadingMassSideExtCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMax - 50 ) < 10 || fatjetMassMax > 120"),
    numberRequired = cms.string(">= 1"),
)

jetSubleadingMassSideExtCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( fatjetMassMin - 50 ) < 10 || fatjetMassMin > 120"),
    numberRequired = cms.string(">= 1"),
)

extendedMassChannel.cuts.append(jetLeadingMassSideExtCut)
extendedMassChannel.cuts.append(jetSubleadingMassSideExtCut)

##########################################################################
##############################  WZ Channel  ##############################
##########################################################################

# preselection + one W-tagged jet and one Z-tagged jet 

WZChannel = cms.PSet(
    name = cms.string("WZChannel"),
    triggers = jetHtTrigger,
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
    triggers = jetHtTrigger,
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
    triggers = jetHtTrigger,
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

import FWCore.ParameterSet.Config as cms
import copy
from AnaFwkTest.Selection.CommonUtils import *  

##########################################################################
############# Define the cuts used by all diboson channels  ##############
##########################################################################

singleJetTrigger = cms.vstring("HLT_PFJet320_v")
jetHtTrigger = cms.vstring("HLT_PFNoPUHT650_v","HLT_PFHT650_v","HLT_HT750_v","HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v")

##########################################################################

metCut = cms.PSet (
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt < 350"),
    numberRequired = cms.string("== 1")
) 

##########################################################################

muonVeto =  cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 2.5 && pt > 20"),
    numberRequired = cms.string("== 0"), 
    isVeto = cms.bool(True),
    alias = cms.string("muon veto")
)

##########################################################################

# Start Electron Cuts 
electronPtCut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 0"),
)
electronEtaCut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(eta) < 1.4442 | abs(eta) > 1.566"),
    numberRequired = cms.string(">= 0"),
)

electronIsoCut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("\
        (pfIso_.sumChargedHadronPt \
        + max(0.0,  \
        pfIso_.sumNeutralHadronEt  \
        + pfIso_.sumPhotonEt \
        - 0.5*pfIso_.sumPUPt)) \
        /pt < 0.10"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("electron dBeta isolation < 0.1")
)

electronD0Cut = cms.PSet (
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("abs(((electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) < 0.02"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("electron dxy(beamspot)")
)

electronIDCut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string(" ( \
        abs(eta) < 1.479 & abs(deltaEtaSuperClusterTrackAtVtx) < 0.004 & \
        abs(deltaPhiSuperClusterTrackAtVtx) < 0.03 & \
        scSigmaIEtaIEta < 0.01 & \
        hadronicOverEm < 0.12  & \
        abs(1/et - 1/pt ) < 0.05  & \
        isGap < 1 ) | \
        (abs(eta) > 1.479 & abs(eta) < 2.5 & abs(deltaEtaSuperClusterTrackAtVtx) < 0.005 & \
        abs(deltaPhiSuperClusterTrackAtVtx) < 0.02 & \
        scSigmaIEtaIEta < 0.03 & \
        hadronicOverEm < 0.10  & \
        abs(1/et - 1/pt ) < 0.05  & \
        isGap < 1)"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("electron Id")
)

electronVeto =  cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 0"), 
    isVeto = cms.bool(True),
    alias = cms.string("electron veto")
)

##########################################################################

# JET CUTS

basicjetPtCut = cms.PSet (
    inputCollection = cms.vstring("basicjets"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2")
)

jetLeadingPtCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("ptLeading > 20"),
    numberRequired = cms.string(">= 1")
)

jetSubleadingPtCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("ptSubleading > 20"),
    numberRequired = cms.string(">= 1")
)

jetLeadingEtaCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs(etaLeading) < 2.0"),
    numberRequired = cms.string(">= 1")
)

jetSubleadingEtaCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs(etaSubleading) < 2.0"),
    numberRequired = cms.string(">= 1")
)

jetExtraJetVeto = cms.PSet (
    inputCollection = cms.vstring("basicjets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2"),
    alias = cms.string("extra jet veto")
)

jetNConstituentsCut = cms.PSet (
    inputCollection = cms.vstring("basicjets"),
    cutString = cms.string("nConstituents >= 2"),
    numberRequired = cms.string(">= 2"),
)

jetLeadingMinTrksCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("basicjetNConstChgdLeading > 0"),
    numberRequired = cms.string(">= 1"),
)

jetSubleadingMinTrksCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("basicjetNConstChgdSubleading > 0"),
    numberRequired = cms.string(">= 1"),
)

jetLeadingMaxTrksCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("chargedMultiplicityLeading < 30"),
    numberRequired = cms.string(">= 1"),
)

jetSubleadingMaxTrksCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("chargedMultiplicitySubleading < 30"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################

# DIJET CUTS

dijetDeltaYCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs ( rapidityDiff ) < 1.2"),
    numberRequired = cms.string(">= 1"),
)

dijetPtBalanceCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fatjetRelPtDiff < 0.15"),
    numberRequired = cms.string(">= 1"),
)

dijetSqrtYCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("minSqrtY > 0.45"), # if minSqrtY > 0.45, that means both leading fat jets are above that cut
    numberRequired = cms.string(">= 1"),
)

dijetMassCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),  
    cutString = cms.string("invMassLeadingSubleading > 500"),   # 500 GeV for testing, official is 1.05 TeV
    numberRequired = cms.string(">= 1"),
)


##########################################################################
########### Define selections by combining pre-defined cuts  #############
##########################################################################

skimSelection = cms.VPSet ()
skimSelection.append(metCut)
skimSelection.append(muonVeto)
skimSelection.append(electronPtCut)
skimSelection.append(electronEtaCut)
skimSelection.append(electronIsoCut)
skimSelection.append(electronD0Cut)
skimSelection.append(electronIDCut)
skimSelection.append(electronVeto)

#skimSelection.append(jetLeadingPtCut)
#skimSelection.append(jetSubleadingPtCut)
skimSelection.append(jetNConstituentsCut)  
skimSelection.append(basicjetPtCut)  
skimSelection.append(jetLeadingEtaCut)
skimSelection.append(jetSubleadingEtaCut)
skimSelection.append(jetExtraJetVeto)

##########################################################################

jetSelection = cms.VPSet ()
#jetSelection.append(jetLeadingMinTrksCut)
#jetSelection.append(jetSubleadingMinTrksCut)

# Do not include the n_trks < 30 cut because this distribution is not yet well understood
# jetSelection.append(jetLeadingMaxTrksCut)
# jetSelection.append(jetSubleadingMaxTrksCut)

##########################################################################

dijetSelection = cms.VPSet ()
dijetSelection.append(dijetDeltaYCut)
dijetSelection.append(dijetPtBalanceCut)
dijetSelection.append(dijetSqrtYCut)
#dijetSelection.append(dijetMassCut)

##########################################################################

preselection = cms.VPSet ()
preselection += skimSelection
preselection += jetSelection
preselection += dijetSelection

##########################################################################

import FWCore.ParameterSet.Config as cms
import copy
from AnaFwkTest.Selection.CommonUtils import *  

##########################################################################
############# Define the cuts used by all diboson channels  ##############
##########################################################################

singleJetTrigger = cms.vstring("HLT_PFJet320_v")

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

jetPtCut = cms.PSet (
    inputCollection = cms.vstring("basicjets"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2")
)

jetEtaCut = cms.PSet (
    inputCollection = cms.vstring("basicjets"),
    cutString = cms.string("fabs(eta) < 2.0"),
    numberRequired = cms.string(">= 2"),
)

jetExtraJetVeto = cms.PSet (
    inputCollection = cms.vstring("basicjets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("extra jet veto")
)

jetNConstituentsCut = cms.PSet (
    inputCollection = cms.vstring("basicjets"),
    cutString = cms.string("nConstituents >= 2"),
    numberRequired = cms.string(">= 2"),
)


jet1MinTrksCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("basicjetNConstChgd1 > 0"),
    numberRequired = cms.string(">= 1"),
)

jet2MinTrksCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("basicjetNConstChgd2 > 0"),
    numberRequired = cms.string(">= 1"),
)

jet1MaxTrksCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("chargedMultiplicity0 < 30"),
    numberRequired = cms.string(">= 1"),
)

jet2MaxTrksCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("chargedMultiplicity1 < 30"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################

# DIJET CUTS

dijetDeltaYCut = cms.PSet (
    inputCollection = cms.vstring("basicjets", "basicjets"),
    cutString = cms.string("fabs ( basicjet.rapidity - basicjet.rapidity ) < 1.2"),
    numberRequired = cms.string("== 1"),
)

dijetPtBalanceCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("basicjetRelPtDiff < 0.15"),
    numberRequired = cms.string(">= 1"),
)

dijetSqrtYCut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("minSqrtY > 0.45"), # if minSqrtY > 0.45, that means both leading fat jets are above that cut
    numberRequired = cms.string(">= 1"),
)

dijetMassCut = cms.PSet (
    inputCollection = cms.vstring("basicjets", "basicjets"),
    cutString = cms.string("invMass (basicjet, basicjet) > 500"),   # 500 GeV for testing, official is 1.05 TeV
    numberRequired = cms.string("== 1"),
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

skimSelection.append(jetPtCut)
skimSelection.append(jetEtaCut)
skimSelection.append(jetExtraJetVeto)
#skimSelection.append(jetNConstituentsCut)  

##########################################################################

jetSelection = cms.VPSet ()
#jetSelection.append(jet1MinTrksCut)
#jetSelection.append(jet2MinTrksCut)
jetSelection.append(jet1MaxTrksCut)
jetSelection.append(jet2MaxTrksCut)

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

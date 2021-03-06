##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##### THIS FILE IS FOR TESTING ONLY
##### DO DEVELOPMENT INSTEAD IN DIBOSONSELECTIONS.PY
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################




















































import FWCore.ParameterSet.Config as cms
import copy
from AnaFwkTest.Selection.CommonUtils import *  

##########################################################################
##### WZ channel
##########################################################################

channelDebug = cms.PSet(
    name = cms.string("channelDebug"),
    triggers = cms.vstring("HLT_PFJet320_v"), # TRIGGER   
    cuts = cms.VPSet (
    )
)
 
channelWZ = cms.PSet(
    name = cms.string("channelWZ"),
    triggers = cms.vstring("HLT_PFJet320_v"), # TRIGGER   
    cuts = cms.VPSet (
        # MET CUT
        cms.PSet (
            inputCollection = cms.vstring("mets"),
            cutString = cms.string("pt < 350"),
            numberRequired = cms.string("== 1")
        ), 
        # MUON VETO
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.5 && pt > 20"),
            numberRequired = cms.string("== 0"), 
            isVeto = cms.bool(True),
            alias = cms.string("muon veto")
        ),
        # Start Electron Veto
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 20"),
            numberRequired = cms.string(">= 0"),
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 1.4442 | abs(eta) > 1.566"),
            numberRequired = cms.string(">= 0"),
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
            cutString = cms.string("abs(((electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) < 0.02"),
            numberRequired = cms.string(">= 0"),
            alias = cms.string("electron dxy(beamspot)")
         ), 
        cms.PSet (
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
            numberRequired = cms.string("== 0"),
            alias = cms.string("electron Id")
        ),
        # JET PT 
        cms.PSet (
            inputCollection = cms.vstring("basicjets"),
            cutString = cms.string("pt > 20"),
            numberRequired = cms.string(">= 2"),
        ),
        # JET ETA
        cms.PSet (
            inputCollection = cms.vstring("basicjets"),
            cutString = cms.string("fabs(eta) < 2.0"),
            numberRequired = cms.string(">= 2"),
        ),
        # # REQUIRE EACH FAT JET TO HAVE AT LEAST 2 SUBJETS
        # cms.PSet (
        #     inputCollection = cms.vstring("basicjets"),
        #     cutString = cms.string("nConstituents >= 2"),
        #     numberRequired = cms.string(">= 2"),
        # ),
        # JET RAPIDITY DIFFERENCE
        cms.PSet (
            inputCollection = cms.vstring("basicjets", "basicjets"),
            cutString = cms.string("fabs ( basicjet.rapidity - basicjet.rapidity ) < 1.2"),
            numberRequired = cms.string("== 1"),
        ),
        # # CHARGED MULTIPLICITY OF JET 1 
        # cms.PSet (
        #     inputCollection = cms.vstring("eventvariables"),
        #     cutString = cms.string("chargedMultiplicity0 < 30"),
        #     numberRequired = cms.string(">= 1"),
        # ),
        # # CHARGED MULTIPLICITY OF JET 2
        # cms.PSet (
        #     inputCollection = cms.vstring("eventvariables"),
        #     cutString = cms.string("chargedMultiplicity1 < 30"),
        #     numberRequired = cms.string(">= 1"),
        # ),
        # JET-JET PT BALANCE
        cms.PSet (
            inputCollection = cms.vstring("eventvariables"),
            cutString = cms.string("basicjetRelPtDiff < 0.15"),
            numberRequired = cms.string(">= 1"),
        ),
        # JET SQRT(Y)
        cms.PSet (
            inputCollection = cms.vstring("eventvariables"),
            cutString = cms.string("minSqrtY > 0.45"), # if minSqrtY > 0.45, that means both
                                                       # leading fat jets are above that cut
            numberRequired = cms.string(">= 1"),
        ),
        # WZ CHANNEL:  LARGER MASS CONSISTENT WITH Z
        cms.PSet (
            inputCollection = cms.vstring("eventvariables"),
            cutString = cms.string("fabs ( basicjetMassMax - " + str(massZ) + " ) < 13"),   
            numberRequired = cms.string(">= 1"),
        ),
        # WZ CHANNEL:  SMALLER MASS CONSISTENT WITH W
        cms.PSet (
            inputCollection = cms.vstring("eventvariables"),
            cutString = cms.string("fabs ( basicjetMassMin - " + str(massW) + " ) < 13"),   
            numberRequired = cms.string(">= 1"),
        ),
        # JET-JET INVARIANT MASS 
        cms.PSet (
            inputCollection = cms.vstring("basicjets", "basicjets"),
#            cutString = cms.string("invMass (basicjet, basicjet) > 1050"),  # Value in arXiv:1506.00962
            cutString = cms.string("invMass (basicjet, basicjet) > 500"),   # for testing
            numberRequired = cms.string("== 1"),
        ),
        )
    )

##########################################################################
######## Set up the preselection for the displaced SUSY analysis #########
##########################################################################

preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
        # EVENT CLEANING
        cms.PSet (
            inputCollection = cms.vstring("events"),
            cutString = cms.string("FilterOutScraping > 0"),
            numberRequired = cms.string(">= 1")
        ),
        # EVENT HAS GOOD PV
        cms.PSet (
            inputCollection = cms.vstring("primaryvertexs"),
            cutString = cms.string("isGood > 0"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON ETA CUT
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 2.5"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON CRACK VETO
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("isEBEEGap = 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron ECAL crack veto")
        ),
        # ELECTRON PT CUT
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON ID
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("                              \
              (pt > 7 && pt < 10                                  \
                && ((abs (scEta) < 0.8 && mvaNonTrigV0 > 0.47)    \
                || (abs (scEta) >= 0.8 && abs (scEta) < 1.479 && mvaNonTrigV0 > 0.004) \
                || (abs (scEta) >= 1.479 && abs (scEta) < 2.5 && mvaNonTrigV0 > 0.295))) \
           || (pt >= 10                                           \
                && ((abs (scEta) < 0.8 && mvaNonTrigV0 > -0.34)   \
                || (abs (scEta) >= 0.8 && abs (scEta) < 1.479 && mvaNonTrigV0 > -0.65) \
                || (abs (scEta) >= 1.479 && abs (scEta) < 2.5 && mvaNonTrigV0 > 0.60)))  \
           "),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron ID")
        ),
        # PHOTON CONVERSION VETO
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("passConvVeto > 0 && numberOfLostHits = 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron conversion rejection")
        ),
        # ELECTRON ISOLATION
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("((chargedHadronIsoDR03 + max (0.0, neutralHadronIsoDR03 + photonIsoDR03 - AEffDr03 * rhoPrime)) / pt) < 0.1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron isolation")
        ),
        # MUON ETA CUT
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.5"),
            numberRequired = cms.string(">= 1")
        ),
        # MUON PT CUT
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        # MUON ID
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("               \
               isGlobalMuon                        \
            && isPFMuon                            \
            && (normalizedChi2 < 10.0)             \
            && (numberOfValidMuonHits > 0)         \
            && (numberOfMatchedStations > 1)       \
            && (numberOfValidPixelHits > 0)        \
            && (numberOfLayersWithMeasurement > 5) \
            "),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("muon ID")
        ),
        # MUON ISOLATION
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("((pfIsoR04SumChargedHadronPt + max (0.0, pfIsoR04SumNeutralHadronEt + pfIsoR04SumPhotonEt - 0.5 * pfIsoR04SumPUPt)) / pt) < 0.12"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("muon isolation")
        ),
        # VETO EVENTS WITH EXTRA ELECTRON
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra electron veto")
        ),
        # VETO EVENTS WITH EXTRA MUON
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra muon veto")
        ),
        # OPPOSITE SIGN E-MU PAIR
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("electron.charge * muon.charge < 0"),
            numberRequired = cms.string("== 1")
        ),
        # ELECTRON AND MUON ARE NOT OVERLAPPING
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("deltaR(electron, muon) > 0.5"),
            numberRequired = cms.string("== 1")
        ),
        #########START OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A JET
        # ONLY CONSIDER 30 GEV JETS
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("pt > 10"),
            numberRequired = cms.string(">= 0")
        ),
        # ELECTRON NOT OVERLAPPING WITH JET
        cms.PSet (
            inputCollection = cms.vstring("electrons", "jets"),
            cutString = cms.string("deltaR(electron, jet) < 0.5"),
            numberRequired = cms.string("== 0"),
            isVeto = cms.bool(True),
            alias = cms.string("electron near jet veto"),
        ),
        # MUON NOT OVERLAPPING WITH JET
        cms.PSet (
            inputCollection = cms.vstring("muons", "jets"),
            cutString = cms.string("deltaR(muon, jet) < 0.5"),
            numberRequired = cms.string("== 0"),
            isVeto = cms.bool(True),
            alias = cms.string("muon near jet veto"),
        ),
        ########### END OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A JET

        # RESTRICT ELECTRONS TO RECONSTRUCTION ACCEPTANCE
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(correctedD0) < 2"),
            numberRequired = cms.string("== 1")
        ),
        # RESTRICT MUONS TO TRIGGER ACCEPTANCE
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(correctedD0) < 2"),
            numberRequired = cms.string("== 1")
        ),
    )
)

##########################################################################





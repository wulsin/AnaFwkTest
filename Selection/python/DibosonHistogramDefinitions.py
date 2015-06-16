import FWCore.ParameterSet.Config as cms
from AnaFwkTest.Selection.CommonUtils import *  

###############################################
##### Set up the histograms to be plotted #####
###############################################

histograms = cms.PSet(
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonNum"),
            title = cms.string("Number of selected muons; Number of selected muons"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("number ( muon )"),
        ),
        cms.PSet (
            name = cms.string("muonPt"),
            title = cms.string("Muon Transverse Momentum; muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonEta"),
            title = cms.string("Muon Pseudorapidity; muon #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
    )
)


MyElectronHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronNum"),
            title = cms.string("Number of selected electrons; Number of selected electrons"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("number ( electron )"),
        ),
        cms.PSet (
            name = cms.string("electronPt"),
            title = cms.string("Electron Transverse Momentum; electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        #  cms.PSet (
        #     name = cms.string("electronGenPt"),
        #     title = cms.string("Electron Gen. Transverse Momentum; generated electron p_{T} [GeV]"),
        #     binsX = cms.untracked.vdouble(100, 0, 500),
        #     inputVariables = cms.vstring("genPT"),
        # ),
        cms.PSet (
            name = cms.string("electronEta"),
            title = cms.string("Electron Eta; electron #eta"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        # cms.PSet (
        #     name = cms.string("electronId"),
        #     title = cms.string("Electron ID; electron ID"),
        #     binsX = cms.untracked.vdouble(4, -1.5, 2.5),
        #     inputVariables = cms.vstring(electronID),
        # ),
    )
)

# FIXME:  We probably should not even include the basicjet histograms,
# since they may be misleading.  
BasicjetBasicjetHistograms = cms.PSet(
    inputCollection = cms.vstring("basicjets", "basicjets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("basicjetbasicjetDeltaR"),
            title = cms.string("DeltaR between 2 jets"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("deltaR (basicjet, basicjet)"),
        ),
        cms.PSet (
            name = cms.string("basicjetbasicjetRapidityDiff"),
            title = cms.string("Eta difference of 2 basicjets;jet |y_{1} - y_{2}|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("fabs (basicjet.rapidity - basicjet.rapidity)"),
        ),
        cms.PSet (
            name = cms.string("basicjetbasicjetEtaDiff"),
            title = cms.string("Eta difference of 2 basicjets;jet |#eta_{1} - #eta_{2}|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("fabs (basicjet.eta - basicjet.eta)"),
        ),
        cms.PSet (
            name = cms.string("basicjetbasicjetPtDiff"),
            title = cms.string("Relative difference in pt;(pT1 - pT2)"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("basicjet.pt - basicjet.pt"),
        ),
        cms.PSet (
            name = cms.string("basicjetbasicjetPtSum"),
            title = cms.string("Sum of pt;(pT1 + pT2)"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("(basicjet.pt + basicjet.pt)"),
        ),
        # cms.PSet (
        #     name = cms.string("basicjetbasicjetPtRelDiff"),
        #     title = cms.string("Relative difference in pt;(pT1 - pT2) / (pT1 + pT2)"),
        #     binsX = cms.untracked.vdouble(100, -1, 1),
        #     inputVariables = cms.vstring("(basicjet.pt - basicjet.pt) / (basicjet.pt + basicjet.pt)"),
        # ),
        cms.PSet (
            name = cms.string("basicjetbasicjetInvMass"),
            title = cms.string("Invariant mass of 2 basicjets"),
            binsX = cms.untracked.vdouble(350, 0, 3500),
            inputVariables = cms.vstring("invMass (basicjet, basicjet)"),
        ),
    )
)


MyJetHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetNum"),
            title = cms.string("Number of selected jets; Number of selected jets"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("number ( jet )"),
        ),
        cms.PSet (
            name = cms.string("jetPt"),
            title = cms.string("Jet Transverse Momentum; p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("jetEta"),
            title = cms.string("Jet Eta; #eta"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("jetPhi"),
            title = cms.string("Jet Phi; #phi"),
            binsX = cms.untracked.vdouble(100, -3.15, 3.15),
            inputVariables = cms.vstring("phi"),
        ),
        # cms.PSet (
        #     name = cms.string("jetNConst"),
        #     title = cms.string("Jet NConst; number of constituents"),
        #     binsX = cms.untracked.vdouble(50, 0, 100),
        #     inputVariables = cms.vstring("Nconst"),
        # ),
        cms.PSet (
            name = cms.string("jetMass"),
            title = cms.string("Jet mass; m_{j} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("mass"),
        ),
        cms.PSet (
            name = cms.string("jetMassDiffW"),
            title = cms.string("Jet mass difference from W; m_{j} - m_{W}"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("mass - " + str(massW)),
        ),
        cms.PSet (
            name = cms.string("jetMassDiffZ"),
            title = cms.string("Jet mass difference from Z; m_{j} - m_{Z}"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("mass - " + str(massZ)),
        ),
        cms.PSet (
            name = cms.string("jetCharge"),
            title = cms.string("Jet Charge; charge"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("jetEtaPhi"),
            title = cms.string("Jet Eta vs. Phi; #phi; #eta"),
            binsX = cms.untracked.vdouble(100, -3.15, 3.15), 
            binsY = cms.untracked.vdouble(100, -3, 3), 
            inputVariables = cms.vstring("phi","eta"),
        ),
        # cms.PSet (
        #     name = cms.string("jetFlavor"),
        #     title = cms.string("Jet Flavor"),
        #     binsX = cms.untracked.vdouble(42, -21, 21),
        #     inputVariables = cms.vstring("flavour"),
        # ),
        cms.PSet (
            name = cms.string("jetChargedHadronEnergyFraction"),
            title = cms.string("Jet Charged Hadron Fraction"),
            binsX = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("chargedHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralHadronEnergyFraction"),
            title = cms.string("Jet Neutral Hadron Fraction"),
            binsX = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("neutralHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralEMEnergyFraction"),
            title = cms.string("Jet Neutral EM Fraction"),
            binsX = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("neutralEmEnergyFraction"),
        ),
        # cms.PSet (
        #     name = cms.string("jetChargedEMEnergyFraction"),
        #     title = cms.string("Jet Charged EM Fraction"),
        #     binsX = cms.untracked.vdouble(120, -0.1, 1.1),
        #     inputVariables = cms.vstring("chargedEmEnergyFraction"),
        # ),
        # cms.PSet (
        #     name = cms.string("jetCSV"),
        #     title = cms.string("Jet Combined Secondary Vertex B-tagging Discriminant"),
        #     binsX = cms.untracked.vdouble(100, -1, 1),
        #     inputVariables = cms.vstring("btagCombinedSecVertex"),
        # ),
        # cms.PSet (
        #     name = cms.string("jetSize"),
        #     title = cms.string("Number of Jets"),
        #     binsX = cms.untracked.vdouble(20, 0, 20),
        #     inputVariables = cms.vstring("jets.size()"),
        # ),
        # cms.PSet (
        #     name = cms.string("jetMetDeltaPhi"),
        #     title = cms.string("Jet-MET Delta Phi; |#Delta(#phi)|"),
        #     binsX = cms.untracked.vdouble(100, 0, 3.15),
        #     inputVariables = cms.vstring("dPhiMet"),
        # ),
        
    )
)



MyBasicJetHistograms = cms.PSet(
    inputCollection = cms.vstring("basicjets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetNum"),
            title = cms.string("Number of selected basicjets; Number of selected basicjets"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("number ( basicjet )"),
        ),
        cms.PSet (
            name = cms.string("jetPt"),
            title = cms.string("Jet Transverse Momentum; p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("jetEta"),
            title = cms.string("Jet Eta; #eta"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("jetRapidity"),
            title = cms.string("Jet Eta; jet y"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("rapidity"),
        ),
        cms.PSet (
            name = cms.string("jetPhi"),
            title = cms.string("Jet Phi; #phi"),
            binsX = cms.untracked.vdouble(100, -3.15, 3.15),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("jetMass"),
            title = cms.string("Jet mass; m_{j} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("mass"),
        ),
        cms.PSet (
            name = cms.string("jetMassDiffW"),
            title = cms.string("Jet mass difference from W; m_{j} - m_{W}"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("mass - " + str(massW)),
        ),
        cms.PSet (
            name = cms.string("jetMassDiffZ"),
            title = cms.string("Jet mass difference from Z; m_{j} - m_{Z}"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("mass - " + str(massZ)),
        ),
        # cms.PSet (
        #     name = cms.string("getJetConstituentsSize"),
        #     title = cms.string("getJetConstituentsSize;getJetConstituentsSize"), 
        #     binsX = cms.untracked.vdouble(31, -0.5, 30.5),
        #     inputVariables = cms.vstring("getJetConstituents.size"),  # FIXME:  produces error:  
        #     # WARNING: "getJetConstituents.size" has unrecognized type "unsigned long int" 
        # ),
        cms.PSet (
            name = cms.string("nConstituents"),
            title = cms.string("nConstituents; nConstituents"), 
            binsX = cms.untracked.vdouble(31, -0.5, 30.5),
            inputVariables = cms.vstring("nConstituents"),
        ),
        cms.PSet (
            name = cms.string("jetCharge"),
            title = cms.string("Jet Charge; charge"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("jetEtaPhi"),
            title = cms.string("Jet Eta vs. Phi; #phi; #eta"),
            binsX = cms.untracked.vdouble(100, -3.15, 3.15), 
            binsY = cms.untracked.vdouble(100, -3, 3), 
            inputVariables = cms.vstring("phi","eta"),
        ),        
    )
)


MyEventVarHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("ptLeading"),
            title = cms.string("p_{T} of leading jet; p_{T} of leading jet [GeV]"), 
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("ptLeading"),
        ),
        cms.PSet (
            name = cms.string("ptSubleading"),
            title = cms.string("p_{T} of subleading jet; p_{T} of subleading jet [GeV]"), 
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("ptSubleading"),
        ),
        cms.PSet (
            name = cms.string("etaLeading"),
            title = cms.string("#eta of leading jet; #eta of leading jet"), 
            binsX = cms.untracked.vdouble(100, -5, 5), 
            inputVariables = cms.vstring("etaLeading"),
        ),
        cms.PSet (
            name = cms.string("etaSubleading"),
            title = cms.string("#eta of subleading jet; #eta of subleading jet"), 
            binsX = cms.untracked.vdouble(100, -5, 5), 
            inputVariables = cms.vstring("etaSubleading"),
        ),
        cms.PSet (
            name = cms.string("rapidityDiff"),
            title = cms.string("rapidity difference of 2 fatjets;jet |y_{1} - y_{2}|"),
            binsX = cms.untracked.vdouble(100, 0, 5), 
            inputVariables = cms.vstring("rapidityDiff"),
        ),
        cms.PSet (
            name = cms.string("fatjetRelPtDiff"),
            title = cms.string("Relative p_{T} difference of leading jets; (p_{T1} - p_{T2}) / (p_{T1} + p_{T2})"),
            binsX = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("fatjetRelPtDiff"),
        ),
        cms.PSet (
            name = cms.string("minSqrtY"),
            title = cms.string("minimum #sqrt{y}; minimum #sqrt{y}"),
            binsX = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("minSqrtY"),
        ),
        cms.PSet (
            name = cms.string("maxSqrtY"),
            title = cms.string("maximum #sqrt{y}; maximum #sqrt{y}"),
            binsX = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("maxSqrtY"),
        ),
        cms.PSet (
            name = cms.string("fatjetMassMin"),
            title = cms.string("mass of lower-mass jet; jet mass [GeV]"), 
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("fatjetMassMin"),
        ),
        cms.PSet (
            name = cms.string("fatjetMassMax"),
            title = cms.string("mass of higher-mass jet; jet mass [GeV]"), 
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("fatjetMassMax"),
        ),
        cms.PSet (
            name = cms.string("invMassLeadingSubleading"),
            title = cms.string("invariant mass of leading and subleading jets; m_{jj} [GeV]"), 
            binsX = cms.untracked.vdouble(350, 0, 3500),
            inputVariables = cms.vstring("invMassLeadingSubleading"),
        ),
        cms.PSet (
            name = cms.string("chargedMultiplicityLeading"),
            title = cms.string("charged multiplicity of jet Leading; charged multiplicity of jet Leading"), 
            binsX = cms.untracked.vdouble(40, 0, 120),
            inputVariables = cms.vstring("chargedMultiplicityLeading"),
        ),
        cms.PSet (
            name = cms.string("chargedMultiplicitySubleading"),
            title = cms.string("charged multiplicity of jet Subleading; charged multiplicity of jet Subleading"), 
            binsX = cms.untracked.vdouble(40, 0, 120),
            inputVariables = cms.vstring("chargedMultiplicitySubleading"),
        ),
        cms.PSet (
            name = cms.string("getJetConstituentsSizeLeading"),
            title = cms.string("getJetConstituentsSizeLeading;getJetConstituentsSizeLeading"),
            binsX = cms.untracked.vdouble(50, 0, 50), 
            inputVariables = cms.vstring("getJetConstituentsSizeLeading"),
        ),
        cms.PSet (
            name = cms.string("getJetConstituentsSizeSubleading"),
            title = cms.string("getJetConstituentsSizeSubleading;getJetConstituentsSizeSubleading"),
            binsX = cms.untracked.vdouble(50, 0, 50), 
            inputVariables = cms.vstring("getJetConstituentsSizeSubleading"),
        ),
        cms.PSet (
            name = cms.string("eventVarMetPt"),
            title = cms.string("Met pt; MET"), 
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("metPt"),
        ),
        # cms.PSet (
        #     name = cms.string("nConstituentsByHandLeading"),
        #     title = cms.string("nConstituentsByHandLeading;nConstituentsByHandLeading"),
        #     binsX = cms.untracked.vdouble(50, 0, 50), 
        #     inputVariables = cms.vstring("nConstituentsByHandLeading"),
        # ),
        # cms.PSet (
        #     name = cms.string("nConstituentsByHandSubleading"),
        #     title = cms.string("nConstituentsByHandSubleading;nConstituentsByHandSubleading"),
        #     binsX = cms.untracked.vdouble(50, 0, 50), 
        #     inputVariables = cms.vstring("nConstituentsByHandSubleading"),
        # ),
    )
)


MyProtoHistograms = cms.PSet(
    # using "events" tells the code to pass the full event
    # to the special module to calculate the final quantity
    inputCollection = cms.string("userVariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("dimuonMetDeltaPhi"),
            title = cms.string("#Delta(#phi) of the dimuon-MET system; dimuon-MET #Delta(#phi)"),
            binsX = cms.untracked.vdouble(100, 0, 3.15),
            inputVariables = cms.vstring("dimuonMetDeltaPhi"),
        ),
        cms.PSet (
            name = cms.string("metPt"),
            title = cms.string("MET;MET [GeV];"),
            binsX = cms.untracked.vdouble(100, 0, 500),  
            inputVariables = cms.vstring("metPt"),
        ),
        cms.PSet (
            name = cms.string("diMuonInvMass"),
            title = cms.string("Di-muon Invariant Mass; M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("dimuonInvMass"),
        ),
    )
)


MyMetHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
        # cms.PSet (
        #     name = cms.string("metNum"),
        #     title = cms.string("Number of selected Mets; Number of selected Mets"),
        #     binsX = cms.untracked.vdouble(10, -0.5, 9.5),
        #     inputVariables = cms.vstring("number ( met )"),
        # ),
        cms.PSet (
            name = cms.string("metPt"),
            title = cms.string("Missing E_{T}; E_{T}^{miss} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        # cms.PSet (
        #     name = cms.string("metPhi"),
        #     title = cms.string("Phi of Missing E_{T}; #phi(E_{T}^{miss})"),
        #     binsX = cms.untracked.vdouble(100, -3.15, 3.15),
        #     inputVariables = cms.vstring("phi"),
        # ),
    )
)

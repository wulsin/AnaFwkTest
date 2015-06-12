#include "TLorentzVector.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "AnaFwkTest/Selection/plugins/AnaFwkTestSubjetVariableProducer.h"
#include "DataFormats/Math/interface/deltaR.h"

// For reference, see:
// https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideSubjetFilterJetProducer
// https://github.com/cms-sw/cmssw/blob/CMSSW_5_3_X/RecoJets/JetProducers/plugins/SubjetFilterJetProducer.h


AnaFwkTestSubjetVariableProducer::AnaFwkTestSubjetVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg) {}

AnaFwkTestSubjetVariableProducer::~AnaFwkTestSubjetVariableProducer() {}

void
AnaFwkTestSubjetVariableProducer::AddVariables (const edm::Event &event) {
#if DATA_FORMAT == AOD

  // Add all of the needed collections to objectsToGet_
  objectsToGet_.insert ("basicjets");  // these are the "fat jets"
  objectsToGet_.insert ("jets");       // these are the subjets  

  // get all the needed collections from the event and put them into the "handles_" collection
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);

  // calculate whatever variables you'd like


  //  cout << (*handles_.basicjets).at(0).subjets()).at(0).pt() << endl;
  //  cout << (*handles_.basicjets).at(0).getJetConstituents().at(0)->pt() << endl;

  int getJetConstituentsSizeLeading = -9;  
  int getJetConstituentsSizeSubleading = -9;  
  int nConstituentsByHandLeading       = -9;  
  int nConstituentsByHandSubleading    = -9;  


  double sqrtY0 = 0.0, sqrtY1 = 0.0;
  double invMassSubjets0 = 0.0, invMassSubjets1 = 0.0;  
  int chargedMultiplicityLeading = -9, chargedMultiplicitySubleading = -9;  
  if ((*handles_.basicjets).size() != 2) {
    cout << "ERROR:  number of basic jets should be exactly 2!  " << endl;
  } else {
    getJetConstituentsSizeLeading  = handles_.basicjets->at(0).getJetConstituents().size();  
    getJetConstituentsSizeSubleading  = handles_.basicjets->at(1).getJetConstituents().size();  
    nConstituentsByHandLeading        = handles_.basicjets->at(0).nConstituents();  
    nConstituentsByHandSubleading     = handles_.basicjets->at(1).nConstituents(); 


    if (handles_.basicjets->at (0).nConstituents () > 1)
      {
        pair<TLorentzVector, TLorentzVector> p;
        p.first.SetPtEtaPhiE (handles_.basicjets->at (0).getJetConstituents ().at (0)->pt (),
                              handles_.basicjets->at (0).getJetConstituents ().at (0)->eta (),
                              handles_.basicjets->at (0).getJetConstituents ().at (0)->phi (),
                              handles_.basicjets->at (0).getJetConstituents ().at (0)->energy ());
        p.second.SetPtEtaPhiE (handles_.basicjets->at (0).getJetConstituents ().at (1)->pt (),
                               handles_.basicjets->at (0).getJetConstituents ().at (1)->eta (),
                               handles_.basicjets->at (0).getJetConstituents ().at (1)->phi (),
                               handles_.basicjets->at (0).getJetConstituents ().at (1)->energy ());
	invMassSubjets0 = jetMass (handles_.basicjets->at (0)); 
        sqrtY0 = min<double> (p.first.Pt (), p.second.Pt ()) * (p.first.DeltaR (p.second) / jetMass (handles_.basicjets->at (0)));
	const reco::PFJet* subjet0 = findSubjet(handles_.jets, handles_.basicjets->at(0).getJetConstituents ().at(0)); 
	const reco::PFJet* subjet1 = findSubjet(handles_.jets, handles_.basicjets->at(0).getJetConstituents ().at(1)); 
	if (subjet0 && subjet1) {
	  chargedMultiplicityLeading = subjet0->chargedMultiplicity() + subjet1->chargedMultiplicity();  
	}
      }
    if (handles_.basicjets->at (1).nConstituents () > 1)
      {
        pair<TLorentzVector, TLorentzVector> p;
        p.first.SetPtEtaPhiE (handles_.basicjets->at (1).getJetConstituents ().at (0)->pt (),
                              handles_.basicjets->at (1).getJetConstituents ().at (0)->eta (),
                              handles_.basicjets->at (1).getJetConstituents ().at (0)->phi (),
                              handles_.basicjets->at (1).getJetConstituents ().at (0)->energy ());
        p.second.SetPtEtaPhiE (handles_.basicjets->at (1).getJetConstituents ().at (1)->pt (),
                               handles_.basicjets->at (1).getJetConstituents ().at (1)->eta (),
                               handles_.basicjets->at (1).getJetConstituents ().at (1)->phi (),
                               handles_.basicjets->at (1).getJetConstituents ().at (1)->energy ());
	invMassSubjets1 = jetMass (handles_.basicjets->at (1)); 
	sqrtY1 = min<double> (p.first.Pt (), p.second.Pt ()) * (p.first.DeltaR (p.second) / jetMass (handles_.basicjets->at (1)));
	const reco::PFJet* subjet0 = findSubjet(handles_.jets, handles_.basicjets->at(1).getJetConstituents ().at(0)); 
	const reco::PFJet* subjet1 = findSubjet(handles_.jets, handles_.basicjets->at(1).getJetConstituents ().at(1)); 
	if (subjet0 && subjet1) {
	  chargedMultiplicitySubleading = subjet0->chargedMultiplicity() + subjet1->chargedMultiplicity();  
	}
      }
  }
  
  (*eventvariables)["minSqrtY"] = min<double> (sqrtY0, sqrtY1);
  (*eventvariables)["maxSqrtY"] = max<double> (sqrtY0, sqrtY1);
  
  
  (*eventvariables)["basicjetMassMin"] = min<double> (invMassSubjets0, invMassSubjets1);  
  (*eventvariables)["basicjetMassMax"] = max<double> (invMassSubjets0, invMassSubjets1);  

  (*eventvariables)["chargedMultiplicityLeading"] = chargedMultiplicityLeading;  
  (*eventvariables)["chargedMultiplicitySubleading"] = chargedMultiplicitySubleading;  


  (*eventvariables)["getJetConstituentsSizeLeading"]  = getJetConstituentsSizeLeading;
  (*eventvariables)["getJetConstituentsSizeSubleading"]  = getJetConstituentsSizeSubleading;
  (*eventvariables)["nConstituentsByHandLeading"]     = nConstituentsByHandLeading;
  (*eventvariables)["nConstituentsByHandSubleading"]     = nConstituentsByHandSubleading;

#endif
}  

double
AnaFwkTestSubjetVariableProducer::jetMass (const reco::BasicJet &jet) const
{
#if DATA_FORMAT == AOD
  return (jet.getJetConstituents ().at (0)->p4 () + jet.getJetConstituents ().at (1)->p4 ()).M ();
#else
  return -1.0;
#endif
}

// Return the subjet closest to cand. 
// Follow algorithm used in const pat::Jet* SubjetFilterValidator::findPATJet()
// in http://cvs.web.cern.ch/cvs/cgi-bin/viewcvs.cgi/UserCode/SchieferD/SubjetFilterValidation/plugins/SubjetFilterValidator.cc?revision=1.3
const reco::PFJet* AnaFwkTestSubjetVariableProducer::findSubjet(const edm::Handle<reco::PFJetCollection>& subjets, const edm::Ptr<reco::Candidate>& cand) const 
{

  const reco::PFJet* result(0);
  double dRMin(1E+10);

  for (reco::PFJetCollection::const_iterator subjet = subjets->begin(); subjet != subjets->end(); ++subjet) { 
    double dR = reco::deltaR(*cand, *subjet);
    if (dR<dRMin) { 
      result = &(*subjet); 
      dRMin=dR; 
    }
  }
  if (dRMin>1E-05) cout<< "findSubjet WARNING: dRMin=" << dRMin
		       << " (pT=" << result->pt() << " / " << cand->pt() << ")" << endl;
  
  return result;

}
  



#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnaFwkTestSubjetVariableProducer);


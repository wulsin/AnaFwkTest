#include "TLorentzVector.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "AnaFwkTest/Selection/plugins/AnaFwkTestSubjetVariableProducer.h"
#include "DataFormats/Math/interface/deltaR.h"

// For reference, see:
// https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideSubjetFilterJetProducer
// https://github.com/cms-sw/cmssw/blob/CMSSW_5_3_X/RecoJets/JetProducers/plugins/SubjetFilterJetProducer.h


AnaFwkTestSubjetVariableProducer::AnaFwkTestSubjetVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  // Add all of the needed collections to objectsToGet_
  objectsToGet_.insert ("basicjets");  // these are the "fat jets"
  objectsToGet_.insert ("jets");       // these are the subjets  
  objectsToGet_.insert ("mets");     
}

AnaFwkTestSubjetVariableProducer::~AnaFwkTestSubjetVariableProducer() {}

void
AnaFwkTestSubjetVariableProducer::AddVariables (const edm::Event &event) {
#if DATA_FORMAT == MINI_AOD

  // get all the needed collections from the event and put them into the "handles_" collection
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);

  // calculate whatever variables you'd like

  (*eventvariables)["metPt"] = (*handles_.mets).at(0).pt();

  int getJetConstituentsSizeLeading = -9;  
  int getJetConstituentsSizeSubleading = -9;  
  int nConstituentsByHandLeading       = -9;  
  int nConstituentsByHandSubleading    = -9;  

  // kinematics of leading and subleading fatjets 
  // these quantities are calculated based on the subjets  
  // "leading" and "subleading" refer to the pt of the jets, not their mass  

  int chargedMultiplicityLeading = -99;
  int chargedMultiplicitySubleading = -99;  

  double sqrtY0 = 0.0, sqrtY1 = 0.0;
  TLorentzVector fatjetLeading, fatjetSubleading;  

  if (handles_.basicjets->size () > 0)
    {
      getJetConstituentsSizeLeading     = handles_.basicjets->at(0).getJetConstituents().size();  
      nConstituentsByHandLeading        = handles_.basicjets->at(0).nConstituents();  

      if (handles_.basicjets->at (0).nConstituents () > 1)
        {
          pair<TLorentzVector, TLorentzVector> subjetMomenta;
          const edm::Ptr<reco::Candidate> subjet0 = handles_.basicjets->at (0).getJetConstituents ().at (0);
          const edm::Ptr<reco::Candidate> subjet1 = handles_.basicjets->at (0).getJetConstituents ().at (1);
          subjetMomenta.first.SetPtEtaPhiE (subjet0->pt (), subjet0->eta (), subjet0->phi (), subjet0->energy ());
          subjetMomenta.second.SetPtEtaPhiE (subjet1->pt (), subjet1->eta (), subjet1->phi (), subjet1->energy ());
          sqrtY0 = min<double> (subjetMomenta.first.Pt (), subjetMomenta.second.Pt ()) * (subjetMomenta.first.DeltaR (subjetMomenta.second) / (subjetMomenta.first + subjetMomenta.second).M ());

          fatjetLeading.SetPtEtaPhiE (0.0, 0.0, 0.0, 0.0);
          chargedMultiplicityLeading = 0;
	  // consider the leading 3 filter jets
          for (int iFilterJet = 2; iFilterJet < min<int> (5, nConstituentsByHandLeading); iFilterJet++)
            {
              const edm::Ptr<reco::Candidate> constituent = handles_.basicjets->at (0).getJetConstituents ().at (iFilterJet);
              const pat::Jet *correctedConstituent = findSubjet (handles_.jets, *constituent);
              TLorentzVector p;
              p.SetPtEtaPhiE (correctedConstituent->pt (), correctedConstituent->eta (), correctedConstituent->phi (), correctedConstituent->energy ());
              fatjetLeading += p;

              chargedMultiplicityLeading += correctedConstituent->chargedMultiplicity ();
            }
        }
    }
  if (handles_.basicjets->size () > 1)
    {
      getJetConstituentsSizeSubleading     = handles_.basicjets->at(1).getJetConstituents().size();  
      nConstituentsByHandSubleading        = handles_.basicjets->at(1).nConstituents();  

      if (handles_.basicjets->at (1).nConstituents () > 1)
        {
          pair<TLorentzVector, TLorentzVector> subjetMomenta;
          const edm::Ptr<reco::Candidate> subjet0 = handles_.basicjets->at (1).getJetConstituents ().at (0);
          const edm::Ptr<reco::Candidate> subjet1 = handles_.basicjets->at (1).getJetConstituents ().at (1);
          subjetMomenta.first.SetPtEtaPhiE (subjet0->pt (), subjet0->eta (), subjet0->phi (), subjet0->energy ());
          subjetMomenta.second.SetPtEtaPhiE (subjet1->pt (), subjet1->eta (), subjet1->phi (), subjet1->energy ());
          sqrtY1 = min<double> (subjetMomenta.first.Pt (), subjetMomenta.second.Pt ()) * (subjetMomenta.first.DeltaR (subjetMomenta.second) / (subjetMomenta.first + subjetMomenta.second).M ());

          fatjetSubleading.SetPtEtaPhiE (0.0, 0.0, 0.0, 0.0);
          chargedMultiplicitySubleading = 0;
	  // consider the leading 3 filter jets
          for (int iFilterJet = 2; iFilterJet < min<int> (5, nConstituentsByHandSubleading); iFilterJet++)
            {
              const edm::Ptr<reco::Candidate> constituent = handles_.basicjets->at (1).getJetConstituents ().at (iFilterJet);
              const pat::Jet *correctedConstituent = findSubjet (handles_.jets, *constituent);
              TLorentzVector p;
              p.SetPtEtaPhiE (correctedConstituent->pt (), correctedConstituent->eta (), correctedConstituent->phi (), correctedConstituent->energy ());
              fatjetSubleading += p;

              chargedMultiplicitySubleading += correctedConstituent->chargedMultiplicity ();
            }
        }
    }
  

  (*eventvariables)["mLeading"] =                   fatjetLeading.M();   		 
  (*eventvariables)["mSubleading"] =   	            fatjetSubleading.M();		 
  (*eventvariables)["ptLeading"] =                  fatjetLeading.Pt();   		 
  (*eventvariables)["ptSubleading"] =   	    fatjetSubleading.Pt();		 
  (*eventvariables)["etaLeading"] =   		    fatjetLeading.Eta();   		 
  (*eventvariables)["etaSubleading"] =   	    fatjetSubleading.Eta();		 
  (*eventvariables)["phiLeading"] =   		    fatjetLeading.Phi();   		 
  (*eventvariables)["phiSubleading"] =   	    fatjetSubleading.Phi();		 
  (*eventvariables)["energyLeading"] =   	    fatjetLeading.E();   	 
  (*eventvariables)["energySubleading"] =   	    fatjetSubleading.E();	 
  (*eventvariables)["invMassLeadingSubleading"] =   (fatjetLeading + fatjetSubleading).M();  
  (*eventvariables)["rapidityDiff"]               = fatjetLeading.Rapidity() - fatjetSubleading.Rapidity();  

  double pt0 = fatjetLeading.Pt();
  double pt1 = fatjetSubleading.Pt();  
  (*eventvariables)["fatjetRelPtDiff"]            = (pt0 - pt1) / (pt0 + pt1); 

  (*eventvariables)["minSqrtY"] = min<double> (sqrtY0, sqrtY1);
  (*eventvariables)["maxSqrtY"] = max<double> (sqrtY0, sqrtY1);
    
  (*eventvariables)["fatjetMassMin"] = min<double> (fatjetLeading.M(), fatjetSubleading.M());  
  (*eventvariables)["fatjetMassMax"] = max<double> (fatjetLeading.M(), fatjetSubleading.M());  

  (*eventvariables)["chargedMultiplicityLeading"]    = chargedMultiplicityLeading;  
  (*eventvariables)["chargedMultiplicitySubleading"] = chargedMultiplicitySubleading;  

  (*eventvariables)["getJetConstituentsSizeLeading"]     = getJetConstituentsSizeLeading;
  (*eventvariables)["getJetConstituentsSizeSubleading"]  = getJetConstituentsSizeSubleading;
  (*eventvariables)["nConstituentsByHandLeading"]        = nConstituentsByHandLeading;
  (*eventvariables)["nConstituentsByHandSubleading"]     = nConstituentsByHandSubleading;

#endif
}  

// Return the subjet closest to cand. 
// Follow algorithm used in const pat::Jet* SubjetFilterValidator::findPATJet()
// in http://cvs.web.cern.ch/cvs/cgi-bin/viewcvs.cgi/UserCode/SchieferD/SubjetFilterValidation/plugins/SubjetFilterValidator.cc?revision=1.3
const pat::Jet *AnaFwkTestSubjetVariableProducer::findSubjet(const edm::Handle<vector<pat::Jet> >& subjets, const reco::Candidate &cand) const 
{

  const pat::Jet* result(0);
  double dRMin(1E+10);

  for (vector<pat::Jet>::const_iterator subjet = subjets->begin(); subjet != subjets->end(); ++subjet) { 
    double dR = reco::deltaR(cand, *subjet);
    if (dR<dRMin) { 
      result = &(*subjet); 
      dRMin=dR; 
    }
  }
  if (dRMin>1E-05) cout<< "findSubjet WARNING: dRMin=" << dRMin
                       << " (pT=" << result->pt() << " / " << cand.pt() << ")" << endl;
  
  return result;

}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnaFwkTestSubjetVariableProducer);


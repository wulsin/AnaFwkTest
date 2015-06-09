#include "TLorentzVector.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "AnaFwkTest/Selection/plugins/AnaFwkTestSubjetVariableProducer.h"
#include "DataFormats/Math/interface/deltaR.h"

AnaFwkTestSubjetVariableProducer::AnaFwkTestSubjetVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg) {}

AnaFwkTestSubjetVariableProducer::~AnaFwkTestSubjetVariableProducer() {}

void
AnaFwkTestSubjetVariableProducer::AddVariables (const edm::Event &event) {

  // Add all of the needed collections to objectsToGet_
  objectsToGet_.insert ("basicjets");

  // get all the needed collections from the event and put them into the "handles_" collection
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);

  // calculate whatever variables you'd like


  //  cout << (*handles_.basicjets).at(0).subjets()).at(0).pt() << endl;
  //  cout << (*handles_.basicjets).at(0).getJetConstituents().at(0)->pt() << endl;

  double sqrtY0 = 0.0, sqrtY1 = 0.0;
  if ((*handles_.basicjets).size() != 2) {
    cout << "ERROR:  number of basic jets should be exactly 2!  " << endl;
  } 
  else {
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
        sqrtY0 = min<double> (p.first.Pt (), p.second.Pt ()) * (p.first.DeltaR (p.second) / jetMass (handles_.basicjets->at (0)));
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
        sqrtY1 = min<double> (p.first.Pt (), p.second.Pt ()) * (p.first.DeltaR (p.second) / jetMass (handles_.basicjets->at (1)));
      }
  }

  (*eventvariables)["minSqrtY"] = min<double> (sqrtY0, sqrtY1);
  (*eventvariables)["maxSqrtY"] = max<double> (sqrtY0, sqrtY1);

}  

double
AnaFwkTestSubjetVariableProducer::jetMass (const reco::BasicJet &jet) const
{
  return (jet.getJetConstituents ().at (0)->p4 () + jet.getJetConstituents ().at (1)->p4 ()).M ();
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnaFwkTestSubjetVariableProducer);

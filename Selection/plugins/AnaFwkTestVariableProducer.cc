#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "AnaFwkTest/Selection/plugins/AnaFwkTestVariableProducer.h"

AnaFwkTestVariableProducer::AnaFwkTestVariableProducer(const edm::ParameterSet &cfg) :
  VariableProducer(cfg) {}

AnaFwkTestVariableProducer::~AnaFwkTestVariableProducer() {}

void
AnaFwkTestVariableProducer::AddVariables (const edm::Event &event) {

  // Add all of the needed collections to objectsToGet_
  objectsToGet_.insert ("muons");
  objectsToGet_.insert ("basicjets");

  // get all the needed collections from the event and put them into the "handles_" collection
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);

  // calculate whatever variables you'd like

  // simple case, just muonPt
  for (const auto &muon1 : *handles_.muons) {
    double value = anatools::getMember(muon1, "pt");
    addUserVar("muonPt", value, muon1);
  }

  // calculate relative pt difference
  // There should be only 2 leading basicjets. 
  if ((*handles_.basicjets).size() != 2) {
    cout << "ERROR:  number of basic jets should be exactly 2!  " << endl;  
  } else {
    double pt1 = (*handles_.basicjets).at(0).pt();  
    double pt2 = (*handles_.basicjets).at(1).pt();  
    double relPtDiff = (pt1 - pt2) / (pt1 + pt2);  
    addUserVar("basicjetRelPtDiff", relPtDiff, (*handles_.basicjets).at(0), (*handles_.basicjets).at(1));  
  }

}  

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnaFwkTestVariableProducer);

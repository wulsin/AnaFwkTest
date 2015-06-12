#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "AnaFwkTest/Selection/plugins/AnaFwkTestEventVariableProducer.h"

AnaFwkTestEventVariableProducer::AnaFwkTestEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg) {}

AnaFwkTestEventVariableProducer::~AnaFwkTestEventVariableProducer() {}

void
AnaFwkTestEventVariableProducer::AddVariables (const edm::Event &event) {
#if DATA_FORMAT == AOD

  // Add all of the needed collections to objectsToGet_
  objectsToGet_.insert ("mets");

  // get all the needed collections from the event and put them into the "handles_" collection
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);

  // calculate whatever variables you'd like

  (*eventvariables)["metPt"] = (*handles_.mets).at(0).pt();

  //  cout << "Debug:  added event variable:  metPt = " <<  (*eventvariables)["metPt"] << endl;  

#endif
}  

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnaFwkTestEventVariableProducer);

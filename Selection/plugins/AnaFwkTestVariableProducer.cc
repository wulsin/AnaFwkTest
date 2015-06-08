#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "AnaFwkTest/Selection/plugins/AnaFwkTestVariableProducer.h"

AnaFwkTestVariableProducer::AnaFwkTestVariableProducer(const edm::ParameterSet &cfg) :
  VariableProducer(cfg) {}

AnaFwkTestVariableProducer::~AnaFwkTestVariableProducer() {}

void
AnaFwkTestVariableProducer::AddVariables (const edm::Event &event) {

  // Add all of the needed collections to objectsToGet_
  objectsToGet_.insert ("muons");

  // get all the needed collections from the event and put them into the "handles_" collection
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);

  // calculate whatever variables you'd like

  // simple case, just muonPt
  for (const auto &muon1 : *handles_.muons) {
    double value = anatools::getMember(muon1, "pt");
    addUserVar("muonPt", value, muon1);
  }

}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnaFwkTestVariableProducer);

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

  if ((*handles_.basicjets).size() != 2) {
    cout << "ERROR:  number of basic jets should be exactly 2!  " << endl;
  } 
  else {
    if ((*handles_.basicjets).at(0).getJetConstituents().size() >= 2) {
      double subjet1pt = (*(*handles_.basicjets).at(0).getJetConstituents().at(0)).pt();
      double subjet2pt = (*(*handles_.basicjets).at(0).getJetConstituents().at(1)).pt();
      double mass = (*handles_.basicjets).at(0).mass();
      //FIXME: start from here
      //      double deltaR = 
    }


    //    (*eventvariables)["jet1nsubjets"] = (*handles_.basicjets).at(0).getJetConstituents().size();

  }

}  

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnaFwkTestSubjetVariableProducer);

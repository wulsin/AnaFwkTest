#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "AnaFwkTest/Selection/plugins/AnaFwkTestEventVariableProducer.h"

AnaFwkTestEventVariableProducer::AnaFwkTestEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg) {}

AnaFwkTestEventVariableProducer::~AnaFwkTestEventVariableProducer() {}

void
AnaFwkTestEventVariableProducer::AddVariables (const edm::Event &event) {

  // Add all of the needed collections to objectsToGet_
  objectsToGet_.insert ("mets");
  objectsToGet_.insert ("basicjets");

  // get all the needed collections from the event and put them into the "handles_" collection
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);

  // calculate whatever variables you'd like

  (*eventvariables)["metPt"] = (*handles_.mets).at(0).pt();

  // calculate relative pt difference
  // There should be only 2 leading basicjets. 
  if ((*handles_.basicjets).size() != 2) {
    cout << "ERROR:  number of basic jets should be exactly 2!  " << endl;  
  } else {
    double pt1 = (*handles_.basicjets).at(0).pt();  
    double pt2 = (*handles_.basicjets).at(1).pt();  
    double relPtDiff = (pt1 - pt2) / (pt1 + pt2);  
    (*eventvariables)["basicjetRelPtDiff"] = relPtDiff;

    double m1 = (*handles_.basicjets).at(0).mass();  
    double m2 = (*handles_.basicjets).at(1).mass();  
    double mhi, mlo;  
    if (m1 > m2) {
      mhi = m1;
      mlo = m2;
    } else {
      mhi = m2;
      mlo = m1;
    }  
    (*eventvariables)["basicjetMassHi"] = mhi;  
    (*eventvariables)["basicjetMassLo"] = mlo;  

  }

  //  cout << "Debug:  added event variable:  metPt = " <<  (*eventvariables)["metPt"] << endl;  

}  

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnaFwkTestEventVariableProducer);

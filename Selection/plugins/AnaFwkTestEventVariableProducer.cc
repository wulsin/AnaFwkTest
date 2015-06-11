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
  objectsToGet_.insert ("basicjets");

  // get all the needed collections from the event and put them into the "handles_" collection
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);

  // calculate whatever variables you'd like

  (*eventvariables)["metPt"] = (*handles_.mets).at(0).pt();

  // There should be only 2 leading basicjets. 
  if ((*handles_.basicjets).size() != 2) {
    cout << "ERROR:  number of basic jets should be exactly 2!  " << endl;  
  } else {


    // Calculate relative pt difference
    double pt1 = (*handles_.basicjets).at(0).pt();  
    double pt2 = (*handles_.basicjets).at(1).pt();  
    double relPtDiff = (pt1 - pt2) / (pt1 + pt2);  
    (*eventvariables)["basicjetRelPtDiff"] = relPtDiff;

    // Calculate mass of upper and lower jets.  
    double m1 = (*handles_.basicjets).at(0).mass();  
    double m2 = (*handles_.basicjets).at(1).mass();  
    // differentiate from basicjetMassMin, which is the mass of the two leading subjets  
    (*eventvariables)["basicjetMassFuncCallMin"] = min<double> (m1, m2);   
    (*eventvariables)["basicjetMassFuncCallMax"] = max<double> (m1, m2); 

    // Calculate number of charged consituents.  
    int nConst1 = 0;
    int nConst2 = 0;
    int nConstChgd1 = 0;
    int nConstChgd2 = 0;
    for (const auto &constit : (*handles_.basicjets).at(0).getJetConstituents()) {
      nConst1++;  
      if (constit->charge() != 0) {
	nConstChgd1++;  
      }
    }
    (*eventvariables)["basicjetNConst1"] = nConst1; 
    (*eventvariables)["basicjetNConst2"] = nConst2; 
    (*eventvariables)["basicjetNConstChgd1"] = nConstChgd1; 
    (*eventvariables)["basicjetNConstChgd2"] = nConstChgd2; 

  }

  //  cout << "Debug:  added event variable:  metPt = " <<  (*eventvariables)["metPt"] << endl;  

#endif
}  

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AnaFwkTestEventVariableProducer);

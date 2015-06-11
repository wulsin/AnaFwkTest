#ifndef ANAFWKTEST_SUBJET_VARIABLE_PRODUCER
#define ANAFWKTEST_SUBJET_VARIABLE_PRODUCER

#include "DataFormats/Candidate/interface/Candidate.h"  
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"

class AnaFwkTestSubjetVariableProducer : public EventVariableProducer
  {
    public:
        AnaFwkTestSubjetVariableProducer (const edm::ParameterSet &);
	~AnaFwkTestSubjetVariableProducer ();

    private:

	// Functions
	void AddVariables(const edm::Event &);
        double jetMass (const reco::BasicJet &) const;
        const reco::PFJet* findSubjet(const edm::Handle<reco::PFJetCollection>& subjets, const edm::Ptr<reco::Candidate>& cand) const; 
  };

#endif

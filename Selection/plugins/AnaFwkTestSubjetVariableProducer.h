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
        const reco::PFJet* findSubjet(const edm::Handle<reco::PFJetCollection>&, const reco::PFJet &) const;
  };

#endif

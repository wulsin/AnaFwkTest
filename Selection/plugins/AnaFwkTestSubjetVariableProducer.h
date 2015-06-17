#ifndef ANAFWKTEST_SUBJET_VARIABLE_PRODUCER
#define ANAFWKTEST_SUBJET_VARIABLE_PRODUCER

#include "DataFormats/Candidate/interface/Candidate.h"  
#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

class AnaFwkTestSubjetVariableProducer : public EventVariableProducer
  {
    public:
        AnaFwkTestSubjetVariableProducer (const edm::ParameterSet &);
	~AnaFwkTestSubjetVariableProducer ();

    private:

	// Functions
	void AddVariables(const edm::Event &);
        const pat::Jet &findSubjet(const edm::Handle<vector<pat::Jet> >&, const reco::Candidate &) const;
  };

#endif

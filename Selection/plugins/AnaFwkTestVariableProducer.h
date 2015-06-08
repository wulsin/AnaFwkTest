#ifndef ANAFWKTEST_VARIABLE_PRODUCER
#define ANAFWKTEST_VARIABLE_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/VariableProducer.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/deltaPhi.h"

class AnaFwkTestVariableProducer : public VariableProducer
  {
    public:
        AnaFwkTestVariableProducer (const edm::ParameterSet &);
	~AnaFwkTestVariableProducer ();

    private:

	// Functions
	void AddVariables(const edm::Event &);
  };

#endif

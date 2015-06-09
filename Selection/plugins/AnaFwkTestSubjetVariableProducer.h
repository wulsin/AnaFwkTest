#ifndef ANAFWKTEST_SUBJET_VARIABLE_PRODUCER
#define ANAFWKTEST_SUBJET_VARIABLE_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"

class AnaFwkTestSubjetVariableProducer : public EventVariableProducer
  {
    public:
        AnaFwkTestSubjetVariableProducer (const edm::ParameterSet &);
	~AnaFwkTestSubjetVariableProducer ();

    private:

	// Functions
	void AddVariables(const edm::Event &);
  };

#endif

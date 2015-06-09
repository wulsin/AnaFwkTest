#ifndef ANAFWKTEST_EVENT_VARIABLE_PRODUCER
#define ANAFWKTEST_EVENT_VARIABLE_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"

class AnaFwkTestEventVariableProducer : public EventVariableProducer
  {
    public:
        AnaFwkTestEventVariableProducer (const edm::ParameterSet &);
	~AnaFwkTestEventVariableProducer ();

    private:

	// Functions
	void AddVariables(const edm::Event &);
  };

#endif

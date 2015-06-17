#ifndef MY_ANALYZER

#define MY_ANALYZER

#include <string>
#include <vector>

#include "DataFormats/Common/interface/Handle.h"

#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

using namespace std;

template<class T>
class LeadingFat : public edm::EDProducer
{
 public:
  LeadingFat (const edm::ParameterSet &);
  virtual ~LeadingFat ();
  void produce (edm::Event &, const edm::EventSetup &);

  static bool jetPtDescending (const T *, const T *);

 private:
  edm::InputTag fats_;
};

#endif

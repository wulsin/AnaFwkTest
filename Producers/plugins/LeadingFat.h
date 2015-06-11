#ifndef MY_ANALYZER

#define MY_ANALYZER

#include <string>
#include <vector>

#include "DataFormats/Common/interface/Handle.h"

#include "DataFormats/JetReco/interface/BasicJet.h"

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

using namespace std;

class LeadingFat : public edm::EDProducer
{
 public:
  LeadingFat (const edm::ParameterSet &);
  virtual ~LeadingFat ();
  void produce (edm::Event &, const edm::EventSetup &);

  static bool jetPtDescending (const reco::BasicJet *, const reco::BasicJet *);

 private:
  edm::InputTag fats_;
};

#endif

#ifndef MY_ANALYZER

#define MY_ANALYZER

#include <string>
#include <vector>

#include "TDatabasePDG.h"
#include "TParticlePDG.h"

#include "DataFormats/Common/interface/Handle.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

using namespace std;

class HighPtZ : public edm::EDFilter
{
 public:
  HighPtZ (const edm::ParameterSet &);
  virtual ~HighPtZ ();
  bool filter (edm::Event &, const edm::EventSetup &);

 private:
  edm::InputTag genParticles_;
  TDatabasePDG pdg_;
  TParticlePDG *zBoson_;
};

#endif

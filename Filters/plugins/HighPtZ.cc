#include "AnaFwkTest/Filters/plugins/HighPtZ.h"

HighPtZ::HighPtZ (const edm::ParameterSet &cfg) :
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles"))
{
  zBoson_ = pdg_.GetParticle (23);
}

HighPtZ::~HighPtZ ()
{
}

bool
HighPtZ::filter (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);

  for (const auto &genParticle : *genParticles)
    {
      if (genParticle.status () != 3)
        break;
      if (abs (genParticle.pdgId ()) != 23)
        continue;
      if (genParticle.pt () < (zBoson_->Mass () / 0.5))
        continue;
      return true;
    }
  return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(HighPtZ);

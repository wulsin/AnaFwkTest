#include "AnaFwkTest/Producers/plugins/LeadingFat.h"

LeadingFat::LeadingFat (const edm::ParameterSet &cfg) :
  fats_ (cfg.getParameter<edm::InputTag> ("fats"))
{
  produces<vector<reco::BasicJet> > ("leadingFat");
}

LeadingFat::~LeadingFat ()
{
}

void
LeadingFat::produce (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::BasicJet> > fats;
  event.getByLabel (fats_, fats);

  vector<const reco::BasicJet *> selectedFats;
  for (const auto &fat : *fats)
    {
      if (fabs (fat.eta ()) > 2.0)
        continue;
      selectedFats.push_back (&fat);
    }
  sort (selectedFats.begin (), selectedFats.end (), jetPtDescending);

  auto_ptr<vector<reco::BasicJet> > leadingFats (new vector<reco::BasicJet> ());
  if (selectedFats.size () > 0)
    leadingFats->push_back (*selectedFats.at (0));
  if (selectedFats.size () > 1)
    leadingFats->push_back (*selectedFats.at (1));
  event.put (leadingFats, "leadingFat");
  leadingFats.reset ();
}

bool
LeadingFat::jetPtDescending (const reco::BasicJet *jet0, const reco::BasicJet *jet1)
{
  return (jet0->pt () > jet1->pt ());
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(LeadingFat);

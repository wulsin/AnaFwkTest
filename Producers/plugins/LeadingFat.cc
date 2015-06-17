#include "AnaFwkTest/Producers/plugins/LeadingFat.h"

template<class T>
LeadingFat<T>::LeadingFat (const edm::ParameterSet &cfg) :
  fats_ (cfg.getParameter<edm::InputTag> ("fats"))
{
  produces<vector<T> > ("leadingFat");
}

template<class T>
LeadingFat<T>::~LeadingFat ()
{
}

template<class T> void
LeadingFat<T>::produce (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<T> > fats;
  event.getByLabel (fats_, fats);

  vector<const T *> selectedFats;
  for (const auto &fat : *fats)
    {
      if (fabs (fat.eta ()) > 2.0)
        continue;
      selectedFats.push_back (&fat);
    }
  sort (selectedFats.begin (), selectedFats.end (), jetPtDescending);

  auto_ptr<vector<T> > leadingFats (new vector<T> ());
  if (selectedFats.size () > 0)
    leadingFats->push_back (*selectedFats.at (0));
  if (selectedFats.size () > 1)
    leadingFats->push_back (*selectedFats.at (1));
  event.put (leadingFats, "leadingFat");
  leadingFats.reset ();
}

template<class T> bool
LeadingFat<T>::jetPtDescending (const T *jet0, const T *jet1)
{
  return (jet0->pt () > jet1->pt ());
}

typedef LeadingFat<reco::BasicJet> LeadingFatBasicJet;
typedef LeadingFat<pat::Jet> LeadingFatPatJet;

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(LeadingFatBasicJet);
DEFINE_FWK_MODULE(LeadingFatPatJet);

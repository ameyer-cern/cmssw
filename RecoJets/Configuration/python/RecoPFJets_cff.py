import FWCore.ParameterSet.Config as cms

from RecoJets.JetProducers.sc5PFJets_cfi import sisCone5PFJets
from RecoJets.JetProducers.ic5PFJets_cfi import iterativeCone5PFJets
from RecoJets.JetProducers.ak5PFJets_cfi import ak5PFJets
from RecoJets.JetProducers.gk5PFJets_cfi import gk5PFJets
from RecoJets.JetProducers.kt4PFJets_cfi import kt4PFJets
from RecoJets.JetProducers.ca4PFJets_cfi import ca4PFJets


sisCone7PFJets = sisCone5PFJets.clone( rParam = 0.7 )
ak7PFJets = ak5PFJets.clone( rParam = 0.7 )
gk7PFJets = gk5PFJets.clone( rParam = 0.7 )
kt6PFJets = kt4PFJets.clone( rParam = 0.6 )
ca6PFJets = ca4PFJets.clone( rParam = 0.6 )

#compute areas for Fastjet PU subtraction  
kt6PFJets.doRhoFastjet = True
kt6PFJets.doAreaFastjet = True
#use active areas and not Voronoi tessellation for the moment
#kt6PFJets.voronoiRfact = 0.9
ak5PFJets.doAreaFastjet = True
ak7PFJets.doAreaFastjet = True

kt6PFJetsCentralChargedPileUp = kt6PFJets.clone(
    src = cms.InputTag("pfPileUpAllChargedParticles"),
    Ghost_EtaMax = cms.double(3.1),
    Rho_EtaMax = cms.double(2.5)
    )

kt6PFJetsCentralNeutral = kt6PFJets.clone(
    src = cms.InputTag("pfAllNeutralHadronsAndPhotons"),
    Ghost_EtaMax = cms.double(3.1),
    Rho_EtaMax = cms.double(2.5)
    )


recoPFJets   =cms.Sequence(kt4PFJets+kt6PFJets+kt6PFJetsCentralChargedPileUp+kt6PFJetsCentralNeutral+
                           iterativeCone5PFJets+
                           ak5PFJets+ak7PFJets)

recoAllPFJets=cms.Sequence(sisCone5PFJets+sisCone7PFJets+
                           kt4PFJets+kt6PFJets+kt6PFJetsCentralChargedPileUp+kt6PFJetsCentralNeutral+
                           iterativeCone5PFJets+
                           ak5PFJets+ak7PFJets+
                           gk5PFJets+gk7PFJets+
                           ca4PFJets+ca6PFJets)

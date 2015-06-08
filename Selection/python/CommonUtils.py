# Common values or utilities

# Masses used in ATLAS paper  
massW = 82.4 
massZ = 92.8  

# Old electron ID:  
# electronID = "(pt > 7 && pt < 10                                  \
# && ((abs (scEta) < 0.8 && mvaNonTrigV0 > 0.47)    \
# || (abs (scEta) >= 0.8 && abs (scEta) < 1.479 && mvaNonTrigV0 > 0.004) \
# || (abs (scEta) >= 1.479 && abs (scEta) < 2.5 && mvaNonTrigV0 > 0.295))) \
# || (pt >= 10                                           \
# && ((abs (scEta) < 0.8 && mvaNonTrigV0 > -0.34)   \
# || (abs (scEta) >= 0.8 && abs (scEta) < 1.479 && mvaNonTrigV0 > -0.65) \
# || (abs (scEta) >= 1.479 && abs (scEta) < 2.5 && mvaNonTrigV0 > 0.60)))  \
# "

# Revised electron ID:  
# Not sure how to access these variables that were in the BEANs:
#  MyElectron.mvaNonTrigV0 = ele->electronID("mvaNonTrigV0");
#  MyElectron.scEta = ele->superCluster()->position().eta();  
electronID = "(pt > 7 && pt < 10                                  \
&& ((abs (scEta) < 0.8 && mvaNonTrigV0 > 0.47)    \
|| (abs (scEta) >= 0.8 && abs (scEta) < 1.479 && mvaNonTrigV0 > 0.004) \
|| (abs (scEta) >= 1.479 && abs (scEta) < 2.5 && mvaNonTrigV0 > 0.295))) \
|| (pt >= 10                                           \
&& ((abs (scEta) < 0.8 && mvaNonTrigV0 > -0.34)   \
|| (abs (scEta) >= 0.8 && abs (scEta) < 1.479 && mvaNonTrigV0 > -0.65) \
|| (abs (scEta) >= 1.479 && abs (scEta) < 2.5 && mvaNonTrigV0 > 0.60)))  \
"



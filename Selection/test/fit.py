#!/usr/bin/env python

# Fits a bkgd function to the m_jj distribution. 
# Adapted from fitExpo.py.  

# Sample usage:
# $ fit.py 

from optparse import OptionParser

parser = OptionParser()
# Options have been deprecated; the desired configuration has been hard-coded.
# parser.add_option("-i", "--infile", dest="infile",
#                                     help="input root file")
# parser.add_option("-n", "--histName", dest="histName",
#                                     help="histogram name")
# parser.add_option("-b", "--rebin", dest="rebinFactor",
#                   help="Rebin the histogram")  
# parser.add_option("-o", "--outfile", dest="outfile",
#                   help="output pdf name (optional)")
# parser.add_option("--lo", dest="lo", default=1050, 
#                   help="Lo limit of fit range")  
# parser.add_option("--hi", dest="hi", default=3550, 
#                   help="Hi limit of fit range")  
parser.add_option("--nobatch", action="store_true", dest="nobatch", default=False,
                  help="do not run in batch mode")   
(arguments, args) = parser.parse_args()

import ROOT  
from ROOT import TFile, TH1F, TCanvas, TF1, TPaveLabel, TStyle, gROOT, TColor  

if not arguments.nobatch: 
    ROOT.gROOT.SetBatch(True)  # To prevent pop-up of canvas  

condorSearch = "20150630_searchChannels"
condorCtrl   = "20150626_extendedMass"
histBaseName = "Eventvariable Plots/invMassLeadingSubleadingATLASBinning"  

def setHistStyle(hist):
    hist.SetLineColor(1)
    hist.SetMarkerStyle(8)
    hist.SetMarkerSize(1)

# Take bkgd function from eqn (1) of arXiv:1506.00962
# x = m_jj
def bkgd(x, par):
    X = x[0] / 8000 # m_jj / sqrt(s)
    xi = 4.0  # hard coded based on values in Table 6  
    return par[0] * pow(1.0 - X, par[1] - xi * par[2]) * pow(X, par[2])  



# if arguments.rebinFactor:
#     hist.Rebin(int(arguments.rebinFactor))

ROOT.gStyle.SetOptStat(1111111)
ROOT.gStyle.SetOptFit(1111)
outfileRoot = "condor/" + condorSearch + "/fit.root"
outfilePdf = outfileRoot.replace(".root", ".pdf")  

# lo = hist.GetBinLowEdge(1)  
# hi = hist.GetBinLowEdge(hist.GetNbinsX()+1)
# if arguments.lo:  
#     lo = float(arguments.lo)  
# if arguments.hi:  
#     hi = float(arguments.hi)  
lo = 1050
hi = 3550 
can = TCanvas()  
can.SetLogy(1)  

myfunc = TF1("myfunc", bkgd, lo, hi, 3)  
can.Print(outfilePdf + "[")



#################
# Control region Channel
#################
inputFileSearch = TFile("condor/" + condorCtrl + "/JetHTData.root", "READ")
hist = inputFileSearch.Get("ExtendedMassChannelPlotter/" + histBaseName).Clone()
if not hist:
    print "Could not find TH1 " + arguments.histName + " in " + inputFile    
myfunc.SetParameter(0, 500)
myfunc.SetParameter(1, 31.)
myfunc.SetParameter(2, -3.0)
hist.GetXaxis().SetRangeUser(1050, 3500)
hist.SetMinimum(1)
hist.SetMaximum(1e6)
hist.Fit("myfunc", "R")   # Fit in range  
hist.SetTitle("Boson mass sideband channel: " + hist.GetTitle())
setHistStyle(hist)
hist.Draw("pe")   
myfunc.Draw("same")
can.Print(outfilePdf)


#################
# Preselection Channel
#################
inputFileSearch = TFile("condor/" + condorSearch + "/JetHTData.root", "READ")
hist = inputFileSearch.Get("PreselectionChannelPlotter/" + histBaseName).Clone()
if not hist:
    print "Could not find TH1 " + arguments.histName + " in " + inputFile    
myfunc.SetParameter(0, 500)
myfunc.SetParameter(1, 31.)
myfunc.SetParameter(2, -3.0)
hist.GetXaxis().SetRangeUser(1050, 3500)
hist.SetMinimum(1)
hist.SetMaximum(1e6)
hist.Fit("myfunc", "R")   # Fit in range  
hist.SetTitle("Preselection channel: " + hist.GetTitle())
setHistStyle(hist)
hist.Draw("pe")   
myfunc.Draw("same")
can.Print(outfilePdf)


#################
# WW Channel
#################
inputFileSearch = TFile("condor/" + condorSearch + "/JetHTData.root", "READ")
hist = inputFileSearch.Get("WWChannelPlotter/" + histBaseName).Clone()
if not hist:
    print "Could not find TH1 " + arguments.histName + " in " + inputFile    

#outputFile = TFile(outfileRoot, "RECREATE")
myfunc.SetParameter(0, 500)
myfunc.SetParameter(1, 31.)
myfunc.SetParameter(2, -3.0)
hist.Fit("myfunc", "R")   # Fit in range  
hist.GetXaxis().SetRangeUser(1050, 3500)
hist.SetMinimum(0.1)
hist.SetMaximum(1e5)
hist.SetTitle("WW channel: " + hist.GetTitle())
setHistStyle(hist)
hist.Draw("pe")   
myfunc.SetLineColor(2)  
myfunc.Draw("same")
#hist.Write()
#can.Write()
#can.SaveAs(outfilePdf + "[")
can.Print(outfilePdf)

#################
# WZ Channel
#################
inputFileSearch = TFile("condor/" + condorSearch + "/JetHTData.root", "READ")
hist = inputFileSearch.Get("WZChannelPlotter/" + histBaseName).Clone()
if not hist:
    print "Could not find TH1 " + arguments.histName + " in " + inputFile    
myfunc.SetParameter(0, 500)
myfunc.SetParameter(1, 31.)
myfunc.SetParameter(2, -3.0)
hist.GetXaxis().SetRangeUser(1050, 3500)
hist.SetMinimum(0.1)
hist.SetMaximum(1e5)
hist.Fit("myfunc", "R")   # Fit in range  
hist.SetTitle("WZ channel: " + hist.GetTitle())
setHistStyle(hist)
hist.Draw("pe")   
myfunc.Draw("same")
can.Print(outfilePdf)

#################
# ZZ Channel
#################
inputFileSearch = TFile("condor/" + condorSearch + "/JetHTData.root", "READ")
hist = inputFileSearch.Get("ZZChannelPlotter/" + histBaseName).Clone()
if not hist:
    print "Could not find TH1 " + arguments.histName + " in " + inputFile    
myfunc.SetParameter(0, 500)
myfunc.SetParameter(1, 31.)
myfunc.SetParameter(2, -3.0)
hist.GetXaxis().SetRangeUser(1050, 3500)
hist.SetMinimum(0.1)
hist.SetMaximum(1e5)
hist.Fit("myfunc", "R")   # Fit in range  
hist.SetTitle("ZZ channel: " + hist.GetTitle())
setHistStyle(hist)
hist.Draw("pe")   
myfunc.Draw("same")
can.Print(outfilePdf)


can.Print(outfilePdf + "]")
#outputFile.Close() 
print "Saved plot in " + outfilePdf + " and " + outfileRoot  

print "Finished fit.py"  








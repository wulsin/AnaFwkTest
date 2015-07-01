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
from ROOT import TFile, TH1F, TCanvas, TF1, TPaveLabel, TStyle, gROOT, TColor, THStack, TLegend, TPaveText

if not arguments.nobatch:
    ROOT.gROOT.SetBatch(True)  # To prevent pop-up of canvas

condorSearch = "20150630_searchChannels"
condorCtrl   = "20150626_extendedMass"
histBaseName = "Eventvariable Plots/invMassLeadingSubleadingATLASBinning"
combineCMSAndATLAS = True

def setStackStyle(stack,hist):
    stack.GetXaxis().SetLabelSize(0.04)
    stack.GetXaxis().SetTitleSize(0.04)
    stack.GetXaxis().SetTitleOffset(1.2)
    stack.GetXaxis().SetRangeUser(1050, 3550)
    stack.GetXaxis().SetTitle(hist.GetXaxis().GetTitle())

    stack.GetYaxis().SetLabelSize(0.04)
    stack.GetYaxis().SetTitleSize(0.04)
    stack.GetYaxis().SetTitleOffset(1.5)
    stack.GetYaxis().SetNdivisions(505)
    stack.GetYaxis().SetTitle(hist.GetYaxis().GetTitle())

    stack.SetMinimum(5.0e-4)
    stack.SetMaximum(1.0e4)

def setHistStyle(hist):
    hist.SetMarkerStyle(20)
    hist.SetLineStyle(1)
    hist.SetMarkerSize(1.5)
    hist.SetLineWidth(1)
    hist.SetMarkerColor(1)
    hist.SetLineColor(1)

    hist.GetXaxis().SetLabelSize(0.04)
    hist.GetXaxis().SetTitleSize(0.04)
    hist.GetXaxis().SetTitleOffset(1.2)
    hist.GetXaxis().SetRangeUser(1050, 3550)

    hist.GetYaxis().SetLabelSize(0.04)
    hist.GetYaxis().SetTitleSize(0.04)
    hist.GetYaxis().SetTitleOffset(1.5)
    hist.GetYaxis().SetNdivisions(505)

# Take bkgd function from eqn (1) of arXiv:1506.00962
# x = m_jj
def bkgd(x, par):
    X = x[0] / 8000 # m_jj / sqrt(s)
    xi = 4.0  # hard coded based on values in Table 6
    return par[0] * pow(1.0 - X, par[1] - xi * par[2]) * pow(X, par[2])



# if arguments.rebinFactor:
#     hist.Rebin(int(arguments.rebinFactor))

ROOT.gStyle.SetOptStat(1111110)
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
can = TCanvas("c1", "c1", 800, 800)
can.SetFillColor(0)
can.SetBorderMode(0)
can.SetBorderSize(2)
can.SetTickx(1)
can.SetTicky(1)
can.SetLeftMargin(0.1281407)
can.SetRightMargin(0.0678392)
can.SetTopMargin(0.0582902)
can.SetFrameFillStyle(0)
can.SetFrameBorderMode(0)
can.SetFrameFillStyle(0)
can.SetFrameBorderMode(0)
can.SetLogy(1)

pt1 = TPaveText(0.136935,0.849741,0.48995,0.896373,"brNDC")
pt1.SetBorderSize(0)
pt1.SetFillStyle(0)
pt1.SetTextFont(62)
pt1.SetTextSize(0.0349741)
pt1.AddText("CMS Preliminary")

pt2 = TPaveText(0.827889,0.939119,0.943467,0.985751,"brNDC")
pt2.SetBorderSize(0)
pt2.SetFillStyle(0)
pt2.SetTextFont(42)
pt2.SetTextSize(0.0349741)
pt2.AddText("8 TeV")

pt3 = TPaveText(0.630653,0.849741,0.815327,0.896373,"brNDC")
pt3.SetBorderSize(0)
pt3.SetFillStyle(0)
pt3.SetTextFont(42)
pt3.SetTextSize(0.0349127)
pt3.SetTextAlign(12)
pt3.AddText("WW channel")

pt4 = TPaveText(0.630653,0.849741,0.815327,0.896373,"brNDC")
pt4.SetBorderSize(0)
pt4.SetFillStyle(0)
pt4.SetTextFont(42)
pt4.SetTextSize(0.0349127)
pt4.SetTextAlign(12)
pt4.AddText("WZ channel")

pt5 = TPaveText(0.630653,0.849741,0.815327,0.896373,"brNDC")
pt5.SetBorderSize(0)
pt5.SetFillStyle(0)
pt5.SetTextFont(42)
pt5.SetTextSize(0.0349127)
pt5.SetTextAlign(12)
pt5.AddText("ZZ channel")

myfunc = TF1("myfunc", bkgd, lo, hi, 3)
myfunc.SetLineColor(419)  # dark green
can.Print(outfilePdf + "[")

outputFile = TFile(outfileRoot, "RECREATE")

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
hist.SetMinimum(0.1)
hist.SetMaximum(1e6)
hist.Fit("myfunc", "R")   # Fit in range
hist.SetTitle("Boson mass sideband channel: " + hist.GetTitle())
setHistStyle(hist)
hist.Draw("pe")
myfunc.Draw("same")
can.Print(outfilePdf)
outputFile.cd()
can.SetName("sideband")
can.Write("sideband")

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
hist.SetMinimum(0.1)
hist.SetMaximum(1e6)
hist.Fit("myfunc", "R")   # Fit in range
hist.SetTitle("Preselection channel: " + hist.GetTitle())
setHistStyle(hist)
hist.Draw("pe")
myfunc.Draw("same")
can.Print(outfilePdf)
outputFile.cd()
can.SetName("preselection")
can.Write("preselection")

#################
# ATLAS data
#################
atlas = {}
atlasFile = TFile("ATLASdata.root", "READ")
atlas["WW"] = atlasFile.Get("WWChannelPlotter/" + histBaseName).Clone()
atlas["WZ"] = atlasFile.Get("WZChannelPlotter/" + histBaseName).Clone()
atlas["ZZ"] = atlasFile.Get("ZZChannelPlotter/" + histBaseName).Clone()
setHistStyle(atlas["WW"])
setHistStyle(atlas["WZ"])
setHistStyle(atlas["ZZ"])

cms = {}

cmsAndAtlas = {}
cmsAndAtlas["WW"] = THStack("wwStack", "")
cmsAndAtlas["WZ"] = THStack("wzStack", "")
cmsAndAtlas["ZZ"] = THStack("zzStack", "")

leg = TLegend(0.562814,0.660622,0.878141,0.819948,"","brNDC")
leg.SetBorderSize(0)
leg.SetTextSize(0.0349127)
leg.SetFillStyle(0)

#################
# WW Channel
#################
hist = inputFileSearch.Get("WWChannelPlotter/" + histBaseName).Clone()
setHistStyle(hist)
if combineCMSAndATLAS:
    cms["WW"] = hist.Clone()
    hist.Add(atlas["WW"])
    cms["WW"].SetFillColor(857)
    atlas["WW"].SetFillColor(628)
    cmsAndAtlas["WW"].Add(cms["WW"])
    cmsAndAtlas["WW"].Add(atlas["WW"])
    cmsAndAtlas["WW"].Draw("hist")
    setStackStyle(cmsAndAtlas["WW"],hist)
if not hist:
    print "Could not find TH1 " + arguments.histName + " in " + inputFile
myfunc.SetParameter(0, 500)
myfunc.SetParameter(1, 31.)
myfunc.SetParameter(2, -3.0)
hist.Fit("myfunc", "R0")   # Fit in range
hist.GetXaxis().SetRangeUser(1050, 3500)
hist.SetTitle("WW channel: " + hist.GetTitle())
hist.Draw("pe same")
myfunc.Draw("same")
leg.AddEntry(hist, "ATLAS+CMS data", "p")
leg.AddEntry(myfunc, "background fit", "l")
leg.AddEntry(atlas["WW"], "ATLAS data", "f")
leg.AddEntry(cms["WW"], "CMS data", "f")
leg.Draw("same")
pt1.Draw("same")
pt2.Draw("same")
pt3.Draw("same")
can.Print(outfilePdf)
outputFile.cd()
can.SetName("ww")
can.Write("ww")

#################
# WZ Channel
#################
hist = inputFileSearch.Get("WZChannelPlotter/" + histBaseName).Clone()
setHistStyle(hist)
if combineCMSAndATLAS:
    cms["WZ"] = hist.Clone()
    hist.Add(atlas["WZ"])
    cms["WZ"].SetFillColor(857)
    atlas["WZ"].SetFillColor(628)
    cmsAndAtlas["WZ"].Add(cms["WZ"])
    cmsAndAtlas["WZ"].Add(atlas["WZ"])
    cmsAndAtlas["WZ"].Draw("hist")
    setStackStyle(cmsAndAtlas["WZ"],hist)
if not hist:
    print "Could not find TH1 " + arguments.histName + " in " + inputFile
myfunc.SetParameter(0, 500)
myfunc.SetParameter(1, 31.)
myfunc.SetParameter(2, -3.0)
hist.GetXaxis().SetRangeUser(1050, 3500)
hist.Fit("myfunc", "R0")   # Fit in range
hist.SetTitle("WZ channel: " + hist.GetTitle())
hist.Draw("pe same")
myfunc.Draw("same")
leg.Draw("same")
pt1.Draw("same")
pt2.Draw("same")
pt4.Draw("same")
can.Print(outfilePdf)
outputFile.cd()
can.SetName("wz")
can.Write("wz")

#################
# ZZ Channel
#################
hist = inputFileSearch.Get("ZZChannelPlotter/" + histBaseName).Clone()
setHistStyle(hist)
if combineCMSAndATLAS:
    cms["ZZ"] = hist.Clone()
    hist.Add(atlas["ZZ"])
    cms["ZZ"].SetFillColor(857)
    atlas["ZZ"].SetFillColor(628)
    cmsAndAtlas["ZZ"].Add(cms["ZZ"])
    cmsAndAtlas["ZZ"].Add(atlas["ZZ"])
    cmsAndAtlas["ZZ"].Draw("hist")
    setStackStyle(cmsAndAtlas["ZZ"],hist)
if not hist:
    print "Could not find TH1 " + arguments.histName + " in " + inputFile
myfunc.SetParameter(0, 500)
myfunc.SetParameter(1, 31.)
myfunc.SetParameter(2, -3.0)
hist.GetXaxis().SetRangeUser(1050, 3500)
hist.Fit("myfunc", "R0")   # Fit in range
hist.SetTitle("ZZ channel: " + hist.GetTitle())
hist.Draw("pe same")
myfunc.Draw("same")
leg.Draw("same")
pt1.Draw("same")
pt2.Draw("same")
pt5.Draw("same")
can.Print(outfilePdf)
outputFile.cd()
can.SetName("zz")
can.Write("zz")

inputFileSearch.Close()

can.Print(outfilePdf + "]")
outputFile.Close()
print "Saved plot in " + outfilePdf + " and " + outfileRoot

print "Finished fit.py"

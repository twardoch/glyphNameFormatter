from glyphNameFormatter import GlyphName
from glyphNameFormatter.unicodeRangeNames import getRangeName, getRangeProcessor, getAllRangeNames, rangeNameToModuleName

from glyphNameFormatter.data import name2unicode_AGD
import importlib


#
#
#   find which unicode ranges are needed to cover the AGD names
#   so we can prioritize the support

def testAGDCoverage():
    wantRanges = []
    glyphCount = {}
    for name in name2unicode_AGD:
        uniNumber = name2unicode_AGD[name]
        thisRange = getRangeName(uniNumber)
        if not thisRange in glyphCount:
            glyphCount[thisRange] = 0
        glyphCount[thisRange] += 1
        if thisRange is None:
            #print name, "no range"
            continue
        if thisRange not in wantRanges:
            wantRanges.append(thisRange)
    supported = []
    notSupported = []
    notNeeded = []
    for name in wantRanges:
        moduleName = rangeNameToModuleName(name)
        try:
            module = importlib.import_module('glyphNameFormatter.rangeProcessors.%s' % moduleName)
            supported.append(name)
        except ImportError:
            notSupported.append(name)
    for name in getAllRangeNames():
        if name not in supported and name not in notSupported:
            notNeeded.append(name)
    supported.sort()
    notSupported.sort()
    notNeeded.sort()
    supportedTotal = 0
    notSupportedTotal = 0
    print "Available range processors for AGD:"
    for n in supported:
        print "\t%8d\t%s"%(glyphCount[n], n)
        supportedTotal += glyphCount[n]
    print "\nMissing range processors for AGD:"
    for n in notSupported:
        print "\t%8d\t%s"%(glyphCount[n], n)
        notSupportedTotal += glyphCount[n]
    print "Coverage complete: %3.1f%%"%(100.0*supportedTotal/(supportedTotal+notSupportedTotal))
    print "\nRange processors not needed for AGD:"
    for n in notNeeded:
        print "\t", n



if __name__ == "__main__":
    testAGDCoverage()
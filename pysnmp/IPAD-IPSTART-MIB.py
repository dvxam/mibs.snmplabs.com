#
# PySNMP MIB module IPAD-IPSTART-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPAD-IPSTART-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, NotificationType, IpAddress, Unsigned32, Integer32, ModuleIdentity, enterprises, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, ObjectIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "NotificationType", "IpAddress", "Unsigned32", "Integer32", "ModuleIdentity", "enterprises", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "ObjectIdentity", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
verilink = MibIdentifier((1, 3, 6, 1, 4, 1, 321))
hbu = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100))
ipad = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1))
ipadFrPort = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 1))
ipadService = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 2))
ipadChannel = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 3))
ipadDLCI = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 4))
ipadEndpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 5))
ipadUser = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 6))
ipadPPP = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 7))
ipadModem = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 8))
ipadSvcAware = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 9))
ipadPktSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 10))
ipadTrapDest = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 11))
ipadMisc = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 12))
ipadRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 13))
ipadSoftKey = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 14))
ipadPPPStartTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4), )
if mibBuilder.loadTexts: ipadPPPStartTable.setStatus('optional')
ipadPPPStartTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1), ).setIndexNames((0, "IPAD-IPSTART-MIB", "ipadPPPStartService"))
if mibBuilder.loadTexts: ipadPPPStartTableEntry.setStatus('mandatory')
ipadPPPStartService = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartService.setStatus('mandatory')
ipadPPPStartLCPState = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("initial", 1), ("starting", 2), ("closed", 3), ("stopped", 4), ("closing", 5), ("stopping", 6), ("reqSent", 7), ("ackRcvd", 8), ("ackSent", 9), ("opened", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPState.setStatus('mandatory')
ipadPPPStartLCPStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPStateTime.setStatus('mandatory')
ipadPPPStartLCPStateChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPStateChanges.setStatus('mandatory')
ipadPPPStartLCPMRU = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPMRU.setStatus('mandatory')
ipadPPPStartLCPAsyncCCM = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPAsyncCCM.setStatus('mandatory')
ipadPPPStartLCPAuthProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("pap", 3), ("chap", 4), ("spap", 5), ("eap", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPAuthProtocol.setStatus('mandatory')
ipadPPPStartLCPQualityProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("lqr", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPQualityProtocol.setStatus('mandatory')
ipadPPPStartLCPMagicNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPMagicNumber.setStatus('mandatory')
ipadPPPStartLCPPFC = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPPFC.setStatus('mandatory')
ipadPPPStartLCPACFC = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPACFC.setStatus('mandatory')
ipadPPPStartLCPFCSAlternatives = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("nullFCS", 3), ("ccitt16bitFCS", 4), ("ccitt32bitFCS", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPFCSAlternatives.setStatus('mandatory')
ipadPPPStartLCPSDP = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPSDP.setStatus('mandatory')
ipadPPPStartLCPCompoundFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPCompoundFrames.setStatus('mandatory')
ipadPPPStartAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("initial", 1), ("starting", 2), ("closed", 3), ("stopped", 4), ("closing", 5), ("stopping", 6), ("reqSent", 7), ("ackRcvd", 8), ("ackSent", 9), ("opened", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartAuthState.setStatus('mandatory')
ipadPPPStartAuthStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartAuthStateTime.setStatus('mandatory')
ipadPPPStartAuthStateChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartAuthStateChanges.setStatus('mandatory')
ipadPPPStartAuthFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartAuthFailureCount.setStatus('mandatory')
ipadPPPStartAuthFailureTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadPPPStartAuthFailureTrapEnable.setStatus('mandatory')
ipadPPPStartIPCPState = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("initial", 1), ("starting", 2), ("closed", 3), ("stopped", 4), ("closing", 5), ("stopping", 6), ("reqSent", 7), ("ackRcvd", 8), ("ackSent", 9), ("opened", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartIPCPState.setStatus('mandatory')
ipadPPPStartIPCPStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartIPCPStateTime.setStatus('mandatory')
ipadPPPStartIPCPStateChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartIPCPStateChanges.setStatus('mandatory')
ipadPPPStartIPCPIPSource = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 23), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartIPCPIPSource.setStatus('mandatory')
ipadPPPStartIPCPIPDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 24), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartIPCPIPDestAddress.setStatus('mandatory')
ipadPPPStartIPCPCompressionProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("regularIPdata", 3), ("compressedTCP", 4), ("uncompressedTCP", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartIPCPCompressionProtocol.setStatus('mandatory')
ipadPPPStartLCPHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 5), )
if mibBuilder.loadTexts: ipadPPPStartLCPHistoryTable.setStatus('optional')
ipadPPPStartLCPHistoryTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 5, 1), ).setIndexNames((0, "IPAD-IPSTART-MIB", "ipadPPPStartLCPHistoryIndex"))
if mibBuilder.loadTexts: ipadPPPStartLCPHistoryTableEntry.setStatus('mandatory')
ipadPPPStartLCPHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPHistoryIndex.setStatus('mandatory')
ipadPPPStartLCPHistoryState = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("initial", 1), ("starting", 2), ("closed", 3), ("stopped", 4), ("closing", 5), ("stopping", 6), ("reqSent", 7), ("ackRcvd", 8), ("ackSent", 9), ("opened", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPHistoryState.setStatus('mandatory')
ipadPPPStartLCPHistoryStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartLCPHistoryStateTime.setStatus('mandatory')
ipadPPPStartAuthHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 6), )
if mibBuilder.loadTexts: ipadPPPStartAuthHistoryTable.setStatus('optional')
ipadPPPStartAuthHistoryTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 6, 1), ).setIndexNames((0, "IPAD-IPSTART-MIB", "ipadPPPStartAuthHistoryIndex"))
if mibBuilder.loadTexts: ipadPPPStartAuthHistoryTableEntry.setStatus('mandatory')
ipadPPPStartAuthHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartAuthHistoryIndex.setStatus('mandatory')
ipadPPPStartAuthHistoryState = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("initial", 1), ("starting", 2), ("closed", 3), ("stopped", 4), ("closing", 5), ("stopping", 6), ("reqSent", 7), ("ackRcvd", 8), ("ackSent", 9), ("opened", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartAuthHistoryState.setStatus('mandatory')
ipadPPPStartAuthHistoryStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartAuthHistoryStateTime.setStatus('mandatory')
ipadPPPStartIPCPHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 7), )
if mibBuilder.loadTexts: ipadPPPStartIPCPHistoryTable.setStatus('optional')
ipadPPPStartIPCPHistoryTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 7, 1), ).setIndexNames((0, "IPAD-IPSTART-MIB", "ipadPPPStartIPCPHistoryIndex"))
if mibBuilder.loadTexts: ipadPPPStartIPCPHistoryTableEntry.setStatus('mandatory')
ipadPPPStartIPCPHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartIPCPHistoryIndex.setStatus('mandatory')
ipadPPPStartIPCPHistoryState = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("initial", 1), ("starting", 2), ("closed", 3), ("stopped", 4), ("closing", 5), ("stopping", 6), ("reqSent", 7), ("ackRcvd", 8), ("ackSent", 9), ("opened", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartIPCPHistoryState.setStatus('mandatory')
ipadPPPStartIPCPHistoryStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadPPPStartIPCPHistoryStateTime.setStatus('mandatory')
ipadPPPStartAuthFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 321, 100) + (0,25050))
mibBuilder.exportSymbols("IPAD-IPSTART-MIB", hbu=hbu, ipadPPPStartIPCPCompressionProtocol=ipadPPPStartIPCPCompressionProtocol, ipadPPPStartAuthFailureTrap=ipadPPPStartAuthFailureTrap, ipadPPPStartAuthHistoryTable=ipadPPPStartAuthHistoryTable, ipadMisc=ipadMisc, ipadPPP=ipadPPP, ipadPPPStartAuthHistoryStateTime=ipadPPPStartAuthHistoryStateTime, ipadPPPStartLCPStateTime=ipadPPPStartLCPStateTime, ipadPPPStartLCPCompoundFrames=ipadPPPStartLCPCompoundFrames, ipadUser=ipadUser, ipadPPPStartLCPFCSAlternatives=ipadPPPStartLCPFCSAlternatives, ipadSvcAware=ipadSvcAware, ipadRouter=ipadRouter, ipad=ipad, ipadPPPStartLCPSDP=ipadPPPStartLCPSDP, ipadPPPStartAuthStateTime=ipadPPPStartAuthStateTime, ipadPPPStartIPCPStateTime=ipadPPPStartIPCPStateTime, ipadPPPStartIPCPHistoryTableEntry=ipadPPPStartIPCPHistoryTableEntry, ipadPPPStartService=ipadPPPStartService, ipadPPPStartLCPQualityProtocol=ipadPPPStartLCPQualityProtocol, ipadFrPort=ipadFrPort, ipadPPPStartLCPACFC=ipadPPPStartLCPACFC, ipadPPPStartIPCPIPDestAddress=ipadPPPStartIPCPIPDestAddress, ipadService=ipadService, ipadPPPStartLCPMRU=ipadPPPStartLCPMRU, ipadPPPStartIPCPStateChanges=ipadPPPStartIPCPStateChanges, ipadPPPStartLCPMagicNumber=ipadPPPStartLCPMagicNumber, ipadPPPStartLCPStateChanges=ipadPPPStartLCPStateChanges, ipadPPPStartIPCPState=ipadPPPStartIPCPState, ipadPPPStartAuthState=ipadPPPStartAuthState, ipadPPPStartAuthStateChanges=ipadPPPStartAuthStateChanges, ipadPPPStartIPCPHistoryState=ipadPPPStartIPCPHistoryState, ipadPPPStartLCPHistoryStateTime=ipadPPPStartLCPHistoryStateTime, ipadPPPStartLCPPFC=ipadPPPStartLCPPFC, ipadPPPStartTable=ipadPPPStartTable, ipadPPPStartLCPAuthProtocol=ipadPPPStartLCPAuthProtocol, ipadPPPStartTableEntry=ipadPPPStartTableEntry, ipadPPPStartLCPHistoryIndex=ipadPPPStartLCPHistoryIndex, ipadPPPStartAuthHistoryState=ipadPPPStartAuthHistoryState, ipadPktSwitch=ipadPktSwitch, ipadDLCI=ipadDLCI, ipadPPPStartAuthFailureCount=ipadPPPStartAuthFailureCount, ipadPPPStartLCPHistoryTableEntry=ipadPPPStartLCPHistoryTableEntry, ipadEndpoint=ipadEndpoint, ipadPPPStartAuthHistoryIndex=ipadPPPStartAuthHistoryIndex, ipadTrapDest=ipadTrapDest, verilink=verilink, ipadModem=ipadModem, ipadPPPStartLCPState=ipadPPPStartLCPState, ipadPPPStartLCPAsyncCCM=ipadPPPStartLCPAsyncCCM, ipadChannel=ipadChannel, ipadPPPStartIPCPIPSource=ipadPPPStartIPCPIPSource, ipadPPPStartLCPHistoryTable=ipadPPPStartLCPHistoryTable, ipadSoftKey=ipadSoftKey, ipadPPPStartLCPHistoryState=ipadPPPStartLCPHistoryState, ipadPPPStartAuthHistoryTableEntry=ipadPPPStartAuthHistoryTableEntry, ipadPPPStartIPCPHistoryTable=ipadPPPStartIPCPHistoryTable, ipadPPPStartIPCPHistoryStateTime=ipadPPPStartIPCPHistoryStateTime, ipadPPPStartAuthFailureTrapEnable=ipadPPPStartAuthFailureTrapEnable, ipadPPPStartIPCPHistoryIndex=ipadPPPStartIPCPHistoryIndex)

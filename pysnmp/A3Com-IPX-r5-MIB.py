#
# PySNMP MIB module A3COM-IPX-R5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/A3COM-IPX-R5-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:29:21 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
MacAddress, = mibBuilder.importSymbols("RFC1286-MIB", "MacAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, MibIdentifier, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, TimeTicks, Unsigned32, enterprises, iso, ModuleIdentity, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "MibIdentifier", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "TimeTicks", "Unsigned32", "enterprises", "iso", "ModuleIdentity", "Counter64", "Gauge32")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComIPX = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 7))
class SMDSAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3ipxGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 7, 1))
a3ipxControl = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7))
class IPXNET(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

a3ipxRouteControl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRouteControl.setStatus('deprecated')
a3ipxWanBcastControl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxWanBcastControl.setStatus('deprecated')
a3ipxUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxUpdateTime.setStatus('deprecated')
a3ipxFlushRipSap = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("rip", 2), ("sap", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxFlushRipSap.setStatus('mandatory')
a3ipxInternalNet = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 5), IPXNET()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxInternalNet.setStatus('mandatory')
a3ipxRouterName = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRouterName.setStatus('mandatory')
a3ipxControlTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1), )
if mibBuilder.loadTexts: a3ipxControlTable.setStatus('mandatory')
a3ipxControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxControlPort"))
if mibBuilder.loadTexts: a3ipxControlEntry.setStatus('mandatory')
a3ipxControlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxControlPort.setStatus('mandatory')
a3ipxControlRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxControlRoute.setStatus('mandatory')
a3ipxControlWanBcast = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxControlWanBcast.setStatus('mandatory')
a3ipxControlChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxControlChecksum.setStatus('mandatory')
a3ipxControlWanOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wan", 1), ("noWan", 2))).clone('noWan')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxControlWanOpt.setStatus('mandatory')
a3ipxRipControlTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 2), )
if mibBuilder.loadTexts: a3ipxRipControlTable.setStatus('mandatory')
a3ipxRipControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxRipControlPort"))
if mibBuilder.loadTexts: a3ipxRipControlEntry.setStatus('mandatory')
a3ipxRipControlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxRipControlPort.setStatus('mandatory')
a3ipxRipControlSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipControlSwitch.setStatus('deprecated')
a3ipxRipControlTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipControlTrigger.setStatus('mandatory')
a3ipxRipControlPoison = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipControlPoison.setStatus('mandatory')
a3ipxRipControlMapOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oldNbrMap", 1), ("newNbrMap", 2))).clone('newNbrMap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipControlMapOpt.setStatus('mandatory')
a3ipxRipControlWanOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wan", 1), ("noWan", 2))).clone('noWan')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipControlWanOpt.setStatus('deprecated')
a3ipxRipControlPerRip = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("periodicRip", 1), ("nonPeriodicRip", 2))).clone('periodicRip')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipControlPerRip.setStatus('mandatory')
a3ipxRipControlPerSap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("periodicSap", 1), ("nonPeriodicSap", 2))).clone('periodicSap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipControlPerSap.setStatus('mandatory')
a3ipxRipControlTalk = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipControlTalk.setStatus('deprecated')
a3ipxRipControlListen = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipControlListen.setStatus('deprecated')
a3ipxSapControlTalk = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxSapControlTalk.setStatus('deprecated')
a3ipxSapControlListen = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxSapControlListen.setStatus('deprecated')
a3ipxRipCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("talkListen", 1), ("talkNoListen", 2), ("noTalkListen", 3), ("noTalkNoListen", 4), ("auto", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipCtl.setStatus('mandatory')
a3ipxSapCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("talkListen", 1), ("talkNoListen", 2), ("noTalkListen", 3), ("noTalkNoListen", 4), ("auto", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxSapCtl.setStatus('mandatory')
a3ipxWaAddrTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 3), )
if mibBuilder.loadTexts: a3ipxWaAddrTable.setStatus('mandatory')
a3ipxWaAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxWaAddrEthAddress"))
if mibBuilder.loadTexts: a3ipxWaAddrEntry.setStatus('mandatory')
a3ipxWaAddrEthAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxWaAddrEthAddress.setStatus('mandatory')
a3ipxWaAddrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxWaAddrPort.setStatus('mandatory')
a3ipxWaAddrDLType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("x25", 1), ("frameRelay", 2), ("smds", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxWaAddrDLType.setStatus('mandatory')
a3ipxWaAddrDLAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 4), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxWaAddrDLAddress.setStatus('mandatory')
a3ipxWaAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxWaAddrStatus.setStatus('mandatory')
a3ipxAttachedNetTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 4), )
if mibBuilder.loadTexts: a3ipxAttachedNetTable.setStatus('mandatory')
a3ipxAttachedNetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxAttachedNetNumber"))
if mibBuilder.loadTexts: a3ipxAttachedNetEntry.setStatus('mandatory')
a3ipxAttachedNetNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 1), IPXNET()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxAttachedNetNumber.setStatus('mandatory')
a3ipxAttachedNetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxAttachedNetPort.setStatus('mandatory')
a3ipxAttachedNetFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee", 2), ("llc", 3), ("snap", 4), ("ppp", 5), ("x25", 6), ("fr", 7), ("smds", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxAttachedNetFormat.setStatus('mandatory')
a3ipxAttachedNetType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxAttachedNetType.setStatus('mandatory')
a3ipxAttachedNetOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxAttachedNetOperState.setStatus('mandatory')
a3ipxAttachedNetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxAttachedNetStatus.setStatus('mandatory')
a3ipxRouteTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 5), )
if mibBuilder.loadTexts: a3ipxRouteTable.setStatus('mandatory')
a3ipxRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxRouteDestNet"), (0, "A3COM-IPX-R5-MIB", "a3ipxRouteType"))
if mibBuilder.loadTexts: a3ipxRouteEntry.setStatus('mandatory')
a3ipxRouteDestNet = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 1), IPXNET()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxRouteDestNet.setStatus('mandatory')
a3ipxRouteAttachedNet = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 2), IPXNET()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRouteAttachedNet.setStatus('mandatory')
a3ipxRouteDLType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernet", 1), ("x25", 2), ("frameRelay", 3), ("smds", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxRouteDLType.setStatus('mandatory')
a3ipxRouteDLAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 4), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRouteDLAddress.setStatus('mandatory')
a3ipxRouteHops = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRouteHops.setStatus('mandatory')
a3ipxRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxRouteType.setStatus('mandatory')
a3ipxRouteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("rip", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxRouteProto.setStatus('mandatory')
a3ipxRouteDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRouteDelay.setStatus('mandatory')
a3ipxRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRouteStatus.setStatus('mandatory')
a3ipxServerTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 6), )
if mibBuilder.loadTexts: a3ipxServerTable.setStatus('mandatory')
a3ipxServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxServerName"), (0, "A3COM-IPX-R5-MIB", "a3ipxServerType"))
if mibBuilder.loadTexts: a3ipxServerEntry.setStatus('mandatory')
a3ipxServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxServerName.setStatus('mandatory')
a3ipxServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxServerType.setStatus('mandatory')
a3ipxServerNet = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 3), IPXNET()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxServerNet.setStatus('mandatory')
a3ipxServerDLAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxServerDLAddress.setStatus('mandatory')
a3ipxServerSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxServerSocket.setStatus('mandatory')
a3ipxServerProto = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("sap", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxServerProto.setStatus('mandatory')
a3ipxServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxServerStatus.setStatus('mandatory')
a3ipxX25configTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 7), )
if mibBuilder.loadTexts: a3ipxX25configTable.setStatus('mandatory')
a3ipxX25configEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxX25configPort"))
if mibBuilder.loadTexts: a3ipxX25configEntry.setStatus('mandatory')
a3ipxX25configPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxX25configPort.setStatus('mandatory')
a3ipxX25configPID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(238)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxX25configPID.setStatus('mandatory')
a3ipxX25configQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxX25configQueueSize.setStatus('deprecated')
a3ipxX25configVClimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxX25configVClimit.setStatus('deprecated')
a3ipxX25configVCtimer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxX25configVCtimer.setStatus('deprecated')
a3ipxX25configProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxX25configProfId.setStatus('mandatory')
a3ipxSmdsGroupAddressTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 8), )
if mibBuilder.loadTexts: a3ipxSmdsGroupAddressTable.setStatus('mandatory')
a3ipxSmdsGroupAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 8, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxSmdsGaIpxPort"))
if mibBuilder.loadTexts: a3ipxSmdsGroupAddressEntry.setStatus('mandatory')
a3ipxSmdsGaIpxPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxSmdsGaIpxPort.setStatus('mandatory')
a3ipxSmdsGaAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 8, 1, 2), SMDSAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxSmdsGaAddress.setStatus('mandatory')
a3ipxPreferredSvrTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 9), )
if mibBuilder.loadTexts: a3ipxPreferredSvrTable.setStatus('mandatory')
a3ipxPreferredSvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 9, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxPrefSvrPort"), (0, "A3COM-IPX-R5-MIB", "a3ipxPrefSvrName"))
if mibBuilder.loadTexts: a3ipxPreferredSvrEntry.setStatus('mandatory')
a3ipxPrefSvrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxPrefSvrPort.setStatus('mandatory')
a3ipxPrefSvrName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxPrefSvrName.setStatus('mandatory')
a3ipxPrefSvrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 9, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxPrefSvrStatus.setStatus('mandatory')
a3ipxPortconfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 10), )
if mibBuilder.loadTexts: a3ipxPortconfigTable.setStatus('mandatory')
a3ipxPortconfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxPortconfigPort"))
if mibBuilder.loadTexts: a3ipxPortconfigEntry.setStatus('mandatory')
a3ipxPortconfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxPortconfigPort.setStatus('mandatory')
a3ipxRipUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipUpdateTime.setStatus('mandatory')
a3ipxSapUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxSapUpdateTime.setStatus('mandatory')
a3ipxDefMetricHops = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxDefMetricHops.setStatus('mandatory')
a3ipxDefMetricTicks = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxDefMetricTicks.setStatus('mandatory')
a3ipxSpoofCtlTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 7, 11), )
if mibBuilder.loadTexts: a3ipxSpoofCtlTable.setStatus('mandatory')
a3ipxSpoofCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 7, 11, 1), ).setIndexNames((0, "A3COM-IPX-R5-MIB", "a3ipxSpoofCtlPort"))
if mibBuilder.loadTexts: a3ipxSpoofCtlEntry.setStatus('mandatory')
a3ipxSpoofCtlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ipxSpoofCtlPort.setStatus('mandatory')
a3ipxSpoofCtlWatchdog = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 7, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxSpoofCtlWatchdog.setStatus('mandatory')
a3ipxRipHoldTimeFactor = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxRipHoldTimeFactor.setStatus('mandatory')
a3ipxSapHoldTimeFactor = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ipxSapHoldTimeFactor.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-IPX-R5-MIB", a3ipxGeneral=a3ipxGeneral, a3ipxServerType=a3ipxServerType, a3ipxServerNet=a3ipxServerNet, a3ipxSapHoldTimeFactor=a3ipxSapHoldTimeFactor, a3ipxRipControlTalk=a3ipxRipControlTalk, a3ipxSmdsGroupAddressEntry=a3ipxSmdsGroupAddressEntry, a3ipxPortconfigEntry=a3ipxPortconfigEntry, a3ipxRipControlEntry=a3ipxRipControlEntry, RowStatus=RowStatus, a3ipxServerEntry=a3ipxServerEntry, a3ipxWaAddrPort=a3ipxWaAddrPort, a3ipxSapControlTalk=a3ipxSapControlTalk, a3ipxUpdateTime=a3ipxUpdateTime, a3ipxRipControlListen=a3ipxRipControlListen, a3ipxRipControlMapOpt=a3ipxRipControlMapOpt, a3ipxPrefSvrPort=a3ipxPrefSvrPort, SMDSAddress=SMDSAddress, a3ipxRipControlSwitch=a3ipxRipControlSwitch, a3ipxPrefSvrName=a3ipxPrefSvrName, a3ipxPrefSvrStatus=a3ipxPrefSvrStatus, a3ipxAttachedNetEntry=a3ipxAttachedNetEntry, a3ipxX25configQueueSize=a3ipxX25configQueueSize, a3ipxControlEntry=a3ipxControlEntry, a3ipxX25configTable=a3ipxX25configTable, a3ipxFlushRipSap=a3ipxFlushRipSap, a3ipxControlTable=a3ipxControlTable, a3ipxSmdsGaAddress=a3ipxSmdsGaAddress, a3ipxAttachedNetType=a3ipxAttachedNetType, a3ipxRouteEntry=a3ipxRouteEntry, a3ipxRouteType=a3ipxRouteType, a3ipxWaAddrDLAddress=a3ipxWaAddrDLAddress, a3ipxWanBcastControl=a3ipxWanBcastControl, a3ipxSapControlListen=a3ipxSapControlListen, brouterMIB=brouterMIB, a3ipxX25configProfId=a3ipxX25configProfId, a3ipxWaAddrDLType=a3ipxWaAddrDLType, a3ipxRipControlPort=a3ipxRipControlPort, a3ipxRipControlWanOpt=a3ipxRipControlWanOpt, a3ipxRouteStatus=a3ipxRouteStatus, a3ipxRipControlPoison=a3ipxRipControlPoison, a3ipxSpoofCtlPort=a3ipxSpoofCtlPort, a3ipxRouteDLAddress=a3ipxRouteDLAddress, a3ipxAttachedNetFormat=a3ipxAttachedNetFormat, a3ipxWaAddrEthAddress=a3ipxWaAddrEthAddress, a3ipxWaAddrEntry=a3ipxWaAddrEntry, a3ipxX25configVClimit=a3ipxX25configVClimit, a3ipxServerName=a3ipxServerName, a3ipxSmdsGroupAddressTable=a3ipxSmdsGroupAddressTable, a3ipxAttachedNetOperState=a3ipxAttachedNetOperState, a3ipxSapUpdateTime=a3ipxSapUpdateTime, a3ipxDefMetricHops=a3ipxDefMetricHops, a3ipxServerProto=a3ipxServerProto, a3ipxRipHoldTimeFactor=a3ipxRipHoldTimeFactor, a3ipxControlWanOpt=a3ipxControlWanOpt, a3ipxWaAddrStatus=a3ipxWaAddrStatus, a3ipxSapCtl=a3ipxSapCtl, a3ipxServerSocket=a3ipxServerSocket, a3ipxX25configVCtimer=a3ipxX25configVCtimer, a3ipxServerTable=a3ipxServerTable, a3ipxRipControlPerSap=a3ipxRipControlPerSap, a3ipxControlPort=a3ipxControlPort, a3ipxServerStatus=a3ipxServerStatus, a3ipxRipControlTable=a3ipxRipControlTable, a3ipxRouterName=a3ipxRouterName, a3ipxRipCtl=a3ipxRipCtl, a3ipxControlChecksum=a3ipxControlChecksum, a3ipxRouteHops=a3ipxRouteHops, a3ipxPreferredSvrEntry=a3ipxPreferredSvrEntry, a3ipxSpoofCtlWatchdog=a3ipxSpoofCtlWatchdog, a3ipxRouteDestNet=a3ipxRouteDestNet, a3ComIPX=a3ComIPX, a3ipxRouteDLType=a3ipxRouteDLType, a3ipxSmdsGaIpxPort=a3ipxSmdsGaIpxPort, a3ipxRouteTable=a3ipxRouteTable, a3ipxAttachedNetStatus=a3ipxAttachedNetStatus, a3ipxAttachedNetNumber=a3ipxAttachedNetNumber, a3ipxPortconfigPort=a3ipxPortconfigPort, IPXNET=IPXNET, a3ipxDefMetricTicks=a3ipxDefMetricTicks, a3ipxAttachedNetPort=a3ipxAttachedNetPort, a3ipxSpoofCtlTable=a3ipxSpoofCtlTable, a3ipxControlWanBcast=a3ipxControlWanBcast, a3ipxRouteDelay=a3ipxRouteDelay, a3Com=a3Com, a3ipxInternalNet=a3ipxInternalNet, a3ipxControl=a3ipxControl, a3ipxX25configPort=a3ipxX25configPort, a3ipxRipControlPerRip=a3ipxRipControlPerRip, a3ipxSpoofCtlEntry=a3ipxSpoofCtlEntry, a3ipxX25configEntry=a3ipxX25configEntry, a3ipxX25configPID=a3ipxX25configPID, a3ipxRouteControl=a3ipxRouteControl, a3ipxRipControlTrigger=a3ipxRipControlTrigger, a3ipxServerDLAddress=a3ipxServerDLAddress, a3ipxPreferredSvrTable=a3ipxPreferredSvrTable, a3ipxWaAddrTable=a3ipxWaAddrTable, a3ipxRipUpdateTime=a3ipxRipUpdateTime, a3ipxPortconfigTable=a3ipxPortconfigTable, a3ipxAttachedNetTable=a3ipxAttachedNetTable, a3ipxControlRoute=a3ipxControlRoute, a3ipxRouteAttachedNet=a3ipxRouteAttachedNet, a3ipxRouteProto=a3ipxRouteProto)

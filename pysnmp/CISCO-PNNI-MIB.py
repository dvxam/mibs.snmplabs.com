#
# PySNMP MIB module CISCO-PNNI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PNNI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
pnniRouteAddrEntry, pnniNodeEntry, pnniIfEntry = mibBuilder.importSymbols("PNNI-MIB", "pnniRouteAddrEntry", "pnniNodeEntry", "pnniIfEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, Integer32, Bits, IpAddress, Gauge32, Counter32, Unsigned32, Counter64, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Integer32", "Bits", "IpAddress", "Gauge32", "Counter32", "Unsigned32", "Counter64", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoPnniMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 65))
ciscoPnniMIB.setRevisions(('1996-10-28 00:00',))
if mibBuilder.loadTexts: ciscoPnniMIB.setLastUpdated('9610280000Z')
if mibBuilder.loadTexts: ciscoPnniMIB.setOrganization('Cisco Systems, Inc.')
ciscoPnniMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 65, 1))
class E164Address(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), )
ciscoPnniBase = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1))
ciscoPnniBackgroundRoutes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniBackgroundRoutes.setStatus('current')
ciscoPnniBackgroundPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniBackgroundPollInterval.setStatus('current')
ciscoPnniBackgroundInsignificantThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(32)).setUnits('changes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniBackgroundInsignificantThreshold.setStatus('current')
ciscoPnniResourceMgmtPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniResourceMgmtPollInterval.setStatus('current')
ciscoPnniAdminWeightMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uniform", 1), ("linespeed", 2))).clone('uniform')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniAdminWeightMode.setStatus('current')
ciscoPnniMaxAdminWeightPercentage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 2000), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniMaxAdminWeightPercentage.setStatus('current')
ciscoPnniRouteOptimizationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 100)).clone(30)).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniRouteOptimizationThreshold.setStatus('current')
ciscoPnniNode = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2))
ciscoPnniNodeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1), )
if mibBuilder.loadTexts: ciscoPnniNodeTable.setStatus('current')
ciscoPnniNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1), )
pnniNodeEntry.registerAugmentions(("CISCO-PNNI-MIB", "ciscoPnniNodeEntry"))
ciscoPnniNodeEntry.setIndexNames(*pnniNodeEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoPnniNodeEntry.setStatus('current')
ciscoPnniNodeAutoSummary = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPnniNodeAutoSummary.setStatus('current')
ciscoPnniNodeRedistributeStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPnniNodeRedistributeStatic.setStatus('current')
ciscoPnniNodePtseRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPnniNodePtseRequest.setStatus('current')
ciscoPnniNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPnniNodeName.setStatus('current')
ciscoPnniNodeScopeMappingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatic", 1), ("manual", 2))).clone('automatic')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPnniNodeScopeMappingMode.setStatus('current')
ciscoPnniInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3))
ciscoPnniIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1), )
if mibBuilder.loadTexts: ciscoPnniIfTable.setStatus('current')
ciscoPnniIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1), )
pnniIfEntry.registerAugmentions(("CISCO-PNNI-MIB", "ciscoPnniIfEntry"))
ciscoPnniIfEntry.setIndexNames(*pnniIfEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoPnniIfEntry.setStatus('current')
ciscoPnniIfLinkSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("adminWeightMinimize", 1), ("blockingMinimize", 2), ("transmitSpeedMaximize", 3), ("loadBalance", 4))).clone('blockingMinimize')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniIfLinkSelection.setStatus('current')
ciscoPnniIfRouteOptimization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disable", 1), ("soft", 2), ("switched", 3), ("switchedAndSoft", 4))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniIfRouteOptimization.setStatus('current')
ciscoPnniIfRouteOptimInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 10000)).clone(60)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniIfRouteOptimInterval.setStatus('current')
ciscoPnniIfRouteOptimStartHour = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setUnits('hour').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniIfRouteOptimStartHour.setStatus('current')
ciscoPnniIfRouteOptimStartMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniIfRouteOptimStartMinute.setStatus('current')
ciscoPnniIfRouteOptimEndHour = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setUnits('hour').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniIfRouteOptimEndHour.setStatus('current')
ciscoPnniIfRouteOptimEndMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniIfRouteOptimEndMinute.setStatus('current')
ciscoPnniPrecedence = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4))
ciscoPnniPrecedenceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4, 1), )
if mibBuilder.loadTexts: ciscoPnniPrecedenceTable.setStatus('current')
ciscoPnniPrecedenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-PNNI-MIB", "ciscoPnniPrecedenceAddressType"))
if mibBuilder.loadTexts: ciscoPnniPrecedenceEntry.setStatus('current')
ciscoPnniPrecedenceAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("staticLocalInternalWithMetrics", 1), ("staticLocalExterior", 2), ("staticLocalExteriorWithMetrics", 3), ("pnniRemoteInternal", 4), ("pnniRemoteInternalWithMetrics", 5), ("pnniRemoteExterior", 6), ("pnniRemoteExteriorWithMetrics", 7))))
if mibBuilder.loadTexts: ciscoPnniPrecedenceAddressType.setStatus('current')
ciscoPnniPrecedenceValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoPnniPrecedenceValue.setStatus('current')
ciscoPnniRouteAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 5))
ciscoPnniRouteAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 5, 1), )
if mibBuilder.loadTexts: ciscoPnniRouteAddrTable.setStatus('current')
ciscoPnniRouteAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 5, 1, 1), )
pnniRouteAddrEntry.registerAugmentions(("CISCO-PNNI-MIB", "ciscoPnniRouteAddrEntry"))
ciscoPnniRouteAddrEntry.setIndexNames(*pnniRouteAddrEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoPnniRouteAddrEntry.setStatus('current')
ciscoPnniRouteAddrForwardingE164Address = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 5, 1, 1, 1), E164Address().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPnniRouteAddrForwardingE164Address.setStatus('current')
ciscoPnniMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 65, 3))
ciscoPnniMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 1))
ciscoPnniMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 2))
ciscoPnniMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 1, 1)).setObjects(("CISCO-PNNI-MIB", "ciscoPnniBasicGroup"), ("CISCO-PNNI-MIB", "ciscoPnniRouteOptimizationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPnniMIBCompliance = ciscoPnniMIBCompliance.setStatus('current')
ciscoPnniBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 2, 1)).setObjects(("CISCO-PNNI-MIB", "ciscoPnniBackgroundRoutes"), ("CISCO-PNNI-MIB", "ciscoPnniBackgroundPollInterval"), ("CISCO-PNNI-MIB", "ciscoPnniBackgroundInsignificantThreshold"), ("CISCO-PNNI-MIB", "ciscoPnniResourceMgmtPollInterval"), ("CISCO-PNNI-MIB", "ciscoPnniAdminWeightMode"), ("CISCO-PNNI-MIB", "ciscoPnniMaxAdminWeightPercentage"), ("CISCO-PNNI-MIB", "ciscoPnniNodeAutoSummary"), ("CISCO-PNNI-MIB", "ciscoPnniNodeRedistributeStatic"), ("CISCO-PNNI-MIB", "ciscoPnniNodePtseRequest"), ("CISCO-PNNI-MIB", "ciscoPnniNodeName"), ("CISCO-PNNI-MIB", "ciscoPnniNodeScopeMappingMode"), ("CISCO-PNNI-MIB", "ciscoPnniIfLinkSelection"), ("CISCO-PNNI-MIB", "ciscoPnniPrecedenceValue"), ("CISCO-PNNI-MIB", "ciscoPnniRouteAddrForwardingE164Address"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPnniBasicGroup = ciscoPnniBasicGroup.setStatus('current')
ciscoPnniRouteOptimizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 2, 2)).setObjects(("CISCO-PNNI-MIB", "ciscoPnniRouteOptimizationThreshold"), ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimization"), ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimInterval"), ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimStartHour"), ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimStartMinute"), ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimEndHour"), ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimEndMinute"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPnniRouteOptimizationGroup = ciscoPnniRouteOptimizationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PNNI-MIB", ciscoPnniIfTable=ciscoPnniIfTable, ciscoPnniPrecedence=ciscoPnniPrecedence, ciscoPnniIfRouteOptimStartHour=ciscoPnniIfRouteOptimStartHour, ciscoPnniRouteAddrEntry=ciscoPnniRouteAddrEntry, ciscoPnniMIB=ciscoPnniMIB, ciscoPnniNodeName=ciscoPnniNodeName, ciscoPnniIfEntry=ciscoPnniIfEntry, PYSNMP_MODULE_ID=ciscoPnniMIB, ciscoPnniMaxAdminWeightPercentage=ciscoPnniMaxAdminWeightPercentage, ciscoPnniInterface=ciscoPnniInterface, E164Address=E164Address, ciscoPnniMIBGroups=ciscoPnniMIBGroups, ciscoPnniRouteOptimizationGroup=ciscoPnniRouteOptimizationGroup, ciscoPnniPrecedenceTable=ciscoPnniPrecedenceTable, ciscoPnniIfLinkSelection=ciscoPnniIfLinkSelection, ciscoPnniRouteOptimizationThreshold=ciscoPnniRouteOptimizationThreshold, ciscoPnniMIBCompliance=ciscoPnniMIBCompliance, ciscoPnniBackgroundPollInterval=ciscoPnniBackgroundPollInterval, ciscoPnniPrecedenceEntry=ciscoPnniPrecedenceEntry, ciscoPnniBackgroundInsignificantThreshold=ciscoPnniBackgroundInsignificantThreshold, ciscoPnniNodeTable=ciscoPnniNodeTable, ciscoPnniBackgroundRoutes=ciscoPnniBackgroundRoutes, ciscoPnniMIBConformance=ciscoPnniMIBConformance, ciscoPnniRouteAddrTable=ciscoPnniRouteAddrTable, ciscoPnniNodeScopeMappingMode=ciscoPnniNodeScopeMappingMode, ciscoPnniNodeAutoSummary=ciscoPnniNodeAutoSummary, ciscoPnniMIBCompliances=ciscoPnniMIBCompliances, ciscoPnniRouteAddr=ciscoPnniRouteAddr, ciscoPnniMIBObjects=ciscoPnniMIBObjects, ciscoPnniIfRouteOptimization=ciscoPnniIfRouteOptimization, ciscoPnniPrecedenceValue=ciscoPnniPrecedenceValue, ciscoPnniIfRouteOptimEndHour=ciscoPnniIfRouteOptimEndHour, ciscoPnniRouteAddrForwardingE164Address=ciscoPnniRouteAddrForwardingE164Address, ciscoPnniAdminWeightMode=ciscoPnniAdminWeightMode, ciscoPnniResourceMgmtPollInterval=ciscoPnniResourceMgmtPollInterval, ciscoPnniNodeEntry=ciscoPnniNodeEntry, ciscoPnniIfRouteOptimEndMinute=ciscoPnniIfRouteOptimEndMinute, ciscoPnniPrecedenceAddressType=ciscoPnniPrecedenceAddressType, ciscoPnniNode=ciscoPnniNode, ciscoPnniBasicGroup=ciscoPnniBasicGroup, ciscoPnniBase=ciscoPnniBase, ciscoPnniIfRouteOptimStartMinute=ciscoPnniIfRouteOptimStartMinute, ciscoPnniIfRouteOptimInterval=ciscoPnniIfRouteOptimInterval, ciscoPnniNodeRedistributeStatic=ciscoPnniNodeRedistributeStatic, ciscoPnniNodePtseRequest=ciscoPnniNodePtseRequest)

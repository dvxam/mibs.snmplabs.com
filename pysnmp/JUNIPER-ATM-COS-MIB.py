#
# PySNMP MIB module JUNIPER-ATM-COS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-ATM-COS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:47:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
atmVclVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVclVci")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
jnxCosFcId, = mibBuilder.importSymbols("JUNIPER-COS-MIB", "jnxCosFcId")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, IpAddress, TimeTicks, ModuleIdentity, Unsigned32, Counter64, Gauge32, ObjectIdentity, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "IpAddress", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxAtmCos = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 21))
jnxAtmCos.setRevisions(('2003-04-09 00:00', '2003-06-20 00:00', '2002-09-04 00:00',))
if mibBuilder.loadTexts: jnxAtmCos.setLastUpdated('200304090000Z')
if mibBuilder.loadTexts: jnxAtmCos.setOrganization('Juniper Networks, Inc.')
jnxCosAtmVcTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 21, 1), )
if mibBuilder.loadTexts: jnxCosAtmVcTable.setStatus('current')
jnxCosAtmVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 21, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: jnxCosAtmVcEntry.setStatus('current')
jnxCosAtmVcCosMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("strict", 0), ("alternate", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcCosMode.setStatus('current')
jnxCosAtmVcScTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2), )
if mibBuilder.loadTexts: jnxCosAtmVcScTable.setStatus('current')
jnxCosAtmVcScEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "JUNIPER-COS-MIB", "jnxCosFcId"))
if mibBuilder.loadTexts: jnxCosAtmVcScEntry.setStatus('current')
jnxCosAtmVcScPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("low", 0), ("high", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScPriority.setStatus('current')
jnxCosAtmVcScTxWeightType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("cells", 0), ("percent", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScTxWeightType.setStatus('current')
jnxCosAtmVcScTxWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScTxWeight.setStatus('current')
jnxCosAtmVcScDpType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("linearRed", 0), ("epd", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScDpType.setStatus('current')
jnxCosAtmVcScLrdpQueueDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScLrdpQueueDepth.setStatus('current')
jnxCosAtmVcScLrdpLowPlpThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScLrdpLowPlpThresh.setStatus('current')
jnxCosAtmVcScLrdpHighPlpThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScLrdpHighPlpThresh.setStatus('current')
jnxCosAtmVcEpdThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcEpdThreshold.setStatus('current')
jnxCosAtmVcQstatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3), )
if mibBuilder.loadTexts: jnxCosAtmVcQstatsTable.setStatus('current')
jnxCosAtmVcQstatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "JUNIPER-COS-MIB", "jnxCosFcId"))
if mibBuilder.loadTexts: jnxCosAtmVcQstatsEntry.setStatus('current')
jnxCosAtmVcQstatsOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutPackets.setStatus('current')
jnxCosAtmVcQstatsOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutBytes.setStatus('current')
jnxCosAtmVcQstatsOutRedDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutRedDropPkts.setStatus('current')
jnxCosAtmVcQstatsOutNonRedDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutNonRedDrops.setStatus('current')
jnxCosAtmVcQstatsOutLpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutLpBytes.setStatus('current')
jnxCosAtmVcQstatsOutLpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutLpPkts.setStatus('current')
jnxCosAtmVcQstatsOutLpDropBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutLpDropBytes.setStatus('current')
jnxCosAtmVcQstatsOutHpDropBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutHpDropBytes.setStatus('current')
jnxCosAtmVcQstatsOutLpDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutLpDropPkts.setStatus('current')
jnxCosAtmVcQstatsOutHpDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutHpDropPkts.setStatus('current')
jnxCosAtmTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4), )
if mibBuilder.loadTexts: jnxCosAtmTrunkTable.setStatus('current')
jnxCosAtmTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-COS-MIB", "jnxCosFcId"))
if mibBuilder.loadTexts: jnxCosAtmTrunkEntry.setStatus('current')
jnxCosAtmTrunkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("alternate", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkMode.setStatus('current')
jnxCosAtmTrunkScPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkScPriority.setStatus('current')
jnxCosAtmTrunkScTxWeightType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cells", 1), ("percent", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkScTxWeightType.setStatus('current')
jnxCosAtmTrunkScTxWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkScTxWeight.setStatus('current')
jnxCosAtmTrunkQaType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("red", 1), ("singleEpd", 2), ("dualEpd", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQaType.setStatus('current')
jnxCosAtmTrunkEpdThresholdPlp0 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkEpdThresholdPlp0.setStatus('current')
jnxCosAtmTrunkEpdThresholdPlp1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkEpdThresholdPlp1.setStatus('current')
jnxCosAtmTrunkQstatsOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutPackets.setStatus('current')
jnxCosAtmTrunkQstatsOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutBytes.setStatus('current')
jnxCosAtmTrunkQstatsOutDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutDrops.setStatus('current')
jnxCosAtmTrunkQstatsOutLpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutLpBytes.setStatus('current')
jnxCosAtmTrunkQstatsOutLpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutLpPkts.setStatus('current')
jnxCosAtmTrunkQstatsOutLpDropBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutLpDropBytes.setStatus('current')
jnxCosAtmTrunkQstatsOutHpDropBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutHpDropBytes.setStatus('current')
jnxCosAtmTrunkQstatsOutLpDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutLpDropPkts.setStatus('current')
jnxCosAtmTrunkQstatsOutHpDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutHpDropPkts.setStatus('current')
jnxCosAtmTrunkQstatsOutHpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutHpBytes.setStatus('current')
jnxCosAtmTrunkQstatsOutHpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutHpPkts.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-ATM-COS-MIB", jnxAtmCos=jnxAtmCos, jnxCosAtmTrunkQstatsOutLpBytes=jnxCosAtmTrunkQstatsOutLpBytes, jnxCosAtmVcScEntry=jnxCosAtmVcScEntry, jnxCosAtmTrunkMode=jnxCosAtmTrunkMode, jnxCosAtmTrunkScTxWeight=jnxCosAtmTrunkScTxWeight, jnxCosAtmTrunkEpdThresholdPlp0=jnxCosAtmTrunkEpdThresholdPlp0, jnxCosAtmTrunkQstatsOutHpPkts=jnxCosAtmTrunkQstatsOutHpPkts, jnxCosAtmVcQstatsEntry=jnxCosAtmVcQstatsEntry, jnxCosAtmVcScTxWeight=jnxCosAtmVcScTxWeight, jnxCosAtmVcQstatsOutPackets=jnxCosAtmVcQstatsOutPackets, jnxCosAtmTrunkScPriority=jnxCosAtmTrunkScPriority, jnxCosAtmVcTable=jnxCosAtmVcTable, jnxCosAtmVcScLrdpQueueDepth=jnxCosAtmVcScLrdpQueueDepth, jnxCosAtmTrunkQstatsOutBytes=jnxCosAtmTrunkQstatsOutBytes, jnxCosAtmVcQstatsOutBytes=jnxCosAtmVcQstatsOutBytes, jnxCosAtmVcQstatsTable=jnxCosAtmVcQstatsTable, jnxCosAtmTrunkQstatsOutDrops=jnxCosAtmTrunkQstatsOutDrops, jnxCosAtmVcScPriority=jnxCosAtmVcScPriority, jnxCosAtmTrunkQstatsOutLpDropPkts=jnxCosAtmTrunkQstatsOutLpDropPkts, jnxCosAtmVcCosMode=jnxCosAtmVcCosMode, jnxCosAtmTrunkScTxWeightType=jnxCosAtmTrunkScTxWeightType, jnxCosAtmTrunkQstatsOutHpBytes=jnxCosAtmTrunkQstatsOutHpBytes, jnxCosAtmVcQstatsOutHpDropPkts=jnxCosAtmVcQstatsOutHpDropPkts, jnxCosAtmTrunkQstatsOutLpPkts=jnxCosAtmTrunkQstatsOutLpPkts, jnxCosAtmTrunkQstatsOutLpDropBytes=jnxCosAtmTrunkQstatsOutLpDropBytes, jnxCosAtmTrunkQstatsOutHpDropBytes=jnxCosAtmTrunkQstatsOutHpDropBytes, jnxCosAtmVcQstatsOutLpPkts=jnxCosAtmVcQstatsOutLpPkts, PYSNMP_MODULE_ID=jnxAtmCos, jnxCosAtmVcQstatsOutLpBytes=jnxCosAtmVcQstatsOutLpBytes, jnxCosAtmTrunkEpdThresholdPlp1=jnxCosAtmTrunkEpdThresholdPlp1, jnxCosAtmVcScDpType=jnxCosAtmVcScDpType, jnxCosAtmVcQstatsOutRedDropPkts=jnxCosAtmVcQstatsOutRedDropPkts, jnxCosAtmVcEntry=jnxCosAtmVcEntry, jnxCosAtmVcEpdThreshold=jnxCosAtmVcEpdThreshold, jnxCosAtmTrunkTable=jnxCosAtmTrunkTable, jnxCosAtmTrunkQstatsOutPackets=jnxCosAtmTrunkQstatsOutPackets, jnxCosAtmVcScTable=jnxCosAtmVcScTable, jnxCosAtmTrunkEntry=jnxCosAtmTrunkEntry, jnxCosAtmVcQstatsOutLpDropBytes=jnxCosAtmVcQstatsOutLpDropBytes, jnxCosAtmVcQstatsOutHpDropBytes=jnxCosAtmVcQstatsOutHpDropBytes, jnxCosAtmVcScTxWeightType=jnxCosAtmVcScTxWeightType, jnxCosAtmVcQstatsOutNonRedDrops=jnxCosAtmVcQstatsOutNonRedDrops, jnxCosAtmTrunkQstatsOutHpDropPkts=jnxCosAtmTrunkQstatsOutHpDropPkts, jnxCosAtmVcScLrdpHighPlpThresh=jnxCosAtmVcScLrdpHighPlpThresh, jnxCosAtmTrunkQaType=jnxCosAtmTrunkQaType, jnxCosAtmVcScLrdpLowPlpThresh=jnxCosAtmVcScLrdpLowPlpThresh, jnxCosAtmVcQstatsOutLpDropPkts=jnxCosAtmVcQstatsOutLpDropPkts)

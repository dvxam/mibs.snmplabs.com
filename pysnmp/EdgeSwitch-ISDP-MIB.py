#
# PySNMP MIB module EdgeSwitch-ISDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-ISDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:56:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibIdentifier, IpAddress, NotificationType, Bits, Gauge32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Counter32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "IpAddress", "NotificationType", "Bits", "Gauge32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Counter32", "ObjectIdentity", "ModuleIdentity")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
fastPathIsdp = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39))
fastPathIsdp.setRevisions(('2011-01-26 00:00', '2010-01-11 00:00', '2007-12-03 00:00',))
if mibBuilder.loadTexts: fastPathIsdp.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathIsdp.setOrganization('Broadcom Inc')
agentIsdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1))
agentIsdpCache = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2))
agentIsdpInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 3))
agentIsdpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 3, 1), )
if mibBuilder.loadTexts: agentIsdpInterfaceTable.setStatus('current')
agentIsdpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 3, 1, 1), ).setIndexNames((0, "EdgeSwitch-ISDP-MIB", "agentIsdpInterfaceIfIndex"))
if mibBuilder.loadTexts: agentIsdpInterfaceEntry.setStatus('current')
agentIsdpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentIsdpInterfaceIfIndex.setStatus('current')
agentIsdpInterfaceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpInterfaceEnable.setStatus('current')
agentIsdpCacheTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1), )
if mibBuilder.loadTexts: agentIsdpCacheTable.setStatus('current')
agentIsdpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1), ).setIndexNames((0, "EdgeSwitch-ISDP-MIB", "agentIsdpCacheIfIndex"), (0, "EdgeSwitch-ISDP-MIB", "agentIsdpCacheIndex"))
if mibBuilder.loadTexts: agentIsdpCacheEntry.setStatus('current')
agentIsdpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentIsdpCacheIfIndex.setStatus('current')
agentIsdpCacheIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentIsdpCacheIndex.setStatus('current')
agentIsdpCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheAddress.setStatus('current')
agentIsdpCacheLocalIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheLocalIntf.setStatus('current')
agentIsdpCacheVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheVersion.setStatus('current')
agentIsdpCacheDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheDeviceId.setStatus('current')
agentIsdpCacheDevicePort = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheDevicePort.setStatus('current')
agentIsdpCachePlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCachePlatform.setStatus('current')
agentIsdpCacheCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheCapabilities.setStatus('current')
agentIsdpCacheLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheLastChange.setStatus('current')
agentIsdpCacheProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheProtocolVersion.setStatus('current')
agentIsdpCacheHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheHoldtime.setStatus('current')
agentIsdpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1))
agentIsdpClear = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 1))
agentIsdpClearStats = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalOperation", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpClearStats.setStatus('current')
agentIsdpClearEntries = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalOperation", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpClearEntries.setStatus('current')
agentIsdpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2))
agentIsdpStatisticsPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsPduReceived.setStatus('current')
agentIsdpStatisticsPduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsPduTransmit.setStatus('current')
agentIsdpStatisticsV1PduReceived = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV1PduReceived.setStatus('current')
agentIsdpStatisticsV1PduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV1PduTransmit.setStatus('current')
agentIsdpStatisticsV2PduReceived = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV2PduReceived.setStatus('current')
agentIsdpStatisticsV2PduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV2PduTransmit.setStatus('current')
agentIsdpStatisticsBadHeaderPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsBadHeaderPduReceived.setStatus('current')
agentIsdpStatisticsChkSumErrorPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsChkSumErrorPduReceived.setStatus('current')
agentIsdpStatisticsFailurePduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsFailurePduTransmit.setStatus('current')
agentIsdpStatisticsInvalidFormatPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsInvalidFormatPduReceived.setStatus('current')
agentIsdpStatisticsTableFull = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 11), Counter32()).setUnits('times').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsTableFull.setStatus('current')
agentIsdpStatisticsIpAddressTableFull = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 2, 12), Counter32()).setUnits('times').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsIpAddressTableFull.setStatus('current')
agentIsdpGlobalRun = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalRun.setStatus('current')
agentIsdpGlobalMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalMessageInterval.setStatus('current')
agentIsdpGlobalHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalHoldTime.setStatus('current')
agentIsdpGlobalDeviceId = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpGlobalDeviceId.setStatus('current')
agentIsdpGlobalAdvertiseV2 = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalAdvertiseV2.setStatus('current')
agentIsdpGlobalDeviceIdFormatCpb = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 9), Bits().clone(namedValues=NamedValues(("serialNumber", 1), ("macAddress", 2), ("other", 4), ("hostName", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpGlobalDeviceIdFormatCpb.setStatus('current')
agentIsdpGlobalDeviceIdFormat = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 39, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("serialNumber", 1), ("macAddress", 2), ("other", 3), ("hostName", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpGlobalDeviceIdFormat.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-ISDP-MIB", agentIsdpStatisticsFailurePduTransmit=agentIsdpStatisticsFailurePduTransmit, agentIsdpStatisticsBadHeaderPduReceived=agentIsdpStatisticsBadHeaderPduReceived, agentIsdpCacheTable=agentIsdpCacheTable, PYSNMP_MODULE_ID=fastPathIsdp, agentIsdpCacheHoldtime=agentIsdpCacheHoldtime, agentIsdpCacheIfIndex=agentIsdpCacheIfIndex, agentIsdpCacheDeviceId=agentIsdpCacheDeviceId, agentIsdpCacheLocalIntf=agentIsdpCacheLocalIntf, agentIsdpGlobalDeviceId=agentIsdpGlobalDeviceId, agentIsdpCachePlatform=agentIsdpCachePlatform, agentIsdpStatisticsTableFull=agentIsdpStatisticsTableFull, agentIsdpClear=agentIsdpClear, agentIsdpGlobalHoldTime=agentIsdpGlobalHoldTime, agentIsdpGlobalDeviceIdFormat=agentIsdpGlobalDeviceIdFormat, agentIsdpStatisticsPduTransmit=agentIsdpStatisticsPduTransmit, agentIsdpCacheEntry=agentIsdpCacheEntry, agentIsdpStatisticsIpAddressTableFull=agentIsdpStatisticsIpAddressTableFull, agentIsdpCacheVersion=agentIsdpCacheVersion, agentIsdpStatisticsChkSumErrorPduReceived=agentIsdpStatisticsChkSumErrorPduReceived, agentIsdpCacheDevicePort=agentIsdpCacheDevicePort, agentIsdpMIBObjects=agentIsdpMIBObjects, agentIsdpCacheIndex=agentIsdpCacheIndex, fastPathIsdp=fastPathIsdp, agentIsdpGlobal=agentIsdpGlobal, agentIsdpInterfaceTable=agentIsdpInterfaceTable, agentIsdpStatisticsInvalidFormatPduReceived=agentIsdpStatisticsInvalidFormatPduReceived, agentIsdpInterface=agentIsdpInterface, agentIsdpClearStats=agentIsdpClearStats, agentIsdpCacheAddress=agentIsdpCacheAddress, agentIsdpStatisticsV1PduTransmit=agentIsdpStatisticsV1PduTransmit, agentIsdpCacheCapabilities=agentIsdpCacheCapabilities, agentIsdpClearEntries=agentIsdpClearEntries, agentIsdpStatisticsV2PduReceived=agentIsdpStatisticsV2PduReceived, agentIsdpGlobalMessageInterval=agentIsdpGlobalMessageInterval, agentIsdpGlobalRun=agentIsdpGlobalRun, agentIsdpInterfaceEntry=agentIsdpInterfaceEntry, agentIsdpInterfaceIfIndex=agentIsdpInterfaceIfIndex, agentIsdpGlobalDeviceIdFormatCpb=agentIsdpGlobalDeviceIdFormatCpb, agentIsdpStatisticsPduReceived=agentIsdpStatisticsPduReceived, agentIsdpStatisticsV2PduTransmit=agentIsdpStatisticsV2PduTransmit, agentIsdpCacheLastChange=agentIsdpCacheLastChange, agentIsdpStatistics=agentIsdpStatistics, agentIsdpCacheProtocolVersion=agentIsdpCacheProtocolVersion, agentIsdpCache=agentIsdpCache, agentIsdpStatisticsV1PduReceived=agentIsdpStatisticsV1PduReceived, agentIsdpGlobalAdvertiseV2=agentIsdpGlobalAdvertiseV2, agentIsdpInterfaceEnable=agentIsdpInterfaceEnable)
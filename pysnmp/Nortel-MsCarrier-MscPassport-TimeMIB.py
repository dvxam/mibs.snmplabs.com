#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-TimeMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-TimeMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
StorageType, Counter32, RowStatus, DisplayString, RowPointer, Unsigned32, Integer32 = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "StorageType", "Counter32", "RowStatus", "DisplayString", "RowPointer", "Unsigned32", "Integer32")
EnterpriseDateAndTime, NonReplicated = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "EnterpriseDateAndTime", "NonReplicated")
mscPassportMIBs, mscComponents = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs", "mscComponents")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, Counter64, Counter32, TimeTicks, MibIdentifier, ObjectIdentity, ModuleIdentity, iso, NotificationType, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Counter64", "Counter32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "NotificationType", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
timeMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13))
mscTime = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19))
mscTimeRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1), )
if mibBuilder.loadTexts: mscTimeRowStatusTable.setStatus('mandatory')
mscTimeRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"))
if mibBuilder.loadTexts: mscTimeRowStatusEntry.setStatus('mandatory')
mscTimeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeRowStatus.setStatus('mandatory')
mscTimeComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeComponentName.setStatus('mandatory')
mscTimeStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeStorageType.setStatus('mandatory')
mscTimeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscTimeIndex.setStatus('mandatory')
mscTimeOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10), )
if mibBuilder.loadTexts: mscTimeOperTable.setStatus('mandatory')
mscTimeOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"))
if mibBuilder.loadTexts: mscTimeOperEntry.setStatus('mandatory')
mscTimeNetworkTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 1), EnterpriseDateAndTime().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(19, 19), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTimeNetworkTime.setStatus('obsolete')
mscTimeSyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 4, 5))).clone(namedValues=NamedValues(("synchronized", 0), ("unsynchronized", 1), ("synchronizing", 4), ("unspecified", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeSyncStatus.setStatus('mandatory')
mscTimeSyncSource = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeSyncSource.setStatus('obsolete')
mscTimeTimeOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTimeTimeOffset.setStatus('obsolete')
mscTimeModuleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 5), EnterpriseDateAndTime().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(19, 19), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTimeModuleTime.setStatus('mandatory')
mscTimeOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-720, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTimeOffset.setStatus('mandatory')
mscTimeMainServer = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeMainServer.setStatus('mandatory')
mscTimeXntpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeXntpVersion.setStatus('mandatory')
mscTimeSyncSourcesTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 391), )
if mibBuilder.loadTexts: mscTimeSyncSourcesTable.setStatus('mandatory')
mscTimeSyncSourcesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 391, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"), (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeSyncSourcesValue"))
if mibBuilder.loadTexts: mscTimeSyncSourcesEntry.setStatus('mandatory')
mscTimeSyncSourcesValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 391, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeSyncSourcesValue.setStatus('mandatory')
mscTimeServer = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3))
mscTimeServerRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1), )
if mibBuilder.loadTexts: mscTimeServerRowStatusTable.setStatus('mandatory')
mscTimeServerRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"), (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeServerIndex"))
if mibBuilder.loadTexts: mscTimeServerRowStatusEntry.setStatus('mandatory')
mscTimeServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTimeServerRowStatus.setStatus('mandatory')
mscTimeServerComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerComponentName.setStatus('mandatory')
mscTimeServerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerStorageType.setStatus('mandatory')
mscTimeServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: mscTimeServerIndex.setStatus('mandatory')
mscTimeServerProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 11), )
if mibBuilder.loadTexts: mscTimeServerProvTable.setStatus('mandatory')
mscTimeServerProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"), (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeServerIndex"))
if mibBuilder.loadTexts: mscTimeServerProvEntry.setStatus('mandatory')
mscTimeServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 11, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTimeServerIpAddress.setStatus('mandatory')
mscTimeServerIpStack = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipiFrIpiVc", 1), ("vrIp", 2))).clone('ipiFrIpiVc')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTimeServerIpStack.setStatus('mandatory')
mscTimeServerStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12), )
if mibBuilder.loadTexts: mscTimeServerStateTable.setStatus('mandatory')
mscTimeServerStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"), (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeServerIndex"))
if mibBuilder.loadTexts: mscTimeServerStateEntry.setStatus('mandatory')
mscTimeServerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerAdminState.setStatus('mandatory')
mscTimeServerOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerOperationalState.setStatus('mandatory')
mscTimeServerUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerUsageState.setStatus('mandatory')
mscTimeServerOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13), )
if mibBuilder.loadTexts: mscTimeServerOperTable.setStatus('mandatory')
mscTimeServerOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"), (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeServerIndex"))
if mibBuilder.loadTexts: mscTimeServerOperEntry.setStatus('mandatory')
mscTimeServerXntpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerXntpVersion.setStatus('mandatory')
mscTimeServerStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerStratum.setStatus('mandatory')
mscTimeServerPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerPoll.setStatus('mandatory')
mscTimeServerPktSent = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerPktSent.setStatus('mandatory')
mscTimeServerPktRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerPktRecv.setStatus('mandatory')
mscTimeServerPktValid = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerPktValid.setStatus('mandatory')
mscTimeServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 392), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeServerStatus.setStatus('mandatory')
mscNS = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20))
mscNSRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1), )
if mibBuilder.loadTexts: mscNSRowStatusTable.setStatus('mandatory')
mscNSRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscNSIndex"))
if mibBuilder.loadTexts: mscNSRowStatusEntry.setStatus('mandatory')
mscNSRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscNSRowStatus.setStatus('mandatory')
mscNSComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNSComponentName.setStatus('mandatory')
mscNSStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNSStorageType.setStatus('mandatory')
mscNSIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscNSIndex.setStatus('mandatory')
mscNSProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10), )
if mibBuilder.loadTexts: mscNSProvTable.setStatus('mandatory')
mscNSProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscNSIndex"))
if mibBuilder.loadTexts: mscNSProvEntry.setStatus('mandatory')
mscNSPrimaryReference = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10, 1, 1), RowPointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscNSPrimaryReference.setStatus('mandatory')
mscNSSecondaryReference = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10, 1, 2), RowPointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscNSSecondaryReference.setStatus('mandatory')
mscNSTertiaryReference = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10, 1, 3), RowPointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscNSTertiaryReference.setStatus('mandatory')
mscNSStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11), )
if mibBuilder.loadTexts: mscNSStateTable.setStatus('mandatory')
mscNSStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscNSIndex"))
if mibBuilder.loadTexts: mscNSStateEntry.setStatus('mandatory')
mscNSAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNSAdminState.setStatus('mandatory')
mscNSOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNSOperationalState.setStatus('mandatory')
mscNSUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNSUsageState.setStatus('mandatory')
mscNSOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12), )
if mibBuilder.loadTexts: mscNSOperTable.setStatus('mandatory')
mscNSOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscNSIndex"))
if mibBuilder.loadTexts: mscNSOperEntry.setStatus('mandatory')
mscNSClockSyncState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("freeRun", 0), ("synchronizing", 1), ("synchronized", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNSClockSyncState.setStatus('mandatory')
mscNSActiveReference = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNSActiveReference.setStatus('mandatory')
mscNSStandbyReference = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12, 1, 3), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNSStandbyReference.setStatus('mandatory')
timeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 1))
timeGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 1, 1))
timeGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 1, 1, 3))
timeGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 1, 1, 3, 2))
timeCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 3))
timeCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 3, 1))
timeCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 3, 1, 3))
timeCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-TimeMIB", mscTimeRowStatusEntry=mscTimeRowStatusEntry, mscNSTertiaryReference=mscNSTertiaryReference, mscTimeRowStatusTable=mscTimeRowStatusTable, mscTimeServerPoll=mscTimeServerPoll, mscNS=mscNS, mscNSProvTable=mscNSProvTable, mscTimeServer=mscTimeServer, mscTimeServerIpStack=mscTimeServerIpStack, mscNSIndex=mscNSIndex, mscNSStateTable=mscNSStateTable, mscTimeXntpVersion=mscTimeXntpVersion, mscTimeSyncSource=mscTimeSyncSource, mscTimeServerRowStatusEntry=mscTimeServerRowStatusEntry, mscNSUsageState=mscNSUsageState, mscNSPrimaryReference=mscNSPrimaryReference, mscNSSecondaryReference=mscNSSecondaryReference, mscTimeSyncSourcesTable=mscTimeSyncSourcesTable, mscTimeServerOperEntry=mscTimeServerOperEntry, mscNSOperationalState=mscNSOperationalState, mscTimeOffset=mscTimeOffset, mscTimeServerStateEntry=mscTimeServerStateEntry, mscTimeServerOperationalState=mscTimeServerOperationalState, mscNSRowStatus=mscNSRowStatus, mscNSProvEntry=mscNSProvEntry, mscTimeServerProvTable=mscTimeServerProvTable, mscTimeServerOperTable=mscTimeServerOperTable, mscNSStateEntry=mscNSStateEntry, mscTimeModuleTime=mscTimeModuleTime, mscTimeServerIndex=mscTimeServerIndex, mscTimeServerPktRecv=mscTimeServerPktRecv, mscTimeSyncSourcesEntry=mscTimeSyncSourcesEntry, mscNSActiveReference=mscNSActiveReference, mscTimeServerPktSent=mscTimeServerPktSent, mscTimeServerUsageState=mscTimeServerUsageState, mscTimeServerXntpVersion=mscTimeServerXntpVersion, mscTimeTimeOffset=mscTimeTimeOffset, mscTimeSyncSourcesValue=mscTimeSyncSourcesValue, mscTimeServerComponentName=mscTimeServerComponentName, mscNSOperEntry=mscNSOperEntry, mscNSClockSyncState=mscNSClockSyncState, timeGroup=timeGroup, timeGroupCA02A=timeGroupCA02A, mscTimeStorageType=mscTimeStorageType, mscTimeServerStatus=mscTimeServerStatus, mscNSRowStatusEntry=mscNSRowStatusEntry, mscTimeServerRowStatus=mscTimeServerRowStatus, mscNSStorageType=mscNSStorageType, mscTimeIndex=mscTimeIndex, mscTimeServerRowStatusTable=mscTimeServerRowStatusTable, mscTimeServerAdminState=mscTimeServerAdminState, mscTimeServerStateTable=mscTimeServerStateTable, mscNSOperTable=mscNSOperTable, mscTimeMainServer=mscTimeMainServer, mscTimeNetworkTime=mscTimeNetworkTime, timeMIB=timeMIB, mscTimeSyncStatus=mscTimeSyncStatus, mscTimeOperTable=mscTimeOperTable, mscTimeServerStratum=mscTimeServerStratum, mscTimeOperEntry=mscTimeOperEntry, timeGroupCA=timeGroupCA, timeGroupCA02=timeGroupCA02, mscTimeRowStatus=mscTimeRowStatus, mscNSComponentName=mscNSComponentName, timeCapabilitiesCA02=timeCapabilitiesCA02, timeCapabilitiesCA=timeCapabilitiesCA, mscTimeServerIpAddress=mscTimeServerIpAddress, mscTimeComponentName=mscTimeComponentName, mscNSRowStatusTable=mscNSRowStatusTable, mscTimeServerProvEntry=mscTimeServerProvEntry, mscTimeServerPktValid=mscTimeServerPktValid, mscNSStandbyReference=mscNSStandbyReference, mscTimeServerStorageType=mscTimeServerStorageType, mscNSAdminState=mscNSAdminState, timeCapabilities=timeCapabilities, timeCapabilitiesCA02A=timeCapabilitiesCA02A, mscTime=mscTime)

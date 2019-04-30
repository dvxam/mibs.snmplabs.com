#
# PySNMP MIB module CISCO-CHANNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CHANNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, Counter32, Bits, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Gauge32, Integer32, NotificationType, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Counter32", "Bits", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Gauge32", "Integer32", "NotificationType", "IpAddress", "Counter64")
TextualConvention, DisplayString, RowStatus, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TimeStamp", "TruthValue")
channel = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 20))
channel.setRevisions(('1998-01-06 00:00', '1998-08-14 00:00', '1997-03-26 00:00', '1996-06-13 00:00', '1995-09-25 00:00', '1994-11-17 00:00',))
if mibBuilder.loadTexts: channel.setLastUpdated('9703260000Z')
if mibBuilder.loadTexts: channel.setOrganization('cisco IBM engineering Working Group')
cipCard = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 20, 1))
cipCardTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1), )
if mibBuilder.loadTexts: cipCardTable.setStatus('current')
cipCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1), ).setIndexNames((0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"))
if mibBuilder.loadTexts: cipCardEntry.setStatus('current')
cipCardEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cipCardEntryIndex.setStatus('current')
cipCardEntryName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipCardEntryName.setStatus('current')
cipCardEntryTotalMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 3), Integer32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryTotalMemory.setStatus('current')
cipCardEntryFreeMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 4), Integer32()).setUnits('kilo bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryFreeMemory.setStatus('current')
cipCardEntryCpuUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryCpuUtilization.setStatus('current')
cipCardEntryTimeSinceLastReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 6), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryTimeSinceLastReset.setStatus('current')
cipCardEntryMajorSwRevisionNr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryMajorSwRevisionNr.setStatus('current')
cipCardEntryMinorSwRevisionNr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryMinorSwRevisionNr.setStatus('current')
cipCardEntryMajorHwRevisionNr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryMajorHwRevisionNr.setStatus('current')
cipCardEntryMinorHwRevisionNr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryMinorHwRevisionNr.setStatus('current')
cipCardEntryCpuLoad1m = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryCpuLoad1m.setStatus('current')
cipCardEntryCpuLoad5m = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryCpuLoad5m.setStatus('current')
cipCardEntryCpuLoad60m = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryCpuLoad60m.setStatus('current')
cipCardEntryDmaLoad1m = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryDmaLoad1m.setStatus('current')
cipCardEntryDmaLoad5m = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryDmaLoad5m.setStatus('current')
cipCardEntryDmaLoad60m = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardEntryDmaLoad60m.setStatus('current')
cipCardApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6), )
if mibBuilder.loadTexts: cipCardApplicationTable.setStatus('current')
cipCardApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6, 1), ).setIndexNames((0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardApplicationNameIndex"))
if mibBuilder.loadTexts: cipCardApplicationEntry.setStatus('current')
cipCardApplicationNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32))
if mibBuilder.loadTexts: cipCardApplicationNameIndex.setStatus('current')
cipCardApplicationRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardApplicationRevision.setStatus('current')
cipCardApplicationCompileInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardApplicationCompileInfo.setStatus('current')
cipCardDaughterBoardTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2), )
if mibBuilder.loadTexts: cipCardDaughterBoardTable.setStatus('current')
cipCardDaughterBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1), ).setIndexNames((0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"))
if mibBuilder.loadTexts: cipCardDaughterBoardEntry.setStatus('current')
cipCardDtrBrdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cipCardDtrBrdIndex.setStatus('current')
cipCardDtrBrdType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("escon", 1), ("busAndTag", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardDtrBrdType.setStatus('current')
cipCardDtrBrdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardDtrBrdStatus.setStatus('current')
cipCardDtrBrdSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardDtrBrdSignal.setStatus('current')
cipCardDtrBrdOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardDtrBrdOnline.setStatus('current')
implicitIncidents = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: implicitIncidents.setStatus('current')
codeViolationErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: codeViolationErrors.setStatus('current')
linkFailureSignalOrSyncLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkFailureSignalOrSyncLoss.setStatus('current')
linkFailureNOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkFailureNOSs.setStatus('current')
linkFailureSequenceTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkFailureSequenceTimeouts.setStatus('current')
linkFailureInvalidSequences = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkFailureInvalidSequences.setStatus('current')
linkIncidentTrapCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("liOther", 1), ("liStatus", 2), ("liImplicitIncidents", 3), ("liBERthreshold", 4), ("liSignalOrSyncLoss", 5), ("liNotOperationalSequence", 6), ("liSequenceTimeouts", 7), ("liInvalidSequences", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkIncidentTrapCause.setStatus('current')
cipCardDtrBrdLastStat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardDtrBrdLastStat.setStatus('current')
cipCardDtrBrdNextStat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardDtrBrdNextStat.setStatus('current')
cipCardDtrBrdChannelLoad1m = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardDtrBrdChannelLoad1m.setStatus('current')
cipCardDtrBrdChannelLoad5m = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardDtrBrdChannelLoad5m.setStatus('current')
cipCardDtrBrdChannelLoad60m = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardDtrBrdChannelLoad60m.setStatus('current')
cipCardSubChannelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3), )
if mibBuilder.loadTexts: cipCardSubChannelTable.setStatus('current')
cipCardSubChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1), ).setIndexNames((0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"))
if mibBuilder.loadTexts: cipCardSubChannelEntry.setStatus('current')
cipCardSubChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelIndex.setStatus('current')
cipCardSubChannelConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelConnections.setStatus('current')
cipCardSubChannelCancels = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelCancels.setStatus('current')
cipCardSubChannelSelectiveResets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelSelectiveResets.setStatus('current')
cipCardSubChannelSystemResets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelSystemResets.setStatus('current')
cipCardSubChannelDeviceErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelDeviceErrors.setStatus('current')
cipCardSubChannelWriteBlocksDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelWriteBlocksDropped.setStatus('current')
cipCardSubChannelLastSenseData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelLastSenseData.setStatus('current')
cipCardSubChannelLastSenseDataTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelLastSenseDataTime.setStatus('current')
cipCardSubChannelCuBusies = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelCuBusies.setStatus('current')
cipCardSubChannelCmdRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelCmdRetries.setStatus('current')
cipCardSubChannelResetEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelResetEvent.setStatus('current')
cipCardSubChannelShortBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelShortBusy.setStatus('current')
cipCardSubChannelCMDRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelCMDRetry.setStatus('current')
cipCardSubChannelBufferWait = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelBufferWait.setStatus('current')
cipCardSubChannelStatPending = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelStatPending.setStatus('current')
cipCardSubChannelSuspend = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelSuspend.setStatus('current')
cipCardSubChannelFBLWait = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardSubChannelFBLWait.setStatus('current')
cipCardClaw = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4))
cipCardClawTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 1), )
if mibBuilder.loadTexts: cipCardClawTable.setStatus('current')
cipCardClawEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardClawIndex"))
if mibBuilder.loadTexts: cipCardClawEntry.setStatus('current')
cipCardClawIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawIndex.setStatus('current')
cipCardClawConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawConnected.setStatus('current')
cipCardClawConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2), )
if mibBuilder.loadTexts: cipCardClawConfigTable.setStatus('current')
cipCardClawConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1), ).setIndexNames((0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardClawIndex"))
if mibBuilder.loadTexts: cipCardClawConfigEntry.setStatus('current')
cipCardClawConfigPath = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardClawConfigPath.setStatus('current')
cipCardClawConfigDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardClawConfigDevice.setStatus('current')
cipCardClawConfigIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardClawConfigIpAddr.setStatus('current')
cipCardClawConfigHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardClawConfigHostName.setStatus('current')
cipCardClawConfigRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardClawConfigRouterName.setStatus('current')
cipCardClawConfigHostAppl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardClawConfigHostAppl.setStatus('current')
cipCardClawConfigRouterAppl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardClawConfigRouterAppl.setStatus('current')
cipCardClawConfigBroadcastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 8), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardClawConfigBroadcastEnable.setStatus('current')
cipCardClawConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardClawConfigRowStatus.setStatus('current')
cipCardClawDataXferStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3), )
if mibBuilder.loadTexts: cipCardClawDataXferStatsTable.setStatus('current')
cipCardClawDataXferStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1), ).setIndexNames((0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"), (0, "CISCO-CHANNEL-MIB", "cipCardClawIndex"))
if mibBuilder.loadTexts: cipCardClawDataXferStatsEntry.setStatus('current')
cipCardClawDataXferStatsBlocksRead = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawDataXferStatsBlocksRead.setStatus('current')
cipCardClawDataXferStatsBlocksWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawDataXferStatsBlocksWritten.setStatus('current')
cipCardClawDataXferStatsBytesRead = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawDataXferStatsBytesRead.setStatus('current')
cipCardClawDataXferStatsHCBytesRead = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawDataXferStatsHCBytesRead.setStatus('current')
cipCardClawDataXferStatsBytesWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawDataXferStatsBytesWritten.setStatus('current')
cipCardClawDataXferStatsHCBytesWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawDataXferStatsHCBytesWritten.setStatus('current')
cipCardClawDataXferStatsReadBlocksDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawDataXferStatsReadBlocksDropped.setStatus('current')
cipCardClawDataXferStatsWriteBlocksDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawDataXferStatsWriteBlocksDropped.setStatus('current')
cipCardClawDataXferStatsBufferGetRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipCardClawDataXferStatsBufferGetRetryCount.setStatus('current')
cipCardTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 5))
cipCardLinkFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 5, 1)).setObjects(("CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdStatus"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdSignal"), ("CISCO-CHANNEL-MIB", "linkIncidentTrapCause"), ("CISCO-CHANNEL-MIB", "implicitIncidents"), ("CISCO-CHANNEL-MIB", "codeViolationErrors"), ("CISCO-CHANNEL-MIB", "linkFailureSignalOrSyncLoss"), ("CISCO-CHANNEL-MIB", "linkFailureNOSs"), ("CISCO-CHANNEL-MIB", "linkFailureSequenceTimeouts"), ("CISCO-CHANNEL-MIB", "linkFailureInvalidSequences"))
if mibBuilder.loadTexts: cipCardLinkFailure.setStatus('deprecated')
cipCardDtrBrdLinkFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 5, 2)).setObjects(("CISCO-CHANNEL-MIB", "cipCardDtrBrdStatus"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdSignal"), ("CISCO-CHANNEL-MIB", "linkIncidentTrapCause"))
if mibBuilder.loadTexts: cipCardDtrBrdLinkFailure.setStatus('current')
ciscoChannelMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 20, 2))
ciscoChannelMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 1))
ciscoChannelMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2))
ciscoChannelMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 1, 1)).setObjects(("CISCO-CHANNEL-MIB", "ciscoChannelGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoChannelMibCompliance = ciscoChannelMibCompliance.setStatus('current')
ciscoChannelMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 1, 2)).setObjects(("CISCO-CHANNEL-MIB", "ciscoChannelGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoChannelMibComplianceRev1 = ciscoChannelMibComplianceRev1.setStatus('current')
ciscoChannelMibComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 1, 3)).setObjects(("CISCO-CHANNEL-MIB", "ciscoChannelGroupRev1"), ("CISCO-CHANNEL-MIB", "ciscoChannelGroupRev2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoChannelMibComplianceRev2 = ciscoChannelMibComplianceRev2.setStatus('current')
ciscoChannelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2, 1)).setObjects(("CISCO-CHANNEL-MIB", "cipCardEntryName"), ("CISCO-CHANNEL-MIB", "cipCardEntryTotalMemory"), ("CISCO-CHANNEL-MIB", "cipCardEntryFreeMemory"), ("CISCO-CHANNEL-MIB", "cipCardEntryCpuUtilization"), ("CISCO-CHANNEL-MIB", "cipCardEntryTimeSinceLastReset"), ("CISCO-CHANNEL-MIB", "cipCardEntryMajorSwRevisionNr"), ("CISCO-CHANNEL-MIB", "cipCardEntryMinorSwRevisionNr"), ("CISCO-CHANNEL-MIB", "cipCardEntryMajorHwRevisionNr"), ("CISCO-CHANNEL-MIB", "cipCardEntryMinorHwRevisionNr"), ("CISCO-CHANNEL-MIB", "cipCardApplicationRevision"), ("CISCO-CHANNEL-MIB", "cipCardApplicationCompileInfo"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdType"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdStatus"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdSignal"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdOnline"), ("CISCO-CHANNEL-MIB", "implicitIncidents"), ("CISCO-CHANNEL-MIB", "codeViolationErrors"), ("CISCO-CHANNEL-MIB", "linkFailureSignalOrSyncLoss"), ("CISCO-CHANNEL-MIB", "linkFailureNOSs"), ("CISCO-CHANNEL-MIB", "linkFailureSequenceTimeouts"), ("CISCO-CHANNEL-MIB", "linkFailureInvalidSequences"), ("CISCO-CHANNEL-MIB", "linkIncidentTrapCause"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelConnections"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelCancels"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelSelectiveResets"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelSystemResets"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelDeviceErrors"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelWriteBlocksDropped"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelLastSenseData"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelLastSenseDataTime"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelCuBusies"), ("CISCO-CHANNEL-MIB", "cipCardClawIndex"), ("CISCO-CHANNEL-MIB", "cipCardClawConnected"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigPath"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigDevice"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigIpAddr"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigHostName"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigRouterName"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigHostAppl"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigRouterAppl"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBlocksRead"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBlocksWritten"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBytesRead"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsHCBytesRead"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBytesWritten"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsHCBytesWritten"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsReadBlocksDropped"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsWriteBlocksDropped"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBufferGetRetryCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoChannelGroup = ciscoChannelGroup.setStatus('current')
ciscoChannelGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2, 2)).setObjects(("CISCO-CHANNEL-MIB", "cipCardEntryName"), ("CISCO-CHANNEL-MIB", "cipCardEntryTotalMemory"), ("CISCO-CHANNEL-MIB", "cipCardEntryFreeMemory"), ("CISCO-CHANNEL-MIB", "cipCardEntryCpuUtilization"), ("CISCO-CHANNEL-MIB", "cipCardEntryTimeSinceLastReset"), ("CISCO-CHANNEL-MIB", "cipCardEntryMajorSwRevisionNr"), ("CISCO-CHANNEL-MIB", "cipCardEntryMinorSwRevisionNr"), ("CISCO-CHANNEL-MIB", "cipCardEntryMajorHwRevisionNr"), ("CISCO-CHANNEL-MIB", "cipCardEntryMinorHwRevisionNr"), ("CISCO-CHANNEL-MIB", "cipCardApplicationRevision"), ("CISCO-CHANNEL-MIB", "cipCardApplicationCompileInfo"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdType"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdStatus"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdSignal"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdOnline"), ("CISCO-CHANNEL-MIB", "implicitIncidents"), ("CISCO-CHANNEL-MIB", "codeViolationErrors"), ("CISCO-CHANNEL-MIB", "linkFailureSignalOrSyncLoss"), ("CISCO-CHANNEL-MIB", "linkFailureNOSs"), ("CISCO-CHANNEL-MIB", "linkFailureSequenceTimeouts"), ("CISCO-CHANNEL-MIB", "linkFailureInvalidSequences"), ("CISCO-CHANNEL-MIB", "linkIncidentTrapCause"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdLastStat"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdNextStat"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelConnections"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelCancels"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelSelectiveResets"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelSystemResets"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelDeviceErrors"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelWriteBlocksDropped"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelLastSenseData"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelLastSenseDataTime"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelCuBusies"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelCmdRetries"), ("CISCO-CHANNEL-MIB", "cipCardClawIndex"), ("CISCO-CHANNEL-MIB", "cipCardClawConnected"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigPath"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigDevice"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigIpAddr"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigHostName"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigRouterName"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigHostAppl"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigRouterAppl"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBlocksRead"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBlocksWritten"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBytesRead"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsHCBytesRead"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBytesWritten"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsHCBytesWritten"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsReadBlocksDropped"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsWriteBlocksDropped"), ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBufferGetRetryCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoChannelGroupRev1 = ciscoChannelGroupRev1.setStatus('current')
ciscoChannelGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2, 3)).setObjects(("CISCO-CHANNEL-MIB", "cipCardEntryCpuLoad1m"), ("CISCO-CHANNEL-MIB", "cipCardEntryCpuLoad5m"), ("CISCO-CHANNEL-MIB", "cipCardEntryCpuLoad60m"), ("CISCO-CHANNEL-MIB", "cipCardEntryDmaLoad1m"), ("CISCO-CHANNEL-MIB", "cipCardEntryDmaLoad5m"), ("CISCO-CHANNEL-MIB", "cipCardEntryDmaLoad60m"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdChannelLoad1m"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdChannelLoad5m"), ("CISCO-CHANNEL-MIB", "cipCardDtrBrdChannelLoad60m"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigBroadcastEnable"), ("CISCO-CHANNEL-MIB", "cipCardClawConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoChannelGroupRev2 = ciscoChannelGroupRev2.setStatus('current')
ciscoChannelGroupRev3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2, 4)).setObjects(("CISCO-CHANNEL-MIB", "cipCardSubChannelResetEvent"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelShortBusy"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelCMDRetry"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelBufferWait"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelStatPending"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelSuspend"), ("CISCO-CHANNEL-MIB", "cipCardSubChannelFBLWait"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoChannelGroupRev3 = ciscoChannelGroupRev3.setStatus('current')
mibBuilder.exportSymbols("CISCO-CHANNEL-MIB", cipCardClawDataXferStatsTable=cipCardClawDataXferStatsTable, cipCardClawConfigTable=cipCardClawConfigTable, cipCardApplicationNameIndex=cipCardApplicationNameIndex, cipCardClawDataXferStatsHCBytesWritten=cipCardClawDataXferStatsHCBytesWritten, linkIncidentTrapCause=linkIncidentTrapCause, cipCardClawDataXferStatsBlocksWritten=cipCardClawDataXferStatsBlocksWritten, ciscoChannelMibCompliance=ciscoChannelMibCompliance, cipCardSubChannelCMDRetry=cipCardSubChannelCMDRetry, ciscoChannelMibComplianceRev1=ciscoChannelMibComplianceRev1, ciscoChannelMibConformance=ciscoChannelMibConformance, cipCardEntryDmaLoad5m=cipCardEntryDmaLoad5m, ciscoChannelGroupRev1=ciscoChannelGroupRev1, cipCardDtrBrdChannelLoad1m=cipCardDtrBrdChannelLoad1m, cipCardSubChannelConnections=cipCardSubChannelConnections, cipCardSubChannelBufferWait=cipCardSubChannelBufferWait, cipCardLinkFailure=cipCardLinkFailure, cipCardDaughterBoardEntry=cipCardDaughterBoardEntry, cipCardSubChannelResetEvent=cipCardSubChannelResetEvent, cipCardDtrBrdLinkFailure=cipCardDtrBrdLinkFailure, cipCardClawDataXferStatsBufferGetRetryCount=cipCardClawDataXferStatsBufferGetRetryCount, cipCardEntryMajorSwRevisionNr=cipCardEntryMajorSwRevisionNr, PYSNMP_MODULE_ID=channel, cipCardTable=cipCardTable, cipCardTraps=cipCardTraps, cipCardSubChannelCmdRetries=cipCardSubChannelCmdRetries, cipCardSubChannelIndex=cipCardSubChannelIndex, cipCardSubChannelShortBusy=cipCardSubChannelShortBusy, cipCardApplicationRevision=cipCardApplicationRevision, cipCardDtrBrdChannelLoad60m=cipCardDtrBrdChannelLoad60m, cipCardEntryCpuLoad1m=cipCardEntryCpuLoad1m, cipCardDaughterBoardTable=cipCardDaughterBoardTable, cipCardClawConfigPath=cipCardClawConfigPath, cipCardClawConfigRowStatus=cipCardClawConfigRowStatus, cipCardDtrBrdOnline=cipCardDtrBrdOnline, cipCardEntryMinorHwRevisionNr=cipCardEntryMinorHwRevisionNr, cipCardClawDataXferStatsWriteBlocksDropped=cipCardClawDataXferStatsWriteBlocksDropped, ciscoChannelGroup=ciscoChannelGroup, linkFailureNOSs=linkFailureNOSs, cipCardEntryCpuLoad5m=cipCardEntryCpuLoad5m, channel=channel, cipCardClawIndex=cipCardClawIndex, cipCardSubChannelSelectiveResets=cipCardSubChannelSelectiveResets, cipCardClawConfigDevice=cipCardClawConfigDevice, cipCardSubChannelDeviceErrors=cipCardSubChannelDeviceErrors, cipCardClawConfigRouterName=cipCardClawConfigRouterName, cipCardSubChannelLastSenseData=cipCardSubChannelLastSenseData, cipCardSubChannelEntry=cipCardSubChannelEntry, linkFailureSignalOrSyncLoss=linkFailureSignalOrSyncLoss, cipCardClawConfigHostAppl=cipCardClawConfigHostAppl, ciscoChannelGroupRev2=ciscoChannelGroupRev2, codeViolationErrors=codeViolationErrors, ciscoChannelMibCompliances=ciscoChannelMibCompliances, cipCardSubChannelLastSenseDataTime=cipCardSubChannelLastSenseDataTime, cipCardClawConfigHostName=cipCardClawConfigHostName, cipCardEntryCpuLoad60m=cipCardEntryCpuLoad60m, cipCardEntryFreeMemory=cipCardEntryFreeMemory, cipCardSubChannelSystemResets=cipCardSubChannelSystemResets, ciscoChannelMibComplianceRev2=ciscoChannelMibComplianceRev2, cipCardDtrBrdIndex=cipCardDtrBrdIndex, ciscoChannelMibGroups=ciscoChannelMibGroups, implicitIncidents=implicitIncidents, cipCardClawConfigIpAddr=cipCardClawConfigIpAddr, cipCardClawDataXferStatsEntry=cipCardClawDataXferStatsEntry, cipCardClaw=cipCardClaw, cipCardSubChannelFBLWait=cipCardSubChannelFBLWait, cipCardEntry=cipCardEntry, cipCardClawConnected=cipCardClawConnected, cipCardClawTable=cipCardClawTable, cipCardClawDataXferStatsBytesRead=cipCardClawDataXferStatsBytesRead, cipCardSubChannelCancels=cipCardSubChannelCancels, cipCardApplicationEntry=cipCardApplicationEntry, cipCardSubChannelTable=cipCardSubChannelTable, cipCardEntryDmaLoad60m=cipCardEntryDmaLoad60m, cipCardDtrBrdStatus=cipCardDtrBrdStatus, cipCardDtrBrdNextStat=cipCardDtrBrdNextStat, linkFailureSequenceTimeouts=linkFailureSequenceTimeouts, cipCardClawEntry=cipCardClawEntry, cipCardEntryDmaLoad1m=cipCardEntryDmaLoad1m, cipCardClawConfigRouterAppl=cipCardClawConfigRouterAppl, cipCardEntryMinorSwRevisionNr=cipCardEntryMinorSwRevisionNr, linkFailureInvalidSequences=linkFailureInvalidSequences, cipCard=cipCard, cipCardEntryMajorHwRevisionNr=cipCardEntryMajorHwRevisionNr, cipCardDtrBrdLastStat=cipCardDtrBrdLastStat, cipCardClawDataXferStatsBlocksRead=cipCardClawDataXferStatsBlocksRead, cipCardClawDataXferStatsReadBlocksDropped=cipCardClawDataXferStatsReadBlocksDropped, cipCardClawConfigBroadcastEnable=cipCardClawConfigBroadcastEnable, cipCardEntryName=cipCardEntryName, ciscoChannelGroupRev3=ciscoChannelGroupRev3, cipCardClawDataXferStatsBytesWritten=cipCardClawDataXferStatsBytesWritten, cipCardClawConfigEntry=cipCardClawConfigEntry, cipCardEntryTimeSinceLastReset=cipCardEntryTimeSinceLastReset, cipCardApplicationCompileInfo=cipCardApplicationCompileInfo, cipCardEntryTotalMemory=cipCardEntryTotalMemory, cipCardDtrBrdType=cipCardDtrBrdType, cipCardSubChannelStatPending=cipCardSubChannelStatPending, cipCardSubChannelSuspend=cipCardSubChannelSuspend, cipCardClawDataXferStatsHCBytesRead=cipCardClawDataXferStatsHCBytesRead, cipCardSubChannelWriteBlocksDropped=cipCardSubChannelWriteBlocksDropped, cipCardEntryIndex=cipCardEntryIndex, cipCardSubChannelCuBusies=cipCardSubChannelCuBusies, cipCardApplicationTable=cipCardApplicationTable, cipCardDtrBrdChannelLoad5m=cipCardDtrBrdChannelLoad5m, cipCardDtrBrdSignal=cipCardDtrBrdSignal, cipCardEntryCpuUtilization=cipCardEntryCpuUtilization)

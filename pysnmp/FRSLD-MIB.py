#
# PySNMP MIB module FRSLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FRSLD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
DLCI, = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "DLCI")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Counter64, ModuleIdentity, MibIdentifier, NotificationType, TimeTicks, Integer32, mib_2, ObjectIdentity, IpAddress, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ModuleIdentity", "MibIdentifier", "NotificationType", "TimeTicks", "Integer32", "mib-2", "ObjectIdentity", "IpAddress", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32")
DisplayString, RowStatus, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TimeStamp", "TextualConvention")
frsldMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 95))
frsldMIB.setRevisions(('2002-01-03 00:00',))
if mibBuilder.loadTexts: frsldMIB.setLastUpdated('200201030000Z')
if mibBuilder.loadTexts: frsldMIB.setOrganization('IETF Frame Relay Service MIB Working Group')
class FrsldTxRP(TextualConvention, Integer32):
    reference = 'FRF.13: Section 2.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("srcLocalRP", 1), ("ingTxLocalRP", 2), ("tpTxLocalRP", 3), ("eqiTxLocalRP", 4), ("eqoTxLocalRP", 5), ("otherTxLocalRP", 6), ("srcRemoteRP", 7), ("ingTxRemoteRP", 8), ("tpTxRemoteRP", 9), ("eqiTxRemoteRP", 10), ("eqoTxRemoteRP", 11), ("otherTxRemoteRP", 12))

class FrsldRxRP(TextualConvention, Integer32):
    reference = 'FRF.13: Section 2.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("desLocalRP", 1), ("ingRxLocalRP", 2), ("tpRxLocalRP", 3), ("eqiRxLocalRP", 4), ("eqoRxLocalRP", 5), ("otherRxLocalRP", 6), ("desRemoteRP", 7), ("ingRxRemoteRP", 8), ("tpRxRemoteRP", 9), ("eqiRxRemoteRP", 10), ("eqoRxRemoteRP", 11), ("otherRxRemoteRP", 12))

frsldObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 1))
frsldCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 2))
frsldConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 3))
frsldPvcCtrlTable = MibTable((1, 3, 6, 1, 2, 1, 95, 1, 1), )
if mibBuilder.loadTexts: frsldPvcCtrlTable.setStatus('current')
frsldPvcCtrlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 95, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FRSLD-MIB", "frsldPvcCtrlDlci"), (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"), (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"))
if mibBuilder.loadTexts: frsldPvcCtrlEntry.setStatus('current')
frsldPvcCtrlDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 1), DLCI())
if mibBuilder.loadTexts: frsldPvcCtrlDlci.setStatus('current')
frsldPvcCtrlTransmitRP = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 2), FrsldTxRP())
if mibBuilder.loadTexts: frsldPvcCtrlTransmitRP.setStatus('current')
frsldPvcCtrlReceiveRP = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 3), FrsldRxRP())
if mibBuilder.loadTexts: frsldPvcCtrlReceiveRP.setStatus('current')
frsldPvcCtrlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldPvcCtrlStatus.setStatus('current')
frsldPvcCtrlPacketFreq = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldPvcCtrlPacketFreq.setStatus('current')
frsldPvcCtrlDelayFrSize = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8188)).clone(128)).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldPvcCtrlDelayFrSize.setStatus('current')
frsldPvcCtrlDelayType = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oneWay", 1), ("roundTrip", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldPvcCtrlDelayType.setStatus('current')
frsldPvcCtrlDelayTimeOut = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldPvcCtrlDelayTimeOut.setStatus('current')
frsldPvcCtrlPurge = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 172800))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldPvcCtrlPurge.setStatus('current')
frsldPvcCtrlDeleteOnPurge = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("sampleContols", 2), ("all", 3))).clone('all')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldPvcCtrlDeleteOnPurge.setStatus('current')
frsldPvcCtrlLastPurgeTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcCtrlLastPurgeTime.setStatus('current')
frsldSmplCtrlTable = MibTable((1, 3, 6, 1, 2, 1, 95, 1, 2), )
if mibBuilder.loadTexts: frsldSmplCtrlTable.setStatus('current')
frsldSmplCtrlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 95, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FRSLD-MIB", "frsldPvcCtrlDlci"), (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"), (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"), (0, "FRSLD-MIB", "frsldSmplCtrlIdx"))
if mibBuilder.loadTexts: frsldSmplCtrlEntry.setStatus('current')
frsldSmplCtrlIdx = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: frsldSmplCtrlIdx.setStatus('current')
frsldSmplCtrlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldSmplCtrlStatus.setStatus('current')
frsldSmplCtrlColPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldSmplCtrlColPeriod.setStatus('current')
frsldSmplCtrlBuckets = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frsldSmplCtrlBuckets.setStatus('current')
frsldSmplCtrlBucketsGranted = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldSmplCtrlBucketsGranted.setStatus('current')
frsldPvcDataTable = MibTable((1, 3, 6, 1, 2, 1, 95, 1, 3), )
if mibBuilder.loadTexts: frsldPvcDataTable.setStatus('current')
frsldPvcDataEntry = MibTableRow((1, 3, 6, 1, 2, 1, 95, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FRSLD-MIB", "frsldPvcCtrlDlci"), (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"), (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"))
if mibBuilder.loadTexts: frsldPvcDataEntry.setStatus('current')
frsldPvcDataMissedPolls = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataMissedPolls.setStatus('current')
frsldPvcDataFrDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataFrDeliveredC.setStatus('current')
frsldPvcDataFrDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataFrDeliveredE.setStatus('current')
frsldPvcDataFrOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataFrOfferedC.setStatus('current')
frsldPvcDataFrOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataFrOfferedE.setStatus('current')
frsldPvcDataDataDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataDataDeliveredC.setStatus('current')
frsldPvcDataDataDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataDataDeliveredE.setStatus('current')
frsldPvcDataDataOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataDataOfferedC.setStatus('current')
frsldPvcDataDataOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataDataOfferedE.setStatus('current')
frsldPvcDataHCFrDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataHCFrDeliveredC.setStatus('current')
frsldPvcDataHCFrDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataHCFrDeliveredE.setStatus('current')
frsldPvcDataHCFrOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataHCFrOfferedC.setStatus('current')
frsldPvcDataHCFrOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataHCFrOfferedE.setStatus('current')
frsldPvcDataHCDataDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataHCDataDeliveredC.setStatus('current')
frsldPvcDataHCDataDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataHCDataDeliveredE.setStatus('current')
frsldPvcDataHCDataOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataHCDataOfferedC.setStatus('current')
frsldPvcDataHCDataOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataHCDataOfferedE.setStatus('current')
frsldPvcDataUnavailableTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 18), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataUnavailableTime.setStatus('current')
frsldPvcDataUnavailables = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcDataUnavailables.setStatus('current')
frsldPvcSampleTable = MibTable((1, 3, 6, 1, 2, 1, 95, 1, 4), )
if mibBuilder.loadTexts: frsldPvcSampleTable.setStatus('current')
frsldPvcSampleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 95, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FRSLD-MIB", "frsldPvcCtrlDlci"), (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"), (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"), (0, "FRSLD-MIB", "frsldSmplCtrlIdx"), (0, "FRSLD-MIB", "frsldPvcSmplIdx"))
if mibBuilder.loadTexts: frsldPvcSampleEntry.setStatus('current')
frsldPvcSmplIdx = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: frsldPvcSmplIdx.setStatus('current')
frsldPvcSmplDelayMin = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 2), Gauge32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplDelayMin.setStatus('current')
frsldPvcSmplDelayMax = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 3), Gauge32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplDelayMax.setStatus('current')
frsldPvcSmplDelayAvg = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 4), Gauge32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplDelayAvg.setStatus('current')
frsldPvcSmplMissedPolls = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplMissedPolls.setStatus('current')
frsldPvcSmplFrDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplFrDeliveredC.setStatus('current')
frsldPvcSmplFrDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplFrDeliveredE.setStatus('current')
frsldPvcSmplFrOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplFrOfferedC.setStatus('current')
frsldPvcSmplFrOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplFrOfferedE.setStatus('current')
frsldPvcSmplDataDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplDataDeliveredC.setStatus('current')
frsldPvcSmplDataDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplDataDeliveredE.setStatus('current')
frsldPvcSmplDataOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplDataOfferedC.setStatus('current')
frsldPvcSmplDataOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplDataOfferedE.setStatus('current')
frsldPvcSmplHCFrDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 14), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplHCFrDeliveredC.setStatus('current')
frsldPvcSmplHCFrDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 15), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplHCFrDeliveredE.setStatus('current')
frsldPvcSmplHCFrOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 16), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplHCFrOfferedC.setStatus('current')
frsldPvcSmplHCFrOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 17), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplHCFrOfferedE.setStatus('current')
frsldPvcSmplHCDataDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 18), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplHCDataDeliveredC.setStatus('current')
frsldPvcSmplHCDataDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 19), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplHCDataDeliveredE.setStatus('current')
frsldPvcSmplHCDataOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 20), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplHCDataOfferedC.setStatus('current')
frsldPvcSmplHCDataOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 21), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplHCDataOfferedE.setStatus('current')
frsldPvcSmplUnavailableTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 22), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplUnavailableTime.setStatus('current')
frsldPvcSmplUnavailables = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 23), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplUnavailables.setStatus('current')
frsldPvcSmplStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 24), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplStartTime.setStatus('current')
frsldPvcSmplEndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 25), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcSmplEndTime.setStatus('current')
frsldPvcCtrlWriteCaps = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 1), Bits().clone(namedValues=NamedValues(("frsldPvcCtrlStatus", 0), ("frsldPvcCtrlPacketFreq", 1), ("frsldPvcCtrlDelayFrSize", 2), ("frsldPvcCtrlDelayType", 3), ("frsldPvcCtrlDelayTimeOut", 4), ("frsldPvcCtrlPurge", 5), ("frsldPvcCtrlDeleteOnPurge", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldPvcCtrlWriteCaps.setStatus('current')
frsldSmplCtrlWriteCaps = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 2), Bits().clone(namedValues=NamedValues(("frsldSmplCtrlStatus", 0), ("frsldSmplCtrlBuckets", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldSmplCtrlWriteCaps.setStatus('current')
frsldRPCaps = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 3), Bits().clone(namedValues=NamedValues(("srcLocalRP", 0), ("ingTxLocalRP", 1), ("tpTxLocalRP", 2), ("eqiTxLocalRP", 3), ("eqoTxLocalRP", 4), ("otherTxLocalRP", 5), ("srcRemoteRP", 6), ("ingTxRemoteRP", 7), ("tpTxRemoteRP", 8), ("eqiTxRemoteRP", 9), ("eqoTxRemoteRP", 10), ("otherTxRemoteRP", 11), ("desLocalRP", 12), ("ingRxLocalRP", 13), ("tpRxLocalRP", 14), ("eqiRxLocalRP", 15), ("eqoRxLocalRP", 16), ("otherRxLocalRP", 17), ("desRemoteRP", 18), ("ingRxRemoteRP", 19), ("tpRxRemoteRP", 20), ("eqiRxRemoteRP", 21), ("eqoRxRemoteRP", 22), ("otherRxRemoteRP", 23)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldRPCaps.setStatus('current')
frsldMaxPvcCtrls = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frsldMaxPvcCtrls.setStatus('current')
frsldNumPvcCtrls = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldNumPvcCtrls.setStatus('current')
frsldMaxSmplCtrls = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frsldMaxSmplCtrls.setStatus('current')
frsldNumSmplCtrls = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsldNumSmplCtrls.setStatus('current')
frsldMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 3, 1))
frsldMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 3, 2))
frsldCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 95, 3, 2, 1)).setObjects(("FRSLD-MIB", "frsldPvcReqCtrlGroup"), ("FRSLD-MIB", "frsldPvcReqDataGroup"), ("FRSLD-MIB", "frsldCapabilitiesGroup"), ("FRSLD-MIB", "frsldPvcHCFrameDataGroup"), ("FRSLD-MIB", "frsldPvcHCOctetDataGroup"), ("FRSLD-MIB", "frsldPvcPacketGroup"), ("FRSLD-MIB", "frsldPvcDelayCtrlGroup"), ("FRSLD-MIB", "frsldPvcSampleCtrlGroup"), ("FRSLD-MIB", "frsldPvcDelayDataGroup"), ("FRSLD-MIB", "frsldPvcSampleDelayGroup"), ("FRSLD-MIB", "frsldPvcSampleDataGroup"), ("FRSLD-MIB", "frsldPvcSampleHCFrameGroup"), ("FRSLD-MIB", "frsldPvcSampleHCDataGroup"), ("FRSLD-MIB", "frsldPvcSampleAvailGroup"), ("FRSLD-MIB", "frsldPvcSampleGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldCompliance = frsldCompliance.setStatus('current')
frsldPvcReqCtrlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 1)).setObjects(("FRSLD-MIB", "frsldPvcCtrlStatus"), ("FRSLD-MIB", "frsldPvcCtrlPurge"), ("FRSLD-MIB", "frsldPvcCtrlDeleteOnPurge"), ("FRSLD-MIB", "frsldPvcCtrlLastPurgeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcReqCtrlGroup = frsldPvcReqCtrlGroup.setStatus('current')
frsldPvcPacketGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 2)).setObjects(("FRSLD-MIB", "frsldPvcCtrlPacketFreq"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcPacketGroup = frsldPvcPacketGroup.setStatus('current')
frsldPvcDelayCtrlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 3)).setObjects(("FRSLD-MIB", "frsldPvcCtrlDelayFrSize"), ("FRSLD-MIB", "frsldPvcCtrlDelayType"), ("FRSLD-MIB", "frsldPvcCtrlDelayTimeOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcDelayCtrlGroup = frsldPvcDelayCtrlGroup.setStatus('current')
frsldPvcSampleCtrlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 4)).setObjects(("FRSLD-MIB", "frsldSmplCtrlStatus"), ("FRSLD-MIB", "frsldSmplCtrlColPeriod"), ("FRSLD-MIB", "frsldSmplCtrlBuckets"), ("FRSLD-MIB", "frsldSmplCtrlBucketsGranted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcSampleCtrlGroup = frsldPvcSampleCtrlGroup.setStatus('current')
frsldPvcReqDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 5)).setObjects(("FRSLD-MIB", "frsldPvcDataFrDeliveredC"), ("FRSLD-MIB", "frsldPvcDataFrDeliveredE"), ("FRSLD-MIB", "frsldPvcDataFrOfferedC"), ("FRSLD-MIB", "frsldPvcDataFrOfferedE"), ("FRSLD-MIB", "frsldPvcDataDataDeliveredC"), ("FRSLD-MIB", "frsldPvcDataDataDeliveredE"), ("FRSLD-MIB", "frsldPvcDataDataOfferedC"), ("FRSLD-MIB", "frsldPvcDataDataOfferedE"), ("FRSLD-MIB", "frsldPvcDataUnavailableTime"), ("FRSLD-MIB", "frsldPvcDataUnavailables"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcReqDataGroup = frsldPvcReqDataGroup.setStatus('current')
frsldPvcDelayDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 6)).setObjects(("FRSLD-MIB", "frsldPvcDataMissedPolls"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcDelayDataGroup = frsldPvcDelayDataGroup.setStatus('current')
frsldPvcHCFrameDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 7)).setObjects(("FRSLD-MIB", "frsldPvcDataHCFrDeliveredC"), ("FRSLD-MIB", "frsldPvcDataHCFrDeliveredE"), ("FRSLD-MIB", "frsldPvcDataHCFrOfferedC"), ("FRSLD-MIB", "frsldPvcDataHCFrOfferedE"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcHCFrameDataGroup = frsldPvcHCFrameDataGroup.setStatus('current')
frsldPvcHCOctetDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 8)).setObjects(("FRSLD-MIB", "frsldPvcDataHCDataDeliveredC"), ("FRSLD-MIB", "frsldPvcDataHCDataDeliveredE"), ("FRSLD-MIB", "frsldPvcDataHCDataOfferedC"), ("FRSLD-MIB", "frsldPvcDataHCDataOfferedE"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcHCOctetDataGroup = frsldPvcHCOctetDataGroup.setStatus('current')
frsldPvcSampleDelayGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 9)).setObjects(("FRSLD-MIB", "frsldPvcSmplDelayMin"), ("FRSLD-MIB", "frsldPvcSmplDelayMax"), ("FRSLD-MIB", "frsldPvcSmplDelayAvg"), ("FRSLD-MIB", "frsldPvcSmplMissedPolls"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcSampleDelayGroup = frsldPvcSampleDelayGroup.setStatus('current')
frsldPvcSampleDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 10)).setObjects(("FRSLD-MIB", "frsldPvcSmplFrDeliveredC"), ("FRSLD-MIB", "frsldPvcSmplFrDeliveredE"), ("FRSLD-MIB", "frsldPvcSmplFrOfferedC"), ("FRSLD-MIB", "frsldPvcSmplFrOfferedE"), ("FRSLD-MIB", "frsldPvcSmplDataDeliveredC"), ("FRSLD-MIB", "frsldPvcSmplDataDeliveredE"), ("FRSLD-MIB", "frsldPvcSmplDataOfferedC"), ("FRSLD-MIB", "frsldPvcSmplDataOfferedE"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcSampleDataGroup = frsldPvcSampleDataGroup.setStatus('current')
frsldPvcSampleHCFrameGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 11)).setObjects(("FRSLD-MIB", "frsldPvcSmplHCFrDeliveredC"), ("FRSLD-MIB", "frsldPvcSmplHCFrDeliveredE"), ("FRSLD-MIB", "frsldPvcSmplHCFrOfferedC"), ("FRSLD-MIB", "frsldPvcSmplHCFrOfferedE"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcSampleHCFrameGroup = frsldPvcSampleHCFrameGroup.setStatus('current')
frsldPvcSampleHCDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 12)).setObjects(("FRSLD-MIB", "frsldPvcSmplHCDataDeliveredC"), ("FRSLD-MIB", "frsldPvcSmplHCDataDeliveredE"), ("FRSLD-MIB", "frsldPvcSmplHCDataOfferedC"), ("FRSLD-MIB", "frsldPvcSmplHCDataOfferedE"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcSampleHCDataGroup = frsldPvcSampleHCDataGroup.setStatus('current')
frsldPvcSampleAvailGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 13)).setObjects(("FRSLD-MIB", "frsldPvcSmplUnavailableTime"), ("FRSLD-MIB", "frsldPvcSmplUnavailables"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcSampleAvailGroup = frsldPvcSampleAvailGroup.setStatus('current')
frsldPvcSampleGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 14)).setObjects(("FRSLD-MIB", "frsldPvcSmplStartTime"), ("FRSLD-MIB", "frsldPvcSmplEndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldPvcSampleGeneralGroup = frsldPvcSampleGeneralGroup.setStatus('current')
frsldCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 15)).setObjects(("FRSLD-MIB", "frsldPvcCtrlWriteCaps"), ("FRSLD-MIB", "frsldSmplCtrlWriteCaps"), ("FRSLD-MIB", "frsldRPCaps"), ("FRSLD-MIB", "frsldMaxPvcCtrls"), ("FRSLD-MIB", "frsldNumPvcCtrls"), ("FRSLD-MIB", "frsldMaxSmplCtrls"), ("FRSLD-MIB", "frsldNumSmplCtrls"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frsldCapabilitiesGroup = frsldCapabilitiesGroup.setStatus('current')
mibBuilder.exportSymbols("FRSLD-MIB", FrsldRxRP=FrsldRxRP, frsldPvcDataFrOfferedC=frsldPvcDataFrOfferedC, frsldSmplCtrlBuckets=frsldSmplCtrlBuckets, frsldPvcCtrlTransmitRP=frsldPvcCtrlTransmitRP, frsldPvcSmplDelayMax=frsldPvcSmplDelayMax, frsldPvcSmplEndTime=frsldPvcSmplEndTime, frsldPvcReqCtrlGroup=frsldPvcReqCtrlGroup, frsldPvcSampleGeneralGroup=frsldPvcSampleGeneralGroup, frsldPvcDataFrDeliveredE=frsldPvcDataFrDeliveredE, frsldPvcSampleCtrlGroup=frsldPvcSampleCtrlGroup, frsldCapabilities=frsldCapabilities, frsldMIBGroups=frsldMIBGroups, frsldPvcCtrlStatus=frsldPvcCtrlStatus, frsldPvcCtrlTable=frsldPvcCtrlTable, frsldPvcSampleAvailGroup=frsldPvcSampleAvailGroup, FrsldTxRP=FrsldTxRP, frsldPvcDataDataDeliveredC=frsldPvcDataDataDeliveredC, frsldPvcSmplDataOfferedE=frsldPvcSmplDataOfferedE, frsldPvcCtrlEntry=frsldPvcCtrlEntry, frsldPvcCtrlDelayType=frsldPvcCtrlDelayType, frsldPvcDataHCDataDeliveredE=frsldPvcDataHCDataDeliveredE, frsldPvcCtrlReceiveRP=frsldPvcCtrlReceiveRP, frsldPvcCtrlDelayFrSize=frsldPvcCtrlDelayFrSize, frsldPvcSmplIdx=frsldPvcSmplIdx, frsldSmplCtrlWriteCaps=frsldSmplCtrlWriteCaps, frsldPvcCtrlPurge=frsldPvcCtrlPurge, frsldPvcCtrlDlci=frsldPvcCtrlDlci, frsldPvcSampleHCDataGroup=frsldPvcSampleHCDataGroup, frsldMIBCompliances=frsldMIBCompliances, frsldNumSmplCtrls=frsldNumSmplCtrls, frsldPvcDataTable=frsldPvcDataTable, frsldSmplCtrlTable=frsldSmplCtrlTable, frsldCompliance=frsldCompliance, frsldSmplCtrlIdx=frsldSmplCtrlIdx, frsldPvcCtrlWriteCaps=frsldPvcCtrlWriteCaps, frsldPvcCtrlLastPurgeTime=frsldPvcCtrlLastPurgeTime, frsldPvcDataHCFrDeliveredE=frsldPvcDataHCFrDeliveredE, frsldRPCaps=frsldRPCaps, frsldSmplCtrlBucketsGranted=frsldSmplCtrlBucketsGranted, frsldPvcSmplFrOfferedE=frsldPvcSmplFrOfferedE, frsldPvcSmplHCDataOfferedC=frsldPvcSmplHCDataOfferedC, frsldConformance=frsldConformance, frsldPvcDelayCtrlGroup=frsldPvcDelayCtrlGroup, frsldPvcSmplHCFrOfferedC=frsldPvcSmplHCFrOfferedC, frsldMIB=frsldMIB, frsldPvcSmplUnavailableTime=frsldPvcSmplUnavailableTime, frsldPvcHCOctetDataGroup=frsldPvcHCOctetDataGroup, frsldPvcSmplUnavailables=frsldPvcSmplUnavailables, frsldPvcDataHCFrDeliveredC=frsldPvcDataHCFrDeliveredC, frsldPvcDataEntry=frsldPvcDataEntry, frsldMaxPvcCtrls=frsldMaxPvcCtrls, PYSNMP_MODULE_ID=frsldMIB, frsldPvcSmplHCDataDeliveredC=frsldPvcSmplHCDataDeliveredC, frsldPvcSmplStartTime=frsldPvcSmplStartTime, frsldPvcSmplDataDeliveredE=frsldPvcSmplDataDeliveredE, frsldObjects=frsldObjects, frsldPvcSampleTable=frsldPvcSampleTable, frsldPvcSmplFrDeliveredC=frsldPvcSmplFrDeliveredC, frsldPvcCtrlDelayTimeOut=frsldPvcCtrlDelayTimeOut, frsldPvcDataHCFrOfferedE=frsldPvcDataHCFrOfferedE, frsldPvcDataUnavailableTime=frsldPvcDataUnavailableTime, frsldPvcSmplDataOfferedC=frsldPvcSmplDataOfferedC, frsldPvcSmplDelayAvg=frsldPvcSmplDelayAvg, frsldCapabilitiesGroup=frsldCapabilitiesGroup, frsldPvcSmplFrOfferedC=frsldPvcSmplFrOfferedC, frsldPvcCtrlPacketFreq=frsldPvcCtrlPacketFreq, frsldPvcDataDataDeliveredE=frsldPvcDataDataDeliveredE, frsldPvcSampleHCFrameGroup=frsldPvcSampleHCFrameGroup, frsldPvcSmplFrDeliveredE=frsldPvcSmplFrDeliveredE, frsldPvcHCFrameDataGroup=frsldPvcHCFrameDataGroup, frsldMaxSmplCtrls=frsldMaxSmplCtrls, frsldPvcDataDataOfferedE=frsldPvcDataDataOfferedE, frsldPvcDelayDataGroup=frsldPvcDelayDataGroup, frsldPvcDataFrOfferedE=frsldPvcDataFrOfferedE, frsldPvcDataHCFrOfferedC=frsldPvcDataHCFrOfferedC, frsldPvcSmplDataDeliveredC=frsldPvcSmplDataDeliveredC, frsldPvcDataMissedPolls=frsldPvcDataMissedPolls, frsldPvcDataHCDataDeliveredC=frsldPvcDataHCDataDeliveredC, frsldPvcDataHCDataOfferedC=frsldPvcDataHCDataOfferedC, frsldPvcSmplHCFrDeliveredE=frsldPvcSmplHCFrDeliveredE, frsldPvcSmplHCDataOfferedE=frsldPvcSmplHCDataOfferedE, frsldPvcSmplHCFrOfferedE=frsldPvcSmplHCFrOfferedE, frsldSmplCtrlStatus=frsldSmplCtrlStatus, frsldPvcSampleDataGroup=frsldPvcSampleDataGroup, frsldPvcDataHCDataOfferedE=frsldPvcDataHCDataOfferedE, frsldPvcDataUnavailables=frsldPvcDataUnavailables, frsldPvcPacketGroup=frsldPvcPacketGroup, frsldPvcReqDataGroup=frsldPvcReqDataGroup, frsldPvcSmplHCFrDeliveredC=frsldPvcSmplHCFrDeliveredC, frsldPvcDataDataOfferedC=frsldPvcDataDataOfferedC, frsldNumPvcCtrls=frsldNumPvcCtrls, frsldPvcDataFrDeliveredC=frsldPvcDataFrDeliveredC, frsldPvcSampleEntry=frsldPvcSampleEntry, frsldSmplCtrlEntry=frsldSmplCtrlEntry, frsldPvcSmplDelayMin=frsldPvcSmplDelayMin, frsldPvcCtrlDeleteOnPurge=frsldPvcCtrlDeleteOnPurge, frsldPvcSmplHCDataDeliveredE=frsldPvcSmplHCDataDeliveredE, frsldPvcSmplMissedPolls=frsldPvcSmplMissedPolls, frsldSmplCtrlColPeriod=frsldSmplCtrlColPeriod, frsldPvcSampleDelayGroup=frsldPvcSampleDelayGroup)
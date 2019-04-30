#
# PySNMP MIB module NMS-IEEE8023-LAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-IEEE8023-LAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nmslocal, = mibBuilder.importSymbols("NMS-SMI", "nmslocal")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Bits, ModuleIdentity, Integer32, Counter64, Gauge32, Unsigned32, TimeTicks, ObjectIdentity, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Bits", "ModuleIdentity", "Integer32", "Counter64", "Gauge32", "Unsigned32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress")
DisplayString, RowStatus, TruthValue, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "MacAddress", "TextualConvention")
lagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232))
if mibBuilder.loadTexts: lagMIB.setLastUpdated('201005180000Z')
if mibBuilder.loadTexts: lagMIB.setOrganization('')
lagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1))
class LacpKey(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class LacpState(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lacpActivity", 0), ("lacpTimeout", 1), ("aggregation", 2), ("synchronization", 3), ("collecting", 4), ("distributing", 5), ("defaulted", 6), ("expired", 7))

class ChurnState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noChurn", 1), ("churn", 2), ("churnMonitor", 3))

class LagMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("lacpActive", 1), ("lacpPassive", 2), ("static", 3))

dot3adAgg = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1))
dot3adAggPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2))
dot3adTablesLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adTablesLastChanged.setStatus('current')
dot3adAggMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggMaxNum.setStatus('current')
dot3adAggPortsMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortsMaxNum.setStatus('current')
dot3adAggTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1), )
if mibBuilder.loadTexts: dot3adAggTable.setStatus('current')
dot3adAggEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1), ).setIndexNames((0, "NMS-IEEE8023-LAG-MIB", "dot3adAggIndex"))
if mibBuilder.loadTexts: dot3adAggEntry.setStatus('current')
dot3adAggIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dot3adAggIndex.setStatus('current')
dot3adAggMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggMACAddress.setStatus('current')
dot3adAggActorSystemPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggActorSystemPriority.setStatus('current')
dot3adAggActorSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggActorSystemID.setStatus('current')
dot3adAggAggregateOrIndividual = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggAggregateOrIndividual.setStatus('current')
dot3adAggActorAdminKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 6), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggActorAdminKey.setStatus('current')
dot3adAggActorOperKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 7), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggActorOperKey.setStatus('current')
dot3adAggPartnerSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPartnerSystemID.setStatus('current')
dot3adAggPartnerSystemPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPartnerSystemPriority.setStatus('current')
dot3adAggPartnerOperKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 10), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPartnerOperKey.setStatus('current')
dot3adAggCollectorMaxDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggCollectorMaxDelay.setStatus('current')
dot3adAggIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 12), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggIfIndex.setStatus('current')
dot3adAggAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 13), LagMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggAdminMode.setStatus('current')
dot3adAggOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 14), LagMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggOperMode.setStatus('current')
dot3adAggRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot3adAggRowStatus.setStatus('current')
dot3adAggPortListTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 2), )
if mibBuilder.loadTexts: dot3adAggPortListTable.setStatus('current')
dot3adAggPortListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 2, 1), ).setIndexNames((0, "NMS-IEEE8023-LAG-MIB", "dot3adAggIndex"))
if mibBuilder.loadTexts: dot3adAggPortListEntry.setStatus('current')
dot3adAggPortListPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 2, 1, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortListPorts.setStatus('current')
dot3adAggPortListAggregatedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 2, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortListAggregatedPorts.setStatus('current')
dot3adAggPortTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1), )
if mibBuilder.loadTexts: dot3adAggPortTable.setStatus('current')
dot3adAggPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1), ).setIndexNames((0, "NMS-IEEE8023-LAG-MIB", "dot3adAggPortIndex"))
if mibBuilder.loadTexts: dot3adAggPortEntry.setStatus('current')
dot3adAggPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dot3adAggPortIndex.setStatus('current')
dot3adAggPortActorSystemPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorSystemPriority.setStatus('current')
dot3adAggPortActorSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorSystemID.setStatus('current')
dot3adAggPortActorAdminKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 4), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorAdminKey.setStatus('current')
dot3adAggPortActorOperKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 5), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorOperKey.setStatus('current')
dot3adAggPortPartnerAdminSystemPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminSystemPriority.setStatus('current')
dot3adAggPortPartnerOperSystemPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperSystemPriority.setStatus('current')
dot3adAggPortPartnerAdminSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminSystemID.setStatus('current')
dot3adAggPortPartnerOperSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperSystemID.setStatus('current')
dot3adAggPortPartnerAdminKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 10), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminKey.setStatus('current')
dot3adAggPortPartnerOperKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 11), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperKey.setStatus('current')
dot3adAggPortSelectedAggID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 12), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortSelectedAggID.setStatus('current')
dot3adAggPortAttachedAggID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 13), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortAttachedAggID.setStatus('current')
dot3adAggPortActorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorPort.setStatus('current')
dot3adAggPortActorPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorPortPriority.setStatus('current')
dot3adAggPortPartnerAdminPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminPort.setStatus('current')
dot3adAggPortPartnerOperPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperPort.setStatus('current')
dot3adAggPortPartnerAdminPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminPortPriority.setStatus('current')
dot3adAggPortPartnerOperPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperPortPriority.setStatus('current')
dot3adAggPortActorAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 20), LacpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorAdminState.setStatus('current')
dot3adAggPortActorOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 21), LacpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorOperState.setStatus('current')
dot3adAggPortPartnerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 22), LacpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminState.setStatus('current')
dot3adAggPortPartnerOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 23), LacpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperState.setStatus('current')
dot3adAggPortAggregateOrIndividual = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortAggregateOrIndividual.setStatus('current')
dot3adAggPortOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 25), LagMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortOperMode.setStatus('current')
dot3adAggPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2), )
if mibBuilder.loadTexts: dot3adAggPortStatsTable.setStatus('current')
dot3adAggPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1), ).setIndexNames((0, "NMS-IEEE8023-LAG-MIB", "dot3adAggPortIndex"))
if mibBuilder.loadTexts: dot3adAggPortStatsEntry.setStatus('current')
dot3adAggPortStatsLACPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsLACPDUsRx.setStatus('current')
dot3adAggPortStatsMarkerPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsMarkerPDUsRx.setStatus('current')
dot3adAggPortStatsMarkerResponsePDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsMarkerResponsePDUsRx.setStatus('current')
dot3adAggPortStatsUnknownRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsUnknownRx.setStatus('current')
dot3adAggPortStatsIllegalRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsIllegalRx.setStatus('current')
dot3adAggPortStatsLACPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsLACPDUsTx.setStatus('current')
dot3adAggPortStatsMarkerPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsMarkerPDUsTx.setStatus('current')
dot3adAggPortStatsMarkerResponsePDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsMarkerResponsePDUsTx.setStatus('current')
dot3adAggPortDebugTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3), )
if mibBuilder.loadTexts: dot3adAggPortDebugTable.setStatus('current')
dot3adAggPortDebugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1), ).setIndexNames((0, "NMS-IEEE8023-LAG-MIB", "dot3adAggPortIndex"))
if mibBuilder.loadTexts: dot3adAggPortDebugEntry.setStatus('current')
dot3adAggPortDebugRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("currentRx", 1), ("expired", 2), ("defaulted", 3), ("initialize", 4), ("lacpDisabled", 5), ("portDisabled", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugRxState.setStatus('current')
dot3adAggPortDebugLastRxTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugLastRxTime.setStatus('current')
dot3adAggPortDebugMuxState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("detached", 1), ("waiting", 2), ("attached", 3), ("collecting", 4), ("distributing", 5), ("collectingDistributing", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugMuxState.setStatus('current')
dot3adAggPortDebugMuxReason = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugMuxReason.setStatus('current')
dot3adAggPortDebugActorChurnState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 5), ChurnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugActorChurnState.setStatus('current')
dot3adAggPortDebugPartnerChurnState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 6), ChurnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugPartnerChurnState.setStatus('current')
dot3adAggPortDebugActorChurnCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugActorChurnCount.setStatus('current')
dot3adAggPortDebugPartnerChurnCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugPartnerChurnCount.setStatus('current')
dot3adAggPortDebugActorSyncTransitionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugActorSyncTransitionCount.setStatus('current')
dot3adAggPortDebugPartnerSyncTransitionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugPartnerSyncTransitionCount.setStatus('current')
dot3adAggPortDebugActorChangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugActorChangeCount.setStatus('current')
dot3adAggPortDebugPartnerChangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugPartnerChangeCount.setStatus('current')
dot3adAggConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2))
dot3adAggGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1))
dot3adAggCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 2))
dot3adAggGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 1)).setObjects(("NMS-IEEE8023-LAG-MIB", "dot3adAggActorSystemID"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggActorSystemPriority"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggAggregateOrIndividual"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggActorAdminKey"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggMACAddress"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggActorOperKey"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPartnerSystemID"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPartnerSystemPriority"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPartnerOperKey"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggCollectorMaxDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggGroup = dot3adAggGroup.setStatus('current')
dot3adAggPortListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 2)).setObjects(("NMS-IEEE8023-LAG-MIB", "dot3adAggPortListPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggPortListGroup = dot3adAggPortListGroup.setStatus('current')
dot3adAggPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 3)).setObjects(("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorSystemPriority"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorSystemID"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorAdminKey"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorOperKey"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminSystemPriority"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperSystemPriority"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminSystemID"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperSystemID"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminKey"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperKey"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortSelectedAggID"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortAttachedAggID"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorPort"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorPortPriority"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminPort"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperPort"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminPortPriority"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperPortPriority"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorAdminState"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorOperState"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminState"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperState"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortAggregateOrIndividual"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggPortGroup = dot3adAggPortGroup.setStatus('current')
dot3adAggPortStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 4)).setObjects(("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsLACPDUsRx"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerPDUsRx"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerResponsePDUsRx"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsUnknownRx"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsIllegalRx"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsLACPDUsTx"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerPDUsTx"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerResponsePDUsTx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggPortStatsGroup = dot3adAggPortStatsGroup.setStatus('current')
dot3adAggPortDebugGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 5)).setObjects(("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugRxState"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugLastRxTime"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugMuxState"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugMuxReason"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChurnState"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChurnState"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChurnCount"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChurnCount"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugActorSyncTransitionCount"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerSyncTransitionCount"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChangeCount"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChangeCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggPortDebugGroup = dot3adAggPortDebugGroup.setStatus('current')
dot3adTablesLastChangedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 1, 6)).setObjects(("NMS-IEEE8023-LAG-MIB", "dot3adTablesLastChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adTablesLastChangedGroup = dot3adTablesLastChangedGroup.setStatus('current')
dot3adAggCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 2, 1)).setObjects(("NMS-IEEE8023-LAG-MIB", "dot3adAggGroup"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortGroup"), ("NMS-IEEE8023-LAG-MIB", "dot3adTablesLastChangedGroup"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortListGroup"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsGroup"), ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggCompliance = dot3adAggCompliance.setStatus('current')
mibBuilder.exportSymbols("NMS-IEEE8023-LAG-MIB", dot3adAggPortDebugEntry=dot3adAggPortDebugEntry, dot3adAggPortDebugActorChurnState=dot3adAggPortDebugActorChurnState, dot3adAggOperMode=dot3adAggOperMode, dot3adAggPortIndex=dot3adAggPortIndex, dot3adAggPortDebugActorSyncTransitionCount=dot3adAggPortDebugActorSyncTransitionCount, dot3adAggPortTable=dot3adAggPortTable, dot3adAggPortPartnerAdminPort=dot3adAggPortPartnerAdminPort, dot3adAggPortStatsMarkerResponsePDUsTx=dot3adAggPortStatsMarkerResponsePDUsTx, dot3adAggPortDebugPartnerChurnState=dot3adAggPortDebugPartnerChurnState, dot3adAggPortPartnerOperState=dot3adAggPortPartnerOperState, dot3adAggPortPartnerAdminKey=dot3adAggPortPartnerAdminKey, dot3adAggPort=dot3adAggPort, LagMode=LagMode, dot3adAggPortActorAdminState=dot3adAggPortActorAdminState, dot3adAggCollectorMaxDelay=dot3adAggCollectorMaxDelay, dot3adAggPortListTable=dot3adAggPortListTable, dot3adAggPortAggregateOrIndividual=dot3adAggPortAggregateOrIndividual, dot3adAggActorOperKey=dot3adAggActorOperKey, dot3adAggPortStatsGroup=dot3adAggPortStatsGroup, LacpState=LacpState, dot3adAggPortListGroup=dot3adAggPortListGroup, dot3adAggPortPartnerAdminState=dot3adAggPortPartnerAdminState, dot3adAggPortDebugActorChangeCount=dot3adAggPortDebugActorChangeCount, dot3adAggPartnerSystemID=dot3adAggPartnerSystemID, dot3adAggPortOperMode=dot3adAggPortOperMode, dot3adAggAdminMode=dot3adAggAdminMode, dot3adAgg=dot3adAgg, dot3adAggActorSystemID=dot3adAggActorSystemID, dot3adAggPortDebugActorChurnCount=dot3adAggPortDebugActorChurnCount, dot3adAggMaxNum=dot3adAggMaxNum, dot3adAggPortStatsLACPDUsRx=dot3adAggPortStatsLACPDUsRx, dot3adAggPortStatsIllegalRx=dot3adAggPortStatsIllegalRx, dot3adAggPortActorPort=dot3adAggPortActorPort, dot3adAggPortDebugLastRxTime=dot3adAggPortDebugLastRxTime, dot3adAggPortActorOperKey=dot3adAggPortActorOperKey, dot3adAggPortStatsUnknownRx=dot3adAggPortStatsUnknownRx, dot3adAggPortAttachedAggID=dot3adAggPortAttachedAggID, dot3adAggPortDebugPartnerSyncTransitionCount=dot3adAggPortDebugPartnerSyncTransitionCount, dot3adAggPortSelectedAggID=dot3adAggPortSelectedAggID, dot3adAggPortEntry=dot3adAggPortEntry, dot3adAggPortDebugGroup=dot3adAggPortDebugGroup, lagMIBObjects=lagMIBObjects, dot3adAggPartnerSystemPriority=dot3adAggPartnerSystemPriority, lagMIB=lagMIB, dot3adAggEntry=dot3adAggEntry, dot3adAggPortPartnerOperPortPriority=dot3adAggPortPartnerOperPortPriority, dot3adAggPortStatsEntry=dot3adAggPortStatsEntry, ChurnState=ChurnState, dot3adAggPortPartnerAdminSystemID=dot3adAggPortPartnerAdminSystemID, dot3adAggPortActorSystemPriority=dot3adAggPortActorSystemPriority, dot3adAggPortActorOperState=dot3adAggPortActorOperState, dot3adAggPortStatsTable=dot3adAggPortStatsTable, dot3adAggPortStatsMarkerResponsePDUsRx=dot3adAggPortStatsMarkerResponsePDUsRx, LacpKey=LacpKey, dot3adAggPortsMaxNum=dot3adAggPortsMaxNum, dot3adAggPortDebugMuxState=dot3adAggPortDebugMuxState, dot3adAggPortDebugMuxReason=dot3adAggPortDebugMuxReason, dot3adAggMACAddress=dot3adAggMACAddress, dot3adAggIfIndex=dot3adAggIfIndex, dot3adAggPortActorAdminKey=dot3adAggPortActorAdminKey, dot3adAggRowStatus=dot3adAggRowStatus, dot3adAggActorSystemPriority=dot3adAggActorSystemPriority, dot3adAggGroup=dot3adAggGroup, dot3adAggGroups=dot3adAggGroups, dot3adAggPortListEntry=dot3adAggPortListEntry, dot3adAggPortActorPortPriority=dot3adAggPortActorPortPriority, dot3adAggCompliances=dot3adAggCompliances, dot3adAggConformance=dot3adAggConformance, dot3adAggPortListAggregatedPorts=dot3adAggPortListAggregatedPorts, dot3adAggPartnerOperKey=dot3adAggPartnerOperKey, dot3adAggPortDebugPartnerChangeCount=dot3adAggPortDebugPartnerChangeCount, dot3adAggPortDebugPartnerChurnCount=dot3adAggPortDebugPartnerChurnCount, dot3adAggPortPartnerAdminSystemPriority=dot3adAggPortPartnerAdminSystemPriority, PYSNMP_MODULE_ID=lagMIB, dot3adAggPortStatsMarkerPDUsTx=dot3adAggPortStatsMarkerPDUsTx, dot3adTablesLastChanged=dot3adTablesLastChanged, dot3adAggPortStatsLACPDUsTx=dot3adAggPortStatsLACPDUsTx, dot3adAggPortListPorts=dot3adAggPortListPorts, dot3adAggTable=dot3adAggTable, dot3adAggPortPartnerOperPort=dot3adAggPortPartnerOperPort, dot3adAggIndex=dot3adAggIndex, dot3adTablesLastChangedGroup=dot3adTablesLastChangedGroup, dot3adAggAggregateOrIndividual=dot3adAggAggregateOrIndividual, dot3adAggCompliance=dot3adAggCompliance, dot3adAggPortPartnerOperSystemPriority=dot3adAggPortPartnerOperSystemPriority, dot3adAggPortStatsMarkerPDUsRx=dot3adAggPortStatsMarkerPDUsRx, dot3adAggPortDebugTable=dot3adAggPortDebugTable, dot3adAggPortPartnerOperKey=dot3adAggPortPartnerOperKey, dot3adAggPortActorSystemID=dot3adAggPortActorSystemID, dot3adAggPortPartnerOperSystemID=dot3adAggPortPartnerOperSystemID, dot3adAggPortDebugRxState=dot3adAggPortDebugRxState, dot3adAggPortGroup=dot3adAggPortGroup, dot3adAggActorAdminKey=dot3adAggActorAdminKey, dot3adAggPortPartnerAdminPortPriority=dot3adAggPortPartnerAdminPortPriority)

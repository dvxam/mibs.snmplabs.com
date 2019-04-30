#
# PySNMP MIB module CISCO-ITP-GSP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-GSP2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cgspInstNetwork, = mibBuilder.importSymbols("CISCO-ITP-GSP-MIB", "cgspInstNetwork")
CItpTcXuaName, CItpTcPointCode, CItpTcLinksetId, CItpTcNetworkName, CItpTcAclId, CItpTcLinkSLC = mibBuilder.importSymbols("CISCO-ITP-TC-MIB", "CItpTcXuaName", "CItpTcPointCode", "CItpTcLinksetId", "CItpTcNetworkName", "CItpTcAclId", "CItpTcLinkSLC")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, ModuleIdentity, TimeTicks, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Counter64, IpAddress, Integer32, iso, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Counter64", "IpAddress", "Integer32", "iso", "Bits", "Unsigned32")
TextualConvention, RowStatus, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TimeStamp")
ciscoGsp2MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 332))
ciscoGsp2MIB.setRevisions(('2008-07-09 00:00', '2007-12-18 00:00', '2004-05-26 00:00', '2003-08-07 00:00', '2003-03-03 00:00',))
if mibBuilder.loadTexts: ciscoGsp2MIB.setLastUpdated('200807090000Z')
if mibBuilder.loadTexts: ciscoGsp2MIB.setOrganization('Cisco Systems, Inc.')
ciscoGsp2MIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 0))
ciscoGsp2MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 1))
ciscoGsp2MIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 2))
cgsp2Events = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1))
cgsp2Qos = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2))
cgsp2LocalPeer = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3))
cgsp2Mtp3Errors = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4))
cgsp2Operation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 5))
cgsp2Context = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6))
class Cgsp2TcQosClass(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class Cgsp2EventIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class CItpTcContextId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CItpTcContextType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 6))
    namedValues = NamedValues(("unknown", 0), ("cs7link", 1), ("asp", 6))

cgsp2EventTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1), )
if mibBuilder.loadTexts: cgsp2EventTable.setStatus('current')
cgsp2EventTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventType"))
if mibBuilder.loadTexts: cgsp2EventTableEntry.setStatus('current')
cgsp2EventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("as", 1), ("asp", 2), ("mtp3", 3), ("pc", 4))))
if mibBuilder.loadTexts: cgsp2EventType.setStatus('current')
cgsp2EventLoggedEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventLoggedEvents.setStatus('current')
cgsp2EventDroppedEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventDroppedEvents.setStatus('current')
cgsp2EventMaxEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgsp2EventMaxEntries.setStatus('current')
cgsp2EventMaxEntriesAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventMaxEntriesAllowed.setStatus('current')
cgsp2EventAsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2), )
if mibBuilder.loadTexts: cgsp2EventAsTable.setStatus('current')
cgsp2EventAsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventAsName"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventAsIndex"))
if mibBuilder.loadTexts: cgsp2EventAsTableEntry.setStatus('current')
cgsp2EventAsName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1, 1), CItpTcXuaName())
if mibBuilder.loadTexts: cgsp2EventAsName.setStatus('current')
cgsp2EventAsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1, 2), Cgsp2EventIndex())
if mibBuilder.loadTexts: cgsp2EventAsIndex.setStatus('current')
cgsp2EventAsText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventAsText.setStatus('current')
cgsp2EventAsTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventAsTimestamp.setStatus('current')
cgsp2EventAspTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3), )
if mibBuilder.loadTexts: cgsp2EventAspTable.setStatus('current')
cgsp2EventAspTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventAspName"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventAspIndex"))
if mibBuilder.loadTexts: cgsp2EventAspTableEntry.setStatus('current')
cgsp2EventAspName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1, 1), CItpTcXuaName())
if mibBuilder.loadTexts: cgsp2EventAspName.setStatus('current')
cgsp2EventAspIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1, 2), Cgsp2EventIndex())
if mibBuilder.loadTexts: cgsp2EventAspIndex.setStatus('current')
cgsp2EventAspText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventAspText.setStatus('current')
cgsp2EventAspTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventAspTimestamp.setStatus('current')
cgsp2EventMtp3Table = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4), )
if mibBuilder.loadTexts: cgsp2EventMtp3Table.setStatus('current')
cgsp2EventMtp3TableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventMtp3Index"))
if mibBuilder.loadTexts: cgsp2EventMtp3TableEntry.setStatus('current')
cgsp2EventMtp3Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4, 1, 1), Cgsp2EventIndex())
if mibBuilder.loadTexts: cgsp2EventMtp3Index.setStatus('current')
cgsp2EventMtp3Text = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventMtp3Text.setStatus('current')
cgsp2EventMtp3Timestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventMtp3Timestamp.setStatus('current')
cgsp2EventPcTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5), )
if mibBuilder.loadTexts: cgsp2EventPcTable.setStatus('current')
cgsp2EventPcTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventPc"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventPcIndex"))
if mibBuilder.loadTexts: cgsp2EventPcTableEntry.setStatus('current')
cgsp2EventPc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1, 1), CItpTcPointCode())
if mibBuilder.loadTexts: cgsp2EventPc.setStatus('current')
cgsp2EventPcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1, 2), Cgsp2EventIndex())
if mibBuilder.loadTexts: cgsp2EventPcIndex.setStatus('current')
cgsp2EventPcText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventPcText.setStatus('current')
cgsp2EventPcTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2EventPcTimestamp.setStatus('current')
cgsp2QosTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1), )
if mibBuilder.loadTexts: cgsp2QosTable.setStatus('current')
cgsp2QosTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2QosClass"))
if mibBuilder.loadTexts: cgsp2QosTableEntry.setStatus('current')
cgsp2QosClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 1), Cgsp2TcQosClass())
if mibBuilder.loadTexts: cgsp2QosClass.setStatus('current')
cgsp2QosType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipPrecedence", 1), ("ipDscp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgsp2QosType.setStatus('current')
cgsp2QosPrecedenceValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgsp2QosPrecedenceValue.setStatus('current')
cgsp2QosIpDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgsp2QosIpDscp.setStatus('current')
cgsp2QosAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 5), CItpTcAclId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgsp2QosAclId.setStatus('current')
cgsp2QosRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgsp2QosRowStatus.setStatus('current')
cgsp2LocalPeerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1), )
if mibBuilder.loadTexts: cgsp2LocalPeerTable.setStatus('current')
cgsp2LocalPeerTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerPort"))
if mibBuilder.loadTexts: cgsp2LocalPeerTableEntry.setStatus('current')
cgsp2LocalPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1, 1), InetPortNumber())
if mibBuilder.loadTexts: cgsp2LocalPeerPort.setStatus('current')
cgsp2LocalPeerSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 32767)).clone(-1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2LocalPeerSlotNumber.setStatus('current')
cgsp2LocalPeerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgsp2LocalPeerRowStatus.setStatus('current')
cgsp2LocalPeerProcessorNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2LocalPeerProcessorNumber.setStatus('current')
cgsp2LpIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2), )
if mibBuilder.loadTexts: cgsp2LpIpAddrTable.setStatus('current')
cgsp2LpIpAddrTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerPort"), (0, "CISCO-ITP-GSP2-MIB", "cgsp2LpIpAddressNumber"))
if mibBuilder.loadTexts: cgsp2LpIpAddrTableEntry.setStatus('current')
cgsp2LpIpAddressNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cgsp2LpIpAddressNumber.setStatus('current')
cgsp2LpIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgsp2LpIpAddressType.setStatus('current')
cgsp2LpIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgsp2LpIpAddress.setStatus('current')
cgsp2LpIpAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgsp2LpIpAddressRowStatus.setStatus('current')
cgsp2Mtp3ErrorsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1), )
if mibBuilder.loadTexts: cgsp2Mtp3ErrorsTable.setStatus('current')
cgsp2Mtp3ErrorsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-ITP-GSP2-MIB", "cgsp2Mtp3ErrorsType"))
if mibBuilder.loadTexts: cgsp2Mtp3ErrorsTableEntry.setStatus('current')
cgsp2Mtp3ErrorsType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: cgsp2Mtp3ErrorsType.setStatus('current')
cgsp2Mtp3ErrorsDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2Mtp3ErrorsDescription.setStatus('current')
cgsp2Mtp3ErrorsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2Mtp3ErrorsCount.setStatus('current')
cgsp2ContextTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1), )
if mibBuilder.loadTexts: cgsp2ContextTable.setStatus('current')
cgsp2ContextEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1), ).setIndexNames((0, "CISCO-ITP-GSP2-MIB", "cgsp2ContextIdentifier"))
if mibBuilder.loadTexts: cgsp2ContextEntry.setStatus('current')
cgsp2ContextIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 1), CItpTcContextId())
if mibBuilder.loadTexts: cgsp2ContextIdentifier.setStatus('current')
cgsp2ContextType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 2), CItpTcContextType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2ContextType.setStatus('current')
cgsp2ContextLinksetName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 3), CItpTcLinksetId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2ContextLinksetName.setStatus('current')
cgsp2ContextSlc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 4), CItpTcLinkSLC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2ContextSlc.setStatus('current')
cgsp2ContextAsName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 5), CItpTcXuaName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2ContextAsName.setStatus('current')
cgsp2ContextAspName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 6), CItpTcXuaName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2ContextAspName.setStatus('current')
cgsp2ContextNetworkName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 7), CItpTcNetworkName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2ContextNetworkName.setStatus('current')
cgsp2OperMtp3Offload = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("main", 1), ("offload", 2))).clone('main')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2OperMtp3Offload.setStatus('current')
cgsp2OperRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("local", 2), ("distributed", 3))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgsp2OperRedundancy.setStatus('current')
ciscoGsp2MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1))
ciscoGsp2MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2))
ciscoGsp2MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 1)).setObjects(("CISCO-ITP-GSP2-MIB", "ciscoGsp2EventsGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2QosGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2LocalPeerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2MIBCompliance = ciscoGsp2MIBCompliance.setStatus('deprecated')
ciscoGsp2MIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 2)).setObjects(("CISCO-ITP-GSP2-MIB", "ciscoGsp2EventsGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2QosGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2LocalPeerGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2Mtp3ErrorsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2MIBComplianceRev1 = ciscoGsp2MIBComplianceRev1.setStatus('deprecated')
ciscoGsp2MIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 3)).setObjects(("CISCO-ITP-GSP2-MIB", "ciscoGsp2EventsGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2QosGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2LocalPeerGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2Mtp3ErrorsGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2OperationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2MIBComplianceRev2 = ciscoGsp2MIBComplianceRev2.setStatus('deprecated')
ciscoGsp2MIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 4)).setObjects(("CISCO-ITP-GSP2-MIB", "ciscoGsp2EventsGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2QosGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2Mtp3ErrorsGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2OperationGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2LocalPeerGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2MIBComplianceRev3 = ciscoGsp2MIBComplianceRev3.setStatus('deprecated')
ciscoGsp2MIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 5)).setObjects(("CISCO-ITP-GSP2-MIB", "ciscoGsp2EventsGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2QosGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2LocalPeerGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2Mtp3ErrorsGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2OperationGroup"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2LocalPeerGroupSup1"), ("CISCO-ITP-GSP2-MIB", "ciscoGsp2ContextGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2MIBComplianceRev4 = ciscoGsp2MIBComplianceRev4.setStatus('current')
ciscoGsp2EventsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 1)).setObjects(("CISCO-ITP-GSP2-MIB", "cgsp2EventLoggedEvents"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventDroppedEvents"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventMaxEntries"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventMaxEntriesAllowed"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventMtp3Text"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventMtp3Timestamp"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventAsText"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventAsTimestamp"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventAspText"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventAspTimestamp"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventPcText"), ("CISCO-ITP-GSP2-MIB", "cgsp2EventPcTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2EventsGroup = ciscoGsp2EventsGroup.setStatus('current')
ciscoGsp2QosGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 2)).setObjects(("CISCO-ITP-GSP2-MIB", "cgsp2QosType"), ("CISCO-ITP-GSP2-MIB", "cgsp2QosPrecedenceValue"), ("CISCO-ITP-GSP2-MIB", "cgsp2QosIpDscp"), ("CISCO-ITP-GSP2-MIB", "cgsp2QosAclId"), ("CISCO-ITP-GSP2-MIB", "cgsp2QosRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2QosGroup = ciscoGsp2QosGroup.setStatus('current')
ciscoGsp2LocalPeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 3)).setObjects(("CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerSlotNumber"), ("CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerRowStatus"), ("CISCO-ITP-GSP2-MIB", "cgsp2LpIpAddressType"), ("CISCO-ITP-GSP2-MIB", "cgsp2LpIpAddress"), ("CISCO-ITP-GSP2-MIB", "cgsp2LpIpAddressRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2LocalPeerGroup = ciscoGsp2LocalPeerGroup.setStatus('current')
ciscoGsp2Mtp3ErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 4)).setObjects(("CISCO-ITP-GSP2-MIB", "cgsp2Mtp3ErrorsDescription"), ("CISCO-ITP-GSP2-MIB", "cgsp2Mtp3ErrorsCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2Mtp3ErrorsGroup = ciscoGsp2Mtp3ErrorsGroup.setStatus('current')
ciscoGsp2OperationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 5)).setObjects(("CISCO-ITP-GSP2-MIB", "cgsp2OperMtp3Offload"), ("CISCO-ITP-GSP2-MIB", "cgsp2OperRedundancy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2OperationGroup = ciscoGsp2OperationGroup.setStatus('current')
ciscoGsp2LocalPeerGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 6)).setObjects(("CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerProcessorNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2LocalPeerGroupSup1 = ciscoGsp2LocalPeerGroupSup1.setStatus('current')
ciscoGsp2ContextGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 7)).setObjects(("CISCO-ITP-GSP2-MIB", "cgsp2ContextType"), ("CISCO-ITP-GSP2-MIB", "cgsp2ContextLinksetName"), ("CISCO-ITP-GSP2-MIB", "cgsp2ContextSlc"), ("CISCO-ITP-GSP2-MIB", "cgsp2ContextAsName"), ("CISCO-ITP-GSP2-MIB", "cgsp2ContextAspName"), ("CISCO-ITP-GSP2-MIB", "cgsp2ContextNetworkName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2ContextGroup = ciscoGsp2ContextGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GSP2-MIB", cgsp2QosIpDscp=cgsp2QosIpDscp, cgsp2Mtp3Errors=cgsp2Mtp3Errors, cgsp2EventType=cgsp2EventType, cgsp2ContextEntry=cgsp2ContextEntry, ciscoGsp2MIBComplianceRev1=ciscoGsp2MIBComplianceRev1, cgsp2EventAsTableEntry=cgsp2EventAsTableEntry, cgsp2EventAspTableEntry=cgsp2EventAspTableEntry, cgsp2QosType=cgsp2QosType, ciscoGsp2MIBCompliance=ciscoGsp2MIBCompliance, cgsp2EventAsTimestamp=cgsp2EventAsTimestamp, cgsp2LocalPeerTable=cgsp2LocalPeerTable, cgsp2Mtp3ErrorsCount=cgsp2Mtp3ErrorsCount, cgsp2QosAclId=cgsp2QosAclId, cgsp2ContextNetworkName=cgsp2ContextNetworkName, PYSNMP_MODULE_ID=ciscoGsp2MIB, cgsp2QosTable=cgsp2QosTable, cgsp2QosPrecedenceValue=cgsp2QosPrecedenceValue, cgsp2QosClass=cgsp2QosClass, cgsp2EventLoggedEvents=cgsp2EventLoggedEvents, cgsp2EventPcTableEntry=cgsp2EventPcTableEntry, cgsp2EventMtp3Table=cgsp2EventMtp3Table, cgsp2ContextSlc=cgsp2ContextSlc, cgsp2Operation=cgsp2Operation, cgsp2EventMaxEntriesAllowed=cgsp2EventMaxEntriesAllowed, cgsp2EventPcText=cgsp2EventPcText, cgsp2QosRowStatus=cgsp2QosRowStatus, cgsp2LocalPeerRowStatus=cgsp2LocalPeerRowStatus, ciscoGsp2MIBNotifs=ciscoGsp2MIBNotifs, cgsp2Mtp3ErrorsDescription=cgsp2Mtp3ErrorsDescription, cgsp2LpIpAddress=cgsp2LpIpAddress, cgsp2EventAspName=cgsp2EventAspName, cgsp2Mtp3ErrorsTable=cgsp2Mtp3ErrorsTable, cgsp2OperMtp3Offload=cgsp2OperMtp3Offload, cgsp2Mtp3ErrorsType=cgsp2Mtp3ErrorsType, ciscoGsp2QosGroup=ciscoGsp2QosGroup, cgsp2LpIpAddrTable=cgsp2LpIpAddrTable, cgsp2EventAsTable=cgsp2EventAsTable, cgsp2EventMtp3Text=cgsp2EventMtp3Text, ciscoGsp2MIBComplianceRev2=ciscoGsp2MIBComplianceRev2, cgsp2LocalPeerPort=cgsp2LocalPeerPort, cgsp2LocalPeerSlotNumber=cgsp2LocalPeerSlotNumber, ciscoGsp2MIBObjects=ciscoGsp2MIBObjects, cgsp2Context=cgsp2Context, cgsp2EventMaxEntries=cgsp2EventMaxEntries, ciscoGsp2LocalPeerGroup=ciscoGsp2LocalPeerGroup, cgsp2Qos=cgsp2Qos, ciscoGsp2EventsGroup=ciscoGsp2EventsGroup, ciscoGsp2MIBConform=ciscoGsp2MIBConform, cgsp2QosTableEntry=cgsp2QosTableEntry, cgsp2LpIpAddressNumber=cgsp2LpIpAddressNumber, cgsp2ContextLinksetName=cgsp2ContextLinksetName, cgsp2LpIpAddressType=cgsp2LpIpAddressType, cgsp2ContextIdentifier=cgsp2ContextIdentifier, cgsp2EventAspTimestamp=cgsp2EventAspTimestamp, cgsp2OperRedundancy=cgsp2OperRedundancy, cgsp2EventAsName=cgsp2EventAsName, ciscoGsp2ContextGroup=ciscoGsp2ContextGroup, ciscoGsp2MIBCompliances=ciscoGsp2MIBCompliances, cgsp2EventAspText=cgsp2EventAspText, ciscoGsp2LocalPeerGroupSup1=ciscoGsp2LocalPeerGroupSup1, cgsp2EventTableEntry=cgsp2EventTableEntry, cgsp2Mtp3ErrorsTableEntry=cgsp2Mtp3ErrorsTableEntry, CItpTcContextType=CItpTcContextType, cgsp2EventAspIndex=cgsp2EventAspIndex, cgsp2LpIpAddressRowStatus=cgsp2LpIpAddressRowStatus, cgsp2ContextType=cgsp2ContextType, cgsp2EventPcTimestamp=cgsp2EventPcTimestamp, cgsp2EventPc=cgsp2EventPc, Cgsp2EventIndex=Cgsp2EventIndex, cgsp2EventMtp3Timestamp=cgsp2EventMtp3Timestamp, cgsp2EventPcTable=cgsp2EventPcTable, cgsp2EventAsText=cgsp2EventAsText, ciscoGsp2MIBGroups=ciscoGsp2MIBGroups, cgsp2EventAspTable=cgsp2EventAspTable, cgsp2EventDroppedEvents=cgsp2EventDroppedEvents, ciscoGsp2MIBComplianceRev3=ciscoGsp2MIBComplianceRev3, cgsp2EventTable=cgsp2EventTable, cgsp2ContextAspName=cgsp2ContextAspName, CItpTcContextId=CItpTcContextId, cgsp2EventAsIndex=cgsp2EventAsIndex, cgsp2EventMtp3Index=cgsp2EventMtp3Index, ciscoGsp2OperationGroup=ciscoGsp2OperationGroup, cgsp2LpIpAddrTableEntry=cgsp2LpIpAddrTableEntry, cgsp2LocalPeerProcessorNumber=cgsp2LocalPeerProcessorNumber, ciscoGsp2MIB=ciscoGsp2MIB, cgsp2ContextAsName=cgsp2ContextAsName, ciscoGsp2Mtp3ErrorsGroup=ciscoGsp2Mtp3ErrorsGroup, cgsp2EventPcIndex=cgsp2EventPcIndex, cgsp2EventMtp3TableEntry=cgsp2EventMtp3TableEntry, cgsp2ContextTable=cgsp2ContextTable, Cgsp2TcQosClass=Cgsp2TcQosClass, cgsp2LocalPeerTableEntry=cgsp2LocalPeerTableEntry, cgsp2Events=cgsp2Events, ciscoGsp2MIBComplianceRev4=ciscoGsp2MIBComplianceRev4, cgsp2LocalPeer=cgsp2LocalPeer)

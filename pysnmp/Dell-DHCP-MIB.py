#
# PySNMP MIB module Dell-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-DHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:40:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
VlanList2, VlanList1, VlanList3, VlanList4 = mibBuilder.importSymbols("Dell-BRIDGEMIBOBJECTS-MIB", "VlanList2", "VlanList1", "VlanList3", "VlanList4")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, Gauge32, Integer32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Counter32, IpAddress, ObjectIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Gauge32", "Integer32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Counter32", "IpAddress", "ObjectIdentity", "MibIdentifier", "NotificationType")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
rsDHCP = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 38))
rsDHCP.setRevisions(('2003-10-18 00:00',))
if mibBuilder.loadTexts: rsDHCP.setLastUpdated('200310180000Z')
if mibBuilder.loadTexts: rsDHCP.setOrganization('Dell')
rsDhcpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDhcpMibVersion.setStatus('current')
rlDhcpRelayMaximalNumberOfNonIpVlans = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpRelayMaximalNumberOfNonIpVlans.setStatus('current')
rlDhcpRelayCurrentNumberOfNonIpVlans = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpRelayCurrentNumberOfNonIpVlans.setStatus('current')
rlDhcpRelayEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 25), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayEnable.setStatus('current')
rlDhcpRelayExists = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 26), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpRelayExists.setStatus('current')
rlDhcpRelayNextServerTable = MibTable((1, 3, 6, 1, 4, 1, 89, 38, 27), )
if mibBuilder.loadTexts: rlDhcpRelayNextServerTable.setStatus('current')
rlDhcpRelayNextServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 38, 27, 1), ).setIndexNames((0, "Dell-DHCP-MIB", "rlDhcpRelayNextServerIpAddr"))
if mibBuilder.loadTexts: rlDhcpRelayNextServerEntry.setStatus('current')
rlDhcpRelayNextServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 27, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpRelayNextServerIpAddr.setStatus('current')
rlDhcpRelayNextServerSecThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 27, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayNextServerSecThreshold.setStatus('current')
rlDhcpRelayNextServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 27, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayNextServerRowStatus.setStatus('current')
rlDhcpRelayInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 89, 38, 28), )
if mibBuilder.loadTexts: rlDhcpRelayInterfaceTable.setStatus('current')
rlDhcpRelayInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 38, 28, 1), ).setIndexNames((0, "Dell-DHCP-MIB", "rlDhcpRelayInterfaceIfindex"))
if mibBuilder.loadTexts: rlDhcpRelayInterfaceEntry.setStatus('current')
rlDhcpRelayInterfaceIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 28, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceIfindex.setStatus('current')
rlDhcpRelayInterfaceUseGiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 28, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceUseGiaddr.setStatus('current')
rlDhcpRelayInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 28, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceRowStatus.setStatus('current')
rlDhcpRelayInterfaceListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 38, 29), )
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListTable.setStatus('current')
rlDhcpRelayInterfaceListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 38, 29, 1), ).setIndexNames((0, "Dell-DHCP-MIB", "rlDhcpRelayInterfaceListIndex"))
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListEntry.setStatus('current')
rlDhcpRelayInterfaceListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 29, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListIndex.setStatus('current')
rlDhcpRelayInterfaceListPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 29, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListPortList.setStatus('current')
rlDhcpRelayInterfaceListVlanId1To1024 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 29, 1, 3), VlanList1()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListVlanId1To1024.setStatus('current')
rlDhcpRelayInterfaceListVlanId1025To2048 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 29, 1, 4), VlanList2()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListVlanId1025To2048.setStatus('current')
rlDhcpRelayInterfaceListVlanId2049To3072 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 29, 1, 5), VlanList3()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListVlanId2049To3072.setStatus('current')
rlDhcpRelayInterfaceListVlanId3073To4094 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 29, 1, 6), VlanList4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListVlanId3073To4094.setStatus('current')
rlDhcpSrvEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 30), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvEnable.setStatus('current')
rlDhcpSrvExists = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 31), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvExists.setStatus('current')
rlDhcpSrvDbLocation = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nvram", 1), ("flash", 2))).clone('flash')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDbLocation.setStatus('obsolete')
rlDhcpSrvMaxNumOfClients = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 33), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvMaxNumOfClients.setStatus('current')
rlDhcpSrvDbNumOfActiveEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 34), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDbNumOfActiveEntries.setStatus('current')
rlDhcpSrvDbErase = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 35), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDbErase.setStatus('obsolete')
rlDhcpSrvProbeEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 36), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvProbeEnable.setStatus('current')
rlDhcpSrvProbeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 37), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(300, 10000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvProbeTimeout.setStatus('current')
rlDhcpSrvProbeRetries = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 38), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvProbeRetries.setStatus('current')
rlDhcpSrvDefaultNetworkPoolName = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 39), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDefaultNetworkPoolName.setStatus('current')
rlDhcpSrvIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 89, 38, 45), )
if mibBuilder.loadTexts: rlDhcpSrvIpAddrTable.setStatus('current')
rlDhcpSrvIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 38, 45, 1), ).setIndexNames((0, "Dell-DHCP-MIB", "rlDhcpSrvIpAddrIpAddr"))
if mibBuilder.loadTexts: rlDhcpSrvIpAddrEntry.setStatus('current')
rlDhcpSrvIpAddrIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrIpAddr.setStatus('current')
rlDhcpSrvIpAddrIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrIpNetMask.setStatus('current')
rlDhcpSrvIpAddrIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrIdentifier.setStatus('current')
rlDhcpSrvIpAddrIdentifierType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("physAddr", 1), ("clientId", 2))).clone('clientId')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrIdentifierType.setStatus('current')
rlDhcpSrvIpAddrClnHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrClnHostName.setStatus('current')
rlDhcpSrvIpAddrMechanism = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("automatic", 2), ("dynamic", 3))).clone('manual')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrMechanism.setStatus('current')
rlDhcpSrvIpAddrAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrAgeTime.setStatus('current')
rlDhcpSrvIpAddrPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrPoolName.setStatus('current')
rlDhcpSrvIpAddrConfParamsName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrConfParamsName.setStatus('current')
rlDhcpSrvIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrRowStatus.setStatus('current')
rlDhcpSrvIpAddrLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 11), Unsigned32().clone(86400)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrLeaseTime.setStatus('current')
rlDhcpSrvIpAddrState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pre-allocated", 1), ("valid", 2), ("expired", 3), ("declined", 4))).clone('valid')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrState.setStatus('current')
rlDhcpSrvIpAddrOptionParamsName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrOptionParamsName.setStatus('current')
rlDhcpSrvDynamicTable = MibTable((1, 3, 6, 1, 4, 1, 89, 38, 46), )
if mibBuilder.loadTexts: rlDhcpSrvDynamicTable.setStatus('current')
rlDhcpSrvDynamicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 38, 46, 1), ).setIndexNames((0, "Dell-DHCP-MIB", "rlDhcpSrvDynamicPoolName"))
if mibBuilder.loadTexts: rlDhcpSrvDynamicEntry.setStatus('current')
rlDhcpSrvDynamicPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicPoolName.setStatus('current')
rlDhcpSrvDynamicIpAddrFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicIpAddrFrom.setStatus('current')
rlDhcpSrvDynamicIpAddrTo = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicIpAddrTo.setStatus('current')
rlDhcpSrvDynamicIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicIpNetMask.setStatus('current')
rlDhcpSrvDynamicLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 5), Unsigned32().clone(86400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicLeaseTime.setStatus('current')
rlDhcpSrvDynamicProbeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicProbeEnable.setStatus('current')
rlDhcpSrvDynamicTotalNumOfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDynamicTotalNumOfAddr.setStatus('current')
rlDhcpSrvDynamicFreeNumOfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDynamicFreeNumOfAddr.setStatus('current')
rlDhcpSrvDynamicConfParamsName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicConfParamsName.setStatus('current')
rlDhcpSrvDynamicRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicRowStatus.setStatus('current')
rlDhcpSrvDynamicAvailableNumOfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDynamicAvailableNumOfAddr.setStatus('current')
rlDhcpSrvDynamicNumOfPreallocatedAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDynamicNumOfPreallocatedAddr.setStatus('current')
rlDhcpSrvDynamicNumOfValidAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDynamicNumOfValidAddr.setStatus('current')
rlDhcpSrvDynamicNumOfExpiredAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDynamicNumOfExpiredAddr.setStatus('current')
rlDhcpSrvDynamicNumOfDeclinedAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDynamicNumOfDeclinedAddr.setStatus('current')
rlDhcpSrvDynamicOptionParamsName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicOptionParamsName.setStatus('current')
rlDhcpSrvConfParamsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 38, 47), )
if mibBuilder.loadTexts: rlDhcpSrvConfParamsTable.setStatus('current')
rlDhcpSrvConfParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 38, 47, 1), ).setIndexNames((0, "Dell-DHCP-MIB", "rlDhcpSrvConfParamsName"))
if mibBuilder.loadTexts: rlDhcpSrvConfParamsEntry.setStatus('current')
rlDhcpSrvConfParamsName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsName.setStatus('current')
rlDhcpSrvConfParamsNextServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNextServerIp.setStatus('current')
rlDhcpSrvConfParamsNextServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNextServerName.setStatus('current')
rlDhcpSrvConfParamsBootfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsBootfileName.setStatus('current')
rlDhcpSrvConfParamsRoutersList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsRoutersList.setStatus('current')
rlDhcpSrvConfParamsTimeSrvList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsTimeSrvList.setStatus('current')
rlDhcpSrvConfParamsDnsList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsDnsList.setStatus('current')
rlDhcpSrvConfParamsDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsDomainName.setStatus('current')
rlDhcpSrvConfParamsNetbiosNameList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNetbiosNameList.setStatus('current')
rlDhcpSrvConfParamsNetbiosNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8))).clone(namedValues=NamedValues(("b-node", 1), ("p-node", 2), ("m-node", 4), ("h-node", 8))).clone('h-node')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNetbiosNodeType.setStatus('current')
rlDhcpSrvConfParamsCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsCommunity.setStatus('obsolete')
rlDhcpSrvConfParamsNmsIp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNmsIp.setStatus('obsolete')
rlDhcpSrvConfParamsOptionsList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsOptionsList.setStatus('obsolete')
rlDhcpSrvConfParamsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 14), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsRowStatus.setStatus('current')
rlDhcpSrvNumOfNetworkPools = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 48), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvNumOfNetworkPools.setStatus('current')
rlDhcpSrvNumOfExcludedPools = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 49), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvNumOfExcludedPools.setStatus('current')
rlDhcpSrvNumOfHostPools = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 50), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvNumOfHostPools.setStatus('current')
rlDhcpSrvNumOfDynamicEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 51), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvNumOfDynamicEntries.setStatus('current')
rlDhcpSrvNumOfUsedEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 52), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvNumOfUsedEntries.setStatus('current')
rlDhcpSrvNumOfPreAllocatedEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 53), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvNumOfPreAllocatedEntries.setStatus('current')
rlDhcpSrvNumOfExpiredEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 54), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvNumOfExpiredEntries.setStatus('current')
rlDhcpSrvNumOfDeclinedEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 55), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvNumOfDeclinedEntries.setStatus('current')
rlDhcpSrvNumOfAutomaticEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 38, 56), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvNumOfAutomaticEntries.setStatus('current')
class RlDhcpSrvOptionTypeEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("boolean", 1), ("integer", 2), ("ascii", 3), ("ip", 4), ("hex", 5), ("ip-list", 6))

rlDhcpSrvOptionParamsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 38, 57), )
if mibBuilder.loadTexts: rlDhcpSrvOptionParamsTable.setStatus('current')
rlDhcpSrvOptionParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 38, 57, 1), ).setIndexNames((0, "Dell-DHCP-MIB", "rlDhcpSrvOptionParamsName"), (0, "Dell-DHCP-MIB", "rlDhcpSrvOptionParamsCode"))
if mibBuilder.loadTexts: rlDhcpSrvOptionParamsEntry.setStatus('current')
rlDhcpSrvOptionParamsName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 57, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvOptionParamsName.setStatus('current')
rlDhcpSrvOptionParamsCode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 57, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvOptionParamsCode.setStatus('current')
rlDhcpSrvOptionParamsType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 57, 1, 3), RlDhcpSrvOptionTypeEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvOptionParamsType.setStatus('current')
rlDhcpSrvOptionParamsOrigString = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 57, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvOptionParamsOrigString.setStatus('current')
rlDhcpSrvOptionParamsDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 57, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvOptionParamsDescription.setStatus('current')
rlDhcpSrvOptionParamsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 57, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvOptionParamsRowStatus.setStatus('current')
rlDhcpSrvAuxOptionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 38, 58), )
if mibBuilder.loadTexts: rlDhcpSrvAuxOptionTable.setStatus('current')
rlDhcpSrvAuxOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 38, 58, 1), ).setIndexNames((0, "Dell-DHCP-MIB", "rlDhcpSrvAuxOptionCode"), (0, "Dell-DHCP-MIB", "rlDhcpSrvAuxOptionType"))
if mibBuilder.loadTexts: rlDhcpSrvAuxOptionEntry.setStatus('current')
rlDhcpSrvAuxOptionCode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 58, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvAuxOptionCode.setStatus('current')
rlDhcpSrvAuxOptionType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 58, 1, 2), RlDhcpSrvOptionTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvAuxOptionType.setStatus('current')
rlDhcpSrvAuxOptionMinVal = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 58, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvAuxOptionMinVal.setStatus('current')
rlDhcpSrvAuxOptionMaxVal = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 38, 58, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvAuxOptionMaxVal.setStatus('current')
mibBuilder.exportSymbols("Dell-DHCP-MIB", rlDhcpSrvOptionParamsName=rlDhcpSrvOptionParamsName, rlDhcpSrvIpAddrConfParamsName=rlDhcpSrvIpAddrConfParamsName, rlDhcpRelayNextServerTable=rlDhcpRelayNextServerTable, rlDhcpRelayCurrentNumberOfNonIpVlans=rlDhcpRelayCurrentNumberOfNonIpVlans, rlDhcpRelayNextServerSecThreshold=rlDhcpRelayNextServerSecThreshold, rlDhcpSrvDynamicOptionParamsName=rlDhcpSrvDynamicOptionParamsName, rlDhcpSrvDynamicLeaseTime=rlDhcpSrvDynamicLeaseTime, rlDhcpSrvAuxOptionEntry=rlDhcpSrvAuxOptionEntry, rlDhcpSrvDynamicIpAddrTo=rlDhcpSrvDynamicIpAddrTo, rlDhcpSrvDynamicProbeEnable=rlDhcpSrvDynamicProbeEnable, rlDhcpSrvAuxOptionTable=rlDhcpSrvAuxOptionTable, rlDhcpSrvDynamicEntry=rlDhcpSrvDynamicEntry, rlDhcpSrvIpAddrAgeTime=rlDhcpSrvIpAddrAgeTime, rlDhcpRelayInterfaceEntry=rlDhcpRelayInterfaceEntry, rlDhcpSrvIpAddrPoolName=rlDhcpSrvIpAddrPoolName, rlDhcpSrvIpAddrMechanism=rlDhcpSrvIpAddrMechanism, rlDhcpSrvDynamicNumOfPreallocatedAddr=rlDhcpSrvDynamicNumOfPreallocatedAddr, rlDhcpSrvConfParamsNmsIp=rlDhcpSrvConfParamsNmsIp, rlDhcpSrvIpAddrOptionParamsName=rlDhcpSrvIpAddrOptionParamsName, rlDhcpSrvDynamicRowStatus=rlDhcpSrvDynamicRowStatus, rlDhcpRelayInterfaceListPortList=rlDhcpRelayInterfaceListPortList, rlDhcpSrvProbeEnable=rlDhcpSrvProbeEnable, rlDhcpSrvIpAddrIdentifierType=rlDhcpSrvIpAddrIdentifierType, rlDhcpSrvConfParamsCommunity=rlDhcpSrvConfParamsCommunity, rlDhcpSrvExists=rlDhcpSrvExists, rlDhcpSrvDynamicAvailableNumOfAddr=rlDhcpSrvDynamicAvailableNumOfAddr, RlDhcpSrvOptionTypeEnum=RlDhcpSrvOptionTypeEnum, rlDhcpRelayInterfaceRowStatus=rlDhcpRelayInterfaceRowStatus, rlDhcpSrvDynamicNumOfExpiredAddr=rlDhcpSrvDynamicNumOfExpiredAddr, rlDhcpSrvDynamicPoolName=rlDhcpSrvDynamicPoolName, rlDhcpSrvDynamicTotalNumOfAddr=rlDhcpSrvDynamicTotalNumOfAddr, rlDhcpSrvConfParamsRowStatus=rlDhcpSrvConfParamsRowStatus, rlDhcpSrvDbLocation=rlDhcpSrvDbLocation, rlDhcpSrvConfParamsNetbiosNameList=rlDhcpSrvConfParamsNetbiosNameList, rlDhcpSrvOptionParamsDescription=rlDhcpSrvOptionParamsDescription, rlDhcpSrvIpAddrClnHostName=rlDhcpSrvIpAddrClnHostName, rlDhcpSrvOptionParamsEntry=rlDhcpSrvOptionParamsEntry, rlDhcpSrvNumOfUsedEntries=rlDhcpSrvNumOfUsedEntries, rlDhcpSrvDynamicFreeNumOfAddr=rlDhcpSrvDynamicFreeNumOfAddr, rlDhcpSrvDynamicIpAddrFrom=rlDhcpSrvDynamicIpAddrFrom, rlDhcpSrvOptionParamsCode=rlDhcpSrvOptionParamsCode, rlDhcpRelayInterfaceListEntry=rlDhcpRelayInterfaceListEntry, rlDhcpSrvIpAddrTable=rlDhcpSrvIpAddrTable, rlDhcpRelayInterfaceListVlanId1025To2048=rlDhcpRelayInterfaceListVlanId1025To2048, rlDhcpSrvConfParamsTimeSrvList=rlDhcpSrvConfParamsTimeSrvList, rlDhcpSrvProbeTimeout=rlDhcpSrvProbeTimeout, rsDhcpMibVersion=rsDhcpMibVersion, rlDhcpSrvNumOfAutomaticEntries=rlDhcpSrvNumOfAutomaticEntries, rlDhcpSrvDynamicIpNetMask=rlDhcpSrvDynamicIpNetMask, rlDhcpRelayInterfaceListVlanId3073To4094=rlDhcpRelayInterfaceListVlanId3073To4094, rlDhcpSrvIpAddrEntry=rlDhcpSrvIpAddrEntry, rlDhcpSrvAuxOptionType=rlDhcpSrvAuxOptionType, rlDhcpSrvProbeRetries=rlDhcpSrvProbeRetries, rlDhcpSrvAuxOptionCode=rlDhcpSrvAuxOptionCode, rlDhcpSrvAuxOptionMaxVal=rlDhcpSrvAuxOptionMaxVal, rlDhcpRelayNextServerEntry=rlDhcpRelayNextServerEntry, rlDhcpSrvNumOfHostPools=rlDhcpSrvNumOfHostPools, rlDhcpRelayInterfaceListIndex=rlDhcpRelayInterfaceListIndex, rlDhcpSrvConfParamsNetbiosNodeType=rlDhcpSrvConfParamsNetbiosNodeType, rlDhcpSrvNumOfPreAllocatedEntries=rlDhcpSrvNumOfPreAllocatedEntries, rlDhcpSrvOptionParamsOrigString=rlDhcpSrvOptionParamsOrigString, rsDHCP=rsDHCP, rlDhcpSrvConfParamsName=rlDhcpSrvConfParamsName, rlDhcpSrvOptionParamsRowStatus=rlDhcpSrvOptionParamsRowStatus, rlDhcpSrvNumOfNetworkPools=rlDhcpSrvNumOfNetworkPools, rlDhcpSrvConfParamsEntry=rlDhcpSrvConfParamsEntry, rlDhcpRelayNextServerRowStatus=rlDhcpRelayNextServerRowStatus, rlDhcpSrvConfParamsTable=rlDhcpSrvConfParamsTable, rlDhcpSrvDynamicConfParamsName=rlDhcpSrvDynamicConfParamsName, rlDhcpSrvAuxOptionMinVal=rlDhcpSrvAuxOptionMinVal, rlDhcpSrvConfParamsDomainName=rlDhcpSrvConfParamsDomainName, rlDhcpRelayEnable=rlDhcpRelayEnable, rlDhcpSrvConfParamsBootfileName=rlDhcpSrvConfParamsBootfileName, rlDhcpRelayInterfaceListVlanId2049To3072=rlDhcpRelayInterfaceListVlanId2049To3072, rlDhcpSrvDefaultNetworkPoolName=rlDhcpSrvDefaultNetworkPoolName, rlDhcpSrvDbErase=rlDhcpSrvDbErase, rlDhcpSrvNumOfDynamicEntries=rlDhcpSrvNumOfDynamicEntries, rlDhcpSrvNumOfExpiredEntries=rlDhcpSrvNumOfExpiredEntries, PYSNMP_MODULE_ID=rsDHCP, rlDhcpSrvEnable=rlDhcpSrvEnable, rlDhcpSrvConfParamsRoutersList=rlDhcpSrvConfParamsRoutersList, rlDhcpSrvIpAddrIpAddr=rlDhcpSrvIpAddrIpAddr, rlDhcpRelayMaximalNumberOfNonIpVlans=rlDhcpRelayMaximalNumberOfNonIpVlans, rlDhcpRelayInterfaceListVlanId1To1024=rlDhcpRelayInterfaceListVlanId1To1024, rlDhcpSrvIpAddrIdentifier=rlDhcpSrvIpAddrIdentifier, rlDhcpSrvDynamicNumOfDeclinedAddr=rlDhcpSrvDynamicNumOfDeclinedAddr, rlDhcpSrvNumOfDeclinedEntries=rlDhcpSrvNumOfDeclinedEntries, rlDhcpRelayInterfaceListTable=rlDhcpRelayInterfaceListTable, rlDhcpSrvOptionParamsType=rlDhcpSrvOptionParamsType, rlDhcpSrvConfParamsOptionsList=rlDhcpSrvConfParamsOptionsList, rlDhcpSrvDynamicNumOfValidAddr=rlDhcpSrvDynamicNumOfValidAddr, rlDhcpSrvDbNumOfActiveEntries=rlDhcpSrvDbNumOfActiveEntries, rlDhcpRelayInterfaceTable=rlDhcpRelayInterfaceTable, rlDhcpSrvConfParamsNextServerName=rlDhcpSrvConfParamsNextServerName, rlDhcpSrvConfParamsDnsList=rlDhcpSrvConfParamsDnsList, rlDhcpSrvNumOfExcludedPools=rlDhcpSrvNumOfExcludedPools, rlDhcpSrvMaxNumOfClients=rlDhcpSrvMaxNumOfClients, rlDhcpSrvIpAddrLeaseTime=rlDhcpSrvIpAddrLeaseTime, rlDhcpRelayNextServerIpAddr=rlDhcpRelayNextServerIpAddr, rlDhcpRelayInterfaceIfindex=rlDhcpRelayInterfaceIfindex, rlDhcpSrvConfParamsNextServerIp=rlDhcpSrvConfParamsNextServerIp, rlDhcpSrvIpAddrIpNetMask=rlDhcpSrvIpAddrIpNetMask, rlDhcpRelayExists=rlDhcpRelayExists, rlDhcpSrvIpAddrState=rlDhcpSrvIpAddrState, rlDhcpRelayInterfaceUseGiaddr=rlDhcpRelayInterfaceUseGiaddr, rlDhcpSrvDynamicTable=rlDhcpSrvDynamicTable, rlDhcpSrvOptionParamsTable=rlDhcpSrvOptionParamsTable, rlDhcpSrvIpAddrRowStatus=rlDhcpSrvIpAddrRowStatus)

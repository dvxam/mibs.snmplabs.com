#
# PySNMP MIB module H3C-DHCPSNOOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-DHCPSNOOP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
hwdot1qVlanIndex, = mibBuilder.importSymbols("HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, Bits, Unsigned32, iso, MibIdentifier, ModuleIdentity, Counter32, Integer32, ObjectIdentity, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Bits", "Unsigned32", "iso", "MibIdentifier", "ModuleIdentity", "Counter32", "Integer32", "ObjectIdentity", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, RowStatus, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "DisplayString", "TruthValue")
h3cDhcpSnoop = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36))
if mibBuilder.loadTexts: h3cDhcpSnoop.setLastUpdated('200501140000Z')
if mibBuilder.loadTexts: h3cDhcpSnoop.setOrganization('Huawei-3com Technologies Co.,Ltd.')
h3cDhcpSnoopMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1))
h3cDhcpSnoopEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDhcpSnoopEnable.setStatus('current')
h3cDhcpSnoopTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2), )
if mibBuilder.loadTexts: h3cDhcpSnoopTable.setStatus('current')
h3cDhcpSnoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1), ).setIndexNames((0, "H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopClientIpAddressType"), (0, "H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopClientIpAddress"))
if mibBuilder.loadTexts: h3cDhcpSnoopEntry.setStatus('current')
h3cDhcpSnoopClientIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 1), InetAddressType().clone('ipv4'))
if mibBuilder.loadTexts: h3cDhcpSnoopClientIpAddressType.setStatus('current')
h3cDhcpSnoopClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: h3cDhcpSnoopClientIpAddress.setStatus('current')
h3cDhcpSnoopClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDhcpSnoopClientMacAddress.setStatus('current')
h3cDhcpSnoopClientProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDhcpSnoopClientProperty.setStatus('current')
h3cDhcpSnoopClientUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDhcpSnoopClientUnitNum.setStatus('current')
h3cDhcpSnoopTrustTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 3), )
if mibBuilder.loadTexts: h3cDhcpSnoopTrustTable.setStatus('current')
h3cDhcpSnoopTrustEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDhcpSnoopTrustEntry.setStatus('current')
h3cDhcpSnoopTrustStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("untrusted", 0), ("trusted", 1))).clone('untrusted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDhcpSnoopTrustStatus.setStatus('current')
h3cDhcpSnoopVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4), )
if mibBuilder.loadTexts: h3cDhcpSnoopVlanTable.setStatus('current')
h3cDhcpSnoopVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4, 1), ).setIndexNames((0, "H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopVlanIndex"))
if mibBuilder.loadTexts: h3cDhcpSnoopVlanEntry.setStatus('current')
h3cDhcpSnoopVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cDhcpSnoopVlanIndex.setStatus('current')
h3cDhcpSnoopVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDhcpSnoopVlanEnable.setStatus('current')
h3cDhcpSnoopTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2))
h3cDhcpSnoopTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 0))
h3cDhcpSnoopTrapsObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 1))
h3cDhcpSnoopSpoofServerMac = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDhcpSnoopSpoofServerMac.setStatus('current')
h3cDhcpSnoopSpoofServerIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 1, 2), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDhcpSnoopSpoofServerIP.setStatus('current')
h3cDhcpSnoopSpoofServerDetected = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), ("H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopSpoofServerMac"), ("H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopSpoofServerIP"))
if mibBuilder.loadTexts: h3cDhcpSnoopSpoofServerDetected.setStatus('current')
mibBuilder.exportSymbols("H3C-DHCPSNOOP-MIB", h3cDhcpSnoopTrapsPrefix=h3cDhcpSnoopTrapsPrefix, h3cDhcpSnoopClientIpAddressType=h3cDhcpSnoopClientIpAddressType, h3cDhcpSnoopTable=h3cDhcpSnoopTable, h3cDhcpSnoopVlanEntry=h3cDhcpSnoopVlanEntry, h3cDhcpSnoopTrapsObject=h3cDhcpSnoopTrapsObject, h3cDhcpSnoopSpoofServerMac=h3cDhcpSnoopSpoofServerMac, h3cDhcpSnoopMibObject=h3cDhcpSnoopMibObject, h3cDhcpSnoop=h3cDhcpSnoop, h3cDhcpSnoopVlanTable=h3cDhcpSnoopVlanTable, h3cDhcpSnoopTraps=h3cDhcpSnoopTraps, h3cDhcpSnoopSpoofServerIP=h3cDhcpSnoopSpoofServerIP, h3cDhcpSnoopVlanEnable=h3cDhcpSnoopVlanEnable, h3cDhcpSnoopTrustStatus=h3cDhcpSnoopTrustStatus, h3cDhcpSnoopEntry=h3cDhcpSnoopEntry, h3cDhcpSnoopClientMacAddress=h3cDhcpSnoopClientMacAddress, h3cDhcpSnoopSpoofServerDetected=h3cDhcpSnoopSpoofServerDetected, h3cDhcpSnoopClientProperty=h3cDhcpSnoopClientProperty, h3cDhcpSnoopClientIpAddress=h3cDhcpSnoopClientIpAddress, h3cDhcpSnoopTrustTable=h3cDhcpSnoopTrustTable, PYSNMP_MODULE_ID=h3cDhcpSnoop, h3cDhcpSnoopTrustEntry=h3cDhcpSnoopTrustEntry, h3cDhcpSnoopEnable=h3cDhcpSnoopEnable, h3cDhcpSnoopClientUnitNum=h3cDhcpSnoopClientUnitNum, h3cDhcpSnoopVlanIndex=h3cDhcpSnoopVlanIndex)
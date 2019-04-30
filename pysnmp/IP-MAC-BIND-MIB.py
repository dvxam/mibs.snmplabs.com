#
# PySNMP MIB module IP-MAC-BIND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IP-MAC-BIND-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, TimeTicks, Integer32, Counter64, ModuleIdentity, IpAddress, MibIdentifier, ObjectIdentity, Counter32, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, DateAndTime, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DateAndTime", "DisplayString", "RowStatus", "TextualConvention")
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

swIpMacBindMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 23))
if mibBuilder.loadTexts: swIpMacBindMIB.setLastUpdated('1004260000Z')
if mibBuilder.loadTexts: swIpMacBindMIB.setOrganization('D-Link Corp.')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swIpMacBindingCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 23, 1))
swIpMacBindingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 23, 2))
swIpMacBindingPortMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 23, 3))
swIpMacBindingMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 23, 4))
swIpMacBindingNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 23, 5))
swIpMacBindingTrapLogState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingTrapLogState.setStatus('current')
swIpMacBindingACLMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingACLMode.setStatus('current')
swIpMacBindingRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingRecoveryInterval.setStatus('current')
swIpMacBindingDHCPSnoopState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingDHCPSnoopState.setStatus('current')
swIpMacBindingDHCPSnoopEntryClearAllState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingDHCPSnoopEntryClearAllState.setStatus('current')
swIpMacBindingARPInspectionState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingARPInspectionState.setStatus('current')
swIpMacBindingIPv6DHCPSnoopState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingIPv6DHCPSnoopState.setStatus('current')
swIpMacBindingNDSnoopState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingNDSnoopState.setStatus('current')
swIpMacBindingIPv6DHCPSnoopEntryClearAllState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingIPv6DHCPSnoopEntryClearAllState.setStatus('current')
swIpMacBindingNDSnoopEntryClearAllState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingNDSnoopEntryClearAllState.setStatus('current')
swIpMacBindingAllPortState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("enable-strict", 2), ("disable", 3), ("enable-loose", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingAllPortState.setStatus('current')
swIpMacBindingPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2), )
if mibBuilder.loadTexts: swIpMacBindingPortTable.setStatus('current')
swIpMacBindingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1), ).setIndexNames((0, "IP-MAC-BIND-MIB", "swIpMacBindingPortIndex"))
if mibBuilder.loadTexts: swIpMacBindingPortEntry.setStatus('current')
swIpMacBindingPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingPortIndex.setStatus('current')
swIpMacBindingPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("enable-strict", 2), ("disable", 3), ("enable-loose", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortState.setStatus('current')
swIpMacBindingPortZeroIPState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortZeroIPState.setStatus('current')
swIpMacBindingPortForwardDhcpPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortForwardDhcpPkt.setStatus('current')
swIpMacBindingPortDHCPSnoopMaxEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortDHCPSnoopMaxEntry.setStatus('current')
swIpMacBindingPortDHCPSnoopEntryClearAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortDHCPSnoopEntryClearAction.setStatus('current')
swIpMacBindingPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("arp", 1), ("acl", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortMode.setStatus('current')
swIpMacBindingPortStopLearningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortStopLearningThreshold.setStatus('current')
swIpMacBindingPortRecoverLearning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortRecoverLearning.setStatus('current')
swIpMacBindingPortLearningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("stop", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingPortLearningStatus.setStatus('current')
swIpMacBindingPortIPv6State = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortIPv6State.setStatus('current')
swIpMacBindingPortIPv6DHCPSnoopMaxEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortIPv6DHCPSnoopMaxEntry.setStatus('current')
swIpMacBindingPortNDSnoopMaxEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortNDSnoopMaxEntry.setStatus('current')
swIpMacBindingPortIPv6DHCPSnoopEntryClearAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortIPv6DHCPSnoopEntryClearAction.setStatus('current')
swIpMacBindingPortNDSnoopEntryClearAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortNDSnoopEntryClearAction.setStatus('current')
swIpMacBindingPortARPInspection = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("strict", 2), ("loose", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortARPInspection.setStatus('current')
swIpMacBindingPortIPInspection = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortIPInspection.setStatus('current')
swIpMacBindingPortIPProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("ipv4", 2), ("ipv6", 3))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingPortIPProtocol.setStatus('current')
swIpMacBindingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1), )
if mibBuilder.loadTexts: swIpMacBindingTable.setStatus('current')
swIpMacBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1), ).setIndexNames((0, "IP-MAC-BIND-MIB", "swIpMacBindingIpIndex"))
if mibBuilder.loadTexts: swIpMacBindingEntry.setStatus('current')
swIpMacBindingIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingIpIndex.setStatus('current')
swIpMacBindingMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIpMacBindingMac.setStatus('current')
swIpMacBindingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIpMacBindingStatus.setStatus('current')
swIpMacBindingPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIpMacBindingPorts.setStatus('current')
swIpMacBindingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingAction.setStatus('current')
swIpMacBindingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("arp", 1), ("acl", 2), ("dhcp-snooping", 3), ("static", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIpMacBindingMode.setStatus('current')
swIpMacBindingAclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingAclStatus.setStatus('current')
swIpMacBindingBlockedTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2), )
if mibBuilder.loadTexts: swIpMacBindingBlockedTable.setStatus('current')
swIpMacBindingBlockedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1), ).setIndexNames((0, "IP-MAC-BIND-MIB", "swIpMacBindingBlockedVID"), (0, "IP-MAC-BIND-MIB", "swIpMacBindingBlockedMac"))
if mibBuilder.loadTexts: swIpMacBindingBlockedEntry.setStatus('current')
swIpMacBindingBlockedVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingBlockedVID.setStatus('current')
swIpMacBindingBlockedMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingBlockedMac.setStatus('current')
swIpMacBindingBlockedVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingBlockedVlanName.setStatus('current')
swIpMacBindingBlockedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingBlockedPort.setStatus('current')
swIpMacBindingBlockedType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("blockByAddrBind", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIpMacBindingBlockedType.setStatus('obsolete')
swIpMacBindingBlockedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingBlockedTime.setStatus('current')
swIpMacBindingBlockedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIpMacBindingBlockedStatus.setStatus('current')
swIpMacBindingDHCPSnoopTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3), )
if mibBuilder.loadTexts: swIpMacBindingDHCPSnoopTable.setStatus('current')
swIpMacBindingDHCPSnoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1), ).setIndexNames((0, "IP-MAC-BIND-MIB", "swIpMacBindingDHCPSnoopIpIndex"))
if mibBuilder.loadTexts: swIpMacBindingDHCPSnoopEntry.setStatus('current')
swIpMacBindingDHCPSnoopIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingDHCPSnoopIpIndex.setStatus('current')
swIpMacBindingDHCPSnoopMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingDHCPSnoopMac.setStatus('current')
swIpMacBindingDHCPSnoopLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingDHCPSnoopLeaseTime.setStatus('current')
swIpMacBindingDHCPSnoopPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingDHCPSnoopPort.setStatus('current')
swIpMacBindingDHCPSnoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingDHCPSnoopStatus.setStatus('current')
swIpMacBindingIPv6Table = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4), )
if mibBuilder.loadTexts: swIpMacBindingIPv6Table.setStatus('current')
swIpMacBindingIPv6Entry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1), ).setIndexNames((0, "IP-MAC-BIND-MIB", "swIpMacBindingIPv6Addr"))
if mibBuilder.loadTexts: swIpMacBindingIPv6Entry.setStatus('current')
swIpMacBindingIPv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 1), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingIPv6Addr.setStatus('current')
swIpMacBindingIPv6MacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIpMacBindingIPv6MacAddr.setStatus('current')
swIpMacBindingIPv6Portlist = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIpMacBindingIPv6Portlist.setStatus('current')
swIpMacBindingIPv6Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dhcp-snooping", 2), ("nd-snooping", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingIPv6Mode.setStatus('current')
swIpMacBindingIPv6ACLStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingIPv6ACLStatus.setStatus('current')
swIpMacBindingIPv6RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIpMacBindingIPv6RowStatus.setStatus('current')
swIpMacBindingIPv6DHCPSnoopTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5), )
if mibBuilder.loadTexts: swIpMacBindingIPv6DHCPSnoopTable.setStatus('current')
swIpMacBindingIPv6DHCPSnoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1), ).setIndexNames((0, "IP-MAC-BIND-MIB", "swIpMacBindingIPv6DHCPSnoopAddr"))
if mibBuilder.loadTexts: swIpMacBindingIPv6DHCPSnoopEntry.setStatus('current')
swIpMacBindingIPv6DHCPSnoopAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 1), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingIPv6DHCPSnoopAddr.setStatus('current')
swIpMacBindingIPv6DHCPSnoopMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingIPv6DHCPSnoopMac.setStatus('current')
swIpMacBindingIPv6DHCPSnoopLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingIPv6DHCPSnoopLeaseTime.setStatus('current')
swIpMacBindingIPv6DHCPSnoopPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingIPv6DHCPSnoopPort.setStatus('current')
swIpMacBindingIPv6DHCPSnoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingIPv6DHCPSnoopStatus.setStatus('current')
swIpMacBindingNDSnoopTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6), )
if mibBuilder.loadTexts: swIpMacBindingNDSnoopTable.setStatus('current')
swIpMacBindingNDSnoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1), ).setIndexNames((0, "IP-MAC-BIND-MIB", "swIpMacBindingNDSnoopAddr"))
if mibBuilder.loadTexts: swIpMacBindingNDSnoopEntry.setStatus('current')
swIpMacBindingNDSnoopAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 1), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingNDSnoopAddr.setStatus('current')
swIpMacBindingNDSnoopMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingNDSnoopMac.setStatus('current')
swIpMacBindingNDSnoopLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingNDSnoopLeaseTime.setStatus('current')
swIpMacBindingNDSnoopPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingNDSnoopPort.setStatus('current')
swIpMacBindingNDSnoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIpMacBindingNDSnoopStatus.setStatus('current')
swIpMacBindingNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0))
swIpMacBindingViolationTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0, 1)).setObjects(("IP-MAC-BIND-MIB", "swIpMacBindingPortIndex"), ("IP-MAC-BIND-MIB", "swIpMacBindingViolationIP"), ("IP-MAC-BIND-MIB", "swIpMacBindingViolationMac"))
if mibBuilder.loadTexts: swIpMacBindingViolationTrap.setStatus('current')
swIpMacBindingStopLearningTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0, 2)).setObjects(("IP-MAC-BIND-MIB", "swIpMacBindingPortIndex"))
if mibBuilder.loadTexts: swIpMacBindingStopLearningTrap.setStatus('current')
swIpMacBindingRecoverLearningTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0, 3)).setObjects(("IP-MAC-BIND-MIB", "swIpMacBindingPortIndex"))
if mibBuilder.loadTexts: swIpMacBindingRecoverLearningTrap.setStatus('current')
swIpMacBindingIPv6ViolationTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0, 4)).setObjects(("IP-MAC-BIND-MIB", "swIpMacBindingPortIndex"), ("IP-MAC-BIND-MIB", "swIpMacBindingViolationIPv6Addr"), ("IP-MAC-BIND-MIB", "swIpMacBindingViolationMac"))
if mibBuilder.loadTexts: swIpMacBindingIPv6ViolationTrap.setStatus('current')
swIpMacBindingNotificationBidings = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 2))
swIpMacBindingViolationIP = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 2, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swIpMacBindingViolationIP.setStatus('current')
swIpMacBindingViolationMac = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 2, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swIpMacBindingViolationMac.setStatus('current')
swIpMacBindingViolationIPv6Addr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 2, 3), Ipv6Address()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swIpMacBindingViolationIPv6Addr.setStatus('current')
mibBuilder.exportSymbols("IP-MAC-BIND-MIB", swIpMacBindingPortIPInspection=swIpMacBindingPortIPInspection, PYSNMP_MODULE_ID=swIpMacBindMIB, swIpMacBindingNDSnoopStatus=swIpMacBindingNDSnoopStatus, swIpMacBindingInfo=swIpMacBindingInfo, swIpMacBindingAllPortState=swIpMacBindingAllPortState, swIpMacBindingIPv6Mode=swIpMacBindingIPv6Mode, swIpMacBindingPortZeroIPState=swIpMacBindingPortZeroIPState, swIpMacBindingIPv6RowStatus=swIpMacBindingIPv6RowStatus, swIpMacBindingNDSnoopState=swIpMacBindingNDSnoopState, swIpMacBindingNotify=swIpMacBindingNotify, swIpMacBindingPortIPv6DHCPSnoopMaxEntry=swIpMacBindingPortIPv6DHCPSnoopMaxEntry, swIpMacBindingIpIndex=swIpMacBindingIpIndex, swIpMacBindingIPv6DHCPSnoopAddr=swIpMacBindingIPv6DHCPSnoopAddr, swIpMacBindingViolationTrap=swIpMacBindingViolationTrap, swIpMacBindingStatus=swIpMacBindingStatus, swIpMacBindingNDSnoopAddr=swIpMacBindingNDSnoopAddr, swIpMacBindingAclStatus=swIpMacBindingAclStatus, swIpMacBindingPorts=swIpMacBindingPorts, swIpMacBindingNDSnoopEntryClearAllState=swIpMacBindingNDSnoopEntryClearAllState, swIpMacBindingMac=swIpMacBindingMac, swIpMacBindingIPv6Portlist=swIpMacBindingIPv6Portlist, swIpMacBindingNDSnoopEntry=swIpMacBindingNDSnoopEntry, swIpMacBindingPortForwardDhcpPkt=swIpMacBindingPortForwardDhcpPkt, swIpMacBindingPortIndex=swIpMacBindingPortIndex, swIpMacBindingPortIPProtocol=swIpMacBindingPortIPProtocol, swIpMacBindingIPv6Addr=swIpMacBindingIPv6Addr, swIpMacBindingViolationIPv6Addr=swIpMacBindingViolationIPv6Addr, swIpMacBindingPortDHCPSnoopMaxEntry=swIpMacBindingPortDHCPSnoopMaxEntry, swIpMacBindingIPv6ViolationTrap=swIpMacBindingIPv6ViolationTrap, swIpMacBindingNDSnoopTable=swIpMacBindingNDSnoopTable, swIpMacBindingARPInspectionState=swIpMacBindingARPInspectionState, swIpMacBindingPortMgmt=swIpMacBindingPortMgmt, swIpMacBindingPortRecoverLearning=swIpMacBindingPortRecoverLearning, swIpMacBindingPortMode=swIpMacBindingPortMode, swIpMacBindingPortStopLearningThreshold=swIpMacBindingPortStopLearningThreshold, swIpMacBindingACLMode=swIpMacBindingACLMode, swIpMacBindingPortNDSnoopEntryClearAction=swIpMacBindingPortNDSnoopEntryClearAction, swIpMacBindingEntry=swIpMacBindingEntry, swIpMacBindingBlockedTable=swIpMacBindingBlockedTable, swIpMacBindingViolationIP=swIpMacBindingViolationIP, swIpMacBindingIPv6DHCPSnoopTable=swIpMacBindingIPv6DHCPSnoopTable, swIpMacBindingViolationMac=swIpMacBindingViolationMac, swIpMacBindingDHCPSnoopState=swIpMacBindingDHCPSnoopState, swIpMacBindingBlockedPort=swIpMacBindingBlockedPort, swIpMacBindingMgmt=swIpMacBindingMgmt, swIpMacBindingCtrl=swIpMacBindingCtrl, swIpMacBindingIPv6DHCPSnoopEntryClearAllState=swIpMacBindingIPv6DHCPSnoopEntryClearAllState, swIpMacBindingMode=swIpMacBindingMode, swIpMacBindingDHCPSnoopEntry=swIpMacBindingDHCPSnoopEntry, swIpMacBindingIPv6DHCPSnoopState=swIpMacBindingIPv6DHCPSnoopState, swIpMacBindingIPv6MacAddr=swIpMacBindingIPv6MacAddr, swIpMacBindingPortEntry=swIpMacBindingPortEntry, swIpMacBindingNDSnoopMac=swIpMacBindingNDSnoopMac, swIpMacBindingPortIPv6DHCPSnoopEntryClearAction=swIpMacBindingPortIPv6DHCPSnoopEntryClearAction, swIpMacBindingTrapLogState=swIpMacBindingTrapLogState, swIpMacBindingIPv6DHCPSnoopStatus=swIpMacBindingIPv6DHCPSnoopStatus, swIpMacBindingBlockedMac=swIpMacBindingBlockedMac, swIpMacBindingBlockedEntry=swIpMacBindingBlockedEntry, swIpMacBindingNDSnoopLeaseTime=swIpMacBindingNDSnoopLeaseTime, swIpMacBindingStopLearningTrap=swIpMacBindingStopLearningTrap, swIpMacBindingDHCPSnoopLeaseTime=swIpMacBindingDHCPSnoopLeaseTime, swIpMacBindingIPv6DHCPSnoopPort=swIpMacBindingIPv6DHCPSnoopPort, PortList=PortList, VlanId=VlanId, swIpMacBindingTable=swIpMacBindingTable, swIpMacBindingPortNDSnoopMaxEntry=swIpMacBindingPortNDSnoopMaxEntry, swIpMacBindingDHCPSnoopPort=swIpMacBindingDHCPSnoopPort, swIpMacBindMIB=swIpMacBindMIB, swIpMacBindingIPv6DHCPSnoopLeaseTime=swIpMacBindingIPv6DHCPSnoopLeaseTime, swIpMacBindingNotifyPrefix=swIpMacBindingNotifyPrefix, swIpMacBindingDHCPSnoopIpIndex=swIpMacBindingDHCPSnoopIpIndex, swIpMacBindingDHCPSnoopMac=swIpMacBindingDHCPSnoopMac, swIpMacBindingRecoverLearningTrap=swIpMacBindingRecoverLearningTrap, swIpMacBindingRecoveryInterval=swIpMacBindingRecoveryInterval, swIpMacBindingIPv6DHCPSnoopMac=swIpMacBindingIPv6DHCPSnoopMac, swIpMacBindingIPv6DHCPSnoopEntry=swIpMacBindingIPv6DHCPSnoopEntry, swIpMacBindingDHCPSnoopTable=swIpMacBindingDHCPSnoopTable, swIpMacBindingBlockedType=swIpMacBindingBlockedType, swIpMacBindingIPv6Entry=swIpMacBindingIPv6Entry, swIpMacBindingNotificationBidings=swIpMacBindingNotificationBidings, swIpMacBindingPortState=swIpMacBindingPortState, swIpMacBindingBlockedStatus=swIpMacBindingBlockedStatus, swIpMacBindingPortDHCPSnoopEntryClearAction=swIpMacBindingPortDHCPSnoopEntryClearAction, swIpMacBindingDHCPSnoopStatus=swIpMacBindingDHCPSnoopStatus, swIpMacBindingNDSnoopPort=swIpMacBindingNDSnoopPort, swIpMacBindingIPv6Table=swIpMacBindingIPv6Table, swIpMacBindingAction=swIpMacBindingAction, swIpMacBindingPortTable=swIpMacBindingPortTable, swIpMacBindingBlockedTime=swIpMacBindingBlockedTime, swIpMacBindingDHCPSnoopEntryClearAllState=swIpMacBindingDHCPSnoopEntryClearAllState, swIpMacBindingIPv6ACLStatus=swIpMacBindingIPv6ACLStatus, swIpMacBindingPortARPInspection=swIpMacBindingPortARPInspection, swIpMacBindingBlockedVlanName=swIpMacBindingBlockedVlanName, swIpMacBindingPortIPv6State=swIpMacBindingPortIPv6State, swIpMacBindingBlockedVID=swIpMacBindingBlockedVID, swIpMacBindingPortLearningStatus=swIpMacBindingPortLearningStatus)

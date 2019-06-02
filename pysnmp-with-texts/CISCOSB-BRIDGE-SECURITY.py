#
# PySNMP MIB module CISCOSB-BRIDGE-SECURITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-BRIDGE-SECURITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, ModuleIdentity, IpAddress, Integer32, NotificationType, MibIdentifier, Gauge32, Counter32, Counter64, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "ModuleIdentity", "IpAddress", "Integer32", "NotificationType", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
RowStatus, DisplayString, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "MacAddress", "TextualConvention", "TruthValue")
rlBridgeSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112))
if mibBuilder.loadTexts: rlBridgeSecurity.setLastUpdated('200604020000Z')
if mibBuilder.loadTexts: rlBridgeSecurity.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlBridgeSecurity.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlBridgeSecurity.setDescription('The private MIB module definition for DHCP Snoop, ARP Inspection and Ip source Guard features.')
rlIpDhcpSnoop = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1))
rlIpSourceGuard = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2))
rlIpArpInspect = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3))
rlProtocolFiltering = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 4))
rlIpDhcpSnoopMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpDhcpSnoopMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopMibVersion.setDescription("MIB's version, the current version is 1.")
rlIpDhcpSnoopEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopEnable.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopEnable.setDescription('Specifies a system DHCP Snoop enable state.')
rlIpDhcpSnoopFileEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopFileEnable.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopFileEnable.setDescription('Specifies a system DHCP Snoop file enable state.')
rlIpDhcpSnoopClearAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("clearNow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopClearAction.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopClearAction.setDescription('Used to clear DHCP Snoop Table.')
rlIpDhcpSnoopFileUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(600, 86400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopFileUpdateTime.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopFileUpdateTime.setDescription('Configures in seconds the period of time between file updates. The valid range is 600 - 86400.')
rlIpDhcpSnoopVerifyMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopVerifyMacAddress.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopVerifyMacAddress.setDescription('Configures on an un-trusted port whether the source MAC address in a DHCP packet matches the client hardware address.')
rlIpDhcpSnoopCurrentEntiresNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpDhcpSnoopCurrentEntiresNumber.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopCurrentEntiresNumber.setDescription('Contain the current number of DHCP snooping entries for all types.')
rlIpDhcpOpt82InsertionEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpOpt82InsertionEnable.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpOpt82InsertionEnable.setDescription('Specifies a DHCP option 82 insertion enable state.')
rlIpDhcpOpt82RxOnUntrustedEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpOpt82RxOnUntrustedEnable.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpOpt82RxOnUntrustedEnable.setDescription('Specifies a DHCP option 82 receive on untrusted port enable state.')
rlIpDhcpSnoopStaticTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 10), )
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticTable.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticTable.setDescription('The table specifies all DHCP Snoop Static (configured by user) entries. The entry contains a local IP address of the DHCP client, a Port interface to which a DHCP client is connected to the switch.')
rlIpDhcpSnoopStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 10, 1), ).setIndexNames((0, "CISCOSB-BRIDGE-SECURITY", "rlIpDhcpSnoopStaticVLANTag"), (0, "CISCOSB-BRIDGE-SECURITY", "rlIpDhcpSnoopStaticMACAddress"))
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticEntry.setDescription('The row definition for this table.')
rlIpDhcpSnoopStaticVLANTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 10, 1, 1), VlanId())
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticVLANTag.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticVLANTag.setDescription('A DHCP Snoop Static entry vlan tag.')
rlIpDhcpSnoopStaticMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 10, 1, 2), MacAddress())
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticMACAddress.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticMACAddress.setDescription('A DHCP Snoop Static entry mac address')
rlIpDhcpSnoopStaticIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 10, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticIPAddress.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticIPAddress.setDescription('A DHCP Snoop Static entry IP address.')
rlIpDhcpSnoopStaticPortInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 10, 1, 4), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticPortInterface.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticPortInterface.setDescription('A DHCP Snoop Static entry Port interface.')
rlIpDhcpSnoopStaticRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 10, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopStaticRowStatus.setDescription('A status can be destroy, active or createAndGo')
class RlIpDhcpSnoopType(TextualConvention, Integer32):
    description = 'Ip Dhcp Snoop entry type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("learnedByProtocol", 1), ("deletedByTimeout", 2), ("static", 3))

rlIpDhcpSnoopTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 11), )
if mibBuilder.loadTexts: rlIpDhcpSnoopTable.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopTable.setDescription('DHCP Snoop entry. Use to add/delete a dynamic entries and to view all entries (dynamic and static)')
rlIpDhcpSnoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 11, 1), ).setIndexNames((0, "CISCOSB-BRIDGE-SECURITY", "rlIpDhcpSnoopVLANTag"), (0, "CISCOSB-BRIDGE-SECURITY", "rlIpDhcpSnoopMACAddress"))
if mibBuilder.loadTexts: rlIpDhcpSnoopEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopEntry.setDescription('The row definition for this table.')
rlIpDhcpSnoopVLANTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 11, 1, 1), VlanId())
if mibBuilder.loadTexts: rlIpDhcpSnoopVLANTag.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopVLANTag.setDescription('A DHCP Snoop entry vlan tag.')
rlIpDhcpSnoopMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 11, 1, 2), MacAddress())
if mibBuilder.loadTexts: rlIpDhcpSnoopMACAddress.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopMACAddress.setDescription('A DHCP Snoop entry mac address')
rlIpDhcpSnoopType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 11, 1, 3), RlIpDhcpSnoopType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopType.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopType.setDescription('A DHCP Snoop entry type: static or dynamic.')
rlIpDhcpSnoopLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 11, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopLeaseTime.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopLeaseTime.setDescription('A DHCP Snoop lease time. For static entry the lease time is 0xFFFFFFFF')
rlIpDhcpSnoopIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 11, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopIPAddress.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopIPAddress.setDescription('The IP address of the DHCP client referred to in this table entry.')
rlIpDhcpSnoopPortInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 11, 1, 6), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopPortInterface.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopPortInterface.setDescription('Identifies the port Interface ifindex, which connected to DHCP client identified with the entry.')
rlIpDhcpSnoopRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 11, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopRowStatus.setDescription('Entry status. A valid status is CreateandGo or Delete.')
rlIpDhcpSnoopEnableVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 12), )
if mibBuilder.loadTexts: rlIpDhcpSnoopEnableVlanTable.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopEnableVlanTable.setDescription('An Ip Dhcp Snooping enabled VLAN table.')
rlIpDhcpSnoopEnableVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 12, 1), ).setIndexNames((0, "CISCOSB-BRIDGE-SECURITY", "rlIpDhcpSnoopEnableVlanTag"))
if mibBuilder.loadTexts: rlIpDhcpSnoopEnableVlanEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopEnableVlanEntry.setDescription('An Ip Dhcp Snooping enabled VLAN entry.')
rlIpDhcpSnoopEnableVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 12, 1, 1), VlanId())
if mibBuilder.loadTexts: rlIpDhcpSnoopEnableVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopEnableVlanTag.setDescription('A DHCP Snoop entry vlan tag.')
rlIpDhcpSnoopEnableVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 12, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopEnableVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopEnableVlanRowStatus.setDescription('Entry status. A valid status is CreateandGo and Delete.')
rlIpDhcpSnoopTrustedPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 13), )
if mibBuilder.loadTexts: rlIpDhcpSnoopTrustedPortTable.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopTrustedPortTable.setDescription('DHCP Snoop Trusted ports entry. The entry created when port is configured as trusted.')
rlIpDhcpSnoopTrustedPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 13, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlIpDhcpSnoopTrustedPortEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopTrustedPortEntry.setDescription('The row definition for this table.')
rlIpDhcpSnoopTrustedPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 1, 13, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpDhcpSnoopTrustedPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpDhcpSnoopTrustedPortRowStatus.setDescription('Entry status. A valid status is CreateandGo or Delete.')
rlIpSourceGuardMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpSourceGuardMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardMibVersion.setDescription("MIB's version, the current version is 1.")
rlIpSourceGuardEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpSourceGuardEnable.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardEnable.setDescription('FALSE - There is no Ip Source Guard in the system. TRUE - Ip Source Guard is enabled on system.')
rlIpSourceGuardRetryToInsert = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noAction", 0), ("retryToInsertNow", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpSourceGuardRetryToInsert.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardRetryToInsert.setDescription('When setted to retryToInsertNow all IP Source Guard inactive entries due to resource problem reinserted in the Policy. On get always return noAction.')
rlIpSourceGuardRetryTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpSourceGuardRetryTime.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardRetryTime.setDescription('Configures in seconds the period of time the application retries to insert inactive by resource problem rules. The actual range is 10-600. 0 used to sign that the timer is not active.')
rlIpSourceGuardPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 5), )
if mibBuilder.loadTexts: rlIpSourceGuardPortTable.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardPortTable.setDescription('IP Source Guard ports entry. The entry created when IP Source Guard enabled on port.')
rlIpSourceGuardPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlIpSourceGuardPortEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardPortEntry.setDescription('The row definition for this table.')
rlIpSourceGuardPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 5, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpSourceGuardPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardPortRowStatus.setDescription('Entry status. A valid status is CreateAndGo or Delete.')
class RlIpSourceGuardType(TextualConvention, Integer32):
    description = 'Ip IP Source Guard entry type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("dynamic", 1), ("static", 2))

class RlIpSourceGuardStatus(TextualConvention, Integer32):
    description = 'Ip IP Source Guard entry status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

class RlIpSourceGuardFailReason(TextualConvention, Integer32):
    description = 'Ip IP Source Guard entry reason.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noProblem", 1), ("noResource", 2), ("noSnoopVlan", 3), ("trustPort", 4))

rlIpSourceGuardTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 6), )
if mibBuilder.loadTexts: rlIpSourceGuardTable.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardTable.setDescription('IP Source Guard entry. Use to view all entries (dynamic and static)')
rlIpSourceGuardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCOSB-BRIDGE-SECURITY", "rlIpSourceGuardIPAddress"), (0, "CISCOSB-BRIDGE-SECURITY", "rlIpSourceGuardVLANTag"))
if mibBuilder.loadTexts: rlIpSourceGuardEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardEntry.setDescription('The row definition for this table.')
rlIpSourceGuardIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: rlIpSourceGuardIPAddress.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardIPAddress.setDescription('The IP address of the Ip Source Guard entry.')
rlIpSourceGuardVLANTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 6, 1, 2), VlanId())
if mibBuilder.loadTexts: rlIpSourceGuardVLANTag.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardVLANTag.setDescription('A Ip Source Guard entry vlan tag.')
rlIpSourceGuardMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 6, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpSourceGuardMACAddress.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardMACAddress.setDescription('A Ip Source Guard entry mac address')
rlIpSourceGuardType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 6, 1, 4), RlIpSourceGuardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpSourceGuardType.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardType.setDescription('A Ip Source Guard entry type: static or dynamic.')
rlIpSourceGuardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 6, 1, 5), RlIpSourceGuardStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpSourceGuardStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardStatus.setDescription('Identifies the status of Ip Source Guard entry.')
rlIpSourceGuardFailReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 6, 1, 6), RlIpSourceGuardFailReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpSourceGuardFailReason.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardFailReason.setDescription('Identifies the reason for in-activity of Ip Source Guard entry.')
rlIpSourceGuardPermittedRuleCounterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 7), )
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterTable.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterTable.setDescription('The table includes, per vlan, the IP Source Guard permitted rules counters.')
rlIpSourceGuardPermittedRuleCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 7, 1), ).setIndexNames((0, "CISCOSB-BRIDGE-SECURITY", "rlIpSourceGuardPermittedRuleCounterVLANTag"))
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterEntry.setDescription('The row definition for this table.')
rlIpSourceGuardPermittedRuleCounterVLANTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 7, 1, 1), VlanId())
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterVLANTag.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterVLANTag.setDescription('Ip Source Guard permitted rules counters entry Vlan tag.')
rlIpSourceGuardPermittedRuleCounterNumOfStaticRules = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterNumOfStaticRules.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterNumOfStaticRules.setDescription('Number of static rules added by IP Source Guard for the permitted Hosts')
rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules.setStatus('current')
if mibBuilder.loadTexts: rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules.setDescription('Number of rules added by IP Source Guard for the permitted Hosts, as a result of DHCP Snooping dynamic information.')
class RlIpArpInspectListNameType(DisplayString):
    description = 'Ip arp inspection list name type.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

rlIpArpInspectMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpArpInspectMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectMibVersion.setDescription("MIB's version, the current version is 1.")
rlIpArpInspectEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectEnable.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectEnable.setDescription('Specifies a system ARP Inspection enable state.')
rlIpArpInspectLogInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectLogInterval.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectLogInterval.setDescription('Specify the minimal interval between successive ARP SYSLOG messages. 0 - message is immediately generated. 0xFFFFFFFF - messages would not be generated. A legal range is 0-86400.')
rlIpArpInspectValidation = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectValidation.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectValidation.setDescription('Defined a specific check on incoming ARP packets: Source MAC: Compare the source MAC address in the Ethernet header against the sender MAC address in the ARP body. This check is performed on both ARP requests and responses. Destination MAC: Compare the destination MAC address in the Ethernet header against the target MAC address in ARP body. This check is performed for ARP responses. IP addresses: Compare the ARP body for invalid and unexpected IP addresses. Addresses include 0.0.0.0, 255.255.255.255, and all IP multicast addresses.')
rlIpArpInspectListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 5), )
if mibBuilder.loadTexts: rlIpArpInspectListTable.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectListTable.setDescription('The table specifies all ARP Inspection List entries. The entry contains a list name, list IP address, a list Mac address.')
rlIpArpInspectListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 5, 1), ).setIndexNames((0, "CISCOSB-BRIDGE-SECURITY", "rlIpArpInspectListName"), (0, "CISCOSB-BRIDGE-SECURITY", "rlIpArpInspectListIPAddress"))
if mibBuilder.loadTexts: rlIpArpInspectListEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectListEntry.setDescription('The row definition for this table.')
rlIpArpInspectListName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 5, 1, 1), RlIpArpInspectListNameType())
if mibBuilder.loadTexts: rlIpArpInspectListName.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectListName.setDescription('The Name of the Access List.')
rlIpArpInspectListIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: rlIpArpInspectListIPAddress.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectListIPAddress.setDescription('ARP Inspection List IP address.')
rlIpArpInspectListMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 5, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectListMACAddress.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectListMACAddress.setDescription('ARP Inspection List mac address')
rlIpArpInspectListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 5, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectListRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectListRowStatus.setDescription('A status can be destroy, active or createAndGo')
rlIpArpInspectEnableVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 6), )
if mibBuilder.loadTexts: rlIpArpInspectEnableVlanTable.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectEnableVlanTable.setDescription('An Ip ARP Inspection enabled VLAN table.')
rlIpArpInspectEnableVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 6, 1), ).setIndexNames((0, "CISCOSB-BRIDGE-SECURITY", "rlIpArpInspectEnableVlanTag"))
if mibBuilder.loadTexts: rlIpArpInspectEnableVlanEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectEnableVlanEntry.setDescription('An Ip ARP Inspection enabled VLAN entry.')
rlIpArpInspectEnableVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 6, 1, 1), VlanId())
if mibBuilder.loadTexts: rlIpArpInspectEnableVlanTag.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectEnableVlanTag.setDescription('An Ip ARP Inspection entry vlan tag.')
rlIpArpInspectAssignedListName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 6, 1, 2), RlIpArpInspectListNameType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectAssignedListName.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectAssignedListName.setDescription('An Ip ARP Inspection assigned ACL name.')
rlIpArpInspectEnableVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 6, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectEnableVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectEnableVlanRowStatus.setDescription('Entry status. A valid status is CreateandGo and Delete.')
rlIpArpInspectVlanNumOfArpForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpArpInspectVlanNumOfArpForwarded.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectVlanNumOfArpForwarded.setDescription('Total number of forwarded ARP packets, packets which were validated by ARP inspection ')
rlIpArpInspectVlanNumOfArpDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpArpInspectVlanNumOfArpDropped.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectVlanNumOfArpDropped.setDescription('Number of dropped ARP packets, which were validated by ARP inspection (mismatch , not-found and dropped for any reason)')
rlIpArpInspectVlanNumOfArpMismatched = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpArpInspectVlanNumOfArpMismatched.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectVlanNumOfArpMismatched.setDescription('Number of dropped ARP packets, which were validated by ARP inspection and inconsistency was found for IP and MAC (mismatch)')
rlIpArpInspectVlanClearCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 6, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectVlanClearCountersAction.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectVlanClearCountersAction.setDescription('If true, clear (set to zero) all Arp Inspection counters: rlIpArpInspectVlanNumOfArpForwarded , rlIpArpInspectVlanNumOfArpDropped and rlIpArpInspectVlanNumOfArpMismatched')
rlIpArpInspectTrustedPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 7), )
if mibBuilder.loadTexts: rlIpArpInspectTrustedPortTable.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectTrustedPortTable.setDescription('ARP Inspection Trusted ports entry. The entry created when port is configured as trusted.')
rlIpArpInspectTrustedPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlIpArpInspectTrustedPortEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectTrustedPortEntry.setDescription('The row definition for this table.')
rlIpArpInspectTrustedPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 7, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectTrustedPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectTrustedPortRowStatus.setDescription('Entry status. A valid status is CreateandGo or Delete.')
rlIpArpInspectClearCountersAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 3, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpArpInspectClearCountersAction.setStatus('current')
if mibBuilder.loadTexts: rlIpArpInspectClearCountersAction.setDescription('If true, clear (set to zero) on all vlans: all Arp Inspection counters: rlIpArpInspectVlanNumOfArpForwarded , rlIpArpInspectVlanNumOfArpDropped and rlIpArpInspectVlanNumOfArpMismatched')
class ProtocolFilteringMap(TextualConvention, Bits):
    description = "This TC describes the list of protocol to be filtered. The bit 'all(0)' indicates all Cisco protocols in range 0100.0ccc.ccc0 - 0100.0ccc.cccf The bit 'cdp(1)' indicates Cisco CDP protocol. Identified by destination mac address: 0100.0ccc.cccc and protocol type:0x2000. The bit 'vtp(2)' indicates Cisco VTP protocol. Identified by destination mac address: 0100.0ccc.cccc and protocol type:0x2003. The bit 'dtp(3)' indicates Cisco DTP protocol. Identified by destination mac address: 0100.0ccc.cccc and protocol type:0x2004. The bit 'udld (4)' indicates Cisco UDLD protocol. Identified by destination mac address: 0100.0ccc.cccc and protocol type:0x0111. The bit 'pagp(5)' indicates Cisco PAGP protocol. Identified by destination mac address: 0100.0ccc.cccc and protocol type: 0x0104. The bit 'sstp(6)' indicates Cisco SSTP protocol. Identified by destination mac address: 0100.0ccc.cccd. "
    status = 'current'
    namedValues = NamedValues(("all", 0), ("cdp", 1), ("vtp", 2), ("dtp", 3), ("udld", 4), ("pagp", 5), ("sstp", 6))

rlProtocolFilteringTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 4, 1), )
if mibBuilder.loadTexts: rlProtocolFilteringTable.setStatus('current')
if mibBuilder.loadTexts: rlProtocolFilteringTable.setDescription('Protocol filter configuration entry')
rlProtocolFilteringEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlProtocolFilteringEntry.setStatus('current')
if mibBuilder.loadTexts: rlProtocolFilteringEntry.setDescription('The row definition for this table.')
rlProtocolFilteringList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 4, 1, 1, 1), ProtocolFilteringMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlProtocolFilteringList.setStatus('current')
if mibBuilder.loadTexts: rlProtocolFilteringList.setDescription('The list of protocol to be filtered.')
rlProtocolFilteringRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112, 4, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlProtocolFilteringRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlProtocolFilteringRowStatus.setDescription('A status can be destroy, active or createAndGo')
mibBuilder.exportSymbols("CISCOSB-BRIDGE-SECURITY", rlIpDhcpSnoopFileUpdateTime=rlIpDhcpSnoopFileUpdateTime, rlIpArpInspectVlanNumOfArpForwarded=rlIpArpInspectVlanNumOfArpForwarded, rlIpDhcpSnoop=rlIpDhcpSnoop, rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules=rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules, rlIpDhcpOpt82RxOnUntrustedEnable=rlIpDhcpOpt82RxOnUntrustedEnable, rlIpSourceGuardType=rlIpSourceGuardType, rlIpDhcpSnoopRowStatus=rlIpDhcpSnoopRowStatus, RlIpSourceGuardType=RlIpSourceGuardType, rlIpArpInspectAssignedListName=rlIpArpInspectAssignedListName, rlIpSourceGuardPortRowStatus=rlIpSourceGuardPortRowStatus, rlBridgeSecurity=rlBridgeSecurity, rlIpSourceGuardPortEntry=rlIpSourceGuardPortEntry, rlProtocolFilteringEntry=rlProtocolFilteringEntry, rlIpArpInspectTrustedPortEntry=rlIpArpInspectTrustedPortEntry, RlIpSourceGuardStatus=RlIpSourceGuardStatus, rlIpArpInspectTrustedPortRowStatus=rlIpArpInspectTrustedPortRowStatus, rlIpArpInspectListRowStatus=rlIpArpInspectListRowStatus, rlIpSourceGuardEntry=rlIpSourceGuardEntry, rlIpSourceGuardPermittedRuleCounterVLANTag=rlIpSourceGuardPermittedRuleCounterVLANTag, rlIpArpInspectTrustedPortTable=rlIpArpInspectTrustedPortTable, rlIpArpInspectEnableVlanEntry=rlIpArpInspectEnableVlanEntry, rlIpSourceGuardRetryTime=rlIpSourceGuardRetryTime, rlIpArpInspectListIPAddress=rlIpArpInspectListIPAddress, rlIpArpInspectValidation=rlIpArpInspectValidation, rlIpDhcpSnoopTrustedPortTable=rlIpDhcpSnoopTrustedPortTable, rlIpSourceGuardEnable=rlIpSourceGuardEnable, rlIpDhcpSnoopEnableVlanTag=rlIpDhcpSnoopEnableVlanTag, rlIpDhcpSnoopStaticVLANTag=rlIpDhcpSnoopStaticVLANTag, rlIpDhcpSnoopStaticMACAddress=rlIpDhcpSnoopStaticMACAddress, rlIpSourceGuardMibVersion=rlIpSourceGuardMibVersion, rlIpDhcpSnoopMibVersion=rlIpDhcpSnoopMibVersion, rlIpDhcpOpt82InsertionEnable=rlIpDhcpOpt82InsertionEnable, rlIpArpInspectListName=rlIpArpInspectListName, rlIpDhcpSnoopPortInterface=rlIpDhcpSnoopPortInterface, rlIpSourceGuardRetryToInsert=rlIpSourceGuardRetryToInsert, rlIpDhcpSnoopType=rlIpDhcpSnoopType, rlIpArpInspectVlanNumOfArpMismatched=rlIpArpInspectVlanNumOfArpMismatched, rlIpArpInspectVlanNumOfArpDropped=rlIpArpInspectVlanNumOfArpDropped, rlIpSourceGuardPortTable=rlIpSourceGuardPortTable, rlIpSourceGuardVLANTag=rlIpSourceGuardVLANTag, RlIpArpInspectListNameType=RlIpArpInspectListNameType, rlIpDhcpSnoopIPAddress=rlIpDhcpSnoopIPAddress, rlIpArpInspectEnable=rlIpArpInspectEnable, rlIpDhcpSnoopStaticIPAddress=rlIpDhcpSnoopStaticIPAddress, rlIpDhcpSnoopVLANTag=rlIpDhcpSnoopVLANTag, rlIpDhcpSnoopFileEnable=rlIpDhcpSnoopFileEnable, rlIpSourceGuardIPAddress=rlIpSourceGuardIPAddress, rlIpArpInspectVlanClearCountersAction=rlIpArpInspectVlanClearCountersAction, rlIpDhcpSnoopEnableVlanRowStatus=rlIpDhcpSnoopEnableVlanRowStatus, rlProtocolFiltering=rlProtocolFiltering, rlIpDhcpSnoopEnableVlanTable=rlIpDhcpSnoopEnableVlanTable, rlIpArpInspectListMACAddress=rlIpArpInspectListMACAddress, rlIpDhcpSnoopVerifyMacAddress=rlIpDhcpSnoopVerifyMacAddress, rlIpDhcpSnoopTrustedPortRowStatus=rlIpDhcpSnoopTrustedPortRowStatus, rlIpSourceGuardFailReason=rlIpSourceGuardFailReason, rlIpSourceGuardPermittedRuleCounterTable=rlIpSourceGuardPermittedRuleCounterTable, rlIpSourceGuardStatus=rlIpSourceGuardStatus, rlProtocolFilteringTable=rlProtocolFilteringTable, rlIpSourceGuardTable=rlIpSourceGuardTable, rlIpDhcpSnoopClearAction=rlIpDhcpSnoopClearAction, RlIpDhcpSnoopType=RlIpDhcpSnoopType, rlIpDhcpSnoopEntry=rlIpDhcpSnoopEntry, rlIpArpInspectListEntry=rlIpArpInspectListEntry, rlIpSourceGuardPermittedRuleCounterEntry=rlIpSourceGuardPermittedRuleCounterEntry, RlIpSourceGuardFailReason=RlIpSourceGuardFailReason, rlIpArpInspectEnableVlanTable=rlIpArpInspectEnableVlanTable, rlIpDhcpSnoopCurrentEntiresNumber=rlIpDhcpSnoopCurrentEntiresNumber, rlIpArpInspectListTable=rlIpArpInspectListTable, rlIpArpInspectMibVersion=rlIpArpInspectMibVersion, rlIpDhcpSnoopEnableVlanEntry=rlIpDhcpSnoopEnableVlanEntry, rlIpArpInspect=rlIpArpInspect, PYSNMP_MODULE_ID=rlBridgeSecurity, rlIpDhcpSnoopTrustedPortEntry=rlIpDhcpSnoopTrustedPortEntry, rlIpArpInspectEnableVlanTag=rlIpArpInspectEnableVlanTag, rlIpDhcpSnoopStaticRowStatus=rlIpDhcpSnoopStaticRowStatus, rlIpSourceGuardMACAddress=rlIpSourceGuardMACAddress, rlProtocolFilteringList=rlProtocolFilteringList, rlIpDhcpSnoopMACAddress=rlIpDhcpSnoopMACAddress, rlIpDhcpSnoopTable=rlIpDhcpSnoopTable, ProtocolFilteringMap=ProtocolFilteringMap, rlIpSourceGuard=rlIpSourceGuard, rlIpDhcpSnoopStaticTable=rlIpDhcpSnoopStaticTable, rlIpDhcpSnoopStaticEntry=rlIpDhcpSnoopStaticEntry, rlIpDhcpSnoopLeaseTime=rlIpDhcpSnoopLeaseTime, rlProtocolFilteringRowStatus=rlProtocolFilteringRowStatus, rlIpArpInspectEnableVlanRowStatus=rlIpArpInspectEnableVlanRowStatus, rlIpDhcpSnoopStaticPortInterface=rlIpDhcpSnoopStaticPortInterface, rlIpArpInspectClearCountersAction=rlIpArpInspectClearCountersAction, rlIpArpInspectLogInterval=rlIpArpInspectLogInterval, rlIpDhcpSnoopEnable=rlIpDhcpSnoopEnable, rlIpSourceGuardPermittedRuleCounterNumOfStaticRules=rlIpSourceGuardPermittedRuleCounterNumOfStaticRules)
#
# PySNMP MIB module DES3200-18-L3MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DES3200-18-L3MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:40:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, MibIdentifier, ObjectIdentity, Integer32, Counter64, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, ModuleIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Integer32", "Counter64", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "ModuleIdentity", "Bits", "Counter32")
TextualConvention, MacAddress, TruthValue, TimeStamp, DisplayString, PhysAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "TruthValue", "TimeStamp", "DisplayString", "PhysAddress", "RowStatus")
des3200_18, = mibBuilder.importSymbols("SWPRIMGMT-DES3200-MIB", "des3200-18")
swL3MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3))
if mibBuilder.loadTexts: swL3MgmtMIB.setLastUpdated('0911070000Z')
if mibBuilder.loadTexts: swL3MgmtMIB.setOrganization('D-Link, Inc.')
if mibBuilder.loadTexts: swL3MgmtMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swL3MgmtMIB.setDescription('The Structure of Layer 3 Network Management Information for enterprise.')
swL3DevMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 1))
swL3IpMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2))
swL3IpCtrlMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1))
class Ipv6Address(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 addresses. This is a binary string of 16 octets in network byte-order.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

swL3IpCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 3), )
if mibBuilder.loadTexts: swL3IpCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlTable.setDescription('This table contains IP interface information.')
swL3IpCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 3, 1), ).setIndexNames((0, "DES3200-18-L3MGMT-MIB", "swL3IpCtrlInterfaceName"))
if mibBuilder.loadTexts: swL3IpCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlEntry.setDescription('A list of information about a specific IP interface.')
swL3IpCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlInterfaceName.setDescription('This object indicates the name of the IP interface.')
swL3IpCtrlIpv6LinkLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 3, 1, 14), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAddress.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAddress.setDescription('The IPv6 link local address for this interface.')
swL3IpCtrlIpv6LinkLocalPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalPrefixLen.setDescription('The IPv6 prefix length for this IPv6 link local address.')
swL3IpCtrlIpv6LinkLocalAutoState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAutoState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAutoState.setDescription('The state of the IPv6 link local auto.')
swL3IpCtrlIpDhcpOption12State = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12State.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12State.setDescription('Enable or disable insertion of option 12 in the DHCPDISCOVER and DHCPREQUEST message.')
swL3IpCtrlIpDhcpOption12HostName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 3, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12HostName.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12HostName.setDescription('Specify the host name to be inserted in the DHCPDISCOVER and DHCPREQUEST message. The specified host name must start with a letter, end with a letter or digit, and have only letters, digits, and hyphen as interior characters; the maximal length is 63. By default, the host name is empty. When set an empty host name, means to clear the host name setting and use the default value to encode option 12.')
swL3Ipv6CtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 4), )
if mibBuilder.loadTexts: swL3Ipv6CtrlTable.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlTable.setDescription('This table contains IPv6 information of an IP interface.')
swL3Ipv6CtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 4, 1), ).setIndexNames((0, "DES3200-18-L3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"))
if mibBuilder.loadTexts: swL3Ipv6CtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlEntry.setDescription('A list of IPv6 information about a specific IP interface.')
swL3Ipv6CtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6CtrlInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlInterfaceName.setDescription('This object indicates the name of the IP interface.')
swL3Ipv6CtrlMaxReassmblySize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6CtrlMaxReassmblySize.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlMaxReassmblySize.setDescription('Maximum Reassembly Size of the IP interface.')
swL3Ipv6CtrlNsRetransTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlNsRetransTimer.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlNsRetransTimer.setDescription("Neighbor solicitation's retransmit timer. The unit is set in milliseconds.")
swL3Ipv6AddressCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 5), )
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlTable.setDescription('This table contains IPv6 address information for each IP interface.')
swL3Ipv6AddressCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 5, 1), ).setIndexNames((0, "DES3200-18-L3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"), (0, "DES3200-18-L3MGMT-MIB", "swL3Ipv6Address"), (0, "DES3200-18-L3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"))
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlEntry.setDescription('A list of information about a specific IPv6 address.')
swL3Ipv6AddressCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlInterfaceName.setDescription('This object indicates the name of the IP interface. ')
swL3Ipv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 5, 1, 2), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6Address.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6Address.setDescription('Specify the IPv6 address.')
swL3Ipv6AddressCtrlPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPrefixLen.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPrefixLen.setDescription('Indicates the prefix length of this IPv6 address.')
swL3Ipv6AddressCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlState.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlState.setDescription('This variable displays the status of the entry. The status is used for creating, modifying, and deleting instances of the objects in this table.')
swL3IpCtrlAllIpIfState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlAllIpIfState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlAllIpIfState.setDescription('This object indicates all interface function state of the device.')
mibBuilder.exportSymbols("DES3200-18-L3MGMT-MIB", swL3Ipv6AddressCtrlEntry=swL3Ipv6AddressCtrlEntry, swL3IpCtrlEntry=swL3IpCtrlEntry, swL3IpCtrlInterfaceName=swL3IpCtrlInterfaceName, swL3IpCtrlMgmt=swL3IpCtrlMgmt, swL3DevMgmt=swL3DevMgmt, PYSNMP_MODULE_ID=swL3MgmtMIB, swL3Ipv6AddressCtrlPrefixLen=swL3Ipv6AddressCtrlPrefixLen, swL3IpCtrlAllIpIfState=swL3IpCtrlAllIpIfState, swL3IpCtrlIpv6LinkLocalAddress=swL3IpCtrlIpv6LinkLocalAddress, swL3Ipv6CtrlNsRetransTimer=swL3Ipv6CtrlNsRetransTimer, swL3IpCtrlIpv6LinkLocalPrefixLen=swL3IpCtrlIpv6LinkLocalPrefixLen, Ipv6Address=Ipv6Address, swL3IpCtrlIpDhcpOption12HostName=swL3IpCtrlIpDhcpOption12HostName, swL3Ipv6CtrlInterfaceName=swL3Ipv6CtrlInterfaceName, swL3Ipv6AddressCtrlInterfaceName=swL3Ipv6AddressCtrlInterfaceName, swL3IpCtrlIpDhcpOption12State=swL3IpCtrlIpDhcpOption12State, swL3Ipv6AddressCtrlState=swL3Ipv6AddressCtrlState, swL3MgmtMIB=swL3MgmtMIB, swL3IpCtrlTable=swL3IpCtrlTable, swL3Ipv6AddressCtrlTable=swL3Ipv6AddressCtrlTable, swL3IpMgmt=swL3IpMgmt, swL3Ipv6Address=swL3Ipv6Address, swL3Ipv6CtrlMaxReassmblySize=swL3Ipv6CtrlMaxReassmblySize, swL3Ipv6CtrlEntry=swL3Ipv6CtrlEntry, swL3Ipv6CtrlTable=swL3Ipv6CtrlTable, swL3IpCtrlIpv6LinkLocalAutoState=swL3IpCtrlIpv6LinkLocalAutoState)
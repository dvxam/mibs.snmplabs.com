#
# PySNMP MIB module JUNIPER-JDHCPV6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JDHCPV6-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
Ipv6AddressPrefix, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix", "Ipv6Address")
jnxJdhcpv6MibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxJdhcpv6MibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Gauge32, Counter64, IpAddress, iso, ModuleIdentity, ObjectIdentity, MibIdentifier, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Gauge32", "Counter64", "IpAddress", "iso", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter32", "Integer32")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
jnxJdhcpv6MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62))
jnxJdhcpv6MIB.setRevisions(('2011-03-15 00:00', '2011-01-25 00:00', '2010-02-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxJdhcpv6MIB.setRevisionsDescriptions(('Add OIDs to the Interface Statistics Table', 'Add Interface Statistics Table', 'Creation Date',))
if mibBuilder.loadTexts: jnxJdhcpv6MIB.setLastUpdated('201103150000Z')
if mibBuilder.loadTexts: jnxJdhcpv6MIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxJdhcpv6MIB.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxJdhcpv6MIB.setDescription('The JUNOS DHCP MIB for the Juniper Networks enterprise.')
jnxJdhcpv6Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 1))
jnxJdhcpv6LocalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2))
jnxJdhcpv6LocalServerStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1))
jnxJdhcpv6LocalServerBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2))
jnxJdhcpv6LocalServerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3))
jnxJdhcpv6LocalServerTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4))
jnxJdhcpv6LocalServerIfcStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5))
jnxJdhcpv6LocalServerTotalDropped = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerTotalDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerTotalDropped.setDescription('Total DHCP v6 packets dropped.')
jnxJdhcpv6LocalServerNoSafdDropped = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerNoSafdDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerNoSafdDropped.setDescription('DHCPv6 packets dropped due to no safd match.')
jnxJdhcpv6LocalServerBadSendDropped = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBadSendDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBadSendDropped.setDescription('DHCPv6 packets dropped due to send error.')
jnxJdhcpv6LocalServerShortPacketDropped = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerShortPacketDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerShortPacketDropped.setDescription('DHCPv6 packets dropped due to packet being too short.')
jnxJdhcpv6LocalServerBadMsgtypeDropped = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBadMsgtypeDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBadMsgtypeDropped.setDescription('DHCPv6 packets dropped due to bad opcode in the packet.')
jnxJdhcpv6LocalServerBadOptionsDropped = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBadOptionsDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBadOptionsDropped.setDescription('DHCPv6 packets dropped due to bad options in the packet.')
jnxJdhcpv6LocalServerBadSrcAddressDropped = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBadSrcAddressDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBadSrcAddressDropped.setDescription('DHCPv6 packets dropped due to invalid addr family.')
jnxJdhcpv6LocalServerRelayHopCountDropped = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRelayHopCountDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRelayHopCountDropped.setDescription('DHCPv6 packets dropped due to max relays supported.')
jnxJdhcpv6LocalServerNoClientIdDropped = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerNoClientIdDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerNoClientIdDropped.setDescription('DHCPv6 packets dropped due to missing client id.')
jnxJdhcpv6LocalServerDeclineReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerDeclineReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerDeclineReceived.setDescription('The number of DHCPv6 Decline packets received.')
jnxJdhcpv6LocalServerSolicitReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerSolicitReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerSolicitReceived.setDescription('The number of DHCPv6 Solicit packets received.')
jnxJdhcpv6LocalServerInformationRequestReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInformationRequestReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInformationRequestReceived.setDescription('The number of DHCPv6 Information Request packets received.')
jnxJdhcpv6LocalServerReleaseReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerReleaseReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerReleaseReceived.setDescription('The number of DHCPv6 Release packets received.')
jnxJdhcpv6LocalServerRequestReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRequestReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRequestReceived.setDescription('The number of DHCPv6 Request packets received.')
jnxJdhcpv6LocalServerConfirmReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerConfirmReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerConfirmReceived.setDescription('The number of DHCPv6 Confirm packets received.')
jnxJdhcpv6LocalServerRenewReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRenewReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRenewReceived.setDescription('The number of DHCPv6 Renew packets received.')
jnxJdhcpv6LocalServerRebindReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRebindReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRebindReceived.setDescription('The number of DHCPv6 Rebind packets received.')
jnxJdhcpv6LocalServerRelayForwReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRelayForwReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRelayForwReceived.setDescription('The number of DHCPv6 Relay Fowr packets received.')
jnxJdhcpv6LocalServerRelayReplReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRelayReplReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerRelayReplReceived.setDescription('The number of DHCPv6 Relay Repl packets received.')
jnxJdhcpv6LocalServerAdvertiseSent = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerAdvertiseSent.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerAdvertiseSent.setDescription('The number of DHCPv6 Advertise packets sent.')
jnxJdhcpv6LocalServerReplySent = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerReplySent.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerReplySent.setDescription('The number of DHCPv6 Reply packets sent.')
jnxJdhcpv6LocalServerReconfigureSent = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerReconfigureSent.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerReconfigureSent.setDescription('The number of DHCPv6 Reconfigure packets sent.')
jnxJdhcpv6LocalServerTotalLeaseCount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerTotalLeaseCount.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerTotalLeaseCount.setDescription('The number of Bound DHCP Clients.')
jnxJdhcpv6LocalServerBindingsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1), )
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsTable.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsTable.setDescription('A table of address bindings maintained by this JUNOS DHCP Local Server.')
jnxJdhcpv6LocalServerBindingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1), ).setIndexNames((0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerBindingsPrefix"), (0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerBindingsLength"))
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsEntry.setDescription('An entry (conceptual row) representing an address binding (client) maintained by this JUNOS DHCP Local Server.')
jnxJdhcpv6LocalServerBindingsPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsPrefix.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsPrefix.setDescription('The prefix associated with this entry in the bindings table.')
jnxJdhcpv6LocalServerBindingsLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsLength.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsLength.setDescription('The length of the prefix in bits.')
jnxJdhcpv6LocalServerBindingsState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsState.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsState.setDescription('The state associated with this entry in the bindings table.')
jnxJdhcpv6LocalServerBindingsLeaseEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsLeaseEndTime.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsLeaseEndTime.setDescription('The time the lease expires on this binding.')
jnxJdhcpv6LocalServerBindingsLeaseExpireTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsLeaseExpireTime.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsLeaseExpireTime.setDescription('The time remaining until the lease expires for this binding.')
jnxJdhcpv6LocalServerBindingsLeaseStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsLeaseStartTime.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsLeaseStartTime.setDescription('The time the lease was started for this binding.')
jnxJdhcpv6LocalServerBindingsIncomingClientInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsIncomingClientInterface.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsIncomingClientInterface.setDescription('The incoming interface or this binding.')
jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId.setDescription('The VLAN ID for this binding.')
jnxJdhcpv6LocalServerBindingsDemuxInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsDemuxInterfaceName.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsDemuxInterfaceName.setDescription('The demux interface for this binding.')
jnxJdhcpv6LocalServerBindingsServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsServerIpAddress.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsServerIpAddress.setDescription('The IP Address associated with the server for this entry in the bindings table.')
jnxJdhcpv6LocalServerBindingsBootpRelayAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsBootpRelayAddress.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsBootpRelayAddress.setDescription('The BOOTP relay Address associated with the server for this entry in the bindings table.')
jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress.setDescription('The Previous BOOTP relay Address associated with the server for this entry in the bindings table.')
jnxJdhcpv6LocalServerBindingsClientPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsClientPoolName.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsClientPoolName.setDescription('The display client pool name.')
jnxJdhcpv6LocalServerBindingsClientProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsClientProfileName.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerBindingsClientProfileName.setDescription('The display client profile name.')
jnxJdhcpv6LocalServerIfcStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1), )
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsTable.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsTable.setDescription('A table of interface statistics maintained by this JUNOS DHCPv6 Local Server.')
jnxJdhcpv6LocalServerIfcStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1), ).setIndexNames((0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerIfcStatsIfIndex"))
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsEntry.setDescription('An entry (conceptual row) representing an address binding (client) maintained by this JUNOS DHCPv6 Local Server.')
jnxJdhcpv6LocalServerIfcStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsIfIndex.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsIfIndex.setDescription('The ifIndex value of the interface for which this entry contains information.')
jnxJdhcpv6LocalServerIfcStatsTotalDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsTotalDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsTotalDropped.setDescription('Total DHCP v6 packets dropped.')
jnxJdhcpv6LocalServerIfcStatsNoSafdDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsNoSafdDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsNoSafdDropped.setDescription('DHCPv6 packets dropped due to no safd match.')
jnxJdhcpv6LocalServerIfcStatsBadSendDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsBadSendDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsBadSendDropped.setDescription('DHCPv6 packets dropped due to send error.')
jnxJdhcpv6LocalServerIfcStatsShortPacketDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsShortPacketDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsShortPacketDropped.setDescription('DHCPv6 packets dropped due to packet being too short.')
jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped.setDescription('DHCPv6 packets dropped due to bad opcode in the packet.')
jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped.setDescription('DHCPv6 packets dropped due to bad options in the packet.')
jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped.setDescription('DHCPv6 packets dropped due to invalid addr family.')
jnxJdhcpv6LocalServerIfcStatsRelayCountDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRelayCountDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRelayCountDropped.setDescription('DHCPv6 packets dropped due to max relays supported.')
jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped.setDescription('DHCPv6 packets dropped due to missing client id.')
jnxJdhcpv6LocalServerIfcStatsDeclineReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsDeclineReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsDeclineReceived.setDescription('The number of DHCPv6 Decline packets received.')
jnxJdhcpv6LocalServerIfcStatsSolicitReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsSolicitReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsSolicitReceived.setDescription('The number of DHCPv6 Solicit packets received.')
jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived.setDescription('The number of DHCPv6 Information Request packets received.')
jnxJdhcpv6LocalServerIfcStatsReleaseReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsReleaseReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsReleaseReceived.setDescription('The number of DHCPv6 Release packets received.')
jnxJdhcpv6LocalServerIfcStatsRequestReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRequestReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRequestReceived.setDescription('The number of DHCPv6 Request packets received.')
jnxJdhcpv6LocalServerIfcStatsConfirmReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsConfirmReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsConfirmReceived.setDescription('The number of DHCPv6 Confirm packets received.')
jnxJdhcpv6LocalServerIfcStatsRenewReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRenewReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRenewReceived.setDescription('The number of DHCPv6 Renew packets received.')
jnxJdhcpv6LocalServerIfcStatsRebindReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRebindReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRebindReceived.setDescription('The number of DHCPv6 Rebind packets received.')
jnxJdhcpv6LocalServerIfcStatsRelayForwReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRelayForwReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRelayForwReceived.setDescription('The number of DHCPv6 Relay Fowr packets received.')
jnxJdhcpv6LocalServerIfcStatsRelayReplReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRelayReplReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsRelayReplReceived.setDescription('The number of DHCPv6 Relay Repl packets received.')
jnxJdhcpv6LocalServerIfcStatsAdvertiseSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsAdvertiseSent.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsAdvertiseSent.setDescription('The number of DHCPv6 Advertise packets sent.')
jnxJdhcpv6LocalServerIfcStatsReplySent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsReplySent.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsReplySent.setDescription('The number of DHCPv6 Reply packets sent.')
jnxJdhcpv6LocalServerIfcStatsReconfigureSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsReconfigureSent.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsReconfigureSent.setDescription('The number of DHCPv6 Reconfigure packets sent.')
jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount.setDescription('The number of Bound DHCP Clients.')
jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped.setDescription('The number of packets dropped due to strict reconfigure.')
jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped.setDescription('The number of packets dropped due to authentication failure.')
jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped.setDescription('The number of packets dropped due to dynamic profile error.')
jnxJdhcpv6LocalServerIfcStatsLicenseDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsLicenseDropped.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerIfcStatsLicenseDropped.setDescription('The number of packets dropped due to license error.')
jnxJdhcpv6RouterName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJdhcpv6RouterName.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6RouterName.setDescription('The VRF ID in JUNOS. Represented as the Logical Router (LR) Name followed by the Router Instance (RI) Name.')
jnxJdhcpv6LocalServerInterfaceName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInterfaceName.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInterfaceName.setDescription('The interface where the DHCP client was detected')
jnxJdhcpv6LocalServerInterfaceLimit = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInterfaceLimit.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInterfaceLimit.setDescription('The number of clients supported on this interface.')
jnxJdhcpv6LocalServerEventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("debug", 0), ("warning", 1), ("critical", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerEventSeverity.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerEventSeverity.setDescription('The level of error. ')
jnxJdhcpv6LocalServerEventString = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerEventString.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerEventString.setDescription('The text of the event string associated with the health event.')
jnxJdhcpv6LocalServerInterfaceLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3, 1)).setObjects(("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RouterName"), ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceName"), ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceLimit"))
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInterfaceLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInterfaceLimitExceeded.setDescription('Reports when the limit of clients has been exceeded on an interface.')
jnxJdhcpv6LocalServerInterfaceLimitAbated = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3, 2)).setObjects(("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RouterName"), ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceName"), ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceLimit"))
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInterfaceLimitAbated.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerInterfaceLimitAbated.setDescription('Reports when the number of clients on an interface has fallen below the limit allowed on that interface.')
jnxJdhcpv6LocalServerHealth = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3, 4)).setObjects(("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RouterName"), ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerEventSeverity"), ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerEventString"))
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerHealth.setStatus('current')
if mibBuilder.loadTexts: jnxJdhcpv6LocalServerHealth.setDescription('Reports when a health event occurs in the V6 Local Server application.')
mibBuilder.exportSymbols("JUNIPER-JDHCPV6-MIB", jnxJdhcpv6LocalServerTotalDropped=jnxJdhcpv6LocalServerTotalDropped, jnxJdhcpv6LocalServerRelayHopCountDropped=jnxJdhcpv6LocalServerRelayHopCountDropped, jnxJdhcpv6LocalServerIfcStatsRebindReceived=jnxJdhcpv6LocalServerIfcStatsRebindReceived, jnxJdhcpv6LocalServerBindingsTable=jnxJdhcpv6LocalServerBindingsTable, jnxJdhcpv6LocalServerIfcStatsTotalDropped=jnxJdhcpv6LocalServerIfcStatsTotalDropped, jnxJdhcpv6LocalServerReconfigureSent=jnxJdhcpv6LocalServerReconfigureSent, jnxJdhcpv6LocalServerTraps=jnxJdhcpv6LocalServerTraps, jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount=jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount, jnxJdhcpv6Objects=jnxJdhcpv6Objects, jnxJdhcpv6LocalServerAdvertiseSent=jnxJdhcpv6LocalServerAdvertiseSent, jnxJdhcpv6LocalServerInformationRequestReceived=jnxJdhcpv6LocalServerInformationRequestReceived, jnxJdhcpv6LocalServerIfcStatsRelayCountDropped=jnxJdhcpv6LocalServerIfcStatsRelayCountDropped, jnxJdhcpv6LocalServerInterfaceLimitAbated=jnxJdhcpv6LocalServerInterfaceLimitAbated, jnxJdhcpv6LocalServerConfirmReceived=jnxJdhcpv6LocalServerConfirmReceived, jnxJdhcpv6LocalServerIfcStatsIfIndex=jnxJdhcpv6LocalServerIfcStatsIfIndex, jnxJdhcpv6LocalServerTotalLeaseCount=jnxJdhcpv6LocalServerTotalLeaseCount, jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped=jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped, jnxJdhcpv6LocalServerIfcStatsReplySent=jnxJdhcpv6LocalServerIfcStatsReplySent, jnxJdhcpv6LocalServerIfcStatsRenewReceived=jnxJdhcpv6LocalServerIfcStatsRenewReceived, jnxJdhcpv6LocalServerBadMsgtypeDropped=jnxJdhcpv6LocalServerBadMsgtypeDropped, jnxJdhcpv6LocalServerIfcStatsEntry=jnxJdhcpv6LocalServerIfcStatsEntry, jnxJdhcpv6LocalServerNoClientIdDropped=jnxJdhcpv6LocalServerNoClientIdDropped, jnxJdhcpv6LocalServerTrapVars=jnxJdhcpv6LocalServerTrapVars, jnxJdhcpv6LocalServerBadSrcAddressDropped=jnxJdhcpv6LocalServerBadSrcAddressDropped, jnxJdhcpv6LocalServerBindingsIncomingClientInterface=jnxJdhcpv6LocalServerBindingsIncomingClientInterface, jnxJdhcpv6RouterName=jnxJdhcpv6RouterName, jnxJdhcpv6LocalServerBindingsDemuxInterfaceName=jnxJdhcpv6LocalServerBindingsDemuxInterfaceName, jnxJdhcpv6LocalServerShortPacketDropped=jnxJdhcpv6LocalServerShortPacketDropped, jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped=jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped, jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress=jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress, jnxJdhcpv6LocalServerDeclineReceived=jnxJdhcpv6LocalServerDeclineReceived, jnxJdhcpv6LocalServerIfcStatsReleaseReceived=jnxJdhcpv6LocalServerIfcStatsReleaseReceived, jnxJdhcpv6LocalServerBindingsEntry=jnxJdhcpv6LocalServerBindingsEntry, jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived=jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived, jnxJdhcpv6LocalServerBindings=jnxJdhcpv6LocalServerBindings, jnxJdhcpv6LocalServerRenewReceived=jnxJdhcpv6LocalServerRenewReceived, jnxJdhcpv6LocalServerBindingsLeaseEndTime=jnxJdhcpv6LocalServerBindingsLeaseEndTime, jnxJdhcpv6LocalServerIfcStats=jnxJdhcpv6LocalServerIfcStats, jnxJdhcpv6LocalServerBadOptionsDropped=jnxJdhcpv6LocalServerBadOptionsDropped, jnxJdhcpv6LocalServerIfcStatsRequestReceived=jnxJdhcpv6LocalServerIfcStatsRequestReceived, jnxJdhcpv6LocalServerInterfaceLimitExceeded=jnxJdhcpv6LocalServerInterfaceLimitExceeded, jnxJdhcpv6LocalServerNoSafdDropped=jnxJdhcpv6LocalServerNoSafdDropped, jnxJdhcpv6LocalServerBindingsLength=jnxJdhcpv6LocalServerBindingsLength, jnxJdhcpv6LocalServerInterfaceLimit=jnxJdhcpv6LocalServerInterfaceLimit, jnxJdhcpv6LocalServerEventSeverity=jnxJdhcpv6LocalServerEventSeverity, jnxJdhcpv6LocalServerBindingsServerIpAddress=jnxJdhcpv6LocalServerBindingsServerIpAddress, jnxJdhcpv6LocalServerHealth=jnxJdhcpv6LocalServerHealth, jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped=jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped, jnxJdhcpv6LocalServerRequestReceived=jnxJdhcpv6LocalServerRequestReceived, jnxJdhcpv6LocalServerIfcStatsRelayForwReceived=jnxJdhcpv6LocalServerIfcStatsRelayForwReceived, jnxJdhcpv6LocalServerBindingsClientProfileName=jnxJdhcpv6LocalServerBindingsClientProfileName, jnxJdhcpv6LocalServerIfcStatsBadSendDropped=jnxJdhcpv6LocalServerIfcStatsBadSendDropped, jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped=jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped, jnxJdhcpv6LocalServerObjects=jnxJdhcpv6LocalServerObjects, jnxJdhcpv6LocalServerBadSendDropped=jnxJdhcpv6LocalServerBadSendDropped, jnxJdhcpv6LocalServerIfcStatsLicenseDropped=jnxJdhcpv6LocalServerIfcStatsLicenseDropped, jnxJdhcpv6LocalServerIfcStatsRelayReplReceived=jnxJdhcpv6LocalServerIfcStatsRelayReplReceived, jnxJdhcpv6LocalServerIfcStatsSolicitReceived=jnxJdhcpv6LocalServerIfcStatsSolicitReceived, jnxJdhcpv6LocalServerRelayReplReceived=jnxJdhcpv6LocalServerRelayReplReceived, jnxJdhcpv6LocalServerIfcStatsShortPacketDropped=jnxJdhcpv6LocalServerIfcStatsShortPacketDropped, jnxJdhcpv6LocalServerInterfaceName=jnxJdhcpv6LocalServerInterfaceName, jnxJdhcpv6LocalServerIfcStatsReconfigureSent=jnxJdhcpv6LocalServerIfcStatsReconfigureSent, jnxJdhcpv6LocalServerIfcStatsConfirmReceived=jnxJdhcpv6LocalServerIfcStatsConfirmReceived, jnxJdhcpv6LocalServerEventString=jnxJdhcpv6LocalServerEventString, jnxJdhcpv6LocalServerBindingsLeaseExpireTime=jnxJdhcpv6LocalServerBindingsLeaseExpireTime, jnxJdhcpv6LocalServerRelayForwReceived=jnxJdhcpv6LocalServerRelayForwReceived, jnxJdhcpv6LocalServerReleaseReceived=jnxJdhcpv6LocalServerReleaseReceived, PYSNMP_MODULE_ID=jnxJdhcpv6MIB, jnxJdhcpv6LocalServerReplySent=jnxJdhcpv6LocalServerReplySent, jnxJdhcpv6LocalServerBindingsState=jnxJdhcpv6LocalServerBindingsState, jnxJdhcpv6LocalServerIfcStatsAdvertiseSent=jnxJdhcpv6LocalServerIfcStatsAdvertiseSent, jnxJdhcpv6LocalServerIfcStatsDeclineReceived=jnxJdhcpv6LocalServerIfcStatsDeclineReceived, jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped=jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped, jnxJdhcpv6MIB=jnxJdhcpv6MIB, jnxJdhcpv6LocalServerIfcStatsTable=jnxJdhcpv6LocalServerIfcStatsTable, jnxJdhcpv6LocalServerBindingsBootpRelayAddress=jnxJdhcpv6LocalServerBindingsBootpRelayAddress, jnxJdhcpv6LocalServerBindingsClientPoolName=jnxJdhcpv6LocalServerBindingsClientPoolName, jnxJdhcpv6LocalServerIfcStatsNoSafdDropped=jnxJdhcpv6LocalServerIfcStatsNoSafdDropped, jnxJdhcpv6LocalServerRebindReceived=jnxJdhcpv6LocalServerRebindReceived, jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped=jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped, jnxJdhcpv6LocalServerBindingsPrefix=jnxJdhcpv6LocalServerBindingsPrefix, jnxJdhcpv6LocalServerStatistics=jnxJdhcpv6LocalServerStatistics, jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId=jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId, jnxJdhcpv6LocalServerSolicitReceived=jnxJdhcpv6LocalServerSolicitReceived, jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped=jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped, jnxJdhcpv6LocalServerBindingsLeaseStartTime=jnxJdhcpv6LocalServerBindingsLeaseStartTime)
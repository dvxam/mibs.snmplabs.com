#
# PySNMP MIB module A3COM-IPEXTNS-R5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/A3COM-IPEXTNS-R5-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:32:21 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, enterprises, ModuleIdentity, NotificationType, IpAddress, Counter32, ObjectIdentity, Bits, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "enterprises", "ModuleIdentity", "NotificationType", "IpAddress", "Counter32", "ObjectIdentity", "Bits", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComIPextns = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 6))
class SMDSAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3IPextMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("multipleNet", 1), ("singleNet", 2))).clone('multipleNet')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPextMode.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPextMode.setDescription('This object determines the mode the IP protocol layer operates in. When in multipleNet mode, the system will accept different network addresses for each of its interfaces. Routing may be disabled (via ipForwarding), but the system will still be in routing mode, i.e., it will keep all of its assigned addresses and it may still participate in routing update protocols (if configured). When in singleNet mode, the IP address assigned to interfaces 1 is applied to all interfaces. ipForwarding can only be disabled, and all RIP parameters, other than those related to listening, will be ignored. Note, when the value of this object is changed, the new IP address must also be set in the same PDU. This is required to ensure connectivity remains. When this object transitions from multipleNet mode to singleNet mode, 1) ipForwarding is automatically set to not-forwarding, 2) all RIP-IP parameters will be ignored except those related to listening on interface 1. These parameters will be applied to all interfaces. 3) an IP address must be configured, in the same request, for interface 1. the agent removes all other IP addresses, and the IP address assigned to interface 1 will apply to all interfaces. When this object transitions back to multipleNet mode, 1) an IP address must be assigned, in the same request, to one of the ports, that IP address will apply only to that port to which it is assigned. The IP address for interface 1 will no longer apply to all interfaces. 2) ipForwarding will stay at not-forwarding, and 3) all previously ignored RIP-IP parameters will take effect. In order to actively route packets, ipForwarding will need to be set to forwarding. During this transition, there is the danger that no IP address will have been configured for the interface that receives the SNMP requests, in which case, the device will no longer be manageable. For this reason, it is suggested that the IP addresses for the interface that receives the SNMP requests be set in the same PDU that sets this object.')
a3IPextFlushCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("flushRoutes", 2), ("flushARP", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPextFlushCtl.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPextFlushCtl.setDescription('When set to 2, this object can be used to remove all dynamically learned entries from the IP routing table. When set to 3, this object can be used to remove dynamically learned entries from the Address Resolution Table.')
a3IPextRelaySrcRteCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("relay", 1), ("discard", 2))).clone('discard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPextRelaySrcRteCtl.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPextRelaySrcRteCtl.setDescription('This object is used to control the relaying of packets that contain the Loose or Strict source route option. If this object is set to relay (1), those packets are relayed. If this object is set to discard (2), those packets are discarded.')
a3IPextSplitLoadCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("split", 1), ("noSplit", 2))).clone('noSplit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPextSplitLoadCtl.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPextSplitLoadCtl.setDescription('This object is used to control load splitting. If split (1), is specified, the traffic load is distributed among a set of least-equal-cost paths. These paths are selected on a round-robin basis. If a path is unreachable, it is not considered a candidate for load splitting.')
a3IPicmpInfoCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("info", 1), ("noInfo", 2))).clone('noInfo')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpInfoCtl.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPicmpInfoCtl.setDescription('This object determines whether this system replies to ICMP Information request packets. If this object is set to info (1), replies are sent. Otherwise, no replies are sent.')
a3IPicmpMaskCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mask", 1), ("noMask", 2))).clone('noMask')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpMaskCtl.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPicmpMaskCtl.setDescription('This object determines whether this system replies to ICMP Address Mask request packets. If this object is set to mask (1), replies are sent. Otherwise, no replies are sent.')
a3IPntmExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 7), )
if mibBuilder.loadTexts: a3IPntmExtTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPntmExtTable.setDescription('This table is an extension of the ipNetToMediaTable from mibII. Currently, this table contains objects for controlling MAC header formats and for controlling proxy ARP for each entry.')
a3IPntmExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPntmIfIndex"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPntmNetAddress"))
if mibBuilder.loadTexts: a3IPntmExtEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPntmExtEntry.setDescription('Each entry in this table corresponds to an entry in the ipNetToMediaTable. Additional columnar objects are defined in this table that are not in the original table.')
a3IPntmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPntmIfIndex.setReference('RFC1213, p. 38, ipNetToMediaTable')
if mibBuilder.loadTexts: a3IPntmIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPntmIfIndex.setDescription("The interface on which this entry's equivalence is effective.")
a3IPntmNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPntmNetAddress.setReference('RFC1213, p. 38, ipNetToMediaTable')
if mibBuilder.loadTexts: a3IPntmNetAddress.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPntmNetAddress.setDescription('The IpAddress corresponding to the media-dependent physical address.')
a3IPntmHdrFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ethernet", 2), ("ieee", 3), ("snap", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPntmHdrFormat.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPntmHdrFormat.setDescription('The header format to be used when sending packets to the destination specified by this table entry. This parameter only applies to networks that support MAC addresses. Entries that correspond to other network types have the value other (1).')
a3IPntmProxyArp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("proxy", 1), ("noProxy", 2))).clone('noProxy')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPntmProxyArp.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPntmProxyArp.setDescription('If this object is set to proxy (1), the system will respond to ARP requests for the IP address of this entry. If this object is set to noProxy (2), no response will be sent.')
a3IPaddrConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 8), )
if mibBuilder.loadTexts: a3IPaddrConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPaddrConfigTable.setDescription('This table contains the IP addresses assigned to each IP port.')
a3IPaddrConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPaddrConfigPort"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPaddrConfigAddr"))
if mibBuilder.loadTexts: a3IPaddrConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPaddrConfigEntry.setDescription('Each entry contains a single IP address and parameters relating to routing IP over a specific port.')
a3IPaddrConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPaddrConfigPort.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPaddrConfigPort.setDescription('The port to which this entry applies.')
a3IPaddrConfigAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPaddrConfigAddr.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPaddrConfigAddr.setDescription('The IP address to which this entry applies.')
a3IPaddrConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigType.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPaddrConfigType.setDescription("When multiple IP addresses are configured for a single interface, this object is used to determine which address is the 'primary' address. 'Primary' addresses are used as the source IP address in packets sent from that interface. When there is only one address configured for an interface, it will be the 'primary' address. If there is an existing 'primary' address when this object is set to primary (1), the existing 'primary' address will be set to 'secondary' automatically.")
a3IPaddrConfigNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigNetMask.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPaddrConfigNetMask.setDescription('The subnet mask associated with the IP address of this entry. The value of the mask is an IP address with all the network bits set to 1 and all the host bits set to 0. If this is not specified, the system will select a mask based on the IP address class.')
a3IPaddrConfigBcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 5), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigBcastAddr.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPaddrConfigBcastAddr.setDescription('The value of the least-significant bit in the IP broadcast address used for sending datagrams on the logical interface associated with the IP address of this entry.')
a3IPaddrConfigMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(68, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigMtu.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPaddrConfigMtu.setDescription('The size of the largest IP datagram which is supported by the logical interface associated with the IP address of this entry. If this is not specified, the system will select a value based on the interface type.')
a3IPaddrConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPaddrConfigStatus.setDescription('This object is used to add and delete entries in this table. See the notes describing RowStatus at the beginning of this MIB.')
a3IPforwardExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 9), )
if mibBuilder.loadTexts: a3IPforwardExtTable.setReference('RFC 1354, ipForwardTable.')
if mibBuilder.loadTexts: a3IPforwardExtTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPforwardExtTable.setDescription('An extension to the ipForwardTable.')
a3IPforwardExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtDest"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtProto"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtPolicy"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtNextHop"))
if mibBuilder.loadTexts: a3IPforwardExtEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPforwardExtEntry.setDescription('Each entry in this table corresponds to a single entry in the ipForwardTable. An additional columnar object has been defined to indicate whether a dynamically learned route may take precendence of a particular static route.')
a3IPforwardExtDest = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPforwardExtDest.setReference('RFC 1354, ipForwardTable.')
if mibBuilder.loadTexts: a3IPforwardExtDest.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPforwardExtDest.setDescription('The destination IP address of this route. This is identical to ipForwardDest.')
a3IPforwardExtProto = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("is-is", 9), ("es-is", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPforwardExtProto.setReference('RFC 1354, ipForwardTable.')
if mibBuilder.loadTexts: a3IPforwardExtProto.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPforwardExtProto.setDescription('The routing mechanism via which this route was learned.')
a3IPforwardExtPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPforwardExtPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPforwardExtPolicy.setDescription("The general set of conditions that would cause the selection of one multipath route (set of next hops for a given destination) is referred to as 'policy'. Unless the mechanism indicated by ipForwardPro- to specifies otherwise, the policy specifier is the IP TOS Field. The encoding of IP TOS is as specified by rfc1354. Zero indicates the default path if no more specific policy applies. Currently, zero is the only TOS value supported by 3Com.")
a3IPforwardExtNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPforwardExtNextHop.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPforwardExtNextHop.setDescription('On remote routes, the address of the next system en route. Otherwise, 0.0.0.0')
a3IPforwardExtOverride = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("override", 1), ("noOverride", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPforwardExtOverride.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPforwardExtOverride.setDescription('This object is used to identify those static routes that may be overridden by dynamically learned routes. For those entries in this table that represent dynamically learned routes, this object will have the value noOverride (2) at all times.')
a3IParpOverBlocked = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpOverBlocked.setStatus('mandatory')
if mibBuilder.loadTexts: a3IParpOverBlocked.setDescription('When the system is in singleNet mode (ie, it is in a bridge state), this parameter controls whether or not ARP request and replies are allowed to be sent or received over a non-forwarding bridged port. If this is set enabled(1), then ARP requests and replies are allowed over non-forwarding ports. If this is set disabled(2), they are not allowed. This object corresponds to the UI parameter: -arp OverBlocked.')
a3IPrarpClientCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPrarpClientCtl.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPrarpClientCtl.setDescription('This allows the RARP client function to be enabled or disabled. If enabled, this system will send RARP requests. If disabled, the system will not send RARP requests. This object corresponds to the UI parameter: -arp RarpCONTrol.')
a3IPrarpServerCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPrarpServerCtl.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPrarpServerCtl.setDescription('This allows the RARP server function to be enabled or disabled. If enabled, this system will respond to RARP requests. If disabled, this system will not respond. This object corresponds to the UI parameter: -arp RarpCONTrol.')
a3IParpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 13), )
if mibBuilder.loadTexts: a3IParpConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3IParpConfigTable.setDescription('This table contains ARP configuration information.')
a3IParpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IParpPortIndex"))
if mibBuilder.loadTexts: a3IParpConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3IParpConfigEntry.setDescription('Each entry in this table contains port-specific ARP configuration information.')
a3IParpPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IParpPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3IParpPortIndex.setDescription('The port index to which these entries apply.')
a3IParpProxyCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("proxy", 1), ("noProxy", 2))).clone('noProxy')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpProxyCtl.setStatus('mandatory')
if mibBuilder.loadTexts: a3IParpProxyCtl.setDescription("This object applies to ARP requests for networks or subnetworks that are in the IP routing table. When this is the case, this system will respond to the request with the MAC address of this system's interface if the value of this object is proxy (1). Otherwise, no ARP response is sent. This object corresponds to the UI parameter: -arp control")
a3IParpHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)).clone(24)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpHoldTime.setStatus('mandatory')
if mibBuilder.loadTexts: a3IParpHoldTime.setDescription('This object determines the amount of time, in hours, an entry can stay in the ARP table. When the specified time elapses, the entry is deleted. When one sixteenth of the time elapses, ARP considers this entry aged. When a packet is destined for an entry that has become aged, the system sends an ARP request, using a unicast address, to the destination to verify whether it is still operational. This object corresponds to the UI parameter: -arp HoldTime.')
a3IParpReqFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 128, 129, 130, 131))).clone(namedValues=NamedValues(("ethernet", 1), ("snap", 2), ("both", 3), ("auto", 128), ("ethAuto", 129), ("snapAuto", 130), ("bothAuto", 131))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpReqFormat.setStatus('mandatory')
if mibBuilder.loadTexts: a3IParpReqFormat.setDescription('This parameter specifies the Ethernet header format used for ARP requests. If this is set to ethernet (1), ARP sends requests with an Ethernet Version 2 header. If this is set to snap (2), ARP sends requests with the IEEE 802.2 and 802.3 headers, including the Snap extension. If this is set to both (3), ARP sends two request packets, one with Ethernet format and one with the Snap extensions. If this is set to auto(128), the default request format is based on the media type of the interface with which this parameter is associated. When GETting the value of this object, the first three enumerations (ethernet, snap, and both) are returned if this parmeter was explicitly set to one of these values. If this parameter was set to auto(128), either ethAuto(129), snapAuto(130), or bothAuto(131) will be returned, depending on which header format is the most appropriate (which is based on the media type of the associated interface). This object corresponds to the UI parameter: -arp RequestFormat.')
a3IParpRemAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpRemAddr.setStatus('mandatory')
if mibBuilder.loadTexts: a3IParpRemAddr.setDescription('The value of this object reflects the IP address that is assigned to the boundary router that is attached to this port. This address is used when a RARP request is received from that boundary router. For those ports that are not attached to a boundary router, this object will have no meaning and no affect on the system.')
a3IParpInvCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpInvCtl.setStatus('mandatory')
if mibBuilder.loadTexts: a3IParpInvCtl.setDescription('This object specifies whether inverse arp is enabled on this port. Note, this affects only Frame Relay ports.')
a3IPsmdsGaTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 14), )
if mibBuilder.loadTexts: a3IPsmdsGaTable.setReference('NETBuilder Ref. Guide, IP service Parameter: GroupAddress.')
if mibBuilder.loadTexts: a3IPsmdsGaTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPsmdsGaTable.setDescription('This table contains a set of IP network address to SMDS Group Address pairings.')
a3IPsmdsGaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPsmdsGaIpNet"))
if mibBuilder.loadTexts: a3IPsmdsGaEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPsmdsGaEntry.setDescription('Each entry in this table contains a single IP network address to SMDS Group Address mapping. This is used in applications running IP over SMDS.')
a3IPsmdsGaIpNet = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPsmdsGaIpNet.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPsmdsGaIpNet.setDescription('This is an IP network address for which there is a corresponding SMDS Group Address.')
a3IPsmdsGa = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1, 2), SMDSAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsmdsGa.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPsmdsGa.setDescription('This is the SMDS Group Address that corresponds to the IP network address identified by a3IPsmdsGaIpNet.')
a3IPsmdsGaStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsmdsGaStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPsmdsGaStatus.setDescription('This object is used to add and delete entries in this table. See the notes describing RowStatus at the beginning of this MIB.')
a3IPx25configTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 15), )
if mibBuilder.loadTexts: a3IPx25configTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPx25configTable.setDescription('This table contains a set of X25 configuration parameters relating to routing IP over x25 networks.')
a3IPx25configEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPx25configPort"))
if mibBuilder.loadTexts: a3IPx25configEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPx25configEntry.setDescription('Each entry contains a set of x25 configuration parameters relating to routing IP over a specific port.')
a3IPx25configPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPx25configPort.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPx25configPort.setDescription('The port number to which this table entry applies.')
a3IPx25configPID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(204)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configPID.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPx25configPID.setDescription('The protocol ID that is included in all outgoing IP packets sent over the x25 port associated with this table entry.')
a3IPx25configQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configQueueSize.setStatus('deprecated')
if mibBuilder.loadTexts: a3IPx25configQueueSize.setDescription('The maximum number of packets that can be queued for a specific DTE address when the virtual circuit or the x25 port is congested. NOTE: this object is no longer supported by NETBuilders running sw version 8.0 and greater.')
a3IPx25configVClimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configVClimit.setStatus('deprecated')
if mibBuilder.loadTexts: a3IPx25configVClimit.setDescription('The maximum number of virtual circuits that can be established concurrently for IP routing. NOTE: this object is no longer supported by NETBuilders running sw version 8.0 and greater.')
a3IPx25configVCtimer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configVCtimer.setStatus('deprecated')
if mibBuilder.loadTexts: a3IPx25configVCtimer.setDescription('The maximum amount of time, in minutes, that can elapse when there is no activity on the x25 virtual circuit before it is cleared. This applies to the first virtual circuit established for a particular DTE address. IF more than one virtual circuit is established for the same DTE address, all are cleared (except for the first one established) when the first virtual circuit is not experiencing congestion. NOTE: this object is no longer supported by NETBuilders running sw version 8.0 and greater.')
a3IPx25configProfID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configProfID.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPx25configProfID.setDescription('This object specifies the X25 User ProfileID to be used for selecting a Virtual Circuit to send IP Packets. Range is 0..255. If the value specified is 0 then use the DTE Profile ID')
a3IPqueuePriority = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("high", 1), ("medium", 2), ("low", 3), ("default", 4), ("unknown", 5))).clone('medium')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPqueuePriority.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPqueuePriority.setDescription('This object, which is used by the Multiple Priority Queue feature, specifies into which queue IP packets are placed. If this object has the value default(4), then IP packets are placed in the system default queue as specified by a3ComDefaultPriority.')
a3IPfwdSubnetBcast = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fwdSubnetBcast", 1), ("noFwdSubnetBcast", 2))).clone('noFwdSubnetBcast')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPfwdSubnetBcast.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPfwdSubnetBcast.setDescription('')
a3IPicmpGenTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 18), )
if mibBuilder.loadTexts: a3IPicmpGenTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPicmpGenTable.setDescription('This table contains ICMP configuration information.')
a3IPicmpGenEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPicmpGenIfIndex"))
if mibBuilder.loadTexts: a3IPicmpGenEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPicmpGenEntry.setDescription('Each entry in this table contains port-specific ICMP configuration information.')
a3IPicmpGenIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPicmpGenIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPicmpGenIfIndex.setDescription('The port to which this entry applies.')
a3IPicmpGenRedirect = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redirect", 1), ("noRedirect", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpGenRedirect.setReference('NETBuilder Ref. Guide, IP service Parameter: ICMPGenerate.')
if mibBuilder.loadTexts: a3IPicmpGenRedirect.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPicmpGenRedirect.setDescription('This object controls whether ICMP issues ReDirect packets on this port.')
a3IPicmpGenDestUnreach = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("destUnreachable", 1), ("noDestUnreachable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpGenDestUnreach.setReference('NETBuilder Ref. Guide, IP service Parameter: ICMPGenerate.')
if mibBuilder.loadTexts: a3IPicmpGenDestUnreach.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPicmpGenDestUnreach.setDescription('This object controls whether ICMP issues Destination Unreachable packets on this port.')
a3IPicmpGenTimeExceed = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("timeExceed", 1), ("noTimeExceed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpGenTimeExceed.setReference('NETBuilder Ref. Guide, IP service Parameter: ICMPGenerate.')
if mibBuilder.loadTexts: a3IPicmpGenTimeExceed.setStatus('mandatory')
if mibBuilder.loadTexts: a3IPicmpGenTimeExceed.setDescription('This object controls whether ICMP issues Time Exceeded packets on this port.')
mibBuilder.exportSymbols("A3COM-IPEXTNS-R5-MIB", a3IPntmExtTable=a3IPntmExtTable, a3IPntmIfIndex=a3IPntmIfIndex, a3IPx25configPID=a3IPx25configPID, a3IPsmdsGaEntry=a3IPsmdsGaEntry, a3IPx25configVCtimer=a3IPx25configVCtimer, a3IPaddrConfigEntry=a3IPaddrConfigEntry, RowStatus=RowStatus, a3IPaddrConfigType=a3IPaddrConfigType, a3IPicmpGenIfIndex=a3IPicmpGenIfIndex, a3IPfwdSubnetBcast=a3IPfwdSubnetBcast, a3IPaddrConfigAddr=a3IPaddrConfigAddr, a3IParpReqFormat=a3IParpReqFormat, a3IPrarpClientCtl=a3IPrarpClientCtl, a3IPx25configTable=a3IPx25configTable, a3IParpConfigEntry=a3IParpConfigEntry, a3IPx25configProfID=a3IPx25configProfID, a3IPextRelaySrcRteCtl=a3IPextRelaySrcRteCtl, a3IPsmdsGa=a3IPsmdsGa, a3IPicmpGenTable=a3IPicmpGenTable, a3IPrarpServerCtl=a3IPrarpServerCtl, a3IPforwardExtEntry=a3IPforwardExtEntry, a3IPforwardExtDest=a3IPforwardExtDest, a3IPforwardExtPolicy=a3IPforwardExtPolicy, a3IPntmNetAddress=a3IPntmNetAddress, a3IParpProxyCtl=a3IParpProxyCtl, a3IPsmdsGaTable=a3IPsmdsGaTable, a3IPicmpGenRedirect=a3IPicmpGenRedirect, a3IPicmpGenEntry=a3IPicmpGenEntry, a3IPaddrConfigBcastAddr=a3IPaddrConfigBcastAddr, a3IPforwardExtOverride=a3IPforwardExtOverride, a3IPaddrConfigPort=a3IPaddrConfigPort, a3IPforwardExtProto=a3IPforwardExtProto, a3IParpRemAddr=a3IParpRemAddr, a3IPicmpMaskCtl=a3IPicmpMaskCtl, a3IPqueuePriority=a3IPqueuePriority, a3IPx25configEntry=a3IPx25configEntry, SMDSAddress=SMDSAddress, a3IPx25configQueueSize=a3IPx25configQueueSize, a3IPaddrConfigMtu=a3IPaddrConfigMtu, a3IPforwardExtTable=a3IPforwardExtTable, a3IPicmpInfoCtl=a3IPicmpInfoCtl, a3IPsmdsGaIpNet=a3IPsmdsGaIpNet, brouterMIB=brouterMIB, a3IPsmdsGaStatus=a3IPsmdsGaStatus, a3IPforwardExtNextHop=a3IPforwardExtNextHop, a3IPextFlushCtl=a3IPextFlushCtl, a3Com=a3Com, a3IParpHoldTime=a3IParpHoldTime, a3IPextSplitLoadCtl=a3IPextSplitLoadCtl, a3IPntmHdrFormat=a3IPntmHdrFormat, a3IPaddrConfigStatus=a3IPaddrConfigStatus, a3IParpOverBlocked=a3IParpOverBlocked, a3IPicmpGenTimeExceed=a3IPicmpGenTimeExceed, a3IPaddrConfigTable=a3IPaddrConfigTable, a3IParpInvCtl=a3IParpInvCtl, a3IPntmProxyArp=a3IPntmProxyArp, a3IPx25configPort=a3IPx25configPort, a3IPicmpGenDestUnreach=a3IPicmpGenDestUnreach, a3IPextMode=a3IPextMode, a3IParpConfigTable=a3IParpConfigTable, a3IPntmExtEntry=a3IPntmExtEntry, a3ComIPextns=a3ComIPextns, a3IPaddrConfigNetMask=a3IPaddrConfigNetMask, a3IParpPortIndex=a3IParpPortIndex, a3IPx25configVClimit=a3IPx25configVClimit)

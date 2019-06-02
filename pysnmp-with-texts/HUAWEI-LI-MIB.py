#
# PySNMP MIB module HUAWEI-LI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:46:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InetPortNumber, InetAddress, InetAddressPrefixLength, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressPrefixLength", "InetAddressType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Integer32, Bits, Unsigned32, TimeTicks, IpAddress, Counter64, Counter32, ModuleIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Bits", "Unsigned32", "TimeTicks", "IpAddress", "Counter64", "Counter32", "ModuleIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention, RowStatus, MacAddress, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "MacAddress", "DateAndTime")
hwLiMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131))
hwLiMib.setRevisions(('2007-06-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwLiMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: hwLiMib.setLastUpdated('200706270000Z')
if mibBuilder.loadTexts: hwLiMib.setOrganization('hw Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwLiMib.setContactInfo(' R&D Meaning, huawei Technologies co.,Ltd. Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwLiMib.setDescription("This module manages huawei's Lawful interception feature.")
class HWLiDscp(TextualConvention, Integer32):
    description = 'An integer that is in the range of the DiffServ codepoint values.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

hwLiMibNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 1))
hwLiMibActive = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 1, 1))
if mibBuilder.loadTexts: hwLiMibActive.setStatus('current')
if mibBuilder.loadTexts: hwLiMibActive.setDescription('This notification is sent when an intercepting router or switch is first capable of intercepting a packet corresponding to a configured data stream. ')
hwLiX3HeartBeatAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 1, 2)).setObjects(("HUAWEI-LI-MIB", "hwLiGatewayX3Address"))
if mibBuilder.loadTexts: hwLiX3HeartBeatAlarm.setStatus('current')
if mibBuilder.loadTexts: hwLiX3HeartBeatAlarm.setDescription('This notification is sent when an LIG is lost connection to the device which intercepting packet corresponding to a configured data stream. ')
hwLiX3HeartBeatRecover = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 1, 3)).setObjects(("HUAWEI-LI-MIB", "hwLiGatewayX3Address"))
if mibBuilder.loadTexts: hwLiX3HeartBeatRecover.setStatus('current')
if mibBuilder.loadTexts: hwLiX3HeartBeatRecover.setDescription('This notification is sent when an LIG is recover connection to the device which intercepting packet corresponding to a configured data stream. ')
hwLiMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2))
hwLiAgentObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1))
hwLiAgentTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLiAgentTime.setStatus('current')
if mibBuilder.loadTexts: hwLiAgentTime.setDescription('The time of the LI agent.Read-only.')
hwLiAgentEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLiAgentEnable.setStatus('current')
if mibBuilder.loadTexts: hwLiAgentEnable.setDescription('The status of the LI agent.Read-only.')
hwLiAgentX2IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLiAgentX2IpAddress.setStatus('current')
if mibBuilder.loadTexts: hwLiAgentX2IpAddress.setDescription('The IP address of the X2 interface in LI agent.Just can be read by server and can be set in command line.')
hwLiAgentX2Port = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 4), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLiAgentX2Port.setStatus('current')
if mibBuilder.loadTexts: hwLiAgentX2Port.setDescription('The Port of the X2 interface in LI agent.Just can be read by server and can be set in command line.')
hwLiAgentX3IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLiAgentX3IpAddress.setStatus('current')
if mibBuilder.loadTexts: hwLiAgentX3IpAddress.setDescription('The IP address of the X3 interface in LI agent.Just can be read by server and can be set in command line.')
hwLiAgentX3Port = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 6), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLiAgentX3Port.setStatus('current')
if mibBuilder.loadTexts: hwLiAgentX3Port.setDescription('The Port of the X3 interface in LI agent.Just can be read by server and can be set in command line.')
hwLiGatewayGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3))
hwLiGatewayNewIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLiGatewayNewIndex.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayNewIndex.setDescription('This object contains a value which may be used as an index value for a new HwLiGatewayEntry. This is to reduce the probability of errors during creation of new hwLiGatewayTable entries.0 means no free resource.')
hwLiGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2), )
if mibBuilder.loadTexts: hwLiGatewayTable.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayTable.setDescription('This table lists the LI Gateway Devices with which the intercepting device communicates. This table is written by the LI Gateway Device, and is always volatile. This is because intercepts may disappear during a restart of the intercepting equipment. Entries are added to this table via hwLiGatewayStatus in accordance with the RowStatus convention.')
hwLiGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1), ).setIndexNames((0, "HUAWEI-LI-MIB", "hwLiGatewayIndex"))
if mibBuilder.loadTexts: hwLiGatewayEntry.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayEntry.setDescription('The entry describes a single session maintained with an application on a LI Gateway Device.')
hwLiGatewayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: hwLiGatewayIndex.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayIndex.setDescription('The index of the LIG itself.')
hwLiGatewayAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayAddressType.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayAddressType.setDescription('The type of address in LIG')
hwLiGatewayX2Protocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("udp", 1), ("tcp", 2))).clone('tcp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX2Protocol.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX2Protocol.setDescription('The protocol used in transferring intercepted data to the Gateway Device. ')
hwLiGatewayX2Address = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX2Address.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX2Address.setDescription("The IP Address of the Gateway Device's network interface to which to direct IRI.")
hwLiGatewayX2Port = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 5), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX2Port.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX2Port.setDescription("The port number on the Gateway Device's network interface to which to direct IRI.")
hwLiGatewayX3Protocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("udp", 1), ("tcp", 2))).clone('udp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX3Protocol.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX3Protocol.setDescription('The protocol used in transferring intercepted data to the Gateway Device. ')
hwLiGatewayX3Address = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX3Address.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX3Address.setDescription("The IP Address of the Gateway Device's network interface to which to direct CC.")
hwLiGatewayX3Port = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 8), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX3Port.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX3Port.setDescription("The port number on the Gateway Device's network interface to which to direct intercepted traffic.")
hwLiGatewayX3HeartBeatTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX3HeartBeatTimer.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX3HeartBeatTimer.setDescription('The timer for sending HeartBeat to LIG,In seconds')
hwLiGatewayX3NoResponseNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 16)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX3NoResponseNum.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX3NoResponseNum.setDescription('The times of heartbeats that allowed to missed from LIG')
hwLiGatewayX3OperateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("noHeartBeat", 2), ("linkdown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLiGatewayX3OperateStatus.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX3OperateStatus.setDescription('The operate status of X3 interface')
hwLiGatewayX3Dscp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 12), HWLiDscp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX3Dscp.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX3Dscp.setDescription('The Differentiated Services Code Point the intercepting device applies to the IP packets encapsulating the intercepted traffic.')
hwLiGatewayRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayRowStatus.setDescription('The status of this conceptual row. This object is used to manage creation, modification and deletion of rows in this table. ')
hwLiGatewayX3AddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 15), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX3AddressType.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX3AddressType.setDescription('The type of address in LIG')
hwLiGatewayX2AddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 16), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiGatewayX2AddressType.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayX2AddressType.setDescription('The type of address in LIG')
hwLiGatewayCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 3), Bits().clone(namedValues=NamedValues(("ipv4SrcInterface", 0), ("ipv6SrcInterface", 1), ("udp", 2), ("tcp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLiGatewayCapabilities.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayCapabilities.setDescription('This object displays the device capabilities with respect to certain fields in Gateway Device table. This may be dependent on hardware capabilities, software capabilities. The following values may be supported: ipv4SrcInterface: SNMP ifIndex Value may be used to select the interface (denoted by hwLiGatewaySrcInterface) on the intercepting device from which to transmit intercepted data to an IPv4 address Gateway Device. ipv6SrcInterface: SNMP ifIndex Value may be used to select the interface (denoted by hwLiGatewaySrcInterface) on the intercepting device from which to transmit intercepted data to an IPv6 address Gateway Device. udp: UDP may be used as transport protocol (denoted by hwLiGatewayTransport) in transferring intercepted data to the Gateway Device. tcp: TCP may be used as transport protocol (denoted by hwLiGatewayTransport) in transferring intercepted data to the Gateway Device.')
hwLiStreamGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4))
hwLiStreamTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2), )
if mibBuilder.loadTexts: hwLiStreamTable.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamTable.setDescription('The Intercept Stream Table lists the IPv4 and IPv6 streams to be intercepted. The same data stream must be used by one LIG. The first index indicates which LIG the intercepted traffic will be diverted to. The second index permits multiple classifiers to be used together, such as having an IP address as source or destination.')
hwLiStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1), ).setIndexNames((0, "HUAWEI-LI-MIB", "hwLiGatewayIndex"), (0, "HUAWEI-LI-MIB", "hwLiStreamIndex"))
if mibBuilder.loadTexts: hwLiStreamEntry.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamEntry.setDescription('A stream entry indicates a single data stream to be intercepted to a Mediation Device. Many selected data streams may go to the same application interface, and many application interfaces are supported.')
hwLiStreamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192)))
if mibBuilder.loadTexts: hwLiStreamIndex.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamIndex.setDescription('The index of the stream itself.')
hwLiStreamLiId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamLiId.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamLiId.setDescription('The ID indicate a independency stream in a LIG .')
hwLiStreamActivationType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("iri", 1), ("cc", 2), ("both", 3))).clone('cc')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamActivationType.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamActivationType.setDescription('Intercepted IRI or CC or BOTH.')
hwLiStreamSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamSessionId.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamSessionId.setDescription('The index of the stream itself.0 means no session ID will be specified')
hwLiStreamTargetIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oneDirection", 1), ("biDirection", 2))).clone('biDirection')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamTargetIdType.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamTargetIdType.setDescription('Target ID type specifies the type of packets. 1 means one direction traffic is intercept, 2 means bidirectional traffic is intercept. for bidirectional interception, if the source IP or destination IP in a packet is equal with the configured hwLiStreamSrcIpAddress If other condition is satisfied then the packet is intercepted. for one-directional interception, if the sourceIP and DestinationIP in a packet is equal with the configured hwLiStreamSrcIpAddress and hwLiStreamDstIPAddressIf other condition is satisfied then the packet is intercepted')
hwLiStreamSrcMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 7), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamSrcMacAddress.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamSrcMacAddress.setDescription('Source Mac address of the packets which will be intercepted.0000-0000-0000 means no MAC address will be specified')
hwLiStreamDstMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 8), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamDstMacAddress.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamDstMacAddress.setDescription('Destination Mac address of the packets which will be intercepted.')
hwLiStreamSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 9), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamSrcIpAddress.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamSrcIpAddress.setDescription('The Source Address used in packet selection. This address will be of the type specified in hwLiStreamIpAddrType.0.0.0.0 means no IP address will be specified')
hwLiStreamSrcIpLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 10), InetAddressPrefixLength().clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamSrcIpLength.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamSrcIpLength.setDescription('The length of the Source Prefix. A value of 32 causes all addresses to match. This prefix length will be consistent with the type specified in hwLiStreamIpAddrType.')
hwLiStreamDstIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 11), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamDstIpAddress.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamDstIpAddress.setDescription('The Destination address or prefix used in packet selection. This address will be of the type specified in hwLiStreamIpAddrType.0.0.0.0 means no IP address will be specified')
hwLiStreamDstIpLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 12), InetAddressPrefixLength().clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamDstIpLength.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamDstIpLength.setDescription('The length of the Destination Prefix. A value of 32 causes all addresses to match. This prefix length will be consistent with the type specified in hwLiStreamIpAddrType.')
hwLiStreamProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamProtocol.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamProtocol.setDescription('Protocol type of the packets which will be intercepted.0 means no Protocol type will be specified')
hwLiStreamSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 14), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamSrcPort.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamSrcPort.setDescription('The fourth layer source port.0 means no Port will be specified')
hwLiStreamDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 15), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamDstPort.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamDstPort.setDescription('The fourth layer Destination port.0 means no Port will be specified')
hwLiStreamIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamIfIndex.setDescription('The interface switch carrying the intercepted taffic.0 means no interface will be specified')
hwLiStreamUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 17), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamUserName.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamUserName.setDescription('The username whose traffic will be intercepted.zero-length means no user will be specified')
hwLiStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamRowStatus.setDescription('The status of this conceptual row. This object is used to manage creation, modification and deletion of rows in this table.')
hwLiStreamSrcIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 19), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamSrcIpAddressType.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamSrcIpAddressType.setDescription('The source IP address of the interception stream')
hwLiStreamDstIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 20), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamDstIpAddressType.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamDstIpAddressType.setDescription('The destination IP address of the interception stream')
hwLiStreamSrcVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 21), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamSrcVpnName.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamSrcVpnName.setDescription('The source VPN instance name whose traffic will be intercepted.zero-length means no VPN will be specified')
hwLiStreamDstVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 22), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamDstVpnName.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamDstVpnName.setDescription('The destination VPN instance name whose traffic will be intercepted. zero-length means no VPN will be specified')
hwLiStreamL2tpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamL2tpIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamL2tpIfIndex.setDescription('The L2TP ifindex of intercepting stream.0 means no l2tpIfindex will be specified')
hwLiStreamL2tpVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamL2tpVlanId.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamL2tpVlanId.setDescription('The L2TP VLAN ID of intercepting stream.0 means no Vlan will be specified')
hwLiStreamAcctSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 25), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLiStreamAcctSessionId.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamAcctSessionId.setDescription('The accounting session ID of intercepting stream.zero-length means no accouting session ID will be specified')
hwLiMibConform = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3))
hwLiMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 2))
hwLiMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 2, 1)).setObjects(("HUAWEI-LI-MIB", "hwLiGatewayComplianceGroup"), ("HUAWEI-LI-MIB", "hwLiStreamComplianceGroup"), ("HUAWEI-LI-MIB", "hwLiNotificationGroup"), ("HUAWEI-LI-MIB", "hwLiGatewayCpbComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLiMibCompliance = hwLiMibCompliance.setStatus('current')
if mibBuilder.loadTexts: hwLiMibCompliance.setDescription('Description.')
hwLiMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3))
hwLiAgentComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 1)).setObjects(("HUAWEI-LI-MIB", "hwLiAgentTime"), ("HUAWEI-LI-MIB", "hwLiAgentEnable"), ("HUAWEI-LI-MIB", "hwLiAgentX2IpAddress"), ("HUAWEI-LI-MIB", "hwLiAgentX2Port"), ("HUAWEI-LI-MIB", "hwLiAgentX3IpAddress"), ("HUAWEI-LI-MIB", "hwLiAgentX3Port"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLiAgentComplianceGroup = hwLiAgentComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: hwLiAgentComplianceGroup.setDescription('Description.')
hwLiGatewayComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 2)).setObjects(("HUAWEI-LI-MIB", "hwLiGatewayNewIndex"), ("HUAWEI-LI-MIB", "hwLiGatewayAddressType"), ("HUAWEI-LI-MIB", "hwLiGatewayX2Protocol"), ("HUAWEI-LI-MIB", "hwLiGatewayX2Address"), ("HUAWEI-LI-MIB", "hwLiGatewayX2Port"), ("HUAWEI-LI-MIB", "hwLiGatewayX3Protocol"), ("HUAWEI-LI-MIB", "hwLiGatewayX3Address"), ("HUAWEI-LI-MIB", "hwLiGatewayX3Port"), ("HUAWEI-LI-MIB", "hwLiGatewayX3HeartBeatTimer"), ("HUAWEI-LI-MIB", "hwLiGatewayX3NoResponseNum"), ("HUAWEI-LI-MIB", "hwLiGatewayX3OperateStatus"), ("HUAWEI-LI-MIB", "hwLiGatewayX3Dscp"), ("HUAWEI-LI-MIB", "hwLiGatewayRowStatus"), ("HUAWEI-LI-MIB", "hwLiGatewayX3AddressType"), ("HUAWEI-LI-MIB", "hwLiGatewayX2AddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLiGatewayComplianceGroup = hwLiGatewayComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayComplianceGroup.setDescription('Description.')
hwLiStreamComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 3)).setObjects(("HUAWEI-LI-MIB", "hwLiStreamLiId"), ("HUAWEI-LI-MIB", "hwLiStreamActivationType"), ("HUAWEI-LI-MIB", "hwLiStreamSessionId"), ("HUAWEI-LI-MIB", "hwLiStreamTargetIdType"), ("HUAWEI-LI-MIB", "hwLiStreamProtocol"), ("HUAWEI-LI-MIB", "hwLiStreamSrcPort"), ("HUAWEI-LI-MIB", "hwLiStreamDstPort"), ("HUAWEI-LI-MIB", "hwLiStreamSrcMacAddress"), ("HUAWEI-LI-MIB", "hwLiStreamDstMacAddress"), ("HUAWEI-LI-MIB", "hwLiStreamSrcIpAddress"), ("HUAWEI-LI-MIB", "hwLiStreamSrcIpLength"), ("HUAWEI-LI-MIB", "hwLiStreamDstIpAddress"), ("HUAWEI-LI-MIB", "hwLiStreamDstIpLength"), ("HUAWEI-LI-MIB", "hwLiStreamIfIndex"), ("HUAWEI-LI-MIB", "hwLiStreamUserName"), ("HUAWEI-LI-MIB", "hwLiStreamRowStatus"), ("HUAWEI-LI-MIB", "hwLiStreamSrcIpAddressType"), ("HUAWEI-LI-MIB", "hwLiStreamDstIpAddressType"), ("HUAWEI-LI-MIB", "hwLiStreamSrcVpnName"), ("HUAWEI-LI-MIB", "hwLiStreamDstVpnName"), ("HUAWEI-LI-MIB", "hwLiStreamL2tpIfIndex"), ("HUAWEI-LI-MIB", "hwLiStreamL2tpVlanId"), ("HUAWEI-LI-MIB", "hwLiStreamAcctSessionId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLiStreamComplianceGroup = hwLiStreamComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: hwLiStreamComplianceGroup.setDescription('Description.')
hwLiNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 4)).setObjects(("HUAWEI-LI-MIB", "hwLiMibActive"), ("HUAWEI-LI-MIB", "hwLiX3HeartBeatAlarm"), ("HUAWEI-LI-MIB", "hwLiX3HeartBeatRecover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLiNotificationGroup = hwLiNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwLiNotificationGroup.setDescription('Description.')
hwLiGatewayCpbComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 5)).setObjects(("HUAWEI-LI-MIB", "hwLiGatewayCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLiGatewayCpbComplianceGroup = hwLiGatewayCpbComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: hwLiGatewayCpbComplianceGroup.setDescription('Description.')
mibBuilder.exportSymbols("HUAWEI-LI-MIB", hwLiGatewayGroup=hwLiGatewayGroup, hwLiGatewayTable=hwLiGatewayTable, hwLiAgentTime=hwLiAgentTime, hwLiX3HeartBeatAlarm=hwLiX3HeartBeatAlarm, hwLiStreamTable=hwLiStreamTable, hwLiStreamAcctSessionId=hwLiStreamAcctSessionId, hwLiStreamL2tpIfIndex=hwLiStreamL2tpIfIndex, hwLiMibActive=hwLiMibActive, hwLiGatewayX3NoResponseNum=hwLiGatewayX3NoResponseNum, hwLiGatewayX2Address=hwLiGatewayX2Address, hwLiStreamComplianceGroup=hwLiStreamComplianceGroup, hwLiStreamDstVpnName=hwLiStreamDstVpnName, hwLiGatewayX3AddressType=hwLiGatewayX3AddressType, hwLiGatewayX3Address=hwLiGatewayX3Address, hwLiAgentX2IpAddress=hwLiAgentX2IpAddress, hwLiGatewayX2Port=hwLiGatewayX2Port, hwLiMibObjects=hwLiMibObjects, hwLiGatewayNewIndex=hwLiGatewayNewIndex, hwLiGatewayX3Dscp=hwLiGatewayX3Dscp, hwLiStreamIndex=hwLiStreamIndex, hwLiStreamDstIpAddress=hwLiStreamDstIpAddress, hwLiStreamL2tpVlanId=hwLiStreamL2tpVlanId, hwLiAgentEnable=hwLiAgentEnable, hwLiStreamIfIndex=hwLiStreamIfIndex, hwLiStreamDstIpAddressType=hwLiStreamDstIpAddressType, hwLiMibCompliances=hwLiMibCompliances, hwLiGatewayCpbComplianceGroup=hwLiGatewayCpbComplianceGroup, hwLiStreamDstMacAddress=hwLiStreamDstMacAddress, hwLiAgentObjects=hwLiAgentObjects, hwLiGatewayX3Protocol=hwLiGatewayX3Protocol, PYSNMP_MODULE_ID=hwLiMib, hwLiStreamSrcMacAddress=hwLiStreamSrcMacAddress, hwLiAgentX2Port=hwLiAgentX2Port, hwLiStreamRowStatus=hwLiStreamRowStatus, hwLiStreamSrcIpAddressType=hwLiStreamSrcIpAddressType, hwLiMibGroups=hwLiMibGroups, hwLiMib=hwLiMib, hwLiX3HeartBeatRecover=hwLiX3HeartBeatRecover, hwLiGatewayRowStatus=hwLiGatewayRowStatus, hwLiStreamGroup=hwLiStreamGroup, hwLiAgentX3IpAddress=hwLiAgentX3IpAddress, hwLiStreamProtocol=hwLiStreamProtocol, hwLiStreamSrcIpLength=hwLiStreamSrcIpLength, hwLiGatewayX2AddressType=hwLiGatewayX2AddressType, hwLiStreamLiId=hwLiStreamLiId, hwLiStreamSessionId=hwLiStreamSessionId, hwLiGatewayAddressType=hwLiGatewayAddressType, hwLiGatewayCapabilities=hwLiGatewayCapabilities, hwLiGatewayIndex=hwLiGatewayIndex, hwLiAgentX3Port=hwLiAgentX3Port, hwLiStreamSrcIpAddress=hwLiStreamSrcIpAddress, hwLiGatewayComplianceGroup=hwLiGatewayComplianceGroup, hwLiStreamSrcVpnName=hwLiStreamSrcVpnName, hwLiStreamTargetIdType=hwLiStreamTargetIdType, hwLiMibNotifs=hwLiMibNotifs, hwLiStreamEntry=hwLiStreamEntry, hwLiAgentComplianceGroup=hwLiAgentComplianceGroup, hwLiGatewayEntry=hwLiGatewayEntry, hwLiStreamDstIpLength=hwLiStreamDstIpLength, hwLiStreamUserName=hwLiStreamUserName, hwLiStreamActivationType=hwLiStreamActivationType, hwLiMibCompliance=hwLiMibCompliance, hwLiGatewayX2Protocol=hwLiGatewayX2Protocol, hwLiStreamSrcPort=hwLiStreamSrcPort, hwLiGatewayX3Port=hwLiGatewayX3Port, hwLiNotificationGroup=hwLiNotificationGroup, hwLiMibConform=hwLiMibConform, HWLiDscp=HWLiDscp, hwLiGatewayX3OperateStatus=hwLiGatewayX3OperateStatus, hwLiStreamDstPort=hwLiStreamDstPort, hwLiGatewayX3HeartBeatTimer=hwLiGatewayX3HeartBeatTimer)
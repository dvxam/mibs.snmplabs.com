#
# PySNMP MIB module UDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:51:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, Unsigned32, Counter64, mib_2, Counter32, Bits, TimeTicks, NotificationType, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Unsigned32", "Counter64", "mib-2", "Counter32", "Bits", "TimeTicks", "NotificationType", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
udpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 50))
udpMIB.setRevisions(('2005-05-20 00:00', '1994-11-01 00:00', '1991-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: udpMIB.setRevisionsDescriptions(('IP version neutral revision, incorporating the following revisions: - Added udpHCInDatagrams and udpHCOutDatagrams in order to provide high-capacity counters for fast networks. - Added text to the descriptions of all counter objects to indicate how discontinuities are detected. - Deprecated the IPv4-specific udpTable and replaced it with the version neutral udpEndpointTable. This table includes support for connected UDP endpoints and support for identification of the operating system process associated with a UDP endpoint. - Deprecated the udpGroup and replaced it with object groups representing the current set of objects. - Deprecated udpMIBCompliance and replaced it with udpMIBCompliance2, which includes the compliance information for the new object groups. This version published as RFC 4113.', 'Initial SMIv2 version, published as RFC 2013.', 'The initial revision of this MIB module was part of MIB-II, published as RFC 1213.',))
if mibBuilder.loadTexts: udpMIB.setLastUpdated('200505200000Z')
if mibBuilder.loadTexts: udpMIB.setOrganization('IETF IPv6 Working Group http://www.ietf.org/html.charters/ipv6-charter.html')
if mibBuilder.loadTexts: udpMIB.setContactInfo('Bill Fenner (editor) AT&T Labs -- Research 75 Willow Rd. Menlo Park, CA 94025 Phone: +1 650 330-7893 Email: <fenner@research.att.com> John Flick (editor) Hewlett-Packard Company 8000 Foothills Blvd. M/S 5557 Roseville, CA 95747 Phone: +1 916 785 4018 Email: <john.flick@hp.com> Send comments to <ipv6@ietf.org>')
if mibBuilder.loadTexts: udpMIB.setDescription('The MIB module for managing UDP implementations. Copyright (C) The Internet Society (2005). This version of this MIB module is part of RFC 4113; see the RFC itself for full legal notices.')
udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
udpInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInDatagrams.setStatus('current')
if mibBuilder.loadTexts: udpInDatagrams.setDescription('The total number of UDP datagrams delivered to UDP users. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.')
udpNoPorts = MibScalar((1, 3, 6, 1, 2, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpNoPorts.setStatus('current')
if mibBuilder.loadTexts: udpNoPorts.setDescription('The total number of received UDP datagrams for which there was no application at the destination port. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.')
udpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInErrors.setStatus('current')
if mibBuilder.loadTexts: udpInErrors.setDescription('The number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.')
udpOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpOutDatagrams.setStatus('current')
if mibBuilder.loadTexts: udpOutDatagrams.setDescription('The total number of UDP datagrams sent from this entity. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.')
udpHCInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpHCInDatagrams.setStatus('current')
if mibBuilder.loadTexts: udpHCInDatagrams.setDescription('The total number of UDP datagrams delivered to UDP users, for devices that can receive more than 1 million UDP datagrams per second. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.')
udpHCOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpHCOutDatagrams.setStatus('current')
if mibBuilder.loadTexts: udpHCOutDatagrams.setDescription('The total number of UDP datagrams sent from this entity, for devices that can transmit more than 1 million UDP datagrams per second. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.')
udpEndpointTable = MibTable((1, 3, 6, 1, 2, 1, 7, 7), )
if mibBuilder.loadTexts: udpEndpointTable.setStatus('current')
if mibBuilder.loadTexts: udpEndpointTable.setDescription("A table containing information about this entity's UDP endpoints on which a local application is currently accepting or sending datagrams. The address type in this table represents the address type used for the communication, irrespective of the higher-layer abstraction. For example, an application using IPv6 'sockets' to communicate via IPv4 between ::ffff:10.0.0.1 and ::ffff:10.0.0.2 would use InetAddressType ipv4(1). Unlike the udpTable in RFC 2013, this table also allows the representation of an application that completely specifies both local and remote addresses and ports. A listening application is represented in three possible ways: 1) An application that is willing to accept both IPv4 and IPv6 datagrams is represented by a udpEndpointLocalAddressType of unknown(0) and a udpEndpointLocalAddress of ''h (a zero-length octet-string). 2) An application that is willing to accept only IPv4 or only IPv6 datagrams is represented by a udpEndpointLocalAddressType of the appropriate address type and a udpEndpointLocalAddress of '0.0.0.0' or '::' respectively. 3) An application that is listening for datagrams only for a specific IP address but from any remote system is represented by a udpEndpointLocalAddressType of the appropriate address type, with udpEndpointLocalAddress specifying the local address. In all cases where the remote is a wildcard, the udpEndpointRemoteAddressType is unknown(0), the udpEndpointRemoteAddress is ''h (a zero-length octet-string), and the udpEndpointRemotePort is 0. If the operating system is demultiplexing UDP packets by remote address and port, or if the application has 'connected' the socket specifying a default remote address and port, the udpEndpointRemote* values should be used to reflect this.")
udpEndpointEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 7, 1), ).setIndexNames((0, "UDP-MIB", "udpEndpointLocalAddressType"), (0, "UDP-MIB", "udpEndpointLocalAddress"), (0, "UDP-MIB", "udpEndpointLocalPort"), (0, "UDP-MIB", "udpEndpointRemoteAddressType"), (0, "UDP-MIB", "udpEndpointRemoteAddress"), (0, "UDP-MIB", "udpEndpointRemotePort"), (0, "UDP-MIB", "udpEndpointInstance"))
if mibBuilder.loadTexts: udpEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: udpEndpointEntry.setDescription('Information about a particular current UDP endpoint. Implementers need to be aware that if the total number of elements (octets or sub-identifiers) in udpEndpointLocalAddress and udpEndpointRemoteAddress exceeds 111, then OIDs of column instances in this table will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.')
udpEndpointLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 1), InetAddressType())
if mibBuilder.loadTexts: udpEndpointLocalAddressType.setStatus('current')
if mibBuilder.loadTexts: udpEndpointLocalAddressType.setDescription('The address type of udpEndpointLocalAddress. Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all local IP addresses are accepted.')
udpEndpointLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 2), InetAddress())
if mibBuilder.loadTexts: udpEndpointLocalAddress.setStatus('current')
if mibBuilder.loadTexts: udpEndpointLocalAddress.setDescription("The local IP address for this UDP endpoint. The value of this object can be represented in three possible ways, depending on the characteristics of the listening application: 1. For an application that is willing to accept both IPv4 and IPv6 datagrams, the value of this object must be ''h (a zero-length octet-string), with the value of the corresponding instance of the udpEndpointLocalAddressType object being unknown(0). 2. For an application that is willing to accept only IPv4 or only IPv6 datagrams, the value of this object must be '0.0.0.0' or '::', respectively, while the corresponding instance of the udpEndpointLocalAddressType object represents the appropriate address type. 3. For an application that is listening for data destined only to a specific IP address, the value of this object is the specific IP address for which this node is receiving packets, with the corresponding instance of the udpEndpointLocalAddressType object representing the appropriate address type. As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
udpEndpointLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: udpEndpointLocalPort.setStatus('current')
if mibBuilder.loadTexts: udpEndpointLocalPort.setDescription('The local port number for this UDP endpoint.')
udpEndpointRemoteAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 4), InetAddressType())
if mibBuilder.loadTexts: udpEndpointRemoteAddressType.setStatus('current')
if mibBuilder.loadTexts: udpEndpointRemoteAddressType.setDescription('The address type of udpEndpointRemoteAddress. Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all remote IP addresses are accepted. Also, note that some combinations of udpEndpointLocalAdressType and udpEndpointRemoteAddressType are not supported. In particular, if the value of this object is not unknown(0), it is expected to always refer to the same IP version as udpEndpointLocalAddressType.')
udpEndpointRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 5), InetAddress())
if mibBuilder.loadTexts: udpEndpointRemoteAddress.setStatus('current')
if mibBuilder.loadTexts: udpEndpointRemoteAddress.setDescription("The remote IP address for this UDP endpoint. If datagrams from any remote system are to be accepted, this value is ''h (a zero-length octet-string). Otherwise, it has the type described by udpEndpointRemoteAddressType and is the address of the remote system from which datagrams are to be accepted (or to which all datagrams will be sent). As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
udpEndpointRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 6), InetPortNumber())
if mibBuilder.loadTexts: udpEndpointRemotePort.setStatus('current')
if mibBuilder.loadTexts: udpEndpointRemotePort.setDescription('The remote port number for this UDP endpoint. If datagrams from any remote system are to be accepted, this value is zero.')
udpEndpointInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: udpEndpointInstance.setStatus('current')
if mibBuilder.loadTexts: udpEndpointInstance.setDescription("The instance of this tuple. This object is used to distinguish among multiple processes 'connected' to the same UDP endpoint. For example, on a system implementing the BSD sockets interface, this would be used to support the SO_REUSEADDR and SO_REUSEPORT socket options.")
udpEndpointProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpEndpointProcess.setStatus('current')
if mibBuilder.loadTexts: udpEndpointProcess.setDescription("The system's process ID for the process associated with this endpoint, or zero if there is no such process. This value is expected to be the same as HOST-RESOURCES-MIB::hrSWRunIndex or SYSAPPL-MIB:: sysApplElmtRunIndex for some row in the appropriate tables.")
udpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 5), )
if mibBuilder.loadTexts: udpTable.setStatus('deprecated')
if mibBuilder.loadTexts: udpTable.setDescription('A table containing IPv4-specific UDP listener information. It contains information about all local IPv4 UDP end-points on which an application is currently accepting datagrams. This table has been deprecated in favor of the version neutral udpEndpointTable.')
udpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 5, 1), ).setIndexNames((0, "UDP-MIB", "udpLocalAddress"), (0, "UDP-MIB", "udpLocalPort"))
if mibBuilder.loadTexts: udpEntry.setStatus('deprecated')
if mibBuilder.loadTexts: udpEntry.setDescription('Information about a particular current UDP listener.')
udpLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpLocalAddress.setStatus('deprecated')
if mibBuilder.loadTexts: udpLocalAddress.setDescription('The local IP address for this UDP listener. In the case of a UDP listener that is willing to accept datagrams for any IP interface associated with the node, the value 0.0.0.0 is used.')
udpLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpLocalPort.setStatus('deprecated')
if mibBuilder.loadTexts: udpLocalPort.setDescription('The local port number for this UDP listener.')
udpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2))
udpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2, 1))
udpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2, 2))
udpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 50, 2, 1, 2)).setObjects(("UDP-MIB", "udpBaseGroup"), ("UDP-MIB", "udpEndpointGroup"), ("UDP-MIB", "udpHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpMIBCompliance2 = udpMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: udpMIBCompliance2.setDescription('The compliance statement for systems that implement UDP. There are a number of INDEX objects that cannot be represented in the form of OBJECT clauses in SMIv2, but for which we have the following compliance requirements, expressed in OBJECT clause form in this description clause: -- OBJECT udpEndpointLocalAddressType -- SYNTAX InetAddressType { unknown(0), ipv4(1), -- ipv6(2), ipv4z(3), -- ipv6z(4) } -- DESCRIPTION -- Support for dns(5) is not required. -- OBJECT udpEndpointLocalAddress -- SYNTAX InetAddress (SIZE(0|4|8|16|20)) -- DESCRIPTION -- Support is only required for zero-length -- octet-strings, and for scoped and unscoped -- IPv4 and IPv6 addresses. -- OBJECT udpEndpointRemoteAddressType -- SYNTAX InetAddressType { unknown(0), ipv4(1), -- ipv6(2), ipv4z(3), -- ipv6z(4) } -- DESCRIPTION -- Support for dns(5) is not required. -- OBJECT udpEndpointRemoteAddress -- SYNTAX InetAddress (SIZE(0|4|8|16|20)) -- DESCRIPTION -- Support is only required for zero-length -- octet-strings, and for scoped and unscoped -- IPv4 and IPv6 addresses. ')
udpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 50, 2, 1, 1)).setObjects(("UDP-MIB", "udpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpMIBCompliance = udpMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: udpMIBCompliance.setDescription('The compliance statement for IPv4-only systems that implement UDP. For IP version independence, this compliance statement is deprecated in favor of udpMIBCompliance2. However, agents are still encouraged to implement these objects in order to interoperate with the deployed base of managers.')
udpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 1)).setObjects(("UDP-MIB", "udpInDatagrams"), ("UDP-MIB", "udpNoPorts"), ("UDP-MIB", "udpInErrors"), ("UDP-MIB", "udpOutDatagrams"), ("UDP-MIB", "udpLocalAddress"), ("UDP-MIB", "udpLocalPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpGroup = udpGroup.setStatus('deprecated')
if mibBuilder.loadTexts: udpGroup.setDescription('The deprecated group of objects providing for management of UDP over IPv4.')
udpBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 2)).setObjects(("UDP-MIB", "udpInDatagrams"), ("UDP-MIB", "udpNoPorts"), ("UDP-MIB", "udpInErrors"), ("UDP-MIB", "udpOutDatagrams"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpBaseGroup = udpBaseGroup.setStatus('current')
if mibBuilder.loadTexts: udpBaseGroup.setDescription('The group of objects providing for counters of UDP statistics.')
udpHCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 3)).setObjects(("UDP-MIB", "udpHCInDatagrams"), ("UDP-MIB", "udpHCOutDatagrams"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpHCGroup = udpHCGroup.setStatus('current')
if mibBuilder.loadTexts: udpHCGroup.setDescription('The group of objects providing for counters of high speed UDP implementations.')
udpEndpointGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 4)).setObjects(("UDP-MIB", "udpEndpointProcess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpEndpointGroup = udpEndpointGroup.setStatus('current')
if mibBuilder.loadTexts: udpEndpointGroup.setDescription("The group of objects providing for the IP version independent management of UDP 'endpoints'.")
mibBuilder.exportSymbols("UDP-MIB", udpMIBCompliances=udpMIBCompliances, udpLocalAddress=udpLocalAddress, udpEndpointInstance=udpEndpointInstance, udpInErrors=udpInErrors, udpEndpointLocalPort=udpEndpointLocalPort, udpTable=udpTable, udpMIBGroups=udpMIBGroups, udpEndpointRemotePort=udpEndpointRemotePort, udpEntry=udpEntry, udpEndpointGroup=udpEndpointGroup, udpLocalPort=udpLocalPort, udpMIB=udpMIB, udpHCInDatagrams=udpHCInDatagrams, udpMIBConformance=udpMIBConformance, udpEndpointTable=udpEndpointTable, PYSNMP_MODULE_ID=udpMIB, udpEndpointRemoteAddressType=udpEndpointRemoteAddressType, udpEndpointProcess=udpEndpointProcess, udpHCOutDatagrams=udpHCOutDatagrams, udpNoPorts=udpNoPorts, udpEndpointRemoteAddress=udpEndpointRemoteAddress, udpEndpointLocalAddressType=udpEndpointLocalAddressType, udpHCGroup=udpHCGroup, udpInDatagrams=udpInDatagrams, udpEndpointEntry=udpEndpointEntry, udpBaseGroup=udpBaseGroup, udpOutDatagrams=udpOutDatagrams, udpMIBCompliance2=udpMIBCompliance2, udpMIBCompliance=udpMIBCompliance, udpEndpointLocalAddress=udpEndpointLocalAddress, udpGroup=udpGroup, udp=udp)

#
# PySNMP MIB module WATCHGUARD-IPSEC-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WATCHGUARD-IPSEC-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:36:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Counter64, ModuleIdentity, ObjectIdentity, Integer32, TimeTicks, iso, Gauge32, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Counter64", "ModuleIdentity", "ObjectIdentity", "Integer32", "TimeTicks", "iso", "Gauge32", "Unsigned32", "enterprises")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-MIB", "watchguard")
wgInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 6))
wgInfoModule.setRevisions(('2007-01-25 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wgInfoModule.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: wgInfoModule.setLastUpdated('200701251200Z')
if mibBuilder.loadTexts: wgInfoModule.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: wgInfoModule.setContactInfo(' Ella Yu WatchGuard Technologies, Inc. 1841 Zanker Road San Jose, CA 95112 USA 408-519-4888 ella.yu@watchguard.com ')
if mibBuilder.loadTexts: wgInfoModule.setDescription('The MIB module describes various tunnel objects of WatchGuard system.')
wgIpsecTunnelMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 6, 5))
if mibBuilder.loadTexts: wgIpsecTunnelMIB.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelMIB.setDescription('This is the base object identifier for all tunnel branches.')
wgIpsecTunnel = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1))
if mibBuilder.loadTexts: wgIpsecTunnel.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnel.setDescription('This is the base object identifier for all tunnel information.')
wgIpsecTunnelNum = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelNum.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelNum.setDescription('The total number of entries in the wgIpsecTunnelTable. ')
wgIpsecTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2), )
if mibBuilder.loadTexts: wgIpsecTunnelTable.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelTable.setDescription('This is the connection table describing all current tunnels exist on this entity.')
wgIpsecTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1), ).setIndexNames((0, "WATCHGUARD-IPSEC-TUNNEL-MIB", "wgIpsecTunnelID"))
if mibBuilder.loadTexts: wgIpsecTunnelEntry.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelEntry.setDescription('An entry (conceptual row) containing the information on a tunnel between two security gateways.')
wgIpsecTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelID.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelID.setDescription('The running index of this tunnel.')
wgIpsecTunnelLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelLocalAddr.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelLocalAddr.setDescription('The local IP address of the current tunnel.')
wgIpsecTunnelPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelPeerAddr.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelPeerAddr.setDescription('The remote IP address of the current tunnel.')
wgIpsecTunnelInSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelInSpi.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelInSpi.setDescription("The security parameters index of inbound SA's within this tunnel.")
wgIpsecTunnelOutSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelOutSpi.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelOutSpi.setDescription("The security parameters index of outbound SA's within this tunnel.")
wgIpsecTunnelCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelCreateTime.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelCreateTime.setDescription('The date and time when the tunnel is created.')
wgIpsecTunnelDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelDeviceID.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelDeviceID.setDescription('The identifier of target device where the SA resides.')
wgIpsecTunnelEspEncryptAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("des", 2), ("three-des", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelEspEncryptAlg.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelEspEncryptAlg.setDescription("The encryption algorithm used in the tunnel. It's 0 if ESP is not used.")
wgIpsecTunnelEspAuthAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("md5", 2), ("sha", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelEspAuthAlg.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelEspAuthAlg.setDescription("The authentication algorithm used in the tunnel. It's 0 if ESP is not used.")
wgIpsecTunnelAhAuthAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("md5", 2), ("sha", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelAhAuthAlg.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelAhAuthAlg.setDescription("The AH authentication algorithm used in the tunnel. It's 0 if AH is not used.")
wgIpsecTunnelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("tunnel", 1), ("transport", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelMode.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelMode.setDescription('The tunnel/transport mode of the tunnel.')
wgIpsecTunnelKeyMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("manual", 1), ("auto-ike", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelKeyMode.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelKeyMode.setDescription('The key mode of the tunnel.')
wgIpsecTunnelLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelLifeTime.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelLifeTime.setDescription('The life time (in hundredths of a second) of the tunnel.')
wgIpsecTunnelLifeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelLifeLength.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelLifeLength.setDescription('The maximum traffic in bytes that the tunnel is allowed to support.')
wgIpsecTunnelInSaBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelInSaBytes.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelInSaBytes.setDescription('Current active inbound SA bytes of the tunnel.')
wgIpsecTunnelOutSaBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelOutSaBytes.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelOutSaBytes.setDescription('Current active outbound SA bytes of the tunnel.')
wgIpsecTunnelAccSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelAccSecs.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelAccSecs.setDescription('The number of seconds that the tunnel has existed.')
wgIpsecTunnelSelectorProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 6, 8, 12, 17, 22, 29, 41, 43, 44, 46, 47, 50, 51, 58, 59, 60, 92, 98, 103, 255))).clone(namedValues=NamedValues(("any", 0), ("icmp", 1), ("igmp", 2), ("ipip", 4), ("tcp", 6), ("egp", 8), ("pup", 12), ("udp", 17), ("idp", 22), ("tp", 29), ("ipv6", 41), ("ipv6-routing", 43), ("ipv6-fragmentation", 44), ("rsvp", 46), ("gre", 47), ("esp", 50), ("ah", 51), ("icmpv6", 58), ("none", 59), ("dstopts", 60), ("mtp", 92), ("encap", 98), ("pim", 103), ("raw", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelSelectorProtocol.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelSelectorProtocol.setDescription('The ip protocol number that this SA selector carries, or 0 if it carries any protocol.')
wgIpsecTunnelSelectorRemoteIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ip-addr-single", 1), ("ip-addr-subnet", 2), ("ip-addr-range", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelSelectorRemoteIPType.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelSelectorRemoteIPType.setDescription('The type of remote IP address of the SA selector in the entity.')
wgIpsecTunnelSelectorRemoteIPOne = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 20), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelSelectorRemoteIPOne.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelSelectorRemoteIPOne.setDescription("The first remote IP address of the SA selector in the entity. It's IP address if remote IP of this selector only has one address. It's IP address of subnet if the remote IP of this selector is IP subnet. It's the start IP address if the remote IP of this selector has a range of addresses.")
wgIpsecTunnelSelectorRemoteIPTwo = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 21), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelSelectorRemoteIPTwo.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelSelectorRemoteIPTwo.setDescription("The second remote IP address of the SA selector in the entity. It's 0 if remote IP of this selector only has one address. It's netmask of subnet if the remote IP of this selector is IP subnet. It's the end IP address if the remote IP of this selector has a range of addresses.")
wgIpsecTunnelSelectorRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelSelectorRemotePort.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelSelectorRemotePort.setDescription('The remote port used by this selector in the entity.')
wgIpsecTunnelSelectorLocalIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ip-addr-single", 1), ("ip-addr-subnet", 2), ("ip-addr-range", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelSelectorLocalIPType.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelSelectorLocalIPType.setDescription('The type of local IP address of the SA selector in the entity.')
wgIpsecTunnelSelectorLocalIPOne = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 24), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelSelectorLocalIPOne.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelSelectorLocalIPOne.setDescription("The first local IP address of the SA selector in the entity. It's IP address if local IP of this selector only has one address. It's IP address of subnet if the local IP of this selector is IP subnet. It's the start IP address if the local IP of this selector has a range of IP addresses.")
wgIpsecTunnelSelectorLocalIPTwo = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 25), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelSelectorLocalIPTwo.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelSelectorLocalIPTwo.setDescription("The second local IP address of the SA selector in the entity. It's 0 if local IP of this selector only has one address. It's netmask of subnet if the local IP of this selector is IP subnet. It's the end IP address if the local IP of this selector has a range of IP addresses.")
wgIpsecTunnelSelectorLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelSelectorLocalPort.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelSelectorLocalPort.setDescription('The local port used by this selector in the entity.')
wgIpsecTunnelNumRekey = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelNumRekey.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelNumRekey.setDescription('The number of rekeys of the tunnel.')
wgIpsecTunnelInKbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 28), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelInKbytes.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelInKbytes.setDescription('Total inbound traffic in Kbytes since the establish of this tunnel.')
wgIpsecTunnelOutKbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 29), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelOutKbytes.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelOutKbytes.setDescription('Total outound traffic in Kbytes since the establish of this connection.')
wgIpsecTunnelInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelInPackets.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelInPackets.setDescription('Total number of inbound packets since the establish of this connection.')
wgIpsecTunnelOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelOutPackets.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelOutPackets.setDescription('Total number of outound packets since the establish of this connection.')
wgIpsecTunnelInDecryptErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelInDecryptErrors.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelInDecryptErrors.setDescription('Total number of packets discarded due to decryption error since the establish of this connection.')
wgIpsecTunnelInAuthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelInAuthErrors.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelInAuthErrors.setDescription('Total number of packets discarded due to authentication error since the establish of this connection.')
wgIpsecTunnelInReplayErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelInReplayErrors.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelInReplayErrors.setDescription('Total number of packets discarded due to replay error since the establish of this connection.')
wgIpsecTunnelInOtherErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelInOtherErrors.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelInOtherErrors.setDescription('The number of packets discarded due to errors other than decryption, authentication or replay errors. This may include packets dropped due to a lack of receive buffers, and may include packets dropped due to congestion at the decryption element.')
wgIpsecTunnelOutDecryptErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelOutDecryptErrors.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelOutDecryptErrors.setDescription('Total number of packets discarded due to decryption error since the establish of this connection.')
wgIpsecTunnelOutAuthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelOutAuthErrors.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelOutAuthErrors.setDescription('Total number of packets discarded due to authentication error since the establish of this connection.')
wgIpsecTunnelOutReplayErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelOutReplayErrors.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelOutReplayErrors.setDescription('Total number of packets discarded due to replay error since the establish of this connection.')
wgIpsecTunnelOutOtherErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelOutOtherErrors.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelOutOtherErrors.setDescription('The number of packets discarded due to errors other than decryption, authentication or replay errors. This may include packets dropped due to a lack of receive buffers, and may include packets dropped due to congestion at the decryption element.')
wgIpsecTunnelUdpEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelUdpEncap.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelUdpEncap.setDescription('Indicates whether if UDP encapsulated IPSec has been enabled.')
wgIpsecTunnelPeerUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 41), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelPeerUdpPort.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelPeerUdpPort.setDescription("The peer's UDP port of current tunnel when UDP encapsulated IPSec is enabled.")
wgIpsecTunnelOrigPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 42), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgIpsecTunnelOrigPeerAddr.setStatus('current')
if mibBuilder.loadTexts: wgIpsecTunnelOrigPeerAddr.setDescription('The original peer ip address of current tunnel when UDP encapsulated IPSec is enabled')
mibBuilder.exportSymbols("WATCHGUARD-IPSEC-TUNNEL-MIB", wgIpsecTunnelLocalAddr=wgIpsecTunnelLocalAddr, wgIpsecTunnelSelectorLocalPort=wgIpsecTunnelSelectorLocalPort, wgIpsecTunnelInKbytes=wgIpsecTunnelInKbytes, wgIpsecTunnelMIB=wgIpsecTunnelMIB, wgIpsecTunnelInAuthErrors=wgIpsecTunnelInAuthErrors, wgIpsecTunnelInSaBytes=wgIpsecTunnelInSaBytes, wgIpsecTunnelAccSecs=wgIpsecTunnelAccSecs, wgIpsecTunnel=wgIpsecTunnel, wgIpsecTunnelInDecryptErrors=wgIpsecTunnelInDecryptErrors, wgIpsecTunnelKeyMode=wgIpsecTunnelKeyMode, wgIpsecTunnelOutAuthErrors=wgIpsecTunnelOutAuthErrors, wgIpsecTunnelOutSaBytes=wgIpsecTunnelOutSaBytes, wgIpsecTunnelInReplayErrors=wgIpsecTunnelInReplayErrors, wgIpsecTunnelSelectorRemotePort=wgIpsecTunnelSelectorRemotePort, wgIpsecTunnelSelectorLocalIPTwo=wgIpsecTunnelSelectorLocalIPTwo, wgIpsecTunnelCreateTime=wgIpsecTunnelCreateTime, wgIpsecTunnelEspAuthAlg=wgIpsecTunnelEspAuthAlg, wgIpsecTunnelEspEncryptAlg=wgIpsecTunnelEspEncryptAlg, wgIpsecTunnelSelectorRemoteIPOne=wgIpsecTunnelSelectorRemoteIPOne, wgIpsecTunnelInPackets=wgIpsecTunnelInPackets, wgIpsecTunnelLifeTime=wgIpsecTunnelLifeTime, wgIpsecTunnelPeerUdpPort=wgIpsecTunnelPeerUdpPort, wgIpsecTunnelEntry=wgIpsecTunnelEntry, wgIpsecTunnelSelectorLocalIPType=wgIpsecTunnelSelectorLocalIPType, wgIpsecTunnelInSpi=wgIpsecTunnelInSpi, wgIpsecTunnelOutDecryptErrors=wgIpsecTunnelOutDecryptErrors, wgIpsecTunnelSelectorRemoteIPTwo=wgIpsecTunnelSelectorRemoteIPTwo, wgIpsecTunnelUdpEncap=wgIpsecTunnelUdpEncap, wgIpsecTunnelOutReplayErrors=wgIpsecTunnelOutReplayErrors, wgIpsecTunnelOutOtherErrors=wgIpsecTunnelOutOtherErrors, wgIpsecTunnelPeerAddr=wgIpsecTunnelPeerAddr, wgIpsecTunnelSelectorRemoteIPType=wgIpsecTunnelSelectorRemoteIPType, wgIpsecTunnelNumRekey=wgIpsecTunnelNumRekey, PYSNMP_MODULE_ID=wgInfoModule, wgIpsecTunnelNum=wgIpsecTunnelNum, wgIpsecTunnelOutSpi=wgIpsecTunnelOutSpi, wgIpsecTunnelOrigPeerAddr=wgIpsecTunnelOrigPeerAddr, wgIpsecTunnelOutPackets=wgIpsecTunnelOutPackets, wgIpsecTunnelTable=wgIpsecTunnelTable, wgIpsecTunnelSelectorLocalIPOne=wgIpsecTunnelSelectorLocalIPOne, wgIpsecTunnelOutKbytes=wgIpsecTunnelOutKbytes, wgIpsecTunnelDeviceID=wgIpsecTunnelDeviceID, wgInfoModule=wgInfoModule, wgIpsecTunnelLifeLength=wgIpsecTunnelLifeLength, wgIpsecTunnelID=wgIpsecTunnelID, wgIpsecTunnelInOtherErrors=wgIpsecTunnelInOtherErrors, wgIpsecTunnelAhAuthAlg=wgIpsecTunnelAhAuthAlg, wgIpsecTunnelMode=wgIpsecTunnelMode, wgIpsecTunnelSelectorProtocol=wgIpsecTunnelSelectorProtocol)
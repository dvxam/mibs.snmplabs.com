#
# PySNMP MIB module REDSTONE-PPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-PPP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex", "InterfaceIndexOrZero")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
RsNextIfIndex, RsEnable = mibBuilder.importSymbols("REDSTONE-TC", "RsNextIfIndex", "RsEnable")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Counter32, Counter64, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Counter32", "Counter64", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "IpAddress", "Unsigned32")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
rsPppMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 11))
rsPppMIB.setRevisions(('1999-07-01 00:00', '1998-01-01 00:00',))
if mibBuilder.loadTexts: rsPppMIB.setLastUpdated('9907010000Z')
if mibBuilder.loadTexts: rsPppMIB.setOrganization('Redstone Communications, Inc.')
class RsPppAuthentication(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("pap", 1), ("chap", 2), ("papChap", 3), ("chapPap", 4))

rsPppObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1))
rsPppLcp = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1))
rsPppSec = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 2))
rsPppIp = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3))
rsPppOsi = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4))
rsPppSession = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5))
rsPppLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1), )
if mibBuilder.loadTexts: rsPppLinkStatusTable.setStatus('current')
rsPppLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsPppLinkStatusEntry.setStatus('current')
rsPppLinkStatusTerminateReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("none", 0), ("other", 1), ("adminDisable", 2), ("lowerLayerDown", 3), ("noUpperInterface", 4), ("authenticationFailure", 5), ("peerTerminated", 6), ("peerRenegotiated", 7), ("maxRetriesExceeded", 8), ("negotiationFailure", 9), ("keepaliveFailure", 10), ("sessionTimeout", 11), ("inactivityTimeout", 12), ("addressLeaseExpired", 13), ("adminLogout", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusTerminateReason.setStatus('current')
rsPppLinkStatusTerminateNegFailOption = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("other", 1), ("localMru", 2), ("remoteMru", 3), ("localMagicNumber", 4), ("remoteMagicNumber", 5), ("localAuthentication", 6), ("localToRemoteProtocolCompression", 7), ("localToRemoteACCompression", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusTerminateNegFailOption.setStatus('current')
rsPppLinkStatusInKeepaliveRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusInKeepaliveRequests.setStatus('current')
rsPppLinkStatusOutKeepaliveRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusOutKeepaliveRequests.setStatus('current')
rsPppLinkStatusInKeepaliveReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusInKeepaliveReplies.setStatus('current')
rsPppLinkStatusOutKeepaliveReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusOutKeepaliveReplies.setStatus('current')
rsPppLinkStatusKeepaliveFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusKeepaliveFailures.setStatus('current')
rsPppLinkStatusLocalMagicNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusLocalMagicNumber.setStatus('current')
rsPppLinkStatusRemoteMagicNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusRemoteMagicNumber.setStatus('current')
rsPppLinkStatusLocalAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 10), RsPppAuthentication()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppLinkStatusLocalAuthentication.setStatus('current')
rsPppLinkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2), )
if mibBuilder.loadTexts: rsPppLinkConfigTable.setStatus('current')
rsPppLinkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1), ).setIndexNames((0, "REDSTONE-PPP-MIB", "rsPppLinkConfigIfIndex"))
if mibBuilder.loadTexts: rsPppLinkConfigEntry.setStatus('current')
rsPppLinkConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rsPppLinkConfigIfIndex.setStatus('current')
rsPppLinkConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsPppLinkConfigRowStatus.setStatus('current')
rsPppLinkConfigLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsPppLinkConfigLowerIfIndex.setStatus('current')
rsPppLinkConfigKeepalive = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 300), )).clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsPppLinkConfigKeepalive.setStatus('current')
rsPppLinkConfigAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 5), RsPppAuthentication().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsPppLinkConfigAuthentication.setStatus('current')
rsPppLinkConfigMaxAuthenRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsPppLinkConfigMaxAuthenRetries.setStatus('current')
rsPppNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 3), RsNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppNextIfIndex.setStatus('current')
rsPppIpTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1), )
if mibBuilder.loadTexts: rsPppIpTable.setStatus('current')
rsPppIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsPppIpEntry.setStatus('current')
rsPppIpServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 1), RsEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppIpServiceStatus.setStatus('current')
rsPppIpTerminateReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("other", 1), ("noService", 2), ("admin", 3), ("linkDown", 4), ("peerTerminated", 5), ("peerRenegotiated", 6), ("maxRetriesExceeded", 7), ("negotiationFailure", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppIpTerminateReason.setStatus('current')
rsPppIpTerminateNegFailOption = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 0), ("other", 1), ("localIpAddress", 2), ("remoteIpAddress", 3), ("remotePrimaryDnsAddress", 4), ("remoteSecondaryDnsAddress", 5), ("remotePrimaryWinsAddress", 6), ("remoteSecondaryWinsAddress", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppIpTerminateNegFailOption.setStatus('current')
rsPppIpLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppIpLocalIpAddress.setStatus('current')
rsPppIpRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppIpRemoteIpAddress.setStatus('current')
rsPppIpRemotePrimaryDnsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppIpRemotePrimaryDnsAddress.setStatus('current')
rsPppIpRemoteSecondaryDnsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppIpRemoteSecondaryDnsAddress.setStatus('current')
rsPppIpRemotePrimaryWinsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppIpRemotePrimaryWinsAddress.setStatus('current')
rsPppIpRemoteSecondaryWinsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppIpRemoteSecondaryWinsAddress.setStatus('current')
rsPppIpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 2), )
if mibBuilder.loadTexts: rsPppIpConfigTable.setStatus('current')
rsPppIpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsPppIpConfigEntry.setStatus('current')
rsPppIpConfigPeerDnsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 2, 1, 1), RsEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsPppIpConfigPeerDnsPriority.setStatus('current')
rsPppIpConfigPeerWinsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 2, 1, 2), RsEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsPppIpConfigPeerWinsPriority.setStatus('current')
rsPppOsiTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1), )
if mibBuilder.loadTexts: rsPppOsiTable.setStatus('current')
rsPppOsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsPppOsiEntry.setStatus('current')
rsPppOsiServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 1), RsEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppOsiServiceStatus.setStatus('current')
rsPppOsiOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("opened", 1), ("not-opened", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppOsiOperStatus.setStatus('current')
rsPppOsiTerminateReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("other", 1), ("noService", 2), ("admin", 3), ("linkDown", 4), ("peerTerminated", 5), ("peerRenegotiated", 6), ("maxRetriesExceeded", 7), ("negotiationFailure", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppOsiTerminateReason.setStatus('current')
rsPppOsiTerminateNegFailOption = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("other", 1), ("localAlignNpdu", 2), ("remoteAlignNpdu", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppOsiTerminateNegFailOption.setStatus('current')
rsPppOsiLocalAlignNpdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 254, 255))).clone(namedValues=NamedValues(("none", 0), ("oneModulo4", 1), ("twoModulo4", 2), ("threeModulo4", 3), ("fourModulo4", 4), ("even", 254), ("odd", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppOsiLocalAlignNpdu.setStatus('current')
rsPppOsiRemoteAlignNpdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 254, 255))).clone(namedValues=NamedValues(("none", 0), ("oneModulo4", 1), ("twoModulo4", 2), ("threeModulo4", 3), ("fourModulo4", 4), ("even", 254), ("odd", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppOsiRemoteAlignNpdu.setStatus('current')
rsPppOsiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 2), )
if mibBuilder.loadTexts: rsPppOsiConfigTable.setStatus('current')
rsPppOsiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsPppOsiConfigEntry.setStatus('current')
rsPppOsiConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("close", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsPppOsiConfigAdminStatus.setStatus('current')
rsPppSessionTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1), )
if mibBuilder.loadTexts: rsPppSessionTable.setStatus('current')
rsPppSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsPppSessionEntry.setStatus('current')
rsPppSessionGrant = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionGrant.setStatus('current')
rsPppSessionTerminateReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("none", 0), ("unknown", 1), ("userRequest", 2), ("keepaliveFailure", 3), ("sessionTimeout", 4), ("inactivityTimeout", 5), ("adminDisable", 6), ("lowerLayerDown", 7), ("noUpperInterface", 8), ("deny", 9), ("noHardware", 10), ("noResources", 11), ("noInterface", 12), ("challengeTimeout", 13), ("requestTimeout", 14), ("authenticatorTimeout", 15), ("addressLeaseExpired", 16), ("adminLogout", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionTerminateReason.setStatus('current')
rsPppSessionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionStartTime.setStatus('current')
rsPppSessionInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionInOctets.setStatus('current')
rsPppSessionOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionOutOctets.setStatus('current')
rsPppSessionInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionInPackets.setStatus('current')
rsPppSessionOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionOutPackets.setStatus('current')
rsPppSessionSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 8), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionSessionTimeout.setStatus('current')
rsPppSessionInactivityTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 9), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionInactivityTimeout.setStatus('current')
rsPppSessionAccountingInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 10), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionAccountingInterval.setStatus('current')
rsPppSessionRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionRemoteIpAddress.setStatus('current')
rsPppSessionRemotePrimaryDnsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionRemotePrimaryDnsAddress.setStatus('current')
rsPppSessionRemoteSecondaryDnsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionRemoteSecondaryDnsAddress.setStatus('current')
rsPppSessionRemotePrimaryWinsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionRemotePrimaryWinsAddress.setStatus('current')
rsPppSessionRemoteSecondaryWinsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPppSessionRemoteSecondaryWinsAddress.setStatus('current')
rsPppConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4))
rsPppCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 1))
rsPppGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2))
rsPppCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 1, 1)).setObjects(("REDSTONE-PPP-MIB", "rsPppLcpGroup"), ("REDSTONE-PPP-MIB", "rsPppIpGroup"), ("REDSTONE-PPP-MIB", "rsPppOsiGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPppCompliance = rsPppCompliance.setStatus('current')
rsPppCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 1, 2)).setObjects(("REDSTONE-PPP-MIB", "rsPppLcpGroup2"), ("REDSTONE-PPP-MIB", "rsPppIpGroup2"), ("REDSTONE-PPP-MIB", "rsPppOsiGroup2"), ("REDSTONE-PPP-MIB", "rsPppSessionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPppCompliance2 = rsPppCompliance2.setStatus('current')
rsPppLcpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 1)).setObjects(("REDSTONE-PPP-MIB", "rsPppLinkConfigRowStatus"), ("REDSTONE-PPP-MIB", "rsPppLinkConfigLowerIfIndex"), ("REDSTONE-PPP-MIB", "rsPppNextIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPppLcpGroup = rsPppLcpGroup.setStatus('current')
rsPppIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 2)).setObjects(("REDSTONE-PPP-MIB", "rsPppIpServiceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPppIpGroup = rsPppIpGroup.setStatus('current')
rsPppOsiGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 3)).setObjects(("REDSTONE-PPP-MIB", "rsPppOsiServiceStatus"), ("REDSTONE-PPP-MIB", "rsPppOsiOperStatus"), ("REDSTONE-PPP-MIB", "rsPppOsiConfigAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPppOsiGroup = rsPppOsiGroup.setStatus('current')
rsPppLcpGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 4)).setObjects(("REDSTONE-PPP-MIB", "rsPppLinkStatusTerminateReason"), ("REDSTONE-PPP-MIB", "rsPppLinkStatusTerminateNegFailOption"), ("REDSTONE-PPP-MIB", "rsPppLinkStatusInKeepaliveRequests"), ("REDSTONE-PPP-MIB", "rsPppLinkStatusOutKeepaliveRequests"), ("REDSTONE-PPP-MIB", "rsPppLinkStatusInKeepaliveReplies"), ("REDSTONE-PPP-MIB", "rsPppLinkStatusOutKeepaliveReplies"), ("REDSTONE-PPP-MIB", "rsPppLinkStatusKeepaliveFailures"), ("REDSTONE-PPP-MIB", "rsPppLinkStatusLocalMagicNumber"), ("REDSTONE-PPP-MIB", "rsPppLinkStatusRemoteMagicNumber"), ("REDSTONE-PPP-MIB", "rsPppLinkStatusLocalAuthentication"), ("REDSTONE-PPP-MIB", "rsPppLinkConfigRowStatus"), ("REDSTONE-PPP-MIB", "rsPppLinkConfigLowerIfIndex"), ("REDSTONE-PPP-MIB", "rsPppLinkConfigKeepalive"), ("REDSTONE-PPP-MIB", "rsPppLinkConfigAuthentication"), ("REDSTONE-PPP-MIB", "rsPppLinkConfigMaxAuthenRetries"), ("REDSTONE-PPP-MIB", "rsPppNextIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPppLcpGroup2 = rsPppLcpGroup2.setStatus('current')
rsPppIpGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 5)).setObjects(("REDSTONE-PPP-MIB", "rsPppIpServiceStatus"), ("REDSTONE-PPP-MIB", "rsPppIpTerminateReason"), ("REDSTONE-PPP-MIB", "rsPppIpTerminateNegFailOption"), ("REDSTONE-PPP-MIB", "rsPppIpRemoteIpAddress"), ("REDSTONE-PPP-MIB", "rsPppIpRemotePrimaryDnsAddress"), ("REDSTONE-PPP-MIB", "rsPppIpRemoteSecondaryDnsAddress"), ("REDSTONE-PPP-MIB", "rsPppIpRemotePrimaryWinsAddress"), ("REDSTONE-PPP-MIB", "rsPppIpRemoteSecondaryWinsAddress"), ("REDSTONE-PPP-MIB", "rsPppIpConfigPeerDnsPriority"), ("REDSTONE-PPP-MIB", "rsPppIpConfigPeerWinsPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPppIpGroup2 = rsPppIpGroup2.setStatus('current')
rsPppOsiGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 6)).setObjects(("REDSTONE-PPP-MIB", "rsPppOsiServiceStatus"), ("REDSTONE-PPP-MIB", "rsPppOsiOperStatus"), ("REDSTONE-PPP-MIB", "rsPppOsiTerminateReason"), ("REDSTONE-PPP-MIB", "rsPppOsiTerminateNegFailOption"), ("REDSTONE-PPP-MIB", "rsPppOsiLocalAlignNpdu"), ("REDSTONE-PPP-MIB", "rsPppOsiRemoteAlignNpdu"), ("REDSTONE-PPP-MIB", "rsPppOsiConfigAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPppOsiGroup2 = rsPppOsiGroup2.setStatus('current')
rsPppSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 7)).setObjects(("REDSTONE-PPP-MIB", "rsPppSessionGrant"), ("REDSTONE-PPP-MIB", "rsPppSessionTerminateReason"), ("REDSTONE-PPP-MIB", "rsPppSessionStartTime"), ("REDSTONE-PPP-MIB", "rsPppSessionInOctets"), ("REDSTONE-PPP-MIB", "rsPppSessionOutOctets"), ("REDSTONE-PPP-MIB", "rsPppSessionInPackets"), ("REDSTONE-PPP-MIB", "rsPppSessionOutPackets"), ("REDSTONE-PPP-MIB", "rsPppSessionSessionTimeout"), ("REDSTONE-PPP-MIB", "rsPppSessionInactivityTimeout"), ("REDSTONE-PPP-MIB", "rsPppSessionAccountingInterval"), ("REDSTONE-PPP-MIB", "rsPppSessionRemoteIpAddress"), ("REDSTONE-PPP-MIB", "rsPppSessionRemotePrimaryDnsAddress"), ("REDSTONE-PPP-MIB", "rsPppSessionRemoteSecondaryDnsAddress"), ("REDSTONE-PPP-MIB", "rsPppSessionRemotePrimaryWinsAddress"), ("REDSTONE-PPP-MIB", "rsPppSessionRemoteSecondaryWinsAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPppSessionGroup = rsPppSessionGroup.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-PPP-MIB", rsPppIpConfigPeerWinsPriority=rsPppIpConfigPeerWinsPriority, rsPppLinkConfigAuthentication=rsPppLinkConfigAuthentication, rsPppSessionInactivityTimeout=rsPppSessionInactivityTimeout, rsPppIpTerminateNegFailOption=rsPppIpTerminateNegFailOption, rsPppLinkStatusLocalAuthentication=rsPppLinkStatusLocalAuthentication, rsPppIpConfigPeerDnsPriority=rsPppIpConfigPeerDnsPriority, rsPppOsiTerminateReason=rsPppOsiTerminateReason, rsPppLinkStatusTerminateNegFailOption=rsPppLinkStatusTerminateNegFailOption, rsPppSessionTable=rsPppSessionTable, rsPppLcpGroup=rsPppLcpGroup, rsPppSessionRemoteSecondaryWinsAddress=rsPppSessionRemoteSecondaryWinsAddress, rsPppIpRemoteIpAddress=rsPppIpRemoteIpAddress, rsPppSessionOutOctets=rsPppSessionOutOctets, rsPppIpRemoteSecondaryDnsAddress=rsPppIpRemoteSecondaryDnsAddress, PYSNMP_MODULE_ID=rsPppMIB, rsPppIp=rsPppIp, rsPppSessionStartTime=rsPppSessionStartTime, rsPppSessionAccountingInterval=rsPppSessionAccountingInterval, rsPppOsi=rsPppOsi, rsPppCompliances=rsPppCompliances, RsPppAuthentication=RsPppAuthentication, rsPppLinkStatusInKeepaliveRequests=rsPppLinkStatusInKeepaliveRequests, rsPppSessionOutPackets=rsPppSessionOutPackets, rsPppLinkStatusOutKeepaliveReplies=rsPppLinkStatusOutKeepaliveReplies, rsPppIpEntry=rsPppIpEntry, rsPppLinkStatusOutKeepaliveRequests=rsPppLinkStatusOutKeepaliveRequests, rsPppSessionRemoteSecondaryDnsAddress=rsPppSessionRemoteSecondaryDnsAddress, rsPppOsiGroup=rsPppOsiGroup, rsPppLinkStatusInKeepaliveReplies=rsPppLinkStatusInKeepaliveReplies, rsPppOsiOperStatus=rsPppOsiOperStatus, rsPppMIB=rsPppMIB, rsPppCompliance=rsPppCompliance, rsPppOsiEntry=rsPppOsiEntry, rsPppIpGroup2=rsPppIpGroup2, rsPppLcpGroup2=rsPppLcpGroup2, rsPppOsiRemoteAlignNpdu=rsPppOsiRemoteAlignNpdu, rsPppIpLocalIpAddress=rsPppIpLocalIpAddress, rsPppSessionRemoteIpAddress=rsPppSessionRemoteIpAddress, rsPppLinkConfigRowStatus=rsPppLinkConfigRowStatus, rsPppSec=rsPppSec, rsPppLinkConfigIfIndex=rsPppLinkConfigIfIndex, rsPppSessionGroup=rsPppSessionGroup, rsPppIpConfigTable=rsPppIpConfigTable, rsPppIpConfigEntry=rsPppIpConfigEntry, rsPppSessionTerminateReason=rsPppSessionTerminateReason, rsPppConformance=rsPppConformance, rsPppSessionInPackets=rsPppSessionInPackets, rsPppIpGroup=rsPppIpGroup, rsPppLinkStatusLocalMagicNumber=rsPppLinkStatusLocalMagicNumber, rsPppLinkStatusTable=rsPppLinkStatusTable, rsPppOsiServiceStatus=rsPppOsiServiceStatus, rsPppSession=rsPppSession, rsPppIpServiceStatus=rsPppIpServiceStatus, rsPppOsiLocalAlignNpdu=rsPppOsiLocalAlignNpdu, rsPppIpRemotePrimaryDnsAddress=rsPppIpRemotePrimaryDnsAddress, rsPppIpRemoteSecondaryWinsAddress=rsPppIpRemoteSecondaryWinsAddress, rsPppSessionInOctets=rsPppSessionInOctets, rsPppOsiGroup2=rsPppOsiGroup2, rsPppNextIfIndex=rsPppNextIfIndex, rsPppLinkStatusKeepaliveFailures=rsPppLinkStatusKeepaliveFailures, rsPppSessionSessionTimeout=rsPppSessionSessionTimeout, rsPppLcp=rsPppLcp, rsPppLinkStatusTerminateReason=rsPppLinkStatusTerminateReason, rsPppSessionRemotePrimaryWinsAddress=rsPppSessionRemotePrimaryWinsAddress, rsPppLinkConfigMaxAuthenRetries=rsPppLinkConfigMaxAuthenRetries, rsPppIpRemotePrimaryWinsAddress=rsPppIpRemotePrimaryWinsAddress, rsPppLinkConfigLowerIfIndex=rsPppLinkConfigLowerIfIndex, rsPppObjects=rsPppObjects, rsPppIpTable=rsPppIpTable, rsPppGroups=rsPppGroups, rsPppCompliance2=rsPppCompliance2, rsPppOsiTerminateNegFailOption=rsPppOsiTerminateNegFailOption, rsPppLinkStatusRemoteMagicNumber=rsPppLinkStatusRemoteMagicNumber, rsPppOsiConfigEntry=rsPppOsiConfigEntry, rsPppLinkConfigTable=rsPppLinkConfigTable, rsPppOsiConfigAdminStatus=rsPppOsiConfigAdminStatus, rsPppOsiTable=rsPppOsiTable, rsPppLinkConfigEntry=rsPppLinkConfigEntry, rsPppIpTerminateReason=rsPppIpTerminateReason, rsPppOsiConfigTable=rsPppOsiConfigTable, rsPppLinkStatusEntry=rsPppLinkStatusEntry, rsPppSessionRemotePrimaryDnsAddress=rsPppSessionRemotePrimaryDnsAddress, rsPppSessionEntry=rsPppSessionEntry, rsPppSessionGrant=rsPppSessionGrant, rsPppLinkConfigKeepalive=rsPppLinkConfigKeepalive)

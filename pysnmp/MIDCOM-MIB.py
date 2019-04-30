#
# PySNMP MIB module MIDCOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MIDCOM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:02:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetPortNumber, InetAddressPrefixLength, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddressPrefixLength", "InetAddress")
NatBindIdOrZero, = mibBuilder.importSymbols("NAT-MIB", "NatBindIdOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Integer32, TimeTicks, MibIdentifier, Counter64, ModuleIdentity, Counter32, Gauge32, Bits, ObjectIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Integer32", "TimeTicks", "MibIdentifier", "Counter64", "ModuleIdentity", "Counter32", "Gauge32", "Bits", "ObjectIdentity", "IpAddress", "NotificationType")
RowStatus, TextualConvention, TruthValue, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString", "StorageType")
midcomMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 171))
midcomMIB.setRevisions(('2007-08-09 10:11',))
if mibBuilder.loadTexts: midcomMIB.setLastUpdated('200708091011Z')
if mibBuilder.loadTexts: midcomMIB.setOrganization('IETF Middlebox Communication Working Group')
midcomNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 171, 0))
midcomObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 171, 1))
midcomConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 171, 2))
midcomTransaction = MibIdentifier((1, 3, 6, 1, 2, 1, 171, 1, 1))
midcomConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 171, 1, 2))
midcomMonitoring = MibIdentifier((1, 3, 6, 1, 2, 1, 171, 1, 3))
midcomRuleTable = MibTable((1, 3, 6, 1, 2, 1, 171, 1, 1, 3), )
if mibBuilder.loadTexts: midcomRuleTable.setStatus('current')
midcomRuleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1), ).setIndexNames((0, "MIDCOM-MIB", "midcomRuleOwner"), (0, "MIDCOM-MIB", "midcomGroupIndex"), (0, "MIDCOM-MIB", "midcomRuleIndex"))
if mibBuilder.loadTexts: midcomRuleEntry.setStatus('current')
midcomRuleOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: midcomRuleOwner.setStatus('current')
midcomRuleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: midcomRuleIndex.setStatus('current')
midcomRuleAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reserve", 1), ("enable", 2), ("notSet", 3))).clone('notSet')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleAdminStatus.setStatus('current')
midcomRuleOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("newEntry", 1), ("setting", 2), ("checkingRequest", 3), ("incorrectRequest", 4), ("processingRequest", 5), ("requestRejected", 6), ("reserved", 7), ("enabled", 8), ("timedOut", 9), ("terminatedOnRequest", 10), ("terminated", 11), ("genericError", 12))).clone('newEntry')).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRuleOperStatus.setStatus('current')
midcomRuleStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 6), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleStorageType.setStatus('current')
midcomRuleStorageTime = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 7), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleStorageTime.setStatus('current')
midcomRuleError = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 8), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRuleError.setStatus('current')
midcomRuleInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 9), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleInterface.setStatus('current')
midcomRuleFlowDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("biDirectional", 3))).clone('outbound')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleFlowDirection.setStatus('current')
midcomRuleMaxIdleTime = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 11), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleMaxIdleTime.setStatus('current')
midcomRuleTransportProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleTransportProtocol.setStatus('current')
midcomRulePortRange = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("single", 1), ("pair", 2))).clone('single')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRulePortRange.setStatus('current')
midcomRuleInternalIpVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 14), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleInternalIpVersion.setStatus('current')
midcomRuleExternalIpVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 15), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleExternalIpVersion.setStatus('current')
midcomRuleInternalIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 16), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleInternalIpAddr.setStatus('current')
midcomRuleInternalIpPrefixLength = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 17), InetAddressPrefixLength().clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleInternalIpPrefixLength.setStatus('current')
midcomRuleInternalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 18), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleInternalPort.setStatus('current')
midcomRuleExternalIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 19), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleExternalIpAddr.setStatus('current')
midcomRuleExternalIpPrefixLength = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 20), InetAddressPrefixLength().clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleExternalIpPrefixLength.setStatus('current')
midcomRuleExternalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 21), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleExternalPort.setStatus('current')
midcomRuleInsideIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 22), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRuleInsideIpAddr.setStatus('current')
midcomRuleInsidePort = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 23), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRuleInsidePort.setStatus('current')
midcomRuleOutsideIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 24), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRuleOutsideIpAddr.setStatus('current')
midcomRuleOutsidePort = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 25), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRuleOutsidePort.setStatus('current')
midcomRuleLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 26), Unsigned32().clone(180)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleLifetime.setStatus('current')
midcomRuleRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: midcomRuleRowStatus.setStatus('current')
midcomGroupTable = MibTable((1, 3, 6, 1, 2, 1, 171, 1, 1, 4), )
if mibBuilder.loadTexts: midcomGroupTable.setStatus('current')
midcomGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 171, 1, 1, 4, 1), ).setIndexNames((0, "MIDCOM-MIB", "midcomRuleOwner"), (0, "MIDCOM-MIB", "midcomGroupIndex"))
if mibBuilder.loadTexts: midcomGroupEntry.setStatus('current')
midcomGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: midcomGroupIndex.setStatus('current')
midcomGroupLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 1, 4, 1, 3), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: midcomGroupLifetime.setStatus('current')
midcomConfigMaxLifetime = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 2, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: midcomConfigMaxLifetime.setStatus('current')
midcomConfigPersistentRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 2, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: midcomConfigPersistentRules.setStatus('current')
midcomConfigIfTable = MibTable((1, 3, 6, 1, 2, 1, 171, 1, 2, 3), )
if mibBuilder.loadTexts: midcomConfigIfTable.setStatus('current')
midcomConfigIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 171, 1, 2, 3, 1), ).setIndexNames((0, "MIDCOM-MIB", "midcomConfigIfIndex"))
if mibBuilder.loadTexts: midcomConfigIfEntry.setStatus('current')
midcomConfigIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 2, 3, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: midcomConfigIfIndex.setStatus('current')
midcomConfigIfBits = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 2, 3, 1, 2), Bits().clone(namedValues=NamedValues(("ipv4", 0), ("ipv6", 1), ("addressWildcards", 2), ("portWildcards", 3), ("firewall", 4), ("nat", 5), ("portTranslation", 6), ("protocolTranslation", 7), ("twiceNat", 8), ("inside", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomConfigIfBits.setStatus('current')
midcomConfigIfEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 2, 3, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: midcomConfigIfEnabled.setStatus('current')
midcomConfigFirewallTable = MibTable((1, 3, 6, 1, 2, 1, 171, 1, 2, 4), )
if mibBuilder.loadTexts: midcomConfigFirewallTable.setStatus('current')
midcomConfigFirewallEntry = MibTableRow((1, 3, 6, 1, 2, 1, 171, 1, 2, 4, 1), ).setIndexNames((0, "MIDCOM-MIB", "midcomConfigFirewallIndex"))
if mibBuilder.loadTexts: midcomConfigFirewallEntry.setStatus('current')
midcomConfigFirewallIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 2, 4, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: midcomConfigFirewallIndex.setStatus('current')
midcomConfigFirewallGroupId = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 2, 4, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: midcomConfigFirewallGroupId.setStatus('current')
midcomConfigFirewallPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 2, 4, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: midcomConfigFirewallPriority.setStatus('current')
class MidcomNatBindMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("addressBind", 1), ("addressPortBind", 2), ("none", 3))

class MidcomNatSessionIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

midcomResourceTable = MibTable((1, 3, 6, 1, 2, 1, 171, 1, 3, 1), )
if mibBuilder.loadTexts: midcomResourceTable.setStatus('current')
midcomResourceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1), )
midcomRuleEntry.registerAugmentions(("MIDCOM-MIB", "midcomResourceEntry"))
midcomResourceEntry.setIndexNames(*midcomRuleEntry.getIndexNames())
if mibBuilder.loadTexts: midcomResourceEntry.setStatus('current')
midcomRscNatInternalAddrBindMode = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 4), MidcomNatBindMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRscNatInternalAddrBindMode.setStatus('current')
midcomRscNatInternalAddrBindId = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 5), NatBindIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRscNatInternalAddrBindId.setStatus('current')
midcomRscNatInsideAddrBindMode = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 6), MidcomNatBindMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRscNatInsideAddrBindMode.setStatus('current')
midcomRscNatInsideAddrBindId = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 7), NatBindIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRscNatInsideAddrBindId.setStatus('current')
midcomRscNatSessionId1 = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 8), MidcomNatSessionIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRscNatSessionId1.setStatus('current')
midcomRscNatSessionId2 = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 9), MidcomNatSessionIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRscNatSessionId2.setStatus('current')
midcomRscFirewallRuleId = MibTableColumn((1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomRscFirewallRuleId.setStatus('current')
midcomStatistics = MibIdentifier((1, 3, 6, 1, 2, 1, 171, 1, 3, 2))
midcomCurrentOwners = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomCurrentOwners.setStatus('current')
midcomTotalRejectedRuleEntries = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalRejectedRuleEntries.setStatus('current')
midcomCurrentRulesIncomplete = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomCurrentRulesIncomplete.setStatus('current')
midcomTotalIncorrectReserveRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalIncorrectReserveRules.setStatus('current')
midcomTotalRejectedReserveRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalRejectedReserveRules.setStatus('current')
midcomCurrentActiveReserveRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomCurrentActiveReserveRules.setStatus('current')
midcomTotalExpiredReserveRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalExpiredReserveRules.setStatus('current')
midcomTotalTerminatedOnRqReserveRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalTerminatedOnRqReserveRules.setStatus('current')
midcomTotalTerminatedReserveRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalTerminatedReserveRules.setStatus('current')
midcomTotalIncorrectEnableRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalIncorrectEnableRules.setStatus('current')
midcomTotalRejectedEnableRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalRejectedEnableRules.setStatus('current')
midcomCurrentActiveEnableRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomCurrentActiveEnableRules.setStatus('current')
midcomTotalExpiredEnableRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalExpiredEnableRules.setStatus('current')
midcomTotalTerminatedOnRqEnableRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalTerminatedOnRqEnableRules.setStatus('current')
midcomTotalTerminatedEnableRules = MibScalar((1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: midcomTotalTerminatedEnableRules.setStatus('current')
midcomUnsolicitedRuleEvent = NotificationType((1, 3, 6, 1, 2, 1, 171, 0, 1)).setObjects(("MIDCOM-MIB", "midcomRuleOperStatus"), ("MIDCOM-MIB", "midcomRuleLifetime"))
if mibBuilder.loadTexts: midcomUnsolicitedRuleEvent.setStatus('current')
midcomSolicitedRuleEvent = NotificationType((1, 3, 6, 1, 2, 1, 171, 0, 2)).setObjects(("MIDCOM-MIB", "midcomRuleOperStatus"), ("MIDCOM-MIB", "midcomRuleLifetime"))
if mibBuilder.loadTexts: midcomSolicitedRuleEvent.setStatus('current')
midcomSolicitedGroupEvent = NotificationType((1, 3, 6, 1, 2, 1, 171, 0, 3)).setObjects(("MIDCOM-MIB", "midcomGroupLifetime"))
if mibBuilder.loadTexts: midcomSolicitedGroupEvent.setStatus('current')
midcomCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 171, 2, 1))
midcomGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 171, 2, 2))
midcomCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 171, 2, 1, 1)).setObjects(("MIDCOM-MIB", "midcomRuleGroup"), ("MIDCOM-MIB", "midcomNotificationsGroup"), ("MIDCOM-MIB", "midcomCapabilitiesGroup"), ("MIDCOM-MIB", "midcomStatisticsGroup"), ("MIDCOM-MIB", "midcomConfigFirewallGroup"), ("MIDCOM-MIB", "midcomResourceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    midcomCompliance = midcomCompliance.setStatus('current')
midcomRuleGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 171, 2, 2, 1)).setObjects(("MIDCOM-MIB", "midcomRuleAdminStatus"), ("MIDCOM-MIB", "midcomRuleOperStatus"), ("MIDCOM-MIB", "midcomRuleStorageType"), ("MIDCOM-MIB", "midcomRuleStorageTime"), ("MIDCOM-MIB", "midcomRuleError"), ("MIDCOM-MIB", "midcomRuleInterface"), ("MIDCOM-MIB", "midcomRuleFlowDirection"), ("MIDCOM-MIB", "midcomRuleMaxIdleTime"), ("MIDCOM-MIB", "midcomRuleTransportProtocol"), ("MIDCOM-MIB", "midcomRulePortRange"), ("MIDCOM-MIB", "midcomRuleInternalIpVersion"), ("MIDCOM-MIB", "midcomRuleExternalIpVersion"), ("MIDCOM-MIB", "midcomRuleInternalIpAddr"), ("MIDCOM-MIB", "midcomRuleInternalIpPrefixLength"), ("MIDCOM-MIB", "midcomRuleInternalPort"), ("MIDCOM-MIB", "midcomRuleExternalIpAddr"), ("MIDCOM-MIB", "midcomRuleExternalIpPrefixLength"), ("MIDCOM-MIB", "midcomRuleExternalPort"), ("MIDCOM-MIB", "midcomRuleInsideIpAddr"), ("MIDCOM-MIB", "midcomRuleInsidePort"), ("MIDCOM-MIB", "midcomRuleOutsideIpAddr"), ("MIDCOM-MIB", "midcomRuleOutsidePort"), ("MIDCOM-MIB", "midcomRuleLifetime"), ("MIDCOM-MIB", "midcomRuleRowStatus"), ("MIDCOM-MIB", "midcomGroupLifetime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    midcomRuleGroup = midcomRuleGroup.setStatus('current')
midcomCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 171, 2, 2, 2)).setObjects(("MIDCOM-MIB", "midcomConfigMaxLifetime"), ("MIDCOM-MIB", "midcomConfigPersistentRules"), ("MIDCOM-MIB", "midcomConfigIfBits"), ("MIDCOM-MIB", "midcomConfigIfEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    midcomCapabilitiesGroup = midcomCapabilitiesGroup.setStatus('current')
midcomConfigFirewallGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 171, 2, 2, 3)).setObjects(("MIDCOM-MIB", "midcomConfigFirewallGroupId"), ("MIDCOM-MIB", "midcomConfigFirewallPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    midcomConfigFirewallGroup = midcomConfigFirewallGroup.setStatus('current')
midcomResourceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 171, 2, 2, 4)).setObjects(("MIDCOM-MIB", "midcomRscNatInternalAddrBindMode"), ("MIDCOM-MIB", "midcomRscNatInternalAddrBindId"), ("MIDCOM-MIB", "midcomRscNatInsideAddrBindMode"), ("MIDCOM-MIB", "midcomRscNatInsideAddrBindId"), ("MIDCOM-MIB", "midcomRscNatSessionId1"), ("MIDCOM-MIB", "midcomRscNatSessionId2"), ("MIDCOM-MIB", "midcomRscFirewallRuleId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    midcomResourceGroup = midcomResourceGroup.setStatus('current')
midcomStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 171, 2, 2, 5)).setObjects(("MIDCOM-MIB", "midcomCurrentOwners"), ("MIDCOM-MIB", "midcomTotalRejectedRuleEntries"), ("MIDCOM-MIB", "midcomCurrentRulesIncomplete"), ("MIDCOM-MIB", "midcomTotalIncorrectReserveRules"), ("MIDCOM-MIB", "midcomTotalRejectedReserveRules"), ("MIDCOM-MIB", "midcomCurrentActiveReserveRules"), ("MIDCOM-MIB", "midcomTotalExpiredReserveRules"), ("MIDCOM-MIB", "midcomTotalTerminatedOnRqReserveRules"), ("MIDCOM-MIB", "midcomTotalTerminatedReserveRules"), ("MIDCOM-MIB", "midcomTotalIncorrectEnableRules"), ("MIDCOM-MIB", "midcomTotalRejectedEnableRules"), ("MIDCOM-MIB", "midcomCurrentActiveEnableRules"), ("MIDCOM-MIB", "midcomTotalExpiredEnableRules"), ("MIDCOM-MIB", "midcomTotalTerminatedOnRqEnableRules"), ("MIDCOM-MIB", "midcomTotalTerminatedEnableRules"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    midcomStatisticsGroup = midcomStatisticsGroup.setStatus('current')
midcomNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 171, 2, 2, 6)).setObjects(("MIDCOM-MIB", "midcomUnsolicitedRuleEvent"), ("MIDCOM-MIB", "midcomSolicitedRuleEvent"), ("MIDCOM-MIB", "midcomSolicitedGroupEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    midcomNotificationsGroup = midcomNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("MIDCOM-MIB", midcomRuleFlowDirection=midcomRuleFlowDirection, midcomCompliance=midcomCompliance, midcomRuleIndex=midcomRuleIndex, midcomRuleAdminStatus=midcomRuleAdminStatus, midcomResourceEntry=midcomResourceEntry, midcomTotalTerminatedReserveRules=midcomTotalTerminatedReserveRules, midcomConfigFirewallEntry=midcomConfigFirewallEntry, midcomRuleInsidePort=midcomRuleInsidePort, midcomRuleInternalIpVersion=midcomRuleInternalIpVersion, midcomRscNatInsideAddrBindId=midcomRscNatInsideAddrBindId, midcomGroupLifetime=midcomGroupLifetime, midcomTotalRejectedRuleEntries=midcomTotalRejectedRuleEntries, midcomStatistics=midcomStatistics, midcomTotalIncorrectEnableRules=midcomTotalIncorrectEnableRules, midcomConfigFirewallGroup=midcomConfigFirewallGroup, midcomRuleError=midcomRuleError, PYSNMP_MODULE_ID=midcomMIB, midcomRuleOutsideIpAddr=midcomRuleOutsideIpAddr, midcomConfigFirewallTable=midcomConfigFirewallTable, midcomResourceGroup=midcomResourceGroup, MidcomNatBindMode=MidcomNatBindMode, midcomRscFirewallRuleId=midcomRscFirewallRuleId, midcomSolicitedGroupEvent=midcomSolicitedGroupEvent, midcomConfigIfIndex=midcomConfigIfIndex, midcomCurrentActiveReserveRules=midcomCurrentActiveReserveRules, midcomTotalTerminatedOnRqReserveRules=midcomTotalTerminatedOnRqReserveRules, midcomCurrentRulesIncomplete=midcomCurrentRulesIncomplete, midcomConfigFirewallPriority=midcomConfigFirewallPriority, midcomRuleGroup=midcomRuleGroup, midcomCurrentActiveEnableRules=midcomCurrentActiveEnableRules, midcomGroupEntry=midcomGroupEntry, midcomTotalTerminatedEnableRules=midcomTotalTerminatedEnableRules, midcomCompliances=midcomCompliances, midcomRscNatSessionId2=midcomRscNatSessionId2, midcomConfigPersistentRules=midcomConfigPersistentRules, midcomSolicitedRuleEvent=midcomSolicitedRuleEvent, midcomRuleOwner=midcomRuleOwner, midcomObjects=midcomObjects, midcomRulePortRange=midcomRulePortRange, midcomTransaction=midcomTransaction, midcomStatisticsGroup=midcomStatisticsGroup, midcomConfig=midcomConfig, midcomRuleExternalPort=midcomRuleExternalPort, midcomRscNatInternalAddrBindMode=midcomRscNatInternalAddrBindMode, midcomGroupIndex=midcomGroupIndex, midcomTotalTerminatedOnRqEnableRules=midcomTotalTerminatedOnRqEnableRules, midcomRuleInsideIpAddr=midcomRuleInsideIpAddr, midcomConfigFirewallIndex=midcomConfigFirewallIndex, midcomRscNatSessionId1=midcomRscNatSessionId1, midcomUnsolicitedRuleEvent=midcomUnsolicitedRuleEvent, midcomRuleOperStatus=midcomRuleOperStatus, midcomConfigFirewallGroupId=midcomConfigFirewallGroupId, midcomTotalRejectedEnableRules=midcomTotalRejectedEnableRules, midcomTotalExpiredReserveRules=midcomTotalExpiredReserveRules, midcomRuleInternalPort=midcomRuleInternalPort, MidcomNatSessionIdOrZero=MidcomNatSessionIdOrZero, midcomConfigIfEnabled=midcomConfigIfEnabled, midcomNotificationsGroup=midcomNotificationsGroup, midcomRscNatInternalAddrBindId=midcomRscNatInternalAddrBindId, midcomTotalRejectedReserveRules=midcomTotalRejectedReserveRules, midcomRuleExternalIpPrefixLength=midcomRuleExternalIpPrefixLength, midcomRuleExternalIpAddr=midcomRuleExternalIpAddr, midcomMIB=midcomMIB, midcomRuleStorageType=midcomRuleStorageType, midcomConfigMaxLifetime=midcomConfigMaxLifetime, midcomNotifications=midcomNotifications, midcomRuleTransportProtocol=midcomRuleTransportProtocol, midcomConformance=midcomConformance, midcomRuleInternalIpAddr=midcomRuleInternalIpAddr, midcomRuleTable=midcomRuleTable, midcomGroups=midcomGroups, midcomCurrentOwners=midcomCurrentOwners, midcomRuleRowStatus=midcomRuleRowStatus, midcomMonitoring=midcomMonitoring, midcomRuleMaxIdleTime=midcomRuleMaxIdleTime, midcomRuleStorageTime=midcomRuleStorageTime, midcomRuleOutsidePort=midcomRuleOutsidePort, midcomRuleInterface=midcomRuleInterface, midcomRuleLifetime=midcomRuleLifetime, midcomRuleInternalIpPrefixLength=midcomRuleInternalIpPrefixLength, midcomTotalIncorrectReserveRules=midcomTotalIncorrectReserveRules, midcomRuleExternalIpVersion=midcomRuleExternalIpVersion, midcomRuleEntry=midcomRuleEntry, midcomConfigIfTable=midcomConfigIfTable, midcomRscNatInsideAddrBindMode=midcomRscNatInsideAddrBindMode, midcomGroupTable=midcomGroupTable, midcomConfigIfEntry=midcomConfigIfEntry, midcomCapabilitiesGroup=midcomCapabilitiesGroup, midcomConfigIfBits=midcomConfigIfBits, midcomResourceTable=midcomResourceTable, midcomTotalExpiredEnableRules=midcomTotalExpiredEnableRules)
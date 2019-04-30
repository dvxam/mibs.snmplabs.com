#
# PySNMP MIB module CADANT-CMTS-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:27:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cadIfMacDomainIfIndex, = mibBuilder.importSymbols("CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex")
cadLayer3, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadLayer3")
mgmdPmStaticGroupAddressType, mgmdPmStaticGroupEntityType, mgmdPmStaticGroupIfIndex = mibBuilder.importSymbols("DC-MGMD-MIB", "mgmdPmStaticGroupAddressType", "mgmdPmStaticGroupEntityType", "mgmdPmStaticGroupIfIndex")
ChSetId, = mibBuilder.importSymbols("DOCS-IF3-MIB", "ChSetId")
dsgIfClassId, Dsid, dsgIfTunnelGrpIndex, dsgIfTunnelIndex = mibBuilder.importSymbols("DSG-IF-MIB", "dsgIfClassId", "Dsid", "dsgIfTunnelGrpIndex", "dsgIfTunnelIndex")
ifIndex, InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddressType, InetAddressPrefixLength, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressPrefixLength", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ModuleIdentity, Integer32, Gauge32, iso, Counter32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ModuleIdentity", "Integer32", "Gauge32", "iso", "Counter32", "ObjectIdentity", "NotificationType")
TruthValue, TextualConvention, DisplayString, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus", "MacAddress")
cadMcastStdMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10))
cadMcastStdMib.setRevisions(('2015-01-28 00:00', '2014-09-22 00:00', '2014-06-04 00:00', '2014-04-08 00:00', '2013-07-18 00:00', '2013-01-28 00:00', '2012-10-08 00:00', '2011-11-08 00:00', '2011-04-05 00:00', '2011-04-04 00:00', '2011-03-21 00:00', '2011-03-08 00:00', '2005-08-09 00:00',))
if mibBuilder.loadTexts: cadMcastStdMib.setLastUpdated('201501280000Z')
if mibBuilder.loadTexts: cadMcastStdMib.setOrganization('Arris Inc')
cadMcastStaticMacIpBindingTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1), )
if mibBuilder.loadTexts: cadMcastStaticMacIpBindingTable.setStatus('current')
cadMcastStaticMacIpBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1), ).setIndexNames((0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastStaticMacIpBindingAddressType"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastStaticMacIpBindingAddress"))
if mibBuilder.loadTexts: cadMcastStaticMacIpBindingEntry.setStatus('current')
cadMcastStaticMacIpBindingAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cadMcastStaticMacIpBindingAddressType.setStatus('current')
cadMcastStaticMacIpBindingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: cadMcastStaticMacIpBindingAddress.setStatus('current')
cadMcastStaticMacIpBindingMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1, 3), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadMcastStaticMacIpBindingMacAddress.setStatus('current')
cadMcastStaticMacIpBindingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadMcastStaticMacIpBindingStatus.setStatus('current')
cadMcastMrouteTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2), )
if mibBuilder.loadTexts: cadMcastMrouteTable.setStatus('current')
cadMcastMrouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1), ).setIndexNames((0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastMrouteType"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastMrouteSourceAddress"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastMrouteSourcePrefix"))
if mibBuilder.loadTexts: cadMcastMrouteEntry.setStatus('current')
cadMcastMrouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cadMcastMrouteType.setStatus('current')
cadMcastMrouteSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: cadMcastMrouteSourceAddress.setStatus('current')
cadMcastMrouteSourcePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 3), InetAddressPrefixLength())
if mibBuilder.loadTexts: cadMcastMrouteSourcePrefix.setStatus('current')
cadMcastMrouteRpfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadMcastMrouteRpfAddress.setStatus('current')
cadMcastMrouteDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadMcastMrouteDistance.setStatus('current')
cadMcastMrouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadMcastMrouteStatus.setStatus('current')
cadMcastForwardTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3), )
if mibBuilder.loadTexts: cadMcastForwardTable.setStatus('current')
cadMcastForwardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1), ).setIndexNames((0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardAddressType"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardGroupAddress"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardSourceAddress"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardSourceIf"))
if mibBuilder.loadTexts: cadMcastForwardEntry.setStatus('current')
cadMcastForwardAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cadMcastForwardAddressType.setStatus('current')
cadMcastForwardGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 2), InetAddress())
if mibBuilder.loadTexts: cadMcastForwardGroupAddress.setStatus('current')
cadMcastForwardSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 3), InetAddress())
if mibBuilder.loadTexts: cadMcastForwardSourceAddress.setStatus('current')
cadMcastForwardSourceIf = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 4), InterfaceIndexOrZero())
if mibBuilder.loadTexts: cadMcastForwardSourceIf.setStatus('current')
cadMcastForwardDestIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastForwardDestIfList.setStatus('current')
cadMcastForwardCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastForwardCount.setStatus('current')
cadMcastForwardDestTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4), )
if mibBuilder.loadTexts: cadMcastForwardDestTable.setStatus('current')
cadMcastForwardDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4, 1), ).setIndexNames((0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardDestIfListId"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardDestIfType"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardDestIf"))
if mibBuilder.loadTexts: cadMcastForwardDestEntry.setStatus('current')
cadMcastForwardDestIfListId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cadMcastForwardDestIfListId.setStatus('current')
cadMcastForwardDestIf = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastForwardDestIf.setStatus('current')
cadMcastForwardDestIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("docsis", 1), ("sdv", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastForwardDestIfType.setStatus('current')
cadMcastGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5))
cadMcastClearForwardCounts = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadMcastClearForwardCounts.setStatus('current')
cadMcastForwardUseDefaultFlow = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadMcastForwardUseDefaultFlow.setStatus('current')
cadMcastDeleteDsg = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadMcastDeleteDsg.setStatus('current')
cadMcastIgmpThrottleEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadMcastIgmpThrottleEnable.setStatus('current')
cadMcastIgmpThrottleBurstSize = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 40)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadMcastIgmpThrottleBurstSize.setStatus('current')
cadMcastIgmpThrottleInterval = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadMcastIgmpThrottleInterval.setStatus('current')
cadMcastIgmpThrottleIncrement = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadMcastIgmpThrottleIncrement.setStatus('current')
cadMcastClearVideoForwardCounts = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadMcastClearVideoForwardCounts.setStatus('current')
cadFqdnCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 6))
cadFqdnCacheEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 6, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadFqdnCacheEnable.setStatus('current')
cadFqdnCachePollInterval = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 6, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(300, 86400)).clone(1800)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadFqdnCachePollInterval.setStatus('current')
cadFqdnCacheRefresh = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 6, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadFqdnCacheRefresh.setStatus('current')
cadFqdnCacheTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7), )
if mibBuilder.loadTexts: cadFqdnCacheTable.setStatus('current')
cadFqdnCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1), ).setIndexNames((0, "CADANT-CMTS-MULTICAST-MIB", "cadFqdnCacheName"))
if mibBuilder.loadTexts: cadFqdnCacheEntry.setStatus('current')
cadFqdnCacheName = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 154)))
if mibBuilder.loadTexts: cadFqdnCacheName.setStatus('current')
cadFqdnCacheFqdn = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadFqdnCacheFqdn.setStatus('current')
cadFqdnCacheIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 3), InetAddressType().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadFqdnCacheIpAddrType.setStatus('current')
cadFqdnCacheIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 4), InetAddress().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadFqdnCacheIpAddress.setStatus('current')
cadFqdnCacheLastUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadFqdnCacheLastUpdateTime.setStatus('current')
cadFqdnCacheStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("validIp", 1), ("unknownIp", 2), ("invalidIp", 3), ("timeout", 4), ("genError", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadFqdnCacheStatus.setStatus('current')
cadDsgIfClassifierCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 8), )
if mibBuilder.loadTexts: cadDsgIfClassifierCfgTable.setStatus('current')
cadDsgIfClassifierCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 8, 1), ).setIndexNames((0, "DSG-IF-MIB", "dsgIfTunnelIndex"), (0, "DSG-IF-MIB", "dsgIfClassId"))
if mibBuilder.loadTexts: cadDsgIfClassifierCfgEntry.setStatus('current')
cadDsgIfSrcName = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 8, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 154))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDsgIfSrcName.setStatus('current')
cadDsgIfClassifierCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 8, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDsgIfClassifierCfgRowStatus.setStatus('current')
cadMgmdPmStaticGroupCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9), )
if mibBuilder.loadTexts: cadMgmdPmStaticGroupCfgTable.setStatus('current')
cadMgmdPmStaticGroupCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9, 1), ).setIndexNames((0, "DC-MGMD-MIB", "mgmdPmStaticGroupEntityType"), (0, "DC-MGMD-MIB", "mgmdPmStaticGroupIfIndex"), (0, "DC-MGMD-MIB", "mgmdPmStaticGroupAddressType"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMgmdPmStaticGroupAddress"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMgmdPmStaticGroupSourceName"))
if mibBuilder.loadTexts: cadMgmdPmStaticGroupCfgEntry.setStatus('current')
cadMgmdPmStaticGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9, 1, 1), InetAddress())
if mibBuilder.loadTexts: cadMgmdPmStaticGroupAddress.setStatus('current')
cadMgmdPmStaticGroupSourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 154))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMgmdPmStaticGroupSourceName.setStatus('current')
cadMgmdPmStaticGroupCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9, 1, 3), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMgmdPmStaticGroupCfgRowStatus.setStatus('current')
cadMcastStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10), )
if mibBuilder.loadTexts: cadMcastStatsTable.setStatus('current')
cadMcastStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1), ).setIndexNames((0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastStatsDsid"))
if mibBuilder.loadTexts: cadMcastStatsEntry.setStatus('current')
cadMcastStatsDsid = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 1), Dsid())
if mibBuilder.loadTexts: cadMcastStatsDsid.setStatus('current')
cadMcastStatsSentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 2), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastStatsSentPkts.setStatus('current')
cadMcastStatsSentOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 3), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastStatsSentOctets.setStatus('current')
cadMcastStatsDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 4), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastStatsDroppedPkts.setStatus('current')
cadMcastStatsDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 5), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastStatsDroppedOctets.setStatus('current')
cadMcastStatsDsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 6), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastStatsDsIfIndex.setStatus('current')
cadMcastStatsTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastStatsTunnelIndex.setStatus('current')
cadMcastStatsDsChSetId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 8), ChSetId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastStatsDsChSetId.setStatus('current')
cadMcastStatsGSFID = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMcastStatsGSFID.setStatus('current')
cadDsgIfTunnelChToGroupTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 11), )
if mibBuilder.loadTexts: cadDsgIfTunnelChToGroupTable.setStatus('current')
cadDsgIfTunnelChToGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 11, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CADANT-CMTS-MULTICAST-MIB", "cadDsgIfTunnelGrpIndex"))
if mibBuilder.loadTexts: cadDsgIfTunnelChToGroupEntry.setStatus('current')
cadDsgIfTunnelGrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 11, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDsgIfTunnelGrpIndex.setStatus('current')
mibBuilder.exportSymbols("CADANT-CMTS-MULTICAST-MIB", cadFqdnCacheIpAddrType=cadFqdnCacheIpAddrType, cadMgmdPmStaticGroupAddress=cadMgmdPmStaticGroupAddress, PYSNMP_MODULE_ID=cadMcastStdMib, cadMcastDeleteDsg=cadMcastDeleteDsg, cadMcastIgmpThrottleEnable=cadMcastIgmpThrottleEnable, cadMcastStaticMacIpBindingStatus=cadMcastStaticMacIpBindingStatus, cadFqdnCacheRefresh=cadFqdnCacheRefresh, cadDsgIfTunnelChToGroupEntry=cadDsgIfTunnelChToGroupEntry, cadMcastStaticMacIpBindingMacAddress=cadMcastStaticMacIpBindingMacAddress, cadMcastForwardTable=cadMcastForwardTable, cadDsgIfSrcName=cadDsgIfSrcName, cadMgmdPmStaticGroupCfgRowStatus=cadMgmdPmStaticGroupCfgRowStatus, cadMcastMrouteSourceAddress=cadMcastMrouteSourceAddress, cadFqdnCfgGroup=cadFqdnCfgGroup, cadMgmdPmStaticGroupSourceName=cadMgmdPmStaticGroupSourceName, cadMcastForwardDestIfListId=cadMcastForwardDestIfListId, cadDsgIfClassifierCfgRowStatus=cadDsgIfClassifierCfgRowStatus, cadMcastStaticMacIpBindingTable=cadMcastStaticMacIpBindingTable, cadMcastMrouteStatus=cadMcastMrouteStatus, cadMcastStatsTunnelIndex=cadMcastStatsTunnelIndex, cadMcastStatsGSFID=cadMcastStatsGSFID, cadDsgIfClassifierCfgTable=cadDsgIfClassifierCfgTable, cadDsgIfClassifierCfgEntry=cadDsgIfClassifierCfgEntry, cadMgmdPmStaticGroupCfgEntry=cadMgmdPmStaticGroupCfgEntry, cadMcastForwardSourceAddress=cadMcastForwardSourceAddress, cadMcastForwardDestTable=cadMcastForwardDestTable, cadMcastStatsDsIfIndex=cadMcastStatsDsIfIndex, cadMcastStatsDroppedPkts=cadMcastStatsDroppedPkts, cadMcastMrouteTable=cadMcastMrouteTable, cadMcastMrouteSourcePrefix=cadMcastMrouteSourcePrefix, cadMcastMrouteType=cadMcastMrouteType, cadMcastStatsEntry=cadMcastStatsEntry, cadFqdnCacheTable=cadFqdnCacheTable, cadMcastForwardCount=cadMcastForwardCount, cadMcastIgmpThrottleIncrement=cadMcastIgmpThrottleIncrement, cadFqdnCacheIpAddress=cadFqdnCacheIpAddress, cadFqdnCacheEntry=cadFqdnCacheEntry, cadMcastStdMib=cadMcastStdMib, cadMcastForwardDestIfType=cadMcastForwardDestIfType, cadMcastIgmpThrottleInterval=cadMcastIgmpThrottleInterval, cadMcastStaticMacIpBindingAddressType=cadMcastStaticMacIpBindingAddressType, cadDsgIfTunnelChToGroupTable=cadDsgIfTunnelChToGroupTable, cadMcastForwardEntry=cadMcastForwardEntry, cadMcastMrouteEntry=cadMcastMrouteEntry, cadMcastMrouteDistance=cadMcastMrouteDistance, cadMcastForwardDestIfList=cadMcastForwardDestIfList, cadMcastForwardUseDefaultFlow=cadMcastForwardUseDefaultFlow, cadMcastStatsDsid=cadMcastStatsDsid, cadMcastForwardSourceIf=cadMcastForwardSourceIf, cadMgmdPmStaticGroupCfgTable=cadMgmdPmStaticGroupCfgTable, cadMcastClearVideoForwardCounts=cadMcastClearVideoForwardCounts, cadFqdnCacheStatus=cadFqdnCacheStatus, cadMcastStatsSentPkts=cadMcastStatsSentPkts, cadMcastMrouteRpfAddress=cadMcastMrouteRpfAddress, cadMcastStaticMacIpBindingAddress=cadMcastStaticMacIpBindingAddress, cadFqdnCachePollInterval=cadFqdnCachePollInterval, cadMcastForwardDestIf=cadMcastForwardDestIf, cadMcastForwardAddressType=cadMcastForwardAddressType, cadMcastStatsDroppedOctets=cadMcastStatsDroppedOctets, cadMcastGlobals=cadMcastGlobals, cadFqdnCacheEnable=cadFqdnCacheEnable, cadMcastStaticMacIpBindingEntry=cadMcastStaticMacIpBindingEntry, cadMcastIgmpThrottleBurstSize=cadMcastIgmpThrottleBurstSize, cadFqdnCacheFqdn=cadFqdnCacheFqdn, cadMcastStatsTable=cadMcastStatsTable, cadFqdnCacheLastUpdateTime=cadFqdnCacheLastUpdateTime, cadMcastStatsSentOctets=cadMcastStatsSentOctets, cadMcastStatsDsChSetId=cadMcastStatsDsChSetId, cadMcastForwardDestEntry=cadMcastForwardDestEntry, cadDsgIfTunnelGrpIndex=cadDsgIfTunnelGrpIndex, cadMcastClearForwardCounts=cadMcastClearForwardCounts, cadFqdnCacheName=cadFqdnCacheName, cadMcastForwardGroupAddress=cadMcastForwardGroupAddress)
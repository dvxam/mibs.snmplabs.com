#
# PySNMP MIB module HPN-ICF-IPA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-IPA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, iso, Bits, Integer32, Counter64, ObjectIdentity, Gauge32, Unsigned32, TimeTicks, NotificationType, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "iso", "Bits", "Integer32", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "TimeTicks", "NotificationType", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
hpnicfIpa = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25))
if mibBuilder.loadTexts: hpnicfIpa.setLastUpdated('200411010000Z')
if mibBuilder.loadTexts: hpnicfIpa.setOrganization('')
if mibBuilder.loadTexts: hpnicfIpa.setContactInfo('')
if mibBuilder.loadTexts: hpnicfIpa.setDescription(' This MIB is used to acquire ip accounting information. The hpnicfIpaAccountListTable is set by user to define the group of ip address which they want to account. This module can be enabled in each port, which was defined in the hpnicfIpaIfConfigTable. If this module has been enabled, the packets will be accounted when crossing the router from the ports having been enabled by user, according to whether the source/destination ip address is in hpnicfIpaAccountListTable and what kinds of function(in/out/both/fw) are enabled and also whether it is denied by the firewall. If it is denied by the firewall, it will be accounted in hpnicfIpaFWListTable If it is accepted by the firewall, and ip source or ip destination is in hpnicfIpaAccountListTable, it will be accounted in hpnicfIpaIntListTable, otherwise it will be accounted in hpnicfIpaExtListTable. And IP Accounting function also differentiates the packets by direction. If the packet is inbound, the accounting information can be seen as hpnicfIpaIntListInPackets/hpnicfIpaIntListInBytes in hpnicfIpaIntListTable, hpnicfIpaExtListInPackets/hpnicfIpaExtListInBytes in hpnicfIpaExtListTable, hpnicfIpaFWListInPackets/hpnicfIpaFWListInBytes in hpnicfIpaFWListTable. or else the accounting information can be seen as hpnicfIpaIntListOutPackets/hpnicfIpaIntListOutBytes in hpnicfIpaIntListTable, hpnicfIpaExtListOutPackets/hpnicfIpaExtListOutBytes in hpnicfIpaExtListTable, hpnicfIpaFWListOutPackets/hpnicfIpaFWListOutBytes in hpnicfIpaFWListTable. ')
class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub- layer must remain constant at least from one re- initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

hpnicfIpaGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1))
hpnicfIpaGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpaGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaGlobalEnable.setDescription(' The indication of whether Ip Accounting function is enabled. If it is disabled, ip packets will not be accounted. ')
hpnicfIpaTimeOutSeconds = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 2), Integer32().clone(43200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpaTimeOutSeconds.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaTimeOutSeconds.setDescription(' The value of List aging timeout. The unit is second. If exceeding the interval, the item in hpnicfIpaIntListTable, hpnicfIpaExtListTable and hpnicfIpaFWListTable will be removed automaticlly. The range is (3600..604800). ')
hpnicfIpaIntListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 3), Integer32().clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpaIntListMaxItemNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListMaxItemNum.setDescription(' The max number of items in hpnicfIpaIntListTable. The range is (0..16384). ')
hpnicfIpaExtListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpaExtListMaxItemNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListMaxItemNum.setDescription(' The max number of items in hpnicfIpaExtListTable. The range is (0..8192). ')
hpnicfIpaFWListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaFWListMaxItemNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaFWListMaxItemNum.setDescription(' The max number of items in hpnicfIpaFWListTable. ')
hpnicfIpaAccountListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaAccountListMaxItemNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaAccountListMaxItemNum.setDescription(' The max number of items in hpnicfIpaAccountListTable. ')
hpnicfIpaAccountListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaAccountListNextIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaAccountListNextIndex.setDescription(' The next available index for creating rows of hpnicfIpaAccountListTable. If the value is zero, it means the table is full and no available index can be used. ')
hpnicfIpaListCleaningFlag = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("cleaningAll", 2), ("cleaningIntList", 3), ("cleaningExtList", 4), ("cleaningFWList", 5))).clone('idle')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpaListCleaningFlag.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaListCleaningFlag.setDescription(' Cleaning List in this module. The default value is idle. If user wants to clean some lists, he can set the value to 2, 3, 4 and 5 to clean the corresponding list. After the operation, the value will return to idle. ')
hpnicfIpaIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2), )
if mibBuilder.loadTexts: hpnicfIpaIfConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIfConfigTable.setDescription(' Enable or disable the ip accounting inbound/outbound function under a particular interface. ')
hpnicfIpaIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1), ).setIndexNames((0, "HPN-ICF-IPA-MIB", "hpnicfIpaIfConfigIfIndex"))
if mibBuilder.loadTexts: hpnicfIpaIfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIfConfigEntry.setDescription(' Entry of the table. ')
hpnicfIpaIfConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpnicfIpaIfConfigIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIfConfigIfIndex.setDescription('It equals to ifIndex')
hpnicfIpaIfConfigInEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpaIfConfigInEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIfConfigInEnable.setDescription(' This object is applicable to hpnicfIpaIntListTable and hpnicfIpaExtListTable. If the value is disabled, inbound ip packets are not accounted. ')
hpnicfIpaIfConfigOutEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpaIfConfigOutEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIfConfigOutEnable.setDescription(' This object is applicable to hpnicfIpaIntListTable and hpnicfIpaExtListTable. If the value is disabled, outbound ip packets are not accounted. ')
hpnicfIpaIfConfigFWEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nodirection", 1), ("inbound", 2), ("outbound", 3), ("bidirection", 4))).clone('nodirection')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpaIfConfigFWEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIfConfigFWEnable.setDescription(" This object is applicable to hpnicfIpaFWListTable only. If the value is 'inbound', then inbound ip packets which are denied by firewall are accounted. If the value is 'outbound', then outbound ip packets which were denied by firewall are accounted. If the value is 'nodirection', neither inbound nor outbound ip packets which were denied by firewall are accounted. If the value is 'bidirection', both inbound and outbound ip packets which were denied by firewall are accounted. ")
hpnicfIpaAccountListTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3), )
if mibBuilder.loadTexts: hpnicfIpaAccountListTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaAccountListTable.setDescription(' The List is used by user to sort packets into two groups by source or destination ip address. When source/destination ip address of a packet matches a item in this table, the packet is accounted in hpnicfIpaIntListTable. When source/destination ip address of a packet does not match any item in this table, the packet is accounted in hpnicfIpaExtListTable. ')
hpnicfIpaAccountListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1), ).setIndexNames((0, "HPN-ICF-IPA-MIB", "hpnicfIpaAccountListIndex"))
if mibBuilder.loadTexts: hpnicfIpaAccountListEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaAccountListEntry.setDescription(' Entry of the table. ')
hpnicfIpaAccountListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfIpaAccountListIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaAccountListIndex.setDescription(' The Index of the table. ')
hpnicfIpaAccountListIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpaAccountListIpAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaAccountListIpAddr.setDescription(" The IP address to which this entry's addressing information pertains. ")
hpnicfIpaAccountListIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpaAccountListIpMask.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaAccountListIpMask.setDescription(' The subnet mask associated with the IP address of this entry. The value of the mask is an IP address with all the network bits set to 1 and all the hosts bits set to 0. ')
hpnicfIpaAccountListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpaAccountListRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaAccountListRowStatus.setDescription(' The row status of the entry, Supporting CreateAndGo and Destroy operation. ')
hpnicfIpaIntListTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4), )
if mibBuilder.loadTexts: hpnicfIpaIntListTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListTable.setDescription(' If matching the ip address recorded in hpnicfIpaAccountListTable and not denied by the firewall, the packets will be accounted in this list. ')
hpnicfIpaIntListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1), ).setIndexNames((0, "HPN-ICF-IPA-MIB", "hpnicfIpaIntListIpSrc"), (0, "HPN-ICF-IPA-MIB", "hpnicfIpaIntListIpDst"), (0, "HPN-ICF-IPA-MIB", "hpnicfIpaIntListProtocol"))
if mibBuilder.loadTexts: hpnicfIpaIntListEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListEntry.setDescription(' Entry of the table. ')
hpnicfIpaIntListIpSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: hpnicfIpaIntListIpSrc.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListIpSrc.setDescription(' Source IP-address of these accounted packets. ')
hpnicfIpaIntListIpDst = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: hpnicfIpaIntListIpDst.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListIpDst.setDescription(' Destination IP-address of these accounted packets. ')
hpnicfIpaIntListProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hpnicfIpaIntListProtocol.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListProtocol.setDescription(' The type of these accounted IP packets defined in RFC 1700. ')
hpnicfIpaIntListInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaIntListInPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListInPackets.setDescription(' The number of inbound packets in hpnicfIpaIntListTable. ')
hpnicfIpaIntListInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaIntListInBytes.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListInBytes.setDescription(' The number of inbound bytes in hpnicfIpaIntListTable. ')
hpnicfIpaIntListOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaIntListOutPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListOutPackets.setDescription(' The number of outbound Packets in hpnicfIpaIntListTable. ')
hpnicfIpaIntListOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaIntListOutBytes.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaIntListOutBytes.setDescription(' The number of outbound bytes in hpnicfIpaIntListTable. ')
hpnicfIpaExtListTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5), )
if mibBuilder.loadTexts: hpnicfIpaExtListTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListTable.setDescription(' If mismatching the ip address recorded in the hpnicfIpaAccountListTable and not denied by the firewall, the packets will be accounted in this list. ')
hpnicfIpaExtListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1), ).setIndexNames((0, "HPN-ICF-IPA-MIB", "hpnicfIpaExtListIpSrc"), (0, "HPN-ICF-IPA-MIB", "hpnicfIpaExtListIpDst"), (0, "HPN-ICF-IPA-MIB", "hpnicfIpaExtListProtocol"))
if mibBuilder.loadTexts: hpnicfIpaExtListEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListEntry.setDescription(' Entry of the table. ')
hpnicfIpaExtListIpSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: hpnicfIpaExtListIpSrc.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListIpSrc.setDescription(' Source IP-address of these accounted packets. ')
hpnicfIpaExtListIpDst = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: hpnicfIpaExtListIpDst.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListIpDst.setDescription(' Destination IP-address of these accounted packets. ')
hpnicfIpaExtListProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hpnicfIpaExtListProtocol.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListProtocol.setDescription(" The value indicates the value of the 'protocol' field which is part of ip packet header. ")
hpnicfIpaExtListInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaExtListInPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListInPackets.setDescription(' The number of inbound packets in hpnicfIpaExtListTable. ')
hpnicfIpaExtListInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaExtListInBytes.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListInBytes.setDescription(' The number of inbound bytes in hpnicfIpaExtListTable. ')
hpnicfIpaExtListOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaExtListOutPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListOutPackets.setDescription(' The number of outbound packets in hpnicfIpaExtListTable. ')
hpnicfIpaExtListOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaExtListOutBytes.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaExtListOutBytes.setDescription(' The number of outbound bytes in hpnicfIpaExtListTable. ')
hpnicfIpaFWListTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6), )
if mibBuilder.loadTexts: hpnicfIpaFWListTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaFWListTable.setDescription(' If the packet is denied by the firewall, it will be accounted in this list. ')
hpnicfIpaFWListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1), ).setIndexNames((0, "HPN-ICF-IPA-MIB", "hpnicfIpaFWListIpSrc"), (0, "HPN-ICF-IPA-MIB", "hpnicfIpaFWListIpDst"))
if mibBuilder.loadTexts: hpnicfIpaFWListEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaFWListEntry.setDescription(' Entry of the table. ')
hpnicfIpaFWListIpSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: hpnicfIpaFWListIpSrc.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaFWListIpSrc.setDescription(' Source IP-address of these accounted packets. ')
hpnicfIpaFWListIpDst = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: hpnicfIpaFWListIpDst.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaFWListIpDst.setDescription(' Destination IP-address of these accounted packets. ')
hpnicfIpaFWListInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaFWListInPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaFWListInPackets.setDescription(' The number of outbound packets in hpnicfIpaFWListTable. ')
hpnicfIpaFWListInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaFWListInBytes.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaFWListInBytes.setDescription(' The number of inbound bytes in hpnicfIpaFWListTable. ')
hpnicfIpaFWListOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaFWListOutPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaFWListOutPackets.setDescription(' The number of outbound packets in hpnicfIpaFWListTable. ')
hpnicfIpaFWListOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpaFWListOutBytes.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpaFWListOutBytes.setDescription(' The number of outbound bytes in hpnicfIpaFWListTable. ')
mibBuilder.exportSymbols("HPN-ICF-IPA-MIB", hpnicfIpaIntListProtocol=hpnicfIpaIntListProtocol, hpnicfIpaIntListInPackets=hpnicfIpaIntListInPackets, hpnicfIpaAccountListRowStatus=hpnicfIpaAccountListRowStatus, hpnicfIpaIntListEntry=hpnicfIpaIntListEntry, hpnicfIpaAccountListNextIndex=hpnicfIpaAccountListNextIndex, hpnicfIpaIntListTable=hpnicfIpaIntListTable, hpnicfIpaFWListInBytes=hpnicfIpaFWListInBytes, hpnicfIpaFWListOutBytes=hpnicfIpaFWListOutBytes, hpnicfIpaAccountListEntry=hpnicfIpaAccountListEntry, hpnicfIpaIntListIpDst=hpnicfIpaIntListIpDst, hpnicfIpaFWListIpDst=hpnicfIpaFWListIpDst, hpnicfIpaExtListIpSrc=hpnicfIpaExtListIpSrc, hpnicfIpaAccountListMaxItemNum=hpnicfIpaAccountListMaxItemNum, hpnicfIpaExtListMaxItemNum=hpnicfIpaExtListMaxItemNum, hpnicfIpaIfConfigEntry=hpnicfIpaIfConfigEntry, hpnicfIpaFWListEntry=hpnicfIpaFWListEntry, hpnicfIpaIfConfigOutEnable=hpnicfIpaIfConfigOutEnable, hpnicfIpaExtListInPackets=hpnicfIpaExtListInPackets, hpnicfIpaFWListInPackets=hpnicfIpaFWListInPackets, hpnicfIpaIfConfigIfIndex=hpnicfIpaIfConfigIfIndex, hpnicfIpaFWListMaxItemNum=hpnicfIpaFWListMaxItemNum, hpnicfIpaGlobalStats=hpnicfIpaGlobalStats, hpnicfIpa=hpnicfIpa, hpnicfIpaGlobalEnable=hpnicfIpaGlobalEnable, hpnicfIpaExtListInBytes=hpnicfIpaExtListInBytes, hpnicfIpaExtListEntry=hpnicfIpaExtListEntry, hpnicfIpaFWListIpSrc=hpnicfIpaFWListIpSrc, hpnicfIpaFWListOutPackets=hpnicfIpaFWListOutPackets, PYSNMP_MODULE_ID=hpnicfIpa, hpnicfIpaFWListTable=hpnicfIpaFWListTable, hpnicfIpaAccountListIpMask=hpnicfIpaAccountListIpMask, hpnicfIpaExtListProtocol=hpnicfIpaExtListProtocol, hpnicfIpaListCleaningFlag=hpnicfIpaListCleaningFlag, hpnicfIpaAccountListIpAddr=hpnicfIpaAccountListIpAddr, hpnicfIpaExtListOutBytes=hpnicfIpaExtListOutBytes, hpnicfIpaIfConfigInEnable=hpnicfIpaIfConfigInEnable, hpnicfIpaIfConfigTable=hpnicfIpaIfConfigTable, hpnicfIpaIntListMaxItemNum=hpnicfIpaIntListMaxItemNum, InterfaceIndex=InterfaceIndex, hpnicfIpaAccountListIndex=hpnicfIpaAccountListIndex, hpnicfIpaIntListIpSrc=hpnicfIpaIntListIpSrc, hpnicfIpaExtListTable=hpnicfIpaExtListTable, hpnicfIpaExtListOutPackets=hpnicfIpaExtListOutPackets, hpnicfIpaExtListIpDst=hpnicfIpaExtListIpDst, hpnicfIpaTimeOutSeconds=hpnicfIpaTimeOutSeconds, hpnicfIpaIfConfigFWEnable=hpnicfIpaIfConfigFWEnable, hpnicfIpaIntListOutPackets=hpnicfIpaIntListOutPackets, hpnicfIpaIntListInBytes=hpnicfIpaIntListInBytes, hpnicfIpaAccountListTable=hpnicfIpaAccountListTable, hpnicfIpaIntListOutBytes=hpnicfIpaIntListOutBytes)
#
# PySNMP MIB module HH3C-DHCPR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DHCPR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
hh3cRhw, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cRhw")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ModuleIdentity, iso, Counter64, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, TimeTicks, Gauge32, MibIdentifier, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "iso", "Counter64", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "TimeTicks", "Gauge32", "MibIdentifier", "NotificationType", "Bits")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hh3cDHCPRelayMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 1))
hh3cDHCPRelayMib.setRevisions(('2003-02-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cDHCPRelayMib.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cDHCPRelayMib.setLastUpdated('200303010000Z')
if mibBuilder.loadTexts: hh3cDHCPRelayMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cDHCPRelayMib.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cDHCPRelayMib.setDescription('This MIB describes objects used for managing DHCP relay.')
hh3cDHCPRelayMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1))
hh3cDHCPRIPTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cDHCPRIPTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRIPTable.setDescription('A table for configuring ip addresses for DHCP relay')
hh3cDHCPRIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-DHCPR-MIB", "hh3cDHCPRIPAddr"))
if mibBuilder.loadTexts: hh3cDHCPRIPEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRIPEntry.setDescription('An entry for configuring ip addresses for DHCP relay')
hh3cDHCPRIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRIPAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRIPAddr.setDescription('Ip address for DHCP relay')
hh3cDHCPRIPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPRIPRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRIPRowStatus.setDescription('RowStatus. Three actions are used: active, createAndGo, destroy')
hh3cDHCPRSeletAllocateModeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 2), )
if mibBuilder.loadTexts: hh3cDHCPRSeletAllocateModeTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRSeletAllocateModeTable.setDescription('A table for selecting allocation mode of dhcp service')
hh3cDHCPRSeletAllocateModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDHCPRSeletAllocateModeEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRSeletAllocateModeEntry.setDescription('An entry for configuring the allocation mode of DHCP service')
hh3cDHCPRSelectAllocateMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("global", 0), ("interface", 1), ("relay", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPRSelectAllocateMode.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRSelectAllocateMode.setDescription('Allocation mode of DHCP service')
hh3cDHCPRelayCycleStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPRelayCycleStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayCycleStatus.setDescription('Status of DHCP relay cycle mode')
hh3cDHCPRRxBadPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRRxBadPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRRxBadPktNum.setDescription('The total number of the bad packets received by DHCP relay')
hh3cDHCPRRxServerPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRRxServerPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRRxServerPktNum.setDescription('The total number of the packets received from DHCP servers by DHCP relay module')
hh3cDHCPRTxServerPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRTxServerPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRTxServerPktNum.setDescription('The total number of the packets transmited to DHCP servers by DHCP relay module')
hh3cDHCPRRxClientPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRRxClientPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRRxClientPktNum.setDescription('The total number of the packets received form DHCP clients by DHCP relay')
hh3cDHCPRTxClientPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRTxClientPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRTxClientPktNum.setDescription('The total number of the brodcast packets transmited to DHCP clients by DHCP relay')
hh3cDHCPRTxClientUniPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRTxClientUniPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRTxClientUniPktNum.setDescription('The total number of the unicast packets received form DHCP clients by DHCP relay')
hh3cDHCPRTxClientBroPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRTxClientBroPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRTxClientBroPktNum.setDescription('The total number of the brodcast packets received form DHCP clients by DHCP relay')
hh3cDHCPRelayDiscoverPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayDiscoverPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayDiscoverPktNum.setDescription('The total number of the DHCP Discover packets handled by DHCP relay')
hh3cDHCPRelayRequestPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayRequestPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayRequestPktNum.setDescription('The total number of the DHCP Request packets handled by DHCP relay')
hh3cDHCPRelayDeclinePktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayDeclinePktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayDeclinePktNum.setDescription('The total number of the DHCP Decline packets handled by DHCP relay')
hh3cDHCPRelayReleasePktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayReleasePktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayReleasePktNum.setDescription('The total number of the DHCP Release packets handled by DHCP relay')
hh3cDHCPRelayInformPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayInformPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayInformPktNum.setDescription('The total number of the DHCP Inform packets handled by DHCP relay')
hh3cDHCPRelayOfferPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayOfferPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayOfferPktNum.setDescription('The total number of the DHCP Offer packets handled by DHCP server')
hh3cDHCPRelayAckPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayAckPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayAckPktNum.setDescription('The total number of the DHCP Ack packets handled by DHCP relay')
hh3cDHCPRelayNakPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayNakPktNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayNakPktNum.setDescription('The total number of the DHCP Nak packets handled by DHCP relay')
hh3cDHCPRelayStatisticsReset = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPRelayStatisticsReset.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayStatisticsReset.setDescription('Reset the above statictics information of handled packets by DHCP relay')
hh3cDHCPRelayMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 1, 2))
hh3cDHCPRelayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 1, 2, 1))
hh3cDHCPRelayMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 1, 2, 2))
hh3cDHCPRelayMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 8, 1, 2, 2, 1)).setObjects(("HH3C-DHCPR-MIB", "hh3cDHCPRIPAddr"), ("HH3C-DHCPR-MIB", "hh3cDHCPRIPRowStatus"), ("HH3C-DHCPR-MIB", "hh3cDHCPRSelectAllocateMode"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayCycleStatus"), ("HH3C-DHCPR-MIB", "hh3cDHCPRRxBadPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRRxServerPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRTxServerPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRRxClientPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRTxClientPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRTxClientUniPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRTxClientBroPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayDiscoverPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayRequestPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayDeclinePktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayReleasePktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayInformPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayOfferPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayAckPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayNakPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayStatisticsReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cDHCPRelayMIBGroup = hh3cDHCPRelayMIBGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPRelayMIBGroup.setDescription('The basic collection of objects providing management of DHCP realy.')
mibBuilder.exportSymbols("HH3C-DHCPR-MIB", hh3cDHCPRIPAddr=hh3cDHCPRIPAddr, hh3cDHCPRelayInformPktNum=hh3cDHCPRelayInformPktNum, hh3cDHCPRelayMIBCompliances=hh3cDHCPRelayMIBCompliances, hh3cDHCPRIPRowStatus=hh3cDHCPRIPRowStatus, hh3cDHCPRSeletAllocateModeTable=hh3cDHCPRSeletAllocateModeTable, hh3cDHCPRelayNakPktNum=hh3cDHCPRelayNakPktNum, PYSNMP_MODULE_ID=hh3cDHCPRelayMib, hh3cDHCPRelayMIBGroups=hh3cDHCPRelayMIBGroups, hh3cDHCPRTxServerPktNum=hh3cDHCPRTxServerPktNum, hh3cDHCPRelayMib=hh3cDHCPRelayMib, hh3cDHCPRTxClientBroPktNum=hh3cDHCPRTxClientBroPktNum, hh3cDHCPRSeletAllocateModeEntry=hh3cDHCPRSeletAllocateModeEntry, hh3cDHCPRelayAckPktNum=hh3cDHCPRelayAckPktNum, hh3cDHCPRSelectAllocateMode=hh3cDHCPRSelectAllocateMode, hh3cDHCPRelayDeclinePktNum=hh3cDHCPRelayDeclinePktNum, hh3cDHCPRRxClientPktNum=hh3cDHCPRRxClientPktNum, hh3cDHCPRelayMibObject=hh3cDHCPRelayMibObject, hh3cDHCPRTxClientUniPktNum=hh3cDHCPRTxClientUniPktNum, hh3cDHCPRRxBadPktNum=hh3cDHCPRRxBadPktNum, hh3cDHCPRelayRequestPktNum=hh3cDHCPRelayRequestPktNum, hh3cDHCPRelayOfferPktNum=hh3cDHCPRelayOfferPktNum, hh3cDHCPRelayReleasePktNum=hh3cDHCPRelayReleasePktNum, hh3cDHCPRelayStatisticsReset=hh3cDHCPRelayStatisticsReset, hh3cDHCPRelayCycleStatus=hh3cDHCPRelayCycleStatus, hh3cDHCPRelayMIBGroup=hh3cDHCPRelayMIBGroup, hh3cDHCPRIPEntry=hh3cDHCPRIPEntry, hh3cDHCPRTxClientPktNum=hh3cDHCPRTxClientPktNum, hh3cDHCPRIPTable=hh3cDHCPRIPTable, hh3cDHCPRelayDiscoverPktNum=hh3cDHCPRelayDiscoverPktNum, hh3cDHCPRRxServerPktNum=hh3cDHCPRRxServerPktNum, hh3cDHCPRelayMIBConformance=hh3cDHCPRelayMIBConformance)

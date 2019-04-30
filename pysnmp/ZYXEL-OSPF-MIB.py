#
# PySNMP MIB module ZYXEL-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-OSPF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ospfLsdbLsid, ospfLsdbType, ospfVirtIfNeighbor, ospfNbrAddressLessIndex, ospfLsdbAreaId, ospfAddressLessIf, ospfVirtIfAreaId, ospfLsdbRouterId, ospfIfIpAddress, ospfAreaId, ospfNbrIpAddr = mibBuilder.importSymbols("OSPF-MIB", "ospfLsdbLsid", "ospfLsdbType", "ospfVirtIfNeighbor", "ospfNbrAddressLessIndex", "ospfLsdbAreaId", "ospfAddressLessIf", "ospfVirtIfAreaId", "ospfLsdbRouterId", "ospfIfIpAddress", "ospfAreaId", "ospfNbrIpAddr")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Bits, ObjectIdentity, MibIdentifier, Counter64, Integer32, Unsigned32, IpAddress, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Bits", "ObjectIdentity", "MibIdentifier", "Counter64", "Integer32", "Unsigned32", "IpAddress", "NotificationType", "iso")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelOspf = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57))
if mibBuilder.loadTexts: zyxelOspf.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelOspf.setOrganization('Enterprise Solution ZyXEL')
zyxelOspfSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1))
zyxelOspfStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2))
zyxelOspfIfTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 1), )
if mibBuilder.loadTexts: zyxelOspfIfTable.setStatus('current')
zyxelOspfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 1, 1), ).setIndexNames((0, "OSPF-MIB", "ospfIfIpAddress"), (0, "OSPF-MIB", "ospfAddressLessIf"))
if mibBuilder.loadTexts: zyxelOspfIfEntry.setStatus('current')
zyOspfIfKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOspfIfKeyId.setStatus('current')
zyxelOspfAreaTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 2), )
if mibBuilder.loadTexts: zyxelOspfAreaTable.setStatus('current')
zyxelOspfAreaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 2, 1), ).setIndexNames((0, "OSPF-MIB", "ospfAreaId"))
if mibBuilder.loadTexts: zyxelOspfAreaEntry.setStatus('current')
zyOspfAreaName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 2, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOspfAreaName.setStatus('current')
zyxelOspfRedistributeRouteTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3), )
if mibBuilder.loadTexts: zyxelOspfRedistributeRouteTable.setStatus('current')
zyxelOspfRedistributeRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1), ).setIndexNames((0, "ZYXEL-OSPF-MIB", "zyOspfRedistributeRouteProtocol"))
if mibBuilder.loadTexts: zyxelOspfRedistributeRouteEntry.setStatus('current')
zyOspfRedistributeRouteProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rip", 1), ("static", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfRedistributeRouteProtocol.setStatus('current')
zyOspfRedistributeRouteState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOspfRedistributeRouteState.setStatus('current')
zyOspfRedistributeRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOspfRedistributeRouteType.setStatus('current')
zyOspfRedistributeRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOspfRedistributeRouteMetric.setStatus('current')
zyxelOspfVirtualLinkTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 4), )
if mibBuilder.loadTexts: zyxelOspfVirtualLinkTable.setStatus('current')
zyxelOspfVirtualLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 4, 1), ).setIndexNames((0, "OSPF-MIB", "ospfVirtIfAreaId"), (0, "OSPF-MIB", "ospfVirtIfNeighbor"))
if mibBuilder.loadTexts: zyxelOspfVirtualLinkEntry.setStatus('current')
zyOspfVirtualLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 4, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOspfVirtualLinkName.setStatus('current')
zyOspfVirtualLinkKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOspfVirtualLinkKeyId.setStatus('current')
zyOspfMaxNumberOfSummaryAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfMaxNumberOfSummaryAddress.setStatus('current')
zyxelOspfSummaryAddressTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6), )
if mibBuilder.loadTexts: zyxelOspfSummaryAddressTable.setStatus('current')
zyxelOspfSummaryAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6, 1), ).setIndexNames((0, "ZYXEL-OSPF-MIB", "zyOspfSummaryAddressIpAddress"), (0, "ZYXEL-OSPF-MIB", "zyOspfSummaryAddressMaskBits"))
if mibBuilder.loadTexts: zyxelOspfSummaryAddressEntry.setStatus('current')
zyOspfSummaryAddressIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: zyOspfSummaryAddressIpAddress.setStatus('current')
zyOspfSummaryAddressMaskBits = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfSummaryAddressMaskBits.setStatus('current')
zyOspfSummaryAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyOspfSummaryAddressRowStatus.setStatus('current')
zyxelOspfGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 7))
zyOspfDistance = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 7, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOspfDistance.setStatus('current')
zyxelOspfIfInfoTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1), )
if mibBuilder.loadTexts: zyxelOspfIfInfoTable.setStatus('current')
zyxelOspfIfInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1), ).setIndexNames((0, "OSPF-MIB", "ospfIfIpAddress"), (0, "OSPF-MIB", "ospfAddressLessIf"))
if mibBuilder.loadTexts: zyxelOspfIfInfoEntry.setStatus('current')
zyOspfIfInfoMaskbits = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfIfInfoMaskbits.setStatus('current')
zyOspfIfInfoDesignatedRouterID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfIfInfoDesignatedRouterID.setStatus('current')
zyOspfIfInfoBackupDesignatedRouterID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfIfInfoBackupDesignatedRouterID.setStatus('current')
zyOspfIfInfoNbrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfIfInfoNbrCount.setStatus('current')
zyOspfIfInfoAdjacentNbrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfIfInfoAdjacentNbrCount.setStatus('current')
zyOspfIfInfoHelloDueTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfIfInfoHelloDueTime.setStatus('current')
zyxelOspfNbrTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2), )
if mibBuilder.loadTexts: zyxelOspfNbrTable.setStatus('current')
zyxelOspfNbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1), ).setIndexNames((0, "OSPF-MIB", "ospfNbrIpAddr"), (0, "OSPF-MIB", "ospfNbrAddressLessIndex"))
if mibBuilder.loadTexts: zyxelOspfNbrEntry.setStatus('current')
zyOspfNbrRole = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dr", 1), ("backup", 2), ("drOther", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfNbrRole.setStatus('current')
zyOspfNbrDeadtime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfNbrDeadtime.setStatus('current')
zyOspfNbrInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfNbrInterface.setStatus('current')
zyOspfNbrRetransmitLSA = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfNbrRetransmitLSA.setStatus('current')
zyOspfNbrRequestLSA = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfNbrRequestLSA.setStatus('current')
zyOspfNbrDatabaseSummaryLSA = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfNbrDatabaseSummaryLSA.setStatus('current')
zyxelOspfLsdbTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3), )
if mibBuilder.loadTexts: zyxelOspfLsdbTable.setStatus('current')
zyxelOspfLsdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3, 1), ).setIndexNames((0, "OSPF-MIB", "ospfLsdbAreaId"), (0, "OSPF-MIB", "ospfLsdbType"), (0, "OSPF-MIB", "ospfLsdbLsid"), (0, "OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: zyxelOspfLsdbEntry.setStatus('current')
zyOspfLsdbLinkCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfLsdbLinkCount.setStatus('current')
zyOspfLsdbRouteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfLsdbRouteIpAddress.setStatus('current')
zyOspfLsdbRouteMaskBits = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyOspfLsdbRouteMaskBits.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-OSPF-MIB", zyOspfIfKeyId=zyOspfIfKeyId, zyxelOspfGeneralGroup=zyxelOspfGeneralGroup, zyxelOspf=zyxelOspf, zyOspfRedistributeRouteMetric=zyOspfRedistributeRouteMetric, zyxelOspfNbrTable=zyxelOspfNbrTable, zyOspfSummaryAddressMaskBits=zyOspfSummaryAddressMaskBits, zyxelOspfAreaEntry=zyxelOspfAreaEntry, zyOspfIfInfoDesignatedRouterID=zyOspfIfInfoDesignatedRouterID, zyOspfMaxNumberOfSummaryAddress=zyOspfMaxNumberOfSummaryAddress, zyxelOspfNbrEntry=zyxelOspfNbrEntry, zyOspfIfInfoNbrCount=zyOspfIfInfoNbrCount, zyxelOspfLsdbTable=zyxelOspfLsdbTable, zyxelOspfSummaryAddressEntry=zyxelOspfSummaryAddressEntry, zyxelOspfRedistributeRouteTable=zyxelOspfRedistributeRouteTable, zyOspfNbrRetransmitLSA=zyOspfNbrRetransmitLSA, zyOspfIfInfoBackupDesignatedRouterID=zyOspfIfInfoBackupDesignatedRouterID, zyOspfLsdbRouteMaskBits=zyOspfLsdbRouteMaskBits, zyOspfSummaryAddressIpAddress=zyOspfSummaryAddressIpAddress, zyOspfRedistributeRouteState=zyOspfRedistributeRouteState, zyOspfIfInfoMaskbits=zyOspfIfInfoMaskbits, zyxelOspfIfInfoEntry=zyxelOspfIfInfoEntry, zyxelOspfRedistributeRouteEntry=zyxelOspfRedistributeRouteEntry, zyOspfAreaName=zyOspfAreaName, zyOspfVirtualLinkKeyId=zyOspfVirtualLinkKeyId, zyOspfNbrDeadtime=zyOspfNbrDeadtime, zyxelOspfIfEntry=zyxelOspfIfEntry, zyxelOspfLsdbEntry=zyxelOspfLsdbEntry, zyOspfLsdbLinkCount=zyOspfLsdbLinkCount, zyOspfDistance=zyOspfDistance, zyOspfNbrDatabaseSummaryLSA=zyOspfNbrDatabaseSummaryLSA, zyxelOspfVirtualLinkEntry=zyxelOspfVirtualLinkEntry, zyxelOspfSummaryAddressTable=zyxelOspfSummaryAddressTable, zyxelOspfSetup=zyxelOspfSetup, zyOspfSummaryAddressRowStatus=zyOspfSummaryAddressRowStatus, zyOspfNbrInterface=zyOspfNbrInterface, zyOspfLsdbRouteIpAddress=zyOspfLsdbRouteIpAddress, zyOspfRedistributeRouteProtocol=zyOspfRedistributeRouteProtocol, zyOspfNbrRole=zyOspfNbrRole, zyOspfIfInfoAdjacentNbrCount=zyOspfIfInfoAdjacentNbrCount, zyxelOspfAreaTable=zyxelOspfAreaTable, zyOspfIfInfoHelloDueTime=zyOspfIfInfoHelloDueTime, zyOspfVirtualLinkName=zyOspfVirtualLinkName, PYSNMP_MODULE_ID=zyxelOspf, zyOspfNbrRequestLSA=zyOspfNbrRequestLSA, zyxelOspfIfInfoTable=zyxelOspfIfInfoTable, zyxelOspfIfTable=zyxelOspfIfTable, zyxelOspfVirtualLinkTable=zyxelOspfVirtualLinkTable, zyOspfRedistributeRouteType=zyOspfRedistributeRouteType, zyxelOspfStatus=zyxelOspfStatus)

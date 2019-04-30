#
# PySNMP MIB module WAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WAN
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, iso, Bits, Gauge32, ModuleIdentity, Counter32, MibIdentifier, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, IpAddress, ObjectIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Bits", "Gauge32", "ModuleIdentity", "Counter32", "MibIdentifier", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "IpAddress", "ObjectIdentity", "enterprises")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
pepwave = MibIdentifier((1, 3, 6, 1, 4, 1, 27662))
wan_status = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 2)).setLabel("wan-status")
if mibBuilder.loadTexts: wan_status.setLastUpdated('201303050000Z')
if mibBuilder.loadTexts: wan_status.setOrganization('PEPWAVE')
class PortSpeedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("auto", 1), ("fullDulplex10", 2), ("halfDulplex10", 3), ("fullDulplex100", 4), ("halfDulplex100", 5), ("fullDulplex1000", 6), ("halfDulplex1000", 7))

wanStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 2, 1))
wanNum = MibScalar((1, 3, 6, 1, 4, 1, 27662, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNum.setStatus('current')
wanTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 2, 1, 2), )
if mibBuilder.loadTexts: wanTable.setStatus('current')
wanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1), ).setIndexNames((0, "WAN", "wanId"))
if mibBuilder.loadTexts: wanEntry.setStatus('current')
wanId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanId.setStatus('current')
wanName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanName.setStatus('current')
wanState = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("disabled", 1), ("disconnected", 2), ("connected", 3), ("connecting", 4), ("activating", 5), ("health-check-fail", 6), ("disconnected-manually", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanState.setStatus('current')
wanHealthCheckState = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("fail", 0), ("success", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanHealthCheckState.setStatus('current')
wanSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanSignal.setStatus('current')
wanCellID = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanCellID.setStatus('current')
wanPdpConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("pdp-ip", 1), ("pdp-ppp", 2), ("pdp-ipv6", 3), ("pdp-ipv4v6", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanPdpConnection.setStatus('current')
wanNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3))
wanNetworkIpTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1), )
if mibBuilder.loadTexts: wanNetworkIpTable.setStatus('current')
wanNetworkIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1), ).setIndexNames((0, "WAN", "wanId"), (0, "WAN", "wanNetworkIpId"))
if mibBuilder.loadTexts: wanNetworkIpEntry.setStatus('current')
wanNetworkIpId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkIpId.setStatus('current')
wanNetworkIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("dhcp", 0), ("static", 1), ("pppoe", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkIpType.setStatus('current')
wanNetworkIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkIpAddress.setStatus('current')
wanNetworkSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkSubnetMask.setStatus('current')
wanNetworkDnsTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 2), )
if mibBuilder.loadTexts: wanNetworkDnsTable.setStatus('current')
wanNetworkDnsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 2, 1), ).setIndexNames((0, "WAN", "wanId"), (0, "WAN", "wanNetworkDnsId"))
if mibBuilder.loadTexts: wanNetworkDnsEntry.setStatus('current')
wanNetworkDnsId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkDnsId.setStatus('current')
wanNetworkDnsServer = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkDnsServer.setStatus('current')
wanNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 3), )
if mibBuilder.loadTexts: wanNetworkTable.setStatus('current')
wanNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 3, 1), ).setIndexNames((0, "WAN", "wanId"))
if mibBuilder.loadTexts: wanNetworkEntry.setStatus('current')
wanNetworkGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkGateway.setStatus('current')
wanDataUsageTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 2, 1, 4), )
if mibBuilder.loadTexts: wanDataUsageTable.setStatus('current')
wanDataUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 2, 1, 4, 1), ).setIndexNames((0, "WAN", "wanId"), (0, "WAN", "dataTypeID"))
if mibBuilder.loadTexts: wanDataUsageEntry.setStatus('current')
dataTypeID = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("daily", 0), ("monthly", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataTypeID.setStatus('current')
wanDataUsageTxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 4, 1, 2), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: wanDataUsageTxByte.setStatus('current')
wanDataUsageRxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 4, 1, 3), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: wanDataUsageRxByte.setStatus('current')
portWanSpeedTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 2, 1, 5), )
if mibBuilder.loadTexts: portWanSpeedTable.setStatus('current')
portWanSpeedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 2, 1, 5, 1), ).setIndexNames((0, "WAN", "portWanSpeedIndex"))
if mibBuilder.loadTexts: portWanSpeedEntry.setStatus('current')
portWanSpeedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portWanSpeedIndex.setStatus('current')
portWanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 2, 1, 5, 1, 2), PortSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portWanSpeed.setStatus('current')
mibBuilder.exportSymbols("WAN", PortSpeedType=PortSpeedType, wanNetworkDnsId=wanNetworkDnsId, portWanSpeed=portWanSpeed, PYSNMP_MODULE_ID=wan_status, wanNetworkIpType=wanNetworkIpType, portWanSpeedEntry=portWanSpeedEntry, wanNetworkGateway=wanNetworkGateway, wanStatus=wanStatus, wanDataUsageTable=wanDataUsageTable, wanState=wanState, wanId=wanId, dataTypeID=dataTypeID, wanNetworkDnsTable=wanNetworkDnsTable, wanNetworkIpEntry=wanNetworkIpEntry, wan_status=wan_status, wanName=wanName, wanDataUsageEntry=wanDataUsageEntry, wanNetwork=wanNetwork, wanNetworkIpTable=wanNetworkIpTable, wanPdpConnection=wanPdpConnection, wanNetworkIpId=wanNetworkIpId, wanSignal=wanSignal, wanNetworkTable=wanNetworkTable, wanNetworkEntry=wanNetworkEntry, wanNetworkSubnetMask=wanNetworkSubnetMask, wanTable=wanTable, portWanSpeedIndex=portWanSpeedIndex, wanHealthCheckState=wanHealthCheckState, wanNetworkDnsEntry=wanNetworkDnsEntry, wanNetworkDnsServer=wanNetworkDnsServer, wanNum=wanNum, wanNetworkIpAddress=wanNetworkIpAddress, wanEntry=wanEntry, portWanSpeedTable=portWanSpeedTable, wanDataUsageTxByte=wanDataUsageTxByte, wanDataUsageRxByte=wanDataUsageRxByte, pepwave=pepwave, wanCellID=wanCellID)

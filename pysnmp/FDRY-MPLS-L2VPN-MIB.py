#
# PySNMP MIB module FDRY-MPLS-L2VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-MPLS-L2VPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
snMpls, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "snMpls")
PortPriorityTC, VlanTagMode = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "PortPriorityTC", "VlanTagMode")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
pwEnetPwInstance, = mibBuilder.importSymbols("PW-ENET-STD-MIB", "pwEnetPwInstance")
pwName, pwIndex, pwID = mibBuilder.importSymbols("PW-STD-MIB", "pwName", "pwIndex", "pwID")
PwOperStatusTC, = mibBuilder.importSymbols("PW-TC-STD-MIB", "PwOperStatusTC")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Bits, Counter32, Counter64, iso, Gauge32, IpAddress, ObjectIdentity, TimeTicks, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Bits", "Counter32", "Counter64", "iso", "Gauge32", "IpAddress", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
vplsConfigName, vplsConfigEntry, vplsConfigIndex = mibBuilder.importSymbols("VPLS-GENERIC-MIB", "vplsConfigName", "vplsConfigEntry", "vplsConfigIndex")
fdryMplsL2VpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2))
fdryMplsL2VpnMIB.setRevisions(('2012-04-04 00:00', '2010-06-02 00:00', '2008-02-07 00:00',))
if mibBuilder.loadTexts: fdryMplsL2VpnMIB.setLastUpdated('201204040000Z')
if mibBuilder.loadTexts: fdryMplsL2VpnMIB.setOrganization('Brocade Communications Systems, Inc.')
class MplsServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vll", 1), ("vllLocal", 2), ("vpls", 3))

class AdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3))

class ClassOfService(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )
class Layer2StateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("preforwarding", 5), ("forwarding", 6))

class FdryPwServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vll", 1), ("vllLocal", 2), ("vpls", 3))

class PwVlanCfg(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4097)

fdryMplsVpnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0))
fdryMplsVllInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1))
fdryMplsVplsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2))
brcdVplsScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 5))
fdryVllEndPointTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1), )
if mibBuilder.loadTexts: fdryVllEndPointTable.setStatus('current')
fdryVllEndPointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1), ).setIndexNames((0, "FDRY-MPLS-L2VPN-MIB", "fdryVllEndPointServiceType"), (0, "PW-STD-MIB", "pwIndex"), (0, "PW-ENET-STD-MIB", "pwEnetPwInstance"))
if mibBuilder.loadTexts: fdryVllEndPointEntry.setStatus('current')
fdryVllEndPointServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 1), MplsServiceType())
if mibBuilder.loadTexts: fdryVllEndPointServiceType.setStatus('current')
fdryVllEndPointVlanTagMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 2), VlanTagMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVllEndPointVlanTagMode.setStatus('current')
fdryVllEndPointClassOfService = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 3), ClassOfService()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVllEndPointClassOfService.setStatus('current')
fdryVllEndPointInHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVllEndPointInHCPkts.setStatus('current')
fdryVllEndPointOutHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVllEndPointOutHCPkts.setStatus('current')
fdryVllEndPointAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 6), AdminStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVllEndPointAdminStatus.setStatus('current')
fdryVllEndPointOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 7), PwOperStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVllEndPointOperStatus.setStatus('current')
fdryVllEndPointRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVllEndPointRowStatus.setStatus('current')
fdryVllEndPointInnerVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 9), PwVlanCfg()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVllEndPointInnerVlanId.setStatus('current')
fdryVllEndPointInHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVllEndPointInHCOctets.setStatus('current')
fdryVllEndPointOutHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVllEndPointOutHCOctets.setStatus('current')
brcdVllEndptVlanExtStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2), )
if mibBuilder.loadTexts: brcdVllEndptVlanExtStatsTable.setStatus('current')
brcdVllEndptVlanExtStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1), ).setIndexNames((0, "FDRY-MPLS-L2VPN-MIB", "fdryVllEndPointServiceType"), (0, "PW-STD-MIB", "pwIndex"), (0, "PW-ENET-STD-MIB", "pwEnetPwInstance"), (0, "FDRY-MPLS-L2VPN-MIB", "brcdVllEndptVlanExtStatsPriorityId"))
if mibBuilder.loadTexts: brcdVllEndptVlanExtStatsEntry.setStatus('current')
brcdVllEndptVlanExtStatsPriorityId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 1), PortPriorityTC())
if mibBuilder.loadTexts: brcdVllEndptVlanExtStatsPriorityId.setStatus('current')
brcdVllEndptVlanExtStatsInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVllEndptVlanExtStatsInPkts.setStatus('current')
brcdVllEndptVlanExtStatsOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVllEndptVlanExtStatsOutPkts.setStatus('current')
brcdVllEndptVlanExtStatsInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVllEndptVlanExtStatsInOctets.setStatus('current')
brcdVllEndptVlanExtStatsOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVllEndptVlanExtStatsOutOctets.setStatus('current')
fdryVplsEndPointTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1), )
if mibBuilder.loadTexts: fdryVplsEndPointTable.setStatus('deprecated')
fdryVplsEndPointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPointPortVlan"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPointIfIndex"))
if mibBuilder.loadTexts: fdryVplsEndPointEntry.setStatus('deprecated')
fdryVplsEndPointPortVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 1), PwVlanCfg())
if mibBuilder.loadTexts: fdryVplsEndPointPortVlan.setStatus('deprecated')
fdryVplsEndPointIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: fdryVplsEndPointIfIndex.setStatus('deprecated')
fdryVplsEndPointVlanTagMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 3), VlanTagMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVplsEndPointVlanTagMode.setStatus('deprecated')
fdryVplsEndPointOutHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVplsEndPointOutHCPkts.setStatus('deprecated')
fdryVplsEndPointState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 5))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("forwarding", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVplsEndPointState.setStatus('deprecated')
fdryVplsEndPointAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 6), AdminStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVplsEndPointAdminStatus.setStatus('deprecated')
fdryVplsEndPointOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 7), PwOperStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVplsEndPointOperStatus.setStatus('deprecated')
fdryVplsEndPointRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVplsEndPointRowStatus.setStatus('deprecated')
fdryVplsEndPointInHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVplsEndPointInHCOctets.setStatus('deprecated')
fdryVplsEndPoint2Table = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3), )
if mibBuilder.loadTexts: fdryVplsEndPoint2Table.setStatus('current')
fdryVplsEndPoint2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2VlanId"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTagType"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTag"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2IfIndex"))
if mibBuilder.loadTexts: fdryVplsEndPoint2Entry.setStatus('current')
fdryVplsEndPoint2VlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 1), PwVlanCfg())
if mibBuilder.loadTexts: fdryVplsEndPoint2VlanId.setStatus('current')
fdryVplsEndPoint2InnerTagType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("innerVlan", 2), ("isid", 3))))
if mibBuilder.loadTexts: fdryVplsEndPoint2InnerTagType.setStatus('current')
fdryVplsEndPoint2InnerTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: fdryVplsEndPoint2InnerTag.setStatus('current')
fdryVplsEndPoint2IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: fdryVplsEndPoint2IfIndex.setStatus('current')
fdryVplsEndPoint2VlanTagMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 5), VlanTagMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVplsEndPoint2VlanTagMode.setStatus('current')
fdryVplsEndPoint2InHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVplsEndPoint2InHCOctets.setStatus('current')
fdryVplsEndPoint2Layer2State = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 7), Layer2StateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVplsEndPoint2Layer2State.setStatus('current')
fdryVplsEndPoint2OperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 8), PwOperStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVplsEndPoint2OperStatus.setStatus('current')
fdryVplsEndPoint2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVplsEndPoint2RowStatus.setStatus('current')
fdryVplsTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2), )
if mibBuilder.loadTexts: fdryVplsTable.setStatus('current')
fdryVplsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1), )
vplsConfigEntry.registerAugmentions(("FDRY-MPLS-L2VPN-MIB", "fdryVplsEntry"))
fdryVplsEntry.setIndexNames(*vplsConfigEntry.getIndexNames())
if mibBuilder.loadTexts: fdryVplsEntry.setStatus('current')
fdryVplsClassOfService = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 1), ClassOfService()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVplsClassOfService.setStatus('current')
fdryVplsMaxMacLearned = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVplsMaxMacLearned.setStatus('current')
fdryVplsClearMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryVplsClearMac.setStatus('current')
fdryVplsVcId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryVplsVcId.setStatus('current')
brcdVplsEndptVlanExtStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4), )
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsTable.setStatus('current')
brcdVplsEndptVlanExtStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2VlanId"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTagType"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTag"), (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2IfIndex"), (0, "FDRY-MPLS-L2VPN-MIB", "brcdVplsEndptVlanExtStatsPriorityId"))
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsEntry.setStatus('current')
brcdVplsEndptVlanExtStatsPriorityId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 1), PortPriorityTC())
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsPriorityId.setStatus('current')
brcdVplsEndptVlanExtStatsInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsInPkts.setStatus('current')
brcdVplsEndptVlanExtStatsOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsOutPkts.setStatus('current')
brcdVplsEndptVlanExtStatsInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsInOctets.setStatus('current')
brcdVplsEndptVlanExtStatsOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsOutOctets.setStatus('current')
brcdVplsEndptVlanExtStatsRoutedInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsRoutedInPkts.setStatus('current')
brcdVplsEndptVlanExtStatsRoutedOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsRoutedOutPkts.setStatus('current')
brcdVplsEndptVlanExtStatsRoutedInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsRoutedInOctets.setStatus('current')
brcdVplsEndptVlanExtStatsRoutedOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsRoutedOutOctets.setStatus('current')
brcdVplsEndptVlanExtStatsSwitchedInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsSwitchedInPkts.setStatus('current')
brcdVplsEndptVlanExtStatsSwitchedOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsSwitchedOutPkts.setStatus('current')
brcdVplsEndptVlanExtStatsSwitchedInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsSwitchedInOctets.setStatus('current')
brcdVplsEndptVlanExtStatsSwitchedOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdVplsEndptVlanExtStatsSwitchedOutOctets.setStatus('current')
brcdVplsMacAgeTimeLocal = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 5, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdVplsMacAgeTimeLocal.setStatus('current')
brcdVplsMacAgeTimeRemote = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 5, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdVplsMacAgeTimeRemote.setStatus('current')
fdryVplsCreated = NotificationType((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0, 1)).setObjects(("VPLS-GENERIC-MIB", "vplsConfigName"), ("FDRY-MPLS-L2VPN-MIB", "fdryVplsVcId"))
if mibBuilder.loadTexts: fdryVplsCreated.setStatus('current')
fdryVplsDeleted = NotificationType((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0, 2)).setObjects(("VPLS-GENERIC-MIB", "vplsConfigName"), ("FDRY-MPLS-L2VPN-MIB", "fdryVplsVcId"))
if mibBuilder.loadTexts: fdryVplsDeleted.setStatus('current')
fdryPwCreated = NotificationType((1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0, 3)).setObjects(("FDRY-MPLS-L2VPN-MIB", "fdryPwServiceType"), ("PW-STD-MIB", "pwName"), ("PW-STD-MIB", "pwID"))
if mibBuilder.loadTexts: fdryPwCreated.setStatus('current')
mibBuilder.exportSymbols("FDRY-MPLS-L2VPN-MIB", fdryVplsEntry=fdryVplsEntry, fdryVplsTable=fdryVplsTable, fdryVplsEndPoint2VlanTagMode=fdryVplsEndPoint2VlanTagMode, fdryVllEndPointOutHCPkts=fdryVllEndPointOutHCPkts, fdryVplsEndPoint2InnerTagType=fdryVplsEndPoint2InnerTagType, brcdVplsEndptVlanExtStatsRoutedOutPkts=brcdVplsEndptVlanExtStatsRoutedOutPkts, fdryVllEndPointOperStatus=fdryVllEndPointOperStatus, fdryVplsEndPointIfIndex=fdryVplsEndPointIfIndex, brcdVplsEndptVlanExtStatsTable=brcdVplsEndptVlanExtStatsTable, brcdVllEndptVlanExtStatsEntry=brcdVllEndptVlanExtStatsEntry, brcdVllEndptVlanExtStatsPriorityId=brcdVllEndptVlanExtStatsPriorityId, fdryVplsEndPoint2InnerTag=fdryVplsEndPoint2InnerTag, brcdVplsEndptVlanExtStatsOutOctets=brcdVplsEndptVlanExtStatsOutOctets, fdryVplsEndPoint2RowStatus=fdryVplsEndPoint2RowStatus, fdryVllEndPointAdminStatus=fdryVllEndPointAdminStatus, fdryVllEndPointInHCOctets=fdryVllEndPointInHCOctets, fdryVplsEndPoint2IfIndex=fdryVplsEndPoint2IfIndex, brcdVplsEndptVlanExtStatsOutPkts=brcdVplsEndptVlanExtStatsOutPkts, brcdVllEndptVlanExtStatsOutPkts=brcdVllEndptVlanExtStatsOutPkts, fdryVplsEndPointState=fdryVplsEndPointState, fdryVplsEndPoint2VlanId=fdryVplsEndPoint2VlanId, fdryMplsL2VpnMIB=fdryMplsL2VpnMIB, fdryVplsEndPointRowStatus=fdryVplsEndPointRowStatus, brcdVplsEndptVlanExtStatsEntry=brcdVplsEndptVlanExtStatsEntry, AdminStatus=AdminStatus, fdryVplsVcId=fdryVplsVcId, fdryVplsEndPointVlanTagMode=fdryVplsEndPointVlanTagMode, fdryVllEndPointOutHCOctets=fdryVllEndPointOutHCOctets, ClassOfService=ClassOfService, fdryVplsEndPointOutHCPkts=fdryVplsEndPointOutHCPkts, fdryVplsEndPointEntry=fdryVplsEndPointEntry, brcdVplsEndptVlanExtStatsRoutedInPkts=brcdVplsEndptVlanExtStatsRoutedInPkts, brcdVplsEndptVlanExtStatsSwitchedOutOctets=brcdVplsEndptVlanExtStatsSwitchedOutOctets, fdryVllEndPointServiceType=fdryVllEndPointServiceType, fdryVplsEndPoint2Layer2State=fdryVplsEndPoint2Layer2State, fdryVplsEndPoint2Entry=fdryVplsEndPoint2Entry, fdryVplsEndPoint2OperStatus=fdryVplsEndPoint2OperStatus, brcdVplsEndptVlanExtStatsInOctets=brcdVplsEndptVlanExtStatsInOctets, fdryMplsVpnNotifications=fdryMplsVpnNotifications, PwVlanCfg=PwVlanCfg, brcdVplsEndptVlanExtStatsRoutedOutOctets=brcdVplsEndptVlanExtStatsRoutedOutOctets, Layer2StateTC=Layer2StateTC, brcdVllEndptVlanExtStatsInPkts=brcdVllEndptVlanExtStatsInPkts, brcdVplsEndptVlanExtStatsRoutedInOctets=brcdVplsEndptVlanExtStatsRoutedInOctets, brcdVplsScalarObjects=brcdVplsScalarObjects, PYSNMP_MODULE_ID=fdryMplsL2VpnMIB, brcdVplsMacAgeTimeLocal=brcdVplsMacAgeTimeLocal, fdryVplsEndPointInHCOctets=fdryVplsEndPointInHCOctets, fdryVllEndPointEntry=fdryVllEndPointEntry, fdryVllEndPointInHCPkts=fdryVllEndPointInHCPkts, fdryMplsVllInfo=fdryMplsVllInfo, fdryVplsCreated=fdryVplsCreated, fdryVplsEndPoint2InHCOctets=fdryVplsEndPoint2InHCOctets, fdryVllEndPointTable=fdryVllEndPointTable, fdryVplsEndPointOperStatus=fdryVplsEndPointOperStatus, fdryPwCreated=fdryPwCreated, fdryVllEndPointInnerVlanId=fdryVllEndPointInnerVlanId, fdryVplsEndPointAdminStatus=fdryVplsEndPointAdminStatus, brcdVplsEndptVlanExtStatsSwitchedOutPkts=brcdVplsEndptVlanExtStatsSwitchedOutPkts, brcdVllEndptVlanExtStatsOutOctets=brcdVllEndptVlanExtStatsOutOctets, fdryVllEndPointVlanTagMode=fdryVllEndPointVlanTagMode, fdryVplsDeleted=fdryVplsDeleted, fdryVplsEndPointTable=fdryVplsEndPointTable, brcdVllEndptVlanExtStatsTable=brcdVllEndptVlanExtStatsTable, fdryVplsEndPointPortVlan=fdryVplsEndPointPortVlan, brcdVplsEndptVlanExtStatsPriorityId=brcdVplsEndptVlanExtStatsPriorityId, FdryPwServiceType=FdryPwServiceType, brcdVplsEndptVlanExtStatsSwitchedInPkts=brcdVplsEndptVlanExtStatsSwitchedInPkts, fdryVplsClearMac=fdryVplsClearMac, fdryMplsVplsInfo=fdryMplsVplsInfo, brcdVplsEndptVlanExtStatsInPkts=brcdVplsEndptVlanExtStatsInPkts, fdryVplsEndPoint2Table=fdryVplsEndPoint2Table, fdryVllEndPointRowStatus=fdryVllEndPointRowStatus, fdryVllEndPointClassOfService=fdryVllEndPointClassOfService, fdryVplsMaxMacLearned=fdryVplsMaxMacLearned, MplsServiceType=MplsServiceType, brcdVplsMacAgeTimeRemote=brcdVplsMacAgeTimeRemote, brcdVplsEndptVlanExtStatsSwitchedInOctets=brcdVplsEndptVlanExtStatsSwitchedInOctets, fdryVplsClassOfService=fdryVplsClassOfService, brcdVllEndptVlanExtStatsInOctets=brcdVllEndptVlanExtStatsInOctets)

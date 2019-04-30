#
# PySNMP MIB module HIRSCHMANN-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HIRSCHMANN-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:18:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
hmPlatform4, = mibBuilder.importSymbols("HIRSCHMANN-MMP4-BASICL2-MIB", "hmPlatform4")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Counter32, IpAddress, Counter64, MibIdentifier, Unsigned32, ObjectIdentity, Integer32, NotificationType, Gauge32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter32", "IpAddress", "Counter64", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Integer32", "NotificationType", "Gauge32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hmPlatform4Multicast = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 15, 4))
hmPlatform4Multicast.setRevisions(('2006-02-03 12:00', '2002-05-08 14:18',))
if mibBuilder.loadTexts: hmPlatform4Multicast.setLastUpdated('200602031200Z')
if mibBuilder.loadTexts: hmPlatform4Multicast.setOrganization('Hirschmann Automation and Control GmbH')
hmAgentMulticastIGMPConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 1))
hmAgentMulticastIGMPAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastIGMPAdminMode.setStatus('current')
hmAgentMulticastIGMPInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 1, 2), )
if mibBuilder.loadTexts: hmAgentMulticastIGMPInterfaceTable.setStatus('obsolete')
hmAgentMulticastIGMPInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 1, 2, 1), ).setIndexNames((0, "HIRSCHMANN-MULTICAST-MIB", "hmAgentMulticastIGMPInterfaceIfIndex"))
if mibBuilder.loadTexts: hmAgentMulticastIGMPInterfaceEntry.setStatus('obsolete')
hmAgentMulticastIGMPInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmAgentMulticastIGMPInterfaceIfIndex.setStatus('obsolete')
hmAgentMulticastIGMPInterfaceAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastIGMPInterfaceAdminMode.setStatus('obsolete')
hmAgentMulticastIGMPSoftwareDSCP = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 1, 210), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64)).clone(48)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastIGMPSoftwareDSCP.setStatus('current')
hmAgentMulticastPIMConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 2))
hmAgentMulticastPIMConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sparse", 1), ("dense", 2))).clone('dense')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastPIMConfigMode.setStatus('obsolete')
hmAgentMulticastPIMPruneHoldtime = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 64800)).clone(210)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastPIMPruneHoldtime.setStatus('obsolete')
hmAgentMulticastPIMSMConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 3))
hmAgentMulticastPIMSMAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastPIMSMAdminMode.setStatus('current')
hmAgentMulticastPIMSMDataThresholdRate = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastPIMSMDataThresholdRate.setStatus('current')
hmAgentMulticastPIMSMRegThresholdRate = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastPIMSMRegThresholdRate.setStatus('current')
hmAgentMulticastPIMSMStaticRPTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 4), )
if mibBuilder.loadTexts: hmAgentMulticastPIMSMStaticRPTable.setStatus('obsolete')
hmAgentMulticastPIMSMStaticRPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 4, 1), ).setIndexNames((0, "HIRSCHMANN-MULTICAST-MIB", "hmAgentMulticastPIMSMStaticRPIpAddr"), (0, "HIRSCHMANN-MULTICAST-MIB", "hmAgentMulticastPIMSMStaticRPGroupIpAddr"), (0, "HIRSCHMANN-MULTICAST-MIB", "hmAgentMulticastPIMSMStaticRPGroupIpMask"))
if mibBuilder.loadTexts: hmAgentMulticastPIMSMStaticRPEntry.setStatus('obsolete')
hmAgentMulticastPIMSMStaticRPIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmAgentMulticastPIMSMStaticRPIpAddr.setStatus('obsolete')
hmAgentMulticastPIMSMStaticRPGroupIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmAgentMulticastPIMSMStaticRPGroupIpAddr.setStatus('obsolete')
hmAgentMulticastPIMSMStaticRPGroupIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 4, 1, 3), IpAddress())
if mibBuilder.loadTexts: hmAgentMulticastPIMSMStaticRPGroupIpMask.setStatus('obsolete')
hmAgentMulticastPIMSMStaticRPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmAgentMulticastPIMSMStaticRPStatus.setStatus('obsolete')
hmAgentMulticastPIMSMInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 5), )
if mibBuilder.loadTexts: hmAgentMulticastPIMSMInterfaceTable.setStatus('obsolete')
hmAgentMulticastPIMSMInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 5, 1), ).setIndexNames((0, "HIRSCHMANN-MULTICAST-MIB", "hmAgentMulticastPIMSMInterfaceIndex"))
if mibBuilder.loadTexts: hmAgentMulticastPIMSMInterfaceEntry.setStatus('obsolete')
hmAgentMulticastPIMSMInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hmAgentMulticastPIMSMInterfaceIndex.setStatus('obsolete')
hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength.setStatus('obsolete')
hmAgentMulticastPIMSMInterfaceCRPPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 3, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastPIMSMInterfaceCRPPreference.setStatus('obsolete')
hmAgentMulticastPIMDMConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 4))
hmAgentMulticastPIMDMAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastPIMDMAdminMode.setStatus('current')
hmAgentMulticastRoutingConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 5))
hmAgentMulticastRoutingAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastRoutingAdminMode.setStatus('current')
hmAgentMulticastDVMRPConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 6))
hmAgentMulticastDVMRPAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentMulticastDVMRPAdminMode.setStatus('current')
hmAgentSnmpTrapFlagsConfigGroupMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 7))
hmAgentSnmpDVMRPTrapFlag = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentSnmpDVMRPTrapFlag.setStatus('current')
hmAgentSnmpPIMTrapFlag = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmAgentSnmpPIMTrapFlag.setStatus('current')
hmAgentIpStaticMRouteTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 8), )
if mibBuilder.loadTexts: hmAgentIpStaticMRouteTable.setStatus('current')
hmAgentIpStaticMRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 8, 1), ).setIndexNames((0, "HIRSCHMANN-MULTICAST-MIB", "hmAgentIpStaticMRouteSrcAddressType"), (0, "HIRSCHMANN-MULTICAST-MIB", "hmAgentIpStaticMRouteSrcIpAddr"), (0, "HIRSCHMANN-MULTICAST-MIB", "hmAgentIpStaticMRouteSrcNetMask"))
if mibBuilder.loadTexts: hmAgentIpStaticMRouteEntry.setStatus('current')
hmAgentIpStaticMRouteSrcAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 8, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hmAgentIpStaticMRouteSrcAddressType.setStatus('current')
hmAgentIpStaticMRouteSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 8, 1, 2), InetAddress())
if mibBuilder.loadTexts: hmAgentIpStaticMRouteSrcIpAddr.setStatus('current')
hmAgentIpStaticMRouteSrcNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: hmAgentIpStaticMRouteSrcNetMask.setStatus('current')
hmAgentIpStaticMRouteRpfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 8, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmAgentIpStaticMRouteRpfIpAddr.setStatus('current')
hmAgentIpStaticMRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 8, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmAgentIpStaticMRouteIfIndex.setStatus('current')
hmAgentIpStaticMRoutePreference = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 8, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmAgentIpStaticMRoutePreference.setStatus('current')
hmAgentIpStaticMRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 8, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmAgentIpStaticMRouteStatus.setStatus('current')
mibBuilder.exportSymbols("HIRSCHMANN-MULTICAST-MIB", hmAgentMulticastPIMConfigGroup=hmAgentMulticastPIMConfigGroup, hmAgentIpStaticMRouteStatus=hmAgentIpStaticMRouteStatus, hmAgentMulticastPIMSMStaticRPGroupIpMask=hmAgentMulticastPIMSMStaticRPGroupIpMask, hmAgentMulticastPIMPruneHoldtime=hmAgentMulticastPIMPruneHoldtime, hmAgentMulticastPIMSMInterfaceCRPPreference=hmAgentMulticastPIMSMInterfaceCRPPreference, hmAgentMulticastIGMPInterfaceTable=hmAgentMulticastIGMPInterfaceTable, hmAgentIpStaticMRouteIfIndex=hmAgentIpStaticMRouteIfIndex, hmAgentIpStaticMRouteSrcIpAddr=hmAgentIpStaticMRouteSrcIpAddr, hmAgentMulticastRoutingConfigGroup=hmAgentMulticastRoutingConfigGroup, hmAgentMulticastPIMConfigMode=hmAgentMulticastPIMConfigMode, hmAgentMulticastDVMRPAdminMode=hmAgentMulticastDVMRPAdminMode, hmAgentMulticastIGMPSoftwareDSCP=hmAgentMulticastIGMPSoftwareDSCP, hmAgentIpStaticMRouteTable=hmAgentIpStaticMRouteTable, hmAgentIpStaticMRouteEntry=hmAgentIpStaticMRouteEntry, hmAgentMulticastPIMSMDataThresholdRate=hmAgentMulticastPIMSMDataThresholdRate, hmAgentMulticastPIMSMInterfaceTable=hmAgentMulticastPIMSMInterfaceTable, hmAgentMulticastRoutingAdminMode=hmAgentMulticastRoutingAdminMode, hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength=hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength, hmAgentMulticastPIMSMStaticRPEntry=hmAgentMulticastPIMSMStaticRPEntry, hmAgentMulticastPIMDMConfigGroup=hmAgentMulticastPIMDMConfigGroup, hmAgentMulticastDVMRPConfigGroup=hmAgentMulticastDVMRPConfigGroup, hmAgentMulticastPIMSMInterfaceEntry=hmAgentMulticastPIMSMInterfaceEntry, hmAgentIpStaticMRoutePreference=hmAgentIpStaticMRoutePreference, hmPlatform4Multicast=hmPlatform4Multicast, hmAgentMulticastPIMSMAdminMode=hmAgentMulticastPIMSMAdminMode, hmAgentMulticastIGMPInterfaceAdminMode=hmAgentMulticastIGMPInterfaceAdminMode, hmAgentMulticastIGMPInterfaceIfIndex=hmAgentMulticastIGMPInterfaceIfIndex, hmAgentMulticastPIMSMConfigGroup=hmAgentMulticastPIMSMConfigGroup, hmAgentMulticastPIMSMStaticRPGroupIpAddr=hmAgentMulticastPIMSMStaticRPGroupIpAddr, hmAgentSnmpTrapFlagsConfigGroupMulticast=hmAgentSnmpTrapFlagsConfigGroupMulticast, PYSNMP_MODULE_ID=hmPlatform4Multicast, hmAgentSnmpPIMTrapFlag=hmAgentSnmpPIMTrapFlag, hmAgentIpStaticMRouteSrcNetMask=hmAgentIpStaticMRouteSrcNetMask, hmAgentMulticastPIMSMRegThresholdRate=hmAgentMulticastPIMSMRegThresholdRate, hmAgentMulticastPIMSMStaticRPIpAddr=hmAgentMulticastPIMSMStaticRPIpAddr, hmAgentMulticastPIMSMStaticRPStatus=hmAgentMulticastPIMSMStaticRPStatus, hmAgentMulticastPIMDMAdminMode=hmAgentMulticastPIMDMAdminMode, hmAgentMulticastIGMPInterfaceEntry=hmAgentMulticastIGMPInterfaceEntry, hmAgentMulticastIGMPAdminMode=hmAgentMulticastIGMPAdminMode, hmAgentMulticastPIMSMStaticRPTable=hmAgentMulticastPIMSMStaticRPTable, hmAgentMulticastPIMSMInterfaceIndex=hmAgentMulticastPIMSMInterfaceIndex, hmAgentMulticastIGMPConfigGroup=hmAgentMulticastIGMPConfigGroup, hmAgentSnmpDVMRPTrapFlag=hmAgentSnmpDVMRPTrapFlag, hmAgentIpStaticMRouteSrcAddressType=hmAgentIpStaticMRouteSrcAddressType, hmAgentIpStaticMRouteRpfIpAddr=hmAgentIpStaticMRouteRpfIpAddr)

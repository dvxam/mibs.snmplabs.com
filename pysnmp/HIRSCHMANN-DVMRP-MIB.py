#
# PySNMP MIB module HIRSCHMANN-DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HIRSCHMANN-DVMRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:18:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
hmPlatform4Multicast, = mibBuilder.importSymbols("HIRSCHMANN-MULTICAST-MIB", "hmPlatform4Multicast")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, iso, Counter32, IpAddress, Counter64, MibIdentifier, Unsigned32, ObjectIdentity, Integer32, NotificationType, Gauge32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter32", "IpAddress", "Counter64", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Integer32", "NotificationType", "Gauge32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hmDVMRPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 15, 4, 100))
hmDVMRPMIB.setRevisions(('2010-04-12 12:00',))
if mibBuilder.loadTexts: hmDVMRPMIB.setLastUpdated('201004121200Z')
if mibBuilder.loadTexts: hmDVMRPMIB.setOrganization('Hirschmann Automation and Control GmbH')
hmDVMRPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1))
hmDVMRP = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1))
hmDVMRPScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1))
hmDVMRPVersionString = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPVersionString.setStatus('current')
hmDVMRPGenerationId = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPGenerationId.setStatus('obsolete')
hmDVMRPNumRoutes = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNumRoutes.setStatus('current')
hmDVMRPReachableRoutes = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPReachableRoutes.setStatus('current')
hmDVMRPUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmDVMRPUpdateInterval.setStatus('current')
hmDVMRPPruneLifetime = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 64800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmDVMRPPruneLifetime.setStatus('current')
hmDVMRPInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2), )
if mibBuilder.loadTexts: hmDVMRPInterfaceTable.setStatus('current')
hmDVMRPInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceIfIndex"))
if mibBuilder.loadTexts: hmDVMRPInterfaceEntry.setStatus('current')
hmDVMRPInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hmDVMRPInterfaceIfIndex.setStatus('current')
hmDVMRPInterfaceLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceLocalAddress.setStatus('current')
hmDVMRPInterfaceMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDVMRPInterfaceMetric.setStatus('current')
hmDVMRPInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDVMRPInterfaceStatus.setStatus('current')
hmDVMRPInterfaceRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceRcvBadPkts.setStatus('current')
hmDVMRPInterfaceRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceRcvBadRoutes.setStatus('current')
hmDVMRPInterfaceSentRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceSentRoutes.setStatus('current')
hmDVMRPInterfaceInterfaceKey = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 8), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDVMRPInterfaceInterfaceKey.setStatus('current')
hmDVMRPInterfaceInterfaceKeyVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDVMRPInterfaceInterfaceKeyVersion.setStatus('current')
hmDVMRPInterfaceGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPInterfaceGenerationId.setStatus('current')
hmDVMRPNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3), )
if mibBuilder.loadTexts: hmDVMRPNeighborTable.setStatus('current')
hmDVMRPNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborIfIndex"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborAddress"))
if mibBuilder.loadTexts: hmDVMRPNeighborEntry.setStatus('current')
hmDVMRPNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hmDVMRPNeighborIfIndex.setStatus('current')
hmDVMRPNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmDVMRPNeighborAddress.setStatus('current')
hmDVMRPNeighborUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborUpTime.setStatus('current')
hmDVMRPNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborExpiryTime.setStatus('current')
hmDVMRPNeighborGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborGenerationId.setStatus('current')
hmDVMRPNeighborMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborMajorVersion.setStatus('current')
hmDVMRPNeighborMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborMinorVersion.setStatus('current')
hmDVMRPNeighborCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 8), Bits().clone(namedValues=NamedValues(("leaf", 0), ("prune", 1), ("generationID", 2), ("mtrace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborCapabilities.setStatus('current')
hmDVMRPNeighborRcvRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborRcvRoutes.setStatus('current')
hmDVMRPNeighborRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborRcvBadPkts.setStatus('current')
hmDVMRPNeighborRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborRcvBadRoutes.setStatus('current')
hmDVMRPNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oneway", 1), ("active", 2), ("ignoring", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPNeighborState.setStatus('current')
hmDVMRPRouteTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4), )
if mibBuilder.loadTexts: hmDVMRPRouteTable.setStatus('current')
hmDVMRPRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteSource"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteSourceMask"))
if mibBuilder.loadTexts: hmDVMRPRouteEntry.setStatus('current')
hmDVMRPRouteSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmDVMRPRouteSource.setStatus('current')
hmDVMRPRouteSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmDVMRPRouteSourceMask.setStatus('current')
hmDVMRPRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteUpstreamNeighbor.setStatus('current')
hmDVMRPRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteIfIndex.setStatus('current')
hmDVMRPRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteMetric.setStatus('current')
hmDVMRPRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteExpiryTime.setStatus('current')
hmDVMRPRouteUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteUpTime.setStatus('current')
hmDVMRPRouteNextHopTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5), )
if mibBuilder.loadTexts: hmDVMRPRouteNextHopTable.setStatus('current')
hmDVMRPRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopSource"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopSourceMask"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopIfIndex"))
if mibBuilder.loadTexts: hmDVMRPRouteNextHopEntry.setStatus('current')
hmDVMRPRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmDVMRPRouteNextHopSource.setStatus('current')
hmDVMRPRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmDVMRPRouteNextHopSourceMask.setStatus('current')
hmDVMRPRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: hmDVMRPRouteNextHopIfIndex.setStatus('current')
hmDVMRPRouteNextHopType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leaf", 1), ("branch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPRouteNextHopType.setStatus('current')
hmDVMRPPruneTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6), )
if mibBuilder.loadTexts: hmDVMRPPruneTable.setStatus('current')
hmDVMRPPruneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1), ).setIndexNames((0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneGroup"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneSource"), (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneSourceMask"))
if mibBuilder.loadTexts: hmDVMRPPruneEntry.setStatus('current')
hmDVMRPPruneGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmDVMRPPruneGroup.setStatus('current')
hmDVMRPPruneSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmDVMRPPruneSource.setStatus('current')
hmDVMRPPruneSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: hmDVMRPPruneSourceMask.setStatus('current')
hmDVMRPPruneExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDVMRPPruneExpiryTime.setStatus('current')
hmDVMRPTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 7))
hmDVMRPNeighborLoss = NotificationType((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 7, 1)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceLocalAddress"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborState"))
if mibBuilder.loadTexts: hmDVMRPNeighborLoss.setStatus('current')
hmDVMRPNeighborNotPruning = NotificationType((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 7, 2)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceLocalAddress"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborCapabilities"))
if mibBuilder.loadTexts: hmDVMRPNeighborNotPruning.setStatus('current')
hmDVMRPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2))
hmDVMRPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 1))
hmDVMRPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2))
hmDVMRPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 1, 1)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPGeneralGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRoutingGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPTreeGroup"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPSecurityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPMIBCompliance = hmDVMRPMIBCompliance.setStatus('current')
hmDVMRPGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 2)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPVersionString"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPGenerationId"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNumRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPReachableRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPGeneralGroup = hmDVMRPGeneralGroup.setStatus('current')
hmDVMRPInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 3)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceLocalAddress"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceMetric"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceStatus"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceRcvBadPkts"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceRcvBadRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceSentRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceGenerationId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPInterfaceGroup = hmDVMRPInterfaceGroup.setStatus('current')
hmDVMRPNeighborGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 4)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborUpTime"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborExpiryTime"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborGenerationId"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborMajorVersion"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborMinorVersion"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborCapabilities"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborRcvRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborRcvBadPkts"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborRcvBadRoutes"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPNeighborGroup = hmDVMRPNeighborGroup.setStatus('current')
hmDVMRPRoutingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 5)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteUpstreamNeighbor"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteIfIndex"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteMetric"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteExpiryTime"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteUpTime"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPRoutingGroup = hmDVMRPRoutingGroup.setStatus('current')
hmDVMRPSecurityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 6)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceInterfaceKey"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceInterfaceKeyVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPSecurityGroup = hmDVMRPSecurityGroup.setStatus('current')
hmDVMRPTreeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 7)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPTreeGroup = hmDVMRPTreeGroup.setStatus('current')
hmDVMRPNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 8)).setObjects(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborLoss"), ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborNotPruning"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmDVMRPNotificationGroup = hmDVMRPNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HIRSCHMANN-DVMRP-MIB", hmDVMRPPruneLifetime=hmDVMRPPruneLifetime, hmDVMRPInterfaceInterfaceKey=hmDVMRPInterfaceInterfaceKey, hmDVMRPNeighborRcvRoutes=hmDVMRPNeighborRcvRoutes, hmDVMRPRouteExpiryTime=hmDVMRPRouteExpiryTime, hmDVMRPScalar=hmDVMRPScalar, hmDVMRPUpdateInterval=hmDVMRPUpdateInterval, hmDVMRPRouteNextHopType=hmDVMRPRouteNextHopType, hmDVMRPNeighborUpTime=hmDVMRPNeighborUpTime, hmDVMRP=hmDVMRP, hmDVMRPNeighborGenerationId=hmDVMRPNeighborGenerationId, hmDVMRPRouteUpstreamNeighbor=hmDVMRPRouteUpstreamNeighbor, hmDVMRPNeighborMajorVersion=hmDVMRPNeighborMajorVersion, hmDVMRPRouteUpTime=hmDVMRPRouteUpTime, hmDVMRPMIB=hmDVMRPMIB, hmDVMRPInterfaceInterfaceKeyVersion=hmDVMRPInterfaceInterfaceKeyVersion, hmDVMRPNeighborMinorVersion=hmDVMRPNeighborMinorVersion, hmDVMRPPruneGroup=hmDVMRPPruneGroup, hmDVMRPInterfaceRcvBadRoutes=hmDVMRPInterfaceRcvBadRoutes, hmDVMRPNeighborGroup=hmDVMRPNeighborGroup, hmDVMRPGeneralGroup=hmDVMRPGeneralGroup, hmDVMRPNumRoutes=hmDVMRPNumRoutes, hmDVMRPRouteNextHopSourceMask=hmDVMRPRouteNextHopSourceMask, hmDVMRPMIBCompliances=hmDVMRPMIBCompliances, hmDVMRPReachableRoutes=hmDVMRPReachableRoutes, hmDVMRPRouteSourceMask=hmDVMRPRouteSourceMask, hmDVMRPPruneTable=hmDVMRPPruneTable, hmDVMRPPruneExpiryTime=hmDVMRPPruneExpiryTime, hmDVMRPInterfaceGroup=hmDVMRPInterfaceGroup, hmDVMRPRouteTable=hmDVMRPRouteTable, hmDVMRPNotificationGroup=hmDVMRPNotificationGroup, hmDVMRPMIBObjects=hmDVMRPMIBObjects, hmDVMRPInterfaceStatus=hmDVMRPInterfaceStatus, hmDVMRPRouteIfIndex=hmDVMRPRouteIfIndex, hmDVMRPNeighborCapabilities=hmDVMRPNeighborCapabilities, hmDVMRPNeighborEntry=hmDVMRPNeighborEntry, hmDVMRPRouteSource=hmDVMRPRouteSource, hmDVMRPRouteMetric=hmDVMRPRouteMetric, hmDVMRPVersionString=hmDVMRPVersionString, hmDVMRPPruneSource=hmDVMRPPruneSource, hmDVMRPMIBConformance=hmDVMRPMIBConformance, hmDVMRPNeighborAddress=hmDVMRPNeighborAddress, hmDVMRPNeighborIfIndex=hmDVMRPNeighborIfIndex, hmDVMRPInterfaceLocalAddress=hmDVMRPInterfaceLocalAddress, hmDVMRPNeighborLoss=hmDVMRPNeighborLoss, hmDVMRPSecurityGroup=hmDVMRPSecurityGroup, hmDVMRPTraps=hmDVMRPTraps, hmDVMRPMIBCompliance=hmDVMRPMIBCompliance, hmDVMRPNeighborState=hmDVMRPNeighborState, hmDVMRPNeighborNotPruning=hmDVMRPNeighborNotPruning, hmDVMRPInterfaceMetric=hmDVMRPInterfaceMetric, hmDVMRPRouteNextHopEntry=hmDVMRPRouteNextHopEntry, hmDVMRPInterfaceIfIndex=hmDVMRPInterfaceIfIndex, hmDVMRPPruneEntry=hmDVMRPPruneEntry, hmDVMRPInterfaceTable=hmDVMRPInterfaceTable, hmDVMRPRouteNextHopTable=hmDVMRPRouteNextHopTable, hmDVMRPTreeGroup=hmDVMRPTreeGroup, hmDVMRPInterfaceRcvBadPkts=hmDVMRPInterfaceRcvBadPkts, PYSNMP_MODULE_ID=hmDVMRPMIB, hmDVMRPInterfaceGenerationId=hmDVMRPInterfaceGenerationId, hmDVMRPInterfaceEntry=hmDVMRPInterfaceEntry, hmDVMRPPruneSourceMask=hmDVMRPPruneSourceMask, hmDVMRPMIBGroups=hmDVMRPMIBGroups, hmDVMRPGenerationId=hmDVMRPGenerationId, hmDVMRPRouteEntry=hmDVMRPRouteEntry, hmDVMRPNeighborRcvBadRoutes=hmDVMRPNeighborRcvBadRoutes, hmDVMRPRouteNextHopSource=hmDVMRPRouteNextHopSource, hmDVMRPInterfaceSentRoutes=hmDVMRPInterfaceSentRoutes, hmDVMRPRouteNextHopIfIndex=hmDVMRPRouteNextHopIfIndex, hmDVMRPRoutingGroup=hmDVMRPRoutingGroup, hmDVMRPNeighborExpiryTime=hmDVMRPNeighborExpiryTime, hmDVMRPNeighborRcvBadPkts=hmDVMRPNeighborRcvBadPkts, hmDVMRPNeighborTable=hmDVMRPNeighborTable)

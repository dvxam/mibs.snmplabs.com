#
# PySNMP MIB module Juniper-DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DVMRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:02:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
junidDvmrpInterfaceEntry, = mibBuilder.importSymbols("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceEntry")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, NotificationType, TimeTicks, ModuleIdentity, Counter64, Unsigned32, ObjectIdentity, Integer32, MibIdentifier, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "TimeTicks", "ModuleIdentity", "Counter64", "Unsigned32", "ObjectIdentity", "Integer32", "MibIdentifier", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
juniDvmrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44))
juniDvmrpMIB.setRevisions(('2003-01-16 20:55', '2001-11-30 21:24',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDvmrpMIB.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names. Added support for unicast routing and the interface announce list name.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniDvmrpMIB.setLastUpdated('200301162055Z')
if mibBuilder.loadTexts: juniDvmrpMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDvmrpMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniDvmrpMIB.setDescription('The Enterprise MIB module for management of Juniper DVMRP routers.')
juniDvmrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1))
juniDvmrp = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1))
juniDvmrpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1))
juniDvmrpAdminState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDvmrpAdminState.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAdminState.setDescription('Controls whether DVMRP is enabled or not.')
juniDvmrpMcastAdminState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDvmrpMcastAdminState.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpMcastAdminState.setDescription('Whether multicast is enabled or not. This is settable via the multicast component.')
juniDvmrpRouteHogNotification = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 134217727))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDvmrpRouteHogNotification.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpRouteHogNotification.setDescription('The number of routes allowed within a 1 minute interval before a trap is issued warning that there may be a route surge going on.')
juniDvmrpRouteLimit = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 134217727))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDvmrpRouteLimit.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpRouteLimit.setDescription('The limit on the number of routes that may be advertised on a DVMRP interface.')
juniDvmrpS32PrunesOnly = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDvmrpS32PrunesOnly.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpS32PrunesOnly.setDescription('Identifies when DVMRP is sending prunes and grafts with only a 32 bit source masks.')
juniDvmrpUnicastRouting = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDvmrpUnicastRouting.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpUnicastRouting.setDescription('Enable/disable the unicast routing portion of the DVMRP.')
juniDvmrpAclDistNbrTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2), )
if mibBuilder.loadTexts: juniDvmrpAclDistNbrTable.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAclDistNbrTable.setDescription('The (conceptual) table listing the access lists distance for a list of neighbors.')
juniDvmrpAclDistNbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1), ).setIndexNames((0, "Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrIfIndex"), (0, "Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrAclListName"))
if mibBuilder.loadTexts: juniDvmrpAclDistNbrEntry.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAclDistNbrEntry.setDescription('An entry (conceptual row) in the juniDvmrpAclDistNbrTable.')
juniDvmrpAclDistNbrIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniDvmrpAclDistNbrIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAclDistNbrIfIndex.setDescription('The ifIndex value of the interface for which DVMRP is enabled.')
juniDvmrpAclDistNbrAclListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80)))
if mibBuilder.loadTexts: juniDvmrpAclDistNbrAclListName.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAclDistNbrAclListName.setDescription('The name of the access list to be used in the filter.')
juniDvmrpAclDistNbrDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpAclDistNbrDistance.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAclDistNbrDistance.setDescription('The administritive distance metric that will be used')
juniDvmrpAclDistNbrNbrListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpAclDistNbrNbrListName.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAclDistNbrNbrListName.setDescription('This is the access list of nbrs for this accept-filter to be applied, this field must be supplied when the row is created')
juniDvmrpAclDistNbrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpAclDistNbrStatus.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAclDistNbrStatus.setDescription('The status of this entry.')
juniDvmrpLocalAddrTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3), )
if mibBuilder.loadTexts: juniDvmrpLocalAddrTable.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpLocalAddrTable.setDescription('The (conceptual) table listing the local addresses. This is used to retrive all of the addresses configured on a DVMRP interface.')
juniDvmrpLocalAddrTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1), ).setIndexNames((0, "Juniper-DVMRP-MIB", "juniDvmrpLocalAddrIfIndex"), (0, "Juniper-DVMRP-MIB", "juniDvmrpLocalAddrAddrOrIfIndex"))
if mibBuilder.loadTexts: juniDvmrpLocalAddrTableEntry.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpLocalAddrTableEntry.setDescription('An entry (conceptual row) in the juniDvmrpLocalAddrTable.')
juniDvmrpLocalAddrIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniDvmrpLocalAddrIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpLocalAddrIfIndex.setDescription('The ifIndex value of the interface for which DVMRP is enabled.')
juniDvmrpLocalAddrAddrOrIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: juniDvmrpLocalAddrAddrOrIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpLocalAddrAddrOrIfIndex.setDescription('For unnumbered interfaces, this takes on the value of the ifIndex. For numbered interfaces, this is the address of one of the addresses associated with the interface.')
juniDvmrpLocalAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDvmrpLocalAddrMask.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpLocalAddrMask.setDescription('The IP Address mask associated with this entry.')
juniDvmrpSummaryAddrTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4), )
if mibBuilder.loadTexts: juniDvmrpSummaryAddrTable.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSummaryAddrTable.setDescription('The (conceptual) table listing the DVMRP summary addresses. This is used to retrive all of the summary address configured on a DVMRP interface.')
juniDvmrpSummaryAddrTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1), ).setIndexNames((0, "Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrIfIndex"), (0, "Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrAddress"), (0, "Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrMask"))
if mibBuilder.loadTexts: juniDvmrpSummaryAddrTableEntry.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSummaryAddrTableEntry.setDescription('An entry (conceptual row) in the juniDvmrpSummaryAddrTable.')
juniDvmrpSummaryAddrIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniDvmrpSummaryAddrIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSummaryAddrIfIndex.setDescription('The ifIndex value of the interface for which DVMRP is enabled.')
juniDvmrpSummaryAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: juniDvmrpSummaryAddrAddress.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSummaryAddrAddress.setDescription('This is the summary address that will be created.')
juniDvmrpSummaryAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 3), IpAddress())
if mibBuilder.loadTexts: juniDvmrpSummaryAddrMask.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSummaryAddrMask.setDescription('The mask of the summary address to be created.')
juniDvmrpSummaryAddrCost = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpSummaryAddrCost.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSummaryAddrCost.setDescription('The administritive distance metric used to actually calculate distance vectors.')
juniDvmrpSummaryAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpSummaryAddrStatus.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSummaryAddrStatus.setDescription('The status of this entry.')
juniDvmrpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5), )
if mibBuilder.loadTexts: juniDvmrpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpInterfaceTable.setDescription("The (conceptual) table listing the router's multicast-capable interfaces. This table augments the DvmrpInterfaceTable.")
juniDvmrpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1), )
junidDvmrpInterfaceEntry.registerAugmentions(("Juniper-DVMRP-MIB", "juniDvmrpInterfaceEntry"))
juniDvmrpInterfaceEntry.setIndexNames(*junidDvmrpInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: juniDvmrpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpInterfaceEntry.setDescription('An entry (conceptual row) in the juniDvmrpInterfaceTable. This row extends ipMRouteInterfaceEntry in the IP Multicast MIB, where the threshold object resides.')
juniDvmrpInterfaceAutoSummary = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpInterfaceAutoSummary.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpInterfaceAutoSummary.setDescription('Enables or disable auto-summarization on this interface.')
juniDvmrpInterfaceMetricOffsetOut = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpInterfaceMetricOffsetOut.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpInterfaceMetricOffsetOut.setDescription('The distance metric for this interface which is used to calculate outbound distance vectors.')
juniDvmrpInterfaceMetricOffsetIn = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpInterfaceMetricOffsetIn.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpInterfaceMetricOffsetIn.setDescription('The distance metric for this interface which is used to calculate inbound distance vectors.')
juniDvmrpInterfaceAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpInterfaceAdminState.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpInterfaceAdminState.setDescription('Controls whether DVMRP is enabled or not.')
juniDvmrpInterfaceAnnounceListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 5, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDvmrpInterfaceAnnounceListName.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpInterfaceAnnounceListName.setDescription('Configures the name of the acceptance announce filter for the IP access list.')
juniDvmrpPruneTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6), )
if mibBuilder.loadTexts: juniDvmrpPruneTable.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpPruneTable.setDescription("The (conceptual) table listing the router's upstream prune state.")
juniDvmrpPruneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1), ).setIndexNames((0, "Juniper-DVMRP-MIB", "juniDvmrpPruneGroup"), (0, "Juniper-DVMRP-MIB", "juniDvmrpPruneSource"), (0, "Juniper-DVMRP-MIB", "juniDvmrpPruneSourceMask"))
if mibBuilder.loadTexts: juniDvmrpPruneEntry.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpPruneEntry.setDescription('An entry (conceptual row) in the juniDvmrpPruneTable.')
juniDvmrpPruneGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: juniDvmrpPruneGroup.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpPruneGroup.setDescription('The group address which has been pruned.')
juniDvmrpPruneSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: juniDvmrpPruneSource.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpPruneSource.setDescription('The address of the source or source network which has been pruned.')
juniDvmrpPruneSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: juniDvmrpPruneSourceMask.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpPruneSourceMask.setDescription("The address of the source or source network which has been pruned. The mask must either be all 1's, or else juniDvmrpPruneSource and juniDvmrpPruneSourceMask must match juniDvmrpRouteSource and juniDvmrpRouteSourceMask for some entry in the juniDvmrpRouteTable.")
juniDvmrpPruneIIFIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDvmrpPruneIIFIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpPruneIIFIfIndex.setDescription('The ifIndex of the upstream interface for this source group entry.')
juniDvmrpPruneUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 6, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDvmrpPruneUpTime.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpPruneUpTime.setDescription('This is the amount of time that this prune has remained valid.')
juniDvmrpSrcGrpOifTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7), )
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifTable.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifTable.setDescription('The (conceptual) OIFs for particular source group entries.')
juniDvmrpSrcGrpOifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1), ).setIndexNames((0, "Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifGroup"), (0, "Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifSource"), (0, "Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifSourceMask"), (0, "Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifOIFIfIndex"))
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifEntry.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifEntry.setDescription('An entry (conceptual row) in the juniDvmrpSrcGrpOifTable.')
juniDvmrpSrcGrpOifGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 1), IpAddress())
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifGroup.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifGroup.setDescription('The group address which has been pruned.')
juniDvmrpSrcGrpOifSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 2), IpAddress())
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifSource.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifSource.setDescription('The address of the source or source network which has been pruned.')
juniDvmrpSrcGrpOifSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 3), IpAddress())
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifSourceMask.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifSourceMask.setDescription("The address of the source or source network which has been pruned. The mask must either be all 1's, or else juniDvmrpPruneSource and juniDvmrpPruneSourceMask must match juniDvmrpRouteSource and juniDvmrpRouteSourceMask for some entry in the juniDvmrpRouteTable.")
juniDvmrpSrcGrpOifOIFIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifOIFIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifOIFIfIndex.setDescription('The ifIndex of one of the downstream interfaces for this source group entry.')
juniDvmrpSrcGrpOifOIFPruned = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifOIFPruned.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifOIFPruned.setDescription('If true this OIF has been pruned.')
juniDvmrpSrcGrpOifOIFDnTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 7, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifOIFDnTTL.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSrcGrpOifOIFDnTTL.setDescription('The timeout for this OIF. If juniDvmrpSrcGrpOifOIFPruned is false then this is undefined.')
juniDvmrpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 0))
juniDvmrpRouteHogNotificationTrap = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 1, 1, 0, 1))
if mibBuilder.loadTexts: juniDvmrpRouteHogNotificationTrap.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpRouteHogNotificationTrap.setDescription('This is an indication that the route hog notification limit has been exceeded during the past minute. It may mean that a route surge is going on.')
juniDvmrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4))
juniDvmrpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 1))
juniDvmrpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2))
juniDvmrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 1, 1)).setObjects(("Juniper-DVMRP-MIB", "juniDvmrpBaseGroup"), ("Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrGroup"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceGroup"), ("Juniper-DVMRP-MIB", "juniDvmrpSourceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpCompliance = juniDvmrpCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: juniDvmrpCompliance.setDescription('Obsolete compliance statement for entities which implement the Juniper DVMRP MIB. This statement became obsolete when new objects were added.')
juniDvmrpCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 1, 2)).setObjects(("Juniper-DVMRP-MIB", "juniDvmrpBaseGroup2"), ("Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrGroup"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceGroup2"), ("Juniper-DVMRP-MIB", "juniDvmrpSourceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpCompliance2 = juniDvmrpCompliance2.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpCompliance2.setDescription('The compliance statement for entities which implement the Juniper DVMRP MIB.')
juniDvmrpBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 1)).setObjects(("Juniper-DVMRP-MIB", "juniDvmrpAdminState"), ("Juniper-DVMRP-MIB", "juniDvmrpMcastAdminState"), ("Juniper-DVMRP-MIB", "juniDvmrpRouteHogNotification"), ("Juniper-DVMRP-MIB", "juniDvmrpRouteLimit"), ("Juniper-DVMRP-MIB", "juniDvmrpS32PrunesOnly"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpBaseGroup = juniDvmrpBaseGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniDvmrpBaseGroup.setDescription('Obsolete collection of objects providing basic management of DVMRP in a Juniper product. This group became obsolete when support was added for the DVMRP unicast routing object.')
juniDvmrpAclDistNbrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 2)).setObjects(("Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrDistance"), ("Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrNbrListName"), ("Juniper-DVMRP-MIB", "juniDvmrpAclDistNbrStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpAclDistNbrGroup = juniDvmrpAclDistNbrGroup.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAclDistNbrGroup.setDescription('A collection of objects providing management of DVMRP access list distance neighbors in a Juniper product.')
juniDvmrpInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 3)).setObjects(("Juniper-DVMRP-MIB", "juniDvmrpLocalAddrMask"), ("Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrCost"), ("Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrStatus"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAutoSummary"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceMetricOffsetOut"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceMetricOffsetIn"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpInterfaceGroup = juniDvmrpInterfaceGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniDvmrpInterfaceGroup.setDescription('Obsolete collection of objects providing management of a DVMRP interface in a Juniper product. This group became obsolete when support for the DVMRP interface announce list name object was added.')
juniDvmrpSourceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 4)).setObjects(("Juniper-DVMRP-MIB", "juniDvmrpPruneIIFIfIndex"), ("Juniper-DVMRP-MIB", "juniDvmrpPruneUpTime"), ("Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifOIFPruned"), ("Juniper-DVMRP-MIB", "juniDvmrpSrcGrpOifOIFDnTTL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpSourceGroup = juniDvmrpSourceGroup.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpSourceGroup.setDescription('A collection of objects providing management of a DVMRP source group in a Juniper product.')
juniDvmrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 5)).setObjects(("Juniper-DVMRP-MIB", "juniDvmrpRouteHogNotificationTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpNotificationGroup = juniDvmrpNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpNotificationGroup.setDescription('A notification for signaling important DVMRP events.')
juniDvmrpBaseGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 6)).setObjects(("Juniper-DVMRP-MIB", "juniDvmrpAdminState"), ("Juniper-DVMRP-MIB", "juniDvmrpMcastAdminState"), ("Juniper-DVMRP-MIB", "juniDvmrpRouteHogNotification"), ("Juniper-DVMRP-MIB", "juniDvmrpRouteLimit"), ("Juniper-DVMRP-MIB", "juniDvmrpS32PrunesOnly"), ("Juniper-DVMRP-MIB", "juniDvmrpUnicastRouting"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpBaseGroup2 = juniDvmrpBaseGroup2.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpBaseGroup2.setDescription('A collection of objects providing basic management of DVMRP in a Juniper product.')
juniDvmrpInterfaceGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 44, 4, 2, 7)).setObjects(("Juniper-DVMRP-MIB", "juniDvmrpLocalAddrMask"), ("Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrCost"), ("Juniper-DVMRP-MIB", "juniDvmrpSummaryAddrStatus"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAutoSummary"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceMetricOffsetOut"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceMetricOffsetIn"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAdminState"), ("Juniper-DVMRP-MIB", "juniDvmrpInterfaceAnnounceListName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpInterfaceGroup2 = juniDvmrpInterfaceGroup2.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpInterfaceGroup2.setDescription('A collection of objects providing management of a DVMRP interface in a Juniper product.')
mibBuilder.exportSymbols("Juniper-DVMRP-MIB", PYSNMP_MODULE_ID=juniDvmrpMIB, juniDvmrpSummaryAddrCost=juniDvmrpSummaryAddrCost, juniDvmrpInterfaceEntry=juniDvmrpInterfaceEntry, juniDvmrpSrcGrpOifOIFPruned=juniDvmrpSrcGrpOifOIFPruned, juniDvmrpNotificationGroup=juniDvmrpNotificationGroup, juniDvmrpInterfaceAutoSummary=juniDvmrpInterfaceAutoSummary, juniDvmrpGroups=juniDvmrpGroups, juniDvmrpInterfaceMetricOffsetOut=juniDvmrpInterfaceMetricOffsetOut, juniDvmrpInterfaceGroup=juniDvmrpInterfaceGroup, juniDvmrpSummaryAddrTable=juniDvmrpSummaryAddrTable, juniDvmrpInterfaceMetricOffsetIn=juniDvmrpInterfaceMetricOffsetIn, juniDvmrpAclDistNbrTable=juniDvmrpAclDistNbrTable, juniDvmrpPruneSource=juniDvmrpPruneSource, juniDvmrpLocalAddrTableEntry=juniDvmrpLocalAddrTableEntry, juniDvmrpSummaryAddrMask=juniDvmrpSummaryAddrMask, juniDvmrpPruneIIFIfIndex=juniDvmrpPruneIIFIfIndex, juniDvmrpMIBObjects=juniDvmrpMIBObjects, juniDvmrpPruneUpTime=juniDvmrpPruneUpTime, juniDvmrpSrcGrpOifSource=juniDvmrpSrcGrpOifSource, juniDvmrpSrcGrpOifOIFIfIndex=juniDvmrpSrcGrpOifOIFIfIndex, juniDvmrpLocalAddrMask=juniDvmrpLocalAddrMask, juniDvmrpMcastAdminState=juniDvmrpMcastAdminState, juniDvmrpSummaryAddrAddress=juniDvmrpSummaryAddrAddress, juniDvmrpSrcGrpOifOIFDnTTL=juniDvmrpSrcGrpOifOIFDnTTL, juniDvmrpCompliance=juniDvmrpCompliance, juniDvmrpPruneEntry=juniDvmrpPruneEntry, juniDvmrpRouteHogNotificationTrap=juniDvmrpRouteHogNotificationTrap, juniDvmrpSrcGrpOifTable=juniDvmrpSrcGrpOifTable, juniDvmrpSrcGrpOifSourceMask=juniDvmrpSrcGrpOifSourceMask, juniDvmrpPruneSourceMask=juniDvmrpPruneSourceMask, juniDvmrpS32PrunesOnly=juniDvmrpS32PrunesOnly, juniDvmrpSourceGroup=juniDvmrpSourceGroup, juniDvmrp=juniDvmrp, juniDvmrpUnicastRouting=juniDvmrpUnicastRouting, juniDvmrpAclDistNbrNbrListName=juniDvmrpAclDistNbrNbrListName, juniDvmrpMIB=juniDvmrpMIB, juniDvmrpConformance=juniDvmrpConformance, juniDvmrpSummaryAddrTableEntry=juniDvmrpSummaryAddrTableEntry, juniDvmrpInterfaceAnnounceListName=juniDvmrpInterfaceAnnounceListName, juniDvmrpSrcGrpOifEntry=juniDvmrpSrcGrpOifEntry, juniDvmrpAclDistNbrAclListName=juniDvmrpAclDistNbrAclListName, juniDvmrpAclDistNbrGroup=juniDvmrpAclDistNbrGroup, juniDvmrpRouteHogNotification=juniDvmrpRouteHogNotification, juniDvmrpSrcGrpOifGroup=juniDvmrpSrcGrpOifGroup, juniDvmrpCompliances=juniDvmrpCompliances, juniDvmrpBaseGroup2=juniDvmrpBaseGroup2, juniDvmrpAclDistNbrIfIndex=juniDvmrpAclDistNbrIfIndex, juniDvmrpAdminState=juniDvmrpAdminState, juniDvmrpAclDistNbrStatus=juniDvmrpAclDistNbrStatus, juniDvmrpScalar=juniDvmrpScalar, juniDvmrpInterfaceTable=juniDvmrpInterfaceTable, juniDvmrpRouteLimit=juniDvmrpRouteLimit, juniDvmrpBaseGroup=juniDvmrpBaseGroup, juniDvmrpTraps=juniDvmrpTraps, juniDvmrpLocalAddrTable=juniDvmrpLocalAddrTable, juniDvmrpPruneGroup=juniDvmrpPruneGroup, juniDvmrpInterfaceGroup2=juniDvmrpInterfaceGroup2, juniDvmrpLocalAddrAddrOrIfIndex=juniDvmrpLocalAddrAddrOrIfIndex, juniDvmrpLocalAddrIfIndex=juniDvmrpLocalAddrIfIndex, juniDvmrpSummaryAddrIfIndex=juniDvmrpSummaryAddrIfIndex, juniDvmrpPruneTable=juniDvmrpPruneTable, juniDvmrpAclDistNbrEntry=juniDvmrpAclDistNbrEntry, juniDvmrpAclDistNbrDistance=juniDvmrpAclDistNbrDistance, juniDvmrpCompliance2=juniDvmrpCompliance2, juniDvmrpSummaryAddrStatus=juniDvmrpSummaryAddrStatus, juniDvmrpInterfaceAdminState=juniDvmrpInterfaceAdminState)

#
# PySNMP MIB module RADLAN-OSPF-LSDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-OSPF-LSDB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:47:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
RouterID, AreaID = mibBuilder.importSymbols("OSPF-MIB", "RouterID", "AreaID")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
rlOspfIfEntry, RlOspfProcessID, rlOspfVirtIfEntry, rlOspf = mibBuilder.importSymbols("RADLAN-OSPF-MIB", "rlOspfIfEntry", "RlOspfProcessID", "rlOspfVirtIfEntry", "rlOspf")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, iso, NotificationType, Gauge32, IpAddress, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, mib_2, Counter32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "iso", "NotificationType", "Gauge32", "IpAddress", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "mib-2", "Counter32", "Integer32", "TimeTicks")
TextualConvention, TruthValue, RowStatus, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString", "TimeStamp")
rlOspfLsdb = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 221))
rlOspfLsdb.setRevisions(('2011-05-04 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlOspfLsdb.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlOspfLsdb.setLastUpdated('201105041700Z')
if mibBuilder.loadTexts: rlOspfLsdb.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlOspfLsdb.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlOspfLsdb.setDescription('The private MIB module definition for OSPF LSA Database MIB.')
rlOspfRouterLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 221, 1), )
if mibBuilder.loadTexts: rlOspfRouterLsaTable.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaTable.setDescription('Router Link State Advertisement.')
rlOspfRouterLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 221, 1, 1), ).setIndexNames((0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaProcessId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaAreaId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaLsid"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaRouterId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaIdx"))
if mibBuilder.loadTexts: rlOspfRouterLsaEntry.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaEntry.setDescription('A single entry from Router LSA.')
rlOspfRouterLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaProcessId.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaProcessId.setDescription('A 32-bit integer uniquely identifying an OSPF process.')
rlOspfRouterLsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaAreaId.setReference('OSPF Version 2, Appendix C.2 Area parameters')
if mibBuilder.loadTexts: rlOspfRouterLsaAreaId.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaAreaId.setDescription('The 32 bit identifier of the Area from which the LSA was received.')
rlOspfRouterLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaLsid.setReference('OSPF Version 2, Section 12.1.4 Link State ID')
if mibBuilder.loadTexts: rlOspfRouterLsaLsid.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaLsid.setDescription('The Link State ID is an LS Type Specific field containing either a Router ID or an IP Address; it identifies the piece of the routing domain that is being described by the advertisement.')
rlOspfRouterLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaRouterId.setReference('OSPF Version 2, Appendix C.1 Global parameters')
if mibBuilder.loadTexts: rlOspfRouterLsaRouterId.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaRouterId.setDescription('The 32 bit number that uniquely identifies the originating router in the Autonomous System.')
rlOspfRouterLsaIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaIdx.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaIdx.setDescription('The index is a unsigned 32-bit integer. It is used as sequence number of entry in the LSA and relevant only for Router or Network LSA which can contain unlimited number of entries.')
rlOspfRouterLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaSequence.setReference('OSPF Version 2, Section 12.1.6 LS sequence number')
if mibBuilder.loadTexts: rlOspfRouterLsaSequence.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaSequence.setDescription('The sequence number field is a signed 32-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement.')
rlOspfRouterLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaAge.setReference('OSPF Version 2, Section 12.1.1 LS age')
if mibBuilder.loadTexts: rlOspfRouterLsaAge.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaAge.setDescription('This field is the age of the link state advertisement in seconds.')
rlOspfRouterLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaChecksum.setReference('OSPF Version 2, Section 12.1.7 LS checksum')
if mibBuilder.loadTexts: rlOspfRouterLsaChecksum.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaChecksum.setDescription("This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum.")
rlOspfRouterLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaLength.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaLength.setDescription('The lenth in bytes of the LSA. This includes the 20 byte LSA header.')
rlOspfRouterLsaBitV = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaBitV.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaBitV.setDescription('When set, the router is an endpoint of one or more fully adjacent virtual links having the described area as Transit area (V is for virtual link endpoint).')
rlOspfRouterLsaBitE = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaBitE.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaBitE.setDescription('When set, the router is an AS boundary router (E is for external).')
rlOspfRouterLsaBitB = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaBitB.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaBitB.setDescription('When set, the router is an area border router (B is for border).')
rlOspfRouterLsaLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaLinks.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaLinks.setDescription('The number of router links described in this LSA. This must be the total collection of router links (i.e., interfaces) to the area.')
rlOspfRouterLsaLinkID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaLinkID.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaLinkID.setDescription("Identifies the object that this router link connects to. Value depends on the link's Type.")
rlOspfRouterLsaLinkData = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaLinkData.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaLinkData.setDescription("Value depends on the link's Type field.")
rlOspfRouterLsaType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pointToPoint", 1), ("transitNetwork", 2), ("stubNetwork", 3), ("virtualLink", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaType.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaType.setDescription('A quick description of the router link.')
rlOspfRouterLsaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRouterLsaMetric.setStatus('current')
if mibBuilder.loadTexts: rlOspfRouterLsaMetric.setDescription('The cost of using this router link.')
rlOspfNetworkLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 221, 2), )
if mibBuilder.loadTexts: rlOspfNetworkLsaTable.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaTable.setDescription('Network Link State Advertisement.')
rlOspfNetworkLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 221, 2, 1), ).setIndexNames((0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaProcessId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaAreaId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaLsid"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaRouterId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaIdx"))
if mibBuilder.loadTexts: rlOspfNetworkLsaEntry.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaEntry.setDescription('A single entry from Network LSA.')
rlOspfNetworkLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaProcessId.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaProcessId.setDescription('A 32-bit integer uniquely identifying an OSPF process.')
rlOspfNetworkLsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaAreaId.setReference('OSPF Version 2, Appendix C.2 Area parameters')
if mibBuilder.loadTexts: rlOspfNetworkLsaAreaId.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaAreaId.setDescription('The 32 bit identifier of the Area from which the LSA was received.')
rlOspfNetworkLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaLsid.setReference('OSPF Version 2, Section 12.1.4 Link State ID')
if mibBuilder.loadTexts: rlOspfNetworkLsaLsid.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaLsid.setDescription('The Link State ID is an LS Type Specific field containing either a Router ID or an IP Address; it identifies the piece of the routing domain that is being described by the advertisement.')
rlOspfNetworkLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaRouterId.setReference('OSPF Version 2, Appendix C.1 Global parameters')
if mibBuilder.loadTexts: rlOspfNetworkLsaRouterId.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaRouterId.setDescription('The 32 bit number that uniquely identifies the originating router in the Autonomous System.')
rlOspfNetworkLsaIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaIdx.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaIdx.setDescription('The index is a unsigned 32-bit integer. It is used as sequence number of entry in the LSA and relevant only for Router or Network LSA which can contain unlimited number of entries.')
rlOspfNetworkLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaSequence.setReference('OSPF Version 2, Section 12.1.6 LS sequence number')
if mibBuilder.loadTexts: rlOspfNetworkLsaSequence.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaSequence.setDescription('The sequence number field is a signed 32-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement.')
rlOspfNetworkLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaAge.setReference('OSPF Version 2, Section 12.1.1 LS age')
if mibBuilder.loadTexts: rlOspfNetworkLsaAge.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaAge.setDescription('This field is the age of the link state advertisement in seconds.')
rlOspfNetworkLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaChecksum.setReference('OSPF Version 2, Section 12.1.7 LS checksum')
if mibBuilder.loadTexts: rlOspfNetworkLsaChecksum.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaChecksum.setDescription("This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum.")
rlOspfNetworkLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaLength.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaLength.setDescription('The lenth in bytes of the LSA. This includes the 20 byte LSA header.')
rlOspfNetworkLsaMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaMask.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaMask.setDescription('The IP address mask for the network.')
rlOspfNetworkLsaAttRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetworkLsaAttRouter.setStatus('current')
if mibBuilder.loadTexts: rlOspfNetworkLsaAttRouter.setDescription('The Router IDs of each of the routers attached to the network.')
rlOspfSummaryType3LsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 221, 3), )
if mibBuilder.loadTexts: rlOspfSummaryType3LsaTable.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaTable.setDescription('Summary Link State Advertisement for network (Type 3).')
rlOspfSummaryType3LsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 221, 3, 1), ).setIndexNames((0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType3LsaProcessId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType3LsaAreaId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType3LsaLsid"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType3LsaRouterId"))
if mibBuilder.loadTexts: rlOspfSummaryType3LsaEntry.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaEntry.setDescription('A single entry from Summary LSA.')
rlOspfSummaryType3LsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaProcessId.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaProcessId.setDescription('A 32-bit integer uniquely identifying an OSPF process.')
rlOspfSummaryType3LsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaAreaId.setReference('OSPF Version 2, Appendix C.2 Area parameters')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaAreaId.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaAreaId.setDescription('The 32 bit identifier of the Area from which the LSA was received.')
rlOspfSummaryType3LsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaLsid.setReference('OSPF Version 2, Section 12.1.4 Link State ID')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaLsid.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaLsid.setDescription('The Link State ID is an LS Type Specific field containing either a Router ID or an IP Address; it identifies the piece of the routing domain that is being described by the advertisement.')
rlOspfSummaryType3LsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaRouterId.setReference('OSPF Version 2, Appendix C.1 Global parameters')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaRouterId.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaRouterId.setDescription('The 32 bit number that uniquely identifies the originating router in the Autonomous System.')
rlOspfSummaryType3LsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaSequence.setReference('OSPF Version 2, Section 12.1.6 LS sequence number')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaSequence.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaSequence.setDescription('The sequence number field is a signed 32-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement.')
rlOspfSummaryType3LsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaAge.setReference('OSPF Version 2, Section 12.1.1 LS age')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaAge.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaAge.setDescription('This field is the age of the link state advertisement in seconds.')
rlOspfSummaryType3LsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaChecksum.setReference('OSPF Version 2, Section 12.1.7 LS checksum')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaChecksum.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaChecksum.setDescription("This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum.")
rlOspfSummaryType3LsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaLength.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaLength.setDescription('The lenth in bytes of the LSA. This includes the 20 byte LSA header.')
rlOspfSummaryType3LsaMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaMask.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaMask.setDescription("Value depends on the link's Type field.")
rlOspfSummaryType3LsaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType3LsaMetric.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType3LsaMetric.setDescription('The cost of using this router link.')
rlOspfSummaryType4LsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 221, 4), )
if mibBuilder.loadTexts: rlOspfSummaryType4LsaTable.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaTable.setDescription('Summary Link State Advertisement for ASBR (Type 4).')
rlOspfSummaryType4LsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 221, 4, 1), ).setIndexNames((0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType4LsaProcessId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType4LsaAreaId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType4LsaLsid"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType4LsaRouterId"))
if mibBuilder.loadTexts: rlOspfSummaryType4LsaEntry.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaEntry.setDescription('A single entry from Summary LSA.')
rlOspfSummaryType4LsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType4LsaProcessId.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaProcessId.setDescription('A 32-bit integer uniquely identifying an OSPF process.')
rlOspfSummaryType4LsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType4LsaAreaId.setReference('OSPF Version 2, Appendix C.2 Area parameters')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaAreaId.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaAreaId.setDescription('The 32 bit identifier of the Area from which the LSA was received.')
rlOspfSummaryType4LsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType4LsaLsid.setReference('OSPF Version 2, Section 12.1.4 Link State ID')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaLsid.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaLsid.setDescription('The Link State ID is an LS Type Specific field containing either a Router ID or an IP Address; it identifies the piece of the routing domain that is being described by the advertisement.')
rlOspfSummaryType4LsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType4LsaRouterId.setReference('OSPF Version 2, Appendix C.1 Global parameters')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaRouterId.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaRouterId.setDescription('The 32 bit number that uniquely identifies the originating router in the Autonomous System.')
rlOspfSummaryType4LsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType4LsaSequence.setReference('OSPF Version 2, Section 12.1.6 LS sequence number')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaSequence.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaSequence.setDescription('The sequence number field is a signed 32-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement.')
rlOspfSummaryType4LsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType4LsaAge.setReference('OSPF Version 2, Section 12.1.1 LS age')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaAge.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaAge.setDescription('This field is the age of the link state advertisement in seconds.')
rlOspfSummaryType4LsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType4LsaChecksum.setReference('OSPF Version 2, Section 12.1.7 LS checksum')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaChecksum.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaChecksum.setDescription("This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum.")
rlOspfSummaryType4LsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType4LsaLength.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaLength.setDescription('The lenth in bytes of the LSA. This includes the 20 byte LSA header.')
rlOspfSummaryType4LsaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSummaryType4LsaMetric.setStatus('current')
if mibBuilder.loadTexts: rlOspfSummaryType4LsaMetric.setDescription('The cost of using this router link.')
rlOspfExternalLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 221, 5), )
if mibBuilder.loadTexts: rlOspfExternalLsaTable.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaTable.setDescription('External Link State Advertisement.')
rlOspfExternalLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 221, 5, 1), ).setIndexNames((0, "RADLAN-OSPF-LSDB-MIB", "rlOspfExternalLsaProcessId"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfExternalLsaLsid"), (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfExternalLsaRouterId"))
if mibBuilder.loadTexts: rlOspfExternalLsaEntry.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaEntry.setDescription('A single entry from External LSA.')
rlOspfExternalLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaProcessId.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaProcessId.setDescription('A 32-bit integer uniquely identifying an OSPF process.')
rlOspfExternalLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaLsid.setReference('OSPF Version 2, Section 12.1.4 Link State ID')
if mibBuilder.loadTexts: rlOspfExternalLsaLsid.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaLsid.setDescription('The Link State ID is an LS Type Specific field containing either a Router ID or an IP Address; it identifies the piece of the routing domain that is being described by the advertisement.')
rlOspfExternalLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 3), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaRouterId.setReference('OSPF Version 2, Appendix C.1 Global parameters')
if mibBuilder.loadTexts: rlOspfExternalLsaRouterId.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaRouterId.setDescription('The 32 bit number that uniquely identifies the originating router in the Autonomous System.')
rlOspfExternalLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaSequence.setReference('OSPF Version 2, Section 12.1.6 LS sequence number')
if mibBuilder.loadTexts: rlOspfExternalLsaSequence.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaSequence.setDescription('The sequence number field is a signed 32-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement.')
rlOspfExternalLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaAge.setReference('OSPF Version 2, Section 12.1.1 LS age')
if mibBuilder.loadTexts: rlOspfExternalLsaAge.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaAge.setDescription('This field is the age of the link state advertisement in seconds.')
rlOspfExternalLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaChecksum.setReference('OSPF Version 2, Section 12.1.7 LS checksum')
if mibBuilder.loadTexts: rlOspfExternalLsaChecksum.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaChecksum.setDescription("This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum.")
rlOspfExternalLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaLength.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaLength.setDescription('The lenth in bytes of the LSA. This includes the 20 byte LSA header.')
rlOspfExternalLsaMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaMask.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaMask.setDescription("Value depends on the link's Type field.")
rlOspfExternalLsaFrwAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaFrwAddress.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaFrwAddress.setDescription("Data traffic for the advertised destination will be forwarded to this address. If the Forwarding address is set to 0.0.0.0, data traffic will be forwarded instead to the LSA's originator (i.e., the responsible AS boundary router).")
rlOspfExternalLsaBitE = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaBitE.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaBitE.setDescription('The type of external metric. If bit E is set, the metric specified is a Type 2 external metric.')
rlOspfExternalLsaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaMetric.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaMetric.setDescription('The cost of this route.')
rlOspfExternalLsaTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfExternalLsaTag.setStatus('current')
if mibBuilder.loadTexts: rlOspfExternalLsaTag.setDescription('A 32-bit field attached to each external route.')
mibBuilder.exportSymbols("RADLAN-OSPF-LSDB-MIB", rlOspfRouterLsaBitV=rlOspfRouterLsaBitV, rlOspfSummaryType3LsaProcessId=rlOspfSummaryType3LsaProcessId, rlOspfSummaryType4LsaLsid=rlOspfSummaryType4LsaLsid, rlOspfRouterLsaLinkData=rlOspfRouterLsaLinkData, rlOspfExternalLsaProcessId=rlOspfExternalLsaProcessId, rlOspfNetworkLsaAreaId=rlOspfNetworkLsaAreaId, rlOspfSummaryType3LsaChecksum=rlOspfSummaryType3LsaChecksum, rlOspfRouterLsaBitB=rlOspfRouterLsaBitB, rlOspfSummaryType3LsaRouterId=rlOspfSummaryType3LsaRouterId, rlOspfLsdb=rlOspfLsdb, rlOspfRouterLsaBitE=rlOspfRouterLsaBitE, rlOspfRouterLsaSequence=rlOspfRouterLsaSequence, PYSNMP_MODULE_ID=rlOspfLsdb, rlOspfRouterLsaRouterId=rlOspfRouterLsaRouterId, rlOspfNetworkLsaSequence=rlOspfNetworkLsaSequence, rlOspfRouterLsaEntry=rlOspfRouterLsaEntry, rlOspfExternalLsaRouterId=rlOspfExternalLsaRouterId, rlOspfExternalLsaLength=rlOspfExternalLsaLength, rlOspfSummaryType3LsaSequence=rlOspfSummaryType3LsaSequence, rlOspfNetworkLsaMask=rlOspfNetworkLsaMask, rlOspfSummaryType3LsaAge=rlOspfSummaryType3LsaAge, rlOspfNetworkLsaLsid=rlOspfNetworkLsaLsid, rlOspfSummaryType4LsaProcessId=rlOspfSummaryType4LsaProcessId, rlOspfRouterLsaChecksum=rlOspfRouterLsaChecksum, rlOspfSummaryType3LsaMask=rlOspfSummaryType3LsaMask, rlOspfExternalLsaSequence=rlOspfExternalLsaSequence, rlOspfSummaryType3LsaAreaId=rlOspfSummaryType3LsaAreaId, rlOspfExternalLsaLsid=rlOspfExternalLsaLsid, rlOspfNetworkLsaTable=rlOspfNetworkLsaTable, rlOspfSummaryType4LsaTable=rlOspfSummaryType4LsaTable, rlOspfRouterLsaMetric=rlOspfRouterLsaMetric, rlOspfExternalLsaMetric=rlOspfExternalLsaMetric, rlOspfSummaryType3LsaTable=rlOspfSummaryType3LsaTable, rlOspfNetworkLsaEntry=rlOspfNetworkLsaEntry, rlOspfExternalLsaBitE=rlOspfExternalLsaBitE, rlOspfRouterLsaLsid=rlOspfRouterLsaLsid, rlOspfSummaryType4LsaChecksum=rlOspfSummaryType4LsaChecksum, rlOspfNetworkLsaProcessId=rlOspfNetworkLsaProcessId, rlOspfRouterLsaIdx=rlOspfRouterLsaIdx, rlOspfNetworkLsaLength=rlOspfNetworkLsaLength, rlOspfExternalLsaChecksum=rlOspfExternalLsaChecksum, rlOspfRouterLsaLinkID=rlOspfRouterLsaLinkID, rlOspfRouterLsaTable=rlOspfRouterLsaTable, rlOspfSummaryType3LsaLsid=rlOspfSummaryType3LsaLsid, rlOspfRouterLsaLinks=rlOspfRouterLsaLinks, rlOspfRouterLsaType=rlOspfRouterLsaType, rlOspfExternalLsaAge=rlOspfExternalLsaAge, rlOspfRouterLsaProcessId=rlOspfRouterLsaProcessId, rlOspfNetworkLsaAge=rlOspfNetworkLsaAge, rlOspfNetworkLsaAttRouter=rlOspfNetworkLsaAttRouter, rlOspfSummaryType4LsaAge=rlOspfSummaryType4LsaAge, rlOspfSummaryType4LsaMetric=rlOspfSummaryType4LsaMetric, rlOspfNetworkLsaIdx=rlOspfNetworkLsaIdx, rlOspfNetworkLsaChecksum=rlOspfNetworkLsaChecksum, rlOspfSummaryType3LsaLength=rlOspfSummaryType3LsaLength, rlOspfRouterLsaLength=rlOspfRouterLsaLength, rlOspfNetworkLsaRouterId=rlOspfNetworkLsaRouterId, rlOspfSummaryType4LsaRouterId=rlOspfSummaryType4LsaRouterId, rlOspfSummaryType4LsaSequence=rlOspfSummaryType4LsaSequence, rlOspfExternalLsaEntry=rlOspfExternalLsaEntry, rlOspfSummaryType4LsaLength=rlOspfSummaryType4LsaLength, rlOspfRouterLsaAreaId=rlOspfRouterLsaAreaId, rlOspfSummaryType3LsaEntry=rlOspfSummaryType3LsaEntry, rlOspfExternalLsaMask=rlOspfExternalLsaMask, rlOspfSummaryType4LsaAreaId=rlOspfSummaryType4LsaAreaId, rlOspfExternalLsaTable=rlOspfExternalLsaTable, rlOspfExternalLsaTag=rlOspfExternalLsaTag, rlOspfRouterLsaAge=rlOspfRouterLsaAge, rlOspfExternalLsaFrwAddress=rlOspfExternalLsaFrwAddress, rlOspfSummaryType3LsaMetric=rlOspfSummaryType3LsaMetric, rlOspfSummaryType4LsaEntry=rlOspfSummaryType4LsaEntry)
#
# PySNMP MIB module TPLINK-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-VRRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Unsigned32, Bits, Counter32, MibIdentifier, TimeTicks, Counter64, iso, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Unsigned32", "Bits", "Counter32", "MibIdentifier", "TimeTicks", "Counter64", "iso", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tplinkVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 65))
tplinkVrrpMIB.setRevisions(('2012-12-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkVrrpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkVrrpMIB.setLastUpdated('201212130000Z')
if mibBuilder.loadTexts: tplinkVrrpMIB.setOrganization('TP-LINK')
if mibBuilder.loadTexts: tplinkVrrpMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkVrrpMIB.setDescription('This MIB describes objects used for managing Virtual Router Redundancy Protocol (VRRP) routers.')
tplinkVrrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1))
tplinkVrrpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 65, 2))
tpVrrpGlobalCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1))
tpVrrpVirtualIpCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2))
tpVrrpTrackCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3))
tpVrrpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4))
tpVrrpGlobalCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1), )
if mibBuilder.loadTexts: tpVrrpGlobalCtrlTable.setStatus('current')
if mibBuilder.loadTexts: tpVrrpGlobalCtrlTable.setDescription("Operations table for a VRRP router which consists of a sequence (i.e., one or more conceptual rows) of 'TpVrrpGlobalCtrlEntry' items.")
tpVrrpGlobalCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-VRRP-MIB", "tpVrrpVrid"), (0, "TPLINK-VRRP-MIB", "tpVrrpVid"))
if mibBuilder.loadTexts: tpVrrpGlobalCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: tpVrrpGlobalCtrlEntry.setDescription(' An entry in the tpVrrpGlobalCtrlTable containing the operational characteristics of a virtual router. On a VRRP router,a given virtual router is identified by a combination of the VID and VRID.Rows in the table can be modified according to the tpVrrpStatus.')
tpVrrpVrid = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpVrid.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVrid.setDescription('This object contains the Virtual Router Identifier (VRID).')
tpVrrpVid = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpVid.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVid.setDescription('The interface index')
tpVrrpIntfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("interfacevlan", 1), ("routedport", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpIntfStatus.setStatus('current')
if mibBuilder.loadTexts: tpVrrpIntfStatus.setDescription('The interface status')
tpVrrpInterfaceIP = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpInterfaceIP.setStatus('current')
if mibBuilder.loadTexts: tpVrrpInterfaceIP.setDescription('The interface IP address.')
tpVrrpMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpMacAddress.setStatus('current')
if mibBuilder.loadTexts: tpVrrpMacAddress.setDescription('The virtual MAC address of the virtual router.')
tpVrrpDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 6), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpDescription.setStatus('current')
if mibBuilder.loadTexts: tpVrrpDescription.setDescription('The description of the VRRP.')
tpVrrpPrimaryVirtualIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpPrimaryVirtualIp.setStatus('current')
if mibBuilder.loadTexts: tpVrrpPrimaryVirtualIp.setDescription('This is the IP address listed as the source in VRRP advertisement last received by this virtual router.')
tpVrrpRunPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpRunPriority.setStatus('current')
if mibBuilder.loadTexts: tpVrrpRunPriority.setDescription('This object specifies the priority to be used for the virtual router master election process. Higher values imply higher priority.A priority of 255 is used for the router that owns the associated IP address(es).')
tpVrrpConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpConfigPriority.setStatus('current')
if mibBuilder.loadTexts: tpVrrpConfigPriority.setDescription('This object operate the priority to be used for the virtual router master election process.')
tpVrrpAdvertisement = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpAdvertisement.setStatus('current')
if mibBuilder.loadTexts: tpVrrpAdvertisement.setDescription('The time interval, in seconds, between sending advertisement messages. Only the master router sends VRRP advertisements.')
tpVrrpPreeptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpPreeptMode.setStatus('current')
if mibBuilder.loadTexts: tpVrrpPreeptMode.setDescription('Controls whether a higher priority virtual router will preempt a lower priority master')
tpVrrpTimeDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpTimeDelay.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTimeDelay.setDescription('This is object is used to config the delay timer associated with the VRRP.')
tpVrrpAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("normal", 0), ("simple", 1), ("md5", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpAuthType.setStatus('current')
if mibBuilder.loadTexts: tpVrrpAuthType.setDescription('Authentication type used for VRRP protocol exchanges between virtual routers. This value of this object is the same for a given ifindex(Vlan ID).')
tpVrrpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 14), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpKey.setStatus('current')
if mibBuilder.loadTexts: tpVrrpKey.setDescription("The Authentication Key. This object is set according to the value of the 'tpVrrpAuthType' object ('Simple' or 'MD5').")
tpVrrpState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("initialize", 0), ("backup", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpState.setStatus('current')
if mibBuilder.loadTexts: tpVrrpState.setDescription("The current state of the virtual router. This object has three defined values: - `initialize', which indicates that all the virtual router is waiting for a startup event. - `backup', which indicates the virtual router is monitoring the availability of the master router. - `master', which indicates that the virtual router is forwarding packets for IP addresses that are associated with this router.")
tpVrrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 16), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpStatus.setStatus('current')
if mibBuilder.loadTexts: tpVrrpStatus.setDescription('The following values are states: these values may be used as follow: active(1),if the entry is being used. createAndGo(4),creat a new entry destroy(6),destory the entry.')
tpVrrpVirtualIpCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1), )
if mibBuilder.loadTexts: tpVrrpVirtualIpCtrlTable.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVirtualIpCtrlTable.setDescription('The table of addresses associated with this virtual router.')
tpVrrpVirtualIpCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1), ).setIndexNames((0, "TPLINK-VRRP-MIB", "tpVrrpVirtualIpVrid"), (0, "TPLINK-VRRP-MIB", "tpVrrpVirtualIpVid"), (0, "TPLINK-VRRP-MIB", "tpVrrpVirtualIpAddress"))
if mibBuilder.loadTexts: tpVrrpVirtualIpCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVirtualIpCtrlEntry.setDescription(' An entry in the table contains an IP address that is associated with a virtual router.')
tpVrrpVirtualIpVrid = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpVirtualIpVrid.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVirtualIpVrid.setDescription('This object contains the Virtual Router Identifier (VRID).')
tpVrrpVirtualIpVid = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpVirtualIpVid.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVirtualIpVid.setDescription('The interface index')
tpVrrpVirtualIpintfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("interfacevlan", 1), ("routedport", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpVirtualIpintfStatus.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVirtualIpintfStatus.setDescription('The interface status')
tpVrrpVirtualIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpVirtualIpAddress.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVirtualIpAddress.setDescription('The virtual IP address associated with a virtual router. ')
tpVrrpVirtualIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 5), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpVirtualIpStatus.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVirtualIpStatus.setDescription('The following values are states: these values may be used as follow: active(1),if the entry is being used. createAndGo(4),creat a new entry destroy(6),destory the entry.')
tpVrrpTrackCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1), )
if mibBuilder.loadTexts: tpVrrpTrackCtrlTable.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTrackCtrlTable.setDescription('The table of ifindex tracked by the virtual router.')
tpVrrpTrackCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1), ).setIndexNames((0, "TPLINK-VRRP-MIB", "tpVrrpTrackVrid"), (0, "TPLINK-VRRP-MIB", "tpVrrpTrackVid"), (0, "TPLINK-VRRP-MIB", "tpVrrpTrackInterface"))
if mibBuilder.loadTexts: tpVrrpTrackCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTrackCtrlEntry.setDescription(' An entry in the table contains the ifindex and reduced priority that is associated with a virtual router. ')
tpVrrpTrackVrid = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpTrackVrid.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTrackVrid.setDescription('This object contains the Virtual Router Identifier (VRID).')
tpVrrpTrackVid = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpTrackVid.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTrackVid.setDescription('The interface index')
tpVrrpTrackIntfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("interfacevlan", 1), ("routedport", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpTrackIntfStatus.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTrackIntfStatus.setDescription('The interface status')
tpVrrpTrackInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpTrackInterface.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTrackInterface.setDescription('The ifindex tracked by the virtual router.')
tpVrrpTrackIntfTrackedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("interfacevlan", 1), ("routedport", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpTrackIntfTrackedStatus.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTrackIntfTrackedStatus.setDescription('The interface status')
tpVrrpTrackPriortiy = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpTrackPriortiy.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTrackPriortiy.setDescription('The object operate the priority of the virtual router when the interface tracked linkdown.')
tpVrrpLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpLinkState.setStatus('current')
if mibBuilder.loadTexts: tpVrrpLinkState.setDescription('The object display the status of the interface tracked .')
tpVrrpTrackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 8), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpVrrpTrackStatus.setStatus('current')
if mibBuilder.loadTexts: tpVrrpTrackStatus.setDescription('The following values are states: these values may be used as follow: active(1),if the entry is being used. createAndGo(4),creat a new entry destroy(6),destory the entry.')
tpVrrpChecksumErrors = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpChecksumErrors.setStatus('current')
if mibBuilder.loadTexts: tpVrrpChecksumErrors.setDescription('The total number of VRRP packets received with an invalid VRRP checksum value.')
tpVrrpVersionErrors = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpVersionErrors.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVersionErrors.setDescription('The total number of VRRP packets received with an unknown or unsupported version number.')
tpVrrpVridErrors = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpVridErrors.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVridErrors.setDescription('The total number of VRRP packets received with an invalid VRID for this virtual router.')
tpvrrpStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("active", 1), ("clear", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpvrrpStatsClear.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsClear.setDescription('The following values are states: these values may be used as follow: active(1),if the entry is being used. clear(0),set the entry to 0.')
tpVrrpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4), )
if mibBuilder.loadTexts: tpVrrpStatsTable.setStatus('current')
if mibBuilder.loadTexts: tpVrrpStatsTable.setDescription('Table of virtual router statistics.')
tpVrrpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1), ).setIndexNames((0, "TPLINK-VRRP-MIB", "tpVrrpStatsVrid"), (0, "TPLINK-VRRP-MIB", "tpVrrpStatsVid"))
if mibBuilder.loadTexts: tpVrrpStatsEntry.setStatus('current')
if mibBuilder.loadTexts: tpVrrpStatsEntry.setDescription('An entry in the table, containing statistics information about a given virtual router.')
tpVrrpStatsVrid = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpStatsVrid.setStatus('current')
if mibBuilder.loadTexts: tpVrrpStatsVrid.setDescription('the VRID of the virtual router. It is used together with interface ID to specify the virtual router to operate statistics.')
tpVrrpStatsVid = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpStatsVid.setStatus('current')
if mibBuilder.loadTexts: tpVrrpStatsVid.setDescription('the interface ID of the virtual router. It is used together with VRID to specify the virtual router to operate statistics.')
tpVrrpStatsIntfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("interfacevlan", 1), ("routedport", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpStatsIntfStatus.setStatus('current')
if mibBuilder.loadTexts: tpVrrpStatsIntfStatus.setDescription('The interface status')
tpVrrpChecksumErr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpChecksumErr.setStatus('current')
if mibBuilder.loadTexts: tpVrrpChecksumErr.setDescription('The total number of VRRP packets received with an invalid VRRP checksum value by this virtual router.')
tpVrrpVersionErr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpVersionErr.setStatus('current')
if mibBuilder.loadTexts: tpVrrpVersionErr.setDescription('The total number of VRRP packets received with an unknown or unsupported version number by this virtual router.')
tpVrrpStatsBecomeMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpVrrpStatsBecomeMaster.setStatus('current')
if mibBuilder.loadTexts: tpVrrpStatsBecomeMaster.setDescription("The total number of times that this virtual router's state has transitioned to MASTER.")
tpvrrpStatsAdvertiseRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsAdvertiseRcvd.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsAdvertiseRcvd.setDescription('The total number of VRRP advertisements received by this virtual router.')
tpvrrpStatsAdvertiseSent = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsAdvertiseSent.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsAdvertiseSent.setDescription('The total number of VRRP advertisements sent by this virtual router.')
tpvrrpStatsAdvertiseIntervalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsAdvertiseIntervalErrors.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsAdvertiseIntervalErrors.setDescription('The total number of VRRP advertisement packets received for which the advertisement interval is different than the one configured for the local virtual router.')
tpvrrpStatsAuthFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsAuthFailures.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsAuthFailures.setDescription('The total number of VRRP packets received that do not pass the authentication check.')
tpvrrpStatsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsIpTtlErrors.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsIpTtlErrors.setDescription('The total number of VRRP packets received by the virtual router with IP TTL (Time-To-Live) not equal to 255.')
tpvrrpStatsPriorityZeroPktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsPriorityZeroPktsRcvd.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsPriorityZeroPktsRcvd.setDescription("The total number of VRRP packets received by the virtual router with a priority of '0'.")
tpvrrpStatsPriorityZeroPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsPriorityZeroPktsSent.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsPriorityZeroPktsSent.setDescription("The total number of VRRP packets sent by the virtual router with a priority of '0'.")
tpvrrpStatsInvalidTypePktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsInvalidTypePktsRcvd.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsInvalidTypePktsRcvd.setDescription("The number of VRRP packets received by the virtual router with an invalid value in the 'type' field.")
tpvrrpStatsAddressListErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsAddressListErrors.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsAddressListErrors.setDescription('The total number of packets received for which the address list does not match the locally configured list for the virtual router.')
tpvrrpStatsInvalidAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsInvalidAuthType.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsInvalidAuthType.setDescription('The total number of packets received with an unknown authentication type.')
tpvrrpStatsAuthTypeMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsAuthTypeMismatch.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsAuthTypeMismatch.setDescription("The total number of packets received with 'Auth Type' not equal to the locally configured authentication method (`vrrpOperAuthType').")
tpvrrpStatsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpvrrpStatsPacketLengthErrors.setStatus('current')
if mibBuilder.loadTexts: tpvrrpStatsPacketLengthErrors.setDescription('The total number of packets received with a packet length less than the length of the VRRP header.')
mibBuilder.exportSymbols("TPLINK-VRRP-MIB", tpVrrpTrackVid=tpVrrpTrackVid, tpVrrpTrackCtrlTable=tpVrrpTrackCtrlTable, tpVrrpGlobalCtrlEntry=tpVrrpGlobalCtrlEntry, tpVrrpVirtualIpVrid=tpVrrpVirtualIpVrid, tpVrrpStatsTable=tpVrrpStatsTable, tpVrrpAuthType=tpVrrpAuthType, tpVrrpStatsVrid=tpVrrpStatsVrid, tpvrrpStatsInvalidAuthType=tpvrrpStatsInvalidAuthType, tpVrrpTrackCtrl=tpVrrpTrackCtrl, tpVrrpTrackInterface=tpVrrpTrackInterface, tpVrrpVirtualIpAddress=tpVrrpVirtualIpAddress, tpVrrpStatsBecomeMaster=tpVrrpStatsBecomeMaster, tpVrrpVirtualIpintfStatus=tpVrrpVirtualIpintfStatus, tpVrrpRunPriority=tpVrrpRunPriority, tpVrrpGlobalCtrlTable=tpVrrpGlobalCtrlTable, tpVrrpLinkState=tpVrrpLinkState, tpvrrpStatsInvalidTypePktsRcvd=tpvrrpStatsInvalidTypePktsRcvd, tpVrrpVrid=tpVrrpVrid, tpvrrpStatsAuthFailures=tpvrrpStatsAuthFailures, tpVrrpStatus=tpVrrpStatus, tpVrrpVid=tpVrrpVid, tpVrrpVirtualIpCtrlEntry=tpVrrpVirtualIpCtrlEntry, tpvrrpStatsAuthTypeMismatch=tpvrrpStatsAuthTypeMismatch, tpVrrpTrackIntfTrackedStatus=tpVrrpTrackIntfTrackedStatus, tpvrrpStatsAdvertiseRcvd=tpvrrpStatsAdvertiseRcvd, tpVrrpAdvertisement=tpVrrpAdvertisement, tpVrrpConfigPriority=tpVrrpConfigPriority, tpVrrpVirtualIpCtrl=tpVrrpVirtualIpCtrl, tpvrrpStatsClear=tpvrrpStatsClear, tpVrrpStatistics=tpVrrpStatistics, tpVrrpTrackStatus=tpVrrpTrackStatus, tplinkVrrpNotifications=tplinkVrrpNotifications, tpVrrpMacAddress=tpVrrpMacAddress, tplinkVrrpMIB=tplinkVrrpMIB, tpVrrpKey=tpVrrpKey, tpVrrpVirtualIpStatus=tpVrrpVirtualIpStatus, tpVrrpTimeDelay=tpVrrpTimeDelay, tpvrrpStatsAddressListErrors=tpvrrpStatsAddressListErrors, tpVrrpPrimaryVirtualIp=tpVrrpPrimaryVirtualIp, tpVrrpInterfaceIP=tpVrrpInterfaceIP, tpVrrpPreeptMode=tpVrrpPreeptMode, tpVrrpStatsIntfStatus=tpVrrpStatsIntfStatus, tpVrrpIntfStatus=tpVrrpIntfStatus, tpVrrpVirtualIpVid=tpVrrpVirtualIpVid, tpVrrpTrackPriortiy=tpVrrpTrackPriortiy, tpVrrpDescription=tpVrrpDescription, tpVrrpChecksumErr=tpVrrpChecksumErr, PYSNMP_MODULE_ID=tplinkVrrpMIB, tpvrrpStatsIpTtlErrors=tpvrrpStatsIpTtlErrors, tpVrrpVersionErrors=tpVrrpVersionErrors, tpvrrpStatsPriorityZeroPktsRcvd=tpvrrpStatsPriorityZeroPktsRcvd, tpVrrpTrackCtrlEntry=tpVrrpTrackCtrlEntry, tpvrrpStatsPacketLengthErrors=tpvrrpStatsPacketLengthErrors, tpVrrpStatsVid=tpVrrpStatsVid, tpVrrpVridErrors=tpVrrpVridErrors, tpvrrpStatsAdvertiseSent=tpvrrpStatsAdvertiseSent, tpVrrpVirtualIpCtrlTable=tpVrrpVirtualIpCtrlTable, tpVrrpTrackIntfStatus=tpVrrpTrackIntfStatus, tplinkVrrpMIBObjects=tplinkVrrpMIBObjects, tpvrrpStatsAdvertiseIntervalErrors=tpvrrpStatsAdvertiseIntervalErrors, tpVrrpStatsEntry=tpVrrpStatsEntry, tpVrrpTrackVrid=tpVrrpTrackVrid, tpVrrpChecksumErrors=tpVrrpChecksumErrors, tpVrrpGlobalCtrl=tpVrrpGlobalCtrl, tpvrrpStatsPriorityZeroPktsSent=tpvrrpStatsPriorityZeroPktsSent, tpVrrpVersionErr=tpVrrpVersionErr, tpVrrpState=tpVrrpState)

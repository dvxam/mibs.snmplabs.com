#
# PySNMP MIB module Wellfleet-SYS-SVC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-SYS-SVC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Unsigned32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, NotificationType, Gauge32, ObjectIdentity, ModuleIdentity, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Unsigned32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "NotificationType", "Gauge32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfNetBootGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfNetBootGroup")
wfNetbootCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1))
wfNetbootImage = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("imageoff", 1), ("imageon", 2))).clone('imageon')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootImage.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootImage.setDescription('Enables booting of an executable image over the network. If disabled, then the image will be read from a local file system.')
wfNetbootConfig = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configoff", 1), ("configon", 2))).clone('configon')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootConfig.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootConfig.setDescription('Enables booting of a configuration file over the network. If disabled, then the config will be read from a local file system.')
wfNetbootServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootServerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootServerAddress.setDescription('IP address of remote server.')
wfNetbootImageName = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootImageName.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootImageName.setDescription('Pathname of image file on remote server.')
wfNetbootConfigName = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootConfigName.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootConfigName.setDescription('Pathname of configuration file on remote server.')
wfNetbootCfgDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2))).clone('create')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootCfgDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCfgDelete.setDescription('create/delete parameter, dflt = created')
wfNetbootCurrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2))
wfNetbootImageCurr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("imagecurroff", 1), ("imagecurron", 2))).clone('imagecurron')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootImageCurr.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootImageCurr.setDescription('Current value of Netboot image flag in Non-Volatile RAM.')
wfNetbootConfigCurr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configcurroff", 1), ("configcurron", 2))).clone('configcurron')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootConfigCurr.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootConfigCurr.setDescription('Current value of Netboot config flag in Non-Volatile RAM.')
wfNetbootServerAddressCurr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootServerAddressCurr.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootServerAddressCurr.setDescription('IP address of remote server.')
wfNetbootImageNameCurr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootImageNameCurr.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootImageNameCurr.setDescription('Pathname of image file on remote server.')
wfNetbootConfigNameCurr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootConfigNameCurr.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootConfigNameCurr.setDescription('Pathname of configuration file on remote server.')
wfNetbootCfgTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3), )
if mibBuilder.loadTexts: wfNetbootCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCfgTable.setDescription('A Table of Interface-specific Netboot Configuration Parameters')
wfNetbootCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1), ).setIndexNames((0, "Wellfleet-SYS-SVC-MIB", "wfNetbootSlot"), (0, "Wellfleet-SYS-SVC-MIB", "wfNetbootConnector"))
if mibBuilder.loadTexts: wfNetbootCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCfgEntry.setDescription("Values of a particular interface's configuration parameters.")
wfNetbootDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2))).clone('create')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootDelete.setDescription('create/delete parameter, dflt = created Deleteing this instance will set the corresponding NOVRAM values to the default settings.')
wfNetbootSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootSlot.setDescription('instance ID Slot, filled in by driver')
wfNetbootConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))).clone(namedValues=NamedValues(("xcvr1", 1), ("com1", 2), ("com2", 3), ("com3", 4), ("xcvr11", 5), ("xcvr12", 6), ("com11", 7), ("com12", 8), ("xcvr21", 9), ("xcvr22", 10), ("com21", 11), ("com22", 12), ("xcvr31", 13), ("xcvr32", 14), ("com31", 15), ("com32", 16), ("xcvr41", 17), ("xcvr42", 18), ("com41", 19), ("com42", 20), ("xcvr2", 21), ("xcvr33", 22), ("xcvr34", 23), ("arnxcvr1", 24), ("arnxcvr2", 25), ("arncom1", 26), ("arncom2", 27), ("arncom3", 28), ("arncom4", 29), ("arncom5", 30), ("arnmau1", 31), ("arnmau2", 32), ("com13", 33), ("com14", 34), ("com23", 35), ("com24", 36), ("com33", 37), ("com34", 38), ("com43", 39), ("com44", 40)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootConnector.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootConnector.setDescription('Unique number which identifies the interface for which the following parameters are configured.')
wfNetbootIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootIpAddr.setDescription('IP address to use on this interface')
wfNetbootIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootIpMask.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootIpMask.setDescription('IP address mask to use on this interface')
wfNetbootNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootNextHop.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootNextHop.setDescription('IP address of the next hop router connected to this interface. This value is used to auto-configure a static route for Network Boot.')
wfNetbootProtoMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("fron", 1), ("x25on", 2), ("intrnclkon", 3), ("noton", 4), ("annexaon", 5), ("lmion", 6), ("ppp", 7))).clone('noton')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootProtoMask.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootProtoMask.setDescription('Bit Mask indicating a non-default protocol is being used on this interface.')
wfNetbootDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootDisable.setDescription('Enable or disable the interface for Netbooting.')
wfNetbootConnName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootConnName.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootConnName.setDescription('Connector name.')
wfNetbootTokenRingSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 16))).clone(namedValues=NamedValues(("mbps4", 4), ("mbps16", 16))).clone('mbps16')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootTokenRingSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootTokenRingSpeed.setDescription('Speed of the Token Ring interface for Netbooting.')
wfNetbootBchanRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(64, 128))).clone(namedValues=NamedValues(("rate64k", 64), ("rate128k", 128))).clone('rate64k')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootBchanRate.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootBchanRate.setDescription('Speed B Channel for Netbooting. AN 200 Only')
wfNetbootDsuCsuOpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(56, 64))).clone(namedValues=NamedValues(("rate56k", 56), ("rate64k", 64))).clone('rate56k')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootDsuCsuOpMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootDsuCsuOpMode.setDescription('Dsu/Csu interface speed for Netbooting')
wfNetbootCurrTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4), )
if mibBuilder.loadTexts: wfNetbootCurrTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrTable.setDescription('A Table of current values for Interface-specific Netboot Parameters')
wfNetbootCurrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1), ).setIndexNames((0, "Wellfleet-SYS-SVC-MIB", "wfNetbootCurrSlot"), (0, "Wellfleet-SYS-SVC-MIB", "wfNetbootCurrConnector"))
if mibBuilder.loadTexts: wfNetbootCurrEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrEntry.setDescription("Values of a particular interface's current configuration parameters.")
wfNetbootCurrSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootCurrSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrSlot.setDescription('instance ID Slot, filled in by driver')
wfNetbootCurrConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))).clone(namedValues=NamedValues(("currxcvr1", 1), ("currcom1", 2), ("currcom2", 3), ("currcom3", 4), ("currxcvr11", 5), ("currxcvr12", 6), ("currcom11", 7), ("currcom12", 8), ("currxcvr21", 9), ("currxcvr22", 10), ("currcom21", 11), ("currcom22", 12), ("currxcvr31", 13), ("currxcvr32", 14), ("currcom31", 15), ("currcom32", 16), ("currxcvr41", 17), ("currxcvr42", 18), ("currcom41", 19), ("currcom42", 20), ("currxcvr2", 21), ("currxcvr33", 22), ("currxcvr34", 23), ("currarnxcvr1", 24), ("currarnxcvr2", 25), ("currarncom1", 26), ("currarncom2", 27), ("currarncom3", 28), ("currarncom4", 29), ("currarncom5", 30), ("currarnmau1", 31), ("currarnmau2", 32), ("currcom13", 33), ("currcom14", 34), ("currcom23", 35), ("currcom24", 36), ("currcom33", 37), ("currcom34", 38), ("currcom43", 39), ("currcom44", 40)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootCurrConnector.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrConnector.setDescription('Unique number which identifies the interface for which the following parameters are configured.')
wfNetbootCurrIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootCurrIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrIpAddr.setDescription('IP address to use on this interface')
wfNetbootCurrIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootCurrIpMask.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrIpMask.setDescription('IP address mask to use on this interface')
wfNetbootCurrNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootCurrNextHop.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrNextHop.setDescription('IP address of the next hop router connected to this interface. This value is used to auto-configure a static route for Network Boot.')
wfNetbootCurrProtoMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("frcurron", 1), ("x25curron", 2), ("intrnclkcurron", 3), ("notcurron", 4), ("annexaon", 5), ("lmion", 6), ("ppp", 7))).clone('notcurron')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootCurrProtoMask.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrProtoMask.setDescription('Bit Mask indicating a non-default protocol is being used on this interface.')
wfNetbootCurrDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootCurrDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrDisable.setDescription('Enable or disable the interface for Netbooting.')
wfNetbootCurrConnName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootCurrConnName.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrConnName.setDescription('Connector name.')
wfNetbootCurrTokenRingSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 16))).clone(namedValues=NamedValues(("mbps4", 4), ("mbps16", 16))).clone('mbps16')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbootCurrTokenRingSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrTokenRingSpeed.setDescription('Speed of the Token Ring interface for Netbooting.')
wfNetbootCurrBchanRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(64, 128))).clone(namedValues=NamedValues(("rate64k", 64), ("rate128k", 128))).clone('rate64k')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootCurrBchanRate.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrBchanRate.setDescription('Speed B Channel for Netbooting. AN 200 Only')
wfNetbootCurrDsuCsuOpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(56, 64))).clone(namedValues=NamedValues(("rate56k", 56), ("rate64k", 64))).clone('rate56k')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbootCurrDsuCsuOpMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbootCurrDsuCsuOpMode.setDescription('Dsu/Csu interface speed for Netbooting')
mibBuilder.exportSymbols("Wellfleet-SYS-SVC-MIB", wfNetbootProtoMask=wfNetbootProtoMask, wfNetbootSlot=wfNetbootSlot, wfNetbootImageNameCurr=wfNetbootImageNameCurr, wfNetbootCurrTable=wfNetbootCurrTable, wfNetbootCfgDelete=wfNetbootCfgDelete, wfNetbootConfigCurr=wfNetbootConfigCurr, wfNetbootCurrTokenRingSpeed=wfNetbootCurrTokenRingSpeed, wfNetbootCurrEntry=wfNetbootCurrEntry, wfNetbootCfgTable=wfNetbootCfgTable, wfNetbootCurrGroup=wfNetbootCurrGroup, wfNetbootDelete=wfNetbootDelete, wfNetbootDsuCsuOpMode=wfNetbootDsuCsuOpMode, wfNetbootCurrBchanRate=wfNetbootCurrBchanRate, wfNetbootServerAddress=wfNetbootServerAddress, wfNetbootCurrIpAddr=wfNetbootCurrIpAddr, wfNetbootCurrIpMask=wfNetbootCurrIpMask, wfNetbootCfgEntry=wfNetbootCfgEntry, wfNetbootCurrSlot=wfNetbootCurrSlot, wfNetbootCurrConnName=wfNetbootCurrConnName, wfNetbootTokenRingSpeed=wfNetbootTokenRingSpeed, wfNetbootImageName=wfNetbootImageName, wfNetbootCurrDisable=wfNetbootCurrDisable, wfNetbootIpMask=wfNetbootIpMask, wfNetbootCurrNextHop=wfNetbootCurrNextHop, wfNetbootNextHop=wfNetbootNextHop, wfNetbootConfigName=wfNetbootConfigName, wfNetbootCurrDsuCsuOpMode=wfNetbootCurrDsuCsuOpMode, wfNetbootIpAddr=wfNetbootIpAddr, wfNetbootImageCurr=wfNetbootImageCurr, wfNetbootCfgGroup=wfNetbootCfgGroup, wfNetbootBchanRate=wfNetbootBchanRate, wfNetbootConnector=wfNetbootConnector, wfNetbootConfig=wfNetbootConfig, wfNetbootConnName=wfNetbootConnName, wfNetbootImage=wfNetbootImage, wfNetbootCurrConnector=wfNetbootCurrConnector, wfNetbootServerAddressCurr=wfNetbootServerAddressCurr, wfNetbootConfigNameCurr=wfNetbootConfigNameCurr, wfNetbootDisable=wfNetbootDisable, wfNetbootCurrProtoMask=wfNetbootCurrProtoMask)
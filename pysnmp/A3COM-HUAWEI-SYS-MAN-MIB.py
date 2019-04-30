#
# PySNMP MIB module A3COM-HUAWEI-SYS-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-SYS-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
SnmpTagValue, SnmpTagList = mibBuilder.importSymbols("SNMP-TARGET-MIB", "SnmpTagValue", "SnmpTagList")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, MibIdentifier, Integer32, Unsigned32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, IpAddress, TimeTicks, Counter32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Integer32", "Unsigned32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "IpAddress", "TimeTicks", "Counter32", "ModuleIdentity", "ObjectIdentity")
TextualConvention, RowStatus, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "DateAndTime")
h3cSystemMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3))
h3cSystemMan.setRevisions(('2004-04-08 13:45',))
if mibBuilder.loadTexts: h3cSystemMan.setLastUpdated('200906070000Z')
if mibBuilder.loadTexts: h3cSystemMan.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cSystemManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1))
h3cSysClock = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1))
h3cSysLocalClock = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysLocalClock.setStatus('current')
h3cSysSummerTime = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1, 2))
h3cSysSummerTimeEnable = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysSummerTimeEnable.setStatus('current')
h3cSysSummerTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysSummerTimeZone.setStatus('current')
h3cSysSummerTimeMethod = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oneOff", 1), ("repeating", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysSummerTimeMethod.setStatus('current')
h3cSysSummerTimeStart = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1, 2, 4), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysSummerTimeStart.setStatus('current')
h3cSysSummerTimeEnd = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1, 2, 5), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysSummerTimeEnd.setStatus('current')
h3cSysSummerTimeOffset = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86399))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysSummerTimeOffset.setStatus('current')
h3cSysLocalClockString = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysLocalClockString.setStatus('current')
h3cSysCurrent = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 2))
h3cSysCurTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 2, 1), )
if mibBuilder.loadTexts: h3cSysCurTable.setStatus('current')
h3cSysCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCurEntPhysicalIndex"))
if mibBuilder.loadTexts: h3cSysCurEntry.setStatus('current')
h3cSysCurEntPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cSysCurEntPhysicalIndex.setStatus('current')
h3cSysCurCFGFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysCurCFGFileIndex.setStatus('current')
h3cSysCurImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysCurImageIndex.setStatus('current')
h3cSysCurBtmFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysCurBtmFileName.setStatus('current')
h3cSysCurUpdateBtmFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysCurUpdateBtmFileName.setStatus('current')
h3cSysReload = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3))
h3cSysReloadSchedule = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysReloadSchedule.setStatus('current')
h3cSysReloadAction = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("reloadUnavailable", 1), ("reloadOnSchedule", 2), ("reloadAtOnce", 3), ("reloadCancel", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysReloadAction.setStatus('current')
h3cSysReloadScheduleTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3), )
if mibBuilder.loadTexts: h3cSysReloadScheduleTable.setStatus('current')
h3cSysReloadScheduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadScheduleIndex"))
if mibBuilder.loadTexts: h3cSysReloadScheduleEntry.setStatus('current')
h3cSysReloadScheduleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cSysReloadScheduleIndex.setStatus('current')
h3cSysReloadEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysReloadEntity.setStatus('current')
h3cSysReloadCfgFile = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysReloadCfgFile.setStatus('current')
h3cSysReloadImage = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysReloadImage.setStatus('current')
h3cSysReloadReason = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysReloadReason.setStatus('current')
h3cSysReloadScheduleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3, 1, 6), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysReloadScheduleTime.setStatus('current')
h3cSysReloadRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysReloadRowStatus.setStatus('current')
h3cSysReloadScheduleTagList = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 3, 1, 8), SnmpTagList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysReloadScheduleTagList.setStatus('current')
h3cSysReloadTag = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 3, 4), SnmpTagValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysReloadTag.setStatus('current')
h3cSysImage = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 4))
h3cSysImageNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysImageNum.setStatus('current')
h3cSysImageTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 4, 2), )
if mibBuilder.loadTexts: h3cSysImageTable.setStatus('current')
h3cSysImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 4, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysImageIndex"))
if mibBuilder.loadTexts: h3cSysImageEntry.setStatus('current')
h3cSysImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cSysImageIndex.setStatus('current')
h3cSysImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 4, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysImageName.setStatus('current')
h3cSysImageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysImageSize.setStatus('current')
h3cSysImageLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 4, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysImageLocation.setStatus('current')
h3cSysImageType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("main", 1), ("backup", 2), ("none", 3), ("secure", 4), ("main-backup", 5), ("main-secure", 6), ("backup-secure", 7), ("main-backup-secure", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysImageType.setStatus('current')
h3cSysCFGFile = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 5))
h3cSysCFGFileNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysCFGFileNum.setStatus('current')
h3cSysCFGFileTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 5, 2), )
if mibBuilder.loadTexts: h3cSysCFGFileTable.setStatus('current')
h3cSysCFGFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 5, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCFGFileIndex"))
if mibBuilder.loadTexts: h3cSysCFGFileEntry.setStatus('current')
h3cSysCFGFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cSysCFGFileIndex.setStatus('current')
h3cSysCFGFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 5, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysCFGFileName.setStatus('current')
h3cSysCFGFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysCFGFileSize.setStatus('current')
h3cSysCFGFileLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 5, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysCFGFileLocation.setStatus('current')
h3cSysBtmFile = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6))
h3cSysBtmFileLoad = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 1))
h3cSysBtmLoadMaxNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysBtmLoadMaxNumber.setStatus('current')
h3cSysBtmLoadTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 2), )
if mibBuilder.loadTexts: h3cSysBtmLoadTable.setStatus('current')
h3cSysBtmLoadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysBtmLoadIndex"))
if mibBuilder.loadTexts: h3cSysBtmLoadEntry.setStatus('current')
h3cSysBtmLoadIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cSysBtmLoadIndex.setStatus('current')
h3cSysBtmFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysBtmFileName.setStatus('current')
h3cSysBtmFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("main", 1), ("none", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysBtmFileType.setStatus('current')
h3cSysBtmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysBtmRowStatus.setStatus('current')
h3cSysBtmErrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalidFile", 1), ("inProgress", 2), ("success", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysBtmErrorStatus.setStatus('current')
h3cSysBtmLoadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 6, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysBtmLoadTime.setStatus('current')
h3cSysPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7))
h3cSysPackageNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageNum.setStatus('current')
h3cSysPackageTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2), )
if mibBuilder.loadTexts: h3cSysPackageTable.setStatus('current')
h3cSysPackageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysPackageIndex"))
if mibBuilder.loadTexts: h3cSysPackageEntry.setStatus('current')
h3cSysPackageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cSysPackageIndex.setStatus('current')
h3cSysPackageName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageName.setStatus('current')
h3cSysPackageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageSize.setStatus('current')
h3cSysPackageLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageLocation.setStatus('current')
h3cSysPackageType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot", 1), ("system", 2), ("feature", 3), ("patch", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageType.setStatus('current')
h3cSysPackageAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("primary", 2), ("secondary", 3), ("primarySecondary", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysPackageAttribute.setStatus('current')
h3cSysPackageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageStatus.setStatus('current')
h3cSysPackageDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageDescription.setStatus('current')
h3cSysPackageFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageFeature.setStatus('current')
h3cSysPackageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageVersion.setStatus('current')
h3cSysPackageOperateEntryLimit = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSysPackageOperateEntryLimit.setStatus('current')
h3cSysPackageOperateTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 4), )
if mibBuilder.loadTexts: h3cSysPackageOperateTable.setStatus('current')
h3cSysPackageOperateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysPackageOperateIndex"))
if mibBuilder.loadTexts: h3cSysPackageOperateEntry.setStatus('current')
h3cSysPackageOperateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cSysPackageOperateIndex.setStatus('current')
h3cSysPackageOperatePackIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysPackageOperatePackIndex.setStatus('current')
h3cSysPackageOperateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysPackageOperateStatus.setStatus('current')
h3cSysPackageOperateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysPackageOperateRowStatus.setStatus('current')
h3cSysPackageOperateResult = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 7, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("opInProgress", 1), ("opSuccess", 2), ("opUnknownFailure", 3), ("opInvalidFile", 4), ("opNotSupport", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysPackageOperateResult.setStatus('current')
h3cSysIpeFile = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8))
h3cSysIpeFileNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpeFileNum.setStatus('current')
h3cSysIpeFileTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 2), )
if mibBuilder.loadTexts: h3cSysIpeFileTable.setStatus('current')
h3cSysIpeFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysIpeFileIndex"))
if mibBuilder.loadTexts: h3cSysIpeFileEntry.setStatus('current')
h3cSysIpeFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cSysIpeFileIndex.setStatus('current')
h3cSysIpeFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpeFileName.setStatus('current')
h3cSysIpeFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpeFileSize.setStatus('current')
h3cSysIpeFileLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpeFileLocation.setStatus('current')
h3cSysIpePackageTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 3), )
if mibBuilder.loadTexts: h3cSysIpePackageTable.setStatus('current')
h3cSysIpePackageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysIpeFileIndex"), (0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysIpePackageIndex"))
if mibBuilder.loadTexts: h3cSysIpePackageEntry.setStatus('current')
h3cSysIpePackageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cSysIpePackageIndex.setStatus('current')
h3cSysIpePackageName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpePackageName.setStatus('current')
h3cSysIpePackageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpePackageSize.setStatus('current')
h3cSysIpePackageType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot", 1), ("system", 2), ("feature", 3), ("patch", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpePackageType.setStatus('current')
h3cSysIpePackageDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpePackageDescription.setStatus('current')
h3cSysIpePackageFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpePackageFeature.setStatus('current')
h3cSysIpePackageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpePackageVersion.setStatus('current')
h3cSysIpeFileOperateTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 4), )
if mibBuilder.loadTexts: h3cSysIpeFileOperateTable.setStatus('current')
h3cSysIpeFileOperateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysIpeFileOperateIndex"))
if mibBuilder.loadTexts: h3cSysIpeFileOperateEntry.setStatus('current')
h3cSysIpeFileOperateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cSysIpeFileOperateIndex.setStatus('current')
h3cSysIpeFileOperateFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysIpeFileOperateFileIndex.setStatus('current')
h3cSysIpeFileOperateAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("primary", 2), ("secondary", 3), ("primarySecondary", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysIpeFileOperateAttribute.setStatus('current')
h3cSysIpeFileOperateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSysIpeFileOperateRowStatus.setStatus('current')
h3cSysIpeFileOperateResult = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 1, 8, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("opInProgress", 1), ("opSuccess", 2), ("opUnknownFailure", 3), ("opInvalidFile", 4), ("opDeviceFull", 5), ("opFileOpenError", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSysIpeFileOperateResult.setStatus('current')
h3cSystemManMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 2))
h3cSysClockChangedNotification = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 2, 1)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysLocalClock"))
if mibBuilder.loadTexts: h3cSysClockChangedNotification.setStatus('current')
h3cSysReloadNotification = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 2, 2)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadImage"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadCfgFile"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadReason"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadScheduleTime"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadAction"))
if mibBuilder.loadTexts: h3cSysReloadNotification.setStatus('current')
h3cSysStartUpNotification = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 2, 3)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysImageType"))
if mibBuilder.loadTexts: h3cSysStartUpNotification.setStatus('current')
h3cSystemManMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3))
h3cSystemManMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 1))
h3cSystemManMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 1, 1)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysClockGroup"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadGroup"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysImageGroup"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCFGFileGroup"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSystemManNotificationGroup"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCurGroup"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSystemBtmLoadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSystemManMIBCompliance = h3cSystemManMIBCompliance.setStatus('current')
h3cSystemManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 2))
h3cSysClockGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 2, 1)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysLocalClock"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysSummerTimeEnable"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysSummerTimeZone"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysSummerTimeMethod"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysSummerTimeStart"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysSummerTimeEnd"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysSummerTimeOffset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSysClockGroup = h3cSysClockGroup.setStatus('current')
h3cSysReloadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 2, 2)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadSchedule"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadAction"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadImage"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadCfgFile"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadReason"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadScheduleTagList"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadTag"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadScheduleTime"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadEntity"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSysReloadGroup = h3cSysReloadGroup.setStatus('current')
h3cSysImageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 2, 3)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysImageNum"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysImageName"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysImageSize"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysImageLocation"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysImageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSysImageGroup = h3cSysImageGroup.setStatus('current')
h3cSysCFGFileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 2, 4)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCFGFileNum"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCFGFileName"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCFGFileSize"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCFGFileLocation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSysCFGFileGroup = h3cSysCFGFileGroup.setStatus('current')
h3cSysCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 2, 5)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCurCFGFileIndex"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCurImageIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSysCurGroup = h3cSysCurGroup.setStatus('current')
h3cSystemManNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 2, 6)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysClockChangedNotification"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysReloadNotification"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysStartUpNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSystemManNotificationGroup = h3cSystemManNotificationGroup.setStatus('current')
h3cSystemBtmLoadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 3, 3, 2, 7)).setObjects(("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCurBtmFileName"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysCurUpdateBtmFileName"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysBtmLoadMaxNumber"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysBtmFileName"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysBtmFileType"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysBtmRowStatus"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysBtmErrorStatus"), ("A3COM-HUAWEI-SYS-MAN-MIB", "h3cSysBtmLoadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSystemBtmLoadGroup = h3cSystemBtmLoadGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-SYS-MAN-MIB", h3cSysCFGFileSize=h3cSysCFGFileSize, h3cSysImageSize=h3cSysImageSize, h3cSysBtmErrorStatus=h3cSysBtmErrorStatus, h3cSysIpeFileOperateTable=h3cSysIpeFileOperateTable, h3cSysReloadCfgFile=h3cSysReloadCfgFile, h3cSysCurEntry=h3cSysCurEntry, h3cSysReloadReason=h3cSysReloadReason, h3cSystemManMIBGroups=h3cSystemManMIBGroups, h3cSysIpeFileIndex=h3cSysIpeFileIndex, h3cSysCFGFileGroup=h3cSysCFGFileGroup, h3cSysSummerTime=h3cSysSummerTime, h3cSysCurTable=h3cSysCurTable, h3cSysPackageEntry=h3cSysPackageEntry, h3cSysBtmLoadTime=h3cSysBtmLoadTime, h3cSysIpeFileOperateFileIndex=h3cSysIpeFileOperateFileIndex, h3cSysPackageType=h3cSysPackageType, h3cSystemBtmLoadGroup=h3cSystemBtmLoadGroup, h3cSysBtmLoadMaxNumber=h3cSysBtmLoadMaxNumber, h3cSysIpePackageVersion=h3cSysIpePackageVersion, h3cSysImageType=h3cSysImageType, h3cSysPackageOperateEntryLimit=h3cSysPackageOperateEntryLimit, h3cSystemManMIBObjects=h3cSystemManMIBObjects, h3cSysSummerTimeMethod=h3cSysSummerTimeMethod, h3cSysIpePackageTable=h3cSysIpePackageTable, h3cSysPackageOperateEntry=h3cSysPackageOperateEntry, h3cSysIpeFileNum=h3cSysIpeFileNum, h3cSysBtmLoadTable=h3cSysBtmLoadTable, h3cSysIpeFileLocation=h3cSysIpeFileLocation, h3cSysPackageOperateResult=h3cSysPackageOperateResult, h3cSysIpePackageDescription=h3cSysIpePackageDescription, h3cSysSummerTimeEnd=h3cSysSummerTimeEnd, h3cSysClockChangedNotification=h3cSysClockChangedNotification, h3cSysSummerTimeStart=h3cSysSummerTimeStart, h3cSysPackageDescription=h3cSysPackageDescription, h3cSysReloadScheduleIndex=h3cSysReloadScheduleIndex, h3cSysSummerTimeOffset=h3cSysSummerTimeOffset, h3cSysClock=h3cSysClock, h3cSysIpeFileOperateEntry=h3cSysIpeFileOperateEntry, h3cSystemManMIBCompliances=h3cSystemManMIBCompliances, h3cSysReload=h3cSysReload, h3cSysReloadScheduleTable=h3cSysReloadScheduleTable, h3cSysPackageTable=h3cSysPackageTable, h3cSysIpePackageSize=h3cSysIpePackageSize, h3cSysPackageSize=h3cSysPackageSize, h3cSysIpeFile=h3cSysIpeFile, h3cSysImageNum=h3cSysImageNum, h3cSysIpePackageName=h3cSysIpePackageName, h3cSysCurImageIndex=h3cSysCurImageIndex, h3cSysReloadImage=h3cSysReloadImage, PYSNMP_MODULE_ID=h3cSystemMan, h3cSysPackageNum=h3cSysPackageNum, h3cSysBtmLoadEntry=h3cSysBtmLoadEntry, h3cSysImageEntry=h3cSysImageEntry, h3cSysClockGroup=h3cSysClockGroup, h3cSysCurGroup=h3cSysCurGroup, h3cSysCurCFGFileIndex=h3cSysCurCFGFileIndex, h3cSysStartUpNotification=h3cSysStartUpNotification, h3cSysImage=h3cSysImage, h3cSysBtmFileType=h3cSysBtmFileType, h3cSysIpeFileOperateResult=h3cSysIpeFileOperateResult, h3cSysImageIndex=h3cSysImageIndex, h3cSysReloadSchedule=h3cSysReloadSchedule, h3cSysBtmFileName=h3cSysBtmFileName, h3cSysCurEntPhysicalIndex=h3cSysCurEntPhysicalIndex, h3cSysCFGFileTable=h3cSysCFGFileTable, h3cSysBtmFileLoad=h3cSysBtmFileLoad, h3cSysBtmFile=h3cSysBtmFile, h3cSysSummerTimeZone=h3cSysSummerTimeZone, h3cSysIpeFileName=h3cSysIpeFileName, h3cSysReloadScheduleTime=h3cSysReloadScheduleTime, h3cSysPackageStatus=h3cSysPackageStatus, h3cSysSummerTimeEnable=h3cSysSummerTimeEnable, h3cSysIpeFileOperateIndex=h3cSysIpeFileOperateIndex, h3cSysIpeFileSize=h3cSysIpeFileSize, h3cSysPackageFeature=h3cSysPackageFeature, h3cSysImageLocation=h3cSysImageLocation, h3cSysCFGFileLocation=h3cSysCFGFileLocation, h3cSysBtmRowStatus=h3cSysBtmRowStatus, h3cSysPackageOperateStatus=h3cSysPackageOperateStatus, h3cSysPackageOperateTable=h3cSysPackageOperateTable, h3cSysCFGFileIndex=h3cSysCFGFileIndex, h3cSysReloadGroup=h3cSysReloadGroup, h3cSysPackageLocation=h3cSysPackageLocation, h3cSysPackageAttribute=h3cSysPackageAttribute, h3cSysImageGroup=h3cSysImageGroup, h3cSysReloadNotification=h3cSysReloadNotification, h3cSysCFGFileNum=h3cSysCFGFileNum, h3cSysPackageOperateRowStatus=h3cSysPackageOperateRowStatus, h3cSysIpePackageFeature=h3cSysIpePackageFeature, h3cSysIpePackageIndex=h3cSysIpePackageIndex, h3cSysCFGFile=h3cSysCFGFile, h3cSysIpeFileOperateRowStatus=h3cSysIpeFileOperateRowStatus, h3cSysImageTable=h3cSysImageTable, h3cSysLocalClockString=h3cSysLocalClockString, h3cSystemManMIBNotifications=h3cSystemManMIBNotifications, h3cSysImageName=h3cSysImageName, h3cSystemManMIBConformance=h3cSystemManMIBConformance, h3cSysReloadRowStatus=h3cSysReloadRowStatus, h3cSysCFGFileName=h3cSysCFGFileName, h3cSysIpeFileTable=h3cSysIpeFileTable, h3cSystemManMIBCompliance=h3cSystemManMIBCompliance, h3cSysPackageIndex=h3cSysPackageIndex, h3cSysIpePackageType=h3cSysIpePackageType, h3cSysIpePackageEntry=h3cSysIpePackageEntry, h3cSysReloadAction=h3cSysReloadAction, h3cSysPackage=h3cSysPackage, h3cSysReloadScheduleTagList=h3cSysReloadScheduleTagList, h3cSysCurUpdateBtmFileName=h3cSysCurUpdateBtmFileName, h3cSysIpeFileEntry=h3cSysIpeFileEntry, h3cSysCurBtmFileName=h3cSysCurBtmFileName, h3cSystemManNotificationGroup=h3cSystemManNotificationGroup, h3cSysBtmLoadIndex=h3cSysBtmLoadIndex, h3cSysReloadTag=h3cSysReloadTag, h3cSysPackageOperatePackIndex=h3cSysPackageOperatePackIndex, h3cSysPackageOperateIndex=h3cSysPackageOperateIndex, h3cSysPackageName=h3cSysPackageName, h3cSysIpeFileOperateAttribute=h3cSysIpeFileOperateAttribute, h3cSystemMan=h3cSystemMan, h3cSysLocalClock=h3cSysLocalClock, h3cSysReloadScheduleEntry=h3cSysReloadScheduleEntry, h3cSysPackageVersion=h3cSysPackageVersion, h3cSysCurrent=h3cSysCurrent, h3cSysCFGFileEntry=h3cSysCFGFileEntry, h3cSysReloadEntity=h3cSysReloadEntity)

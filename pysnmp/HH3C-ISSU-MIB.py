#
# PySNMP MIB module HH3C-ISSU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-ISSU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, MibIdentifier, ObjectIdentity, Gauge32, Bits, Integer32, Counter32, TimeTicks, Counter64, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Gauge32", "Bits", "Integer32", "Counter32", "TimeTicks", "Counter64", "IpAddress", "NotificationType")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
hh3cIssuUpgrade = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 133))
hh3cIssuUpgrade.setRevisions(('2013-01-15 15:36',))
if mibBuilder.loadTexts: hh3cIssuUpgrade.setLastUpdated('201301151536Z')
if mibBuilder.loadTexts: hh3cIssuUpgrade.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cIssuUpgradeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1))
hh3cIssuUpgradeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1))
hh3cIssuUpgradeImageTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cIssuUpgradeImageTable.setStatus('current')
hh3cIssuUpgradeImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1), ).setIndexNames((0, "HH3C-ISSU-MIB", "hh3cIssuUpgradeImageIndex"))
if mibBuilder.loadTexts: hh3cIssuUpgradeImageEntry.setStatus('current')
hh3cIssuUpgradeImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cIssuUpgradeImageIndex.setStatus('current')
hh3cIssuUpgradeImageType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot", 1), ("system", 2), ("feature", 3), ("ipe", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIssuUpgradeImageType.setStatus('current')
hh3cIssuUpgradeImageURL = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIssuUpgradeImageURL.setStatus('current')
hh3cIssuUpgradeImageRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIssuUpgradeImageRowStatus.setStatus('current')
hh3cIssuOp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2))
hh3cIssuOpType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("done", 2), ("test", 3), ("install", 4), ("rollback", 5))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIssuOpType.setStatus('current')
hh3cIssuImageFileOverwrite = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIssuImageFileOverwrite.setStatus('current')
hh3cIssuOpTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIssuOpTrapEnable.setStatus('current')
hh3cIssuOpStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("failure", 2), ("inProgress", 3), ("success", 4), ("rollbackInProgress", 5), ("rollbackSuccess", 6))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuOpStatus.setStatus('current')
hh3cIssuFailedReason = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuFailedReason.setStatus('current')
hh3cIssuOpTimeCompleted = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuOpTimeCompleted.setStatus('current')
hh3cIssuLastOpType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("done", 2), ("test", 3), ("install", 4), ("rollback", 5))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuLastOpType.setStatus('current')
hh3cIssuLastOpStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("failure", 2), ("inProgress", 3), ("success", 4), ("rollbackInProgress", 5), ("rollbackSuccess", 6))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuLastOpStatus.setStatus('current')
hh3cIssuLastOpFailedReason = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuLastOpFailedReason.setStatus('current')
hh3cIssuLastOpTimeCompleted = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuLastOpTimeCompleted.setStatus('current')
hh3cIssuUpgradeResultGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2))
hh3cIssuCompatibleResult = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 1))
hh3cIssuCompatibleResultStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("inCompatible", 2), ("compatible", 3), ("failure", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuCompatibleResultStatus.setStatus('current')
hh3cIssuCompatibleResultFailedReason = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuCompatibleResultFailedReason.setStatus('current')
hh3cIssuTestResultTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2), )
if mibBuilder.loadTexts: hh3cIssuTestResultTable.setStatus('current')
hh3cIssuTestResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1), ).setIndexNames((0, "HH3C-ISSU-MIB", "hh3cIssuTestResultIndex"))
if mibBuilder.loadTexts: hh3cIssuTestResultEntry.setStatus('current')
hh3cIssuTestResultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cIssuTestResultIndex.setStatus('current')
hh3cIssuTestDeviceChassisID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuTestDeviceChassisID.setStatus('current')
hh3cIssuTestDeviceSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuTestDeviceSlotID.setStatus('current')
hh3cIssuTestDeviceCpuID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuTestDeviceCpuID.setStatus('current')
hh3cIssuTestDeviceUpgradeWay = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("reboot", 2), ("sequenceReboot", 3), ("issuReboot", 4), ("serviceUpgrade", 5), ("fileUpgrade", 6), ("incompatibleUpgrade", 7))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuTestDeviceUpgradeWay.setStatus('current')
hh3cIssuUpgradeResultTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3), )
if mibBuilder.loadTexts: hh3cIssuUpgradeResultTable.setStatus('current')
hh3cIssuUpgradeResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1), ).setIndexNames((0, "HH3C-ISSU-MIB", "hh3cIssuUpgradeResultIndex"))
if mibBuilder.loadTexts: hh3cIssuUpgradeResultEntry.setStatus('current')
hh3cIssuUpgradeResultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cIssuUpgradeResultIndex.setStatus('current')
hh3cIssuUpgradeDeviceChassisID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuUpgradeDeviceChassisID.setStatus('current')
hh3cIssuUpgradeDeviceSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuUpgradeDeviceSlotID.setStatus('current')
hh3cIssuUpgradeDeviceCpuID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuUpgradeDeviceCpuID.setStatus('current')
hh3cIssuUpgradeState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("init", 1), ("loading", 2), ("loaded", 3), ("switching", 4), ("switchover", 5), ("committing", 6), ("committed", 7), ("rollbacking", 8), ("rollbacked", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuUpgradeState.setStatus('current')
hh3cIssuDeviceUpgradeWay = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("reboot", 2), ("sequenceReboot", 3), ("issuReboot", 4), ("serviceUpgrade", 5), ("fileUpgrade", 6), ("incompatibleUpgrade", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuDeviceUpgradeWay.setStatus('current')
hh3cIssuUpgradeDeviceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("waitingUpgrade", 1), ("inProcess", 2), ("success", 3), ("failure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuUpgradeDeviceStatus.setStatus('current')
hh3cIssuUpgradeFailedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIssuUpgradeFailedReason.setStatus('current')
hh3cIssuUpgradeNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 133, 2))
hh3cIssuUpgradeTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 133, 2, 0))
hh3cIssuUpgradeOpCompletionNotify = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 133, 2, 0, 1)).setObjects(("HH3C-ISSU-MIB", "hh3cIssuOpType"), ("HH3C-ISSU-MIB", "hh3cIssuOpStatus"), ("HH3C-ISSU-MIB", "hh3cIssuFailedReason"), ("HH3C-ISSU-MIB", "hh3cIssuOpTimeCompleted"))
if mibBuilder.loadTexts: hh3cIssuUpgradeOpCompletionNotify.setStatus('current')
mibBuilder.exportSymbols("HH3C-ISSU-MIB", hh3cIssuUpgradeResultTable=hh3cIssuUpgradeResultTable, hh3cIssuTestDeviceChassisID=hh3cIssuTestDeviceChassisID, hh3cIssuUpgradeImageEntry=hh3cIssuUpgradeImageEntry, hh3cIssuImageFileOverwrite=hh3cIssuImageFileOverwrite, hh3cIssuUpgradeImageTable=hh3cIssuUpgradeImageTable, hh3cIssuUpgradeResultIndex=hh3cIssuUpgradeResultIndex, hh3cIssuCompatibleResultFailedReason=hh3cIssuCompatibleResultFailedReason, hh3cIssuOpType=hh3cIssuOpType, hh3cIssuTestResultTable=hh3cIssuTestResultTable, hh3cIssuTestResultIndex=hh3cIssuTestResultIndex, hh3cIssuUpgradeDeviceSlotID=hh3cIssuUpgradeDeviceSlotID, hh3cIssuLastOpTimeCompleted=hh3cIssuLastOpTimeCompleted, hh3cIssuUpgradeResultEntry=hh3cIssuUpgradeResultEntry, hh3cIssuUpgradeOpCompletionNotify=hh3cIssuUpgradeOpCompletionNotify, hh3cIssuLastOpStatus=hh3cIssuLastOpStatus, hh3cIssuOpTimeCompleted=hh3cIssuOpTimeCompleted, hh3cIssuCompatibleResultStatus=hh3cIssuCompatibleResultStatus, hh3cIssuUpgradeDeviceChassisID=hh3cIssuUpgradeDeviceChassisID, hh3cIssuTestDeviceUpgradeWay=hh3cIssuTestDeviceUpgradeWay, hh3cIssuDeviceUpgradeWay=hh3cIssuDeviceUpgradeWay, hh3cIssuOp=hh3cIssuOp, hh3cIssuUpgradeImageType=hh3cIssuUpgradeImageType, hh3cIssuUpgradeImageURL=hh3cIssuUpgradeImageURL, hh3cIssuLastOpType=hh3cIssuLastOpType, hh3cIssuTestDeviceCpuID=hh3cIssuTestDeviceCpuID, hh3cIssuUpgradeGroup=hh3cIssuUpgradeGroup, hh3cIssuUpgradeFailedReason=hh3cIssuUpgradeFailedReason, hh3cIssuUpgradeMibObjects=hh3cIssuUpgradeMibObjects, hh3cIssuLastOpFailedReason=hh3cIssuLastOpFailedReason, hh3cIssuUpgradeTrapPrefix=hh3cIssuUpgradeTrapPrefix, hh3cIssuOpStatus=hh3cIssuOpStatus, hh3cIssuUpgradeImageIndex=hh3cIssuUpgradeImageIndex, hh3cIssuUpgrade=hh3cIssuUpgrade, hh3cIssuUpgradeDeviceStatus=hh3cIssuUpgradeDeviceStatus, hh3cIssuCompatibleResult=hh3cIssuCompatibleResult, hh3cIssuUpgradeState=hh3cIssuUpgradeState, hh3cIssuOpTrapEnable=hh3cIssuOpTrapEnable, hh3cIssuUpgradeDeviceCpuID=hh3cIssuUpgradeDeviceCpuID, hh3cIssuUpgradeResultGroup=hh3cIssuUpgradeResultGroup, hh3cIssuUpgradeImageRowStatus=hh3cIssuUpgradeImageRowStatus, hh3cIssuFailedReason=hh3cIssuFailedReason, hh3cIssuTestDeviceSlotID=hh3cIssuTestDeviceSlotID, hh3cIssuUpgradeNotify=hh3cIssuUpgradeNotify, hh3cIssuTestResultEntry=hh3cIssuTestResultEntry, PYSNMP_MODULE_ID=hh3cIssuUpgrade)
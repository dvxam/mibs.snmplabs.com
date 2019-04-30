#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-GMETA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-GMETA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:59:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, CiscoNetworkAddress, CiscoInetAddressMask, Unsigned64, CiscoAlarmSeverity = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec", "CiscoNetworkAddress", "CiscoInetAddressMask", "Unsigned64", "CiscoAlarmSeverity")
ciscoUnifiedComputingMIBObjects, CucsManagedObjectId, CucsManagedObjectDn = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectId", "CucsManagedObjectDn")
CucsGmetaHolderFsmTaskItem, CucsGmetaVersion, CucsFsmFsmStageStatus, CucsFsmCompletion, CucsMoMoClassId, CucsGmetaHolderFsmStageName, CucsGmetaPollInterval, CucsGmetaHolderFsmCurrentFsm, CucsGmetaInventoryStatus, CucsExtpolConnType, CucsGmetaHolderFsmTaskFlags, CucsConditionRemoteInvRslt, CucsGmetaCategory = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsGmetaHolderFsmTaskItem", "CucsGmetaVersion", "CucsFsmFsmStageStatus", "CucsFsmCompletion", "CucsMoMoClassId", "CucsGmetaHolderFsmStageName", "CucsGmetaPollInterval", "CucsGmetaHolderFsmCurrentFsm", "CucsGmetaInventoryStatus", "CucsExtpolConnType", "CucsGmetaHolderFsmTaskFlags", "CucsConditionRemoteInvRslt", "CucsGmetaCategory")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ObjectIdentity, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, ModuleIdentity, Counter32, iso, NotificationType, Integer32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter32", "iso", "NotificationType", "Integer32", "Unsigned32", "Bits")
TruthValue, TimeInterval, MacAddress, DisplayString, DateAndTime, TextualConvention, RowPointer, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeInterval", "MacAddress", "DisplayString", "DateAndTime", "TextualConvention", "RowPointer", "TimeStamp")
cucsGmetaObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72))
if mibBuilder.loadTexts: cucsGmetaObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsGmetaObjects.setOrganization('Cisco Systems Inc.')
cucsGmetaClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1), )
if mibBuilder.loadTexts: cucsGmetaClassTable.setStatus('current')
cucsGmetaClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaClassInstanceId"))
if mibBuilder.loadTexts: cucsGmetaClassEntry.setStatus('current')
cucsGmetaClassInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGmetaClassInstanceId.setStatus('current')
cucsGmetaClassDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaClassDn.setStatus('current')
cucsGmetaClassRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaClassRn.setStatus('current')
cucsGmetaClassAdminPropMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 4), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaClassAdminPropMask.setStatus('current')
cucsGmetaClassEpClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 5), CucsMoMoClassId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaClassEpClassId.setStatus('current')
cucsGmetaClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaClassId.setStatus('current')
cucsGmetaClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaClassName.setStatus('current')
cucsGmetaClassOperPropMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 8), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaClassOperPropMask.setStatus('current')
cucsGmetaEpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2), )
if mibBuilder.loadTexts: cucsGmetaEpTable.setStatus('current')
cucsGmetaEpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaEpInstanceId"))
if mibBuilder.loadTexts: cucsGmetaEpEntry.setStatus('current')
cucsGmetaEpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGmetaEpInstanceId.setStatus('current')
cucsGmetaEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaEpDn.setStatus('current')
cucsGmetaEpRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaEpRn.setStatus('current')
cucsGmetaHolderTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3), )
if mibBuilder.loadTexts: cucsGmetaHolderTable.setStatus('current')
cucsGmetaHolderEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaHolderInstanceId"))
if mibBuilder.loadTexts: cucsGmetaHolderEntry.setStatus('current')
cucsGmetaHolderInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGmetaHolderInstanceId.setStatus('current')
cucsGmetaHolderDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderDn.setStatus('current')
cucsGmetaHolderRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderRn.setStatus('current')
cucsGmetaHolderCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 4), CucsGmetaCategory()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderCategory.setStatus('current')
cucsGmetaHolderFsmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmDescr.setStatus('current')
cucsGmetaHolderFsmFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmFlags.setStatus('current')
cucsGmetaHolderFsmPrev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmPrev.setStatus('current')
cucsGmetaHolderFsmProgr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmProgr.setStatus('current')
cucsGmetaHolderFsmRmtInvErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmRmtInvErrCode.setStatus('current')
cucsGmetaHolderFsmRmtInvErrDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmRmtInvErrDescr.setStatus('current')
cucsGmetaHolderFsmRmtInvRslt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 11), CucsConditionRemoteInvRslt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmRmtInvRslt.setStatus('current')
cucsGmetaHolderFsmStageDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageDescr.setStatus('current')
cucsGmetaHolderFsmStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 13), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStamp.setStatus('current')
cucsGmetaHolderFsmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStatus.setStatus('current')
cucsGmetaHolderFsmTry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmTry.setStatus('current')
cucsGmetaHolderInventoryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 16), CucsGmetaInventoryStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderInventoryStatus.setStatus('current')
cucsGmetaHolderPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 17), CucsGmetaPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderPollInterval.setStatus('current')
cucsGmetaHolderProvider = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 18), CucsExtpolConnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderProvider.setStatus('current')
cucsGmetaHolderInventoryVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 19), CucsGmetaVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderInventoryVersion.setStatus('current')
cucsGmetaHolderGenNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderGenNum.setStatus('current')
cucsGmetaHolderFsmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4), )
if mibBuilder.loadTexts: cucsGmetaHolderFsmTable.setStatus('current')
cucsGmetaHolderFsmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaHolderFsmInstanceId"))
if mibBuilder.loadTexts: cucsGmetaHolderFsmEntry.setStatus('current')
cucsGmetaHolderFsmInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGmetaHolderFsmInstanceId.setStatus('current')
cucsGmetaHolderFsmDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmDn.setStatus('current')
cucsGmetaHolderFsmRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmRn.setStatus('current')
cucsGmetaHolderFsmCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmCompletionTime.setStatus('current')
cucsGmetaHolderFsmCurrentFsm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 5), CucsGmetaHolderFsmCurrentFsm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmCurrentFsm.setStatus('current')
cucsGmetaHolderFsmDescrData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmDescrData.setStatus('current')
cucsGmetaHolderFsmFsmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 7), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmFsmStatus.setStatus('current')
cucsGmetaHolderFsmProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmProgress.setStatus('current')
cucsGmetaHolderFsmRmtErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmRmtErrCode.setStatus('current')
cucsGmetaHolderFsmRmtErrDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmRmtErrDescr.setStatus('current')
cucsGmetaHolderFsmRmtRslt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 11), CucsConditionRemoteInvRslt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmRmtRslt.setStatus('current')
cucsGmetaHolderFsmStageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5), )
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageTable.setStatus('current')
cucsGmetaHolderFsmStageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaHolderFsmStageInstanceId"))
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageEntry.setStatus('current')
cucsGmetaHolderFsmStageInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageInstanceId.setStatus('current')
cucsGmetaHolderFsmStageDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageDn.setStatus('current')
cucsGmetaHolderFsmStageRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageRn.setStatus('current')
cucsGmetaHolderFsmStageDescrData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageDescrData.setStatus('current')
cucsGmetaHolderFsmStageLastUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageLastUpdateTime.setStatus('current')
cucsGmetaHolderFsmStageName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 6), CucsGmetaHolderFsmStageName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageName.setStatus('current')
cucsGmetaHolderFsmStageOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageOrder.setStatus('current')
cucsGmetaHolderFsmStageRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageRetry.setStatus('current')
cucsGmetaHolderFsmStageStageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 9), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmStageStageStatus.setStatus('current')
cucsGmetaHolderFsmTaskTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6), )
if mibBuilder.loadTexts: cucsGmetaHolderFsmTaskTable.setStatus('current')
cucsGmetaHolderFsmTaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaHolderFsmTaskInstanceId"))
if mibBuilder.loadTexts: cucsGmetaHolderFsmTaskEntry.setStatus('current')
cucsGmetaHolderFsmTaskInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGmetaHolderFsmTaskInstanceId.setStatus('current')
cucsGmetaHolderFsmTaskDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmTaskDn.setStatus('current')
cucsGmetaHolderFsmTaskRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmTaskRn.setStatus('current')
cucsGmetaHolderFsmTaskCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 4), CucsFsmCompletion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmTaskCompletion.setStatus('current')
cucsGmetaHolderFsmTaskFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 5), CucsGmetaHolderFsmTaskFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmTaskFlags.setStatus('current')
cucsGmetaHolderFsmTaskItem = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 6), CucsGmetaHolderFsmTaskItem()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmTaskItem.setStatus('current')
cucsGmetaHolderFsmTaskSeqId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaHolderFsmTaskSeqId.setStatus('current')
cucsGmetaPolicyMapElementTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7), )
if mibBuilder.loadTexts: cucsGmetaPolicyMapElementTable.setStatus('current')
cucsGmetaPolicyMapElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaPolicyMapElementInstanceId"))
if mibBuilder.loadTexts: cucsGmetaPolicyMapElementEntry.setStatus('current')
cucsGmetaPolicyMapElementInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGmetaPolicyMapElementInstanceId.setStatus('current')
cucsGmetaPolicyMapElementDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPolicyMapElementDn.setStatus('current')
cucsGmetaPolicyMapElementRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPolicyMapElementRn.setStatus('current')
cucsGmetaPolicyMapElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPolicyMapElementName.setStatus('current')
cucsGmetaPolicyMapHolderTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8), )
if mibBuilder.loadTexts: cucsGmetaPolicyMapHolderTable.setStatus('current')
cucsGmetaPolicyMapHolderEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaPolicyMapHolderInstanceId"))
if mibBuilder.loadTexts: cucsGmetaPolicyMapHolderEntry.setStatus('current')
cucsGmetaPolicyMapHolderInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGmetaPolicyMapHolderInstanceId.setStatus('current')
cucsGmetaPolicyMapHolderDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPolicyMapHolderDn.setStatus('current')
cucsGmetaPolicyMapHolderRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPolicyMapHolderRn.setStatus('current')
cucsGmetaPropTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9), )
if mibBuilder.loadTexts: cucsGmetaPropTable.setStatus('current')
cucsGmetaPropEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaPropInstanceId"))
if mibBuilder.loadTexts: cucsGmetaPropEntry.setStatus('current')
cucsGmetaPropInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGmetaPropInstanceId.setStatus('current')
cucsGmetaPropDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPropDn.setStatus('current')
cucsGmetaPropRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPropRn.setStatus('current')
cucsGmetaPropName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPropName.setStatus('current')
cucsGmetaPropOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPropOrder.setStatus('current')
cucsGmetaPropPropId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGmetaPropPropId.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-GMETA-MIB", cucsGmetaEpEntry=cucsGmetaEpEntry, cucsGmetaHolderFsmInstanceId=cucsGmetaHolderFsmInstanceId, cucsGmetaPropRn=cucsGmetaPropRn, cucsGmetaHolderFsmTaskSeqId=cucsGmetaHolderFsmTaskSeqId, cucsGmetaEpRn=cucsGmetaEpRn, cucsGmetaHolderCategory=cucsGmetaHolderCategory, cucsGmetaHolderTable=cucsGmetaHolderTable, cucsGmetaHolderFsmStageLastUpdateTime=cucsGmetaHolderFsmStageLastUpdateTime, cucsGmetaClassDn=cucsGmetaClassDn, cucsGmetaHolderFsmTaskEntry=cucsGmetaHolderFsmTaskEntry, cucsGmetaPolicyMapElementEntry=cucsGmetaPolicyMapElementEntry, cucsGmetaHolderDn=cucsGmetaHolderDn, cucsGmetaClassTable=cucsGmetaClassTable, cucsGmetaHolderFsmRmtErrCode=cucsGmetaHolderFsmRmtErrCode, cucsGmetaHolderFsmRmtInvRslt=cucsGmetaHolderFsmRmtInvRslt, cucsGmetaHolderFsmTaskTable=cucsGmetaHolderFsmTaskTable, cucsGmetaClassOperPropMask=cucsGmetaClassOperPropMask, cucsGmetaHolderFsmProgr=cucsGmetaHolderFsmProgr, cucsGmetaHolderProvider=cucsGmetaHolderProvider, cucsGmetaClassAdminPropMask=cucsGmetaClassAdminPropMask, cucsGmetaHolderFsmEntry=cucsGmetaHolderFsmEntry, cucsGmetaHolderFsmPrev=cucsGmetaHolderFsmPrev, cucsGmetaHolderFsmRn=cucsGmetaHolderFsmRn, cucsGmetaHolderFsmTry=cucsGmetaHolderFsmTry, cucsGmetaHolderGenNum=cucsGmetaHolderGenNum, cucsGmetaHolderFsmStamp=cucsGmetaHolderFsmStamp, cucsGmetaPolicyMapElementTable=cucsGmetaPolicyMapElementTable, cucsGmetaHolderFsmStageRetry=cucsGmetaHolderFsmStageRetry, cucsGmetaHolderFsmTaskItem=cucsGmetaHolderFsmTaskItem, cucsGmetaHolderFsmStatus=cucsGmetaHolderFsmStatus, cucsGmetaHolderPollInterval=cucsGmetaHolderPollInterval, cucsGmetaPropOrder=cucsGmetaPropOrder, cucsGmetaPolicyMapHolderRn=cucsGmetaPolicyMapHolderRn, cucsGmetaHolderFsmTaskRn=cucsGmetaHolderFsmTaskRn, cucsGmetaHolderFsmCurrentFsm=cucsGmetaHolderFsmCurrentFsm, cucsGmetaPolicyMapElementName=cucsGmetaPolicyMapElementName, cucsGmetaHolderInventoryVersion=cucsGmetaHolderInventoryVersion, cucsGmetaEpInstanceId=cucsGmetaEpInstanceId, cucsGmetaClassInstanceId=cucsGmetaClassInstanceId, cucsGmetaHolderInventoryStatus=cucsGmetaHolderInventoryStatus, cucsGmetaPropEntry=cucsGmetaPropEntry, cucsGmetaHolderFsmRmtErrDescr=cucsGmetaHolderFsmRmtErrDescr, cucsGmetaHolderFsmTaskDn=cucsGmetaHolderFsmTaskDn, cucsGmetaHolderFsmDescr=cucsGmetaHolderFsmDescr, cucsGmetaPropInstanceId=cucsGmetaPropInstanceId, cucsGmetaHolderFsmProgress=cucsGmetaHolderFsmProgress, cucsGmetaHolderFsmStageTable=cucsGmetaHolderFsmStageTable, cucsGmetaObjects=cucsGmetaObjects, cucsGmetaHolderFsmFsmStatus=cucsGmetaHolderFsmFsmStatus, cucsGmetaHolderFsmStageDn=cucsGmetaHolderFsmStageDn, cucsGmetaEpDn=cucsGmetaEpDn, cucsGmetaHolderInstanceId=cucsGmetaHolderInstanceId, cucsGmetaHolderFsmRmtRslt=cucsGmetaHolderFsmRmtRslt, cucsGmetaPropName=cucsGmetaPropName, cucsGmetaPolicyMapHolderTable=cucsGmetaPolicyMapHolderTable, cucsGmetaHolderFsmStageDescr=cucsGmetaHolderFsmStageDescr, cucsGmetaHolderFsmStageOrder=cucsGmetaHolderFsmStageOrder, cucsGmetaHolderFsmStageName=cucsGmetaHolderFsmStageName, cucsGmetaHolderFsmTable=cucsGmetaHolderFsmTable, cucsGmetaPolicyMapElementRn=cucsGmetaPolicyMapElementRn, cucsGmetaPolicyMapElementInstanceId=cucsGmetaPolicyMapElementInstanceId, cucsGmetaClassId=cucsGmetaClassId, cucsGmetaHolderFsmTaskInstanceId=cucsGmetaHolderFsmTaskInstanceId, cucsGmetaHolderFsmStageStageStatus=cucsGmetaHolderFsmStageStageStatus, cucsGmetaEpTable=cucsGmetaEpTable, cucsGmetaPolicyMapHolderEntry=cucsGmetaPolicyMapHolderEntry, cucsGmetaHolderFsmFlags=cucsGmetaHolderFsmFlags, cucsGmetaClassEpClassId=cucsGmetaClassEpClassId, cucsGmetaHolderFsmStageEntry=cucsGmetaHolderFsmStageEntry, cucsGmetaClassName=cucsGmetaClassName, cucsGmetaHolderFsmStageInstanceId=cucsGmetaHolderFsmStageInstanceId, cucsGmetaHolderFsmDescrData=cucsGmetaHolderFsmDescrData, cucsGmetaHolderFsmDn=cucsGmetaHolderFsmDn, cucsGmetaHolderFsmStageRn=cucsGmetaHolderFsmStageRn, PYSNMP_MODULE_ID=cucsGmetaObjects, cucsGmetaHolderFsmStageDescrData=cucsGmetaHolderFsmStageDescrData, cucsGmetaPolicyMapElementDn=cucsGmetaPolicyMapElementDn, cucsGmetaHolderFsmTaskCompletion=cucsGmetaHolderFsmTaskCompletion, cucsGmetaClassRn=cucsGmetaClassRn, cucsGmetaClassEntry=cucsGmetaClassEntry, cucsGmetaPropTable=cucsGmetaPropTable, cucsGmetaPolicyMapHolderDn=cucsGmetaPolicyMapHolderDn, cucsGmetaPropDn=cucsGmetaPropDn, cucsGmetaHolderFsmTaskFlags=cucsGmetaHolderFsmTaskFlags, cucsGmetaHolderEntry=cucsGmetaHolderEntry, cucsGmetaHolderFsmRmtInvErrCode=cucsGmetaHolderFsmRmtInvErrCode, cucsGmetaPolicyMapHolderInstanceId=cucsGmetaPolicyMapHolderInstanceId, cucsGmetaHolderRn=cucsGmetaHolderRn, cucsGmetaPropPropId=cucsGmetaPropPropId, cucsGmetaHolderFsmCompletionTime=cucsGmetaHolderFsmCompletionTime, cucsGmetaHolderFsmRmtInvErrDescr=cucsGmetaHolderFsmRmtInvErrDescr)

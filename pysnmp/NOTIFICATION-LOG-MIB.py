#
# PySNMP MIB module NOTIFICATION-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOTIFICATION-LOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:14:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
SnmpAdminString, SnmpEngineID = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpEngineID")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, mib_2, MibIdentifier, iso, TimeTicks, Bits, ModuleIdentity, Gauge32, ObjectIdentity, Unsigned32, NotificationType, Counter64, IpAddress, Opaque, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "mib-2", "MibIdentifier", "iso", "TimeTicks", "Bits", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "Counter64", "IpAddress", "Opaque", "Integer32")
TextualConvention, RowStatus, DisplayString, TimeStamp, DateAndTime, TDomain, StorageType, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TimeStamp", "DateAndTime", "TDomain", "StorageType", "TAddress")
notificationLogMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 92))
notificationLogMIB.setRevisions(('2000-11-27 00:00',))
if mibBuilder.loadTexts: notificationLogMIB.setLastUpdated('200011270000Z')
if mibBuilder.loadTexts: notificationLogMIB.setOrganization('IETF Distributed Management Working Group')
notificationLogMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 1))
nlmConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 1, 1))
nlmStats = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 1, 2))
nlmLog = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 1, 3))
nlmConfigGlobalEntryLimit = MibScalar((1, 3, 6, 1, 2, 1, 92, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nlmConfigGlobalEntryLimit.setStatus('current')
nlmConfigGlobalAgeOut = MibScalar((1, 3, 6, 1, 2, 1, 92, 1, 1, 2), Unsigned32()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: nlmConfigGlobalAgeOut.setStatus('current')
nlmConfigLogTable = MibTable((1, 3, 6, 1, 2, 1, 92, 1, 1, 3), )
if mibBuilder.loadTexts: nlmConfigLogTable.setStatus('current')
nlmConfigLogEntry = MibTableRow((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1), ).setIndexNames((0, "NOTIFICATION-LOG-MIB", "nlmLogName"))
if mibBuilder.loadTexts: nlmConfigLogEntry.setStatus('current')
nlmLogName = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: nlmLogName.setStatus('current')
nlmConfigLogFilterName = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nlmConfigLogFilterName.setStatus('current')
nlmConfigLogEntryLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nlmConfigLogEntryLimit.setStatus('current')
nlmConfigLogAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nlmConfigLogAdminStatus.setStatus('current')
nlmConfigLogOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("operational", 2), ("noFilter", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmConfigLogOperStatus.setStatus('current')
nlmConfigLogStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nlmConfigLogStorageType.setStatus('current')
nlmConfigLogEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nlmConfigLogEntryStatus.setStatus('current')
nlmStatsGlobalNotificationsLogged = MibScalar((1, 3, 6, 1, 2, 1, 92, 1, 2, 1), Counter32()).setUnits('notifications').setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmStatsGlobalNotificationsLogged.setStatus('current')
nlmStatsGlobalNotificationsBumped = MibScalar((1, 3, 6, 1, 2, 1, 92, 1, 2, 2), Counter32()).setUnits('notifications').setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmStatsGlobalNotificationsBumped.setStatus('current')
nlmStatsLogTable = MibTable((1, 3, 6, 1, 2, 1, 92, 1, 2, 3), )
if mibBuilder.loadTexts: nlmStatsLogTable.setStatus('current')
nlmStatsLogEntry = MibTableRow((1, 3, 6, 1, 2, 1, 92, 1, 2, 3, 1), )
nlmConfigLogEntry.registerAugmentions(("NOTIFICATION-LOG-MIB", "nlmStatsLogEntry"))
nlmStatsLogEntry.setIndexNames(*nlmConfigLogEntry.getIndexNames())
if mibBuilder.loadTexts: nlmStatsLogEntry.setStatus('current')
nlmStatsLogNotificationsLogged = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 2, 3, 1, 1), Counter32()).setUnits('notifications').setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmStatsLogNotificationsLogged.setStatus('current')
nlmStatsLogNotificationsBumped = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 2, 3, 1, 2), Counter32()).setUnits('notifications').setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmStatsLogNotificationsBumped.setStatus('current')
nlmLogTable = MibTable((1, 3, 6, 1, 2, 1, 92, 1, 3, 1), )
if mibBuilder.loadTexts: nlmLogTable.setStatus('current')
nlmLogEntry = MibTableRow((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1), ).setIndexNames((0, "NOTIFICATION-LOG-MIB", "nlmLogName"), (0, "NOTIFICATION-LOG-MIB", "nlmLogIndex"))
if mibBuilder.loadTexts: nlmLogEntry.setStatus('current')
nlmLogIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: nlmLogIndex.setStatus('current')
nlmLogTime = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogTime.setStatus('current')
nlmLogDateAndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogDateAndTime.setStatus('current')
nlmLogEngineID = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 4), SnmpEngineID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogEngineID.setStatus('current')
nlmLogEngineTAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 5), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogEngineTAddress.setStatus('current')
nlmLogEngineTDomain = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 6), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogEngineTDomain.setStatus('current')
nlmLogContextEngineID = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 7), SnmpEngineID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogContextEngineID.setStatus('current')
nlmLogContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogContextName.setStatus('current')
nlmLogNotificationID = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 9), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogNotificationID.setStatus('current')
nlmLogVariableTable = MibTable((1, 3, 6, 1, 2, 1, 92, 1, 3, 2), )
if mibBuilder.loadTexts: nlmLogVariableTable.setStatus('current')
nlmLogVariableEntry = MibTableRow((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1), ).setIndexNames((0, "NOTIFICATION-LOG-MIB", "nlmLogName"), (0, "NOTIFICATION-LOG-MIB", "nlmLogIndex"), (0, "NOTIFICATION-LOG-MIB", "nlmLogVariableIndex"))
if mibBuilder.loadTexts: nlmLogVariableEntry.setStatus('current')
nlmLogVariableIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: nlmLogVariableIndex.setStatus('current')
nlmLogVariableID = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableID.setStatus('current')
nlmLogVariableValueType = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("counter32", 1), ("unsigned32", 2), ("timeTicks", 3), ("integer32", 4), ("ipAddress", 5), ("octetString", 6), ("objectId", 7), ("counter64", 8), ("opaque", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableValueType.setStatus('current')
nlmLogVariableCounter32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableCounter32Val.setStatus('current')
nlmLogVariableUnsigned32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableUnsigned32Val.setStatus('current')
nlmLogVariableTimeTicksVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableTimeTicksVal.setStatus('current')
nlmLogVariableInteger32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableInteger32Val.setStatus('current')
nlmLogVariableOctetStringVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableOctetStringVal.setStatus('current')
nlmLogVariableIpAddressVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableIpAddressVal.setStatus('current')
nlmLogVariableOidVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 10), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableOidVal.setStatus('current')
nlmLogVariableCounter64Val = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableCounter64Val.setStatus('current')
nlmLogVariableOpaqueVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 12), Opaque()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlmLogVariableOpaqueVal.setStatus('current')
notificationLogMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 3))
notificationLogMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 3, 1))
notificationLogMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 3, 2))
notificationLogMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 92, 3, 1, 1)).setObjects(("NOTIFICATION-LOG-MIB", "notificationLogConfigGroup"), ("NOTIFICATION-LOG-MIB", "notificationLogStatsGroup"), ("NOTIFICATION-LOG-MIB", "notificationLogLogGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationLogMIBCompliance = notificationLogMIBCompliance.setStatus('current')
notificationLogConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 92, 3, 2, 1)).setObjects(("NOTIFICATION-LOG-MIB", "nlmConfigGlobalEntryLimit"), ("NOTIFICATION-LOG-MIB", "nlmConfigGlobalAgeOut"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogFilterName"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogEntryLimit"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogAdminStatus"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogOperStatus"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogStorageType"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationLogConfigGroup = notificationLogConfigGroup.setStatus('current')
notificationLogStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 92, 3, 2, 2)).setObjects(("NOTIFICATION-LOG-MIB", "nlmStatsGlobalNotificationsLogged"), ("NOTIFICATION-LOG-MIB", "nlmStatsGlobalNotificationsBumped"), ("NOTIFICATION-LOG-MIB", "nlmStatsLogNotificationsLogged"), ("NOTIFICATION-LOG-MIB", "nlmStatsLogNotificationsBumped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationLogStatsGroup = notificationLogStatsGroup.setStatus('current')
notificationLogLogGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 92, 3, 2, 3)).setObjects(("NOTIFICATION-LOG-MIB", "nlmLogTime"), ("NOTIFICATION-LOG-MIB", "nlmLogEngineID"), ("NOTIFICATION-LOG-MIB", "nlmLogEngineTAddress"), ("NOTIFICATION-LOG-MIB", "nlmLogEngineTDomain"), ("NOTIFICATION-LOG-MIB", "nlmLogContextEngineID"), ("NOTIFICATION-LOG-MIB", "nlmLogContextName"), ("NOTIFICATION-LOG-MIB", "nlmLogNotificationID"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableID"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableValueType"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableCounter32Val"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableUnsigned32Val"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableTimeTicksVal"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableInteger32Val"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableOctetStringVal"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableIpAddressVal"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableOidVal"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableCounter64Val"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableOpaqueVal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationLogLogGroup = notificationLogLogGroup.setStatus('current')
notificationLogDateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 92, 3, 2, 4)).setObjects(("NOTIFICATION-LOG-MIB", "nlmLogDateAndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationLogDateGroup = notificationLogDateGroup.setStatus('current')
mibBuilder.exportSymbols("NOTIFICATION-LOG-MIB", nlmConfigLogAdminStatus=nlmConfigLogAdminStatus, nlmConfigLogEntryStatus=nlmConfigLogEntryStatus, nlmConfigGlobalEntryLimit=nlmConfigGlobalEntryLimit, nlmLogVariableOidVal=nlmLogVariableOidVal, nlmLogVariableInteger32Val=nlmLogVariableInteger32Val, nlmLogVariableCounter64Val=nlmLogVariableCounter64Val, nlmLogTime=nlmLogTime, notificationLogMIBGroups=notificationLogMIBGroups, notificationLogConfigGroup=notificationLogConfigGroup, nlmLogNotificationID=nlmLogNotificationID, notificationLogMIBObjects=notificationLogMIBObjects, nlmLogVariableIpAddressVal=nlmLogVariableIpAddressVal, nlmLogDateAndTime=nlmLogDateAndTime, nlmConfigGlobalAgeOut=nlmConfigGlobalAgeOut, nlmLogVariableValueType=nlmLogVariableValueType, nlmConfigLogFilterName=nlmConfigLogFilterName, nlmLogVariableOpaqueVal=nlmLogVariableOpaqueVal, nlmConfigLogTable=nlmConfigLogTable, nlmLogVariableOctetStringVal=nlmLogVariableOctetStringVal, nlmLogContextEngineID=nlmLogContextEngineID, nlmLogEngineTAddress=nlmLogEngineTAddress, nlmLogVariableCounter32Val=nlmLogVariableCounter32Val, notificationLogStatsGroup=notificationLogStatsGroup, nlmLogVariableUnsigned32Val=nlmLogVariableUnsigned32Val, nlmStats=nlmStats, nlmConfigLogEntry=nlmConfigLogEntry, nlmLog=nlmLog, nlmLogName=nlmLogName, nlmConfigLogOperStatus=nlmConfigLogOperStatus, nlmStatsLogNotificationsLogged=nlmStatsLogNotificationsLogged, nlmLogVariableID=nlmLogVariableID, nlmLogVariableTimeTicksVal=nlmLogVariableTimeTicksVal, notificationLogLogGroup=notificationLogLogGroup, nlmLogIndex=nlmLogIndex, notificationLogMIB=notificationLogMIB, notificationLogMIBCompliances=notificationLogMIBCompliances, nlmStatsLogTable=nlmStatsLogTable, nlmLogEntry=nlmLogEntry, nlmLogContextName=nlmLogContextName, nlmConfigLogStorageType=nlmConfigLogStorageType, notificationLogMIBCompliance=notificationLogMIBCompliance, nlmConfig=nlmConfig, nlmStatsGlobalNotificationsBumped=nlmStatsGlobalNotificationsBumped, nlmStatsLogEntry=nlmStatsLogEntry, nlmLogVariableEntry=nlmLogVariableEntry, notificationLogMIBConformance=notificationLogMIBConformance, notificationLogDateGroup=notificationLogDateGroup, nlmLogVariableTable=nlmLogVariableTable, nlmStatsLogNotificationsBumped=nlmStatsLogNotificationsBumped, nlmLogVariableIndex=nlmLogVariableIndex, nlmStatsGlobalNotificationsLogged=nlmStatsGlobalNotificationsLogged, nlmLogTable=nlmLogTable, nlmConfigLogEntryLimit=nlmConfigLogEntryLimit, PYSNMP_MODULE_ID=notificationLogMIB, nlmLogEngineID=nlmLogEngineID, nlmLogEngineTDomain=nlmLogEngineTDomain)
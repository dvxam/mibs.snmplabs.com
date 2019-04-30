#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-FSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-FSM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:59:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, CiscoNetworkAddress, CiscoInetAddressMask, Unsigned64, CiscoAlarmSeverity = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec", "CiscoNetworkAddress", "CiscoInetAddressMask", "Unsigned64", "CiscoAlarmSeverity")
CucsManagedObjectDn, ciscoUnifiedComputingMIBObjects, CucsManagedObjectId = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectDn", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectId")
CucsFsmFsmStageStatus, = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsFsmFsmStageStatus")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Bits, Counter64, Unsigned32, Gauge32, iso, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Bits", "Counter64", "Unsigned32", "Gauge32", "iso", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "ObjectIdentity", "TimeTicks")
MacAddress, RowPointer, TruthValue, TimeInterval, DisplayString, TimeStamp, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowPointer", "TruthValue", "TimeInterval", "DisplayString", "TimeStamp", "TextualConvention", "DateAndTime")
cucsFsmObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63))
if mibBuilder.loadTexts: cucsFsmObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsFsmObjects.setOrganization('Cisco Systems Inc.')
cucsFsmStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1), )
if mibBuilder.loadTexts: cucsFsmStatusTable.setStatus('current')
cucsFsmStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FSM-MIB", "cucsFsmStatusInstanceId"))
if mibBuilder.loadTexts: cucsFsmStatusEntry.setStatus('current')
cucsFsmStatusInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFsmStatusInstanceId.setStatus('current')
cucsFsmStatusDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusDn.setStatus('current')
cucsFsmStatusRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusRn.setStatus('current')
cucsFsmStatusConvertedEpRef = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusConvertedEpRef.setStatus('current')
cucsFsmStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusDescr.setStatus('current')
cucsFsmStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusName.setStatus('current')
cucsFsmStatusObjectClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusObjectClassName.setStatus('current')
cucsFsmStatusRemoteEpRef = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusRemoteEpRef.setStatus('current')
cucsFsmStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 9), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusState.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-FSM-MIB", cucsFsmStatusState=cucsFsmStatusState, cucsFsmStatusObjectClassName=cucsFsmStatusObjectClassName, cucsFsmObjects=cucsFsmObjects, cucsFsmStatusInstanceId=cucsFsmStatusInstanceId, cucsFsmStatusName=cucsFsmStatusName, cucsFsmStatusRn=cucsFsmStatusRn, cucsFsmStatusTable=cucsFsmStatusTable, cucsFsmStatusRemoteEpRef=cucsFsmStatusRemoteEpRef, cucsFsmStatusDn=cucsFsmStatusDn, cucsFsmStatusConvertedEpRef=cucsFsmStatusConvertedEpRef, cucsFsmStatusDescr=cucsFsmStatusDescr, PYSNMP_MODULE_ID=cucsFsmObjects, cucsFsmStatusEntry=cucsFsmStatusEntry)

#
# PySNMP MIB module CISCO-LWAPP-MESH-BATTERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-MESH-BATTERY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:48:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
cLApName, cLApSysMacAddress = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApName", "cLApSysMacAddress")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, NotificationType, Counter64, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, TimeTicks, IpAddress, Unsigned32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "NotificationType", "Counter64", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "TimeTicks", "IpAddress", "Unsigned32", "Gauge32", "iso")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoLwappMeshBatteryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 620))
ciscoLwappMeshBatteryMIB.setRevisions(('2010-09-08 00:00', '2007-02-27 00:00',))
if mibBuilder.loadTexts: ciscoLwappMeshBatteryMIB.setLastUpdated('201009080000Z')
if mibBuilder.loadTexts: ciscoLwappMeshBatteryMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappMeshBatteryMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 0))
ciscoLwappMeshBatteryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 1))
ciscoLwappMeshBatteryMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 2))
ciscoLwappMeshBatteryInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1))
ciscoLwappMeshBatteryNotifControlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 2))
clMeshNodeBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1), )
if mibBuilder.loadTexts: clMeshNodeBatteryTable.setStatus('current')
clMeshNodeBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"))
if mibBuilder.loadTexts: clMeshNodeBatteryEntry.setStatus('current')
clMeshNodeBatteryModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryModelName.setStatus('current')
clMeshNodeBatteryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("normal", 2), ("overloaded", 3), ("low", 4), ("acfail", 5), ("replace", 6), ("missing", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryStatus.setStatus('current')
clMeshNodeBatteryChargingState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("charging", 3), ("discharging", 4), ("charged", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryChargingState.setStatus('deprecated')
clMeshNodeBatteryChargingLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 4), Integer32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryChargingLevel.setStatus('current')
clMeshNodeBatteryRemainingCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 5), Unsigned32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryRemainingCapacity.setStatus('deprecated')
clMeshNodeBatterySwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatterySwVersion.setStatus('current')
clMeshNodeBatterySerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatterySerialNumber.setStatus('current')
clMeshNodeBatteryInputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 8), Unsigned32()).setUnits('milliVolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryInputVoltage.setStatus('current')
clMeshNodeBatteryOutputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 9), Unsigned32()).setUnits('milliVolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryOutputVoltage.setStatus('current')
clMeshNodeBatteryOutputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 10), Unsigned32()).setUnits('milliWatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryOutputPower.setStatus('current')
clMeshNodeBatteryInternalVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 11), Unsigned32()).setUnits('milliVolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryInternalVoltage.setStatus('current')
clMeshNodeBatteryTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 12), Integer32()).setUnits('degree Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryTemperature.setStatus('current')
clMeshNodeBatteryCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 13), Unsigned32()).setUnits('milliAmps').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryCurrent.setStatus('deprecated')
clMeshNodeBatteryCurrentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 14), Integer32()).setUnits('milliAmps').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryCurrentValue.setStatus('current')
clMeshBatteryAlarmEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshBatteryAlarmEnabled.setStatus('current')
ciscoLwappMeshBatteryAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 620, 0, 1)).setObjects(("CISCO-LWAPP-AP-MIB", "cLApName"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"))
if mibBuilder.loadTexts: ciscoLwappMeshBatteryAlarm.setStatus('current')
ciscoLwappMeshBatteryMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1))
ciscoLwappMeshBatteryMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2))
ciscoLwappMeshBatteryMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1, 1)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryInfoGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsConfigGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryMIBCompliance = ciscoLwappMeshBatteryMIBCompliance.setStatus('deprecated')
ciscoLwappMeshBatteryMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1, 2)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsConfigGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryInfoGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryMIBComplianceRev1 = ciscoLwappMeshBatteryMIBComplianceRev1.setStatus('deprecated')
ciscoLwappMeshBatteryMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1, 3)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsConfigGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryInfoGroupRev2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryMIBComplianceRev2 = ciscoLwappMeshBatteryMIBComplianceRev2.setStatus('current')
ciscoLwappMeshBatteryInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 1)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryModelName"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingState"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingLevel"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryRemainingCapacity"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySwVersion"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySerialNumber"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputPower"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInternalVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryTemperature"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryInfoGroup = ciscoLwappMeshBatteryInfoGroup.setStatus('deprecated')
ciscoLwappMeshBatteryNotifsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 2)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshBatteryAlarmEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryNotifsConfigGroup = ciscoLwappMeshBatteryNotifsConfigGroup.setStatus('current')
ciscoLwappMeshBatteryNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 3)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryNotifsGroup = ciscoLwappMeshBatteryNotifsGroup.setStatus('current')
ciscoLwappMeshBatteryInfoGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 4)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryModelName"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingState"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingLevel"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryRemainingCapacity"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySwVersion"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySerialNumber"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputPower"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInternalVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryTemperature"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryCurrentValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryInfoGroupRev1 = ciscoLwappMeshBatteryInfoGroupRev1.setStatus('deprecated')
ciscoLwappMeshBatteryInfoGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 5)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryModelName"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingLevel"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySwVersion"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySerialNumber"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputPower"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInternalVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryTemperature"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryCurrentValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryInfoGroupRev2 = ciscoLwappMeshBatteryInfoGroupRev2.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-MESH-BATTERY-MIB", clMeshNodeBatteryCurrent=clMeshNodeBatteryCurrent, ciscoLwappMeshBatteryInfoGroupRev2=ciscoLwappMeshBatteryInfoGroupRev2, ciscoLwappMeshBatteryMIBComplianceRev2=ciscoLwappMeshBatteryMIBComplianceRev2, clMeshNodeBatteryTable=clMeshNodeBatteryTable, clMeshNodeBatteryOutputVoltage=clMeshNodeBatteryOutputVoltage, ciscoLwappMeshBatteryNotifsConfigGroup=ciscoLwappMeshBatteryNotifsConfigGroup, ciscoLwappMeshBatteryMIBGroups=ciscoLwappMeshBatteryMIBGroups, clMeshNodeBatteryRemainingCapacity=clMeshNodeBatteryRemainingCapacity, clMeshNodeBatteryInternalVoltage=clMeshNodeBatteryInternalVoltage, clMeshNodeBatteryEntry=clMeshNodeBatteryEntry, clMeshBatteryAlarmEnabled=clMeshBatteryAlarmEnabled, PYSNMP_MODULE_ID=ciscoLwappMeshBatteryMIB, clMeshNodeBatteryInputVoltage=clMeshNodeBatteryInputVoltage, ciscoLwappMeshBatteryMIBConform=ciscoLwappMeshBatteryMIBConform, ciscoLwappMeshBatteryAlarm=ciscoLwappMeshBatteryAlarm, ciscoLwappMeshBatteryMIBCompliances=ciscoLwappMeshBatteryMIBCompliances, ciscoLwappMeshBatteryInfo=ciscoLwappMeshBatteryInfo, clMeshNodeBatteryStatus=clMeshNodeBatteryStatus, clMeshNodeBatteryModelName=clMeshNodeBatteryModelName, clMeshNodeBatteryChargingLevel=clMeshNodeBatteryChargingLevel, ciscoLwappMeshBatteryInfoGroup=ciscoLwappMeshBatteryInfoGroup, clMeshNodeBatterySerialNumber=clMeshNodeBatterySerialNumber, clMeshNodeBatteryOutputPower=clMeshNodeBatteryOutputPower, ciscoLwappMeshBatteryMIBObjects=ciscoLwappMeshBatteryMIBObjects, ciscoLwappMeshBatteryMIBNotifs=ciscoLwappMeshBatteryMIBNotifs, clMeshNodeBatteryCurrentValue=clMeshNodeBatteryCurrentValue, ciscoLwappMeshBatteryInfoGroupRev1=ciscoLwappMeshBatteryInfoGroupRev1, clMeshNodeBatteryChargingState=clMeshNodeBatteryChargingState, clMeshNodeBatteryTemperature=clMeshNodeBatteryTemperature, ciscoLwappMeshBatteryMIB=ciscoLwappMeshBatteryMIB, clMeshNodeBatterySwVersion=clMeshNodeBatterySwVersion, ciscoLwappMeshBatteryMIBCompliance=ciscoLwappMeshBatteryMIBCompliance, ciscoLwappMeshBatteryNotifControlConfig=ciscoLwappMeshBatteryNotifControlConfig, ciscoLwappMeshBatteryNotifsGroup=ciscoLwappMeshBatteryNotifsGroup, ciscoLwappMeshBatteryMIBComplianceRev1=ciscoLwappMeshBatteryMIBComplianceRev1)

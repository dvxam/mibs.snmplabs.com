#
# PySNMP MIB module LIEBERT-UPSTATION-G-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIEBERT-UPSTATION-G-UPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Integer32, IpAddress, Counter32, Counter64, Bits, NotificationType, ObjectIdentity, MibIdentifier, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, NotificationType, iso, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Counter32", "Counter64", "Bits", "NotificationType", "ObjectIdentity", "MibIdentifier", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "NotificationType", "iso", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
emerson = MibIdentifier((1, 3, 6, 1, 4, 1, 476))
liebertCorp = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1))
liebertUps = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1))
luExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1))
luExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 2))
luPrivate = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 3))
luCore = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1))
lcUpsIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1))
lcUpsIdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsIdentManufacturer.setStatus('optional')
lcUpsIdentModel = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsIdentModel.setStatus('optional')
lcUpsIdentSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsIdentSoftwareVersion.setStatus('optional')
lcUpsIdentSpecific = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsIdentSpecific.setStatus('optional')
lcUpsBattery = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2))
lcUpsBatTimeRemaining = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsBatTimeRemaining.setStatus('optional')
lcUpsBatTemperature = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsBatTemperature.setStatus('optional')
lcUpsBatVoltage = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsBatVoltage.setStatus('optional')
lcUpsBatCurrent = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsBatCurrent.setStatus('optional')
lcUpsBatCapacity = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsBatCapacity.setStatus('optional')
lcUpsInput = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3))
lcUpsInputFrequency = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsInputFrequency.setStatus('optional')
lcUpsInputNumLines = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsInputNumLines.setStatus('optional')
lcUpsInputTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6), )
if mibBuilder.loadTexts: lcUpsInputTable.setStatus('optional')
lcUpsInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1), ).setIndexNames((0, "LIEBERT-UPSTATION-G-UPS-MIB", "lcUpsInputLine"))
if mibBuilder.loadTexts: lcUpsInputEntry.setStatus('optional')
lcUpsInputLine = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsInputLine.setStatus('optional')
lcUpsInputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsInputVoltage.setStatus('optional')
lcUpsInputCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsInputCurrent.setStatus('optional')
lcUpsInputVA = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsInputVA.setStatus('optional')
lcUpsOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4))
lcUpsOutputFrequency = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsOutputFrequency.setStatus('optional')
lcUpsOutputNumLines = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsOutputNumLines.setStatus('optional')
lcUpsInverter = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5))
lcUpsInverterStatus = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("on", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsInverterStatus.setStatus('optional')
lcUpsInverterTemp = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsInverterTemp.setStatus('optional')
lcUpsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6))
lcUpsAlarms = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsAlarms.setStatus('optional')
lcUpsAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2), )
if mibBuilder.loadTexts: lcUpsAlarmTable.setStatus('optional')
lcUpsAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1), ).setIndexNames((0, "LIEBERT-UPSTATION-G-UPS-MIB", "lcUpsAlarmId"))
if mibBuilder.loadTexts: lcUpsAlarmEntry.setStatus('optional')
lcUpsAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsAlarmId.setStatus('optional')
lcUpsAlarmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsAlarmDescr.setStatus('optional')
lcUpsAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsAlarmTime.setStatus('optional')
lcUpsAlarmConditions = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3))
lcUpsAlarmLowBatteryWarning = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 1))
lcUpsAlarmLowBatteryShutdown = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 2))
lcUpsAlarmUtilFailed = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 3))
lcUpsAlarmOverTempWarning = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 4))
lcUpsAlarmOverTempShutdown = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 5))
lcUpsAlarmOutputOverloadShutdown = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 7))
lcUpsAlarmInputOverVoltage = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 8))
lcUpsAlarmBatteryBad = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 9))
lcUpsAlarmOnBattery = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 10))
lcUpsAlarmStopNoticeIssued = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 11))
lcUpsAlarmUpsOff = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 12))
lcUpsTest = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7))
lcUpsTestBattery = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("start", 2), ("abort", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsTestBattery.setStatus('optional')
lcUpsTestBatteryStatus = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("passed", 2), ("failed", 3), ("inProgress", 4), ("sysFailure", 5), ("notSupported", 6), ("inhibited", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsTestBatteryStatus.setStatus('optional')
lcUpsTestDiag = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("start", 2), ("abort", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsTestDiag.setStatus('optional')
lcUpsTestDiagStatus = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("passed", 2), ("failed", 3), ("inProgress", 4), ("sysFailure", 5), ("notSupported", 6), ("inhibited", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lcUpsTestDiagStatus.setStatus('optional')
lcUpsControl = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8))
lcUpsControlOutputOffDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlOutputOffDelay.setStatus('optional')
lcUpsControlOutputOnDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlOutputOnDelay.setStatus('optional')
lcUpsControlOutputOffTrapDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlOutputOffTrapDelay.setStatus('optional')
lcUpsControlOutputOnTrapDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlOutputOnTrapDelay.setStatus('optional')
lcUpsControlUnixShutdownDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlUnixShutdownDelay.setStatus('optional')
lcUpsControlUnixShutdownTrapDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlUnixShutdownTrapDelay.setStatus('optional')
lcUpsControlCancelCommands = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("cancel", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlCancelCommands.setStatus('optional')
lcUpsControlRebootAgentDelay = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsControlRebootAgentDelay.setStatus('optional')
lcUpsNominal = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9))
lcUpsNominalOutputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalOutputVoltage.setStatus('optional')
lcUpsNominalInputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalInputVoltage.setStatus('optional')
lcUpsNominalOutputVA = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalOutputVA.setStatus('optional')
lcUpsNominalOutputFreq = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalOutputFreq.setStatus('optional')
lcUpsNominalInputFreq = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lcUpsNominalInputFreq.setStatus('optional')
lcUpsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11))
lcUpsOverloadShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,2)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsOnBatteryTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,3)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsLowBatteryWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,4)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsLowBatteryShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,5)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsUtilPowerFailedTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,6)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsUtilPowerRestoredTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,7)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsInputOverVoltageTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,8)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsOverTempWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,9)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsOverTempShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,10)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,11)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsOutputOffTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,12)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsOutputOffWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,13)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsOutputOnTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,14)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsOutputOnWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,15)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsUnixShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,16)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lcUpsUnixShutdownWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11) + (0,17)).setObjects(("SNMPv2-MIB", "sysUpTime"))
luUPStationG = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4))
lgUpsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6))
lgUpsAlarmConditions = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1))
lgUpsAlarmDCOverVoltageShutdown = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 1))
lgUpsAlarmOutputShortShutdown = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 2))
lgUpsAlarmLNReversedShutdown = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 3))
lgUpsAlarmRemoteShutdown = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 4))
lgUpsAlarmInputUVOnStartup = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 5))
lgUpsAlarmPFCFailedOnStartup = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 6))
lgUpsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11))
lgUpsDCOverVoltageShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11) + (0,1)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lgUpsOutputShortShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11) + (0,2)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lgUpsLNReversedShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11) + (0,3)).setObjects(("SNMPv2-MIB", "sysUpTime"))
lgUpsInputUVOnStartupTrap = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11) + (0,4)).setObjects(("SNMPv2-MIB", "sysUpTime"))
mibBuilder.exportSymbols("LIEBERT-UPSTATION-G-UPS-MIB", lcUpsOutputNumLines=lcUpsOutputNumLines, lcUpsBattery=lcUpsBattery, lcUpsUnixShutdownTrap=lcUpsUnixShutdownTrap, lcUpsControl=lcUpsControl, lcUpsAlarmLowBatteryShutdown=lcUpsAlarmLowBatteryShutdown, lcUpsLowBatteryShutdownTrap=lcUpsLowBatteryShutdownTrap, lcUpsControlUnixShutdownDelay=lcUpsControlUnixShutdownDelay, lcUpsInputNumLines=lcUpsInputNumLines, lcUpsControlOutputOffTrapDelay=lcUpsControlOutputOffTrapDelay, lcUpsIdentSoftwareVersion=lcUpsIdentSoftwareVersion, lcUpsBatCurrent=lcUpsBatCurrent, lcUpsInputTable=lcUpsInputTable, luUPStationG=luUPStationG, lcUpsOverTempShutdownTrap=lcUpsOverTempShutdownTrap, lcUpsAlarms=lcUpsAlarms, lcUpsAlarmConditions=lcUpsAlarmConditions, lcUpsTestDiagStatus=lcUpsTestDiagStatus, lcUpsControlUnixShutdownTrapDelay=lcUpsControlUnixShutdownTrapDelay, lcUpsUnixShutdownWarningTrap=lcUpsUnixShutdownWarningTrap, lgUpsOutputShortShutdownTrap=lgUpsOutputShortShutdownTrap, lcUpsOutputOnTrap=lcUpsOutputOnTrap, lcUpsAlarm=lcUpsAlarm, lgUpsAlarmConditions=lgUpsAlarmConditions, lcUpsControlCancelCommands=lcUpsControlCancelCommands, lcUpsOutput=lcUpsOutput, lcUpsAlarmStopNoticeIssued=lcUpsAlarmStopNoticeIssued, lcUpsNominal=lcUpsNominal, lcUpsOutputOffWarningTrap=lcUpsOutputOffWarningTrap, lgUpsAlarmOutputShortShutdown=lgUpsAlarmOutputShortShutdown, lcUpsOverloadShutdownTrap=lcUpsOverloadShutdownTrap, lgUpsAlarm=lgUpsAlarm, lcUpsAlarmTable=lcUpsAlarmTable, lcUpsIdent=lcUpsIdent, lcUpsBatVoltage=lcUpsBatVoltage, lcUpsBatCapacity=lcUpsBatCapacity, lcUpsUtilPowerFailedTrap=lcUpsUtilPowerFailedTrap, lgUpsDCOverVoltageShutdownTrap=lgUpsDCOverVoltageShutdownTrap, lcUpsControlOutputOffDelay=lcUpsControlOutputOffDelay, lcUpsNominalOutputVA=lcUpsNominalOutputVA, lcUpsInputOverVoltageTrap=lcUpsInputOverVoltageTrap, lgUpsAlarmLNReversedShutdown=lgUpsAlarmLNReversedShutdown, lcUpsIdentManufacturer=lcUpsIdentManufacturer, lcUpsAlarmLowBatteryWarning=lcUpsAlarmLowBatteryWarning, lcUpsNominalOutputFreq=lcUpsNominalOutputFreq, lcUpsNominalInputVoltage=lcUpsNominalInputVoltage, lcUpsOnBatteryTrap=lcUpsOnBatteryTrap, lcUpsOverTempWarningTrap=lcUpsOverTempWarningTrap, lgUpsAlarmDCOverVoltageShutdown=lgUpsAlarmDCOverVoltageShutdown, lcUpsControlRebootAgentDelay=lcUpsControlRebootAgentDelay, lcUpsInputCurrent=lcUpsInputCurrent, lcUpsOutputOnWarningTrap=lcUpsOutputOnWarningTrap, lcUpsNominalInputFreq=lcUpsNominalInputFreq, lcUpsTestBatteryStatus=lcUpsTestBatteryStatus, lcUpsIdentSpecific=lcUpsIdentSpecific, lcUpsAlarmOverTempWarning=lcUpsAlarmOverTempWarning, lcUpsInputEntry=lcUpsInputEntry, luCore=luCore, luExperimental=luExperimental, lcUpsTestBattery=lcUpsTestBattery, liebertUps=liebertUps, lcUpsAlarmEntry=lcUpsAlarmEntry, lcUpsControlOutputOnTrapDelay=lcUpsControlOutputOnTrapDelay, lcUpsInverterTemp=lcUpsInverterTemp, lcUpsAlarmId=lcUpsAlarmId, lcUpsUtilPowerRestoredTrap=lcUpsUtilPowerRestoredTrap, lcUpsAlarmDescr=lcUpsAlarmDescr, lcUpsAlarmInputOverVoltage=lcUpsAlarmInputOverVoltage, lcUpsInputVA=lcUpsInputVA, lcUpsOutputOffTrap=lcUpsOutputOffTrap, luPrivate=luPrivate, emerson=emerson, lcUpsBatTemperature=lcUpsBatTemperature, lgUpsAlarmRemoteShutdown=lgUpsAlarmRemoteShutdown, lcUpsTest=lcUpsTest, lcUpsInverterStatus=lcUpsInverterStatus, lcUpsInput=lcUpsInput, lgUpsLNReversedShutdownTrap=lgUpsLNReversedShutdownTrap, lcUpsBatTimeRemaining=lcUpsBatTimeRemaining, lcUpsInputFrequency=lcUpsInputFrequency, lcUpsAlarmTime=lcUpsAlarmTime, lcUpsOutputFrequency=lcUpsOutputFrequency, lcUpsAlarmUpsOff=lcUpsAlarmUpsOff, liebertCorp=liebertCorp, lcUpsAlarmUtilFailed=lcUpsAlarmUtilFailed, lgUpsTraps=lgUpsTraps, lcUpsInverter=lcUpsInverter, lcUpsNominalOutputVoltage=lcUpsNominalOutputVoltage, lcUpsAlarmOutputOverloadShutdown=lcUpsAlarmOutputOverloadShutdown, lcUpsLowBatteryWarningTrap=lcUpsLowBatteryWarningTrap, lcUpsTraps=lcUpsTraps, luExtensions=luExtensions, lcUpsControlOutputOnDelay=lcUpsControlOutputOnDelay, lcUpsAlarmOverTempShutdown=lcUpsAlarmOverTempShutdown, lcUpsIdentModel=lcUpsIdentModel, lcUpsInputVoltage=lcUpsInputVoltage, lcUpsAlarmBatteryBad=lcUpsAlarmBatteryBad, lgUpsAlarmInputUVOnStartup=lgUpsAlarmInputUVOnStartup, lgUpsInputUVOnStartupTrap=lgUpsInputUVOnStartupTrap, lcUpsAlarmOnBattery=lcUpsAlarmOnBattery, lcUpsInputLine=lcUpsInputLine, lcUpsAlarmTrap=lcUpsAlarmTrap, lcUpsTestDiag=lcUpsTestDiag, lgUpsAlarmPFCFailedOnStartup=lgUpsAlarmPFCFailedOnStartup)

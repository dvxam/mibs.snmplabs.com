#
# PySNMP MIB module AC-ANALOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AC-ANALOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
audioCodes, acProducts, acBoardMibs, acGeneric, acRegistrations = mibBuilder.importSymbols("AUDIOCODES-TYPES-MIB", "audioCodes", "acProducts", "acBoardMibs", "acGeneric", "acRegistrations")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, TimeTicks, NotificationType, ObjectIdentity, Bits, Counter32, iso, ModuleIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "TimeTicks", "NotificationType", "ObjectIdentity", "Bits", "Counter32", "iso", "ModuleIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "enterprises")
DateAndTime, TextualConvention, TAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "TAddress", "DisplayString")
acAnalog = ModuleIdentity((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8))
if mibBuilder.loadTexts: acAnalog.setLastUpdated('200911181414Z')
if mibBuilder.loadTexts: acAnalog.setOrganization('AudioCodes Ltd')
acAnalogConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1))
acAnalogConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1))
acAnalogMisc = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 1))
acAnalogMiscCurrentDisconnectDuration = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(200, 1500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogMiscCurrentDisconnectDuration.setStatus('current')
acAnalogMiscFlashHookPeriod = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(25, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogMiscFlashHookPeriod.setStatus('current')
acAnalogMiscGroundKeyDetection = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogMiscGroundKeyDetection.setStatus('current')
acAuxiliaryFiles = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 2))
acAuxiliaryFilesFxsCoefficients = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 2, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAuxiliaryFilesFxsCoefficients.setStatus('current')
acAuxiliaryFilesFxoCoefficients = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 2, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAuxiliaryFilesFxoCoefficients.setStatus('current')
acAnalogFxoConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2))
acAnalogFxo = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1))
acAnalogFxoFarEndDisconnectType = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxoFarEndDisconnectType.setStatus('current')
acAnalogFxoCountryCoefficients = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(66, 70))).clone(namedValues=NamedValues(("europe", 66), ("unitedStates", 70)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxoCountryCoefficients.setStatus('current')
acAnalogFxoDCRemover = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxoDCRemover.setStatus('current')
acAnalogFxoFarEndDisconnectToneTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21), )
if mibBuilder.loadTexts: acAnalogFxoFarEndDisconnectToneTable.setStatus('current')
acAnalogFxoFarEndDisconnectToneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1), ).setIndexNames((0, "AC-ANALOG-MIB", "acAnalogFxoFarEndDisconnectToneIndex"))
if mibBuilder.loadTexts: acAnalogFxoFarEndDisconnectToneEntry.setStatus('current')
acAnalogFxoFarEndDisconnectToneRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxoFarEndDisconnectToneRowStatus.setStatus('current')
acAnalogFxoFarEndDisconnectToneAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxoFarEndDisconnectToneAction.setStatus('current')
acAnalogFxoFarEndDisconnectToneActionResult = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoFarEndDisconnectToneActionResult.setStatus('current')
acAnalogFxoFarEndDisconnectToneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoFarEndDisconnectToneIndex.setStatus('current')
acAnalogFxoFarEndDisconnectToneType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 298, 299))).clone(namedValues=NamedValues(("acNullTone", 0), ("acDialTone", 1), ("acRingingTone", 2), ("acBusyTone", 3), ("acCongestionTone", 4), ("acSpecialInfoTone", 5), ("acWarningTone", 6), ("acReorderTone", 7), ("acConfirmationTone", 8), ("acWaitingTone", 9), ("acCallProgressCo1Tone", 10), ("acCallProgressCo2Tone", 11), ("acOldMilliwattTone", 12), ("acNewMilliwattTone", 13), ("acMessageWaitingIndicator", 14), ("acStutterDialTone", 15), ("acStutterOffHookWarningTone", 16), ("acWaitingTone1", 17), ("acComfortTone", 18), ("acNAKTone", 19), ("acVacantNumberTone", 20), ("acSpecialConditionTone", 21), ("acDialTone2", 22), ("acOnHoldTone", 23), ("acCallTransferDialTone", 24), ("acCallForwardTone", 25), ("acCreditCardServiceTone", 26), ("acSpecialRecallDialTone", 27), ("acAlertingTone", 28), ("acNetworkCongestionTone", 29), ("acWaitingTone2", 30), ("acWaitingTone3", 31), ("acWaitingTone4", 32), ("acConfEnterTone", 33), ("acConfExitTone", 34), ("acConfLockTone", 35), ("acConfUnlockTone", 36), ("acConfTimeLimitTone", 37), ("acPayphoneRecognitionTone", 38), ("acCallerWaitingTone", 39), ("acCNGFaxTone", 40), ("acPrecConfNotifyType", 41), ("acPresConfNotifyType", 42), ("acPrecPreemptType", 43), ("acPrecRTType", 44), ("acR15reqOfANItone", 45), ("acCo1Tone", 200), ("acCo2Tone", 201), ("acPlayRecordBeepTone", 202), ("acTrunkTestingTestProgressTone", 203), ("acTrunkTestingTestTone", 204), ("acTrunkTestingGuardTone", 205), ("acFSKTrunkTestingTone", 206), ("acGeneralTrunkTestingTone1", 207), ("acGeneralTrunkTestingTone2", 208), ("acGeneralTrunkTestingTone3", 209), ("acSpecialInfoToneFirst", 210), ("acSpecialInfoToneSecond", 211), ("acSpecialInfoToneThird", 212), ("acTTYTone", 213), ("acTT904ContinuityTone", 214), ("acTTMilliwattLossMeasureTone", 215), ("acCarrierDialTone", 216), ("acCarrierAnswerTone", 217), ("acCarrierChargingTone", 218), ("acLongDistanceIndicatorTone", 219), ("acSTUModemFirstTone", 298), ("acSTUModemSecondTone", 299)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxoFarEndDisconnectToneType.setStatus('current')
acAnalogFxsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3))
acAnalogFxs = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1))
acAnalogFxsPolarityReversalType = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("soft", 0), ("hard", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsPolarityReversalType.setStatus('current')
acAnalogFxsMeteringType = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mt12kHz", 0), ("mt16kHz", 1), ("mtPolarityReversal", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsMeteringType.setStatus('current')
acAnalogFxsLifeLineType = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("acLifeLineType-Hardware-Only", 0), ("acLifeLineTypeHardware-And-Link-Detection", 1), ("acLifeLineType-Hardware-And-Link-And-Network-Detection", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsLifeLineType.setStatus('current')
acAnalogFxsMinFlashHookTime = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(25, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsMinFlashHookTime.setStatus('current')
acAnalogFxsCallerIDTimingMode = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsCallerIDTimingMode.setStatus('current')
acAnalogFxsBellcoreCallerIDTypeOneSubStandard = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("bellcore-Between-Rings", 0), ("bellcore-Not-Ring-Related", 1), ("bellcore-Before-Ring-RP-AS", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsBellcoreCallerIDTypeOneSubStandard.setStatus('current')
acAnalogFxsETSICallerIDTypeOneSubStandard = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("eTSI-Between-Rings", 0), ("eTSI-Before-Ring-DT-AS", 1), ("eTSI-Before-Ring-RP-AS", 2), ("eTSI-Before-Ring-LR-DT-AS", 3), ("eTSI-Not-Ring-Related-DT-AS", 4), ("eTSI-Not-Ring-Related-RP-AS", 5), ("eTSI-Not-Ring-Related-LR-DT-AS", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsETSICallerIDTypeOneSubStandard.setStatus('current')
acAnalogFxsETSIVMWITypeOneStandard = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("eTSI-VMWI-Between-Rings", 0), ("eTSI-VMWI-Before-Ring-DT-AS", 1), ("eTSI-VMWI-Before-Ring-RP-AS", 2), ("eTSI-VMWI-Before-Ring-LR-DT-AS", 3), ("eTSI-VMWI-Not-Ring-Related-DT-AS", 4), ("eTSI-VMWI-Not-Ring-Related-RP-AS", 5), ("eTSI-VMWI-Not-Ring-Related-LR-DT-AS", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsETSIVMWITypeOneStandard.setStatus('current')
acAnalogFxsBellcoreVMWITypeOneStandard = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("bellcore-VMWI-Between-Rings", 0), ("bellcore-VMWI-Not-Ring-Related", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsBellcoreVMWITypeOneStandard.setStatus('current')
acAnalogFxsDisableAutoCalibration = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsDisableAutoCalibration.setStatus('current')
acAnalogFxsExternalLifeLinePorts = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsExternalLifeLinePorts.setStatus('current')
acAnalogFxsCountryCoefficients = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(66, 70))).clone(namedValues=NamedValues(("europe", 66), ("unitedStates", 70)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsCountryCoefficients.setStatus('current')
acAnalogFxsTTXVoltageLevel = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2))).clone(namedValues=NamedValues(("notAvailable", -1), ("ttxVoltageLevel0V", 0), ("ttxVoltageLevel05", 1), ("ttxVoltageLevel1V", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsTTXVoltageLevel.setStatus('current')
acAnalogStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2))
acAnalogStatusMisc = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 1))
acAnalogStatusMiscFxsOrFxo = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("fXO", 0), ("fXS", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogStatusMiscFxsOrFxo.setStatus('current')
acAnalogStatusMiscBoardTemperature = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogStatusMiscBoardTemperature.setStatus('current')
acAnalogStatusMiscAnalogChannelsCount = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogStatusMiscAnalogChannelsCount.setStatus('current')
acAnalogFxsFxo = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20))
acAnalogFxsFxoTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1), )
if mibBuilder.loadTexts: acAnalogFxsFxoTable.setStatus('current')
acAnalogFxsFxoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1), ).setIndexNames((0, "AC-ANALOG-MIB", "acAnalogFxsFxoIndex"))
if mibBuilder.loadTexts: acAnalogFxsFxoEntry.setStatus('current')
acAnalogFxsFxoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 24)))
if mibBuilder.loadTexts: acAnalogFxsFxoIndex.setStatus('current')
acAnalogFxsFxoType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("fXO", 0), ("fXS", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsFxoType.setStatus('current')
acAnalogFxsFxoChipRevNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsFxoChipRevNum.setStatus('current')
acAnalogFxsFxoHookState = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("onHookState", 1), ("offHookState", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsFxoHookState.setStatus('current')
acAnalogAction = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3))
acAnalogFxoAction = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1))
acAnalogFxoLineTestTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1), )
if mibBuilder.loadTexts: acAnalogFxoLineTestTable.setStatus('current')
acAnalogFxoLineTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1), ).setIndexNames((0, "AC-ANALOG-MIB", "acAnalogFxoLineTestIndex"))
if mibBuilder.loadTexts: acAnalogFxoLineTestEntry.setStatus('current')
acAnalogFxoLineTestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 24)))
if mibBuilder.loadTexts: acAnalogFxoLineTestIndex.setStatus('current')
acAnalogFxoLineTestActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noTestActivated", 0), ("runLineTest", 1), ("lineTestDone", 2), ("testFailed", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxoLineTestActivate.setStatus('current')
acAnalogFxoLineTestHookState = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("onHookState", 1), ("offHookState", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoLineTestHookState.setStatus('current')
acAnalogFxoLineTestPolarityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normalPolarity", 1), ("reversePolarity", 2), ("notAvailable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoLineTestPolarityStatus.setStatus('current')
acAnalogFxoLineTestLineConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lineDisconnected", 1), ("lineConnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoLineTestLineConnectionStatus.setStatus('current')
acAnalogFxoLineTestLineCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoLineTestLineCurrent.setStatus('current')
acAnalogFxoLineTestLineVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoLineTestLineVoltage.setStatus('current')
acAnalogFxoLineTestRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoLineTestRingState.setStatus('current')
acAnalogFxoLineTestLinePolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("positive", 1), ("negative", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoLineTestLinePolarity.setStatus('current')
acAnalogFxoLineTestMwiState = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoLineTestMwiState.setStatus('current')
acAnalogFxoLineTestLastCurrentDisconnectDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxoLineTestLastCurrentDisconnectDuration.setStatus('current')
acAnalogFxsAction = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2))
acAnalogFxsLineTestTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1), )
if mibBuilder.loadTexts: acAnalogFxsLineTestTable.setStatus('current')
acAnalogFxsLineTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1), ).setIndexNames((0, "AC-ANALOG-MIB", "acAnalogFxsLineTestIndex"))
if mibBuilder.loadTexts: acAnalogFxsLineTestEntry.setStatus('current')
acAnalogFxsLineTestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 24)))
if mibBuilder.loadTexts: acAnalogFxsLineTestIndex.setStatus('current')
acAnalogFxsLineTestActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noTestActivated", 0), ("runLineTest", 1), ("lineTestDone", 2), ("testFailed", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogFxsLineTestActivate.setStatus('current')
acAnalogFxsLineTestHookState = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("onHookState", 1), ("offHookState", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsLineTestHookState.setStatus('current')
acAnalogFxsLineTestRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("offRingState", 1), ("onRingState", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsLineTestRingState.setStatus('current')
acAnalogFxsLineTestPolarityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normalPolarity", 1), ("reversePolarity", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsLineTestPolarityStatus.setStatus('current')
acAnalogFxsLineTestMessageWaitingIndication = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noWaitingMessage", 1), ("waitingMessage", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsLineTestMessageWaitingIndication.setStatus('current')
acAnalogFxsLineTestLineCurrentReading = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsLineTestLineCurrentReading.setStatus('current')
acAnalogFxsLineTestLineVoltageReading = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-6000, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsLineTestLineVoltageReading.setStatus('current')
acAnalogFxsLineTestAnalogVoltageReading = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(300, 340))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsLineTestAnalogVoltageReading.setStatus('current')
acAnalogFxsLineTestRingVoltageReading = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-13000, 13000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsLineTestRingVoltageReading.setStatus('current')
acAnalogFxsLineTestLongLineCurrentReading = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogFxsLineTestLongLineCurrentReading.setStatus('current')
acAnalogCommonAction = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3))
acAnalogCommonChannelTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3, 1), )
if mibBuilder.loadTexts: acAnalogCommonChannelTable.setStatus('current')
acAnalogCommonChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3, 1, 1), ).setIndexNames((0, "AC-ANALOG-MIB", "acAnalogCommonChannelIndex"))
if mibBuilder.loadTexts: acAnalogCommonChannelEntry.setStatus('current')
acAnalogCommonChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5000)))
if mibBuilder.loadTexts: acAnalogCommonChannelIndex.setStatus('current')
acAnalogCommonChannelAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noAction", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acAnalogCommonChannelAction.setStatus('current')
acAnalogLegs = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21))
acAnalogLegsTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1), )
if mibBuilder.loadTexts: acAnalogLegsTable.setStatus('current')
acAnalogLegsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1), ).setIndexNames((0, "AC-ANALOG-MIB", "acAnalogLegsLegIndex"))
if mibBuilder.loadTexts: acAnalogLegsEntry.setStatus('current')
acAnalogLegsLegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5000)))
if mibBuilder.loadTexts: acAnalogLegsLegIndex.setStatus('current')
acAnalogLegsCallIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogLegsCallIndex.setStatus('current')
acAnalogLegsAnalogType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fxs", 1), ("fxo", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogLegsAnalogType.setStatus('current')
acAnalogLegsEchoCanceller = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogLegsEchoCanceller.setStatus('current')
acAnalogLegsHighPassFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogLegsHighPassFilter.setStatus('current')
acAnalogLegsDTMFDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogLegsDTMFDetection.setStatus('current')
acAnalogLegsVoiceVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogLegsVoiceVolume.setStatus('current')
acAnalogLegsInputGain = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogLegsInputGain.setStatus('current')
acAnalogLegsLegName = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acAnalogLegsLegName.setStatus('current')
mibBuilder.exportSymbols("AC-ANALOG-MIB", acAnalogFxoFarEndDisconnectToneEntry=acAnalogFxoFarEndDisconnectToneEntry, acAnalogLegsLegIndex=acAnalogLegsLegIndex, acAnalogFxsFxoType=acAnalogFxsFxoType, acAnalogConfig=acAnalogConfig, acAnalogLegsCallIndex=acAnalogLegsCallIndex, acAnalogFxoFarEndDisconnectToneTable=acAnalogFxoFarEndDisconnectToneTable, acAnalogStatusMiscAnalogChannelsCount=acAnalogStatusMiscAnalogChannelsCount, acAnalogFxsCountryCoefficients=acAnalogFxsCountryCoefficients, acAnalogLegs=acAnalogLegs, acAnalogFxsConfig=acAnalogFxsConfig, acAnalogFxsLineTestActivate=acAnalogFxsLineTestActivate, acAnalogFxsETSIVMWITypeOneStandard=acAnalogFxsETSIVMWITypeOneStandard, acAnalogMiscCurrentDisconnectDuration=acAnalogMiscCurrentDisconnectDuration, acAnalogFxsFxoEntry=acAnalogFxsFxoEntry, acAuxiliaryFilesFxsCoefficients=acAuxiliaryFilesFxsCoefficients, acAnalogFxsLineTestEntry=acAnalogFxsLineTestEntry, acAnalogFxsLineTestLineCurrentReading=acAnalogFxsLineTestLineCurrentReading, acAnalogFxoConfig=acAnalogFxoConfig, acAnalog=acAnalog, acAnalogFxsTTXVoltageLevel=acAnalogFxsTTXVoltageLevel, acAnalogMisc=acAnalogMisc, acAnalogFxsFxoTable=acAnalogFxsFxoTable, acAnalogFxsMinFlashHookTime=acAnalogFxsMinFlashHookTime, acAnalogLegsAnalogType=acAnalogLegsAnalogType, acAnalogFxoLineTestLinePolarity=acAnalogFxoLineTestLinePolarity, acAnalogFxoLineTestEntry=acAnalogFxoLineTestEntry, acAnalogLegsTable=acAnalogLegsTable, acAnalogLegsEchoCanceller=acAnalogLegsEchoCanceller, acAnalogFxsLineTestLongLineCurrentReading=acAnalogFxsLineTestLongLineCurrentReading, acAuxiliaryFiles=acAuxiliaryFiles, acAnalogFxsFxoChipRevNum=acAnalogFxsFxoChipRevNum, acAnalogFxoFarEndDisconnectToneActionResult=acAnalogFxoFarEndDisconnectToneActionResult, acAnalogFxoLineTestIndex=acAnalogFxoLineTestIndex, acAnalogFxsExternalLifeLinePorts=acAnalogFxsExternalLifeLinePorts, acAnalogFxsLineTestPolarityStatus=acAnalogFxsLineTestPolarityStatus, acAnalogFxsLineTestLineVoltageReading=acAnalogFxsLineTestLineVoltageReading, acAnalogConfiguration=acAnalogConfiguration, acAnalogAction=acAnalogAction, acAnalogFxs=acAnalogFxs, acAnalogCommonChannelTable=acAnalogCommonChannelTable, acAnalogFxsLifeLineType=acAnalogFxsLifeLineType, acAnalogStatusMiscBoardTemperature=acAnalogStatusMiscBoardTemperature, acAnalogMiscGroundKeyDetection=acAnalogMiscGroundKeyDetection, acAnalogFxoLineTestLineConnectionStatus=acAnalogFxoLineTestLineConnectionStatus, acAnalogLegsVoiceVolume=acAnalogLegsVoiceVolume, acAnalogFxsLineTestRingState=acAnalogFxsLineTestRingState, acAnalogFxsLineTestIndex=acAnalogFxsLineTestIndex, acAnalogFxsFxo=acAnalogFxsFxo, acAnalogCommonChannelAction=acAnalogCommonChannelAction, acAnalogFxoLineTestMwiState=acAnalogFxoLineTestMwiState, acAnalogFxsLineTestMessageWaitingIndication=acAnalogFxsLineTestMessageWaitingIndication, acAnalogFxsPolarityReversalType=acAnalogFxsPolarityReversalType, acAnalogLegsEntry=acAnalogLegsEntry, acAuxiliaryFilesFxoCoefficients=acAuxiliaryFilesFxoCoefficients, acAnalogFxoLineTestActivate=acAnalogFxoLineTestActivate, acAnalogFxoCountryCoefficients=acAnalogFxoCountryCoefficients, acAnalogStatus=acAnalogStatus, acAnalogFxsETSICallerIDTypeOneSubStandard=acAnalogFxsETSICallerIDTypeOneSubStandard, acAnalogFxoFarEndDisconnectToneAction=acAnalogFxoFarEndDisconnectToneAction, acAnalogFxsLineTestRingVoltageReading=acAnalogFxsLineTestRingVoltageReading, acAnalogFxsLineTestHookState=acAnalogFxsLineTestHookState, acAnalogFxsFxoHookState=acAnalogFxsFxoHookState, acAnalogFxsDisableAutoCalibration=acAnalogFxsDisableAutoCalibration, acAnalogFxsLineTestTable=acAnalogFxsLineTestTable, acAnalogFxoLineTestRingState=acAnalogFxoLineTestRingState, acAnalogFxoLineTestTable=acAnalogFxoLineTestTable, acAnalogLegsHighPassFilter=acAnalogLegsHighPassFilter, acAnalogFxsFxoIndex=acAnalogFxsFxoIndex, acAnalogFxo=acAnalogFxo, acAnalogFxsCallerIDTimingMode=acAnalogFxsCallerIDTimingMode, acAnalogStatusMisc=acAnalogStatusMisc, acAnalogLegsLegName=acAnalogLegsLegName, acAnalogFxoLineTestHookState=acAnalogFxoLineTestHookState, acAnalogFxoLineTestLineCurrent=acAnalogFxoLineTestLineCurrent, acAnalogFxoLineTestLastCurrentDisconnectDuration=acAnalogFxoLineTestLastCurrentDisconnectDuration, acAnalogFxsAction=acAnalogFxsAction, acAnalogFxsMeteringType=acAnalogFxsMeteringType, acAnalogFxsBellcoreVMWITypeOneStandard=acAnalogFxsBellcoreVMWITypeOneStandard, acAnalogLegsInputGain=acAnalogLegsInputGain, acAnalogCommonChannelIndex=acAnalogCommonChannelIndex, acAnalogFxoFarEndDisconnectType=acAnalogFxoFarEndDisconnectType, acAnalogFxsLineTestAnalogVoltageReading=acAnalogFxsLineTestAnalogVoltageReading, acAnalogFxoAction=acAnalogFxoAction, acAnalogFxoFarEndDisconnectToneIndex=acAnalogFxoFarEndDisconnectToneIndex, acAnalogFxoFarEndDisconnectToneType=acAnalogFxoFarEndDisconnectToneType, acAnalogLegsDTMFDetection=acAnalogLegsDTMFDetection, acAnalogFxoFarEndDisconnectToneRowStatus=acAnalogFxoFarEndDisconnectToneRowStatus, acAnalogMiscFlashHookPeriod=acAnalogMiscFlashHookPeriod, acAnalogFxoLineTestPolarityStatus=acAnalogFxoLineTestPolarityStatus, acAnalogStatusMiscFxsOrFxo=acAnalogStatusMiscFxsOrFxo, PYSNMP_MODULE_ID=acAnalog, acAnalogCommonAction=acAnalogCommonAction, acAnalogFxoLineTestLineVoltage=acAnalogFxoLineTestLineVoltage, acAnalogFxsBellcoreCallerIDTypeOneSubStandard=acAnalogFxsBellcoreCallerIDTypeOneSubStandard, acAnalogFxoDCRemover=acAnalogFxoDCRemover, acAnalogCommonChannelEntry=acAnalogCommonChannelEntry)

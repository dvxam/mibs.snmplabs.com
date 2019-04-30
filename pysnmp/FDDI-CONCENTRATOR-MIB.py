#
# PySNMP MIB module FDDI-CONCENTRATOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDDI-CONCENTRATOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, enterprises, IpAddress, iso, Bits, Integer32, Gauge32, ModuleIdentity, ObjectIdentity, Unsigned32, NotificationType, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "IpAddress", "iso", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "NotificationType", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fibronics = MibIdentifier((1, 3, 6, 1, 4, 1, 22))
fddiConcentrator = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70))
concentratorPORT = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70, 1))
concentratorPROCESSOR = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70, 2))
concentratorMEMORY = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70, 3))
concentratorSERIALPORT = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70, 4))
concentratorVERSIONS = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70, 5))
concentratorPOWER = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70, 6))
concentratorTRAPS = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70, 7))
concentratorIDENTIFIER = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70, 8))
concentratorTRAFFIC = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 70, 9))
concentratorPORTTable = MibTable((1, 3, 6, 1, 4, 1, 22, 70, 1, 1), )
if mibBuilder.loadTexts: concentratorPORTTable.setStatus('mandatory')
concentratorPORTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1), ).setIndexNames((0, "FDDI-CONCENTRATOR-MIB", "concentratorPORTSMTIndex"), (0, "FDDI-CONCENTRATOR-MIB", "concentratorPORTIndex"))
if mibBuilder.loadTexts: concentratorPORTEntry.setStatus('mandatory')
concentratorPORTSMTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPORTSMTIndex.setStatus('mandatory')
concentratorPORTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPORTIndex.setStatus('mandatory')
concentratorPORTType = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unknown", 1), ("fiber", 2), ("utp", 3), ("stp", 4), ("ibm", 5), ("plastic", 6), ("baseT", 7), ("mono", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPORTType.setStatus('mandatory')
concentratorPORTStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("failed", 2), ("undefind", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPORTStatus.setStatus('mandatory')
concentratorPROCESSORType = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unkown", 1), ("p88", 2), ("p86", 3), ("p186", 4), ("p286", 5), ("p386", 6), ("p486", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPROCESSORType.setStatus('mandatory')
concentratorPROCESSORFrequency = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPROCESSORFrequency.setStatus('mandatory')
concentratorSystemMEMORYAvailable = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorSystemMEMORYAvailable.setStatus('mandatory')
concentratorSystemMEMORYFree = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorSystemMEMORYFree.setStatus('mandatory')
concentratorBufferMEMORYAvailable = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorBufferMEMORYAvailable.setStatus('mandatory')
concentratorMEMORYFlashEPROM = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notpresent", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorMEMORYFlashEPROM.setStatus('mandatory')
concentratorSERIALPORTBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concentratorSERIALPORTBaudRate.setStatus('mandatory')
concentratorSERIALPORTParity = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("odd", 2), ("even", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorSERIALPORTParity.setStatus('mandatory')
concentratorSERIALPORTStopBits = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorSERIALPORTStopBits.setStatus('mandatory')
concentratorVERSIONSBoardSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 5, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONSBoardSerialNumber.setStatus('mandatory')
concentratorVERSIONSNMP = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 5, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONSNMP.setStatus('mandatory')
concentratorVERSIONBIOS = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 5, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONBIOS.setStatus('mandatory')
concentratorVERSIONSMT = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 5, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONSMT.setStatus('mandatory')
concentratorVERSIONMAC = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 5, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONMAC.setStatus('mandatory')
concentratorVERSIONHRDWR = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 5, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONHRDWR.setStatus('mandatory')
concentratorVERSIONSlotsNumber = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 5, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONSlotsNumber.setStatus('mandatory')
concentratorVERSIONSlotsTable = MibTable((1, 3, 6, 1, 4, 1, 22, 70, 5, 8), )
if mibBuilder.loadTexts: concentratorVERSIONSlotsTable.setStatus('mandatory')
concentratorVERSIONSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1), ).setIndexNames((0, "FDDI-CONCENTRATOR-MIB", "concentratorVERSIONSlotIndex"))
if mibBuilder.loadTexts: concentratorVERSIONSlotEntry.setStatus('mandatory')
concentratorVERSIONSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONSlotIndex.setStatus('mandatory')
concentratorVERSIONSlotSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONSlotSerialNumber.setStatus('mandatory')
concentratorVERSIONSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONSlotId.setStatus('mandatory')
concentratorVERSIONSlotHrdwrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONSlotHrdwrStatus.setStatus('mandatory')
concentratorVERSIONSlotRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorVERSIONSlotRevision.setStatus('mandatory')
concentratorPOWERFirstSupplyState = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2), ("notpresent", 3), ("reserved", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPOWERFirstSupplyState.setStatus('mandatory')
concentratorPOWERSecondSupplyState = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2), ("notpresent", 3), ("reserved", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPOWERSecondSupplyState.setStatus('mandatory')
concentratorPOWERFirstFANState = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPOWERFirstFANState.setStatus('mandatory')
concentratorPOWERSecondFANState = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPOWERSecondFANState.setStatus('mandatory')
concentratorPOWERTemperature = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPOWERTemperature.setStatus('mandatory')
concentratorPOWERBatteryStatus = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 6, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2), ("notpresent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorPOWERBatteryStatus.setStatus('mandatory')
concentratorMgrAddress = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 7, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concentratorMgrAddress.setStatus('mandatory')
concentratorTRAFFICSMTTransmits = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 9, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorTRAFFICSMTTransmits.setStatus('mandatory')
concentratorTRAFFICSMTReceivs = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 9, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorTRAFFICSMTReceivs.setStatus('mandatory')
concentratorTRAFFICRS232Activity = MibScalar((1, 3, 6, 1, 4, 1, 22, 70, 9, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("nonactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concentratorTRAFFICRS232Activity.setStatus('mandatory')
mibBuilder.exportSymbols("FDDI-CONCENTRATOR-MIB", concentratorPORTEntry=concentratorPORTEntry, concentratorPORTIndex=concentratorPORTIndex, concentratorPORTType=concentratorPORTType, concentratorBufferMEMORYAvailable=concentratorBufferMEMORYAvailable, concentratorVERSIONSlotRevision=concentratorVERSIONSlotRevision, concentratorPROCESSORType=concentratorPROCESSORType, concentratorVERSIONSlotsNumber=concentratorVERSIONSlotsNumber, concentratorPROCESSOR=concentratorPROCESSOR, concentratorTRAPS=concentratorTRAPS, concentratorSERIALPORTBaudRate=concentratorSERIALPORTBaudRate, concentratorMEMORY=concentratorMEMORY, concentratorPOWERSecondSupplyState=concentratorPOWERSecondSupplyState, concentratorTRAFFICRS232Activity=concentratorTRAFFICRS232Activity, concentratorTRAFFIC=concentratorTRAFFIC, concentratorSERIALPORTStopBits=concentratorSERIALPORTStopBits, concentratorVERSIONSlotEntry=concentratorVERSIONSlotEntry, concentratorPORTTable=concentratorPORTTable, concentratorPOWERSecondFANState=concentratorPOWERSecondFANState, concentratorSystemMEMORYFree=concentratorSystemMEMORYFree, concentratorTRAFFICSMTReceivs=concentratorTRAFFICSMTReceivs, concentratorMEMORYFlashEPROM=concentratorMEMORYFlashEPROM, concentratorTRAFFICSMTTransmits=concentratorTRAFFICSMTTransmits, concentratorVERSIONSlotIndex=concentratorVERSIONSlotIndex, concentratorSERIALPORTParity=concentratorSERIALPORTParity, concentratorPORTSMTIndex=concentratorPORTSMTIndex, concentratorVERSIONS=concentratorVERSIONS, concentratorIDENTIFIER=concentratorIDENTIFIER, concentratorVERSIONSBoardSerialNumber=concentratorVERSIONSBoardSerialNumber, concentratorVERSIONBIOS=concentratorVERSIONBIOS, concentratorSystemMEMORYAvailable=concentratorSystemMEMORYAvailable, fibronics=fibronics, concentratorVERSIONSlotSerialNumber=concentratorVERSIONSlotSerialNumber, concentratorPOWERTemperature=concentratorPOWERTemperature, concentratorVERSIONSlotId=concentratorVERSIONSlotId, concentratorPROCESSORFrequency=concentratorPROCESSORFrequency, concentratorPORT=concentratorPORT, fddiConcentrator=fddiConcentrator, concentratorPOWERFirstSupplyState=concentratorPOWERFirstSupplyState, concentratorPOWER=concentratorPOWER, concentratorVERSIONMAC=concentratorVERSIONMAC, concentratorVERSIONSlotHrdwrStatus=concentratorVERSIONSlotHrdwrStatus, concentratorPOWERBatteryStatus=concentratorPOWERBatteryStatus, concentratorVERSIONSMT=concentratorVERSIONSMT, concentratorPORTStatus=concentratorPORTStatus, concentratorVERSIONHRDWR=concentratorVERSIONHRDWR, concentratorPOWERFirstFANState=concentratorPOWERFirstFANState, concentratorVERSIONSNMP=concentratorVERSIONSNMP, concentratorSERIALPORT=concentratorSERIALPORT, concentratorVERSIONSlotsTable=concentratorVERSIONSlotsTable, concentratorMgrAddress=concentratorMgrAddress)

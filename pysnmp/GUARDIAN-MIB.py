#
# PySNMP MIB module GUARDIAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GUARDIAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, NotificationType, IpAddress, MibIdentifier, Integer32, Counter32, Gauge32, Counter64, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "NotificationType", "IpAddress", "MibIdentifier", "Integer32", "Counter32", "Gauge32", "Counter64", "enterprises", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
westek = MibIdentifier((1, 3, 6, 1, 4, 1, 3166))
guardian = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1))
device = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2))
masks = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 4))
special = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 5))
devInput = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1))
devFan = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2))
devTemp = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3))
devISA = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4))
devDC = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5))
devInput1 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 1))
devInput2 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 2))
devInput3 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 3))
devInput4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 4))
devFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1))
devFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2))
devFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3))
devFan4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4))
devTemp1 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1))
devTemp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2))
devTemp3 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3))
devTemp4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4))
devTemp5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5))
devTemp6 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6))
devTemp7 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7))
devTemp8 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8))
devISAP12 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1))
devISAP5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2))
devISAN5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3))
devISAN12 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4))
devDCP12 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1))
devDCP5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2))
guardianRev = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: guardianRev.setStatus('mandatory')
control = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("reset", 1), ("updatenvr", 2), ("reset2nvr", 3), ("reset2fac", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: control.setStatus('mandatory')
devInpStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInpStat.setStatus('mandatory')
devFanStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFanStat.setStatus('mandatory')
devTempStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTempStat.setStatus('mandatory')
devISAStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAStat.setStatus('mandatory')
devDCStat = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCStat.setStatus('mandatory')
devInp1Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp1Val.setStatus('mandatory')
devInp1Pol = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp1Pol.setStatus('mandatory')
devInp2Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp2Val.setStatus('mandatory')
devInp2Pol = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp2Pol.setStatus('mandatory')
devInp3Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp3Val.setStatus('mandatory')
devInp3Pol = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp3Pol.setStatus('mandatory')
devInp4Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp4Val.setStatus('mandatory')
devInp4Pol = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devInp4Pol.setStatus('mandatory')
devFan1Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFan1Val.setStatus('mandatory')
devFan1Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan1Min.setStatus('mandatory')
devFan1Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan1Max.setStatus('mandatory')
devFan2Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFan2Val.setStatus('mandatory')
devFan2Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan2Min.setStatus('mandatory')
devFan2Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan2Max.setStatus('mandatory')
devFan3Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFan3Val.setStatus('mandatory')
devFan3Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan3Min.setStatus('mandatory')
devFan3Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan3Max.setStatus('mandatory')
devFan4Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFan4Val.setStatus('mandatory')
devFan4Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan4Min.setStatus('mandatory')
devFan4Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devFan4Max.setStatus('mandatory')
devTemp1Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp1Val.setStatus('mandatory')
devTemp1Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp1Min.setStatus('mandatory')
devTemp1Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp1Max.setStatus('mandatory')
devTemp2Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp2Val.setStatus('mandatory')
devTemp2Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp2Min.setStatus('mandatory')
devTemp2Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp2Max.setStatus('mandatory')
devTemp3Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp3Val.setStatus('mandatory')
devTemp3Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp3Min.setStatus('mandatory')
devTemp3Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp3Max.setStatus('mandatory')
devTemp4Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp4Val.setStatus('mandatory')
devTemp4Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp4Min.setStatus('mandatory')
devTemp4Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp4Max.setStatus('mandatory')
devTemp5Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp5Val.setStatus('mandatory')
devTemp5Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp5Min.setStatus('mandatory')
devTemp5Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp5Max.setStatus('mandatory')
devTemp6Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp6Val.setStatus('mandatory')
devTemp6Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp6Min.setStatus('mandatory')
devTemp6Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp6Max.setStatus('mandatory')
devTemp7Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp7Val.setStatus('mandatory')
devTemp7Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp7Min.setStatus('mandatory')
devTemp7Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp7Max.setStatus('mandatory')
devTemp8Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTemp8Val.setStatus('mandatory')
devTemp8Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp8Min.setStatus('mandatory')
devTemp8Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-23, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devTemp8Max.setStatus('mandatory')
devISAP12Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devISAP12Val.setStatus('mandatory')
devISAP12Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAP12Min.setStatus('mandatory')
devISAP12Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAP12Max.setStatus('mandatory')
devISAP5Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devISAP5Val.setStatus('mandatory')
devISAP5Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAP5Min.setStatus('mandatory')
devISAP5Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAP5Max.setStatus('mandatory')
devISAN5Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devISAN5Val.setStatus('mandatory')
devISAN5Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAN5Min.setStatus('mandatory')
devISAN5Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAN5Max.setStatus('mandatory')
devISAN12Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devISAN12Val.setStatus('mandatory')
devISAN12Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAN12Min.setStatus('mandatory')
devISAN12Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devISAN12Max.setStatus('mandatory')
devDCP12Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDCP12Val.setStatus('mandatory')
devDCP12Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCP12Min.setStatus('mandatory')
devDCP12Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCP12Max.setStatus('mandatory')
devDCP5Val = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDCP5Val.setStatus('mandatory')
devDCP5Min = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCP5Min.setStatus('mandatory')
devDCP5Max = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 700))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDCP5Max.setStatus('mandatory')
fanErrors = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fanErrors.setStatus('mandatory')
tempErrors = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempErrors.setStatus('mandatory')
isaErrors = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isaErrors.setStatus('mandatory')
dcErrors = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcErrors.setStatus('mandatory')
inputPSU = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inputPSU.setStatus('mandatory')
inputTamper = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inputTamper.setStatus('mandatory')
enOutput0 = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enOutput0.setStatus('mandatory')
enOutput1 = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enOutput1.setStatus('mandatory')
enOutput2 = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enOutput2.setStatus('mandatory')
enOutput3 = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enOutput3.setStatus('mandatory')
enBeeper = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enBeeper.setStatus('mandatory')
enRelay = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enRelay.setStatus('mandatory')
enReset = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 4, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enReset.setStatus('mandatory')
watchdog = MibScalar((1, 3, 6, 1, 4, 1, 3166, 1, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: watchdog.setStatus('mandatory')
inputsAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,0))
fanAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,1))
tempAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,2))
isaAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,3))
dcAlert = NotificationType((1, 3, 6, 1, 4, 1, 3166, 1) + (0,4))
mibBuilder.exportSymbols("GUARDIAN-MIB", devFan3Min=devFan3Min, devISA=devISA, devTemp3=devTemp3, devInp4Pol=devInp4Pol, devTemp8Max=devTemp8Max, inputPSU=inputPSU, devTemp1=devTemp1, devTemp3Val=devTemp3Val, devISAN12Max=devISAN12Max, devISAP12Max=devISAP12Max, tempAlert=tempAlert, devFan4Max=devFan4Max, devTemp3Max=devTemp3Max, devFan=devFan, devTemp1Max=devTemp1Max, devDCP12Val=devDCP12Val, inputsAlert=inputsAlert, devDC=devDC, devDCP12=devDCP12, devInp2Val=devInp2Val, devInp2Pol=devInp2Pol, devTemp6=devTemp6, isaErrors=isaErrors, devISAP12Min=devISAP12Min, devFanStat=devFanStat, devFan1Min=devFan1Min, isaAlert=isaAlert, devISAStat=devISAStat, devTemp8Min=devTemp8Min, devDCStat=devDCStat, devInput=devInput, devInp3Val=devInp3Val, devTemp7Min=devTemp7Min, devTemp1Min=devTemp1Min, devTemp4Min=devTemp4Min, devTemp7=devTemp7, devTemp2Max=devTemp2Max, devDCP5Min=devDCP5Min, devFan2=devFan2, devFan4=devFan4, devTemp1Val=devTemp1Val, devFan1Val=devFan1Val, devInput4=devInput4, devInp1Pol=devInp1Pol, devFan2Max=devFan2Max, devTemp2=devTemp2, fanErrors=fanErrors, devFan4Min=devFan4Min, enRelay=enRelay, fanAlert=fanAlert, enOutput2=enOutput2, enReset=enReset, devISAN12=devISAN12, tempErrors=tempErrors, devISAN5=devISAN5, control=control, devTemp8=devTemp8, devFan2Val=devFan2Val, devFan4Val=devFan4Val, devTemp6Val=devTemp6Val, dcErrors=dcErrors, devDCP5=devDCP5, devTemp7Val=devTemp7Val, masks=masks, devFan1=devFan1, devInp1Val=devInp1Val, devTemp2Min=devTemp2Min, westek=westek, devISAN12Min=devISAN12Min, devISAN5Max=devISAN5Max, devTemp4Val=devTemp4Val, enOutput3=enOutput3, devISAP5=devISAP5, devTemp8Val=devTemp8Val, devInput2=devInput2, devTemp3Min=devTemp3Min, devInpStat=devInpStat, devTempStat=devTempStat, inputTamper=inputTamper, devTemp7Max=devTemp7Max, devTemp5Min=devTemp5Min, devFan1Max=devFan1Max, devFan2Min=devFan2Min, devFan3=devFan3, devTemp4Max=devTemp4Max, devTemp2Val=devTemp2Val, enBeeper=enBeeper, devDCP5Max=devDCP5Max, devISAP12Val=devISAP12Val, devFan3Val=devFan3Val, devISAP5Min=devISAP5Min, dcAlert=dcAlert, guardianRev=guardianRev, devTemp=devTemp, enOutput1=enOutput1, devISAN5Min=devISAN5Min, devInput1=devInput1, device=device, devTemp5Val=devTemp5Val, devISAN12Val=devISAN12Val, devDCP12Min=devDCP12Min, devTemp6Max=devTemp6Max, devISAP12=devISAP12, guardian=guardian, devInp4Val=devInp4Val, devInput3=devInput3, devTemp5=devTemp5, devISAP5Max=devISAP5Max, devISAP5Val=devISAP5Val, devInp3Pol=devInp3Pol, devDCP12Max=devDCP12Max, devFan3Max=devFan3Max, watchdog=watchdog, devDCP5Val=devDCP5Val, enOutput0=enOutput0, special=special, devTemp5Max=devTemp5Max, devTemp4=devTemp4, devTemp6Min=devTemp6Min, devISAN5Val=devISAN5Val)
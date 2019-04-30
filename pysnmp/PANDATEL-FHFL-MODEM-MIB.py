#
# PySNMP MIB module PANDATEL-FHFL-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANDATEL-FHFL-MODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mdmSpecifics, device_id = mibBuilder.importSymbols("PANDATEL-MODEM-MIB", "mdmSpecifics", "device-id")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Bits, NotificationType, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter64, IpAddress, Counter32, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "NotificationType", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter64", "IpAddress", "Counter32", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fhfl_modem = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 101)).setLabel("fhfl-modem")
fhfl = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101))
fhflModemTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1), )
if mibBuilder.loadTexts: fhflModemTable.setStatus('mandatory')
fhflTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1), ).setIndexNames((0, "PANDATEL-FHFL-MODEM-MIB", "mdmRack"), (0, "PANDATEL-FHFL-MODEM-MIB", "mdmModem"), (0, "PANDATEL-FHFL-MODEM-MIB", "mdmPosition"))
if mibBuilder.loadTexts: fhflTableEntry.setStatus('mandatory')
mdmRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmRack.setStatus('mandatory')
mdmModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModem.setStatus('mandatory')
mdmPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmPosition.setStatus('mandatory')
mdmModemName = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemName.setStatus('mandatory')
mdmInterfaceEmulationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 99))).clone(namedValues=NamedValues(("other", 1), ("dte", 2), ("dce", 3), ("te", 4), ("nt", 5), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmInterfaceEmulationMode.setStatus('mandatory')
mdmModemProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 99))).clone(namedValues=NamedValues(("other", 1), ("e1", 2), ("t1", 3), ("e2", 4), ("t2", 5), ("e1-t1", 6), ("e2-t2", 7), ("e3", 8), ("t3", 9), ("hssi", 10), ("atm", 11), ("eth10base-t-fullduplex", 12), ("eth10base-t-halfduplex", 13), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemProperty.setStatus('mandatory')
mdmClockSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("dual", 2), ("single", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockSystem.setStatus('mandatory')
mdmClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("internal", 2), ("remote", 3), ("external", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockSource.setStatus('mandatory')
mdmDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("other", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDataRate.setStatus('mandatory')
mdmLocalCarrierDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 101, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("fo-link-and-remote-handshake", 2), ("fo-link", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmLocalCarrierDetect.setStatus('mandatory')
mibBuilder.exportSymbols("PANDATEL-FHFL-MODEM-MIB", fhfl=fhfl, mdmClockSource=mdmClockSource, mdmPosition=mdmPosition, fhflModemTable=fhflModemTable, mdmClockSystem=mdmClockSystem, mdmModemName=mdmModemName, fhflTableEntry=fhflTableEntry, mdmLocalCarrierDetect=mdmLocalCarrierDetect, fhfl_modem=fhfl_modem, mdmModem=mdmModem, mdmDataRate=mdmDataRate, mdmRack=mdmRack, mdmModemProperty=mdmModemProperty, mdmInterfaceEmulationMode=mdmInterfaceEmulationMode)

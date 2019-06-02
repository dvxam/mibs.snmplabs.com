#
# PySNMP MIB module DEVCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEVCONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:41:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter64, IpAddress, iso, Bits, NotificationType, ModuleIdentity, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter64", "IpAddress", "iso", "Bits", "NotificationType", "ModuleIdentity", "Unsigned32", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
aniDevControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 4))
if mibBuilder.loadTexts: aniDevControl.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevControl.setOrganization('Aperto Networks')
if mibBuilder.loadTexts: aniDevControl.setContactInfo(' Postal: Aperto Networks Inc 1637 S Main Street Milpitas, California 95035 Tel: +1 408 719 9977 ')
if mibBuilder.loadTexts: aniDevControl.setDescription('This group allows users to handle device control operations like resetting the device and setting to factory defaults. It can be used for both BSU and SU. ')
aniDevControlResetDevice = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevControlResetDevice.setStatus('current')
if mibBuilder.loadTexts: aniDevControlResetDevice.setDescription('Setting this object to true(1) causes the device to reset. Setting the object to false(2) is not allowed. If a Get request is sent before this object is actually set, the value false(2) will be returned. ')
aniDevControlSetFactoryDefaults = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevControlSetFactoryDefaults.setStatus('current')
if mibBuilder.loadTexts: aniDevControlSetFactoryDefaults.setDescription('This object provides an option to reset configuration parameters to factory defaults. Setting this object to true(1) allows restoring all configuration parameters to factory default values. Setting the object to false(2) is not allowed. If a Get request is sent before this object is actually set, the value false(2) will be returned. Note: This parameter is not supported for this release. Hence it is defined as a read-only object. ')
aniDevControlStartUpload = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevControlStartUpload.setStatus('current')
if mibBuilder.loadTexts: aniDevControlStartUpload.setDescription('Setting this object to true(1) causes the device to upload the entire Configuration File onto the TFTP server on the service provider side. aniDevTftpServer is the designated TFTP server used in this upload process. Setting the object to false(2) is not allowed. If a Get request is sent before this object is actually set, the value false(2) will be returned. ')
aniDevControlUploadState = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("successful", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevControlUploadState.setStatus('current')
if mibBuilder.loadTexts: aniDevControlUploadState.setDescription('Reading this object returns the status of the previous upload process. The possible return values are: successful(1) - upload operation completed successfully failed(2) - upload operation failed If a Get request is sent before aniDevControlStartUpload is actually set, the value successful(1) will be returned by default. ')
mibBuilder.exportSymbols("DEVCONTROL-MIB", PYSNMP_MODULE_ID=aniDevControl, aniDevControlStartUpload=aniDevControlStartUpload, aniDevControlResetDevice=aniDevControlResetDevice, aniDevControlUploadState=aniDevControlUploadState, aniDevControlSetFactoryDefaults=aniDevControlSetFactoryDefaults, aniDevControl=aniDevControl)
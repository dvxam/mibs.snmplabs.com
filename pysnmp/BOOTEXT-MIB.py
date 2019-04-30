#
# PySNMP MIB module BOOTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BOOTEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:22:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bootExt, = mibBuilder.importSymbols("APENT-MIB", "bootExt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Bits, TimeTicks, Counter32, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Bits", "TimeTicks", "Counter32", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bootExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 31, 1))
if mibBuilder.loadTexts: bootExtMib.setLastUpdated('9801282000Z')
if mibBuilder.loadTexts: bootExtMib.setOrganization('ArrowPoint Communications Inc.')
apBootBootP = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootBootP.setStatus('current')
apBootIpOfSystem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootIpOfSystem.setStatus('current')
apBootPrimaryType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3), ("not-configured", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootPrimaryType.setStatus('current')
apBootPrimaryFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootPrimaryFileName.setStatus('current')
apBootPrimaryFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootPrimaryFTPRecordName.setStatus('current')
apBootSecondaryType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3), ("not-configured", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootSecondaryType.setStatus('current')
apBootSecondaryFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootSecondaryFileName.setStatus('current')
apBootSecondaryFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootSecondaryFTPRecordName.setStatus('current')
apBootLastType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootLastType.setStatus('current')
apBootLastFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootLastFileName.setStatus('current')
apBootLastFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootLastFTPRecordName.setStatus('current')
apBootNetmaskOfSystem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootNetmaskOfSystem.setStatus('current')
apBootRedundantBootP = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantBootP.setStatus('current')
apBootRedundantIpOfSystem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantIpOfSystem.setStatus('current')
apBootRedundantPrimaryType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3), ("not-configured", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantPrimaryType.setStatus('current')
apBootRedundantPrimaryFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantPrimaryFileName.setStatus('current')
apBootRedundantPrimaryFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantPrimaryFTPRecordName.setStatus('current')
apBootRedundantSecondaryType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3), ("not-configured", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantSecondaryType.setStatus('current')
apBootRedundantSecondaryFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantSecondaryFileName.setStatus('current')
apBootRedundantSecondaryFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantSecondaryFTPRecordName.setStatus('current')
apBootRedundantLastType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootRedundantLastType.setStatus('current')
apBootRedundantLastFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootRedundantLastFileName.setStatus('current')
apBootRedundantLastFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootRedundantLastFTPRecordName.setStatus('current')
apBootRedundantNetmaskOfSystem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 25), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantNetmaskOfSystem.setStatus('current')
apBootPrimaryAltCfgPath = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootPrimaryAltCfgPath.setStatus('current')
apBootSecondaryAltCfgPath = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootSecondaryAltCfgPath.setStatus('current')
apBootRedundantPrimaryAltCfgPath = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantPrimaryAltCfgPath.setStatus('current')
apBootRedundantSecondaryAltCfgPath = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantSecondaryAltCfgPath.setStatus('current')
mibBuilder.exportSymbols("BOOTEXT-MIB", apBootPrimaryType=apBootPrimaryType, apBootRedundantLastFileName=apBootRedundantLastFileName, apBootRedundantLastFTPRecordName=apBootRedundantLastFTPRecordName, apBootLastFileName=apBootLastFileName, apBootLastFTPRecordName=apBootLastFTPRecordName, apBootPrimaryFTPRecordName=apBootPrimaryFTPRecordName, apBootBootP=apBootBootP, apBootRedundantBootP=apBootRedundantBootP, apBootRedundantSecondaryType=apBootRedundantSecondaryType, apBootRedundantSecondaryFileName=apBootRedundantSecondaryFileName, apBootNetmaskOfSystem=apBootNetmaskOfSystem, apBootRedundantLastType=apBootRedundantLastType, bootExtMib=bootExtMib, apBootRedundantIpOfSystem=apBootRedundantIpOfSystem, PYSNMP_MODULE_ID=bootExtMib, apBootRedundantPrimaryFTPRecordName=apBootRedundantPrimaryFTPRecordName, apBootSecondaryType=apBootSecondaryType, apBootPrimaryAltCfgPath=apBootPrimaryAltCfgPath, apBootSecondaryFTPRecordName=apBootSecondaryFTPRecordName, apBootSecondaryFileName=apBootSecondaryFileName, apBootPrimaryFileName=apBootPrimaryFileName, apBootLastType=apBootLastType, apBootRedundantSecondaryAltCfgPath=apBootRedundantSecondaryAltCfgPath, apBootIpOfSystem=apBootIpOfSystem, apBootRedundantPrimaryType=apBootRedundantPrimaryType, apBootRedundantNetmaskOfSystem=apBootRedundantNetmaskOfSystem, apBootSecondaryAltCfgPath=apBootSecondaryAltCfgPath, apBootRedundantSecondaryFTPRecordName=apBootRedundantSecondaryFTPRecordName, apBootRedundantPrimaryAltCfgPath=apBootRedundantPrimaryAltCfgPath, apBootRedundantPrimaryFileName=apBootRedundantPrimaryFileName)

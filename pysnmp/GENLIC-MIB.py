#
# PySNMP MIB module GENLIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GENLIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Unsigned32, Gauge32, IpAddress, Integer32, enterprises, Bits, iso, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Unsigned32", "Gauge32", "IpAddress", "Integer32", "enterprises", "Bits", "iso", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lannet = MibIdentifier((1, 3, 6, 1, 4, 1, 81))
license = ModuleIdentity((1, 3, 6, 1, 4, 1, 81, 37))
if mibBuilder.loadTexts: license.setLastUpdated('0006220000Z')
if mibBuilder.loadTexts: license.setOrganization('Lucent Technologies Inc.')
licensePerModule = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 37, 1))
licModuleIdentTable = MibTable((1, 3, 6, 1, 4, 1, 81, 37, 1, 1), )
if mibBuilder.loadTexts: licModuleIdentTable.setStatus('current')
licModuleIdentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 37, 1, 1, 1), ).setIndexNames((0, "GENLIC-MIB", "licModuleIdentIndex"))
if mibBuilder.loadTexts: licModuleIdentEntry.setStatus('current')
licModuleIdentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 37, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licModuleIdentIndex.setStatus('current')
licModuleIdentUniqueID = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 37, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: licModuleIdentUniqueID.setStatus('current')
licFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 81, 37, 1, 2), )
if mibBuilder.loadTexts: licFeatureTable.setStatus('current')
licFeatureTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1), ).setIndexNames((0, "GENLIC-MIB", "licModuleIdentIndex"), (0, "GENLIC-MIB", "licFeatureId"))
if mibBuilder.loadTexts: licFeatureTableEntry.setStatus('current')
licFeatureId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 208, 209))).clone(namedValues=NamedValues(("smon", 1), ("richLayer2", 2), ("routing", 3), ("serverLoadBalance", 4), ("rfc1483", 5), ("loadBalance", 6), ("cajunViewPlus", 208), ("realNetRules", 209)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licFeatureId.setStatus('current')
licFeatureModifier = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: licFeatureModifier.setStatus('current')
licFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: licFeatureName.setStatus('current')
licFeatureLicense = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 12)).clone(hexValue="0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: licFeatureLicense.setStatus('current')
licFeatureLicenseStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 37, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("licensed", 1), ("unlicensed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licFeatureLicenseStatus.setStatus('current')
mibBuilder.exportSymbols("GENLIC-MIB", lannet=lannet, licModuleIdentTable=licModuleIdentTable, licFeatureLicenseStatus=licFeatureLicenseStatus, licensePerModule=licensePerModule, licModuleIdentEntry=licModuleIdentEntry, licFeatureId=licFeatureId, license=license, licModuleIdentIndex=licModuleIdentIndex, licFeatureTable=licFeatureTable, licFeatureModifier=licFeatureModifier, licFeatureTableEntry=licFeatureTableEntry, licFeatureLicense=licFeatureLicense, licModuleIdentUniqueID=licModuleIdentUniqueID, licFeatureName=licFeatureName, PYSNMP_MODULE_ID=license)

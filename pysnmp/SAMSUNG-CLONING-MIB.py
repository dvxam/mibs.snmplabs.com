#
# PySNMP MIB module SAMSUNG-CLONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-CLONING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hrDeviceIndex, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrDeviceIndex")
samsungCommonMIB, = mibBuilder.importSymbols("SAMSUNG-COMMON-MIB", "samsungCommonMIB")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Integer32, NotificationType, TimeTicks, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Unsigned32, Counter64, MibIdentifier, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "NotificationType", "TimeTicks", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Unsigned32", "Counter64", "MibIdentifier", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
scmCloningMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82))
if mibBuilder.loadTexts: scmCloningMIB.setLastUpdated('200511090000Z')
if mibBuilder.loadTexts: scmCloningMIB.setOrganization('Samsung Common Management Interface Working Group')
scmCloning = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1))
scmCloningTable = MibTable((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1), )
if mibBuilder.loadTexts: scmCloningTable.setStatus('current')
scmCloningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1), ).setIndexNames((0, "SAMSUNG-CLONING-MIB", "scmCloningIndex"))
if mibBuilder.loadTexts: scmCloningEntry.setStatus('current')
scmCloningIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningIndex.setStatus('current')
scmCloningIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningIPAddress.setStatus('current')
scmCloningResult = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("completed", 1), ("processing", 2), ("invalidFile", 3), ("versionMismatch", 4), ("notSupportedCloning", 5), ("busy", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningResult.setStatus('current')
scmCloningDate = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningDate.setStatus('current')
scmCloningSimple = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2))
scmCloningLastIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningLastIPAddress.setStatus('current')
scmCloningLastResult = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("completed", 1), ("processing", 2), ("invalidFile", 3), ("versionMismatch", 4), ("notSupportedCloning", 5), ("busy", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningLastResult.setStatus('current')
scmCloningLastDate = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningLastDate.setStatus('current')
scmCloningSupported = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningSupported.setStatus('current')
scmCloningTrap = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 3))
if mibBuilder.loadTexts: scmCloningTrap.setStatus('current')
scmCloningTrapSimple = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 3, 1))
scmCloningTrapResult = NotificationType((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 3, 1, 1)).setObjects(("SAMSUNG-CLONING-MIB", "scmCloningLastIPAddress"), ("SAMSUNG-CLONING-MIB", "scmCloningLastResult"))
if mibBuilder.loadTexts: scmCloningTrapResult.setStatus('current')
mibBuilder.exportSymbols("SAMSUNG-CLONING-MIB", scmCloningMIB=scmCloningMIB, scmCloningIPAddress=scmCloningIPAddress, scmCloningLastResult=scmCloningLastResult, scmCloningSimple=scmCloningSimple, scmCloningLastDate=scmCloningLastDate, scmCloningResult=scmCloningResult, scmCloningEntry=scmCloningEntry, scmCloningTable=scmCloningTable, scmCloningTrapSimple=scmCloningTrapSimple, scmCloningLastIPAddress=scmCloningLastIPAddress, scmCloningTrapResult=scmCloningTrapResult, scmCloningSupported=scmCloningSupported, PYSNMP_MODULE_ID=scmCloningMIB, scmCloning=scmCloning, scmCloningTrap=scmCloningTrap, scmCloningIndex=scmCloningIndex, scmCloningDate=scmCloningDate)

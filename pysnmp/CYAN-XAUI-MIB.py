#
# PySNMP MIB module CYAN-XAUI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-XAUI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
cyanEntityModules, = mibBuilder.importSymbols("CYAN-MIB", "cyanEntityModules")
CyanAdminStateTc, CyanOpStateQualTc, CyanSecServiceStateTc, CyanOpStateTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanAdminStateTc", "CyanOpStateQualTc", "CyanSecServiceStateTc", "CyanOpStateTc")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, iso, MibIdentifier, Unsigned32, Bits, NotificationType, ModuleIdentity, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "iso", "MibIdentifier", "Unsigned32", "Bits", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyanXauiModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170))
cyanXauiModule.setRevisions(('2014-12-07 05:45',))
if mibBuilder.loadTexts: cyanXauiModule.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanXauiModule.setOrganization('Cyan, Inc.')
cyanXauiMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1))
cyanXauiTable = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1), )
if mibBuilder.loadTexts: cyanXauiTable.setStatus('current')
cyanXauiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1), ).setIndexNames((0, "CYAN-XAUI-MIB", "cyanXauiShelfId"), (0, "CYAN-XAUI-MIB", "cyanXauiModuleId"), (0, "CYAN-XAUI-MIB", "cyanXauiXauiId"))
if mibBuilder.loadTexts: cyanXauiEntry.setStatus('current')
cyanXauiShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanXauiShelfId.setStatus('current')
cyanXauiModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanXauiModuleId.setStatus('current')
cyanXauiXauiId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cyanXauiXauiId.setStatus('current')
cyanXauiAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 4), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiAdminState.setStatus('current')
cyanXauiAutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiAutoinserviceSoakTimeSec.setStatus('current')
cyanXauiOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 6), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiOperState.setStatus('current')
cyanXauiOperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 7), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiOperStateQual.setStatus('current')
cyanXauiPortSpeedMbps = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiPortSpeedMbps.setStatus('current')
cyanXauiSecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 9), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiSecServState.setStatus('current')
cyanXauiObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 20)).setObjects(("CYAN-XAUI-MIB", "cyanXauiAdminState"), ("CYAN-XAUI-MIB", "cyanXauiAutoinserviceSoakTimeSec"), ("CYAN-XAUI-MIB", "cyanXauiOperState"), ("CYAN-XAUI-MIB", "cyanXauiOperStateQual"), ("CYAN-XAUI-MIB", "cyanXauiPortSpeedMbps"), ("CYAN-XAUI-MIB", "cyanXauiSecServState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanXauiObjectGroup = cyanXauiObjectGroup.setStatus('current')
cyanXauiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 30)).setObjects(("CYAN-XAUI-MIB", "cyanXauiObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanXauiCompliance = cyanXauiCompliance.setStatus('current')
mibBuilder.exportSymbols("CYAN-XAUI-MIB", cyanXauiOperState=cyanXauiOperState, cyanXauiCompliance=cyanXauiCompliance, cyanXauiPortSpeedMbps=cyanXauiPortSpeedMbps, cyanXauiOperStateQual=cyanXauiOperStateQual, cyanXauiXauiId=cyanXauiXauiId, cyanXauiMibObjects=cyanXauiMibObjects, cyanXauiEntry=cyanXauiEntry, cyanXauiModule=cyanXauiModule, PYSNMP_MODULE_ID=cyanXauiModule, cyanXauiShelfId=cyanXauiShelfId, cyanXauiSecServState=cyanXauiSecServState, cyanXauiTable=cyanXauiTable, cyanXauiAutoinserviceSoakTimeSec=cyanXauiAutoinserviceSoakTimeSec, cyanXauiAdminState=cyanXauiAdminState, cyanXauiObjectGroup=cyanXauiObjectGroup, cyanXauiModuleId=cyanXauiModuleId)
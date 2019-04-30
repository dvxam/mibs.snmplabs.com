#
# PySNMP MIB module ENTERASYS-WIFI-PROTECTED-ACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-WIFI-PROTECTED-ACCESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:50:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, ModuleIdentity, Unsigned32, Counter64, Gauge32, TimeTicks, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "ModuleIdentity", "Unsigned32", "Counter64", "Gauge32", "TimeTicks", "ObjectIdentity", "MibIdentifier")
TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
etsysWiFiProtectedAccessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32))
etsysWiFiProtectedAccessMIB.setRevisions(('2003-11-06 15:15', '2003-08-07 17:08',))
if mibBuilder.loadTexts: etsysWiFiProtectedAccessMIB.setLastUpdated('200311061515Z')
if mibBuilder.loadTexts: etsysWiFiProtectedAccessMIB.setOrganization('Enterasys Networks, Inc')
etsysWiFiProtectedAccessObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1))
etsysWPAConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1), )
if mibBuilder.loadTexts: etsysWPAConfigTable.setStatus('current')
etsysWPAConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1), ).setIndexNames((0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigIndex"))
if mibBuilder.loadTexts: etsysWPAConfigEntry.setStatus('current')
etsysWPAConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: etsysWPAConfigIndex.setStatus('current')
etsysWPAConfigOptionImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAConfigOptionImplemented.setStatus('current')
etsysWPAConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigEnabled.setStatus('current')
etsysWPAConfigTKIPNumberOfReplayCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAConfigTKIPNumberOfReplayCounters.setStatus('current')
etsysWPAConfigVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAConfigVersion.setStatus('current')
etsysWPAConfigPairwiseKeysSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAConfigPairwiseKeysSupported.setStatus('current')
etsysWPAConfigMulticastCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigMulticastCipher.setStatus('current')
etsysWPAConfigGroupRekeyMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("timeBased", 2), ("packetBased", 3))).clone('timeBased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigGroupRekeyMethod.setStatus('current')
etsysWPAConfigGroupRekeyTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(86400)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigGroupRekeyTime.setStatus('current')
etsysWPAConfigGroupRekeyPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('1000 packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigGroupRekeyPackets.setStatus('current')
etsysWPAConfigGroupRekeyStrict = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigGroupRekeyStrict.setStatus('current')
etsysWPAConfigPSKValue = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigPSKValue.setStatus('current')
etsysWPAConfigPSKPassPhrase = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigPSKPassPhrase.setStatus('current')
etsysWPAConfigPSKValueEntered = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAConfigPSKValueEntered.setStatus('current')
etsysWPAConfigMultipleAuthSuitesSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAConfigMultipleAuthSuitesSupported.setStatus('current')
etsysWPAConfigGroupMasterRekeyTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(604800)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigGroupMasterRekeyTime.setStatus('current')
etsysWPAConfigGroupUpdateTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(100)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigGroupUpdateTimeOut.setStatus('current')
etsysWPAConfigGroupUpdateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigGroupUpdateCount.setStatus('current')
etsysWPAConfigPairwiseUpdateTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(100)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigPairwiseUpdateTimeOut.setStatus('current')
etsysWPAConfigPairwiseUpdateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigPairwiseUpdateCount.setStatus('current')
etsysWPAConfigLegacyOptionSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 21), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAConfigLegacyOptionSupported.setStatus('current')
etsysWPAConfigAllowLegacyClients = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 22), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigAllowLegacyClients.setStatus('current')
etsysWPAConfigRekeyPairwiseWEP = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 23), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigRekeyPairwiseWEP.setStatus('current')
etsysWPAConfigUnicastCiphersTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2), )
if mibBuilder.loadTexts: etsysWPAConfigUnicastCiphersTable.setStatus('current')
etsysWPAConfigUnicastCiphersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2, 1), ).setIndexNames((0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigIndex"), (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigUnicastCipherIndex"))
if mibBuilder.loadTexts: etsysWPAConfigUnicastCiphersEntry.setStatus('current')
etsysWPAConfigUnicastCipherIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: etsysWPAConfigUnicastCipherIndex.setStatus('current')
etsysWPAConfigUnicastCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAConfigUnicastCipher.setStatus('current')
etsysWPAConfigUnicastCipherEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigUnicastCipherEnabled.setStatus('current')
etsysWPAConfigAuthenticationSuitesTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3), )
if mibBuilder.loadTexts: etsysWPAConfigAuthenticationSuitesTable.setStatus('current')
etsysWPAConfigAuthenticationSuitesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3, 1), ).setIndexNames((0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigIndex"), (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigAuthenticationSuiteIndex"))
if mibBuilder.loadTexts: etsysWPAConfigAuthenticationSuitesEntry.setStatus('current')
etsysWPAConfigAuthenticationSuiteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: etsysWPAConfigAuthenticationSuiteIndex.setStatus('current')
etsysWPAConfigAuthenticationSuite = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAConfigAuthenticationSuite.setStatus('current')
etsysWPAConfigAuthenticationSuiteEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysWPAConfigAuthenticationSuiteEnabled.setStatus('current')
etsysWPAStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4), )
if mibBuilder.loadTexts: etsysWPAStatsTable.setStatus('current')
etsysWPAStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1), ).setIndexNames((0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigIndex"), (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsIndex"))
if mibBuilder.loadTexts: etsysWPAStatsEntry.setStatus('current')
etsysWPAStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: etsysWPAStatsIndex.setStatus('current')
etsysWPAStatsSTAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAStatsSTAAddress.setStatus('current')
etsysWPAStatsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAStatsVersion.setStatus('current')
etsysWPAStatsSelectedUnicastCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAStatsSelectedUnicastCipher.setStatus('current')
etsysWPAStatsTKIPICVErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAStatsTKIPICVErrors.setStatus('current')
etsysWPAStatsTKIPLocalMICFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAStatsTKIPLocalMICFailures.setStatus('current')
etsysWPAStatsTKIPRemoteMICFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAStatsTKIPRemoteMICFailures.setStatus('current')
etsysWPAStatsTKIPCounterMeasuresInvoked = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysWPAStatsTKIPCounterMeasuresInvoked.setStatus('current')
etsysWpaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2))
etsysWpaGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1))
etsysWpaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 2))
etsysWpaBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1, 1)).setObjects(("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigOptionImplemented"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigEnabled"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigTKIPNumberOfReplayCounters"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigVersion"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPairwiseKeysSupported"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigMulticastCipher"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupRekeyMethod"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupRekeyTime"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupRekeyPackets"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupRekeyStrict"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPSKValue"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPSKValueEntered"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigMultipleAuthSuitesSupported"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPSKPassPhrase"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupMasterRekeyTime"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupUpdateTimeOut"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupUpdateCount"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPairwiseUpdateTimeOut"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPairwiseUpdateCount"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigLegacyOptionSupported"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigAllowLegacyClients"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigRekeyPairwiseWEP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysWpaBaseGroup = etsysWpaBaseGroup.setStatus('current')
etsysWpaUnicastCipherGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1, 2)).setObjects(("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigUnicastCipher"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigUnicastCipherEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysWpaUnicastCipherGroup = etsysWpaUnicastCipherGroup.setStatus('current')
etsysWpaAuthSuiteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1, 3)).setObjects(("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigAuthenticationSuite"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigAuthenticationSuiteEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysWpaAuthSuiteGroup = etsysWpaAuthSuiteGroup.setStatus('current')
etsysWpaStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1, 4)).setObjects(("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsSTAAddress"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsVersion"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsSelectedUnicastCipher"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsTKIPICVErrors"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsTKIPLocalMICFailures"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsTKIPRemoteMICFailures"), ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsTKIPCounterMeasuresInvoked"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysWpaStatsGroup = etsysWpaStatsGroup.setStatus('current')
etsysWpaCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 2, 1)).setObjects(("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWpaBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysWpaCompliance = etsysWpaCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", etsysWPAConfigMultipleAuthSuitesSupported=etsysWPAConfigMultipleAuthSuitesSupported, etsysWpaStatsGroup=etsysWpaStatsGroup, etsysWpaAuthSuiteGroup=etsysWpaAuthSuiteGroup, etsysWpaGroups=etsysWpaGroups, etsysWPAConfigAuthenticationSuitesEntry=etsysWPAConfigAuthenticationSuitesEntry, etsysWPAConfigEntry=etsysWPAConfigEntry, etsysWPAConfigTable=etsysWPAConfigTable, etsysWPAConfigPSKValue=etsysWPAConfigPSKValue, etsysWPAConfigVersion=etsysWPAConfigVersion, etsysWPAConfigGroupUpdateTimeOut=etsysWPAConfigGroupUpdateTimeOut, etsysWPAConfigUnicastCiphersTable=etsysWPAConfigUnicastCiphersTable, etsysWPAConfigGroupUpdateCount=etsysWPAConfigGroupUpdateCount, etsysWPAConfigRekeyPairwiseWEP=etsysWPAConfigRekeyPairwiseWEP, etsysWPAConfigAuthenticationSuiteIndex=etsysWPAConfigAuthenticationSuiteIndex, etsysWPAStatsIndex=etsysWPAStatsIndex, etsysWPAStatsSTAAddress=etsysWPAStatsSTAAddress, PYSNMP_MODULE_ID=etsysWiFiProtectedAccessMIB, etsysWPAConfigPairwiseUpdateTimeOut=etsysWPAConfigPairwiseUpdateTimeOut, etsysWPAStatsTKIPRemoteMICFailures=etsysWPAStatsTKIPRemoteMICFailures, etsysWPAConfigAuthenticationSuite=etsysWPAConfigAuthenticationSuite, etsysWpaCompliance=etsysWpaCompliance, etsysWpaUnicastCipherGroup=etsysWpaUnicastCipherGroup, etsysWPAConfigGroupMasterRekeyTime=etsysWPAConfigGroupMasterRekeyTime, etsysWPAStatsTKIPLocalMICFailures=etsysWPAStatsTKIPLocalMICFailures, etsysWpaBaseGroup=etsysWpaBaseGroup, etsysWPAConfigPairwiseKeysSupported=etsysWPAConfigPairwiseKeysSupported, etsysWPAConfigAuthenticationSuiteEnabled=etsysWPAConfigAuthenticationSuiteEnabled, etsysWPAConfigGroupRekeyStrict=etsysWPAConfigGroupRekeyStrict, etsysWiFiProtectedAccessMIB=etsysWiFiProtectedAccessMIB, etsysWPAConfigUnicastCipher=etsysWPAConfigUnicastCipher, etsysWPAConfigPSKPassPhrase=etsysWPAConfigPSKPassPhrase, etsysWPAConfigAllowLegacyClients=etsysWPAConfigAllowLegacyClients, etsysWiFiProtectedAccessObjects=etsysWiFiProtectedAccessObjects, etsysWPAStatsTKIPICVErrors=etsysWPAStatsTKIPICVErrors, etsysWPAConfigLegacyOptionSupported=etsysWPAConfigLegacyOptionSupported, etsysWPAConfigGroupRekeyTime=etsysWPAConfigGroupRekeyTime, etsysWPAConfigTKIPNumberOfReplayCounters=etsysWPAConfigTKIPNumberOfReplayCounters, etsysWPAStatsEntry=etsysWPAStatsEntry, etsysWPAStatsSelectedUnicastCipher=etsysWPAStatsSelectedUnicastCipher, etsysWPAConfigPSKValueEntered=etsysWPAConfigPSKValueEntered, etsysWPAConfigUnicastCiphersEntry=etsysWPAConfigUnicastCiphersEntry, etsysWPAConfigGroupRekeyMethod=etsysWPAConfigGroupRekeyMethod, etsysWPAConfigUnicastCipherEnabled=etsysWPAConfigUnicastCipherEnabled, etsysWPAConfigAuthenticationSuitesTable=etsysWPAConfigAuthenticationSuitesTable, etsysWpaCompliances=etsysWpaCompliances, etsysWPAStatsTKIPCounterMeasuresInvoked=etsysWPAStatsTKIPCounterMeasuresInvoked, etsysWPAConfigOptionImplemented=etsysWPAConfigOptionImplemented, etsysWPAStatsTable=etsysWPAStatsTable, etsysWPAStatsVersion=etsysWPAStatsVersion, etsysWpaConformance=etsysWpaConformance, etsysWPAConfigEnabled=etsysWPAConfigEnabled, etsysWPAConfigUnicastCipherIndex=etsysWPAConfigUnicastCipherIndex, etsysWPAConfigIndex=etsysWPAConfigIndex, etsysWPAConfigMulticastCipher=etsysWPAConfigMulticastCipher, etsysWPAConfigPairwiseUpdateCount=etsysWPAConfigPairwiseUpdateCount, etsysWPAConfigGroupRekeyPackets=etsysWPAConfigGroupRekeyPackets)

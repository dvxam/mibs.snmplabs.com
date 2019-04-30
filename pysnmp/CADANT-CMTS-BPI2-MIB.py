#
# PySNMP MIB module CADANT-CMTS-BPI2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-BPI2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:26:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
cadSystem, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadSystem")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Counter64, NotificationType, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, ModuleIdentity, Unsigned32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Counter64", "NotificationType", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Integer32", "Counter32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
cadBpi2Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5))
cadBpi2Mib.setRevisions(('2014-07-30 00:00', '2006-12-18 00:00',))
if mibBuilder.loadTexts: cadBpi2Mib.setLastUpdated('201407300000Z')
if mibBuilder.loadTexts: cadBpi2Mib.setOrganization('Cadant Inc')
cadBpi2CmtsBaseTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1), )
if mibBuilder.loadTexts: cadBpi2CmtsBaseTable.setStatus('current')
cadBpi2CmtsBaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cadBpi2CmtsBaseEntry.setStatus('current')
cadBpi2CmtsDefaultAuthLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6048000)).clone(604800)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadBpi2CmtsDefaultAuthLifetime.setStatus('current')
cadBpi2CmtsDefaultTEKLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 604800)).clone(43200)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadBpi2CmtsDefaultTEKLifetime.setStatus('current')
cadBpi2CmtsDefaultSelfSignedManufCertTrust = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trusted", 1), ("untrusted", 2))).clone('untrusted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadBpi2CmtsDefaultSelfSignedManufCertTrust.setStatus('current')
cadBpi2CmtsCheckCertValidityPeriods = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadBpi2CmtsCheckCertValidityPeriods.setStatus('current')
cadBpi2CmtsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 2))
cadBpi2CmtsAES128Enable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 5, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadBpi2CmtsAES128Enable.setStatus('current')
mibBuilder.exportSymbols("CADANT-CMTS-BPI2-MIB", cadBpi2CmtsDefaultTEKLifetime=cadBpi2CmtsDefaultTEKLifetime, PYSNMP_MODULE_ID=cadBpi2Mib, cadBpi2CmtsDefaultSelfSignedManufCertTrust=cadBpi2CmtsDefaultSelfSignedManufCertTrust, cadBpi2CmtsAES128Enable=cadBpi2CmtsAES128Enable, cadBpi2CmtsBaseTable=cadBpi2CmtsBaseTable, cadBpi2CmtsBaseEntry=cadBpi2CmtsBaseEntry, cadBpi2Mib=cadBpi2Mib, cadBpi2CmtsDefaultAuthLifetime=cadBpi2CmtsDefaultAuthLifetime, cadBpi2CmtsConfig=cadBpi2CmtsConfig, cadBpi2CmtsCheckCertValidityPeriods=cadBpi2CmtsCheckCertValidityPeriods)
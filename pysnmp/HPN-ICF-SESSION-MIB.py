#
# PySNMP MIB module HPN-ICF-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-SESSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, Gauge32, Integer32, Counter64, Bits, IpAddress, TimeTicks, NotificationType, Unsigned32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Gauge32", "Integer32", "Counter64", "Bits", "IpAddress", "TimeTicks", "NotificationType", "Unsigned32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfSession = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149))
hpnicfSession.setRevisions(('2013-12-20 00:00',))
if mibBuilder.loadTexts: hpnicfSession.setLastUpdated('201312200000Z')
if mibBuilder.loadTexts: hpnicfSession.setOrganization('')
hpnicfSessionTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1))
hpnicfSessionStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1), )
if mibBuilder.loadTexts: hpnicfSessionStatTable.setStatus('current')
hpnicfSessionStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-SESSION-MIB", "hpnicfSessionStatChassis"), (0, "HPN-ICF-SESSION-MIB", "hpnicfSessionStatSlot"), (0, "HPN-ICF-SESSION-MIB", "hpnicfSessionStatCPUID"))
if mibBuilder.loadTexts: hpnicfSessionStatEntry.setStatus('current')
hpnicfSessionStatChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534)))
if mibBuilder.loadTexts: hpnicfSessionStatChassis.setStatus('current')
hpnicfSessionStatSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534)))
if mibBuilder.loadTexts: hpnicfSessionStatSlot.setStatus('current')
hpnicfSessionStatCPUID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: hpnicfSessionStatCPUID.setStatus('current')
hpnicfSessionStatCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSessionStatCount.setStatus('current')
hpnicfSessionStatCreateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSessionStatCreateRate.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-SESSION-MIB", hpnicfSessionStatSlot=hpnicfSessionStatSlot, hpnicfSessionStatCPUID=hpnicfSessionStatCPUID, hpnicfSessionStatChassis=hpnicfSessionStatChassis, hpnicfSessionTables=hpnicfSessionTables, hpnicfSessionStatCount=hpnicfSessionStatCount, hpnicfSessionStatEntry=hpnicfSessionStatEntry, hpnicfSession=hpnicfSession, hpnicfSessionStatTable=hpnicfSessionStatTable, PYSNMP_MODULE_ID=hpnicfSession, hpnicfSessionStatCreateRate=hpnicfSessionStatCreateRate)

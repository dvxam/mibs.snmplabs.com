#
# PySNMP MIB module BAY-STACK-ECMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-ECMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, iso, NotificationType, Integer32, ModuleIdentity, Counter64, TimeTicks, IpAddress, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "iso", "NotificationType", "Integer32", "ModuleIdentity", "Counter64", "TimeTicks", "IpAddress", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackEcmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 15))
bayStackEcmpMib.setRevisions(('2012-06-01 00:00', '2005-09-09 00:00',))
if mibBuilder.loadTexts: bayStackEcmpMib.setLastUpdated('201206010000Z')
if mibBuilder.loadTexts: bayStackEcmpMib.setOrganization('Nortel Networks')
bsEcmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 15, 0))
bsEcmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 15, 1))
bsEcmpScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 1))
bsEcmpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2), )
if mibBuilder.loadTexts: bsEcmpConfigTable.setStatus('current')
bsEcmpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-ECMP-MIB", "bsEcmpConfigRoutingProtocol"))
if mibBuilder.loadTexts: bsEcmpConfigEntry.setStatus('current')
bsEcmpConfigRoutingProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("static", 1), ("rip", 2), ("ospf", 3), ("bgp", 4))))
if mibBuilder.loadTexts: bsEcmpConfigRoutingProtocol.setStatus('current')
bsEcmpConfigMaxPath = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsEcmpConfigMaxPath.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-ECMP-MIB", bsEcmpScalars=bsEcmpScalars, bsEcmpObjects=bsEcmpObjects, bsEcmpConfigMaxPath=bsEcmpConfigMaxPath, bsEcmpConfigEntry=bsEcmpConfigEntry, bsEcmpConfigRoutingProtocol=bsEcmpConfigRoutingProtocol, bsEcmpNotifications=bsEcmpNotifications, PYSNMP_MODULE_ID=bayStackEcmpMib, bsEcmpConfigTable=bsEcmpConfigTable, bayStackEcmpMib=bayStackEcmpMib)

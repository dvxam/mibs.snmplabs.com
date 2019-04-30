#
# PySNMP MIB module TCAv1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TCAv1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, ObjectIdentity, TimeTicks, Bits, Gauge32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Unsigned32, iso, enterprises, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "ObjectIdentity", "TimeTicks", "Bits", "Gauge32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Unsigned32", "iso", "enterprises", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bellcore = MibIdentifier((1, 3, 6, 1, 4, 1, 148))
requirements = MibIdentifier((1, 3, 6, 1, 4, 1, 148, 1))
tcaMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 148, 1, 5))
tcaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 148, 1, 5, 1))
tcaTable = MibTable((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1), )
if mibBuilder.loadTexts: tcaTable.setStatus('mandatory')
tcaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1), ).setIndexNames((0, "TCAv1-MIB", "tcaIfIndex"), (0, "TCAv1-MIB", "tcaIndex"))
if mibBuilder.loadTexts: tcaEntry.setStatus('mandatory')
tcaIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaIfIndex.setStatus('mandatory')
tcaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaIndex.setStatus('mandatory')
tcaObject = MibTableColumn((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaObject.setStatus('mandatory')
tcaObjectDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaObjectDesc.setStatus('mandatory')
tcaThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaThreshold.setStatus('mandatory')
tcaSampleType = MibTableColumn((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("intervalAbsoluteValue", 1), ("intervalDeltaValue", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaSampleType.setStatus('mandatory')
tcaCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaCounts.setStatus('mandatory')
tcaTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcaTimeStamp.setStatus('mandatory')
tcaTrapEnabler = MibTableColumn((1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcaTrapEnabler.setStatus('mandatory')
tcaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 148, 1, 5, 2))
tcaGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 148, 1, 5, 2, 1))
tcaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 148, 1, 5, 2, 2))
tcaCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 148, 1, 5, 2, 2, 1))
tcaGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 148, 1, 5, 2, 1, 1))
mibBuilder.exportSymbols("TCAv1-MIB", tcaCompliance=tcaCompliance, tcaGroup=tcaGroup, tcaObjects=tcaObjects, tcaTimeStamp=tcaTimeStamp, tcaIfIndex=tcaIfIndex, requirements=requirements, tcaObject=tcaObject, tcaTrapEnabler=tcaTrapEnabler, tcaConformance=tcaConformance, tcaSampleType=tcaSampleType, tcaObjectDesc=tcaObjectDesc, tcaIndex=tcaIndex, tcaMIB=tcaMIB, bellcore=bellcore, tcaCompliances=tcaCompliances, tcaEntry=tcaEntry, tcaCounts=tcaCounts, tcaGroups=tcaGroups, tcaTable=tcaTable, tcaThreshold=tcaThreshold)
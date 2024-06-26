#
# PySNMP MIB module ZHONE-COM-CES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-CES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:40:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
atmfCESAtmVpi, atmfCESLocalAddr, atmfCESOperStatus, atmfCESConnType, atmfCESConfRowStatus, atmfCESBufMaxSize, atmfCESAtmVci, atmfCESPartialFill, atmfCESCas, atmfCESCdvRxT, atmfCESCbrIndex, atmfCESCbrService, atmfCESCbrClockMode, atmfCESConfEntry, atmfCESAtmIndex, atmfCESAdminStatus, atmfCESCellLossIntegrationPeriod = mibBuilder.importSymbols("ATMF-CES", "atmfCESAtmVpi", "atmfCESLocalAddr", "atmfCESOperStatus", "atmfCESConnType", "atmfCESConfRowStatus", "atmfCESBufMaxSize", "atmfCESAtmVci", "atmfCESPartialFill", "atmfCESCas", "atmfCESCdvRxT", "atmfCESCbrIndex", "atmfCESCbrService", "atmfCESCbrClockMode", "atmfCESConfEntry", "atmfCESAtmIndex", "atmfCESAdminStatus", "atmfCESCellLossIntegrationPeriod")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, NotificationType, Bits, TimeTicks, Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, Integer32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Bits", "TimeTicks", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "Integer32", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhoneCes, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneCes", "zhoneModules")
comCesExtension = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 108))
comCesExtension.setRevisions(('2005-04-13 12:04', '2004-08-16 12:00',))
if mibBuilder.loadTexts: comCesExtension.setLastUpdated('200508131230Z')
if mibBuilder.loadTexts: comCesExtension.setOrganization('Zhone Technologies, Inc.')
zhoneAtmfCESConfExtTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 10, 1), )
if mibBuilder.loadTexts: zhoneAtmfCESConfExtTable.setStatus('current')
zhoneAtmfCESConfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1), )
atmfCESConfEntry.registerAugmentions(("ZHONE-COM-CES-MIB", "zhoneAtmfCESConfExtEntry"))
zhoneAtmfCESConfExtEntry.setIndexNames(*atmfCESConfEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneAtmfCESConfExtEntry.setStatus('current')
zhoneAtmfCESDs0Bundle = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 1), Bits().clone(namedValues=NamedValues(("ts0", 0), ("ts1", 1), ("ts2", 2), ("ts3", 3), ("ts4", 4), ("ts5", 5), ("ts6", 6), ("ts7", 7), ("ts8", 8), ("ts9", 9), ("ts10", 10), ("ts11", 11), ("ts12", 12), ("ts13", 13), ("ts14", 14), ("ts15", 15), ("ts16", 16), ("ts17", 17), ("ts18", 18), ("ts19", 19), ("ts20", 20), ("ts21", 21), ("ts22", 22), ("ts23", 23), ("ts24", 24), ("ts25", 25), ("ts26", 26), ("ts27", 27), ("ts28", 28), ("ts29", 29), ("ts30", 30), ("ts31", 31)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneAtmfCESDs0Bundle.setStatus('current')
zhoneAtmfCESConfExtAtmfCESSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneAtmfCESConfExtAtmfCESSrcIpAddr.setStatus('current')
zhoneAtmfCESConfExtAtmfCESDstIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneAtmfCESConfExtAtmfCESDstIpAddr.setStatus('current')
zhoneAtmfCESConfExtAtmfCESSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneAtmfCESConfExtAtmfCESSrcPort.setStatus('current')
zhoneAtmfCESConfExtAtmfCESDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 10, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneAtmfCESConfExtAtmfCESDstPort.setStatus('current')
zhoneAtmfCESGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 4, 10, 2)).setObjects(("ZHONE-COM-CES-MIB", "zhoneAtmfCESDs0Bundle"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhoneAtmfCESGroup = zhoneAtmfCESGroup.setStatus('current')
mibBuilder.exportSymbols("ZHONE-COM-CES-MIB", zhoneAtmfCESConfExtTable=zhoneAtmfCESConfExtTable, zhoneAtmfCESConfExtAtmfCESDstPort=zhoneAtmfCESConfExtAtmfCESDstPort, zhoneAtmfCESConfExtAtmfCESSrcIpAddr=zhoneAtmfCESConfExtAtmfCESSrcIpAddr, zhoneAtmfCESConfExtAtmfCESDstIpAddr=zhoneAtmfCESConfExtAtmfCESDstIpAddr, PYSNMP_MODULE_ID=comCesExtension, comCesExtension=comCesExtension, zhoneAtmfCESDs0Bundle=zhoneAtmfCESDs0Bundle, zhoneAtmfCESConfExtEntry=zhoneAtmfCESConfExtEntry, zhoneAtmfCESGroup=zhoneAtmfCESGroup, zhoneAtmfCESConfExtAtmfCESSrcPort=zhoneAtmfCESConfExtAtmfCESSrcPort)

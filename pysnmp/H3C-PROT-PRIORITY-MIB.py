#
# PySNMP MIB module H3C-PROT-PRIORITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-PROT-PRIORITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:10:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, iso, ObjectIdentity, IpAddress, Counter32, MibIdentifier, NotificationType, Unsigned32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "iso", "ObjectIdentity", "IpAddress", "Counter32", "MibIdentifier", "NotificationType", "Unsigned32", "Bits", "ModuleIdentity")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
h3cProtocolPriority = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37))
h3cProtocolPriority.setRevisions(('2005-01-17 16:33',))
if mibBuilder.loadTexts: h3cProtocolPriority.setLastUpdated('200501171633Z')
if mibBuilder.loadTexts: h3cProtocolPriority.setOrganization('Huawei 3Com Technologies Co., Ltd.')
h3cProtocolPriorityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1))
h3cPPri = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1))
h3cProtocolPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1), )
if mibBuilder.loadTexts: h3cProtocolPriorityTable.setStatus('current')
h3cProtocolPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1), ).setIndexNames((0, "H3C-PROT-PRIORITY-MIB", "h3cPPriProtocolType"))
if mibBuilder.loadTexts: h3cProtocolPriorityEntry.setStatus('current')
h3cPPriProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ospf", 1), ("telnet", 2), ("snmp", 3), ("icmp", 4), ("bgp", 5), ("ldp", 6))))
if mibBuilder.loadTexts: h3cPPriProtocolType.setStatus('current')
h3cPPriPriorityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipPrecedence", 1), ("dscp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriPriorityType.setStatus('current')
h3cPPriPriorityVlaue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriPriorityVlaue.setStatus('current')
h3cPPriRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriRowStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-PROT-PRIORITY-MIB", h3cProtocolPriority=h3cProtocolPriority, h3cPPriPriorityType=h3cPPriPriorityType, h3cPPriRowStatus=h3cPPriRowStatus, h3cProtocolPriorityEntry=h3cProtocolPriorityEntry, h3cProtocolPriorityObjects=h3cProtocolPriorityObjects, PYSNMP_MODULE_ID=h3cProtocolPriority, h3cPPri=h3cPPri, h3cPPriProtocolType=h3cPPriProtocolType, h3cProtocolPriorityTable=h3cProtocolPriorityTable, h3cPPriPriorityVlaue=h3cPPriPriorityVlaue)

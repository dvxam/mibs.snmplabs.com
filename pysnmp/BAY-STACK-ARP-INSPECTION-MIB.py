#
# PySNMP MIB module BAY-STACK-ARP-INSPECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-ARP-INSPECTION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, Unsigned32, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Gauge32, Counter64, NotificationType, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Gauge32", "Counter64", "NotificationType", "Integer32", "TimeTicks")
MacAddress, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackArpInspectionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 18))
bayStackArpInspectionMib.setRevisions(('2013-10-11 00:00', '2013-07-05 00:00', '2008-10-30 00:00', '2006-06-23 00:00',))
if mibBuilder.loadTexts: bayStackArpInspectionMib.setLastUpdated('201310110000Z')
if mibBuilder.loadTexts: bayStackArpInspectionMib.setOrganization('Nortel Ltd.')
bsArpInspectionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 18, 0))
bsArpInspectionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 18, 1))
bsArpInspectionVlanTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 1), )
if mibBuilder.loadTexts: bsArpInspectionVlanTable.setStatus('current')
bsArpInspectionVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 1, 1), ).setIndexNames((0, "BAY-STACK-ARP-INSPECTION-MIB", "bsArpInspectionVlanId"))
if mibBuilder.loadTexts: bsArpInspectionVlanEntry.setStatus('current')
bsArpInspectionVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts: bsArpInspectionVlanId.setStatus('current')
bsArpInspectionVlanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsArpInspectionVlanEnabled.setStatus('current')
bsArpInspectionIfTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 2), )
if mibBuilder.loadTexts: bsArpInspectionIfTable.setStatus('current')
bsArpInspectionIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-ARP-INSPECTION-MIB", "bsArpInspectionIfIndex"))
if mibBuilder.loadTexts: bsArpInspectionIfEntry.setStatus('current')
bsArpInspectionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsArpInspectionIfIndex.setStatus('current')
bsArpInspectionIfTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsArpInspectionIfTrusted.setStatus('current')
bsArpInspectionNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 3))
bsArpInspectionNotificationSourceMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 3, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsArpInspectionNotificationSourceMACAddr.setStatus('current')
bsaiArpPacketDroppedOnUntrustedPort = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 18, 0, 1)).setObjects(("BAY-STACK-ARP-INSPECTION-MIB", "bsArpInspectionIfTrusted"), ("BAY-STACK-ARP-INSPECTION-MIB", "bsArpInspectionNotificationSourceMACAddr"))
if mibBuilder.loadTexts: bsaiArpPacketDroppedOnUntrustedPort.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-ARP-INSPECTION-MIB", bsArpInspectionIfEntry=bsArpInspectionIfEntry, bsArpInspectionVlanTable=bsArpInspectionVlanTable, bsArpInspectionObjects=bsArpInspectionObjects, bayStackArpInspectionMib=bayStackArpInspectionMib, bsArpInspectionNotifications=bsArpInspectionNotifications, PYSNMP_MODULE_ID=bayStackArpInspectionMib, bsArpInspectionVlanEnabled=bsArpInspectionVlanEnabled, bsArpInspectionIfTable=bsArpInspectionIfTable, bsArpInspectionNotificationSourceMACAddr=bsArpInspectionNotificationSourceMACAddr, bsArpInspectionIfIndex=bsArpInspectionIfIndex, bsArpInspectionIfTrusted=bsArpInspectionIfTrusted, bsArpInspectionNotificationObjects=bsArpInspectionNotificationObjects, bsArpInspectionVlanId=bsArpInspectionVlanId, bsArpInspectionVlanEntry=bsArpInspectionVlanEntry, bsaiArpPacketDroppedOnUntrustedPort=bsaiArpPacketDroppedOnUntrustedPort)

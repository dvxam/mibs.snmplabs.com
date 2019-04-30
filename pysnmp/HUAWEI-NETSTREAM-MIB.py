#
# PySNMP MIB module HUAWEI-NETSTREAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-NETSTREAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:35:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, NotificationType, Bits, Gauge32, ObjectIdentity, MibIdentifier, Unsigned32, NotificationGroup, Bits, ObjectGroup, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter32, iso, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "NotificationType", "Bits", "Gauge32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "NotificationGroup", "Bits", "ObjectGroup", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter32", "iso", "ModuleCompliance")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
hwNetStreamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110))
if mibBuilder.loadTexts: hwNetStreamMIB.setLastUpdated('200510250000Z')
if mibBuilder.loadTexts: hwNetStreamMIB.setOrganization('Huawei Technologies co.,Ltd.')
hwNetStreamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1))
hwNetStreamNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2))
hwNetStreamlastchangedtime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNetStreamlastchangedtime.setStatus('current')
hwNetStreamIfIndexTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 2), )
if mibBuilder.loadTexts: hwNetStreamIfIndexTable.setStatus('current')
hwNetStreamIfIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 2, 1), ).setIndexNames((0, "HUAWEI-NETSTREAM-MIB", "hwNetStream16BitIndex"))
if mibBuilder.loadTexts: hwNetStreamIfIndexEntry.setStatus('current')
hwNetStream16BitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNetStream16BitIndex.setStatus('current')
hwifNet32BitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwifNet32BitIndex.setStatus('current')
hwNetStreamTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2, 0))
hwNetStreamIndexStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2, 0, 1))
if mibBuilder.loadTexts: hwNetStreamIndexStatusChanged.setStatus('current')
hwNetStreamIndexUsedUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2, 0, 2))
if mibBuilder.loadTexts: hwNetStreamIndexUsedUp.setStatus('current')
hwNetStreamSessionFull = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 2, 0, 3))
if mibBuilder.loadTexts: hwNetStreamSessionFull.setStatus('current')
hwNetstreamConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3))
hwNetstreamGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 1))
hwNetstreamCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 2))
hwNetstreamCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 2, 1)).setObjects(("HUAWEI-NETSTREAM-MIB", "hwNetstreamExtGroup"), ("HUAWEI-NETSTREAM-MIB", "hwNotificationExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwNetstreamCompliance = hwNetstreamCompliance.setStatus('current')
hwNetstreamExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 1, 2)).setObjects(("HUAWEI-NETSTREAM-MIB", "hwNetStreamlastchangedtime"), ("HUAWEI-NETSTREAM-MIB", "hwNetStream16BitIndex"), ("HUAWEI-NETSTREAM-MIB", "hwifNet32BitIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwNetstreamExtGroup = hwNetstreamExtGroup.setStatus('current')
hwNotificationExtGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 110, 3, 1, 3)).setObjects(("HUAWEI-NETSTREAM-MIB", "hwNetStreamIndexUsedUp"), ("HUAWEI-NETSTREAM-MIB", "hwNetStreamIndexStatusChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwNotificationExtGroup = hwNotificationExtGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-NETSTREAM-MIB", hwNetStreamObjects=hwNetStreamObjects, hwNetStreamNotifications=hwNetStreamNotifications, hwNetstreamConformance=hwNetstreamConformance, hwifNet32BitIndex=hwifNet32BitIndex, hwNetstreamExtGroup=hwNetstreamExtGroup, hwNetStreamSessionFull=hwNetStreamSessionFull, hwNetstreamCompliance=hwNetstreamCompliance, hwNetStreamIfIndexTable=hwNetStreamIfIndexTable, hwNotificationExtGroup=hwNotificationExtGroup, hwNetStreamMIB=hwNetStreamMIB, hwNetStreamIfIndexEntry=hwNetStreamIfIndexEntry, hwNetStream16BitIndex=hwNetStream16BitIndex, hwNetstreamCompliances=hwNetstreamCompliances, hwNetStreamTrapPrefix=hwNetStreamTrapPrefix, hwNetstreamGroups=hwNetstreamGroups, hwNetStreamIndexStatusChanged=hwNetStreamIndexStatusChanged, hwNetStreamIndexUsedUp=hwNetStreamIndexUsedUp, hwNetStreamlastchangedtime=hwNetStreamlastchangedtime, PYSNMP_MODULE_ID=hwNetStreamMIB)
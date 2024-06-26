#
# PySNMP MIB module RAPID-SYSTEM-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAPID-SYSTEM-CONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, IpAddress, MibIdentifier, Counter64, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, iso, ObjectIdentity, NotificationType, ModuleIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "iso", "ObjectIdentity", "NotificationType", "ModuleIdentity", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsSystemConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 2))
rsSystemConfigMIB.setRevisions(('1999-06-26 12:00', '2002-11-01 12:00', '2004-06-01 12:00',))
if mibBuilder.loadTexts: rsSystemConfigMIB.setLastUpdated('9906261200Z')
if mibBuilder.loadTexts: rsSystemConfigMIB.setOrganization('WatchGuard Technologies, Inc.')
rsSysTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 3))
if mibBuilder.loadTexts: rsSysTraps.setStatus('current')
rsSysTrapObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 4))
if mibBuilder.loadTexts: rsSysTrapObjects.setStatus('current')
rsSysTrapControl = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 5))
if mibBuilder.loadTexts: rsSysTrapControl.setStatus('current')
rsAlarmId = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmId.setStatus('current')
rsAlarmLabel = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmLabel.setStatus('current')
rsAlarmTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmTime.setStatus('current')
rsAlarmLevel = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 3, 2, 1))).clone(namedValues=NamedValues(("normal", 4), ("warning", 3), ("error", 2), ("critical", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmLevel.setStatus('current')
rsAlarmHostname = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmHostname.setStatus('current')
rsAlarmMsg = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 4, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmMsg.setStatus('current')
rsAlarmTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4355, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAlarmTrapEnable.setStatus('current')
rsSysTrapsPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0))
if mibBuilder.loadTexts: rsSysTrapsPrefix.setStatus('current')
rsAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 1)).setObjects(("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmId"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmLabel"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmTime"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmLevel"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmHostname"), ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmMsg"))
if mibBuilder.loadTexts: rsAlarmTrap.setStatus('current')
rsSnmpStart = NotificationType((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 2))
if mibBuilder.loadTexts: rsSnmpStart.setStatus('current')
rsSnmpShutdown = NotificationType((1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 3))
if mibBuilder.loadTexts: rsSnmpShutdown.setStatus('current')
mibBuilder.exportSymbols("RAPID-SYSTEM-CONFIG-MIB", PYSNMP_MODULE_ID=rsSystemConfigMIB, rsSysTrapControl=rsSysTrapControl, rsSysTrapsPrefix=rsSysTrapsPrefix, rsSystemConfigMIB=rsSystemConfigMIB, rsAlarmId=rsAlarmId, rsSnmpShutdown=rsSnmpShutdown, rsSysTraps=rsSysTraps, rsAlarmTrapEnable=rsAlarmTrapEnable, rsSysTrapObjects=rsSysTrapObjects, rsAlarmLevel=rsAlarmLevel, rsAlarmLabel=rsAlarmLabel, rsSnmpStart=rsSnmpStart, rsAlarmTrap=rsAlarmTrap, rsAlarmHostname=rsAlarmHostname, rsAlarmMsg=rsAlarmMsg, rsAlarmTime=rsAlarmTime)

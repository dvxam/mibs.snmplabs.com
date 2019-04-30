#
# PySNMP MIB module GWMONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GWMONITOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, Unsigned32, NotificationType, MibIdentifier, TimeTicks, Counter64, Bits, Integer32, ObjectIdentity, ModuleIdentity, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Unsigned32", "NotificationType", "MibIdentifier", "TimeTicks", "Counter64", "Bits", "Integer32", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
gwmontr = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 40))
gwmonserver = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 40, 5))
gwmonTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1))
gwmonTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2))
gwmonTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: gwmonTrapTime.setStatus('mandatory')
gwmonAgentName = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: gwmonAgentName.setStatus('mandatory')
gwmonAgentType = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: gwmonAgentType.setStatus('mandatory')
gwmonStatus = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: gwmonStatus.setStatus('mandatory')
gwmonStatusDuration = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 5), TimeTicks())
if mibBuilder.loadTexts: gwmonStatusDuration.setStatus('mandatory')
gwmonThreshold = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: gwmonThreshold.setStatus('mandatory')
gwmonThresholdValues = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: gwmonThresholdValues.setStatus('mandatory')
gwmonThresholdSeverity = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: gwmonThresholdSeverity.setStatus('mandatory')
gwmonServerName = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: gwmonServerName.setStatus('mandatory')
gwmonServerIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: gwmonServerIPAddress.setStatus('mandatory')
gwmonThresholdExceededTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2) + (0,1)).setObjects(("GWMONITOR-MIB", "gwmonTrapTime"), ("GWMONITOR-MIB", "gwmonAgentType"), ("GWMONITOR-MIB", "gwmonAgentName"), ("GWMONITOR-MIB", "gwmonServerName"), ("GWMONITOR-MIB", "gwmonServerIPAddress"), ("GWMONITOR-MIB", "gwmonThresholdValues"), ("GWMONITOR-MIB", "gwmonThresholdSeverity"))
gwmonThresholdRecoveredTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2) + (0,2)).setObjects(("GWMONITOR-MIB", "gwmonTrapTime"), ("GWMONITOR-MIB", "gwmonAgentType"), ("GWMONITOR-MIB", "gwmonAgentName"), ("GWMONITOR-MIB", "gwmonServerName"), ("GWMONITOR-MIB", "gwmonServerIPAddress"))
gwmonAgentDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2) + (0,3)).setObjects(("GWMONITOR-MIB", "gwmonTrapTime"), ("GWMONITOR-MIB", "gwmonAgentType"), ("GWMONITOR-MIB", "gwmonAgentName"), ("GWMONITOR-MIB", "gwmonServerName"), ("GWMONITOR-MIB", "gwmonServerIPAddress"))
gwmonAgentUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2) + (0,4)).setObjects(("GWMONITOR-MIB", "gwmonTrapTime"), ("GWMONITOR-MIB", "gwmonAgentType"), ("GWMONITOR-MIB", "gwmonAgentName"), ("GWMONITOR-MIB", "gwmonServerName"), ("GWMONITOR-MIB", "gwmonServerIPAddress"))
gwmonTestTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2) + (0,5)).setObjects(("GWMONITOR-MIB", "gwmonTrapTime"))
gwmonPeriodicTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2) + (0,6)).setObjects(("GWMONITOR-MIB", "gwmonTrapTime"))
mibBuilder.exportSymbols("GWMONITOR-MIB", gwmontr=gwmontr, gwmonAgentUpTrap=gwmonAgentUpTrap, gwmonTraps=gwmonTraps, gwmonTrapTime=gwmonTrapTime, gwmonAgentType=gwmonAgentType, gwmonStatusDuration=gwmonStatusDuration, gwmonServerName=gwmonServerName, gwmonTestTrap=gwmonTestTrap, gwmonServerIPAddress=gwmonServerIPAddress, gwmonAgentName=gwmonAgentName, gwmonThreshold=gwmonThreshold, mibDoc=mibDoc, gwmonPeriodicTrap=gwmonPeriodicTrap, gwmonThresholdSeverity=gwmonThresholdSeverity, gwmonserver=gwmonserver, gwmonAgentDownTrap=gwmonAgentDownTrap, novell=novell, gwmonThresholdRecoveredTrap=gwmonThresholdRecoveredTrap, gwmonTrapInfo=gwmonTrapInfo, gwmonThresholdExceededTrap=gwmonThresholdExceededTrap, gwmonStatus=gwmonStatus, gwmonThresholdValues=gwmonThresholdValues)

#
# PySNMP MIB module H323-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H323-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
gwID, timeOccurred, reason, registrationStatus, comment, gwType, csID, port, percent, csType, gwIP, moduleID, code = mibBuilder.importSymbols("AGGREGATED-EXT-MIB", "gwID", "timeOccurred", "reason", "registrationStatus", "comment", "gwType", "csID", "port", "percent", "csType", "gwIP", "moduleID", "code")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, enterprises, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectName, Counter64, Unsigned32, snmpModules, ObjectIdentity, MibIdentifier, Gauge32, IpAddress, Counter32, NotificationType, ModuleIdentity, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectName", "Counter64", "Unsigned32", "snmpModules", "ObjectIdentity", "MibIdentifier", "Gauge32", "IpAddress", "Counter32", "NotificationType", "ModuleIdentity", "Bits", "Integer32")
TestAndIncr, DisplayString, RowStatus, TruthValue, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "DisplayString", "RowStatus", "TruthValue", "TimeStamp", "TextualConvention")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
h323DeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3))
h323Traps = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0))
if mibBuilder.loadTexts: h323Traps.setLastUpdated('240701')
if mibBuilder.loadTexts: h323Traps.setOrganization('Lucent Technologies')
h323CSConnectionStatus = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 0)).setObjects(("AGGREGATED-EXT-MIB", "timeOccurred"), ("AGGREGATED-EXT-MIB", "code"), ("AGGREGATED-EXT-MIB", "csID"), ("AGGREGATED-EXT-MIB", "csType"), ("AGGREGATED-EXT-MIB", "registrationStatus"), ("AGGREGATED-EXT-MIB", "reason"), ("AGGREGATED-EXT-MIB", "comment"))
if mibBuilder.loadTexts: h323CSConnectionStatus.setStatus('current')
h323GatewayUtilization = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 1)).setObjects(("AGGREGATED-EXT-MIB", "timeOccurred"), ("AGGREGATED-EXT-MIB", "code"), ("AGGREGATED-EXT-MIB", "gwID"), ("AGGREGATED-EXT-MIB", "moduleID"), ("AGGREGATED-EXT-MIB", "percent"), ("AGGREGATED-EXT-MIB", "comment"))
if mibBuilder.loadTexts: h323GatewayUtilization.setStatus('current')
h323DSError = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 2)).setObjects(("AGGREGATED-EXT-MIB", "timeOccurred"), ("AGGREGATED-EXT-MIB", "code"), ("AGGREGATED-EXT-MIB", "reason"), ("AGGREGATED-EXT-MIB", "comment"))
if mibBuilder.loadTexts: h323DSError.setStatus('current')
h323UnreachableGateway = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 3)).setObjects(("AGGREGATED-EXT-MIB", "timeOccurred"), ("AGGREGATED-EXT-MIB", "code"), ("AGGREGATED-EXT-MIB", "gwID"), ("AGGREGATED-EXT-MIB", "gwType"), ("AGGREGATED-EXT-MIB", "gwIP"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "comment"))
if mibBuilder.loadTexts: h323UnreachableGateway.setStatus('current')
h323CommandFailed = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 4)).setObjects(("AGGREGATED-EXT-MIB", "timeOccurred"), ("AGGREGATED-EXT-MIB", "code"), ("AGGREGATED-EXT-MIB", "reason"), ("AGGREGATED-EXT-MIB", "comment"))
if mibBuilder.loadTexts: h323CommandFailed.setStatus('current')
mibBuilder.exportSymbols("H323-TRAP-MIB", h323CSConnectionStatus=h323CSConnectionStatus, h323UnreachableGateway=h323UnreachableGateway, h323CommandFailed=h323CommandFailed, softSwitch=softSwitch, products=products, h323Traps=h323Traps, PYSNMP_MODULE_ID=h323Traps, h323GatewayUtilization=h323GatewayUtilization, h323DSError=h323DSError, h323DeviceServer=h323DeviceServer, lucent=lucent)
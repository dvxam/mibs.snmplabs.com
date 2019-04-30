#
# PySNMP MIB module RUCKUS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ruckusCommonSystemModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonSystemModule")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Gauge32, MibIdentifier, ObjectIdentity, TimeTicks, Unsigned32, Counter64, Counter32, IpAddress, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Gauge32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Unsigned32", "Counter64", "Counter32", "IpAddress", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ruckusSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1))
if mibBuilder.loadTexts: ruckusSystemMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusSystemMIB.setOrganization('Ruckus Wireless, Inc.')
ruckusSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1))
ruckusSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 1))
ruckusSystemServices = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2))
ruckusSystemCommands = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3))
ruckusSystemEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 2))
ruckusSystemCPUUtil = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSystemCPUUtil.setStatus('current')
ruckusSystemMemoryUtil = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSystemMemoryUtil.setStatus('current')
ruckusSystemHTTP = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 1))
ruckusSystemHTTPS = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 2))
ruckusSystemTelnet = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 3))
ruckusSystemSSH = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 4))
ruckusSystemBonjour = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 5))
ruckusSystemSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6))
ruckusSystemNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7))
ruckusSystemFlexMaster = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 8))
ruckusSystemHTTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemHTTPStatus.setStatus('current')
ruckusSystemHTTPSStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemHTTPSStatus.setStatus('current')
ruckusSystemTelnetStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 3, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemTelnetStatus.setStatus('current')
ruckusSystemSSHStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 4, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSSHStatus.setStatus('current')
ruckusSystemBonjourStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 5, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemBonjourStatus.setStatus('current')
ruckusSystemSyslogStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSyslogStatus.setStatus('current')
ruckusSystemSyslogServerIP = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSyslogServerIP.setStatus('current')
ruckusSystemSyslogServerPort = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSyslogServerPort.setStatus('current')
ruckusSystemNTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 1), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSystemNTPStatus.setStatus('current')
ruckusSystemNTPGMTTime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSystemNTPGMTTime.setStatus('current')
ruckusSystemNTPActiveServer = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemNTPActiveServer.setStatus('current')
ruckusSystemNTPUpdate = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemNTPUpdate.setStatus('current')
ruckusSystemFlexMasterURL = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 8, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemFlexMasterURL.setStatus('current')
ruckusSystemReboot = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemReboot.setStatus('current')
ruckusSystemSetFactory = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSetFactory.setStatus('current')
ruckusSystemDHCPRenew = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemDHCPRenew.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-SYSTEM-MIB", ruckusSystemReboot=ruckusSystemReboot, ruckusSystemServices=ruckusSystemServices, ruckusSystemNTPActiveServer=ruckusSystemNTPActiveServer, ruckusSystemDHCPRenew=ruckusSystemDHCPRenew, ruckusSystemHTTP=ruckusSystemHTTP, ruckusSystemMemoryUtil=ruckusSystemMemoryUtil, ruckusSystemNTPStatus=ruckusSystemNTPStatus, ruckusSystemEvents=ruckusSystemEvents, ruckusSystemObjects=ruckusSystemObjects, ruckusSystemCPUUtil=ruckusSystemCPUUtil, ruckusSystemBonjourStatus=ruckusSystemBonjourStatus, ruckusSystemSyslogStatus=ruckusSystemSyslogStatus, ruckusSystemSSHStatus=ruckusSystemSSHStatus, ruckusSystemNTPGMTTime=ruckusSystemNTPGMTTime, ruckusSystemHTTPS=ruckusSystemHTTPS, ruckusSystemSyslogServerIP=ruckusSystemSyslogServerIP, ruckusSystemBonjour=ruckusSystemBonjour, ruckusSystemHTTPStatus=ruckusSystemHTTPStatus, ruckusSystemMIB=ruckusSystemMIB, ruckusSystemInfo=ruckusSystemInfo, ruckusSystemFlexMasterURL=ruckusSystemFlexMasterURL, ruckusSystemCommands=ruckusSystemCommands, ruckusSystemSyslog=ruckusSystemSyslog, ruckusSystemSetFactory=ruckusSystemSetFactory, ruckusSystemHTTPSStatus=ruckusSystemHTTPSStatus, ruckusSystemSSH=ruckusSystemSSH, ruckusSystemTelnet=ruckusSystemTelnet, ruckusSystemNTP=ruckusSystemNTP, ruckusSystemTelnetStatus=ruckusSystemTelnetStatus, PYSNMP_MODULE_ID=ruckusSystemMIB, ruckusSystemNTPUpdate=ruckusSystemNTPUpdate, ruckusSystemFlexMaster=ruckusSystemFlexMaster, ruckusSystemSyslogServerPort=ruckusSystemSyslogServerPort)
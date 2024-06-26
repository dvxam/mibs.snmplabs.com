#
# PySNMP MIB module RDN-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
riverdelta, = mibBuilder.importSymbols("RDN-MIB", "riverdelta")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Integer32, Counter64, Unsigned32, Counter32, TimeTicks, MibIdentifier, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Integer32", "Counter64", "Unsigned32", "Counter32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rdnSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 3))
rdnSyslog.setRevisions(('2008-08-08 00:00', '2004-01-23 00:00', '2003-11-05 00:00', '2003-01-30 00:00', '2000-06-14 00:00', '2000-06-08 00:00', '2000-05-23 00:00', '2000-05-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rdnSyslog.setRevisionsDescriptions(('Removed Compilier Warning by changing rdnSyslogServerTableEntry to rdnSyslogServerEntry.Added Copyright Statement into MIB modules description.', 'Updated the definition of rdnSyslogTrapSeverity object.', 'Updated the CONTACT-INFO.', 'Obsolete syslogRateLimitAutoRestart. Can now use docsDevEvThrottleAdminStatus', 'Added variable syslogRateLimitAutoRestart to allow turning on/off syslog rate-limit auto-restart.', 'Added syslogMessageTable.', 'Changed import of the riverdelta chassis mib to just the riverdelta definition mib.', 'Initial creation.',))
if mibBuilder.loadTexts: rdnSyslog.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnSyslog.setOrganization('Motorola')
if mibBuilder.loadTexts: rdnSyslog.setContactInfo('Motorola Customer Service 101 Tournament Drive Horsham, PA 19044 US Tel: +1 888 944 4357 Int Tel: +1 215 323 0044 Fax: +1 215 323 1502 Email: CPSSupport@Motorola.com')
if mibBuilder.loadTexts: rdnSyslog.setDescription('MIB module for Motorola syslog. Copyright (C) 2000, 2008 by Motorola, Inc. All rights reserved.')
rdnSyslogSize = MibScalar((1, 3, 6, 1, 4, 1, 4981, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnSyslogSize.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogSize.setDescription('Current size in bytes of the syslog file.')
rdnSyslogMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 4981, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4096, 5242880)).clone(4096)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnSyslogMaxSize.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogMaxSize.setDescription('Maximum size in bytes of the syslog file.')
rdnSyslogServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 4981, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnSyslogServerEnable.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogServerEnable.setDescription('Enable or disable logging to remote syslog servers.')
rdnSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 4981, 3, 4), )
if mibBuilder.loadTexts: rdnSyslogServerTable.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogServerTable.setDescription('Table of remote syslog servers, of which there can be at most 3 entries.')
rdnSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4981, 3, 4, 1), ).setIndexNames((0, "RDN-SYSLOG-MIB", "rdnSyslogServerIndex"))
if mibBuilder.loadTexts: rdnSyslogServerEntry.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogServerEntry.setDescription('syslog table entry.')
rdnSyslogServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 3, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: rdnSyslogServerIndex.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogServerIndex.setDescription('Index into the remote syslog server table.')
rdnSyslogServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 3, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnSyslogServerAddress.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogServerAddress.setDescription('The IP address of this syslog server.')
rdnSyslogServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnSyslogServerStatus.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogServerStatus.setDescription('Status of remote syslog server. Always enabled; set to disable to delete a syslog server from the syslogServerTable. Setting this to disabled will remove this entry from the table.')
rdnSyslogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4981, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disable", 0), ("informational", 1), ("notifications", 2), ("warnings", 3), ("errors", 4), ("critical", 5), ("alerts", 6), ("emergencies", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnSyslogSeverity.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogSeverity.setDescription('Severity of syslog messages reported/sent to a remote syslog server.')
rdnSyslogConsoleSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4981, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disable", 0), ("informational", 1), ("notifications", 2), ("warnings", 3), ("errors", 4), ("critical", 5), ("alerts", 6), ("emergencies", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnSyslogConsoleSeverity.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogConsoleSeverity.setDescription('Severity of syslog messages reported/sent to a console.')
rdnSyslogClear = MibScalar((1, 3, 6, 1, 4, 1, 4981, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnSyslogClear.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogClear.setDescription('Indicates whether syslog file contains syslog messages. This value is FALSE if syslog contains syslog messages, TRUE otherwise. Set to TRUE to clear all messages from the syslog file.')
rdnSyslogTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4981, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disable", 0), ("informational", 1), ("notifications", 2), ("warnings", 3), ("errors", 4), ("critical", 5), ("alerts", 6), ("emergencies", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnSyslogTrapSeverity.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogTrapSeverity.setDescription('SNMP trap severity level for which a syslog message severity level equal to or above will generate an SNMP trap. Set to disable to turn off generation of any traps.')
rdnSyslogMessageTable = MibTable((1, 3, 6, 1, 4, 1, 4981, 3, 9), )
if mibBuilder.loadTexts: rdnSyslogMessageTable.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogMessageTable.setDescription('Table of the latest syslog message strings.')
rdnSyslogMessageTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4981, 3, 9, 1), ).setIndexNames((0, "RDN-SYSLOG-MIB", "rdnSyslogMessageIndex"))
if mibBuilder.loadTexts: rdnSyslogMessageTableEntry.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogMessageTableEntry.setDescription('syslog message table entry.')
rdnSyslogMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 3, 9, 1, 1), Integer32())
if mibBuilder.loadTexts: rdnSyslogMessageIndex.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogMessageIndex.setDescription('Index into the syslog message table.')
rdnSyslogMessageString = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 3, 9, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdnSyslogMessageString.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogMessageString.setDescription('Actual message string of entry in syslog message table.')
rdnSyslogRateLimitAutoRestart = MibScalar((1, 3, 6, 1, 4, 1, 4981, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnSyslogRateLimitAutoRestart.setStatus('obsolete')
if mibBuilder.loadTexts: rdnSyslogRateLimitAutoRestart.setDescription('Enable or disable rate-limit auto-restart on logging of syslog messages.')
rdnSyslogMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 3, 0))
rdnSyslogTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 3, 0, 0))
rdnSyslogSeverityTrap = NotificationType((1, 3, 6, 1, 4, 1, 4981, 3, 0, 0, 1)).setObjects(("RDN-SYSLOG-MIB", "rdnSyslogTrapSeverity"))
if mibBuilder.loadTexts: rdnSyslogSeverityTrap.setStatus('current')
if mibBuilder.loadTexts: rdnSyslogSeverityTrap.setDescription('A syslogSeverityTrap trap signifies that the system logger has received a syslog message with its own severity level greater than or equal to the severity level of syslog MIB Object syslogTrapSeverity.')
mibBuilder.exportSymbols("RDN-SYSLOG-MIB", rdnSyslogServerIndex=rdnSyslogServerIndex, rdnSyslogSeverityTrap=rdnSyslogSeverityTrap, rdnSyslogSize=rdnSyslogSize, rdnSyslogServerStatus=rdnSyslogServerStatus, PYSNMP_MODULE_ID=rdnSyslog, rdnSyslogServerEnable=rdnSyslogServerEnable, rdnSyslogMessageString=rdnSyslogMessageString, rdnSyslogMessageTable=rdnSyslogMessageTable, rdnSyslogServerAddress=rdnSyslogServerAddress, rdnSyslogMessageTableEntry=rdnSyslogMessageTableEntry, rdnSyslogSeverity=rdnSyslogSeverity, rdnSyslogRateLimitAutoRestart=rdnSyslogRateLimitAutoRestart, rdnSyslogTraps=rdnSyslogTraps, rdnSyslogServerTable=rdnSyslogServerTable, rdnSyslogMessageIndex=rdnSyslogMessageIndex, rdnSyslog=rdnSyslog, rdnSyslogClear=rdnSyslogClear, rdnSyslogConsoleSeverity=rdnSyslogConsoleSeverity, rdnSyslogMIB=rdnSyslogMIB, rdnSyslogServerEntry=rdnSyslogServerEntry, rdnSyslogTrapSeverity=rdnSyslogTrapSeverity, rdnSyslogMaxSize=rdnSyslogMaxSize)

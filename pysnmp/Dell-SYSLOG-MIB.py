#
# PySNMP MIB module Dell-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:42:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, TimeTicks, ModuleIdentity, Bits, Gauge32, Counter32, IpAddress, MibIdentifier, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "TimeTicks", "ModuleIdentity", "Bits", "Gauge32", "Counter32", "IpAddress", "MibIdentifier", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity")
RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
rlSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 82))
rlSyslog.setRevisions(('2006-02-12 00:00', '2003-09-22 00:00',))
if mibBuilder.loadTexts: rlSyslog.setLastUpdated('200602120000Z')
if mibBuilder.loadTexts: rlSyslog.setOrganization('Dell')
class RlSyslogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("notActive", 8))

rlSyslogPrivate = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 82, 2))
rlSyslogGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogGlobalEnable.setStatus('current')
rlSyslogMinLogToConsoleSeverity = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 2), RlSyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToConsoleSeverity.setStatus('current')
rlSyslogMinLogToFileSeverity = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 3), RlSyslogSeverity().clone('error')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToFileSeverity.setStatus('current')
rlSyslogMinLogToCacheSeverity = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 4), RlSyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToCacheSeverity.setStatus('current')
rlSyslogClearLogfile = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogClearLogfile.setStatus('current')
rlSyslogClearCache = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogClearCache.setStatus('current')
rlSyslogMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogMibVersion.setStatus('current')
rlSyslogLogTable = MibTable((1, 3, 6, 1, 4, 1, 89, 82, 2, 8), )
if mibBuilder.loadTexts: rlSyslogLogTable.setStatus('current')
rlSyslogLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1), ).setIndexNames((0, "Dell-SYSLOG-MIB", "rlSyslogLogCounter"))
if mibBuilder.loadTexts: rlSyslogLogEntry.setStatus('current')
rlSyslogLogCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCounter.setStatus('current')
rlSyslogLogDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogDateTime.setStatus('current')
rlSyslogLogAppMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogAppMnemonic.setStatus('current')
rlSyslogLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 4), RlSyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogSeverity.setStatus('current')
rlSyslogLogMessageMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogMessageMnemonic.setStatus('current')
rlSyslogLogText1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText1.setStatus('current')
rlSyslogLogText2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText2.setStatus('current')
rlSyslogLogText3 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText3.setStatus('current')
rlSyslogLogText4 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText4.setStatus('current')
rlSyslogLogCacheTable = MibTable((1, 3, 6, 1, 4, 1, 89, 82, 2, 9), )
if mibBuilder.loadTexts: rlSyslogLogCacheTable.setStatus('current')
rlSyslogLogCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1), ).setIndexNames((0, "Dell-SYSLOG-MIB", "rlSyslogLogCacheCounter"))
if mibBuilder.loadTexts: rlSyslogLogCacheEntry.setStatus('current')
rlSyslogLogCacheCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheCounter.setStatus('current')
rlSyslogLogCacheDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheDateTime.setStatus('current')
rlSyslogLogCacheAppMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheAppMnemonic.setStatus('current')
rlSyslogLogCacheSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 4), RlSyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheSeverity.setStatus('current')
rlSyslogLogCacheMessageMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheMessageMnemonic.setStatus('current')
rlSyslogLogCacheText1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText1.setStatus('current')
rlSyslogLogCacheText2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText2.setStatus('current')
rlSyslogLogCacheText3 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText3.setStatus('current')
rlSyslogLogCacheText4 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText4.setStatus('current')
rlSyslogConsoleMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogConsoleMessagesIgnored.setStatus('current')
rlSyslogFileMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogFileMessagesIgnored.setStatus('current')
rlSyslogFileMessagesLogged = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogFileMessagesLogged.setStatus('current')
rlSyslogCacheTotalMessages = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCacheTotalMessages.setStatus('current')
rlSyslogAggregationEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogAggregationEnable.setStatus('current')
rlSyslogAggregationAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 3600)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogAggregationAgingTime.setStatus('current')
rlSyslogMinLogToWebSeverity = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 16), RlSyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToWebSeverity.setStatus('current')
rlSyslogAlarmFlag = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 17), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogAlarmFlag.setStatus('current')
rlSyslogOriginId = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("default", 1), ("hostname", 2), ("ip", 3), ("ipv6", 4), ("string", 5))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogOriginId.setStatus('current')
rlSyslogOriginIdString = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogOriginIdString.setStatus('current')
rlSyslogHeaderSendingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 20), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogHeaderSendingEnabled.setStatus('current')
rlSyslogPhaseOneTests = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 82, 3))
rlSyslogPhaseOneTestGenerator = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 36, 41, 42, 43, 47, 62))).clone(namedValues=NamedValues(("successfulRegistration", 11), ("regTheSameComponentTwice", 12), ("regWithInvalidComponentID", 13), ("regWithInvalidApplicationID", 14), ("regWithInvalidMessageString", 15), ("regWithInvalidMessageList", 16), ("regWithInvalidApplicationList", 17), ("successfulLoggingWithNoParams", 21), ("logWithUnregisteredComponentID", 22), ("logWithInvalidComponentID", 23), ("logWithBadApplicationID", 24), ("logWithBadMessageID", 25), ("paramFormatting", 31), ("insufficientParams", 32), ("incorrectParams", 33), ("tooManyParams", 34), ("oversizedParams", 35), ("trapParams", 36), ("successfulFatalError", 41), ("fatalErrorThroughNonFatalInterface", 42), ("nonFatalErrorThroughFatalInterface", 43), ("nestedFatalErrors", 47), ("snmpAccessToLongMessage", 62)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogPhaseOneTestGenerator.setStatus('current')
rlSyslogCountersPerSeverityTable = MibTable((1, 3, 6, 1, 4, 1, 89, 82, 2, 21), )
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityTable.setStatus('current')
rlSyslogCountersPerSeverityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1), ).setIndexNames((0, "Dell-SYSLOG-MIB", "rlSyslogCountersPerSeverityIndex"))
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityEntry.setStatus('current')
rlSyslogCountersPerSeverityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("static", 1))))
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityIndex.setStatus('current')
rlSyslogCountersPerSeverityEmergencyCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityEmergencyCounter.setStatus('current')
rlSyslogCountersPerSeverityAlertCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityAlertCounter.setStatus('current')
rlSyslogCountersPerSeverityCriticalCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityCriticalCounter.setStatus('current')
rlSyslogCountersPerSeverityErrorCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityErrorCounter.setStatus('current')
rlSyslogCountersPerSeverityWarningCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityWarningCounter.setStatus('current')
rlSyslogCountersPerSeverityNoticeCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityNoticeCounter.setStatus('current')
rlSyslogCountersPerSeverityInfoCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityInfoCounter.setStatus('current')
rlSyslogCountersPerSeverityDebugCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 21, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCountersPerSeverityDebugCounter.setStatus('current')
rlSyslogLastIndexPerSeverityTable = MibTable((1, 3, 6, 1, 4, 1, 89, 82, 2, 22), )
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityTable.setStatus('current')
rlSyslogLastIndexPerSeverityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1), ).setIndexNames((0, "Dell-SYSLOG-MIB", "rlSyslogLastIndexPerSeverityIndex"))
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityEntry.setStatus('current')
rlSyslogLastIndexPerSeverityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("static", 1))))
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityIndex.setStatus('current')
rlSyslogLastIndexPerSeverityEmergencyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityEmergencyIndex.setStatus('current')
rlSyslogLastIndexPerSeverityAlertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityAlertIndex.setStatus('current')
rlSyslogLastIndexPerSeverityCriticalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityCriticalIndex.setStatus('current')
rlSyslogLastIndexPerSeverityErrorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityErrorIndex.setStatus('current')
rlSyslogLastIndexPerSeverityWarningIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityWarningIndex.setStatus('current')
rlSyslogLastIndexPerSeverityNoticeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityNoticeIndex.setStatus('current')
rlSyslogLastIndexPerSeverityInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityInfoIndex.setStatus('current')
rlSyslogLastIndexPerSeverityDebugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 22, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLastIndexPerSeverityDebugIndex.setStatus('current')
mibBuilder.exportSymbols("Dell-SYSLOG-MIB", rlSyslogCountersPerSeverityEntry=rlSyslogCountersPerSeverityEntry, rlSyslogCountersPerSeverityEmergencyCounter=rlSyslogCountersPerSeverityEmergencyCounter, rlSyslogLogCacheDateTime=rlSyslogLogCacheDateTime, rlSyslogLogCacheAppMnemonic=rlSyslogLogCacheAppMnemonic, RlSyslogSeverity=RlSyslogSeverity, rlSyslogMinLogToFileSeverity=rlSyslogMinLogToFileSeverity, rlSyslogLogCacheCounter=rlSyslogLogCacheCounter, rlSyslogLogCacheText2=rlSyslogLogCacheText2, rlSyslogConsoleMessagesIgnored=rlSyslogConsoleMessagesIgnored, rlSyslogPhaseOneTests=rlSyslogPhaseOneTests, rlSyslogLastIndexPerSeverityErrorIndex=rlSyslogLastIndexPerSeverityErrorIndex, rlSyslogLastIndexPerSeverityWarningIndex=rlSyslogLastIndexPerSeverityWarningIndex, rlSyslogLogText3=rlSyslogLogText3, rlSyslogCountersPerSeverityInfoCounter=rlSyslogCountersPerSeverityInfoCounter, rlSyslogPhaseOneTestGenerator=rlSyslogPhaseOneTestGenerator, rlSyslogCountersPerSeverityCriticalCounter=rlSyslogCountersPerSeverityCriticalCounter, rlSyslogLastIndexPerSeverityTable=rlSyslogLastIndexPerSeverityTable, rlSyslogCountersPerSeverityAlertCounter=rlSyslogCountersPerSeverityAlertCounter, rlSyslogHeaderSendingEnabled=rlSyslogHeaderSendingEnabled, rlSyslogLogCacheMessageMnemonic=rlSyslogLogCacheMessageMnemonic, rlSyslogLogTable=rlSyslogLogTable, rlSyslogLogCounter=rlSyslogLogCounter, rlSyslogLogCacheTable=rlSyslogLogCacheTable, rlSyslogAggregationEnable=rlSyslogAggregationEnable, rlSyslogOriginIdString=rlSyslogOriginIdString, rlSyslogLogEntry=rlSyslogLogEntry, rlSyslogLastIndexPerSeverityNoticeIndex=rlSyslogLastIndexPerSeverityNoticeIndex, rlSyslogLogCacheText1=rlSyslogLogCacheText1, rlSyslogLogCacheEntry=rlSyslogLogCacheEntry, rlSyslogCountersPerSeverityWarningCounter=rlSyslogCountersPerSeverityWarningCounter, rlSyslogMinLogToConsoleSeverity=rlSyslogMinLogToConsoleSeverity, rlSyslogLogCacheText3=rlSyslogLogCacheText3, rlSyslogAlarmFlag=rlSyslogAlarmFlag, rlSyslogMinLogToCacheSeverity=rlSyslogMinLogToCacheSeverity, rlSyslogLogCacheSeverity=rlSyslogLogCacheSeverity, rlSyslogLogCacheText4=rlSyslogLogCacheText4, rlSyslogFileMessagesLogged=rlSyslogFileMessagesLogged, rlSyslogCacheTotalMessages=rlSyslogCacheTotalMessages, rlSyslogAggregationAgingTime=rlSyslogAggregationAgingTime, rlSyslogMibVersion=rlSyslogMibVersion, rlSyslogMinLogToWebSeverity=rlSyslogMinLogToWebSeverity, rlSyslogLogDateTime=rlSyslogLogDateTime, rlSyslogLastIndexPerSeverityEntry=rlSyslogLastIndexPerSeverityEntry, rlSyslogLogText4=rlSyslogLogText4, rlSyslogLogSeverity=rlSyslogLogSeverity, rlSyslogFileMessagesIgnored=rlSyslogFileMessagesIgnored, rlSyslogPrivate=rlSyslogPrivate, rlSyslogLogAppMnemonic=rlSyslogLogAppMnemonic, rlSyslogCountersPerSeverityTable=rlSyslogCountersPerSeverityTable, rlSyslogCountersPerSeverityDebugCounter=rlSyslogCountersPerSeverityDebugCounter, rlSyslogLogText1=rlSyslogLogText1, rlSyslogLastIndexPerSeverityInfoIndex=rlSyslogLastIndexPerSeverityInfoIndex, PYSNMP_MODULE_ID=rlSyslog, rlSyslogGlobalEnable=rlSyslogGlobalEnable, rlSyslogCountersPerSeverityIndex=rlSyslogCountersPerSeverityIndex, rlSyslogClearCache=rlSyslogClearCache, rlSyslogLastIndexPerSeverityCriticalIndex=rlSyslogLastIndexPerSeverityCriticalIndex, rlSyslogLastIndexPerSeverityAlertIndex=rlSyslogLastIndexPerSeverityAlertIndex, rlSyslogClearLogfile=rlSyslogClearLogfile, rlSyslogLogText2=rlSyslogLogText2, rlSyslog=rlSyslog, rlSyslogOriginId=rlSyslogOriginId, rlSyslogCountersPerSeverityNoticeCounter=rlSyslogCountersPerSeverityNoticeCounter, rlSyslogCountersPerSeverityErrorCounter=rlSyslogCountersPerSeverityErrorCounter, rlSyslogLastIndexPerSeverityEmergencyIndex=rlSyslogLastIndexPerSeverityEmergencyIndex, rlSyslogLastIndexPerSeverityIndex=rlSyslogLastIndexPerSeverityIndex, rlSyslogLastIndexPerSeverityDebugIndex=rlSyslogLastIndexPerSeverityDebugIndex, rlSyslogLogMessageMnemonic=rlSyslogLogMessageMnemonic)

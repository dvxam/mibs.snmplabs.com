#
# PySNMP MIB module Juniper-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-LOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniLogSeverity, = mibBuilder.importSymbols("Juniper-TC", "JuniLogSeverity")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, ObjectIdentity, Unsigned32, ModuleIdentity, iso, TimeTicks, MibIdentifier, Counter64, NotificationType, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "iso", "TimeTicks", "MibIdentifier", "Counter64", "NotificationType", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress")
DisplayString, DateAndTime, TextualConvention, RowStatus, TruthValue, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "RowStatus", "TruthValue", "TimeStamp")
juniLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28))
juniLogMIB.setRevisions(('2002-09-16 21:44', '2001-03-16 19:02', '2000-03-27 05:00', '1999-11-08 00:00',))
if mibBuilder.loadTexts: juniLogMIB.setLastUpdated('200209162144Z')
if mibBuilder.loadTexts: juniLogMIB.setOrganization('Juniper Networks, Inc.')
class JuniLogCatName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class JuniLogVerbosity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("low", 0), ("medium", 1), ("high", 2))

class JuniLogSyslogFacility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("local0", 0), ("local1", 1), ("local2", 2), ("local3", 3), ("local4", 4), ("local5", 5), ("local6", 6), ("local7", 7))

juniLogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1))
juniLogDestinations = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1))
juniLogCategories = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2))
juniLogMessages = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3))
juniLogDestSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1))
juniLogDestConsole = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2))
juniLogDestNvFile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3))
juniLogDestSyslogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 1), JuniLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLogDestSyslogSeverity.setStatus('obsolete')
juniLogDestSyslogAddress = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLogDestSyslogAddress.setStatus('obsolete')
juniLogSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3), )
if mibBuilder.loadTexts: juniLogSyslogTable.setStatus('current')
juniLogSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1), ).setIndexNames((0, "Juniper-LOG-MIB", "juniLogSyslogIpAddress"))
if mibBuilder.loadTexts: juniLogSyslogEntry.setStatus('current')
juniLogSyslogIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: juniLogSyslogIpAddress.setStatus('current')
juniLogSyslogRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniLogSyslogRowStatus.setStatus('current')
juniLogSyslogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 3), JuniLogSeverity().clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniLogSyslogSeverity.setStatus('current')
juniLogSyslogFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 4), JuniLogSyslogFacility().clone('local7')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniLogSyslogFacility.setStatus('current')
juniLogDestConsoleSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2, 1), JuniLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLogDestConsoleSeverity.setStatus('current')
juniLogDestNvFileSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3, 1), JuniLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLogDestNvFileSeverity.setStatus('current')
juniLogCatScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 1))
juniLogCatTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2), )
if mibBuilder.loadTexts: juniLogCatTable.setStatus('current')
juniLogCatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1), ).setIndexNames((0, "Juniper-LOG-MIB", "juniLogCatIndex"))
if mibBuilder.loadTexts: juniLogCatEntry.setStatus('current')
juniLogCatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: juniLogCatIndex.setStatus('current')
juniLogCatName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 2), JuniLogCatName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogCatName.setStatus('current')
juniLogCatDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogCatDescr.setStatus('current')
juniLogCatEngineering = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogCatEngineering.setStatus('current')
juniLogCatDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogCatDiscards.setStatus('current')
juniLogCatSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 6), JuniLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLogCatSeverity.setStatus('current')
juniLogCatVerbosity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 7), JuniLogVerbosity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLogCatVerbosity.setStatus('current')
juniLogCatNameTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3), )
if mibBuilder.loadTexts: juniLogCatNameTable.setStatus('current')
juniLogCatNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1), ).setIndexNames((1, "Juniper-LOG-MIB", "juniLogCatNameName"))
if mibBuilder.loadTexts: juniLogCatNameEntry.setStatus('current')
juniLogCatNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 1), JuniLogCatName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogCatNameName.setStatus('current')
juniLogCatNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogCatNameIndex.setStatus('current')
juniLogMsgScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1))
juniLogMsgCapacity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 1), Integer32()).setUnits('messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogMsgCapacity.setStatus('current')
juniLogMsgLastSeqNumber = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogMsgLastSeqNumber.setStatus('current')
juniLogMsgTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2), )
if mibBuilder.loadTexts: juniLogMsgTable.setStatus('current')
juniLogMsgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1), ).setIndexNames((0, "Juniper-LOG-MIB", "juniLogMsgSysUpTimeStamp"), (0, "Juniper-LOG-MIB", "juniLogMsgSequenceNumber"))
if mibBuilder.loadTexts: juniLogMsgEntry.setStatus('current')
juniLogMsgSysUpTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 1), TimeStamp())
if mibBuilder.loadTexts: juniLogMsgSysUpTimeStamp.setStatus('current')
juniLogMsgSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: juniLogMsgSequenceNumber.setStatus('current')
juniLogMsgCatName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 3), JuniLogCatName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogMsgCatName.setStatus('current')
juniLogMsgCatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogMsgCatIndex.setStatus('current')
juniLogMsgSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 5), JuniLogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogMsgSeverity.setStatus('current')
juniLogMsgText = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogMsgText.setStatus('current')
juniLogMsgDateAndTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLogMsgDateAndTimeStamp.setStatus('current')
juniLogTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2))
juniLogMsgThreshold = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLogMsgThreshold.setStatus('current')
juniLogTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0))
juniLogMsgThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0, 1)).setObjects(("Juniper-LOG-MIB", "juniLogMsgCapacity"), ("Juniper-LOG-MIB", "juniLogMsgLastSeqNumber"), ("Juniper-LOG-MIB", "juniLogMsgThreshold"))
if mibBuilder.loadTexts: juniLogMsgThresholdTrap.setStatus('current')
juniLogMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4))
juniLogMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1))
juniLogMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2))
juniLogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 1)).setObjects(("Juniper-LOG-MIB", "juniLogGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogCompliance = juniLogCompliance.setStatus('obsolete')
juniLogCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 2)).setObjects(("Juniper-LOG-MIB", "juniLogGroup2"), ("Juniper-LOG-MIB", "juniLogTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogCompliance2 = juniLogCompliance2.setStatus('current')
juniLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 1)).setObjects(("Juniper-LOG-MIB", "juniLogDestSyslogSeverity"), ("Juniper-LOG-MIB", "juniLogDestSyslogAddress"), ("Juniper-LOG-MIB", "juniLogDestConsoleSeverity"), ("Juniper-LOG-MIB", "juniLogDestNvFileSeverity"), ("Juniper-LOG-MIB", "juniLogCatName"), ("Juniper-LOG-MIB", "juniLogCatDescr"), ("Juniper-LOG-MIB", "juniLogCatEngineering"), ("Juniper-LOG-MIB", "juniLogCatDiscards"), ("Juniper-LOG-MIB", "juniLogCatSeverity"), ("Juniper-LOG-MIB", "juniLogCatVerbosity"), ("Juniper-LOG-MIB", "juniLogCatNameName"), ("Juniper-LOG-MIB", "juniLogCatNameIndex"), ("Juniper-LOG-MIB", "juniLogMsgCapacity"), ("Juniper-LOG-MIB", "juniLogMsgLastSeqNumber"), ("Juniper-LOG-MIB", "juniLogMsgCatName"), ("Juniper-LOG-MIB", "juniLogMsgCatIndex"), ("Juniper-LOG-MIB", "juniLogMsgSeverity"), ("Juniper-LOG-MIB", "juniLogMsgText"), ("Juniper-LOG-MIB", "juniLogMsgDateAndTimeStamp"), ("Juniper-LOG-MIB", "juniLogMsgThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogGroup = juniLogGroup.setStatus('obsolete')
juniLogGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 2)).setObjects(("Juniper-LOG-MIB", "juniLogSyslogRowStatus"), ("Juniper-LOG-MIB", "juniLogSyslogSeverity"), ("Juniper-LOG-MIB", "juniLogSyslogFacility"), ("Juniper-LOG-MIB", "juniLogDestConsoleSeverity"), ("Juniper-LOG-MIB", "juniLogDestNvFileSeverity"), ("Juniper-LOG-MIB", "juniLogCatName"), ("Juniper-LOG-MIB", "juniLogCatDescr"), ("Juniper-LOG-MIB", "juniLogCatEngineering"), ("Juniper-LOG-MIB", "juniLogCatDiscards"), ("Juniper-LOG-MIB", "juniLogCatSeverity"), ("Juniper-LOG-MIB", "juniLogCatVerbosity"), ("Juniper-LOG-MIB", "juniLogCatNameName"), ("Juniper-LOG-MIB", "juniLogCatNameIndex"), ("Juniper-LOG-MIB", "juniLogMsgCapacity"), ("Juniper-LOG-MIB", "juniLogMsgLastSeqNumber"), ("Juniper-LOG-MIB", "juniLogMsgCatName"), ("Juniper-LOG-MIB", "juniLogMsgCatIndex"), ("Juniper-LOG-MIB", "juniLogMsgSeverity"), ("Juniper-LOG-MIB", "juniLogMsgText"), ("Juniper-LOG-MIB", "juniLogMsgDateAndTimeStamp"), ("Juniper-LOG-MIB", "juniLogMsgThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogGroup2 = juniLogGroup2.setStatus('current')
juniLogTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 3)).setObjects(("Juniper-LOG-MIB", "juniLogMsgThresholdTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogTrapGroup = juniLogTrapGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-LOG-MIB", juniLogDestNvFileSeverity=juniLogDestNvFileSeverity, juniLogSyslogIpAddress=juniLogSyslogIpAddress, JuniLogCatName=JuniLogCatName, juniLogCatNameIndex=juniLogCatNameIndex, juniLogMsgDateAndTimeStamp=juniLogMsgDateAndTimeStamp, juniLogTrapGroup=juniLogTrapGroup, juniLogSyslogRowStatus=juniLogSyslogRowStatus, juniLogDestSyslogSeverity=juniLogDestSyslogSeverity, juniLogCatScalars=juniLogCatScalars, juniLogCompliance2=juniLogCompliance2, juniLogDestSyslogAddress=juniLogDestSyslogAddress, juniLogObjects=juniLogObjects, juniLogDestConsole=juniLogDestConsole, juniLogDestSyslog=juniLogDestSyslog, JuniLogVerbosity=JuniLogVerbosity, juniLogCatSeverity=juniLogCatSeverity, juniLogMsgCapacity=juniLogMsgCapacity, juniLogMsgTable=juniLogMsgTable, juniLogMIBConformance=juniLogMIBConformance, juniLogMIBCompliances=juniLogMIBCompliances, juniLogCatVerbosity=juniLogCatVerbosity, juniLogMsgCatName=juniLogMsgCatName, juniLogSyslogFacility=juniLogSyslogFacility, juniLogMessages=juniLogMessages, juniLogMsgLastSeqNumber=juniLogMsgLastSeqNumber, juniLogDestinations=juniLogDestinations, juniLogMsgSysUpTimeStamp=juniLogMsgSysUpTimeStamp, juniLogMsgSeverity=juniLogMsgSeverity, juniLogMsgThresholdTrap=juniLogMsgThresholdTrap, juniLogCatName=juniLogCatName, juniLogCompliance=juniLogCompliance, juniLogMsgScalars=juniLogMsgScalars, juniLogMIB=juniLogMIB, juniLogCatTable=juniLogCatTable, juniLogCatEngineering=juniLogCatEngineering, juniLogTrapControl=juniLogTrapControl, juniLogDestNvFile=juniLogDestNvFile, juniLogCatIndex=juniLogCatIndex, PYSNMP_MODULE_ID=juniLogMIB, juniLogCatDiscards=juniLogCatDiscards, juniLogMsgEntry=juniLogMsgEntry, JuniLogSyslogFacility=JuniLogSyslogFacility, juniLogSyslogSeverity=juniLogSyslogSeverity, juniLogCatEntry=juniLogCatEntry, juniLogSyslogTable=juniLogSyslogTable, juniLogCatDescr=juniLogCatDescr, juniLogDestConsoleSeverity=juniLogDestConsoleSeverity, juniLogMIBGroups=juniLogMIBGroups, juniLogCatNameTable=juniLogCatNameTable, juniLogMsgThreshold=juniLogMsgThreshold, juniLogMsgSequenceNumber=juniLogMsgSequenceNumber, juniLogCatNameEntry=juniLogCatNameEntry, juniLogTrapPrefix=juniLogTrapPrefix, juniLogSyslogEntry=juniLogSyslogEntry, juniLogGroup=juniLogGroup, juniLogMsgText=juniLogMsgText, juniLogCatNameName=juniLogCatNameName, juniLogGroup2=juniLogGroup2, juniLogCategories=juniLogCategories, juniLogMsgCatIndex=juniLogMsgCatIndex)

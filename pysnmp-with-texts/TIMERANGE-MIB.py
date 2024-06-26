#
# PySNMP MIB module TIMERANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMERANGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:05:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, NotificationType, iso, Counter64, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "NotificationType", "iso", "Counter64", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DateAndTime, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TextualConvention", "DisplayString")
swTimeRangeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 50))
if mibBuilder.loadTexts: swTimeRangeMIB.setLastUpdated('0703270000Z')
if mibBuilder.loadTexts: swTimeRangeMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swTimeRangeMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swTimeRangeMIB.setDescription('This MIB defines a specific range of time to activate a function.')
swTimeRangeCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 50, 1))
swTimeRangeInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 50, 2))
swTimeRangeMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 50, 3))
swTimeRangeMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1), )
if mibBuilder.loadTexts: swTimeRangeMgmtTable.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeMgmtTable.setDescription('A table that contains the information of each time range.')
swTimeRangeMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1), ).setIndexNames((0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"))
if mibBuilder.loadTexts: swTimeRangeMgmtEntry.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeMgmtEntry.setDescription('A list of information of each time range.')
swTimeRangeMgmtRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swTimeRangeMgmtRangeName.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeMgmtRangeName.setDescription('The range name of the time range.')
swTimeRangeMgmtSelectDays = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swTimeRangeMgmtSelectDays.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeMgmtSelectDays.setDescription("Each day in the week is presented by an abbreviation: 'SUN', 'MON', TUE', 'WED', 'THU', 'FRI', and 'SAT'. The 'SUN' stands for Sunday, 'MON' stands for Monday, and so on. If more than one day is required, a comma is used to separate those days.")
swTimeRangeMgmtStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swTimeRangeMgmtStartTime.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeMgmtStartTime.setDescription('The start time of a day. The format is hh:mm:ss ONLY; and cannot be set using a different format. The ending time must be set later than the starting time. The default value is 00:00:00.')
swTimeRangeMgmtEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swTimeRangeMgmtEndTime.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeMgmtEndTime.setDescription('The end time of a day. The format is hh:mm:ss ONLY; and cannot be set using a different format. The ending time must be set later than the starting time. The default value is 24:00:00.')
swTimeRangeMgmtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swTimeRangeMgmtStatus.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeMgmtStatus.setDescription('This object indicates the RowStatus of this entry.')
swTimeRangeACLTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2), )
if mibBuilder.loadTexts: swTimeRangeACLTable.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeACLTable.setDescription('This table maintains time-range settings associated with a specific rule in the ACL rule table. Please refer to the swACLEtherRuleTable, swACLIpRuleTable, swACLIpv6RuleTable and swACLPktContRuleTable for detailed ACL rule information.')
swTimeRangeACLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2, 1), ).setIndexNames((0, "TIMERANGE-MIB", "swTimeRangeACLProfileID"), (0, "TIMERANGE-MIB", "swTimeRangeACLAccessID"))
if mibBuilder.loadTexts: swTimeRangeACLEntry.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeACLEntry.setDescription('The entry maintains time-range names associated with the ACL rule table.')
swTimeRangeACLProfileID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swTimeRangeACLProfileID.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeACLProfileID.setDescription('The ID of the ACL mask entry, which is unique in the mask list.')
swTimeRangeACLAccessID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swTimeRangeACLAccessID.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeACLAccessID.setDescription('The ID of the ACL rule entry as related to the swTimeRangeACLProfileID.')
swTimeRangeACLTimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swTimeRangeACLTimeRangeName.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeACLTimeRangeName.setDescription('Specifies a time-range name associated with a specific ACL entry. The time-range name must first be created before being associated with the access rule. If this name is an empty string, it means the time-range profile will no longer be associated with the access rule. When a rule is de-associated with a time range, the access rule will be enabled all the time.')
swTimeRangeCPUACLTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3), )
if mibBuilder.loadTexts: swTimeRangeCPUACLTable.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeCPUACLTable.setDescription('This table maintains time-range settings associated with a specific rule in the CPU ACL rule table. Please refer to the swCpuAclEtherRuleTable, swCpuAclIpRuleTable, swCpuAclPktContRuleTable and swCpuAclIpv6RuleTable for detailed CPU ACL rule information.')
swTimeRangeCPUACLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3, 1), ).setIndexNames((0, "TIMERANGE-MIB", "swTimeRangeCPUACLProfileID"), (0, "TIMERANGE-MIB", "swTimeRangeCPUACLAccessID"))
if mibBuilder.loadTexts: swTimeRangeCPUACLEntry.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeCPUACLEntry.setDescription('The entry maintains time-range names associated with the CPU ACL rule table.')
swTimeRangeCPUACLProfileID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swTimeRangeCPUACLProfileID.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeCPUACLProfileID.setDescription('The ID of the CPU ACL mask entry, which is unique in the mask list.')
swTimeRangeCPUACLAccessID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swTimeRangeCPUACLAccessID.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeCPUACLAccessID.setDescription('The ID of the CPU ACL rule entry as related to the swTimeRangeCPUACLProfileID.')
swTimeRangeCPUACLTimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 50, 3, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swTimeRangeCPUACLTimeRangeName.setStatus('current')
if mibBuilder.loadTexts: swTimeRangeCPUACLTimeRangeName.setDescription('Specifies a time-range name associated with a specific CPU ACL entry. The time-range name must first be created before being associated with the access rule. If this name is an empty string, it means the time-range profile will no longer be associated with the access rule. When a rule is de-associated with a time range, the access rule will be enabled all the time.')
mibBuilder.exportSymbols("TIMERANGE-MIB", PYSNMP_MODULE_ID=swTimeRangeMIB, swTimeRangeCPUACLAccessID=swTimeRangeCPUACLAccessID, swTimeRangeMgmt=swTimeRangeMgmt, swTimeRangeMgmtRangeName=swTimeRangeMgmtRangeName, swTimeRangeMgmtStartTime=swTimeRangeMgmtStartTime, swTimeRangeACLProfileID=swTimeRangeACLProfileID, swTimeRangeCtrl=swTimeRangeCtrl, swTimeRangeMIB=swTimeRangeMIB, swTimeRangeMgmtSelectDays=swTimeRangeMgmtSelectDays, swTimeRangeACLAccessID=swTimeRangeACLAccessID, swTimeRangeMgmtEntry=swTimeRangeMgmtEntry, swTimeRangeCPUACLEntry=swTimeRangeCPUACLEntry, swTimeRangeMgmtEndTime=swTimeRangeMgmtEndTime, swTimeRangeACLEntry=swTimeRangeACLEntry, swTimeRangeACLTable=swTimeRangeACLTable, swTimeRangeMgmtTable=swTimeRangeMgmtTable, swTimeRangeCPUACLTimeRangeName=swTimeRangeCPUACLTimeRangeName, swTimeRangeMgmtStatus=swTimeRangeMgmtStatus, swTimeRangeCPUACLTable=swTimeRangeCPUACLTable, swTimeRangeInfo=swTimeRangeInfo, swTimeRangeACLTimeRangeName=swTimeRangeACLTimeRangeName, swTimeRangeCPUACLProfileID=swTimeRangeCPUACLProfileID)

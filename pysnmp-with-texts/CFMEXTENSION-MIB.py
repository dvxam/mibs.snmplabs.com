#
# PySNMP MIB module CFMEXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CFMEXTENSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:48:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
dot1agCfmMaIndex, dot1agCfmMdIndex, Dot1agCfmMepId, Dot1agCfmMDLevel, dot1agCfmMaMepListIdentifier, dot1agCfmMepIdentifier = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMaIndex", "dot1agCfmMdIndex", "Dot1agCfmMepId", "Dot1agCfmMDLevel", "dot1agCfmMaMepListIdentifier", "dot1agCfmMepIdentifier")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, IpAddress, ModuleIdentity, Gauge32, TimeTicks, MibIdentifier, Counter32, Integer32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Gauge32", "TimeTicks", "MibIdentifier", "Counter32", "Integer32", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swCFMExtensionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 86))
if mibBuilder.loadTexts: swCFMExtensionMIB.setLastUpdated('0909260000Z')
if mibBuilder.loadTexts: swCFMExtensionMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swCFMExtensionMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swCFMExtensionMIB.setDescription('The structure of CFM extension for ITU Y1731.')
swCFMExtFaultMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 86, 1))
swCFMExtNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 86, 100))
swCFMExtMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1), )
if mibBuilder.loadTexts: swCFMExtMgmtTable.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtTable.setDescription('A table that contains CFM extension fault management configuration information.')
swCFMExtMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtMgmtEntry.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtEntry.setDescription('A list of CFM extension fault management configuration information.')
swCFMExtMgmtAISState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtAISState.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtAISState.setDescription('This object indicates the AIS function State.')
swCFMExtMgmtAISPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("one-second", 1), ("one-minute", 2))).clone('one-second')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtAISPeriod.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtAISPeriod.setDescription('This object indicates the transmitting interval of AIS PDU.')
swCFMExtMgmtAISLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 3), Dot1agCfmMDLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtAISLevel.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtAISLevel.setDescription('This object indicates the client level to which AIS PDU is sent.')
swCFMExtMgmtAISStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("cleared", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swCFMExtMgmtAISStatus.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtAISStatus.setDescription('This object indicates the status of AIS function.')
swCFMExtMgmtLockState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtLockState.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtLockState.setDescription('This object indicates the lock function state.')
swCFMExtMgmtLockPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("one-second", 1), ("one-minute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtLockPeriod.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtLockPeriod.setDescription('This object indicates the period of sending lock PDU.')
swCFMExtMgmtLockLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 7), Dot1agCfmMDLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtLockLevel.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtLockLevel.setDescription('This object indicates the client level to which lock PDU is sent.')
swCFMExtMgmtLockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("cleared", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swCFMExtMgmtLockStatus.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtLockStatus.setDescription('This object indicates the status of lock function.')
swCFMExtMgmtLockCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 2), )
if mibBuilder.loadTexts: swCFMExtMgmtLockCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtLockCtrlTable.setDescription('A table that contains CFM extension lock control information.')
swCFMExtMgmtLockCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaMepListIdentifier"))
if mibBuilder.loadTexts: swCFMExtMgmtLockCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtLockCtrlEntry.setDescription('A list of CFM extension lock control information.')
swCFMExtMgmtLockCtrlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtLockCtrlAction.setStatus('current')
if mibBuilder.loadTexts: swCFMExtMgmtLockCtrlAction.setDescription('This object indicates the action of the lock control function.')
swCFMExtNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0))
swCFMExtAISOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 1)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtAISOccurred.setStatus('current')
if mibBuilder.loadTexts: swCFMExtAISOccurred.setDescription('A notification is generated when local MEP enters AIS status.')
swCFMExtAISCleared = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 2)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtAISCleared.setStatus('current')
if mibBuilder.loadTexts: swCFMExtAISCleared.setDescription('A notification is generated when local MEP exits AIS status.')
swCFMExtLockOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 3)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtLockOccurred.setStatus('current')
if mibBuilder.loadTexts: swCFMExtLockOccurred.setDescription('A notification is generated when local MEP enters lock status.')
swCFMExtLockCleared = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 4)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtLockCleared.setStatus('current')
if mibBuilder.loadTexts: swCFMExtLockCleared.setDescription('A notification is generated when local MEP exits lock status.')
mibBuilder.exportSymbols("CFMEXTENSION-MIB", swCFMExtMgmtLockStatus=swCFMExtMgmtLockStatus, swCFMExtMgmtLockLevel=swCFMExtMgmtLockLevel, swCFMExtMgmtAISLevel=swCFMExtMgmtAISLevel, swCFMExtAISOccurred=swCFMExtAISOccurred, swCFMExtMgmtAISState=swCFMExtMgmtAISState, swCFMExtMgmtTable=swCFMExtMgmtTable, PYSNMP_MODULE_ID=swCFMExtensionMIB, swCFMExtLockOccurred=swCFMExtLockOccurred, swCFMExtAISCleared=swCFMExtAISCleared, swCFMExtNotify=swCFMExtNotify, swCFMExtMgmtLockCtrlAction=swCFMExtMgmtLockCtrlAction, swCFMExtFaultMgmt=swCFMExtFaultMgmt, swCFMExtMgmtEntry=swCFMExtMgmtEntry, swCFMExtMgmtAISPeriod=swCFMExtMgmtAISPeriod, swCFMExtensionMIB=swCFMExtensionMIB, swCFMExtMgmtAISStatus=swCFMExtMgmtAISStatus, swCFMExtMgmtLockCtrlTable=swCFMExtMgmtLockCtrlTable, swCFMExtNotifyPrefix=swCFMExtNotifyPrefix, swCFMExtLockCleared=swCFMExtLockCleared, swCFMExtMgmtLockState=swCFMExtMgmtLockState, swCFMExtMgmtLockPeriod=swCFMExtMgmtLockPeriod, swCFMExtMgmtLockCtrlEntry=swCFMExtMgmtLockCtrlEntry)
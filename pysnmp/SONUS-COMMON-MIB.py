#
# PySNMP MIB module SONUS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-COMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter64, Gauge32, MibIdentifier, IpAddress, Bits, TimeTicks, ObjectIdentity, ModuleIdentity, Integer32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter64", "Gauge32", "MibIdentifier", "IpAddress", "Bits", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Integer32", "iso", "Counter32")
TextualConvention, DateAndTime, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString", "RowStatus")
sonusSystemMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusSystemMIBs")
SonusNameReference, SonusTrapType, SonusAccessLevel, SonusEventClass, SonusName, SonusAdminState, SonusEventLevel, SonusEventString = mibBuilder.importSymbols("SONUS-TC", "SonusNameReference", "SonusTrapType", "SonusAccessLevel", "SonusEventClass", "SonusName", "SonusAdminState", "SonusEventLevel", "SonusEventString")
sonusCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5))
if mibBuilder.loadTexts: sonusCommonMIB.setLastUpdated('200102030000Z')
if mibBuilder.loadTexts: sonusCommonMIB.setOrganization('Sonus Networks, Inc.')
sonusCommonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1))
sonusNetMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1))
sonusNetMgmtClient = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1))
sonusNetMgmtClientNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtClientNextIndex.setStatus('current')
sonusNetMgmtClientTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2), )
if mibBuilder.loadTexts: sonusNetMgmtClientTable.setStatus('current')
sonusNetMgmtClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1), ).setIndexNames((0, "SONUS-COMMON-MIB", "sonusNetMgmtClientIndex"))
if mibBuilder.loadTexts: sonusNetMgmtClientEntry.setStatus('current')
sonusNetMgmtClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtClientIndex.setStatus('current')
sonusNetMgmtClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 2), SonusName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientName.setStatus('current')
sonusNetMgmtClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 3), SonusAdminState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientState.setStatus('current')
sonusNetMgmtClientIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 4), IpAddress().clone(hexValue="01010101")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientIpAddr.setStatus('current')
sonusNetMgmtClientAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 5), SonusAccessLevel().clone('readOnly')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientAccess.setStatus('current')
sonusNetMgmtClientSnmpCommunityGet = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 23)).clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientSnmpCommunityGet.setStatus('current')
sonusNetMgmtClientSnmpCommunitySet = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 23)).clone('private')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientSnmpCommunitySet.setStatus('current')
sonusNetMgmtClientSnmpCommunityTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 23)).clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientSnmpCommunityTrap.setStatus('current')
sonusNetMgmtClientTrapState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 9), SonusAdminState().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientTrapState.setStatus('current')
sonusNetMgmtClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientRowStatus.setStatus('current')
sonusNetMgmtClientTrapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(162)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientTrapPort.setStatus('current')
sonusNetMgmtClientAllTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 12), SonusTrapType().clone('trapv2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientAllTraps.setStatus('current')
sonusNetMgmtClientInformReqTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqTimeout.setStatus('current')
sonusNetMgmtClientInformReqRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqRetries.setStatus('current')
sonusNetMgmtClientInformReqMaxQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqMaxQueue.setStatus('current')
sonusNetMgmtClientStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3), )
if mibBuilder.loadTexts: sonusNetMgmtClientStatusTable.setStatus('current')
sonusNetMgmtClientStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3, 1), ).setIndexNames((0, "SONUS-COMMON-MIB", "sonusNetMgmtClientStatusIndex"))
if mibBuilder.loadTexts: sonusNetMgmtClientStatusEntry.setStatus('current')
sonusNetMgmtClientStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: sonusNetMgmtClientStatusIndex.setStatus('current')
sonusNetMgmtClientStatusLastConfigChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtClientStatusLastConfigChange.setStatus('current')
sonusNetMgmtTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2))
sonusNetMgmtTrapNextIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 1))
sonusNetMgmtTrapTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2), )
if mibBuilder.loadTexts: sonusNetMgmtTrapTable.setStatus('current')
sonusNetMgmtTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1), ).setIndexNames((0, "SONUS-COMMON-MIB", "sonusNetMgmtTrapIndex"))
if mibBuilder.loadTexts: sonusNetMgmtTrapEntry.setStatus('current')
sonusNetMgmtTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1))
if mibBuilder.loadTexts: sonusNetMgmtTrapIndex.setStatus('current')
sonusNetMgmtTrapName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 2), SonusName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapName.setStatus('current')
sonusNetMgmtTrapMIBName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapMIBName.setStatus('obsolete')
sonusNetMgmtTrapOID = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapOID.setStatus('current')
sonusNetMgmtTrapClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 5), SonusEventClass().clone('sysmgmt')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapClass.setStatus('current')
sonusNetMgmtTrapLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 6), SonusEventLevel().clone('info')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapLevel.setStatus('current')
sonusNetMgmtTrapState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 7), SonusAdminState().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtTrapState.setStatus('current')
sonusNetMgmtNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3))
sonusNetMgmtNotifyNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtNotifyNextIndex.setStatus('current')
sonusNetMgmtNotifyTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2), )
if mibBuilder.loadTexts: sonusNetMgmtNotifyTable.setStatus('current')
sonusNetMgmtNotifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1), ).setIndexNames((0, "SONUS-COMMON-MIB", "sonusNetMgmtNotifyIndex"))
if mibBuilder.loadTexts: sonusNetMgmtNotifyEntry.setStatus('current')
sonusNetMgmtNotifyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1))
if mibBuilder.loadTexts: sonusNetMgmtNotifyIndex.setStatus('current')
sonusNetMgmtNotifyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 2), SonusName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyName.setStatus('current')
sonusNetMgmtNotifyMgmtName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 3), SonusNameReference()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyMgmtName.setStatus('current')
sonusNetMgmtNotifyTrapName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 4), SonusNameReference()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyTrapName.setStatus('current')
sonusNetMgmtNotifyTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 5), SonusTrapType().clone('trapv2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyTrapType.setStatus('current')
sonusNetMgmtNotifyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyRowStatus.setStatus('current')
sonusCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2))
sonusCommonMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 0))
sonusCommonMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1))
sonusShelfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusShelfIndex.setStatus('current')
sonusSlotIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSlotIndex.setStatus('current')
sonusPortIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusPortIndex.setStatus('current')
sonusDs3Index = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusDs3Index.setStatus('current')
sonusDs1Index = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusDs1Index.setStatus('current')
sonusEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 6), SonusEventString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusEventDescription.setStatus('current')
sonusEventClass = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 7), SonusEventClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusEventClass.setStatus('current')
sonusEventLevel = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 8), SonusEventLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusEventLevel.setStatus('current')
sonusSequenceId = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSequenceId.setStatus('current')
sonusEventTime = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusEventTime.setStatus('current')
sonusNetMgmtInformReqDiscards = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtInformReqDiscards.setStatus('current')
sonusNetMgmtClientInformReqQueueFlushedNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 0, 1)).setObjects(("SONUS-COMMON-MIB", "sonusNetMgmtClientName"), ("SONUS-COMMON-MIB", "sonusNetMgmtInformReqDiscards"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqQueueFlushedNotification.setStatus('current')
sonusNetMgmtClientInformReqQueueFullNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 0, 2)).setObjects(("SONUS-COMMON-MIB", "sonusNetMgmtClientName"), ("SONUS-COMMON-MIB", "sonusNetMgmtInformReqDiscards"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqQueueFullNotification.setStatus('current')
mibBuilder.exportSymbols("SONUS-COMMON-MIB", sonusCommonMIB=sonusCommonMIB, sonusCommonMIBNotifications=sonusCommonMIBNotifications, sonusNetMgmtClientNextIndex=sonusNetMgmtClientNextIndex, sonusNetMgmtClientName=sonusNetMgmtClientName, sonusNetMgmtClientIndex=sonusNetMgmtClientIndex, sonusNetMgmtNotifyTrapName=sonusNetMgmtNotifyTrapName, sonusNetMgmtClientStatusEntry=sonusNetMgmtClientStatusEntry, sonusNetMgmtClientInformReqQueueFullNotification=sonusNetMgmtClientInformReqQueueFullNotification, sonusNetMgmtTrapClass=sonusNetMgmtTrapClass, sonusCommonMIBNotificationsObjects=sonusCommonMIBNotificationsObjects, sonusNetMgmtTrapLevel=sonusNetMgmtTrapLevel, sonusNetMgmtClientState=sonusNetMgmtClientState, sonusNetMgmtTrap=sonusNetMgmtTrap, sonusNetMgmtClientStatusLastConfigChange=sonusNetMgmtClientStatusLastConfigChange, sonusNetMgmtNotifyTable=sonusNetMgmtNotifyTable, sonusNetMgmtNotifyTrapType=sonusNetMgmtNotifyTrapType, sonusDs1Index=sonusDs1Index, sonusNetMgmtInformReqDiscards=sonusNetMgmtInformReqDiscards, sonusNetMgmtClientIpAddr=sonusNetMgmtClientIpAddr, sonusNetMgmtClientAllTraps=sonusNetMgmtClientAllTraps, sonusEventTime=sonusEventTime, sonusNetMgmtTrapState=sonusNetMgmtTrapState, sonusPortIndex=sonusPortIndex, sonusNetMgmtClientTrapPort=sonusNetMgmtClientTrapPort, sonusNetMgmtClientSnmpCommunitySet=sonusNetMgmtClientSnmpCommunitySet, sonusCommonMIBObjects=sonusCommonMIBObjects, sonusNetMgmtClientRowStatus=sonusNetMgmtClientRowStatus, sonusNetMgmtClientStatusIndex=sonusNetMgmtClientStatusIndex, sonusNetMgmtClientStatusTable=sonusNetMgmtClientStatusTable, sonusNetMgmtTrapOID=sonusNetMgmtTrapOID, sonusNetMgmt=sonusNetMgmt, sonusDs3Index=sonusDs3Index, PYSNMP_MODULE_ID=sonusCommonMIB, sonusNetMgmtTrapMIBName=sonusNetMgmtTrapMIBName, sonusNetMgmtClientInformReqTimeout=sonusNetMgmtClientInformReqTimeout, sonusNetMgmtClientInformReqRetries=sonusNetMgmtClientInformReqRetries, sonusNetMgmtClient=sonusNetMgmtClient, sonusNetMgmtNotifyNextIndex=sonusNetMgmtNotifyNextIndex, sonusNetMgmtNotifyEntry=sonusNetMgmtNotifyEntry, sonusNetMgmtClientInformReqMaxQueue=sonusNetMgmtClientInformReqMaxQueue, sonusNetMgmtTrapIndex=sonusNetMgmtTrapIndex, sonusCommonMIBNotificationsPrefix=sonusCommonMIBNotificationsPrefix, sonusNetMgmtClientSnmpCommunityGet=sonusNetMgmtClientSnmpCommunityGet, sonusNetMgmtTrapNextIndex=sonusNetMgmtTrapNextIndex, sonusEventClass=sonusEventClass, sonusNetMgmtNotifyIndex=sonusNetMgmtNotifyIndex, sonusNetMgmtNotifyName=sonusNetMgmtNotifyName, sonusEventLevel=sonusEventLevel, sonusSequenceId=sonusSequenceId, sonusNetMgmtNotify=sonusNetMgmtNotify, sonusNetMgmtTrapTable=sonusNetMgmtTrapTable, sonusNetMgmtClientAccess=sonusNetMgmtClientAccess, sonusNetMgmtClientEntry=sonusNetMgmtClientEntry, sonusShelfIndex=sonusShelfIndex, sonusSlotIndex=sonusSlotIndex, sonusNetMgmtTrapEntry=sonusNetMgmtTrapEntry, sonusNetMgmtClientTable=sonusNetMgmtClientTable, sonusNetMgmtClientSnmpCommunityTrap=sonusNetMgmtClientSnmpCommunityTrap, sonusNetMgmtNotifyMgmtName=sonusNetMgmtNotifyMgmtName, sonusNetMgmtClientInformReqQueueFlushedNotification=sonusNetMgmtClientInformReqQueueFlushedNotification, sonusNetMgmtTrapName=sonusNetMgmtTrapName, sonusEventDescription=sonusEventDescription, sonusNetMgmtNotifyRowStatus=sonusNetMgmtNotifyRowStatus, sonusNetMgmtClientTrapState=sonusNetMgmtClientTrapState)
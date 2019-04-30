#
# PySNMP MIB module HH3C-UI-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-UI-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:17:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, TimeTicks, ModuleIdentity, NotificationType, Gauge32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ObjectIdentity, MibIdentifier, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ModuleIdentity", "NotificationType", "Gauge32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier", "Counter64", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hh3cUIMgt = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 2))
if mibBuilder.loadTexts: hh3cUIMgt.setLastUpdated('200404081405Z')
if mibBuilder.loadTexts: hh3cUIMgt.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cUIMgtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1))
hh3cUIBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1))
hh3cUIScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 1))
hh3cUITrapBindObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 2))
hh3cTerminalUserName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cTerminalUserName.setStatus('current')
hh3cTerminalSource = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cTerminalSource.setStatus('current')
hh3cTerminalUserAuthFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("exceedRetries", 1), ("authTimeout", 2), ("otherReason", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cTerminalUserAuthFailureReason.setStatus('current')
hh3cUINotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3))
hh3cUINotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3, 0))
hh3cLogIn = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3, 0, 1)).setObjects(("HH3C-UI-MAN-MIB", "hh3cTerminalUserName"), ("HH3C-UI-MAN-MIB", "hh3cTerminalSource"))
if mibBuilder.loadTexts: hh3cLogIn.setStatus('current')
hh3cLogOut = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3, 0, 2)).setObjects(("HH3C-UI-MAN-MIB", "hh3cTerminalUserName"), ("HH3C-UI-MAN-MIB", "hh3cTerminalSource"))
if mibBuilder.loadTexts: hh3cLogOut.setStatus('current')
hh3cLogInAuthenFailure = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 1, 3, 0, 3)).setObjects(("HH3C-UI-MAN-MIB", "hh3cTerminalUserName"), ("HH3C-UI-MAN-MIB", "hh3cTerminalSource"), ("HH3C-UI-MAN-MIB", "hh3cTerminalUserAuthFailureReason"))
if mibBuilder.loadTexts: hh3cLogInAuthenFailure.setStatus('current')
hh3cVtyMan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2))
hh3cVtyAccTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cVtyAccTable.setStatus('current')
hh3cVtyAccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1), ).setIndexNames((0, "HH3C-UI-MAN-MIB", "hh3cVtyAccUserIndex"), (0, "HH3C-UI-MAN-MIB", "hh3cVtyAccConnway"))
if mibBuilder.loadTexts: hh3cVtyAccEntry.setStatus('current')
hh3cVtyAccUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hh3cVtyAccUserIndex.setStatus('current')
hh3cVtyAccConnway = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 11, 12))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("linkinbound", 3), ("acl6inbound", 11), ("acl6outbound", 12))))
if mibBuilder.loadTexts: hh3cVtyAccConnway.setStatus('current')
hh3cVtyAccAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVtyAccAclNum.setStatus('current')
hh3cVtyAccEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVtyAccEntryRowStatus.setStatus('current')
hh3cConStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3))
hh3cConStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3, 1), )
if mibBuilder.loadTexts: hh3cConStatusTable.setStatus('current')
hh3cConStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3, 1, 1), ).setIndexNames((0, "HH3C-UI-MAN-MIB", "hh3cConUserIndex"))
if mibBuilder.loadTexts: hh3cConStatusEntry.setStatus('current')
hh3cConUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cConUserIndex.setStatus('current')
hh3cConReAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 2, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cConReAuth.setStatus('current')
hh3cUIMgtMIBConformance18 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 2))
hh3cUIMgtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 1))
hh3cUIMgtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 1, 1)).setObjects(("HH3C-UI-MAN-MIB", "hh3cUIMgtBasicGroup"), ("HH3C-UI-MAN-MIB", "hh3cConStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUIMgtMIBCompliance = hh3cUIMgtMIBCompliance.setStatus('current')
hh3cUIMgtManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 2))
hh3cUIMgtBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 2, 1)).setObjects(("HH3C-UI-MAN-MIB", "hh3cVtyAccAclNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUIMgtBasicGroup = hh3cUIMgtBasicGroup.setStatus('current')
hh3cConStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 2, 2, 2, 2)).setObjects(("HH3C-UI-MAN-MIB", "hh3cConReAuth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cConStatusGroup = hh3cConStatusGroup.setStatus('current')
mibBuilder.exportSymbols("HH3C-UI-MAN-MIB", hh3cUINotifications=hh3cUINotifications, hh3cConStatusGroup=hh3cConStatusGroup, hh3cUIMgtMIBConformance18=hh3cUIMgtMIBConformance18, hh3cConStatus=hh3cConStatus, hh3cUINotificationsPrefix=hh3cUINotificationsPrefix, hh3cUITrapBindObjects=hh3cUITrapBindObjects, hh3cLogInAuthenFailure=hh3cLogInAuthenFailure, hh3cVtyAccUserIndex=hh3cVtyAccUserIndex, hh3cUIMgt=hh3cUIMgt, hh3cVtyMan=hh3cVtyMan, hh3cTerminalUserAuthFailureReason=hh3cTerminalUserAuthFailureReason, hh3cTerminalSource=hh3cTerminalSource, hh3cConStatusTable=hh3cConStatusTable, hh3cUIMgtMIBCompliances=hh3cUIMgtMIBCompliances, hh3cConStatusEntry=hh3cConStatusEntry, hh3cLogIn=hh3cLogIn, hh3cVtyAccTable=hh3cVtyAccTable, hh3cLogOut=hh3cLogOut, hh3cUIMgtMIBCompliance=hh3cUIMgtMIBCompliance, hh3cConUserIndex=hh3cConUserIndex, hh3cUIMgtManMIBGroups=hh3cUIMgtManMIBGroups, hh3cVtyAccEntry=hh3cVtyAccEntry, hh3cUIMgtObjects=hh3cUIMgtObjects, hh3cUIMgtBasicGroup=hh3cUIMgtBasicGroup, hh3cVtyAccEntryRowStatus=hh3cVtyAccEntryRowStatus, hh3cVtyAccAclNum=hh3cVtyAccAclNum, hh3cVtyAccConnway=hh3cVtyAccConnway, PYSNMP_MODULE_ID=hh3cUIMgt, hh3cUIScalarObjects=hh3cUIScalarObjects, hh3cTerminalUserName=hh3cTerminalUserName, hh3cConReAuth=hh3cConReAuth, hh3cUIBasicInfo=hh3cUIBasicInfo)

#
# PySNMP MIB module H3C-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-USER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, ModuleIdentity, TimeTicks, Bits, Integer32, Counter32, Gauge32, Unsigned32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "TimeTicks", "Bits", "Integer32", "Counter32", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "iso")
DisplayString, RowStatus, MacAddress, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "MacAddress", "DateAndTime", "TextualConvention")
h3cUser = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12))
if mibBuilder.loadTexts: h3cUser.setLastUpdated('200304100000Z')
if mibBuilder.loadTexts: h3cUser.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

h3cUserObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1))
h3cUserInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1), )
if mibBuilder.loadTexts: h3cUserInfoTable.setStatus('current')
h3cUserInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1), ).setIndexNames((0, "H3C-USER-MIB", "h3cUserIndex"))
if mibBuilder.loadTexts: h3cUserInfoEntry.setStatus('current')
h3cUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cUserName.setStatus('current')
h3cUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cUserPassword.setStatus('current')
h3cAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cAuthMode.setStatus('current')
h3cUserLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cUserLevel.setStatus('current')
h3cUserState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("active", 0), ("block", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cUserState.setStatus('current')
h3cUserInfoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cUserInfoRowStatus.setStatus('current')
h3cUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483646)))
if mibBuilder.loadTexts: h3cUserIndex.setStatus('current')
h3cUserAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2), )
if mibBuilder.loadTexts: h3cUserAttributeTable.setStatus('current')
h3cUserAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1), ).setIndexNames((0, "H3C-USER-MIB", "h3cUserIndex"))
if mibBuilder.loadTexts: h3cUserAttributeEntry.setStatus('current')
h3cAccessLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cAccessLimit.setStatus('current')
h3cIdleCut = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIdleCut.setStatus('current')
h3cIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIPAddress.setStatus('current')
h3cNasIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cNasIPAddress.setStatus('current')
h3cSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSlotNum.setStatus('current')
h3cSubSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSubSlotNum.setStatus('current')
h3cPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPortNum.setStatus('current')
h3cMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 8), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMacAddress.setStatus('current')
h3cVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVlan.setStatus('current')
h3cFtpService = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 10), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFtpService.setStatus('current')
h3cFtpDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 11), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFtpDirectory.setStatus('current')
h3cLanAccessService = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 12), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cLanAccessService.setStatus('current')
h3cSshService = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 13), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSshService.setStatus('current')
h3cTelnetService = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 14), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cTelnetService.setStatus('current')
h3cTerminalService = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 15), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cTerminalService.setStatus('current')
h3cExpirationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 16), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cExpirationDate.setStatus('current')
h3cUserGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cUserGroup.setStatus('current')
h3cPortalService = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 18), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPortalService.setStatus('current')
h3cPPPService = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 19), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPPPService.setStatus('current')
h3cHttpService = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 20), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cHttpService.setStatus('current')
h3cHttpsService = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 21), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cHttpsService.setStatus('current')
h3cUserMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cUserMaxNum.setStatus('current')
h3cUserCurrNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cUserCurrNum.setStatus('current')
h3cUserIndexIndicator = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cUserIndexIndicator.setStatus('current')
h3cUserRoleTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 6), )
if mibBuilder.loadTexts: h3cUserRoleTable.setStatus('current')
h3cUserRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 6, 1), ).setIndexNames((0, "H3C-USER-MIB", "h3cUserIndex"), (0, "H3C-USER-MIB", "h3cUserRole"))
if mibBuilder.loadTexts: h3cUserRoleEntry.setStatus('current')
h3cUserRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: h3cUserRole.setStatus('current')
h3cUserRoleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cUserRoleStatus.setStatus('current')
h3cUserGroupObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2))
h3cUserGroupInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2, 1), )
if mibBuilder.loadTexts: h3cUserGroupInfoTable.setStatus('current')
h3cUserGroupInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2, 1, 1), ).setIndexNames((0, "H3C-USER-MIB", "h3cUserGroupName"))
if mibBuilder.loadTexts: h3cUserGroupInfoEntry.setStatus('current')
h3cUserGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80)))
if mibBuilder.loadTexts: h3cUserGroupName.setStatus('current')
h3cUserGroupInfoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cUserGroupInfoRowStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-USER-MIB", PYSNMP_MODULE_ID=h3cUser, h3cUserInfoRowStatus=h3cUserInfoRowStatus, h3cUserGroup=h3cUserGroup, ServiceType=ServiceType, h3cUserRole=h3cUserRole, h3cIPAddress=h3cIPAddress, h3cExpirationDate=h3cExpirationDate, h3cUserObjects=h3cUserObjects, h3cIdleCut=h3cIdleCut, h3cNasIPAddress=h3cNasIPAddress, h3cPortNum=h3cPortNum, h3cSubSlotNum=h3cSubSlotNum, h3cHttpsService=h3cHttpsService, h3cFtpService=h3cFtpService, h3cTelnetService=h3cTelnetService, h3cUserAttributeEntry=h3cUserAttributeEntry, h3cUserInfoEntry=h3cUserInfoEntry, h3cUserIndex=h3cUserIndex, h3cFtpDirectory=h3cFtpDirectory, h3cHttpService=h3cHttpService, h3cUserGroupInfoEntry=h3cUserGroupInfoEntry, h3cUserInfoTable=h3cUserInfoTable, h3cUserPassword=h3cUserPassword, h3cUserRoleStatus=h3cUserRoleStatus, DisplayString=DisplayString, h3cUserName=h3cUserName, h3cUserGroupInfoRowStatus=h3cUserGroupInfoRowStatus, h3cUserCurrNum=h3cUserCurrNum, h3cSshService=h3cSshService, h3cAuthMode=h3cAuthMode, h3cUserState=h3cUserState, h3cVlan=h3cVlan, h3cUserLevel=h3cUserLevel, h3cAccessLimit=h3cAccessLimit, h3cPortalService=h3cPortalService, h3cLanAccessService=h3cLanAccessService, h3cUserIndexIndicator=h3cUserIndexIndicator, h3cUserRoleEntry=h3cUserRoleEntry, h3cTerminalService=h3cTerminalService, h3cSlotNum=h3cSlotNum, h3cMacAddress=h3cMacAddress, h3cUserAttributeTable=h3cUserAttributeTable, h3cUserGroupObjects=h3cUserGroupObjects, h3cUser=h3cUser, h3cUserGroupInfoTable=h3cUserGroupInfoTable, h3cPPPService=h3cPPPService, h3cUserMaxNum=h3cUserMaxNum, h3cUserGroupName=h3cUserGroupName, h3cUserRoleTable=h3cUserRoleTable)

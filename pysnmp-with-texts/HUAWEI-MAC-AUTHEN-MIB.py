#
# PySNMP MIB module HUAWEI-MAC-AUTHEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MAC-AUTHEN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:46:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifDescr, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifDescr", "InterfaceIndexOrZero")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
VlanIdOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, Unsigned32, NotificationType, MibIdentifier, IpAddress, TimeTicks, ObjectIdentity, Gauge32, Counter64, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "ObjectIdentity", "Gauge32", "Counter64", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity")
MacAddress, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "RowStatus")
hwMacAuthenMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171))
hwMacAuthenMIB.setRevisions(('2009-12-15 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwMacAuthenMIB.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hwMacAuthenMIB.setLastUpdated('200912151800Z')
if mibBuilder.loadTexts: hwMacAuthenMIB.setOrganization('Huawei Technologies co., Ltd.')
if mibBuilder.loadTexts: hwMacAuthenMIB.setContactInfo(' R&D NanJing, Huawei Technologies co.,Ltd. Huihong Bld.,NO.91 Baixia Rd., Bai-Xia District NanJing P.R. China Zip:210001 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwMacAuthenMIB.setDescription('This MIB describes objects used for mac-authentication,including configuring mac-authentication.')
hwMacAuthenObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1))
hwMacAuthenGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenGlobalEnable.setDescription('The Global MAC authenticate. Enable this before you want to enable other interfaces MAC authentication. ')
hwMacAuthenModeUsername = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("macAddressWithoutHyphen", 1), ("macAddressWithHyphen", 2), ("fixed", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenModeUsername.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenModeUsername.setDescription('Specify MAC authentication mode config.')
hwMacAuthenPassword = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenPassword.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenPassword.setDescription('Special the fixed password. ')
hwMacAuthenUsername = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenUsername.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenUsername.setDescription('Special the fixed username. ')
hwMacAuthenDomain = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenDomain.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenDomain.setDescription('Specify domain server configuration. ')
hwMacAuthenTimerOfflineDetect = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 7200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenTimerOfflineDetect.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenTimerOfflineDetect.setDescription('Specify timer configuration.')
hwMacAuthenTimerQuiet = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenTimerQuiet.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenTimerQuiet.setDescription('Specify timer configuration.')
hwMacAuthenTimerServerTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenTimerServerTimeout.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenTimerServerTimeout.setDescription('Specify timer configuration.')
hwMacAuthenReauthInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenReauthInterval.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenReauthInterval.setDescription('Specify timer configuration of guest vlan reauthentication. ')
hwMacAuthenCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10), )
if mibBuilder.loadTexts: hwMacAuthenCfgTable.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenCfgTable.setDescription('The MAC authentication configuration table.')
hwMacAuthenCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1), ).setIndexNames((0, "HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortIndex"))
if mibBuilder.loadTexts: hwMacAuthenCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenCfgEntry.setDescription('An entry in the MAC authentication configuration table.')
hwMacAuthenPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1280)))
if mibBuilder.loadTexts: hwMacAuthenPortIndex.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenPortIndex.setDescription('The Index of L2-Switch Interface.')
hwMacAuthenPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 2), EnabledStatus().clone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMacAuthenPortEnable.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenPortEnable.setDescription(' Whether to enable MAC authentication on this interface.')
hwMacAuthenGuestVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 3), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMacAuthenGuestVlan.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenGuestVlan.setDescription(' Specify guest vlan configuration information for ports.')
hwMacAuthenMaxUserNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192)).clone(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMacAuthenMaxUserNum.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenMaxUserNum.setDescription('The max number of users. ')
hwMacAuthenPortDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenPortDomain.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenPortDomain.setDescription('Specify domain server configuration for ports.')
hwMacAuthenPortModeUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("obeyGlobalConfiguration", 1), ("macAddressWithoutHyphen", 2), ("macAddressWithHyphen", 3), ("fixed", 4))).clone('obeyGlobalConfiguration')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenPortModeUserName.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenPortModeUserName.setDescription('Specify MAC authentication mode config for ports.')
hwMacAuthenPortUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenPortUserName.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenPortUserName.setDescription('Special the fixed username for ports.')
hwMacAuthenPortPassWord = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenPortPassWord.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenPortPassWord.setDescription('Special the fixed password for ports.')
hwMacAuthenPortPwdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2))).clone('simple')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenPortPwdType.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenPortPwdType.setDescription('The type of port password. ')
hwMacAuthenPwdType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMacAuthenPwdType.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenPwdType.setDescription('The type of global password. ')
hwMacAuthenMibTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 2))
hwMacAuthenMaxUserAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 2, 1)).setObjects(("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hwMacAuthenMaxUserAlarm.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenMaxUserAlarm.setDescription('The number of ahthenticate users is reached the max number. ')
hwMacAuthenConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3))
hwMacAuthenCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 1))
hwMacAuthenCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 1, 1)).setObjects(("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMacAuthenCompliance = hwMacAuthenCompliance.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenCompliance.setDescription('The compliance statement for systems supporting this module.')
hwMacAuthenCfgGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 2))
hwMacAuthenCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 2, 1)).setObjects(("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenGlobalEnable"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenModeUsername"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPassword"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenUsername"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenDomain"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenTimerOfflineDetect"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenTimerQuiet"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenTimerServerTimeout"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenReauthInterval"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortEnable"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenGuestVlan"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenMaxUserNum"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortDomain"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortModeUserName"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortUserName"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortPassWord"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortPwdType"), ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPwdType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMacAuthenCfgGroup = hwMacAuthenCfgGroup.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenCfgGroup.setDescription("The mac-authen's Configuration group.")
hwMacAuthenTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 2, 2)).setObjects(("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenMaxUserAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMacAuthenTrapGroup = hwMacAuthenTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwMacAuthenTrapGroup.setDescription("The mac-authen's Notification group.")
mibBuilder.exportSymbols("HUAWEI-MAC-AUTHEN-MIB", hwMacAuthenPortUserName=hwMacAuthenPortUserName, hwMacAuthenTrapGroup=hwMacAuthenTrapGroup, hwMacAuthenTimerOfflineDetect=hwMacAuthenTimerOfflineDetect, hwMacAuthenObjects=hwMacAuthenObjects, hwMacAuthenPwdType=hwMacAuthenPwdType, PYSNMP_MODULE_ID=hwMacAuthenMIB, hwMacAuthenTimerServerTimeout=hwMacAuthenTimerServerTimeout, hwMacAuthenPortIndex=hwMacAuthenPortIndex, hwMacAuthenPortPassWord=hwMacAuthenPortPassWord, hwMacAuthenCfgTable=hwMacAuthenCfgTable, hwMacAuthenTimerQuiet=hwMacAuthenTimerQuiet, hwMacAuthenCompliances=hwMacAuthenCompliances, hwMacAuthenDomain=hwMacAuthenDomain, hwMacAuthenCfgEntry=hwMacAuthenCfgEntry, hwMacAuthenUsername=hwMacAuthenUsername, hwMacAuthenReauthInterval=hwMacAuthenReauthInterval, hwMacAuthenPortModeUserName=hwMacAuthenPortModeUserName, hwMacAuthenPassword=hwMacAuthenPassword, hwMacAuthenGuestVlan=hwMacAuthenGuestVlan, hwMacAuthenMibTraps=hwMacAuthenMibTraps, hwMacAuthenCfgGroup=hwMacAuthenCfgGroup, hwMacAuthenMaxUserAlarm=hwMacAuthenMaxUserAlarm, hwMacAuthenModeUsername=hwMacAuthenModeUsername, hwMacAuthenPortPwdType=hwMacAuthenPortPwdType, hwMacAuthenPortEnable=hwMacAuthenPortEnable, hwMacAuthenConformance=hwMacAuthenConformance, hwMacAuthenCompliance=hwMacAuthenCompliance, hwMacAuthenMIB=hwMacAuthenMIB, hwMacAuthenMaxUserNum=hwMacAuthenMaxUserNum, hwMacAuthenGlobalEnable=hwMacAuthenGlobalEnable, hwMacAuthenCfgGroups=hwMacAuthenCfgGroups, hwMacAuthenPortDomain=hwMacAuthenPortDomain)
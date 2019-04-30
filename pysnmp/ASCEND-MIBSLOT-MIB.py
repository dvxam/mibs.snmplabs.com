#
# PySNMP MIB module ASCEND-MIBSLOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSLOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, ObjectIdentity, NotificationType, Integer32, Unsigned32, Counter64, Gauge32, TimeTicks, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "ObjectIdentity", "NotificationType", "Integer32", "Unsigned32", "Counter64", "Gauge32", "TimeTicks", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibtcpModemProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 112))
mibdhcpServerProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 111))
mibappOptionsProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 109))
mibdnisProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 113))
mibwanOptionsProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 110))
mibtcpModemProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 112, 1), )
if mibBuilder.loadTexts: mibtcpModemProfileTable.setStatus('mandatory')
mibtcpModemProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1), ).setIndexNames((0, "ASCEND-MIBSLOT-MIB", "tcpModemProfile-Index-o"))
if mibBuilder.loadTexts: mibtcpModemProfileEntry.setStatus('mandatory')
tcpModemProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1, 1), Integer32()).setLabel("tcpModemProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpModemProfile_Index_o.setStatus('mandatory')
tcpModemProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("tcpModemProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpModemProfile_Enabled.setStatus('mandatory')
tcpModemProfile_Port = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1, 3), Integer32()).setLabel("tcpModemProfile-Port").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpModemProfile_Port.setStatus('mandatory')
tcpModemProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("tcpModemProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpModemProfile_Action_o.setStatus('mandatory')
mibdhcpServerProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 111, 1), )
if mibBuilder.loadTexts: mibdhcpServerProfileTable.setStatus('mandatory')
mibdhcpServerProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1), ).setIndexNames((0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-Index-o"))
if mibBuilder.loadTexts: mibdhcpServerProfileEntry.setStatus('mandatory')
dhcpServerProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 1), Integer32()).setLabel("dhcpServerProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerProfile_Index_o.setStatus('mandatory')
dhcpServerProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dhcpServerProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_Enabled.setStatus('mandatory')
dhcpServerProfile_PnpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dhcpServerProfile-PnpEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_PnpEnabled.setStatus('mandatory')
dhcpServerProfile_IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 4), IpAddress()).setLabel("dhcpServerProfile-IpAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_IpAddress.setStatus('mandatory')
dhcpServerProfile_Netmask = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 5), IpAddress()).setLabel("dhcpServerProfile-Netmask").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_Netmask.setStatus('mandatory')
dhcpServerProfile_RenewalTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 6), Integer32()).setLabel("dhcpServerProfile-RenewalTime").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_RenewalTime.setStatus('mandatory')
dhcpServerProfile_BecomeDefRouter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dhcpServerProfile-BecomeDefRouter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_BecomeDefRouter.setStatus('mandatory')
dhcpServerProfile_DialIfLinkDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dhcpServerProfile-DialIfLinkDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_DialIfLinkDown.setStatus('mandatory')
dhcpServerProfile_AlwaysSpoof = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dhcpServerProfile-AlwaysSpoof").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_AlwaysSpoof.setStatus('mandatory')
dhcpServerProfile_ValidateIp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dhcpServerProfile-ValidateIp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_ValidateIp.setStatus('mandatory')
dhcpServerProfile_MaxNoReplyWait = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 11), Integer32()).setLabel("dhcpServerProfile-MaxNoReplyWait").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_MaxNoReplyWait.setStatus('mandatory')
dhcpServerProfile_GroupOneCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 12), Integer32()).setLabel("dhcpServerProfile-GroupOneCount").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_GroupOneCount.setStatus('mandatory')
dhcpServerProfile_IpGroupTwo = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 13), IpAddress()).setLabel("dhcpServerProfile-IpGroupTwo").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_IpGroupTwo.setStatus('mandatory')
dhcpServerProfile_GroupTwoCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 14), Integer32()).setLabel("dhcpServerProfile-GroupTwoCount").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_GroupTwoCount.setStatus('mandatory')
dhcpServerProfile_IpGroupTwoNetmask = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 15), IpAddress()).setLabel("dhcpServerProfile-IpGroupTwoNetmask").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_IpGroupTwoNetmask.setStatus('mandatory')
dhcpServerProfile_TftpHost = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 16), DisplayString()).setLabel("dhcpServerProfile-TftpHost").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_TftpHost.setStatus('mandatory')
dhcpServerProfile_BootpPath = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 17), DisplayString()).setLabel("dhcpServerProfile-BootpPath").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_BootpPath.setStatus('mandatory')
dhcpServerProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("dhcpServerProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_Action_o.setStatus('mandatory')
mibdhcpServerProfile_HostAddrTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 111, 2), ).setLabel("mibdhcpServerProfile-HostAddrTable")
if mibBuilder.loadTexts: mibdhcpServerProfile_HostAddrTable.setStatus('mandatory')
mibdhcpServerProfile_HostAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 111, 2, 1), ).setLabel("mibdhcpServerProfile-HostAddrEntry").setIndexNames((0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostAddr-Index-o"), (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostAddr-Index1-o"))
if mibBuilder.loadTexts: mibdhcpServerProfile_HostAddrEntry.setStatus('mandatory')
dhcpServerProfile_HostAddr_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 2, 1, 1), Integer32()).setLabel("dhcpServerProfile-HostAddr-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerProfile_HostAddr_Index_o.setStatus('mandatory')
dhcpServerProfile_HostAddr_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 2, 1, 2), Integer32()).setLabel("dhcpServerProfile-HostAddr-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerProfile_HostAddr_Index1_o.setStatus('mandatory')
dhcpServerProfile_HostAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 2, 1, 3), DisplayString()).setLabel("dhcpServerProfile-HostAddr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_HostAddr.setStatus('mandatory')
mibdhcpServerProfile_HostNetmaskTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 111, 3), ).setLabel("mibdhcpServerProfile-HostNetmaskTable")
if mibBuilder.loadTexts: mibdhcpServerProfile_HostNetmaskTable.setStatus('mandatory')
mibdhcpServerProfile_HostNetmaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 111, 3, 1), ).setLabel("mibdhcpServerProfile-HostNetmaskEntry").setIndexNames((0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostNetmask-Index-o"), (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostNetmask-Index1-o"))
if mibBuilder.loadTexts: mibdhcpServerProfile_HostNetmaskEntry.setStatus('mandatory')
dhcpServerProfile_HostNetmask_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 3, 1, 1), Integer32()).setLabel("dhcpServerProfile-HostNetmask-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerProfile_HostNetmask_Index_o.setStatus('mandatory')
dhcpServerProfile_HostNetmask_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 3, 1, 2), Integer32()).setLabel("dhcpServerProfile-HostNetmask-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerProfile_HostNetmask_Index1_o.setStatus('mandatory')
dhcpServerProfile_HostNetmask = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 3, 1, 3), IpAddress()).setLabel("dhcpServerProfile-HostNetmask").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_HostNetmask.setStatus('mandatory')
mibdhcpServerProfile_HostIpTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 111, 4), ).setLabel("mibdhcpServerProfile-HostIpTable")
if mibBuilder.loadTexts: mibdhcpServerProfile_HostIpTable.setStatus('mandatory')
mibdhcpServerProfile_HostIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 111, 4, 1), ).setLabel("mibdhcpServerProfile-HostIpEntry").setIndexNames((0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostIp-Index-o"), (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostIp-Index1-o"))
if mibBuilder.loadTexts: mibdhcpServerProfile_HostIpEntry.setStatus('mandatory')
dhcpServerProfile_HostIp_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 4, 1, 1), Integer32()).setLabel("dhcpServerProfile-HostIp-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerProfile_HostIp_Index_o.setStatus('mandatory')
dhcpServerProfile_HostIp_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 4, 1, 2), Integer32()).setLabel("dhcpServerProfile-HostIp-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerProfile_HostIp_Index1_o.setStatus('mandatory')
dhcpServerProfile_HostIp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 111, 4, 1, 3), IpAddress()).setLabel("dhcpServerProfile-HostIp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpServerProfile_HostIp.setStatus('mandatory')
mibappOptionsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 109, 1), )
if mibBuilder.loadTexts: mibappOptionsProfileTable.setStatus('mandatory')
mibappOptionsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1), ).setIndexNames((0, "ASCEND-MIBSLOT-MIB", "appOptionsProfile-Index-o"))
if mibBuilder.loadTexts: mibappOptionsProfileEntry.setStatus('mandatory')
appOptionsProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 1), Integer32()).setLabel("appOptionsProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: appOptionsProfile_Index_o.setStatus('mandatory')
appOptionsProfile_PwsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("appOptionsProfile-PwsEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: appOptionsProfile_PwsEnabled.setStatus('mandatory')
appOptionsProfile_PwsHost = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 3), IpAddress()).setLabel("appOptionsProfile-PwsHost").setMaxAccess("readwrite")
if mibBuilder.loadTexts: appOptionsProfile_PwsHost.setStatus('mandatory')
appOptionsProfile_PwsPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 4), Integer32()).setLabel("appOptionsProfile-PwsPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: appOptionsProfile_PwsPort.setStatus('mandatory')
appOptionsProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("appOptionsProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: appOptionsProfile_Action_o.setStatus('mandatory')
mibdnisProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 113, 1), )
if mibBuilder.loadTexts: mibdnisProfileTable.setStatus('mandatory')
mibdnisProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 113, 1, 1), ).setIndexNames((0, "ASCEND-MIBSLOT-MIB", "dnisProfile-Index-o"))
if mibBuilder.loadTexts: mibdnisProfileEntry.setStatus('mandatory')
dnisProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 1, 1, 1), Integer32()).setLabel("dnisProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dnisProfile_Index_o.setStatus('mandatory')
dnisProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dnisProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnisProfile_Enabled.setStatus('mandatory')
dnisProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("dnisProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnisProfile_Action_o.setStatus('mandatory')
mibdnisProfile_DnisTabTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 113, 2), ).setLabel("mibdnisProfile-DnisTabTable")
if mibBuilder.loadTexts: mibdnisProfile_DnisTabTable.setStatus('mandatory')
mibdnisProfile_DnisTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1), ).setLabel("mibdnisProfile-DnisTabEntry").setIndexNames((0, "ASCEND-MIBSLOT-MIB", "dnisProfile-DnisTab-Index-o"), (0, "ASCEND-MIBSLOT-MIB", "dnisProfile-DnisTab-Index1-o"))
if mibBuilder.loadTexts: mibdnisProfile_DnisTabEntry.setStatus('mandatory')
dnisProfile_DnisTab_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 1), Integer32()).setLabel("dnisProfile-DnisTab-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dnisProfile_DnisTab_Index_o.setStatus('mandatory')
dnisProfile_DnisTab_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 2), Integer32()).setLabel("dnisProfile-DnisTab-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dnisProfile_DnisTab_Index1_o.setStatus('mandatory')
dnisProfile_DnisTab_DnisNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 3), DisplayString()).setLabel("dnisProfile-DnisTab-DnisNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnisProfile_DnisTab_DnisNumber.setStatus('mandatory')
dnisProfile_DnisTab_DnisMaxCalls = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 4), Integer32()).setLabel("dnisProfile-DnisTab-DnisMaxCalls").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnisProfile_DnisTab_DnisMaxCalls.setStatus('mandatory')
dnisProfile_DnisTab_DnisMaxCallsModem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 5), Integer32()).setLabel("dnisProfile-DnisTab-DnisMaxCallsModem").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnisProfile_DnisTab_DnisMaxCallsModem.setStatus('mandatory')
dnisProfile_DnisTab_DnisMaxCallsHdlc = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 6), Integer32()).setLabel("dnisProfile-DnisTab-DnisMaxCallsHdlc").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnisProfile_DnisTab_DnisMaxCallsHdlc.setStatus('mandatory')
dnisProfile_DnisTab_DnisMaxCallsV110 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 7), Integer32()).setLabel("dnisProfile-DnisTab-DnisMaxCallsV110").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnisProfile_DnisTab_DnisMaxCallsV110.setStatus('mandatory')
mibwanOptionsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 110, 1), )
if mibBuilder.loadTexts: mibwanOptionsProfileTable.setStatus('mandatory')
mibwanOptionsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1), ).setIndexNames((0, "ASCEND-MIBSLOT-MIB", "wanOptionsProfile-Index-o"))
if mibBuilder.loadTexts: mibwanOptionsProfileEntry.setStatus('mandatory')
wanOptionsProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 1), Integer32()).setLabel("wanOptionsProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: wanOptionsProfile_Index_o.setStatus('mandatory')
wanOptionsProfile_DialPlan = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 2), Integer32()).setLabel("wanOptionsProfile-DialPlan").setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanOptionsProfile_DialPlan.setStatus('mandatory')
wanOptionsProfile_TrunkGroupsNa = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("wanOptionsProfile-TrunkGroupsNa").setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanOptionsProfile_TrunkGroupsNa.setStatus('mandatory')
wanOptionsProfile_RingBack = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("wanOptionsProfile-RingBack").setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanOptionsProfile_RingBack.setStatus('mandatory')
wanOptionsProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("wanOptionsProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanOptionsProfile_Action_o.setStatus('mandatory')
mibwanOptionsProfile_EtherAnsNumberTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 110, 2), ).setLabel("mibwanOptionsProfile-EtherAnsNumberTable")
if mibBuilder.loadTexts: mibwanOptionsProfile_EtherAnsNumberTable.setStatus('mandatory')
mibwanOptionsProfile_EtherAnsNumberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 110, 2, 1), ).setLabel("mibwanOptionsProfile-EtherAnsNumberEntry").setIndexNames((0, "ASCEND-MIBSLOT-MIB", "wanOptionsProfile-EtherAnsNumber-Index-o"), (0, "ASCEND-MIBSLOT-MIB", "wanOptionsProfile-EtherAnsNumber-Index1-o"))
if mibBuilder.loadTexts: mibwanOptionsProfile_EtherAnsNumberEntry.setStatus('mandatory')
wanOptionsProfile_EtherAnsNumber_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 110, 2, 1, 1), Integer32()).setLabel("wanOptionsProfile-EtherAnsNumber-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: wanOptionsProfile_EtherAnsNumber_Index_o.setStatus('mandatory')
wanOptionsProfile_EtherAnsNumber_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 110, 2, 1, 2), Integer32()).setLabel("wanOptionsProfile-EtherAnsNumber-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: wanOptionsProfile_EtherAnsNumber_Index1_o.setStatus('mandatory')
wanOptionsProfile_EtherAnsNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 110, 2, 1, 3), DisplayString()).setLabel("wanOptionsProfile-EtherAnsNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanOptionsProfile_EtherAnsNumber.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBSLOT-MIB", mibdhcpServerProfile_HostAddrTable=mibdhcpServerProfile_HostAddrTable, dhcpServerProfile_AlwaysSpoof=dhcpServerProfile_AlwaysSpoof, dhcpServerProfile_DialIfLinkDown=dhcpServerProfile_DialIfLinkDown, mibwanOptionsProfileTable=mibwanOptionsProfileTable, dnisProfile_DnisTab_DnisMaxCallsV110=dnisProfile_DnisTab_DnisMaxCallsV110, mibdnisProfileEntry=mibdnisProfileEntry, dhcpServerProfile_Netmask=dhcpServerProfile_Netmask, mibdnisProfile=mibdnisProfile, dnisProfile_Index_o=dnisProfile_Index_o, dhcpServerProfile_IpGroupTwoNetmask=dhcpServerProfile_IpGroupTwoNetmask, dnisProfile_Enabled=dnisProfile_Enabled, dnisProfile_DnisTab_Index_o=dnisProfile_DnisTab_Index_o, mibappOptionsProfileTable=mibappOptionsProfileTable, wanOptionsProfile_TrunkGroupsNa=wanOptionsProfile_TrunkGroupsNa, wanOptionsProfile_Index_o=wanOptionsProfile_Index_o, dhcpServerProfile_BootpPath=dhcpServerProfile_BootpPath, mibwanOptionsProfile=mibwanOptionsProfile, appOptionsProfile_Index_o=appOptionsProfile_Index_o, tcpModemProfile_Enabled=tcpModemProfile_Enabled, dnisProfile_DnisTab_DnisNumber=dnisProfile_DnisTab_DnisNumber, dhcpServerProfile_HostNetmask_Index_o=dhcpServerProfile_HostNetmask_Index_o, dhcpServerProfile_GroupTwoCount=dhcpServerProfile_GroupTwoCount, appOptionsProfile_Action_o=appOptionsProfile_Action_o, dnisProfile_DnisTab_Index1_o=dnisProfile_DnisTab_Index1_o, dhcpServerProfile_IpGroupTwo=dhcpServerProfile_IpGroupTwo, dhcpServerProfile_HostIp_Index_o=dhcpServerProfile_HostIp_Index_o, dhcpServerProfile_IpAddress=dhcpServerProfile_IpAddress, appOptionsProfile_PwsHost=appOptionsProfile_PwsHost, mibtcpModemProfileTable=mibtcpModemProfileTable, dnisProfile_DnisTab_DnisMaxCallsModem=dnisProfile_DnisTab_DnisMaxCallsModem, wanOptionsProfile_DialPlan=wanOptionsProfile_DialPlan, mibwanOptionsProfile_EtherAnsNumberEntry=mibwanOptionsProfile_EtherAnsNumberEntry, dhcpServerProfile_HostAddr=dhcpServerProfile_HostAddr, tcpModemProfile_Port=tcpModemProfile_Port, wanOptionsProfile_Action_o=wanOptionsProfile_Action_o, mibwanOptionsProfile_EtherAnsNumberTable=mibwanOptionsProfile_EtherAnsNumberTable, dhcpServerProfile_HostNetmask_Index1_o=dhcpServerProfile_HostNetmask_Index1_o, mibdnisProfileTable=mibdnisProfileTable, mibdhcpServerProfile_HostNetmaskEntry=mibdhcpServerProfile_HostNetmaskEntry, dhcpServerProfile_ValidateIp=dhcpServerProfile_ValidateIp, dhcpServerProfile_Enabled=dhcpServerProfile_Enabled, mibdhcpServerProfile_HostAddrEntry=mibdhcpServerProfile_HostAddrEntry, mibdhcpServerProfile_HostIpEntry=mibdhcpServerProfile_HostIpEntry, mibdhcpServerProfile_HostNetmaskTable=mibdhcpServerProfile_HostNetmaskTable, dhcpServerProfile_TftpHost=dhcpServerProfile_TftpHost, mibdnisProfile_DnisTabEntry=mibdnisProfile_DnisTabEntry, dhcpServerProfile_GroupOneCount=dhcpServerProfile_GroupOneCount, dhcpServerProfile_HostIp=dhcpServerProfile_HostIp, wanOptionsProfile_RingBack=wanOptionsProfile_RingBack, wanOptionsProfile_EtherAnsNumber_Index1_o=wanOptionsProfile_EtherAnsNumber_Index1_o, mibappOptionsProfileEntry=mibappOptionsProfileEntry, mibdhcpServerProfile_HostIpTable=mibdhcpServerProfile_HostIpTable, mibdnisProfile_DnisTabTable=mibdnisProfile_DnisTabTable, dhcpServerProfile_HostAddr_Index1_o=dhcpServerProfile_HostAddr_Index1_o, dhcpServerProfile_RenewalTime=dhcpServerProfile_RenewalTime, wanOptionsProfile_EtherAnsNumber_Index_o=wanOptionsProfile_EtherAnsNumber_Index_o, wanOptionsProfile_EtherAnsNumber=wanOptionsProfile_EtherAnsNumber, mibwanOptionsProfileEntry=mibwanOptionsProfileEntry, mibdhcpServerProfileTable=mibdhcpServerProfileTable, dhcpServerProfile_MaxNoReplyWait=dhcpServerProfile_MaxNoReplyWait, tcpModemProfile_Action_o=tcpModemProfile_Action_o, mibtcpModemProfileEntry=mibtcpModemProfileEntry, mibtcpModemProfile=mibtcpModemProfile, dhcpServerProfile_PnpEnabled=dhcpServerProfile_PnpEnabled, dhcpServerProfile_HostIp_Index1_o=dhcpServerProfile_HostIp_Index1_o, dhcpServerProfile_Action_o=dhcpServerProfile_Action_o, dhcpServerProfile_HostAddr_Index_o=dhcpServerProfile_HostAddr_Index_o, dnisProfile_DnisTab_DnisMaxCalls=dnisProfile_DnisTab_DnisMaxCalls, mibdhcpServerProfile=mibdhcpServerProfile, mibappOptionsProfile=mibappOptionsProfile, dhcpServerProfile_HostNetmask=dhcpServerProfile_HostNetmask, tcpModemProfile_Index_o=tcpModemProfile_Index_o, appOptionsProfile_PwsPort=appOptionsProfile_PwsPort, appOptionsProfile_PwsEnabled=appOptionsProfile_PwsEnabled, mibdhcpServerProfileEntry=mibdhcpServerProfileEntry, dhcpServerProfile_BecomeDefRouter=dhcpServerProfile_BecomeDefRouter, dnisProfile_DnisTab_DnisMaxCallsHdlc=dnisProfile_DnisTab_DnisMaxCallsHdlc, dhcpServerProfile_Index_o=dhcpServerProfile_Index_o, DisplayString=DisplayString, dnisProfile_Action_o=dnisProfile_Action_o)

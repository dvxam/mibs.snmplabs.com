#
# PySNMP MIB module STATIC-MAC-BASED-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STATIC-MAC-BASED-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Counter64, ObjectIdentity, IpAddress, Integer32, Counter32, NotificationType, Unsigned32, MibIdentifier, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "Counter32", "NotificationType", "Unsigned32", "MibIdentifier", "Gauge32", "TimeTicks")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
swSMBVMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 56))
if mibBuilder.loadTexts: swSMBVMIB.setLastUpdated('0901160000Z')
if mibBuilder.loadTexts: swSMBVMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swSMBVMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swSMBVMIB.setDescription('The structure of static MAC-based VLAN information for the proprietary enterprise.')
swSmbvCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 56, 1))
swSmbvInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 56, 2))
swSmbvMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 56, 3))
swStaticMacBasedVlanCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1), )
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlTable.setStatus('obsolete')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlTable.setDescription('A table that contains static MAC-based VLAN information.')
swStaticMacBasedVlanCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1, 1), ).setIndexNames((0, "STATIC-MAC-BASED-VLAN-MIB", "swStaticMacBasedVlanCtrlMacAddr"))
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlEntry.setStatus('obsolete')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlEntry.setDescription('A list that contains static MAC-based VLAN entries.')
swStaticMacBasedVlanCtrlMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlMacAddr.setStatus('obsolete')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlMacAddr.setDescription('This object indicates the MAC address.')
swStaticMacBasedVlanCtrlVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlVlanName.setStatus('obsolete')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlVlanName.setDescription('This object indicates the VLAN name associated with the VLAN ID.')
swStaticMacBasedVlanCtrlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlStatus.setStatus('obsolete')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlStatus.setDescription('This object indicates the status of this entry.')
swStaticMacBasedVlanCtrlOptionTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2), )
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionTable.setStatus('current')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionTable.setDescription('This table is an upgrade of the swStaticMacBasedVlanCtrlTable because the index of a special MAC-based VLAN entry has changed and so has the compatibility. A table that contains static MAC-based VLAN information.')
swStaticMacBasedVlanCtrlOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1), ).setIndexNames((0, "STATIC-MAC-BASED-VLAN-MIB", "swStaticMacBasedVlanCtrlOptionMacAddr"), (0, "STATIC-MAC-BASED-VLAN-MIB", "swStaticMacBasedOptionVlanID"))
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionEntry.setStatus('current')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionEntry.setDescription('A list that contains static MAC-based VLAN entries.')
swStaticMacBasedVlanCtrlOptionMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionMacAddr.setStatus('current')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionMacAddr.setDescription('This object indicates the MAC address.')
swStaticMacBasedOptionVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swStaticMacBasedOptionVlanID.setStatus('current')
if mibBuilder.loadTexts: swStaticMacBasedOptionVlanID.setDescription('This object indicates the VLAN ID associated with the mac address.')
swStaticMacBasedVlanCtrlOptionType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("static", 1), ("mac-based-access-control", 2), ("ieee8021x", 3), ("wac", 4), ("jwac", 5), ("multiple-authentication", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionType.setStatus('current')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionType.setDescription('This object indicates the type of special MAC-based VLAN entry.')
swStaticMacBasedVlanCtrlOptionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionStatus.setStatus('current')
if mibBuilder.loadTexts: swStaticMacBasedVlanCtrlOptionStatus.setDescription('This object indicates the status of this entry.')
mibBuilder.exportSymbols("STATIC-MAC-BASED-VLAN-MIB", swStaticMacBasedOptionVlanID=swStaticMacBasedOptionVlanID, swSMBVMIB=swSMBVMIB, swStaticMacBasedVlanCtrlOptionStatus=swStaticMacBasedVlanCtrlOptionStatus, swStaticMacBasedVlanCtrlTable=swStaticMacBasedVlanCtrlTable, swStaticMacBasedVlanCtrlVlanName=swStaticMacBasedVlanCtrlVlanName, swStaticMacBasedVlanCtrlOptionType=swStaticMacBasedVlanCtrlOptionType, swStaticMacBasedVlanCtrlOptionEntry=swStaticMacBasedVlanCtrlOptionEntry, swSmbvInfo=swSmbvInfo, swStaticMacBasedVlanCtrlOptionMacAddr=swStaticMacBasedVlanCtrlOptionMacAddr, swStaticMacBasedVlanCtrlMacAddr=swStaticMacBasedVlanCtrlMacAddr, PYSNMP_MODULE_ID=swSMBVMIB, swStaticMacBasedVlanCtrlEntry=swStaticMacBasedVlanCtrlEntry, swStaticMacBasedVlanCtrlStatus=swStaticMacBasedVlanCtrlStatus, swSmbvMgmt=swSmbvMgmt, swStaticMacBasedVlanCtrlOptionTable=swStaticMacBasedVlanCtrlOptionTable, swSmbvCtrl=swSmbvCtrl)

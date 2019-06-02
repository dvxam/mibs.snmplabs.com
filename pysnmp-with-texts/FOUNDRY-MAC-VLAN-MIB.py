#
# PySNMP MIB module FOUNDRY-MAC-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-MAC-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:15:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Counter64, Unsigned32, ModuleIdentity, MibIdentifier, iso, TimeTicks, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Counter64", "Unsigned32", "ModuleIdentity", "MibIdentifier", "iso", "TimeTicks", "Counter32", "Bits")
DisplayString, TextualConvention, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress", "RowStatus")
fdryMacVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32))
fdryMacVlanMIB.setRevisions(('2010-06-02 00:00', '2008-12-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fdryMacVlanMIB.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', 'Replaces earlier snMacVlan MIB.',))
if mibBuilder.loadTexts: fdryMacVlanMIB.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: fdryMacVlanMIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: fdryMacVlanMIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: fdryMacVlanMIB.setDescription("Management Information Base module for MAC-based VLAN configuration and statistics. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
fdryMacVlanGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 1))
fdryMacVlanTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2))
fdryMacVlanGlobalClearOper = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryMacVlanGlobalClearOper.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanGlobalClearOper.setDescription('valid(0) - this value is always returned when the variable is read. clear(1) - setting the variable to this value clears the operational MAC-based VLAN information for all ports.')
fdryMacVlanGlobalDynConfigState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryMacVlanGlobalDynConfigState.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanGlobalDynConfigState.setDescription('Enable/disable MAC-based VLAN dynamic activation on the global level.')
fdryMacVlanPortMemberTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1), )
if mibBuilder.loadTexts: fdryMacVlanPortMemberTable.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanPortMemberTable.setDescription('MAC-based VLAN port membership table.')
fdryMacVlanPortMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacVlanPortMemberVLanId"), (0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacVlanPortMemberPortId"))
if mibBuilder.loadTexts: fdryMacVlanPortMemberEntry.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanPortMemberEntry.setDescription('An entry of the MAC-based VLAN port membership table.')
fdryMacVlanPortMemberVLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: fdryMacVlanPortMemberVLanId.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanPortMemberVLanId.setDescription('The VLAN identifier (VLAN ID).')
fdryMacVlanPortMemberPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: fdryMacVlanPortMemberPortId.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanPortMemberPortId.setDescription('The ifIndex of the port which is a member of the MAC-based VLAN.')
fdryMacVlanPortMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryMacVlanPortMemberRowStatus.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanPortMemberRowStatus.setDescription('This object is used to create and delete rows in the table.')
fdryMacVlanIfTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2), )
if mibBuilder.loadTexts: fdryMacVlanIfTable.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanIfTable.setDescription('MAC-based VLAN Interface table.')
fdryMacVlanIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1), ).setIndexNames((0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacVlanIfIndex"))
if mibBuilder.loadTexts: fdryMacVlanIfEntry.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanIfEntry.setDescription('An entry in the MAC-based VLAN interface table.')
fdryMacVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: fdryMacVlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanIfIndex.setDescription('The ifIndex of the interface which is a member of the MAC-based VLAN.')
fdryMacVlanIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryMacVlanIfEnable.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanIfEnable.setDescription('The administrative status requested by management for MAC-based VLANs on this interface. The value enabled(1) indicates that MAC-based VLANs should be enabled on this interface, When disabled(2), MAC-based VLANs are disabled on this interface. Enable/disable MAC-based VLAN on this interface.')
fdryMacVlanIfMaxEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 32)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryMacVlanIfMaxEntry.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanIfMaxEntry.setDescription('The maximum number of allowed and denied MAC address (static and dynamic) that can be leared on this interface. The default value is 2. The value should be between 2 to 32.')
fdryMacVlanIfClearOper = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryMacVlanIfClearOper.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanIfClearOper.setDescription('valid(0) - this value is always returned when the variable is read. clear(1) - setting the variable to this value clears the operational MAC-based VLAN information for a port.')
fdryMacVlanIfClearConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryMacVlanIfClearConfig.setStatus('current')
if mibBuilder.loadTexts: fdryMacVlanIfClearConfig.setDescription('valid(0) - this value is always returned when the variable is read. clear(1) - setting the variable to this value clears the configured MAC-based VLAN information for a port.')
fdryMacBasedVlanTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3), )
if mibBuilder.loadTexts: fdryMacBasedVlanTable.setStatus('current')
if mibBuilder.loadTexts: fdryMacBasedVlanTable.setDescription('MAC-based VLAN table.')
fdryMacBasedVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1), ).setIndexNames((0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacVlanIfIndex"), (0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacBasedVlanId"), (0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacBasedVlanMac"))
if mibBuilder.loadTexts: fdryMacBasedVlanEntry.setStatus('current')
if mibBuilder.loadTexts: fdryMacBasedVlanEntry.setDescription('An entry in the MAC-based VLAN table.')
fdryMacBasedVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: fdryMacBasedVlanId.setStatus('current')
if mibBuilder.loadTexts: fdryMacBasedVlanId.setDescription('The VLAN ID for this entry.')
fdryMacBasedVlanMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1, 2), MacAddress())
if mibBuilder.loadTexts: fdryMacBasedVlanMac.setStatus('current')
if mibBuilder.loadTexts: fdryMacBasedVlanMac.setDescription('A host source MAC address to be authenticated.')
fdryMacBasedVlanPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryMacBasedVlanPriority.setStatus('current')
if mibBuilder.loadTexts: fdryMacBasedVlanPriority.setDescription('The priority of the source MAC address.')
fdryMacBasedVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryMacBasedVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: fdryMacBasedVlanRowStatus.setDescription('This object is used to create and delete rows in the table.')
mibBuilder.exportSymbols("FOUNDRY-MAC-VLAN-MIB", fdryMacVlanGlobalObjects=fdryMacVlanGlobalObjects, fdryMacBasedVlanMac=fdryMacBasedVlanMac, fdryMacVlanPortMemberVLanId=fdryMacVlanPortMemberVLanId, fdryMacBasedVlanRowStatus=fdryMacBasedVlanRowStatus, fdryMacVlanPortMemberPortId=fdryMacVlanPortMemberPortId, fdryMacVlanPortMemberTable=fdryMacVlanPortMemberTable, fdryMacVlanTableObjects=fdryMacVlanTableObjects, fdryMacBasedVlanId=fdryMacBasedVlanId, fdryMacVlanMIB=fdryMacVlanMIB, fdryMacVlanGlobalClearOper=fdryMacVlanGlobalClearOper, PYSNMP_MODULE_ID=fdryMacVlanMIB, fdryMacVlanIfMaxEntry=fdryMacVlanIfMaxEntry, fdryMacBasedVlanEntry=fdryMacBasedVlanEntry, fdryMacVlanIfClearConfig=fdryMacVlanIfClearConfig, fdryMacBasedVlanTable=fdryMacBasedVlanTable, fdryMacVlanIfEnable=fdryMacVlanIfEnable, fdryMacBasedVlanPriority=fdryMacBasedVlanPriority, fdryMacVlanIfClearOper=fdryMacVlanIfClearOper, fdryMacVlanIfEntry=fdryMacVlanIfEntry, fdryMacVlanPortMemberRowStatus=fdryMacVlanPortMemberRowStatus, fdryMacVlanIfIndex=fdryMacVlanIfIndex, fdryMacVlanGlobalDynConfigState=fdryMacVlanGlobalDynConfigState, fdryMacVlanIfTable=fdryMacVlanIfTable, fdryMacVlanPortMemberEntry=fdryMacVlanPortMemberEntry)
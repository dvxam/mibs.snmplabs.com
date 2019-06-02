#
# PySNMP MIB module H3C-SNMP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-SNMP-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:23:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
SnmpSecurityModel, SnmpAdminString, SnmpSecurityLevel = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpSecurityModel", "SnmpAdminString", "SnmpSecurityLevel")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, IpAddress, MibIdentifier, ModuleIdentity, Counter32, NotificationType, Bits, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter32", "NotificationType", "Bits", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cSnmpExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104))
h3cSnmpExt.setRevisions(('2009-04-07 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cSnmpExt.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: h3cSnmpExt.setLastUpdated('200904071700Z')
if mibBuilder.loadTexts: h3cSnmpExt.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cSnmpExt.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: h3cSnmpExt.setDescription('This MIB file is to provide the object definition of the SNMP extended information.')
h3cSnmpExtScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1))
h3cSnmpExtTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2))
h3cSnmpExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 3))
h3cSnmpExtSnmpChannel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(161)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSnmpExtSnmpChannel.setStatus('current')
if mibBuilder.loadTexts: h3cSnmpExtSnmpChannel.setDescription('The channel number used by SNMP.')
h3cSnmpExtReadCommunitySingle = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSnmpExtReadCommunitySingle.setStatus('current')
if mibBuilder.loadTexts: h3cSnmpExtReadCommunitySingle.setDescription('The first read community.')
h3cSnmpExtWriteCommunitySingle = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSnmpExtWriteCommunitySingle.setStatus('current')
if mibBuilder.loadTexts: h3cSnmpExtWriteCommunitySingle.setDescription('The first write community.')
h3cSnmpExtCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1), )
if mibBuilder.loadTexts: h3cSnmpExtCommunityTable.setStatus('current')
if mibBuilder.loadTexts: h3cSnmpExtCommunityTable.setDescription('Modify the extended properties of SNMP community or user.')
h3cSnmpExtCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1), ).setIndexNames((0, "H3C-SNMP-EXT-MIB", "h3cSnmpExtCommunitySecurityLevel"), (0, "H3C-SNMP-EXT-MIB", "h3cSnmpExtCommunitySecurityName"))
if mibBuilder.loadTexts: h3cSnmpExtCommunityEntry.setStatus('current')
if mibBuilder.loadTexts: h3cSnmpExtCommunityEntry.setDescription('The entry of h3cSnmpExtCommunityTable')
h3cSnmpExtCommunitySecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 1), SnmpSecurityModel())
if mibBuilder.loadTexts: h3cSnmpExtCommunitySecurityLevel.setStatus('current')
if mibBuilder.loadTexts: h3cSnmpExtCommunitySecurityLevel.setDescription("The Security Model of the specified community or user. This object may not take the 'any' (0) value.")
h3cSnmpExtCommunitySecurityName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 2), SnmpAdminString())
if mibBuilder.loadTexts: h3cSnmpExtCommunitySecurityName.setStatus('current')
if mibBuilder.loadTexts: h3cSnmpExtCommunitySecurityName.setDescription('The Security Name of the specified community or user.')
h3cSnmpExtCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSnmpExtCommunityName.setStatus('current')
if mibBuilder.loadTexts: h3cSnmpExtCommunityName.setDescription('The specified community name.')
h3cSnmpExtCommunityAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 2999), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSnmpExtCommunityAclNum.setStatus('current')
if mibBuilder.loadTexts: h3cSnmpExtCommunityAclNum.setDescription('The specified ACL (Access Control List) number used by the community or the user.')
mibBuilder.exportSymbols("H3C-SNMP-EXT-MIB", h3cSnmpExtSnmpChannel=h3cSnmpExtSnmpChannel, h3cSnmpExtCommunityAclNum=h3cSnmpExtCommunityAclNum, h3cSnmpExtCommunityTable=h3cSnmpExtCommunityTable, h3cSnmpExtCommunitySecurityName=h3cSnmpExtCommunitySecurityName, h3cSnmpExtReadCommunitySingle=h3cSnmpExtReadCommunitySingle, h3cSnmpExtCommunitySecurityLevel=h3cSnmpExtCommunitySecurityLevel, h3cSnmpExtCommunityName=h3cSnmpExtCommunityName, h3cSnmpExt=h3cSnmpExt, h3cSnmpExtWriteCommunitySingle=h3cSnmpExtWriteCommunitySingle, h3cSnmpExtScalarObjects=h3cSnmpExtScalarObjects, h3cSnmpExtCommunityEntry=h3cSnmpExtCommunityEntry, h3cSnmpExtNotifications=h3cSnmpExtNotifications, h3cSnmpExtTables=h3cSnmpExtTables, PYSNMP_MODULE_ID=h3cSnmpExt)
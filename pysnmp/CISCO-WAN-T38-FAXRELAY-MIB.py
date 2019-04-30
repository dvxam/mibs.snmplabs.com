#
# PySNMP MIB module CISCO-WAN-T38-FAXRELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-T38-FAXRELAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, Counter64, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, ModuleIdentity, iso, TimeTicks, NotificationType, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Counter64", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "ModuleIdentity", "iso", "TimeTicks", "NotificationType", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanT38FaxRelayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 19))
ciscoWanT38FaxRelayMIB.setRevisions(('2004-02-19 00:00', '2002-06-01 00:00', '2002-04-12 15:00',))
if mibBuilder.loadTexts: ciscoWanT38FaxRelayMIB.setLastUpdated('200402190000Z')
if mibBuilder.loadTexts: ciscoWanT38FaxRelayMIB.setOrganization('Cisco Systems, Inc.')
ciscoWanT38FaxRelayMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 19, 1))
t38FaxRelayGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1))
t38FaxRelayGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1), )
if mibBuilder.loadTexts: t38FaxRelayGrpTable.setStatus('current')
t38FaxRelayGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-T38-FAXRELAY-MIB", "t38vismDs1Number"))
if mibBuilder.loadTexts: t38FaxRelayGrpEntry.setStatus('current')
t38vismDs1Number = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: t38vismDs1Number.setStatus('current')
t38MaxFaxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("fx2400bps", 1), ("fx4800bps", 2), ("fx7200bps", 3), ("fx9600bps", 4), ("fx12000bps", 5), ("fx14400bps", 6))).clone('fx14400bps')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38MaxFaxTxRate.setStatus('current')
t38FaxInfoFieldSize = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(48)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38FaxInfoFieldSize.setStatus('deprecated')
t38HsDataPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10, 20, 30, 40))).clone(namedValues=NamedValues(("tenms", 10), ("twentyms", 20), ("thirtyms", 30), ("fortyms", 40))).clone('thirtyms')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38HsDataPacketSize.setStatus('current')
t38LsDataRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38LsDataRedundancy.setStatus('current')
t38HsDataRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38HsDataRedundancy.setStatus('current')
t38TCFmethod = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("localTCF", 1), ("networkTCF", 2))).clone('networkTCF')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38TCFmethod.setStatus('current')
t38ErrCorrection = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38ErrCorrection.setStatus('deprecated')
t38NSFOverride = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38NSFOverride.setStatus('current')
t38NSFCountryCode = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(173)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38NSFCountryCode.setStatus('current')
t38NSFVendorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(81)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38NSFVendorCode.setStatus('current')
t38NseAckTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(250, 10000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38NseAckTimeOut.setStatus('current')
t38FxLCO = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("gwAndPt", 1), ("gw", 2), ("ptAndGw", 3), ("pt", 4), ("off", 5))).clone('gwAndPt')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38FxLCO.setStatus('current')
t38Redundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38Redundancy.setStatus('deprecated')
t38T30ECM = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t38T30ECM.setStatus('current')
t38NotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 19, 2))
t38Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 19, 2, 0))
t38FaxRelayMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 19, 3))
t38FaxRelayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 1))
t38FaxRelayMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 2))
t38FaxRelayMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 1, 1)).setObjects(("CISCO-WAN-T38-FAXRELAY-MIB", "t38FaxRelayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t38FaxRelayMIBCompliance = t38FaxRelayMIBCompliance.setStatus('deprecated')
t38FaxRelayMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 1, 2)).setObjects(("CISCO-WAN-T38-FAXRELAY-MIB", "t38FaxRelayGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t38FaxRelayMIBComplianceRev1 = t38FaxRelayMIBComplianceRev1.setStatus('current')
t38FaxRelayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 2, 1)).setObjects(("CISCO-WAN-T38-FAXRELAY-MIB", "t38MaxFaxTxRate"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38FaxInfoFieldSize"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38HsDataPacketSize"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38LsDataRedundancy"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38HsDataRedundancy"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38TCFmethod"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38ErrCorrection"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFOverride"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFCountryCode"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFVendorCode"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NseAckTimeOut"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38FxLCO"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38Redundancy"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38T30ECM"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t38FaxRelayGroup = t38FaxRelayGroup.setStatus('deprecated')
t38FaxRelayGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 2, 2)).setObjects(("CISCO-WAN-T38-FAXRELAY-MIB", "t38MaxFaxTxRate"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38HsDataPacketSize"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38LsDataRedundancy"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38HsDataRedundancy"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38TCFmethod"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFOverride"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFCountryCode"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFVendorCode"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NseAckTimeOut"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38FxLCO"), ("CISCO-WAN-T38-FAXRELAY-MIB", "t38T30ECM"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t38FaxRelayGroupRev1 = t38FaxRelayGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-T38-FAXRELAY-MIB", t38NseAckTimeOut=t38NseAckTimeOut, t38FaxRelayMIBConformance=t38FaxRelayMIBConformance, t38HsDataPacketSize=t38HsDataPacketSize, t38T30ECM=t38T30ECM, t38FaxRelayGroup=t38FaxRelayGroup, ciscoWanT38FaxRelayMIB=ciscoWanT38FaxRelayMIB, t38MaxFaxTxRate=t38MaxFaxTxRate, t38NSFOverride=t38NSFOverride, t38FaxRelayGrp=t38FaxRelayGrp, t38Redundancy=t38Redundancy, t38FaxRelayMIBCompliances=t38FaxRelayMIBCompliances, t38FxLCO=t38FxLCO, t38FaxRelayMIBCompliance=t38FaxRelayMIBCompliance, PYSNMP_MODULE_ID=ciscoWanT38FaxRelayMIB, t38FaxInfoFieldSize=t38FaxInfoFieldSize, t38NSFCountryCode=t38NSFCountryCode, t38FaxRelayGrpTable=t38FaxRelayGrpTable, ciscoWanT38FaxRelayMIBObjects=ciscoWanT38FaxRelayMIBObjects, t38TCFmethod=t38TCFmethod, t38FaxRelayGrpEntry=t38FaxRelayGrpEntry, t38NSFVendorCode=t38NSFVendorCode, t38FaxRelayMIBComplianceRev1=t38FaxRelayMIBComplianceRev1, t38NotificationPrefix=t38NotificationPrefix, t38FaxRelayGroupRev1=t38FaxRelayGroupRev1, t38Notifications=t38Notifications, t38ErrCorrection=t38ErrCorrection, t38LsDataRedundancy=t38LsDataRedundancy, t38vismDs1Number=t38vismDs1Number, t38HsDataRedundancy=t38HsDataRedundancy, t38FaxRelayMIBGroups=t38FaxRelayMIBGroups)
#
# PySNMP MIB module CISCO-FCOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FCOE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
fcmInstanceIndex, fcmSwitchIndex = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex", "fcmSwitchIndex")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, Counter64, Counter32, ObjectIdentity, IpAddress, TimeTicks, NotificationType, iso, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Counter32", "ObjectIdentity", "IpAddress", "TimeTicks", "NotificationType", "iso", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Gauge32")
MacAddress, TextualConvention, DisplayString, TimeStamp, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "TimeStamp", "RowStatus", "TruthValue")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
ciscoFCoEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 673))
ciscoFCoEMIB.setRevisions(('2008-06-16 00:00',))
if mibBuilder.loadTexts: ciscoFCoEMIB.setLastUpdated('200806160000Z')
if mibBuilder.loadTexts: ciscoFCoEMIB.setOrganization('Cisco Systems Inc.')
ciscoFCoEMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 673, 1))
ciscoFCoEMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 673, 2))
cfcoeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1))
cfcoeFipSnoopingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2))
class VfcBindType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("interfaceIndex", 1), ("macAddress", 2))

cfcoeCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1), )
if mibBuilder.loadTexts: cfcoeCfgTable.setStatus('current')
cfcoeCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"))
if mibBuilder.loadTexts: cfcoeCfgEntry.setStatus('current')
cfcoeCfgFcmap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcoeCfgFcmap.setStatus('current')
cfcoeCfgDynamicVfcCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcoeCfgDynamicVfcCreation.setStatus('current')
cfcoeCfgDynamicVfcAgeTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcoeCfgDynamicVfcAgeTimer.setStatus('current')
cfcoeCfgDefaultFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcoeCfgDefaultFCFPriority.setStatus('current')
cfcoeCfgDATov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcoeCfgDATov.setStatus('current')
cfcoeCfgAddressingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fpma", 1), ("spma", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcoeCfgAddressingMode.setStatus('current')
cfcoeVLANTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2), )
if mibBuilder.loadTexts: cfcoeVLANTable.setStatus('current')
cfcoeVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "CISCO-FCOE-MIB", "cfcoeVLANIndex"), (0, "CISCO-FCOE-MIB", "cfcoeFabricIndex"))
if mibBuilder.loadTexts: cfcoeVLANEntry.setStatus('current')
cfcoeVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: cfcoeVLANIndex.setStatus('current')
cfcoeFabricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: cfcoeFabricIndex.setStatus('current')
cfcoeVLANOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcoeVLANOperState.setStatus('current')
cfcoeVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcoeVLANRowStatus.setStatus('current')
cfcoeStaticVfcTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3), )
if mibBuilder.loadTexts: cfcoeStaticVfcTable.setStatus('current')
cfcoeStaticVfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "CISCO-FCOE-MIB", "cfcoeStaticVfcIndex"))
if mibBuilder.loadTexts: cfcoeStaticVfcEntry.setStatus('current')
cfcoeStaticVfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cfcoeStaticVfcIndex.setStatus('current')
cfcoeStaticVfcFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcoeStaticVfcFCFPriority.setStatus('current')
cfcoeStaticVfcBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 3), VfcBindType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcoeStaticVfcBindType.setStatus('current')
cfcoeStaticVfcBindIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcoeStaticVfcBindIfIndex.setStatus('current')
cfcoeStaticVfcBindMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcoeStaticVfcBindMACAddress.setStatus('current')
cfcoeStaticVfcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcoeStaticVfcIfIndex.setStatus('current')
cfcoeStaticVfcCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcoeStaticVfcCreationTime.setStatus('current')
cfcoeStaticVfcFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcoeStaticVfcFailureCause.setStatus('current')
cfcoeStaticVfcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcoeStaticVfcRowStatus.setStatus('current')
cfcoeFipSnoopingEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcoeFipSnoopingEnable.setStatus('current')
cfcoeFipSnoopingFcmap = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcoeFipSnoopingFcmap.setStatus('current')
cfcoeEnodeIntfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 3), )
if mibBuilder.loadTexts: cfcoeEnodeIntfTable.setStatus('current')
cfcoeEnodeIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-FCOE-MIB", "cfcoeEnodeIntfIfIndex"))
if mibBuilder.loadTexts: cfcoeEnodeIntfEntry.setStatus('current')
cfcoeEnodeIntfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cfcoeEnodeIntfIfIndex.setStatus('current')
cfcoeEnodeIntfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcoeEnodeIntfRowStatus.setStatus('current')
cFCoEMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 1))
cFCoEMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2))
cFCoEMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 1, 1)).setObjects(("CISCO-FCOE-MIB", "cfcoeCfgConformanceObjects"), ("CISCO-FCOE-MIB", "cfcoeVLANConformanceObjects"), ("CISCO-FCOE-MIB", "cfcoeStaticVfcConformanceObjects"), ("CISCO-FCOE-MIB", "cfcoeFipSnoopingConformanceObjects"), ("CISCO-FCOE-MIB", "cfcoeEnodeIntfObjects"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCoEMIBCompliance = cFCoEMIBCompliance.setStatus('current')
cfcoeCfgConformanceObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 1)).setObjects(("CISCO-FCOE-MIB", "cfcoeCfgFcmap"), ("CISCO-FCOE-MIB", "cfcoeCfgDynamicVfcCreation"), ("CISCO-FCOE-MIB", "cfcoeCfgDynamicVfcAgeTimer"), ("CISCO-FCOE-MIB", "cfcoeCfgDefaultFCFPriority"), ("CISCO-FCOE-MIB", "cfcoeCfgDATov"), ("CISCO-FCOE-MIB", "cfcoeCfgAddressingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcoeCfgConformanceObjects = cfcoeCfgConformanceObjects.setStatus('current')
cfcoeVLANConformanceObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 2)).setObjects(("CISCO-FCOE-MIB", "cfcoeVLANOperState"), ("CISCO-FCOE-MIB", "cfcoeVLANRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcoeVLANConformanceObjects = cfcoeVLANConformanceObjects.setStatus('current')
cfcoeStaticVfcConformanceObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 3)).setObjects(("CISCO-FCOE-MIB", "cfcoeStaticVfcFCFPriority"), ("CISCO-FCOE-MIB", "cfcoeStaticVfcBindType"), ("CISCO-FCOE-MIB", "cfcoeStaticVfcBindIfIndex"), ("CISCO-FCOE-MIB", "cfcoeStaticVfcBindMACAddress"), ("CISCO-FCOE-MIB", "cfcoeStaticVfcIfIndex"), ("CISCO-FCOE-MIB", "cfcoeStaticVfcCreationTime"), ("CISCO-FCOE-MIB", "cfcoeStaticVfcFailureCause"), ("CISCO-FCOE-MIB", "cfcoeStaticVfcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcoeStaticVfcConformanceObjects = cfcoeStaticVfcConformanceObjects.setStatus('current')
cfcoeFipSnoopingConformanceObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 4)).setObjects(("CISCO-FCOE-MIB", "cfcoeFipSnoopingEnable"), ("CISCO-FCOE-MIB", "cfcoeFipSnoopingFcmap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcoeFipSnoopingConformanceObjects = cfcoeFipSnoopingConformanceObjects.setStatus('current')
cfcoeEnodeIntfObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 5)).setObjects(("CISCO-FCOE-MIB", "cfcoeEnodeIntfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcoeEnodeIntfObjects = cfcoeEnodeIntfObjects.setStatus('current')
mibBuilder.exportSymbols("CISCO-FCOE-MIB", cfcoeStaticVfcTable=cfcoeStaticVfcTable, cfcoeVLANConformanceObjects=cfcoeVLANConformanceObjects, cfcoeVLANTable=cfcoeVLANTable, cfcoeFipSnoopingConformanceObjects=cfcoeFipSnoopingConformanceObjects, cfcoeCfgTable=cfcoeCfgTable, cfcoeEnodeIntfIfIndex=cfcoeEnodeIntfIfIndex, cFCoEMIBCompliance=cFCoEMIBCompliance, cfcoeStaticVfcRowStatus=cfcoeStaticVfcRowStatus, cfcoeEnodeIntfTable=cfcoeEnodeIntfTable, cfcoeStaticVfcEntry=cfcoeStaticVfcEntry, cfcoeFipSnoopingObjects=cfcoeFipSnoopingObjects, cfcoeCfgDynamicVfcCreation=cfcoeCfgDynamicVfcCreation, cfcoeCfgDynamicVfcAgeTimer=cfcoeCfgDynamicVfcAgeTimer, cfcoeCfgFcmap=cfcoeCfgFcmap, PYSNMP_MODULE_ID=ciscoFCoEMIB, cfcoeCfgAddressingMode=cfcoeCfgAddressingMode, cFCoEMIBGroups=cFCoEMIBGroups, cfcoeFipSnoopingFcmap=cfcoeFipSnoopingFcmap, cfcoeStaticVfcBindIfIndex=cfcoeStaticVfcBindIfIndex, cfcoeEnodeIntfObjects=cfcoeEnodeIntfObjects, ciscoFCoEMIBConformance=ciscoFCoEMIBConformance, cfcoeStaticVfcFCFPriority=cfcoeStaticVfcFCFPriority, cfcoeStaticVfcBindType=cfcoeStaticVfcBindType, cfcoeVLANRowStatus=cfcoeVLANRowStatus, cfcoeFipSnoopingEnable=cfcoeFipSnoopingEnable, cfcoeStaticVfcConformanceObjects=cfcoeStaticVfcConformanceObjects, cFCoEMIBCompliances=cFCoEMIBCompliances, cfcoeStaticVfcCreationTime=cfcoeStaticVfcCreationTime, cfcoeStaticVfcBindMACAddress=cfcoeStaticVfcBindMACAddress, cfcoeVLANEntry=cfcoeVLANEntry, cfcoeConfig=cfcoeConfig, cfcoeVLANOperState=cfcoeVLANOperState, cfcoeCfgDefaultFCFPriority=cfcoeCfgDefaultFCFPriority, cfcoeStaticVfcIndex=cfcoeStaticVfcIndex, cfcoeCfgDATov=cfcoeCfgDATov, cfcoeVLANIndex=cfcoeVLANIndex, cfcoeCfgConformanceObjects=cfcoeCfgConformanceObjects, cfcoeStaticVfcIfIndex=cfcoeStaticVfcIfIndex, cfcoeEnodeIntfEntry=cfcoeEnodeIntfEntry, ciscoFCoEMIB=ciscoFCoEMIB, cfcoeFabricIndex=cfcoeFabricIndex, cfcoeStaticVfcFailureCause=cfcoeStaticVfcFailureCause, ciscoFCoEMIBObjects=ciscoFCoEMIBObjects, VfcBindType=VfcBindType, cfcoeCfgEntry=cfcoeCfgEntry, cfcoeEnodeIntfRowStatus=cfcoeEnodeIntfRowStatus)

#
# PySNMP MIB module BLADETYPE2-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLADETYPE2-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:22:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
BridgeId, = mibBuilder.importSymbols("BRIDGE-MIB", "BridgeId")
hpSwitchBladeType2_Mgmt, = mibBuilder.importSymbols("HP-SWITCH-PL-MIB", "hpSwitchBladeType2-Mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, Counter64, Counter32, iso, Integer32, TimeTicks, NotificationType, IpAddress, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Counter64", "Counter32", "iso", "Integer32", "TimeTicks", "NotificationType", "IpAddress", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
qos = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8))
if mibBuilder.loadTexts: qos.setLastUpdated('200312050000Z')
if mibBuilder.loadTexts: qos.setOrganization('Hewlett Packard Company')
qosConfigs = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1))
qosStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 2))
qosInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 3))
qosOper = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 4))
qos8021p = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1))
aclCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2))
qosCurCfgPortPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 1), )
if mibBuilder.loadTexts: qosCurCfgPortPriorityTable.setStatus('current')
qosCurCfgPortPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 1, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "qosCurCfgPortIndex"))
if mibBuilder.loadTexts: qosCurCfgPortPriorityEntry.setStatus('current')
qosCurCfgPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosCurCfgPortIndex.setStatus('current')
qosCurCfgPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosCurCfgPortPriority.setStatus('current')
qosNewCfgPortPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 2), )
if mibBuilder.loadTexts: qosNewCfgPortPriorityTable.setStatus('current')
qosNewCfgPortPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 2, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "qosNewCfgPortIndex"))
if mibBuilder.loadTexts: qosNewCfgPortPriorityEntry.setStatus('current')
qosNewCfgPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosNewCfgPortIndex.setStatus('current')
qosNewCfgPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosNewCfgPortPriority.setStatus('current')
qosCurCfgPriorityCoSTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 3), )
if mibBuilder.loadTexts: qosCurCfgPriorityCoSTable.setStatus('current')
qosCurCfgPriorityCoSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 3, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "qosCurCfgPriorityIndex"))
if mibBuilder.loadTexts: qosCurCfgPriorityCoSEntry.setStatus('current')
qosCurCfgPriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosCurCfgPriorityIndex.setStatus('current')
qosCurCfgPriorityCoSq = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosCurCfgPriorityCoSq.setStatus('current')
qosNewCfgPriorityCoSTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 4), )
if mibBuilder.loadTexts: qosNewCfgPriorityCoSTable.setStatus('current')
qosNewCfgPriorityCoSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 4, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "qosNewCfgPriorityIndex"))
if mibBuilder.loadTexts: qosNewCfgPriorityCoSEntry.setStatus('current')
qosNewCfgPriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosNewCfgPriorityIndex.setStatus('current')
qosNewCfgPriorityCoSq = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosNewCfgPriorityCoSq.setStatus('current')
qosCurCfgCosWeightTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 5), )
if mibBuilder.loadTexts: qosCurCfgCosWeightTable.setStatus('current')
qosCurCfgCosWeightEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 5, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "qosCurCfgCosIndex"))
if mibBuilder.loadTexts: qosCurCfgCosWeightEntry.setStatus('current')
qosCurCfgCosIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosCurCfgCosIndex.setStatus('current')
qosCurCfgCosWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosCurCfgCosWeight.setStatus('current')
qosNewCfgCosWeightTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 6), )
if mibBuilder.loadTexts: qosNewCfgCosWeightTable.setStatus('current')
qosNewCfgCosWeightEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 6, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "qosNewCfgCosIndex"))
if mibBuilder.loadTexts: qosNewCfgCosWeightEntry.setStatus('current')
qosNewCfgCosIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosNewCfgCosIndex.setStatus('current')
qosNewCfgCosWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosNewCfgCosWeight.setStatus('current')
qosCurCfgCosNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 8))).clone(namedValues=NamedValues(("num2", 2), ("num8", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosCurCfgCosNum.setStatus('current')
qosNewCfgCosNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 8))).clone(namedValues=NamedValues(("num2", 2), ("num8", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosNewCfgCosNum.setStatus('current')
aclCurCfgPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1), )
if mibBuilder.loadTexts: aclCurCfgPortTable.setStatus('current')
aclCurCfgPortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "aclCurCfgPortIndex"))
if mibBuilder.loadTexts: aclCurCfgPortTableEntry.setStatus('current')
aclCurCfgPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgPortIndex.setStatus('current')
aclCurCfgPortAclBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgPortAclBmap.setStatus('current')
aclCurCfgPortAclBlkBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgPortAclBlkBmap.setStatus('current')
aclCurCfgPortAclGrpBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgPortAclGrpBmap.setStatus('current')
aclNewCfgPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2), )
if mibBuilder.loadTexts: aclNewCfgPortTable.setStatus('current')
aclNewCfgPortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "aclNewCfgPortIndex"))
if mibBuilder.loadTexts: aclNewCfgPortTableEntry.setStatus('current')
aclNewCfgPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgPortIndex.setStatus('current')
aclNewCfgPortAddAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgPortAddAcl.setStatus('current')
aclNewCfgPortAddAclBlk = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgPortAddAclBlk.setStatus('current')
aclNewCfgPortAddAclGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgPortAddAclGrp.setStatus('current')
aclNewCfgPortRemoveAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgPortRemoveAcl.setStatus('current')
aclNewCfgPortRemoveAclBlk = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgPortRemoveAclBlk.setStatus('current')
aclNewCfgPortRemoveAclGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgPortRemoveAclGrp.setStatus('current')
aclNewCfgPortAclBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgPortAclBmap.setStatus('current')
aclNewCfgPortAclBlkBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgPortAclBlkBmap.setStatus('current')
aclNewCfgPortAclGrpBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgPortAclGrpBmap.setStatus('current')
aclCurCfgPortAclMeterTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3), )
if mibBuilder.loadTexts: aclCurCfgPortAclMeterTable.setStatus('current')
aclCurCfgPortAclMeterTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "aclCurCfgPortMeterConfigIndex"), (0, "BLADETYPE2-QOS-MIB", "aclCurCfgAclMeterIndex"))
if mibBuilder.loadTexts: aclCurCfgPortAclMeterTableEntry.setStatus('current')
aclCurCfgPortMeterConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgPortMeterConfigIndex.setStatus('current')
aclCurCfgAclMeterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclMeterIndex.setStatus('current')
aclCurCfgAclMeterCommitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 1000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclMeterCommitRate.setStatus('current')
aclCurCfgAclMeterMaxBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(32, 64, 128, 256, 512, 1024, 2048, 4096))).clone(namedValues=NamedValues(("k32", 32), ("k64", 64), ("k128", 128), ("k256", 256), ("k512", 512), ("k1024", 1024), ("k2048", 2048), ("k4096", 4096)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclMeterMaxBurstSize.setStatus('current')
aclCurCfgAclMeterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclMeterStatus.setStatus('current')
aclCurCfgAclMeterDropOrPass = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("drop", 2), ("pass", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclMeterDropOrPass.setStatus('current')
aclCurCfgAclMeterAclBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclMeterAclBmap.setStatus('current')
aclCurCfgAclMeterAclBlkBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclMeterAclBlkBmap.setStatus('current')
aclCurCfgAclMeterAclGrpBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclMeterAclGrpBmap.setStatus('current')
aclNewCfgPortAclMeterTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4), )
if mibBuilder.loadTexts: aclNewCfgPortAclMeterTable.setStatus('current')
aclNewCfgPortAclMeterTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "aclNewCfgPortMeterConfigIndex"), (0, "BLADETYPE2-QOS-MIB", "aclNewCfgAclMeterIndex"))
if mibBuilder.loadTexts: aclNewCfgPortAclMeterTableEntry.setStatus('current')
aclNewCfgPortMeterConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgPortMeterConfigIndex.setStatus('current')
aclNewCfgAclMeterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgAclMeterIndex.setStatus('current')
aclNewCfgAclMeterCommitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterCommitRate.setStatus('current')
aclNewCfgAclMeterMaxBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(32, 64, 128, 256, 512, 1024, 2048, 4096))).clone(namedValues=NamedValues(("k32", 32), ("k64", 64), ("k128", 128), ("k256", 256), ("k512", 512), ("k1024", 1024), ("k2048", 2048), ("k4096", 4096)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterMaxBurstSize.setStatus('current')
aclNewCfgAclMeterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterStatus.setStatus('current')
aclNewCfgAclMeterDropOrPass = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("drop", 2), ("pass", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterDropOrPass.setStatus('current')
aclNewCfgAclMeterAssignAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterAssignAcl.setStatus('current')
aclNewCfgAclMeterAssignAclBlk = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterAssignAclBlk.setStatus('current')
aclNewCfgAclMeterAssignAclGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterAssignAclGrp.setStatus('current')
aclNewCfgAclMeterUnAssignAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterUnAssignAcl.setStatus('current')
aclNewCfgAclMeterUnAssignAclBlk = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterUnAssignAclBlk.setStatus('current')
aclNewCfgAclMeterUnAssignAclGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclMeterUnAssignAclGrp.setStatus('current')
aclNewCfgAclMeterAclBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgAclMeterAclBmap.setStatus('current')
aclNewCfgAclMeterAclBlkBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgAclMeterAclBlkBmap.setStatus('current')
aclNewCfgAclMeterAclGrpBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgAclMeterAclGrpBmap.setStatus('current')
aclCurCfgPortAclRemarkTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5), )
if mibBuilder.loadTexts: aclCurCfgPortAclRemarkTable.setStatus('current')
aclCurCfgPortAclRemarkTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "aclCurCfgPortRemarkConfigIndex"), (0, "BLADETYPE2-QOS-MIB", "aclCurCfgAclRemarkIndex"))
if mibBuilder.loadTexts: aclCurCfgPortAclRemarkTableEntry.setStatus('current')
aclCurCfgPortRemarkConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgPortRemarkConfigIndex.setStatus('current')
aclCurCfgAclRemarkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclRemarkIndex.setStatus('current')
aclCurCfgAclRemarkInProfUpdatePri = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclRemarkInProfUpdatePri.setStatus('current')
aclCurCfgAclRemarkInProfUpdateTosPrec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclRemarkInProfUpdateTosPrec.setStatus('current')
aclCurCfgAclRemarkInProfUpdateDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclRemarkInProfUpdateDscp.setStatus('current')
aclCurCfgAclRemarkOutProfUpdateDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclRemarkOutProfUpdateDscp.setStatus('current')
aclCurCfgAclRemarkAclBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclRemarkAclBmap.setStatus('current')
aclCurCfgAclRemarkAclBlkBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclRemarkAclBlkBmap.setStatus('current')
aclCurCfgAclRemarkAclGrpBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclCurCfgAclRemarkAclGrpBmap.setStatus('current')
aclNewCfgPortAclRemarkTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6), )
if mibBuilder.loadTexts: aclNewCfgPortAclRemarkTable.setStatus('current')
aclNewCfgPortAclRemarkTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1), ).setIndexNames((0, "BLADETYPE2-QOS-MIB", "aclNewCfgPortRemarkConfigIndex"), (0, "BLADETYPE2-QOS-MIB", "aclNewCfgAclRemarkIndex"))
if mibBuilder.loadTexts: aclNewCfgPortAclRemarkTableEntry.setStatus('current')
aclNewCfgPortRemarkConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgPortRemarkConfigIndex.setStatus('current')
aclNewCfgAclRemarkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgAclRemarkIndex.setStatus('current')
aclNewCfgAclRemarkInProfUpdatePri = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkInProfUpdatePri.setStatus('current')
aclNewCfgAclRemarkInProfUpdateTosPrec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkInProfUpdateTosPrec.setStatus('current')
aclNewCfgAclRemarkInProfUpdateDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkInProfUpdateDscp.setStatus('current')
aclNewCfgAclRemarkOutProfUpdateDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkOutProfUpdateDscp.setStatus('current')
aclNewCfgAclRemarkAssignAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkAssignAcl.setStatus('current')
aclNewCfgAclRemarkAssignAclBlk = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkAssignAclBlk.setStatus('current')
aclNewCfgAclRemarkAssignAclGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkAssignAclGrp.setStatus('current')
aclNewCfgAclRemarkUnAssignAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkUnAssignAcl.setStatus('current')
aclNewCfgAclRemarkUnAssignAclBlk = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkUnAssignAclBlk.setStatus('current')
aclNewCfgAclRemarkUnAssignAclGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkUnAssignAclGrp.setStatus('current')
aclNewCfgAclRemarkAclBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgAclRemarkAclBmap.setStatus('current')
aclNewCfgAclRemarkAclBlkBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgAclRemarkAclBlkBmap.setStatus('current')
aclNewCfgAclRemarkAclGrpBmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclNewCfgAclRemarkAclGrpBmap.setStatus('current')
aclNewCfgAclRemarkReset = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclNewCfgAclRemarkReset.setStatus('current')
mibBuilder.exportSymbols("BLADETYPE2-QOS-MIB", qosNewCfgCosNum=qosNewCfgCosNum, aclNewCfgPortRemoveAcl=aclNewCfgPortRemoveAcl, aclNewCfgAclRemarkOutProfUpdateDscp=aclNewCfgAclRemarkOutProfUpdateDscp, aclNewCfgAclMeterAclBlkBmap=aclNewCfgAclMeterAclBlkBmap, qosCurCfgPriorityCoSq=qosCurCfgPriorityCoSq, aclCurCfgPortAclRemarkTable=aclCurCfgPortAclRemarkTable, qosCurCfgPortIndex=qosCurCfgPortIndex, aclCurCfgAclRemarkInProfUpdateDscp=aclCurCfgAclRemarkInProfUpdateDscp, aclNewCfgPortAclBlkBmap=aclNewCfgPortAclBlkBmap, qosCurCfgCosNum=qosCurCfgCosNum, aclCurCfgPortTable=aclCurCfgPortTable, aclCurCfgAclMeterMaxBurstSize=aclCurCfgAclMeterMaxBurstSize, aclCurCfgPortRemarkConfigIndex=aclCurCfgPortRemarkConfigIndex, aclNewCfgAclMeterCommitRate=aclNewCfgAclMeterCommitRate, aclNewCfgPortAclRemarkTableEntry=aclNewCfgPortAclRemarkTableEntry, qosStats=qosStats, qosCurCfgCosIndex=qosCurCfgCosIndex, qos8021p=qos8021p, aclCurCfgPortMeterConfigIndex=aclCurCfgPortMeterConfigIndex, aclNewCfgAclMeterAssignAclGrp=aclNewCfgAclMeterAssignAclGrp, aclCurCfgPortAclRemarkTableEntry=aclCurCfgPortAclRemarkTableEntry, qosNewCfgCosWeight=qosNewCfgCosWeight, aclCurCfgAclRemarkOutProfUpdateDscp=aclCurCfgAclRemarkOutProfUpdateDscp, aclNewCfgPortAclMeterTable=aclNewCfgPortAclMeterTable, qosCurCfgPriorityCoSTable=qosCurCfgPriorityCoSTable, qosCurCfgCosWeightEntry=qosCurCfgCosWeightEntry, aclNewCfgPortMeterConfigIndex=aclNewCfgPortMeterConfigIndex, qosCurCfgPortPriority=qosCurCfgPortPriority, qosNewCfgCosWeightEntry=qosNewCfgCosWeightEntry, aclCurCfgPortAclBlkBmap=aclCurCfgPortAclBlkBmap, aclNewCfgAclMeterUnAssignAclGrp=aclNewCfgAclMeterUnAssignAclGrp, qosCurCfgPortPriorityTable=qosCurCfgPortPriorityTable, aclNewCfgAclRemarkAssignAcl=aclNewCfgAclRemarkAssignAcl, aclNewCfgPortRemoveAclBlk=aclNewCfgPortRemoveAclBlk, aclNewCfgAclRemarkUnAssignAclGrp=aclNewCfgAclRemarkUnAssignAclGrp, aclCurCfgAclRemarkAclBmap=aclCurCfgAclRemarkAclBmap, qosCurCfgPriorityIndex=qosCurCfgPriorityIndex, aclNewCfgPortAclBmap=aclNewCfgPortAclBmap, aclNewCfgAclRemarkAclBmap=aclNewCfgAclRemarkAclBmap, qosNewCfgPortPriorityEntry=qosNewCfgPortPriorityEntry, aclNewCfgAclMeterStatus=aclNewCfgAclMeterStatus, qosNewCfgPortPriority=qosNewCfgPortPriority, aclNewCfgPortAddAclBlk=aclNewCfgPortAddAclBlk, aclCurCfgAclRemarkAclGrpBmap=aclCurCfgAclRemarkAclGrpBmap, aclNewCfgPortAclGrpBmap=aclNewCfgPortAclGrpBmap, aclNewCfgPortIndex=aclNewCfgPortIndex, aclNewCfgAclRemarkInProfUpdateTosPrec=aclNewCfgAclRemarkInProfUpdateTosPrec, aclNewCfgPortAclMeterTableEntry=aclNewCfgPortAclMeterTableEntry, aclNewCfgAclRemarkAclBlkBmap=aclNewCfgAclRemarkAclBlkBmap, aclNewCfgAclRemarkAssignAclBlk=aclNewCfgAclRemarkAssignAclBlk, qosCurCfgCosWeightTable=qosCurCfgCosWeightTable, qosNewCfgPortPriorityTable=qosNewCfgPortPriorityTable, aclCurCfgAclMeterAclGrpBmap=aclCurCfgAclMeterAclGrpBmap, aclNewCfgPortRemarkConfigIndex=aclNewCfgPortRemarkConfigIndex, aclCurCfgPortTableEntry=aclCurCfgPortTableEntry, aclNewCfgAclMeterIndex=aclNewCfgAclMeterIndex, aclCurCfgAclMeterCommitRate=aclCurCfgAclMeterCommitRate, qosNewCfgCosIndex=qosNewCfgCosIndex, PYSNMP_MODULE_ID=qos, aclNewCfgAclMeterAssignAclBlk=aclNewCfgAclMeterAssignAclBlk, aclNewCfgPortRemoveAclGrp=aclNewCfgPortRemoveAclGrp, qosNewCfgPriorityCoSq=qosNewCfgPriorityCoSq, aclNewCfgPortAddAcl=aclNewCfgPortAddAcl, qosCurCfgCosWeight=qosCurCfgCosWeight, aclNewCfgAclMeterAclGrpBmap=aclNewCfgAclMeterAclGrpBmap, aclCurCfgPortAclMeterTableEntry=aclCurCfgPortAclMeterTableEntry, aclNewCfgAclRemarkReset=aclNewCfgAclRemarkReset, aclNewCfgAclRemarkAssignAclGrp=aclNewCfgAclRemarkAssignAclGrp, aclNewCfgAclMeterAssignAcl=aclNewCfgAclMeterAssignAcl, aclNewCfgAclMeterAclBmap=aclNewCfgAclMeterAclBmap, qosNewCfgCosWeightTable=qosNewCfgCosWeightTable, qosNewCfgPriorityCoSTable=qosNewCfgPriorityCoSTable, aclNewCfgAclMeterMaxBurstSize=aclNewCfgAclMeterMaxBurstSize, aclNewCfgPortAclRemarkTable=aclNewCfgPortAclRemarkTable, aclNewCfgAclMeterUnAssignAcl=aclNewCfgAclMeterUnAssignAcl, aclCurCfgAclRemarkInProfUpdatePri=aclCurCfgAclRemarkInProfUpdatePri, aclCurCfgAclRemarkIndex=aclCurCfgAclRemarkIndex, aclCurCfgAclRemarkInProfUpdateTosPrec=aclCurCfgAclRemarkInProfUpdateTosPrec, aclCurCfgAclRemarkAclBlkBmap=aclCurCfgAclRemarkAclBlkBmap, aclNewCfgPortTableEntry=aclNewCfgPortTableEntry, qosNewCfgPriorityIndex=qosNewCfgPriorityIndex, aclNewCfgAclRemarkUnAssignAcl=aclNewCfgAclRemarkUnAssignAcl, qosConfigs=qosConfigs, aclCurCfgPortAclGrpBmap=aclCurCfgPortAclGrpBmap, aclCurCfgPortAclBmap=aclCurCfgPortAclBmap, aclNewCfgAclRemarkInProfUpdatePri=aclNewCfgAclRemarkInProfUpdatePri, aclNewCfgAclRemarkInProfUpdateDscp=aclNewCfgAclRemarkInProfUpdateDscp, aclCurCfgAclMeterAclBlkBmap=aclCurCfgAclMeterAclBlkBmap, aclNewCfgAclRemarkIndex=aclNewCfgAclRemarkIndex, aclNewCfgAclRemarkUnAssignAclBlk=aclNewCfgAclRemarkUnAssignAclBlk, aclCfg=aclCfg, qosNewCfgPortIndex=qosNewCfgPortIndex, aclCurCfgAclMeterIndex=aclCurCfgAclMeterIndex, qosNewCfgPriorityCoSEntry=qosNewCfgPriorityCoSEntry, qosOper=qosOper, aclNewCfgAclMeterDropOrPass=aclNewCfgAclMeterDropOrPass, aclNewCfgAclRemarkAclGrpBmap=aclNewCfgAclRemarkAclGrpBmap, qos=qos, qosInfo=qosInfo, aclCurCfgAclMeterStatus=aclCurCfgAclMeterStatus, aclCurCfgPortAclMeterTable=aclCurCfgPortAclMeterTable, aclCurCfgAclMeterAclBmap=aclCurCfgAclMeterAclBmap, qosCurCfgPriorityCoSEntry=qosCurCfgPriorityCoSEntry, aclCurCfgPortIndex=aclCurCfgPortIndex, aclNewCfgPortAddAclGrp=aclNewCfgPortAddAclGrp, aclNewCfgAclMeterUnAssignAclBlk=aclNewCfgAclMeterUnAssignAclBlk, aclNewCfgPortTable=aclNewCfgPortTable, qosCurCfgPortPriorityEntry=qosCurCfgPortPriorityEntry, aclCurCfgAclMeterDropOrPass=aclCurCfgAclMeterDropOrPass)

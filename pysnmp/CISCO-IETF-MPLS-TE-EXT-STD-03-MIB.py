#
# PySNMP MIB module CISCO-IETF-MPLS-TE-EXT-STD-03-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
CMplsLocalId, CMplsGlobalId, CMplsIccId, CMplsNodeId = mibBuilder.importSymbols("CISCO-MPLS-TC-EXT-STD-MIB", "CMplsLocalId", "CMplsGlobalId", "CMplsIccId", "CMplsNodeId")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsStdMIB, MplsTunnelIndex, MplsTunnelInstanceIndex = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB", "MplsTunnelIndex", "MplsTunnelInstanceIndex")
mplsTunnelIngressLSRId, mplsTunnelInstance, mplsTunnelIndex, mplsTunnelEgressLSRId = mibBuilder.importSymbols("MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId", "mplsTunnelInstance", "mplsTunnelIndex", "mplsTunnelEgressLSRId")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, Unsigned32, MibIdentifier, iso, NotificationType, zeroDotZero, Counter64, Counter32, Bits, Integer32, IpAddress, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "MibIdentifier", "iso", "NotificationType", "zeroDotZero", "Counter64", "Counter32", "Bits", "Integer32", "IpAddress", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
RowStatus, TextualConvention, DisplayString, TruthValue, RowPointer, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue", "RowPointer", "StorageType")
cmplsTeExtStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 146))
cmplsTeExtStdMIB.setRevisions(('2012-04-08 00:00',))
if mibBuilder.loadTexts: cmplsTeExtStdMIB.setLastUpdated('201206060000Z')
if mibBuilder.loadTexts: cmplsTeExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
cmplsTeExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 146, 0))
cmplsTeExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 146, 1))
cmplsTeExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 146, 2))
cmplsNodeConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1), )
if mibBuilder.loadTexts: cmplsNodeConfigTable.setStatus('current')
cmplsNodeConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigLocalId"))
if mibBuilder.loadTexts: cmplsNodeConfigEntry.setStatus('current')
cmplsNodeConfigLocalId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 1), CMplsLocalId())
if mibBuilder.loadTexts: cmplsNodeConfigLocalId.setStatus('current')
cmplsNodeConfigGlobalId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 2), CMplsGlobalId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsNodeConfigGlobalId.setStatus('current')
cmplsNodeConfigNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 3), CMplsNodeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsNodeConfigNodeId.setStatus('current')
cmplsNodeConfigIccId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 4), CMplsIccId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsNodeConfigIccId.setStatus('current')
cmplsNodeConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsNodeConfigRowStatus.setStatus('current')
cmplsNodeConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 6), StorageType().clone('volatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsNodeConfigStorageType.setStatus('current')
cmplsNodeIpMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2), )
if mibBuilder.loadTexts: cmplsNodeIpMapTable.setStatus('current')
cmplsNodeIpMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2, 1), ).setIndexNames((0, "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIpMapGlobalId"), (0, "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIpMapNodeId"))
if mibBuilder.loadTexts: cmplsNodeIpMapEntry.setStatus('current')
cmplsNodeIpMapGlobalId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2, 1, 1), CMplsGlobalId())
if mibBuilder.loadTexts: cmplsNodeIpMapGlobalId.setStatus('current')
cmplsNodeIpMapNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2, 1, 2), CMplsNodeId())
if mibBuilder.loadTexts: cmplsNodeIpMapNodeId.setStatus('current')
cmplsNodeIpMapLocalId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2, 1, 3), CMplsLocalId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsNodeIpMapLocalId.setStatus('current')
cmplsNodeIccMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 3), )
if mibBuilder.loadTexts: cmplsNodeIccMapTable.setStatus('current')
cmplsNodeIccMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 3, 1), ).setIndexNames((0, "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIccMapIccId"))
if mibBuilder.loadTexts: cmplsNodeIccMapEntry.setStatus('current')
cmplsNodeIccMapIccId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 3, 1, 1), CMplsIccId())
if mibBuilder.loadTexts: cmplsNodeIccMapIccId.setStatus('current')
cmplsNodeIccMapLocalId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 3, 1, 2), CMplsLocalId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsNodeIccMapLocalId.setStatus('current')
cmplsTunnelExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4), )
if mibBuilder.loadTexts: cmplsTunnelExtTable.setStatus('current')
cmplsTunnelExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1), ).setIndexNames((0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"), (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"), (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"), (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"))
if mibBuilder.loadTexts: cmplsTunnelExtEntry.setStatus('current')
cmplsTunnelOppositeDirPtr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 1), RowPointer().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsTunnelOppositeDirPtr.setStatus('current')
cmplsTunnelExtOppositeDirTnlValid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsTunnelExtOppositeDirTnlValid.setStatus('current')
cmplsTunnelExtDestTnlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 3), MplsTunnelIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsTunnelExtDestTnlIndex.setStatus('current')
cmplsTunnelExtDestTnlLspIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 4), MplsTunnelInstanceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsTunnelExtDestTnlLspIndex.setStatus('current')
cmplsTunnelExtDestTnlValid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsTunnelExtDestTnlValid.setStatus('current')
cmplsTunnelReversePerfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5), )
if mibBuilder.loadTexts: cmplsTunnelReversePerfTable.setStatus('current')
cmplsTunnelReversePerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1), ).setIndexNames((0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"), (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"), (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"), (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"))
if mibBuilder.loadTexts: cmplsTunnelReversePerfEntry.setStatus('current')
cmplsTunnelReversePerfPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsTunnelReversePerfPackets.setStatus('current')
cmplsTunnelReversePerfHCPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsTunnelReversePerfHCPackets.setStatus('current')
cmplsTunnelReversePerfErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsTunnelReversePerfErrors.setStatus('current')
cmplsTunnelReversePerfBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsTunnelReversePerfBytes.setStatus('current')
cmplsTunnelReversePerfHCBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsTunnelReversePerfHCBytes.setStatus('current')
cmplsTeExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 1))
cmplsTeExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 2))
cmplsTeExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 2, 1)).setObjects(("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtGroup"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtIpOperatorGroup"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsTeExtModuleFullCompliance = cmplsTeExtModuleFullCompliance.setStatus('current')
cmplsTeExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 2, 2)).setObjects(("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtGroup"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtIpOperatorGroup"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsTeExtModuleReadOnlyCompliance = cmplsTeExtModuleReadOnlyCompliance.setStatus('current')
cmplsTunnelExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 1, 1)).setObjects(("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelOppositeDirPtr"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtOppositeDirTnlValid"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtDestTnlIndex"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtDestTnlLspIndex"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtDestTnlValid"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfPackets"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfHCPackets"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfErrors"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfBytes"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfHCBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsTunnelExtGroup = cmplsTunnelExtGroup.setStatus('current')
cmplsTunnelExtIpOperatorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 1, 2)).setObjects(("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigGlobalId"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigNodeId"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigRowStatus"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigStorageType"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIpMapLocalId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsTunnelExtIpOperatorGroup = cmplsTunnelExtIpOperatorGroup.setStatus('current')
cmplsTunnelExtIccOperatorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 1, 3)).setObjects(("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigIccId"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigRowStatus"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigStorageType"), ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIccMapLocalId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsTunnelExtIccOperatorGroup = cmplsTunnelExtIccOperatorGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", cmplsTunnelExtDestTnlValid=cmplsTunnelExtDestTnlValid, cmplsNodeConfigStorageType=cmplsNodeConfigStorageType, cmplsNodeIccMapIccId=cmplsNodeIccMapIccId, cmplsNodeIpMapLocalId=cmplsNodeIpMapLocalId, cmplsTeExtGroups=cmplsTeExtGroups, PYSNMP_MODULE_ID=cmplsTeExtStdMIB, cmplsTeExtModuleReadOnlyCompliance=cmplsTeExtModuleReadOnlyCompliance, cmplsTunnelExtTable=cmplsTunnelExtTable, cmplsTunnelReversePerfHCPackets=cmplsTunnelReversePerfHCPackets, cmplsNodeConfigGlobalId=cmplsNodeConfigGlobalId, cmplsTunnelExtIpOperatorGroup=cmplsTunnelExtIpOperatorGroup, cmplsTeExtCompliances=cmplsTeExtCompliances, cmplsTunnelExtEntry=cmplsTunnelExtEntry, cmplsTeExtModuleFullCompliance=cmplsTeExtModuleFullCompliance, cmplsTunnelReversePerfPackets=cmplsTunnelReversePerfPackets, cmplsNodeIpMapGlobalId=cmplsNodeIpMapGlobalId, cmplsTunnelExtDestTnlIndex=cmplsTunnelExtDestTnlIndex, cmplsNodeConfigIccId=cmplsNodeConfigIccId, cmplsNodeIpMapNodeId=cmplsNodeIpMapNodeId, cmplsTunnelExtGroup=cmplsTunnelExtGroup, cmplsTunnelReversePerfBytes=cmplsTunnelReversePerfBytes, cmplsNodeConfigEntry=cmplsNodeConfigEntry, cmplsNodeIccMapEntry=cmplsNodeIccMapEntry, cmplsTunnelReversePerfTable=cmplsTunnelReversePerfTable, cmplsTeExtConformance=cmplsTeExtConformance, cmplsNodeConfigTable=cmplsNodeConfigTable, cmplsTunnelExtOppositeDirTnlValid=cmplsTunnelExtOppositeDirTnlValid, cmplsNodeIccMapTable=cmplsNodeIccMapTable, cmplsTunnelReversePerfEntry=cmplsTunnelReversePerfEntry, cmplsNodeIpMapEntry=cmplsNodeIpMapEntry, cmplsTunnelOppositeDirPtr=cmplsTunnelOppositeDirPtr, cmplsNodeIccMapLocalId=cmplsNodeIccMapLocalId, cmplsTeExtStdMIB=cmplsTeExtStdMIB, cmplsTunnelExtIccOperatorGroup=cmplsTunnelExtIccOperatorGroup, cmplsNodeConfigRowStatus=cmplsNodeConfigRowStatus, cmplsTeExtNotifications=cmplsTeExtNotifications, cmplsNodeConfigNodeId=cmplsNodeConfigNodeId, cmplsNodeIpMapTable=cmplsNodeIpMapTable, cmplsTunnelReversePerfHCBytes=cmplsTunnelReversePerfHCBytes, cmplsNodeConfigLocalId=cmplsNodeConfigLocalId, cmplsTunnelReversePerfErrors=cmplsTunnelReversePerfErrors, cmplsTeExtObjects=cmplsTeExtObjects, cmplsTunnelExtDestTnlLspIndex=cmplsTunnelExtDestTnlLspIndex)
#
# PySNMP MIB module CISCO-OPTICAL-IF-CROSS-CONNECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OPTICAL-IF-CROSS-CONNECT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Unsigned32, Bits, ObjectIdentity, IpAddress, ModuleIdentity, TimeTicks, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Unsigned32", "Bits", "ObjectIdentity", "IpAddress", "ModuleIdentity", "TimeTicks", "Integer32", "Counter32")
TimeStamp, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString", "RowStatus")
ciscoOpticalIfCrossConnectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 68))
ciscoOpticalIfCrossConnectMIB.setRevisions(('2002-03-13 00:00', '2001-04-20 00:00',))
if mibBuilder.loadTexts: ciscoOpticalIfCrossConnectMIB.setLastUpdated('200203130000Z')
if mibBuilder.loadTexts: ciscoOpticalIfCrossConnectMIB.setOrganization('Cisco Systems, Inc.')
coifccMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 68, 1))
coifccMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 68, 2))
class CoifccCrossConnectOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("up", 1), ("down", 2), ("dormant", 3), ("unknown", 4))

coifccInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 1))
coifccCrossConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2))
coifccInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 1, 1), )
if mibBuilder.loadTexts: coifccInterfaceTable.setStatus('current')
coifccInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: coifccInterfaceEntry.setStatus('current')
coifccIfCrossConnectIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483547))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coifccIfCrossConnectIdentifier.setStatus('current')
coifccCcIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coifccCcIndexNext.setStatus('current')
coifccCcLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coifccCcLastChange.setStatus('current')
coifccCrossConnectTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3), )
if mibBuilder.loadTexts: coifccCrossConnectTable.setStatus('current')
coifccCrossConnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcIndex"), (0, "CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcLowIfIndex"), (0, "CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcHighIfIndex"))
if mibBuilder.loadTexts: coifccCrossConnectEntry.setStatus('current')
coifccCcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coifccCcIndex.setStatus('current')
coifccCcLowIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: coifccCcLowIfIndex.setStatus('current')
coifccCcHighIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: coifccCcHighIfIndex.setStatus('current')
coifccCcSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("electricalCrossConnect", 2), ("opticalCrossConnect", 3), ("autoSelect", 4))).clone('autoSelect')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: coifccCcSwitchType.setStatus('current')
coifccCcKind = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("provisioned", 1), ("automatic", 2), ("dynamic", 3), ("protection", 4), ("other", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: coifccCcKind.setStatus('current')
coifccCcCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coifccCcCreationTime.setStatus('current')
coifccCcL2HOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 7), CoifccCrossConnectOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coifccCcL2HOperStatus.setStatus('current')
coifccCcH2LOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 8), CoifccCrossConnectOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coifccCcH2LOperStatus.setStatus('current')
coifccCcL2HLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coifccCcL2HLastChange.setStatus('current')
coifccCcH2LLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coifccCcH2LLastChange.setStatus('current')
coifccCcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: coifccCcRowStatus.setStatus('current')
coifccCcL2HAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-400, 0))).setUnits('1/10ths of dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: coifccCcL2HAttenuation.setStatus('current')
coifccCcH2LAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-400, 0))).setUnits('1/10ths of dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: coifccCcH2LAttenuation.setStatus('current')
coifccMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 1))
coifccMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 2))
coifccMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 1, 1)).setObjects(("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccInterfaceGroup"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCrossConnectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coifccMIBCompliance = coifccMIBCompliance.setStatus('deprecated')
coifccMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 1, 2)).setObjects(("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccInterfaceGroup"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCrossConnectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coifccMIBComplianceRev1 = coifccMIBComplianceRev1.setStatus('current')
coifccInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 2, 1)).setObjects(("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccIfCrossConnectIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coifccInterfaceGroup = coifccInterfaceGroup.setStatus('current')
coifccCrossConnectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 2, 2)).setObjects(("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcIndexNext"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcLastChange"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcSwitchType"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcKind"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcCreationTime"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcL2HOperStatus"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcH2LOperStatus"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcL2HLastChange"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcH2LLastChange"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coifccCrossConnectGroup = coifccCrossConnectGroup.setStatus('current')
coifccAttenuationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 2, 3)).setObjects(("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcL2HAttenuation"), ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcH2LAttenuation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coifccAttenuationGroup = coifccAttenuationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", coifccMIBComplianceRev1=coifccMIBComplianceRev1, coifccCrossConnectGroup=coifccCrossConnectGroup, coifccCcKind=coifccCcKind, coifccCcIndex=coifccCcIndex, ciscoOpticalIfCrossConnectMIB=ciscoOpticalIfCrossConnectMIB, coifccMIBCompliance=coifccMIBCompliance, coifccCcRowStatus=coifccCcRowStatus, coifccCcHighIfIndex=coifccCcHighIfIndex, coifccInterfaceEntry=coifccInterfaceEntry, PYSNMP_MODULE_ID=ciscoOpticalIfCrossConnectMIB, coifccIfCrossConnectIdentifier=coifccIfCrossConnectIdentifier, coifccMIBCompliances=coifccMIBCompliances, coifccCcSwitchType=coifccCcSwitchType, coifccInterfaceTable=coifccInterfaceTable, coifccCcL2HOperStatus=coifccCcL2HOperStatus, coifccCrossConnectEntry=coifccCrossConnectEntry, coifccCrossConnect=coifccCrossConnect, CoifccCrossConnectOperStatus=CoifccCrossConnectOperStatus, coifccAttenuationGroup=coifccAttenuationGroup, coifccCcH2LLastChange=coifccCcH2LLastChange, coifccCcL2HLastChange=coifccCcL2HLastChange, coifccCcIndexNext=coifccCcIndexNext, coifccMIBGroups=coifccMIBGroups, coifccInterface=coifccInterface, coifccCcLastChange=coifccCcLastChange, coifccCcCreationTime=coifccCcCreationTime, coifccCrossConnectTable=coifccCrossConnectTable, coifccCcH2LAttenuation=coifccCcH2LAttenuation, coifccInterfaceGroup=coifccInterfaceGroup, coifccCcLowIfIndex=coifccCcLowIfIndex, coifccCcH2LOperStatus=coifccCcH2LOperStatus, coifccMIBObjects=coifccMIBObjects, coifccCcL2HAttenuation=coifccCcL2HAttenuation, coifccMIBConformance=coifccMIBConformance)
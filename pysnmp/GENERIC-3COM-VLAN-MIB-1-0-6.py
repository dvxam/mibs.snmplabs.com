#
# PySNMP MIB module GENERIC-3COM-VLAN-MIB-1-0-6 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GENERIC-3COM-VLAN-MIB-1-0-6
# Produced by pysmi-0.3.4 at Mon Apr 29 19:05:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, Gauge32, ObjectIdentity, Integer32, Unsigned32, Bits, NotificationType, MibIdentifier, Counter64, ModuleIdentity, IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Gauge32", "ObjectIdentity", "Integer32", "Unsigned32", "Bits", "NotificationType", "MibIdentifier", "Counter64", "ModuleIdentity", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
generic = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10))
genExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1))
genVirtual = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14))
a3ComVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1))
a3ComVlanProtocolsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2))
a3ComVirtualGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 3))
a3ComEncapsulationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4))
class A3ComVlanType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("vlanLayer2", 1), ("vlanUnspecifiedProtocols", 2), ("vlanIPProtocol", 3), ("vlanIPXProtocol", 4), ("vlanAppleTalkProtocol", 5), ("vlanXNSProtocol", 6), ("vlanISOProtocol", 7), ("vlanDECNetProtocol", 8), ("vlanNetBIOSProtocol", 9), ("vlanSNAProtocol", 10), ("vlanVINESProtocol", 11), ("vlanX25Protocol", 12), ("vlanIGMPProtocol", 13), ("vlanSessionLayer", 14), ("vlanNetBeui", 15), ("vlanLayeredProtocols", 16), ("vlanIPXIIProtocol", 17), ("vlanIPX8022Protocol", 18), ("vlanIPX8023Protocol", 19))

class A3ComVlanLayer3Type(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("vlanIPProtocol", 1), ("vlanIPXProtocol", 2), ("vlanAppleTalkProtocol", 3), ("vlanXNSProtocol", 4), ("vlanSNAProtocol", 5), ("vlanDECNetProtocol", 6), ("vlanNetBIOSProtocol", 7), ("vlanVINESProtocol", 8), ("vlanX25Protocol", 9), ("vlanIPXIIProtocol", 10), ("vlanIPX8022Protocol", 11), ("vlanIPX8023Protocol", 12))

a3ComVlanGlobalMappingTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1), )
if mibBuilder.loadTexts: a3ComVlanGlobalMappingTable.setStatus('mandatory')
a3ComVlanGlobalMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-6", "a3ComVlanGlobalMappingIdentifier"))
if mibBuilder.loadTexts: a3ComVlanGlobalMappingEntry.setStatus('mandatory')
a3ComVlanGlobalMappingIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIdentifier.setStatus('mandatory')
a3ComVlanGlobalMappingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIfIndex.setStatus('mandatory')
a3ComVlanIfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2), )
if mibBuilder.loadTexts: a3ComVlanIfTable.setStatus('mandatory')
a3ComVlanIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-6", "a3ComVlanIfIndex"))
if mibBuilder.loadTexts: a3ComVlanIfEntry.setStatus('mandatory')
a3ComVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: a3ComVlanIfIndex.setStatus('mandatory')
a3ComVlanIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfDescr.setStatus('mandatory')
a3ComVlanIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 3), A3ComVlanType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfType.setStatus('mandatory')
a3ComVlanIfGlobalIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfGlobalIdentifier.setStatus('mandatory')
a3ComVlanIfInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComVlanIfInfo.setStatus('mandatory')
a3ComVlanIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfStatus.setStatus('mandatory')
a3ComIpVlanTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1), )
if mibBuilder.loadTexts: a3ComIpVlanTable.setStatus('mandatory')
a3ComIpVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-6", "a3ComVlanIfIndex"))
if mibBuilder.loadTexts: a3ComIpVlanEntry.setStatus('mandatory')
a3ComIpVlanIpNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComIpVlanIpNetAddress.setStatus('mandatory')
a3ComIpVlanIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComIpVlanIpNetMask.setStatus('mandatory')
a3ComIpVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComIpVlanStatus.setStatus('mandatory')
a3ComVlanProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2), )
if mibBuilder.loadTexts: a3ComVlanProtocolTable.setStatus('mandatory')
a3ComVlanProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-6", "a3ComVlanProtocolIfIndex"), (0, "GENERIC-3COM-VLAN-MIB-1-0-6", "a3ComVlanProtocolIndex"))
if mibBuilder.loadTexts: a3ComVlanProtocolEntry.setStatus('mandatory')
a3ComVlanProtocolIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: a3ComVlanProtocolIfIndex.setStatus('mandatory')
a3ComVlanProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2, 1, 2), A3ComVlanLayer3Type())
if mibBuilder.loadTexts: a3ComVlanProtocolIndex.setStatus('mandatory')
a3ComVlanProtocolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 2, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanProtocolStatus.setStatus('mandatory')
class A3ComVlanEncapsType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vlanEncaps3ComProprietaryVLT", 1), ("vlanEncaps8021q", 2), ("vlanEncapsPre8021qONcore", 3))

a3ComVlanEncapsIfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1), )
if mibBuilder.loadTexts: a3ComVlanEncapsIfTable.setStatus('mandatory')
a3ComVlanEncapsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-6", "a3ComVlanEncapsIfIndex"))
if mibBuilder.loadTexts: a3ComVlanEncapsIfEntry.setStatus('mandatory')
a3ComVlanEncapsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: a3ComVlanEncapsIfIndex.setStatus('mandatory')
a3ComVlanEncapsIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 2), A3ComVlanEncapsType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfType.setStatus('mandatory')
a3ComVlanEncapsIfTag = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfTag.setStatus('mandatory')
a3ComVlanEncapsIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfStatus.setStatus('mandatory')
a3ComNextAvailableVirtIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComNextAvailableVirtIfIndex.setStatus('mandatory')
mibBuilder.exportSymbols("GENERIC-3COM-VLAN-MIB-1-0-6", a3ComVlanIfIndex=a3ComVlanIfIndex, generic=generic, a3ComVlanGroup=a3ComVlanGroup, a3ComVlanIfStatus=a3ComVlanIfStatus, a3ComVlanProtocolEntry=a3ComVlanProtocolEntry, a3ComVlanIfTable=a3ComVlanIfTable, a3ComIpVlanTable=a3ComIpVlanTable, genExperimental=genExperimental, a3ComIpVlanEntry=a3ComIpVlanEntry, a3ComIpVlanIpNetAddress=a3ComIpVlanIpNetAddress, a3ComVlanProtocolIfIndex=a3ComVlanProtocolIfIndex, a3ComVlanEncapsIfTable=a3ComVlanEncapsIfTable, a3ComVlanEncapsIfEntry=a3ComVlanEncapsIfEntry, a3ComNextAvailableVirtIfIndex=a3ComNextAvailableVirtIfIndex, a3ComIpVlanStatus=a3ComIpVlanStatus, a3ComVlanGlobalMappingIfIndex=a3ComVlanGlobalMappingIfIndex, a3ComVlanProtocolStatus=a3ComVlanProtocolStatus, A3ComVlanEncapsType=A3ComVlanEncapsType, A3ComVlanLayer3Type=A3ComVlanLayer3Type, a3Com=a3Com, a3ComVlanProtocolsGroup=a3ComVlanProtocolsGroup, a3ComVlanIfDescr=a3ComVlanIfDescr, a3ComVlanIfType=a3ComVlanIfType, a3ComVlanIfInfo=a3ComVlanIfInfo, a3ComVlanEncapsIfIndex=a3ComVlanEncapsIfIndex, a3ComIpVlanIpNetMask=a3ComIpVlanIpNetMask, a3ComVlanProtocolTable=a3ComVlanProtocolTable, a3ComEncapsulationGroup=a3ComEncapsulationGroup, a3ComVlanGlobalMappingTable=a3ComVlanGlobalMappingTable, a3ComVlanGlobalMappingEntry=a3ComVlanGlobalMappingEntry, a3ComVlanEncapsIfStatus=a3ComVlanEncapsIfStatus, a3ComVlanGlobalMappingIdentifier=a3ComVlanGlobalMappingIdentifier, a3ComVlanIfEntry=a3ComVlanIfEntry, genVirtual=genVirtual, a3ComVirtualGroup=a3ComVirtualGroup, A3ComVlanType=A3ComVlanType, a3ComVlanEncapsIfTag=a3ComVlanEncapsIfTag, a3ComVlanProtocolIndex=a3ComVlanProtocolIndex, a3ComVlanIfGlobalIdentifier=a3ComVlanIfGlobalIdentifier, a3ComVlanEncapsIfType=a3ComVlanEncapsIfType)

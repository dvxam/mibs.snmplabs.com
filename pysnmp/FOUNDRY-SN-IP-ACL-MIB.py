#
# PySNMP MIB module FOUNDRY-SN-IP-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-SN-IP-ACL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
RtrStatus, = mibBuilder.importSymbols("FOUNDRY-SN-IP-MIB", "RtrStatus")
router, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "router")
PortQosTC, FdryVlanIdOrNoneTC = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "PortQosTC", "FdryVlanIdOrNoneTC")
ifIndex, InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, Bits, ObjectIdentity, Gauge32, TimeTicks, Counter64, ModuleIdentity, iso, MibIdentifier, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Bits", "ObjectIdentity", "Gauge32", "TimeTicks", "Counter64", "ModuleIdentity", "iso", "MibIdentifier", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, MacAddress, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "RowStatus", "TruthValue", "DisplayString")
snAgAcl = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15))
snAgAcl.setRevisions(('2014-01-28 00:00', '2011-03-02 00:00', '2010-06-02 00:00', '2009-09-30 00:00',))
if mibBuilder.loadTexts: snAgAcl.setLastUpdated('201103020000Z')
if mibBuilder.loadTexts: snAgAcl.setOrganization('Brocade Communications Systems, Inc.')
class SnRowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4))

class Action(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("deny", 0), ("permit", 1))

class TruthVal(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("false", 0), ("true", 1))

class FdryClauseIndexTC(TextualConvention, Unsigned32):
    status = 'current'

class AclNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 5100)

class AclNameString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Operator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 7))
    namedValues = NamedValues(("eq", 0), ("neq", 1), ("lt", 2), ("gt", 3), ("range", 4), ("undefined", 7))

class IpProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PrecedenceValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("routine", 0), ("priority", 1), ("immediate", 2), ("flash", 3), ("flashoverride", 4), ("critical", 5), ("internet", 6), ("network", 7), ("undefined", 8))

class TosValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("normal", 0), ("minMonetaryCost", 1), ("maxReliability", 2), ("tosValue3", 3), ("maxThroughput", 4), ("tosValue5", 5), ("tosValue6", 6), ("tosValue7", 7), ("minDelay", 8), ("tosValue9", 9), ("tosValue10", 10), ("tosValue11", 11), ("tosValue12", 12), ("tosValue13", 13), ("tosValue14", 14), ("tosValue15", 15), ("undefined", 16))

class Direction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inbound", 0), ("outbound", 1))

class FdryEnetTypeOrZeroTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("invalid", 0), ("ipv4", 1), ("arp", 2), ("ipv6", 3))

snAgAclGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1))
snAgAclGblCurRowIndex = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclGblCurRowIndex.setStatus('current')
snAgAclGblAcctEnable = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclGblAcctEnable.setStatus('current')
snAgAclGblIfIPv4AcctClear = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclGblIfIPv4AcctClear.setStatus('current')
snAgAclGblIfIPv6AcctClear = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclGblIfIPv6AcctClear.setStatus('current')
snAgAclGblRebindAclNumber = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 5), AclNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclGblRebindAclNumber.setStatus('current')
snAgAclGblRebindAclName = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclGblRebindAclName.setStatus('current')
brcdPbrAclAccntFilterAclName = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdPbrAclAccntFilterAclName.setStatus('current')
brcdPbrAclAccntCounterType = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cumulative", 1), ("last5min", 2))).clone('cumulative')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdPbrAclAccntCounterType.setStatus('current')
snAgAclTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2), )
if mibBuilder.loadTexts: snAgAclTable.setStatus('current')
snAgAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1), ).setIndexNames((0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclIndex"))
if mibBuilder.loadTexts: snAgAclEntry.setStatus('current')
snAgAclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclIndex.setStatus('current')
snAgAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 2), AclNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclNumber.setStatus('current')
snAgAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclName.setStatus('current')
snAgAclAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclAction.setStatus('current')
snAgAclProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 5), IpProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclProtocol.setStatus('current')
snAgAclSourceIp = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceIp.setStatus('current')
snAgAclSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceMask.setStatus('current')
snAgAclSourceOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 8), Operator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceOperator.setStatus('current')
snAgAclSourceOperand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceOperand1.setStatus('current')
snAgAclSourceOperand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceOperand2.setStatus('current')
snAgAclDestinationIp = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationIp.setStatus('current')
snAgAclDestinationMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationMask.setStatus('current')
snAgAclDestinationOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 13), Operator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationOperator.setStatus('current')
snAgAclDestinationOperand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationOperand1.setStatus('current')
snAgAclDestinationOperand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationOperand2.setStatus('current')
snAgAclPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 16), PrecedenceValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPrecedence.setStatus('current')
snAgAclTos = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 17), TosValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclTos.setStatus('current')
snAgAclEstablished = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 18), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclEstablished.setStatus('current')
snAgAclLogOption = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 19), TruthVal()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclLogOption.setStatus('current')
snAgAclStandardFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 20), TruthVal()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclStandardFlag.setStatus('current')
snAgAclRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 21), SnRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclRowStatus.setStatus('current')
snAgAclFlowCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclFlowCounter.setStatus('current')
snAgAclPacketCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclPacketCounter.setStatus('current')
snAgAclComments = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 24), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclComments.setStatus('current')
snAgAclIpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclIpPriority.setStatus('current')
snAgAclPriorityForce = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPriorityForce.setStatus('current')
snAgAclPriorityMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPriorityMapping.setStatus('current')
snAgAclDscpMarking = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDscpMarking.setStatus('current')
snAgAclDscpMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDscpMapping.setStatus('current')
snAgAclIcmpCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclIcmpCode.setStatus('current')
snAgAclParameters = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 31), Bits().clone(namedValues=NamedValues(("matchFragmentedPackets", 0), ("matchNonFragmentedPackets", 1), ("matchTcpSynSetPackets", 2), ("permitFailedRPFCheckPackets", 3), ("mirrorPermitPackets", 4), ("sendPermitPacketsToSflowCollector", 5), ("dscpMappingFlagSet", 6), ("dscpMarkingFlagSet", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclParameters.setStatus('current')
snAgAclVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 32), FdryVlanIdOrNoneTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgAclVlanId.setStatus('current')
snAgAclClauseString = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 33), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclClauseString.setStatus('current')
snAgAclBindToPortTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3), )
if mibBuilder.loadTexts: snAgAclBindToPortTable.setStatus('current')
snAgAclBindToPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1), ).setIndexNames((0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclPortNum"), (0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclPortBindDirection"))
if mibBuilder.loadTexts: snAgAclBindToPortEntry.setStatus('current')
snAgAclPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclPortNum.setStatus('current')
snAgAclPortBindDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 2), Direction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclPortBindDirection.setStatus('current')
snAgAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclNum.setStatus('current')
snAgAclNameString = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclNameString.setStatus('current')
snAgBindPortListInVirtualInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgBindPortListInVirtualInterface.setStatus('current')
snAgAclPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 6), SnRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPortRowStatus.setStatus('current')
snAgAclIfBindTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4), )
if mibBuilder.loadTexts: snAgAclIfBindTable.setStatus('current')
snAgAclIfBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1), ).setIndexNames((0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclIfBindIndex"), (0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclIfBindDirection"))
if mibBuilder.loadTexts: snAgAclIfBindEntry.setStatus('current')
snAgAclIfBindIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclIfBindIndex.setStatus('current')
snAgAclIfBindDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 2), Direction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclIfBindDirection.setStatus('current')
snAgAclIfBindNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 199))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgAclIfBindNum.setStatus('current')
snAgAclIfBindName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgAclIfBindName.setStatus('current')
snAgAclIfBindVifPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgAclIfBindVifPortList.setStatus('current')
snAgAclIfBindRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 6), SnRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgAclIfBindRowStatus.setStatus('current')
snAgAclIfBindDenyLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgAclIfBindDenyLogging.setStatus('current')
snAgAclIfIpv6BindName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgAclIfIpv6BindName.setStatus('current')
agAclAccntTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5), )
if mibBuilder.loadTexts: agAclAccntTable.setStatus('current')
agAclAccntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1), ).setIndexNames((0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntKind"), (0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntIfIndex"), (0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntDirection"), (0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntAclNumber"), (0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntFilterId"))
if mibBuilder.loadTexts: agAclAccntEntry.setStatus('current')
agAclAccntKind = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3, 4, 5, 7))).clone(namedValues=NamedValues(("ipv4", 0), ("l2", 1), ("rateLimit", 3), ("receiveAcl", 4), ("ipv6", 5), ("ipv6ReceiveAcl", 7))))
if mibBuilder.loadTexts: agAclAccntKind.setStatus('current')
agAclAccntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: agAclAccntIfIndex.setStatus('current')
agAclAccntDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 3), Direction())
if mibBuilder.loadTexts: agAclAccntDirection.setStatus('current')
agAclAccntAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 4), AclNumber())
if mibBuilder.loadTexts: agAclAccntAclNumber.setStatus('current')
agAclAccntFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 5), Unsigned32())
if mibBuilder.loadTexts: agAclAccntFilterId.setStatus('current')
agAclAccntAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 6), AclNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntAclName.setStatus('current')
agAclAccntOneSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntOneSecond.setStatus('current')
agAclAccntOneMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntOneMinute.setStatus('current')
agAclAccntFiveMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntFiveMinute.setStatus('current')
agAclAccntCumulative = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntCumulative.setStatus('current')
agAclAccntRaclDropCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntRaclDropCnt.setStatus('current')
agAclAccntRaclFwdCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntRaclFwdCnt.setStatus('current')
agAclAccntRaclRemarkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntRaclRemarkCnt.setStatus('current')
agAclAccntRaclTotalCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntRaclTotalCnt.setStatus('current')
agAclAccntRaclTotalSWHitCountCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agAclAccntRaclTotalSWHitCountCnt.setStatus('current')
fdryL2AclNextClauseTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 6), )
if mibBuilder.loadTexts: fdryL2AclNextClauseTable.setStatus('current')
fdryL2AclNextClauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 6, 1), ).setIndexNames((0, "FOUNDRY-SN-IP-ACL-MIB", "fdryL2AclNumber"))
if mibBuilder.loadTexts: fdryL2AclNextClauseEntry.setStatus('current')
fdryL2AclNextClauseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 6, 1, 1), FdryClauseIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryL2AclNextClauseIndex.setStatus('current')
fdryL2AclTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7), )
if mibBuilder.loadTexts: fdryL2AclTable.setStatus('current')
fdryL2AclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1), ).setIndexNames((0, "FOUNDRY-SN-IP-ACL-MIB", "fdryL2AclNumber"), (0, "FOUNDRY-SN-IP-ACL-MIB", "fdryL2AclClauseIndex"))
if mibBuilder.loadTexts: fdryL2AclEntry.setStatus('current')
fdryL2AclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 1), AclNumber())
if mibBuilder.loadTexts: fdryL2AclNumber.setStatus('current')
fdryL2AclClauseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 2), FdryClauseIndexTC())
if mibBuilder.loadTexts: fdryL2AclClauseIndex.setStatus('current')
fdryL2AclAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 3), Action()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclAction.setStatus('current')
fdryL2AclSourceMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 4), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclSourceMac.setStatus('current')
fdryL2AclSourceMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 5), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclSourceMacMask.setStatus('current')
fdryL2AclDestinationMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 6), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclDestinationMac.setStatus('current')
fdryL2AclDestinationMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 7), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclDestinationMacMask.setStatus('current')
fdryL2AclVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 8), FdryVlanIdOrNoneTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclVlanId.setStatus('current')
fdryL2AclEthernetType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 9), FdryEnetTypeOrZeroTC().clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclEthernetType.setStatus('current')
fdryL2AclDot1pPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 10), PortQosTC().clone('level0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclDot1pPriority.setStatus('current')
fdryL2AclDot1pPriorityForce = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 11), PortQosTC().clone('level0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclDot1pPriorityForce.setStatus('current')
fdryL2AclDot1pPriorityMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 12), PortQosTC().clone('level0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclDot1pPriorityMapping.setStatus('current')
fdryL2AclMirrorPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 13), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclMirrorPackets.setStatus('current')
fdryL2AclLogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclLogEnable.setStatus('current')
fdryL2AclRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclRowStatus.setStatus('current')
fdryL2AclIfBindTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8), )
if mibBuilder.loadTexts: fdryL2AclIfBindTable.setStatus('current')
fdryL2AclIfBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FOUNDRY-SN-IP-ACL-MIB", "fdryL2AclIfBindDirection"))
if mibBuilder.loadTexts: fdryL2AclIfBindEntry.setStatus('current')
fdryL2AclIfBindDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8, 1, 1), Direction())
if mibBuilder.loadTexts: fdryL2AclIfBindDirection.setStatus('current')
fdryL2AclIfBindAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclIfBindAclNumber.setStatus('current')
fdryL2AclIfBindRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryL2AclIfBindRowStatus.setStatus('current')
brcdPbrAclAccntTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9), )
if mibBuilder.loadTexts: brcdPbrAclAccntTable.setStatus('current')
brcdPbrAclAccntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1), ).setIndexNames((0, "FOUNDRY-SN-IP-ACL-MIB", "brcdPbrAclAccntKind"), (0, "FOUNDRY-SN-IP-ACL-MIB", "brcdPbrAclAccntIfIndex"), (0, "FOUNDRY-SN-IP-ACL-MIB", "brcdPbrSerialNumber"))
if mibBuilder.loadTexts: brcdPbrAclAccntEntry.setStatus('current')
brcdPbrAclAccntKind = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4PolicyBasedRouting", 1), ("ipv6PolicyBasedRouting", 2))))
if mibBuilder.loadTexts: brcdPbrAclAccntKind.setStatus('current')
brcdPbrAclAccntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: brcdPbrAclAccntIfIndex.setStatus('current')
brcdPbrSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: brcdPbrSerialNumber.setStatus('current')
brcdPbrAclAccntAclInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdPbrAclAccntAclInfo.setStatus('current')
mibBuilder.exportSymbols("FOUNDRY-SN-IP-ACL-MIB", fdryL2AclNextClauseEntry=fdryL2AclNextClauseEntry, snAgAclNumber=snAgAclNumber, fdryL2AclTable=fdryL2AclTable, fdryL2AclNextClauseIndex=fdryL2AclNextClauseIndex, snAgAclIfBindDirection=snAgAclIfBindDirection, agAclAccntRaclTotalSWHitCountCnt=agAclAccntRaclTotalSWHitCountCnt, snAgAclIfIpv6BindName=snAgAclIfIpv6BindName, snAgAclGlobal=snAgAclGlobal, fdryL2AclDot1pPriority=fdryL2AclDot1pPriority, snAgAclIfBindIndex=snAgAclIfBindIndex, snAgAclName=snAgAclName, fdryL2AclIfBindAclNumber=fdryL2AclIfBindAclNumber, snAgAclDestinationIp=snAgAclDestinationIp, PrecedenceValue=PrecedenceValue, snAgAclGblIfIPv6AcctClear=snAgAclGblIfIPv6AcctClear, Direction=Direction, FdryClauseIndexTC=FdryClauseIndexTC, brcdPbrAclAccntFilterAclName=brcdPbrAclAccntFilterAclName, snAgAclDscpMarking=snAgAclDscpMarking, snAgAclIfBindTable=snAgAclIfBindTable, fdryL2AclEthernetType=fdryL2AclEthernetType, fdryL2AclClauseIndex=fdryL2AclClauseIndex, snAgAclNum=snAgAclNum, snAgAclRowStatus=snAgAclRowStatus, snAgAclDestinationOperator=snAgAclDestinationOperator, snAgAclBindToPortEntry=snAgAclBindToPortEntry, snAgAclDestinationOperand1=snAgAclDestinationOperand1, snAgAclSourceOperator=snAgAclSourceOperator, fdryL2AclIfBindRowStatus=fdryL2AclIfBindRowStatus, brcdPbrAclAccntIfIndex=brcdPbrAclAccntIfIndex, snAgAclVlanId=snAgAclVlanId, agAclAccntRaclTotalCnt=agAclAccntRaclTotalCnt, snAgAclIfBindRowStatus=snAgAclIfBindRowStatus, brcdPbrAclAccntEntry=brcdPbrAclAccntEntry, snAgAclTos=snAgAclTos, snAgAclPrecedence=snAgAclPrecedence, brcdPbrAclAccntCounterType=brcdPbrAclAccntCounterType, agAclAccntFilterId=agAclAccntFilterId, agAclAccntRaclFwdCnt=agAclAccntRaclFwdCnt, agAclAccntFiveMinute=agAclAccntFiveMinute, fdryL2AclDot1pPriorityForce=fdryL2AclDot1pPriorityForce, TosValue=TosValue, fdryL2AclIfBindDirection=fdryL2AclIfBindDirection, snAgAclClauseString=snAgAclClauseString, fdryL2AclMirrorPackets=fdryL2AclMirrorPackets, snAgAclDestinationOperand2=snAgAclDestinationOperand2, snAgAcl=snAgAcl, AclNameString=AclNameString, snAgAclIndex=snAgAclIndex, IpProtocol=IpProtocol, AclNumber=AclNumber, SnRowStatus=SnRowStatus, agAclAccntRaclRemarkCnt=agAclAccntRaclRemarkCnt, snAgAclSourceOperand2=snAgAclSourceOperand2, fdryL2AclIfBindTable=fdryL2AclIfBindTable, fdryL2AclVlanId=fdryL2AclVlanId, snAgAclFlowCounter=snAgAclFlowCounter, snAgAclEstablished=snAgAclEstablished, snAgAclGblIfIPv4AcctClear=snAgAclGblIfIPv4AcctClear, snAgAclLogOption=snAgAclLogOption, fdryL2AclDestinationMacMask=fdryL2AclDestinationMacMask, brcdPbrAclAccntAclInfo=brcdPbrAclAccntAclInfo, snAgAclSourceOperand1=snAgAclSourceOperand1, snAgAclPacketCounter=snAgAclPacketCounter, snAgAclIfBindDenyLogging=snAgAclIfBindDenyLogging, snAgAclGblCurRowIndex=snAgAclGblCurRowIndex, TruthVal=TruthVal, Action=Action, snAgAclIpPriority=snAgAclIpPriority, snAgAclPriorityMapping=snAgAclPriorityMapping, fdryL2AclDestinationMac=fdryL2AclDestinationMac, brcdPbrAclAccntTable=brcdPbrAclAccntTable, PYSNMP_MODULE_ID=snAgAcl, FdryEnetTypeOrZeroTC=FdryEnetTypeOrZeroTC, agAclAccntCumulative=agAclAccntCumulative, snAgAclGblRebindAclName=snAgAclGblRebindAclName, fdryL2AclLogEnable=fdryL2AclLogEnable, snAgAclSourceMask=snAgAclSourceMask, fdryL2AclRowStatus=fdryL2AclRowStatus, fdryL2AclIfBindEntry=fdryL2AclIfBindEntry, snAgAclDestinationMask=snAgAclDestinationMask, snAgAclIfBindEntry=snAgAclIfBindEntry, snAgAclPortRowStatus=snAgAclPortRowStatus, brcdPbrAclAccntKind=brcdPbrAclAccntKind, snAgAclIcmpCode=snAgAclIcmpCode, agAclAccntOneSecond=agAclAccntOneSecond, fdryL2AclNumber=fdryL2AclNumber, snAgAclAction=snAgAclAction, fdryL2AclNextClauseTable=fdryL2AclNextClauseTable, fdryL2AclAction=fdryL2AclAction, agAclAccntRaclDropCnt=agAclAccntRaclDropCnt, snAgAclPortNum=snAgAclPortNum, snAgAclSourceIp=snAgAclSourceIp, fdryL2AclSourceMac=fdryL2AclSourceMac, snAgAclPriorityForce=snAgAclPriorityForce, agAclAccntDirection=agAclAccntDirection, fdryL2AclDot1pPriorityMapping=fdryL2AclDot1pPriorityMapping, agAclAccntAclName=agAclAccntAclName, Operator=Operator, snAgAclComments=snAgAclComments, snAgAclIfBindVifPortList=snAgAclIfBindVifPortList, snAgAclProtocol=snAgAclProtocol, snAgAclNameString=snAgAclNameString, snAgAclGblAcctEnable=snAgAclGblAcctEnable, agAclAccntEntry=agAclAccntEntry, agAclAccntOneMinute=agAclAccntOneMinute, snAgAclStandardFlag=snAgAclStandardFlag, snAgAclIfBindNum=snAgAclIfBindNum, snAgAclIfBindName=snAgAclIfBindName, agAclAccntKind=agAclAccntKind, snAgAclParameters=snAgAclParameters, agAclAccntTable=agAclAccntTable, snAgAclDscpMapping=snAgAclDscpMapping, agAclAccntAclNumber=agAclAccntAclNumber, snAgAclBindToPortTable=snAgAclBindToPortTable, snAgAclGblRebindAclNumber=snAgAclGblRebindAclNumber, snAgAclTable=snAgAclTable, fdryL2AclSourceMacMask=fdryL2AclSourceMacMask, snAgBindPortListInVirtualInterface=snAgBindPortListInVirtualInterface, fdryL2AclEntry=fdryL2AclEntry, snAgAclPortBindDirection=snAgAclPortBindDirection, brcdPbrSerialNumber=brcdPbrSerialNumber, snAgAclEntry=snAgAclEntry, agAclAccntIfIndex=agAclAccntIfIndex)
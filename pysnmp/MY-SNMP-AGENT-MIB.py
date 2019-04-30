#
# PySNMP MIB module MY-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-SNMP-AGENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
ConfigStatus, MyTrapType = mibBuilder.importSymbols("MY-TC", "ConfigStatus", "MyTrapType")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Bits, Integer32, Counter64, TimeTicks, MibIdentifier, Gauge32, ObjectIdentity, NotificationType, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Integer32", "Counter64", "TimeTicks", "MibIdentifier", "Gauge32", "ObjectIdentity", "NotificationType", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
mySnmpAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5))
mySnmpAgentMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: mySnmpAgentMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: mySnmpAgentMIB.setOrganization('D-Link Crop.')
mySnmpAgentMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1))
mySnmpCommunityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1))
mySnmpTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2))
class Community(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

myCommunityMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCommunityMaxNum.setStatus('current')
myCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2), )
if mibBuilder.loadTexts: myCommunityTable.setStatus('current')
myCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1), ).setIndexNames((0, "MY-SNMP-AGENT-MIB", "myCommunityName"))
if mibBuilder.loadTexts: myCommunityEntry.setStatus('current')
myCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 1), Community()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCommunityName.setStatus('current')
myCommunityWritable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readonly", 1), ("writable", 2))).clone('readonly')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myCommunityWritable.setStatus('current')
myCommunityUserIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myCommunityUserIpAddr.setStatus('current')
myCommunityEnableIpAddrAuthen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 4), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myCommunityEnableIpAddrAuthen.setStatus('current')
myCommunityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myCommunityStatus.setStatus('current')
myTrapDstMaxNumber = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myTrapDstMaxNumber.setStatus('current')
myTrapDstTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2), )
if mibBuilder.loadTexts: myTrapDstTable.setStatus('current')
myTrapDstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1), ).setIndexNames((0, "MY-SNMP-AGENT-MIB", "myTrapDstAddr"))
if mibBuilder.loadTexts: myTrapDstEntry.setStatus('current')
myTrapDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myTrapDstAddr.setStatus('current')
myTrapDstCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1, 2), Community().clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myTrapDstCommunity.setStatus('current')
myTrapDstSendTrapClass = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("snmpv1-Trap", 1), ("snmpv2c-Trap", 2))).clone('snmpv1-Trap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myTrapDstSendTrapClass.setStatus('current')
myTrapDstEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myTrapDstEntryStatus.setStatus('current')
myTrapActionTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 3), )
if mibBuilder.loadTexts: myTrapActionTable.setStatus('current')
myTrapActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 3, 1), ).setIndexNames((0, "MY-SNMP-AGENT-MIB", "myTrapType"))
if mibBuilder.loadTexts: myTrapActionEntry.setStatus('current')
myTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 3, 1, 1), MyTrapType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myTrapType.setStatus('current')
myTrapAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("sendtrap", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myTrapAction.setStatus('current')
mySnmpAgentMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2))
mySnmpAgentMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 1))
mySnmpAgentMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 2))
mySnmpAgentMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 1, 1)).setObjects(("MY-SNMP-AGENT-MIB", "myCommunityMIBGroup"), ("MY-SNMP-AGENT-MIB", "mySnmpTrapMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mySnmpAgentMIBCompliance = mySnmpAgentMIBCompliance.setStatus('current')
myCommunityMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 2, 1)).setObjects(("MY-SNMP-AGENT-MIB", "myCommunityMaxNum"), ("MY-SNMP-AGENT-MIB", "myCommunityName"), ("MY-SNMP-AGENT-MIB", "myCommunityWritable"), ("MY-SNMP-AGENT-MIB", "myCommunityUserIpAddr"), ("MY-SNMP-AGENT-MIB", "myCommunityEnableIpAddrAuthen"), ("MY-SNMP-AGENT-MIB", "myCommunityStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myCommunityMIBGroup = myCommunityMIBGroup.setStatus('current')
mySnmpTrapMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 5, 2, 2, 2)).setObjects(("MY-SNMP-AGENT-MIB", "myTrapDstSendTrapClass"), ("MY-SNMP-AGENT-MIB", "myTrapDstMaxNumber"), ("MY-SNMP-AGENT-MIB", "myTrapDstAddr"), ("MY-SNMP-AGENT-MIB", "myTrapDstCommunity"), ("MY-SNMP-AGENT-MIB", "myTrapDstEntryStatus"), ("MY-SNMP-AGENT-MIB", "myTrapType"), ("MY-SNMP-AGENT-MIB", "myTrapAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mySnmpTrapMIBGroup = mySnmpTrapMIBGroup.setStatus('current')
mibBuilder.exportSymbols("MY-SNMP-AGENT-MIB", mySnmpAgentMIBCompliance=mySnmpAgentMIBCompliance, myTrapType=myTrapType, mySnmpAgentMIBCompliances=mySnmpAgentMIBCompliances, mySnmpAgentMIBGroups=mySnmpAgentMIBGroups, myCommunityWritable=myCommunityWritable, mySnmpAgentMIBObjects=mySnmpAgentMIBObjects, myCommunityStatus=myCommunityStatus, myTrapDstTable=myTrapDstTable, myCommunityEntry=myCommunityEntry, myTrapDstMaxNumber=myTrapDstMaxNumber, myTrapAction=myTrapAction, myCommunityUserIpAddr=myCommunityUserIpAddr, PYSNMP_MODULE_ID=mySnmpAgentMIB, mySnmpTrapMIBGroup=mySnmpTrapMIBGroup, myTrapDstEntry=myTrapDstEntry, myCommunityTable=myCommunityTable, myCommunityEnableIpAddrAuthen=myCommunityEnableIpAddrAuthen, Community=Community, myCommunityMIBGroup=myCommunityMIBGroup, mySnmpCommunityObjects=mySnmpCommunityObjects, myCommunityMaxNum=myCommunityMaxNum, myTrapDstEntryStatus=myTrapDstEntryStatus, myTrapDstCommunity=myTrapDstCommunity, myTrapDstAddr=myTrapDstAddr, myTrapActionEntry=myTrapActionEntry, mySnmpAgentMIBConformance=mySnmpAgentMIBConformance, myTrapDstSendTrapClass=myTrapDstSendTrapClass, myCommunityName=myCommunityName, mySnmpAgentMIB=mySnmpAgentMIB, myTrapActionTable=myTrapActionTable, mySnmpTrapObjects=mySnmpTrapObjects)
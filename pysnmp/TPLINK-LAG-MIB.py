#
# PySNMP MIB module TPLINK-LAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-LAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, MibIdentifier, Counter64, Gauge32, IpAddress, Counter32, TimeTicks, ObjectIdentity, Unsigned32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "MibIdentifier", "Counter64", "Gauge32", "IpAddress", "Counter32", "TimeTicks", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "NotificationType")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkLagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 9))
tplinkLagMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkLagMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkLagMIB.setOrganization('TPLINK')
tplinkLagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1))
tplinkLagNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 9, 2))
tplinkLagMIBGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 1))
tplinkLagTable = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2))
tplinkLagLacpManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3))
tpLagMaxEntryNum = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpLagMaxEntryNum.setStatus('current')
tpLagLoadBalance = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("mac-source", 0), ("mac-dest", 1), ("mac-source-dest", 2), ("ip-source", 3), ("ip-dest", 4), ("ip-source-dest", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpLagLoadBalance.setStatus('current')
tpLagTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3), )
if mibBuilder.loadTexts: tpLagTable.setStatus('current')
tpLagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1), ).setIndexNames((0, "TPLINK-LAG-MIB", "tpLagIndex"))
if mibBuilder.loadTexts: tpLagEntry.setStatus('current')
tpLagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpLagIndex.setStatus('current')
tpLagType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("active", 2), ("passive", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpLagType.setStatus('current')
tpLagMember = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpLagMember.setStatus('current')
tpLagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpLagRowStatus.setStatus('current')
tpLacpSystemPriority = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpLacpSystemPriority.setStatus('current')
tpLacpTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2), )
if mibBuilder.loadTexts: tpLacpTable.setStatus('current')
tpLacpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpLacpEntry.setStatus('current')
tpLacpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpLacpPort.setStatus('current')
tpLacpAdminKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpLacpAdminKey.setStatus('current')
tpLacpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpLacpPortPriority.setStatus('current')
tpLacpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("active", 1), ("passive", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpLacpMode.setStatus('current')
tpLacpChan = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpLacpChan.setStatus('current')
mibBuilder.exportSymbols("TPLINK-LAG-MIB", tpLacpSystemPriority=tpLacpSystemPriority, tpLagMaxEntryNum=tpLagMaxEntryNum, PYSNMP_MODULE_ID=tplinkLagMIB, tpLacpPortPriority=tpLacpPortPriority, tpLagType=tpLagType, tpLacpPort=tpLacpPort, tplinkLagLacpManage=tplinkLagLacpManage, tpLacpEntry=tpLacpEntry, tpLacpMode=tpLacpMode, tpLagTable=tpLagTable, tpLagLoadBalance=tpLagLoadBalance, tpLacpTable=tpLacpTable, tpLagMember=tpLagMember, tpLacpAdminKey=tpLacpAdminKey, tplinkLagNotifications=tplinkLagNotifications, tpLagRowStatus=tpLagRowStatus, tplinkLagMIB=tplinkLagMIB, tpLacpChan=tpLacpChan, tplinkLagMIBObjects=tplinkLagMIBObjects, tplinkLagTable=tplinkLagTable, tpLagEntry=tpLagEntry, tpLagIndex=tpLagIndex, tplinkLagMIBGlobalConfig=tplinkLagMIBGlobalConfig)
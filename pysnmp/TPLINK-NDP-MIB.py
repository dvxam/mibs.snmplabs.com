#
# PySNMP MIB module TPLINK-NDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-NDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, Gauge32, iso, TimeTicks, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, ModuleIdentity, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Gauge32", "iso", "TimeTicks", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "ModuleIdentity", "NotificationType", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ndpManage, = mibBuilder.importSymbols("TPLINK-CLUSTER-MIB", "ndpManage")
ndpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 1))
ndpStatus = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ndpStatus.setStatus('current')
ndpAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ndpAgingTime.setStatus('current')
ndpHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ndpHelloTime.setStatus('current')
ndpPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2), )
if mibBuilder.loadTexts: ndpPortTable.setStatus('current')
ndpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ndpPortEntry.setStatus('current')
ndpPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ndpPortStatus.setStatus('current')
ndpPortRecvPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ndpPortRecvPkt.setStatus('current')
ndpPortSendPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ndpPortSendPkt.setStatus('current')
ndpPortErrPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ndpPortErrPkt.setStatus('current')
ndpPortNeighborNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ndpPortNeighborNum.setStatus('current')
mibBuilder.exportSymbols("TPLINK-NDP-MIB", ndpHelloTime=ndpHelloTime, ndpPortRecvPkt=ndpPortRecvPkt, ndpAgingTime=ndpAgingTime, ndpPortStatus=ndpPortStatus, ndpPortNeighborNum=ndpPortNeighborNum, ndpPortTable=ndpPortTable, ndpStatus=ndpStatus, ndpPortErrPkt=ndpPortErrPkt, ndpPortSendPkt=ndpPortSendPkt, ndpGlobalConfig=ndpGlobalConfig, ndpPortEntry=ndpPortEntry)

#
# PySNMP MIB module Double-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Double-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:43:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Integer32, IpAddress, iso, Gauge32, Unsigned32, Counter64, TimeTicks, ObjectIdentity, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Integer32", "IpAddress", "iso", "Gauge32", "Unsigned32", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "MibIdentifier")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
swDoubleVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 28))
if mibBuilder.loadTexts: swDoubleVlanMIB.setLastUpdated('200601160000Z')
if mibBuilder.loadTexts: swDoubleVlanMIB.setOrganization('.')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swDoubleVlanCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 28, 1))
swDoubleVlanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 28, 2))
swDoubleVlanMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 28, 3))
swDoubleVlanGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 28, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDoubleVlanGlobalState.setStatus('current')
swDoubleVlanCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1), )
if mibBuilder.loadTexts: swDoubleVlanCtrlTable.setStatus('current')
swDoubleVlanCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1), ).setIndexNames((0, "Double-VLAN-MIB", "swDoubleVlanSPVIDIndex"))
if mibBuilder.loadTexts: swDoubleVlanCtrlEntry.setStatus('current')
swDoubleVlanSPVIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDoubleVlanSPVIDIndex.setStatus('current')
swDoubleVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDoubleVlanName.setStatus('current')
swDoubleVlanTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDoubleVlanTPID.setStatus('current')
swDoubleVlanUplinkPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDoubleVlanUplinkPorts.setStatus('current')
swDoubleVlanAccessPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDoubleVlanAccessPorts.setStatus('current')
swDoubleVlanUnknowPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 6), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDoubleVlanUnknowPorts.setStatus('current')
swDoubleVlanDeletePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 7), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDoubleVlanDeletePorts.setStatus('current')
swDoubleVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDoubleVlanStatus.setStatus('current')
mibBuilder.exportSymbols("Double-VLAN-MIB", swDoubleVlanCtrlTable=swDoubleVlanCtrlTable, swDoubleVlanTPID=swDoubleVlanTPID, swDoubleVlanUplinkPorts=swDoubleVlanUplinkPorts, swDoubleVlanUnknowPorts=swDoubleVlanUnknowPorts, swDoubleVlanDeletePorts=swDoubleVlanDeletePorts, PortList=PortList, swDoubleVlanName=swDoubleVlanName, swDoubleVlanCtrlEntry=swDoubleVlanCtrlEntry, swDoubleVlanCtrl=swDoubleVlanCtrl, swDoubleVlanInfo=swDoubleVlanInfo, swDoubleVlanAccessPorts=swDoubleVlanAccessPorts, swDoubleVlanSPVIDIndex=swDoubleVlanSPVIDIndex, swDoubleVlanMIB=swDoubleVlanMIB, PYSNMP_MODULE_ID=swDoubleVlanMIB, swDoubleVlanMgmt=swDoubleVlanMgmt, swDoubleVlanStatus=swDoubleVlanStatus, swDoubleVlanGlobalState=swDoubleVlanGlobalState)
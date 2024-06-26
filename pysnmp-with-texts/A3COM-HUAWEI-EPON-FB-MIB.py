#
# PySNMP MIB module A3COM-HUAWEI-EPON-FB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-EPON-FB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:04:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cEpon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cEpon")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32, Gauge32, ModuleIdentity, ObjectIdentity, NotificationType, Integer32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Integer32", "MibIdentifier", "Bits")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
h3cEponFBMibObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6))
if mibBuilder.loadTexts: h3cEponFBMibObjects.setLastUpdated('200711271008Z')
if mibBuilder.loadTexts: h3cEponFBMibObjects.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cEponFBMibObjects.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cEponFBMibObjects.setDescription(' The objects in this MIB module are used to manage and display current configuration of fiber backup groups based on EPON OLT port. ')
h3cEponFBMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1))
h3cEponFBMIBTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1, 1), )
if mibBuilder.loadTexts: h3cEponFBMIBTable.setStatus('current')
if mibBuilder.loadTexts: h3cEponFBMIBTable.setDescription('This table defines several optical fiber-backup system parameters.')
h3cEponFBMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-EPON-FB-MIB", "h3cEponFBGroupIndex"))
if mibBuilder.loadTexts: h3cEponFBMIBEntry.setStatus('current')
if mibBuilder.loadTexts: h3cEponFBMIBEntry.setDescription('The entry of h3cEponFBMIBTable.')
h3cEponFBGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cEponFBGroupIndex.setStatus('current')
if mibBuilder.loadTexts: h3cEponFBGroupIndex.setDescription('The EPON fiber-backup group ID.')
h3cEponFBGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEponFBGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cEponFBGroupRowStatus.setDescription('This object allows entry to be created and deleted from the h3cEponFBMIBTable.')
h3cEponFBMasterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEponFBMasterPort.setStatus('current')
if mibBuilder.loadTexts: h3cEponFBMasterPort.setDescription('OLT port ifindex of the fiber-backup group. Use it to set or get the group master port.')
h3cEponFBSlavePort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEponFBSlavePort.setStatus('current')
if mibBuilder.loadTexts: h3cEponFBSlavePort.setDescription('OLT port ifindex of the fiber-backup group. Use it to set or get the group slave port. h3cEponFBSlavePort must be set after h3cEponFBMasterPort. ')
h3cEponFBMasterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEponFBMasterPortStatus.setStatus('current')
if mibBuilder.loadTexts: h3cEponFBMasterPortStatus.setDescription("The master port status of the fiber-backup group. The active state indicates that the port's role is master, the olt chip is right and the optical module is inserted. The down state indicates others conditions.")
h3cEponFBSlavePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cEponFBSlavePortStatus.setStatus('current')
if mibBuilder.loadTexts: h3cEponFBSlavePortStatus.setDescription("The slave port status of the fiber-backup group. The ready state indicates that the port's role is slave, the olt chip is right and optical module is inserted. The down state indicates others conditions.")
h3cEponFBSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cEponFBSwitchover.setStatus('current')
if mibBuilder.loadTexts: h3cEponFBSwitchover.setDescription("Switch the fiber backup group's two port manually. The group must has two ports and the value of h3cEponFBSlavePortStatus must be ready before Switchover. after Switchover the port's role will be changed. The value true is for switch-over. The default value is false.")
mibBuilder.exportSymbols("A3COM-HUAWEI-EPON-FB-MIB", h3cEponFBMasterPortStatus=h3cEponFBMasterPortStatus, h3cEponFBMibObjects=h3cEponFBMibObjects, h3cEponFBGroupRowStatus=h3cEponFBGroupRowStatus, h3cEponFBSlavePort=h3cEponFBSlavePort, PYSNMP_MODULE_ID=h3cEponFBMibObjects, h3cEponFBMIBEntry=h3cEponFBMIBEntry, h3cEponFBSlavePortStatus=h3cEponFBSlavePortStatus, h3cEponFBMIB=h3cEponFBMIB, h3cEponFBMIBTable=h3cEponFBMIBTable, h3cEponFBGroupIndex=h3cEponFBGroupIndex, h3cEponFBSwitchover=h3cEponFBSwitchover, h3cEponFBMasterPort=h3cEponFBMasterPort)

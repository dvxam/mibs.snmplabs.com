#
# PySNMP MIB module NETI-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETI-COMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:09:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, enterprises, Counter32, ModuleIdentity, MibIdentifier, Counter64, Integer32, TimeTicks, IpAddress, NotificationType, Unsigned32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "enterprises", "Counter32", "ModuleIdentity", "MibIdentifier", "Counter64", "Integer32", "TimeTicks", "IpAddress", "NotificationType", "Unsigned32", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netinsight = ModuleIdentity((1, 3, 6, 1, 4, 1, 2928))
netinsight.setRevisions(('2014-10-23 13:00', '2014-04-01 10:00', '2013-10-10 09:00', '2013-06-03 11:00', '2013-01-30 13:00', '2012-09-12 11:00', '2012-03-22 09:20', '2012-03-16 13:00', '2011-03-25 14:00', '2010-11-10 08:00', '2010-02-04 15:00', '2008-12-19 14:00', '2008-12-12 13:00', '2008-10-15 12:00', '2008-06-19 10:00', '2007-07-31 15:00', '2007-01-26 11:00', '2006-08-17 08:30', '2005-12-15 00:00', '2003-03-25 00:00',))
if mibBuilder.loadTexts: netinsight.setLastUpdated('201410231300Z')
if mibBuilder.loadTexts: netinsight.setOrganization('Net Insight AB')
class FaultStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("fault", 2))

netiReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1))
nimbraOne = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1))
nimbra101 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 2))
nimbra210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 3))
nimbra220 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 4))
nimbra290 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 5))
nimbraTwo = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 6))
netiRegGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 7))
nimbra291 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 8))
nimbra340 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9))
nimbra680 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10))
nimbra340HD = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 11))
nimbra360 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 12))
nimbra360Gold = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 12, 1))
nimbra688 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 13))
nimbra130 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 14))
nimbra380 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 15))
nimbra230 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 16))
nimbra320 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 17))
nimbra140 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 18))
nimbra310 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 19))
nimbra240 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 20))
nimbra640 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 21))
nimbraVA210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 22))
nimbraVA210FV = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 22, 1))
nimbraVA210DCV1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 22, 2))
nimbraVA210DCV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 22, 3))
nimbra390 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 23))
nimbraVA220 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 25))
nimbraOneChassisTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 1))
nimbraOneBaseUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 1, 1))
nimbraOneBackplaneTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 2))
nimbraOneBackplane = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 2, 1))
nimbraOneContainerTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 3))
nimbraOneSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 3, 1))
nimbraOnePowerSupplyTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 4))
nimbraOnePowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 4, 1))
nimbraOneFanTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 5))
nimbraOneFan = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 5, 1))
nimbraOneModuleTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6))
nimbraOneModuleTypesMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 1))
nimbraOneModuleTypesMgmtControlModule = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 1, 1))
nimbraOneModuleTypesDtm = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2))
nimbraOneModuleTypesDtm850ShortHaulRight = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 1))
nimbraOneModuleTypesDtm850ShortHaulLeft = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 2))
nimbraOneModuleTypesDtm850LongHaulRight = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 3))
nimbraOneModuleTypesDtm850LongHaulLeft = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 4))
nimbraOneModuleTypesDtm1000ShortHaulRight = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 5))
nimbraOneModuleTypesDtm1000ShortHaulLeft = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 6))
nimbraOneModuleTypesDtm1000LongHaulRight = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 7))
nimbraOneModuleTypesDtm1000LongHaulLeft = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 8))
nimbraOneModuleTypesDtm150Right = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 9))
nimbraOneModuleTypesDtm150Left = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 10))
nimbraOneModuleTypesDtm622 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 11))
nimbraOneModuleTypesTrunk1Gbps = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 12))
nimbraOneModuleTypesTrunkDS3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 13))
nimbraOneModuleTypesTrunkOC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 14))
nimbraOneModuleTypesTrunk4xOC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 15))
nimbraOneModuleTypesTrunkOC12 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 16))
nimbraOneModuleTypesTrunkOC48 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 17))
nimbraOneModuleTypesTrunk3xIP = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 18))
nimbraOneModuleTypesAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3))
nimbraOneModuleTypesAccessE1Right = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 1))
nimbraOneModuleTypesAccessE1Left = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 2))
nimbraOneModuleTypesAccessT1Right = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 3))
nimbraOneModuleTypesAccessT1Left = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 4))
nimbraOneModuleTypesAccessVideo270Right = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 5))
nimbraOneModuleTypesAccessVideo270Left = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 6))
nimbraOneModuleTypesAccessEthernet8pRight = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 7))
nimbraOneModuleTypesAccessEthernet8pLeft = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 8))
nimbraOneModuleTypesAccessGigabitEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 9))
nimbraOneModuleTypesAccessASIRight = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 11))
nimbraOneModuleTypesAccessASILeft = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 12))
nimbraOneModuleTypesAccessGbE = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 13))
nimbraOneModuleTypesAccess8xEth = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 14))
nimbraOneModuleTypesAccessASI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 15))
nimbraOneModuleTypesAccessSDI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 16))
nimbraOneModuleTypesAccess4xOC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 17))
nimbraOneModuleTypesAccessE1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 18))
nimbraOneModuleTypesAccessT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 19))
nimbraOneModuleTypesAccess8xASI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 20))
nimbraOneModuleTypesAccess8xAESEBU = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 21))
nimbraOneModuleTypesTrunkAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 4))
nimbraOneModuleTypesTrunkAccess4xDS3E3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 4, 1))
nimbraOneModuleTypesAux = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 5))
nimbraOneModuleTypesAuxGPIO = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 5, 1))
nimbraOneThermometerTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 7))
nimbraOneThermometer = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 1, 7, 1))
nimbra290ChassisTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 5, 1))
nimbra290BaseUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 5, 1, 1))
nimbra290PowerSupplyTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 5, 2))
nimbra290PowerUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 5, 2, 1))
nimbra290FanTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 5, 3))
nimbra290Fan = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 5, 3, 1))
nimbra340ChassisTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 1))
nimbra340ContainerTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 3))
nimbra340PowerSupplyTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 4))
nimbra340FanTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 5))
nimbra340ModuleTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6))
nimbra340ModuleTypesMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 1))
nimbra340ModuleTypesMgmtControlModule = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 1, 1))
nimbra340ModuleTypesDtm = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2))
nimbra340ModuleTypesTrunk1Gbps = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 1))
nimbra340ModuleTypesTrunkDS3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 2))
nimbra340ModuleTypesTrunkOC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 3))
nimbra340ModuleTypesTrunk4xOC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 4))
nimbra340ModuleTypesTrunkOC12 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 5))
nimbra340ModuleTypesTrunkOC48 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 6))
nimbra340ModuleTypesTrunk3xIP = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 7))
nimbra340ModuleTypesAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3))
nimbra340ModuleTypesAccessGbE = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 1))
nimbra340ModuleTypesAccess8xEth = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 2))
nimbra340ModuleTypesAccessASI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 3))
nimbra340ModuleTypesAccessSDI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 4))
nimbra340ModuleTypesAccess4xOC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 5))
nimbra340ModuleTypesAccessE1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 6))
nimbra340ModuleTypesAccessT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 7))
nimbra340ModuleTypesAccess8xASI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 8))
nimbra340ModuleTypesAccessHDSDI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 9))
nimbra340ModuleTypesAccess8xAESEBU = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 10))
nimbra340ModuleTypesAccess8xSDI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 11))
nimbra360ModuleTypesDtm = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 4))
nimbra360ModuleTypesTrunkFunction = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 4, 1))
nimbra340ModuleTypesAux = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 5))
nimbra340ModuleTypesAuxGPIO = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 5, 1))
nimbra340ModuleTypesTrunkAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 6))
nimbra340ModuleTypesTrunkAccess4xDS3E3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 6, 1))
nimbra380ModuleTypesAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 7))
nimbra380ModuleTypesAccess8xGbE = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 7, 1))
nimbra340ThermometerTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 7))
nimbra340Thermometer = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 9, 7, 1))
nimbra680ChassisTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 1))
nimbra680ContainerTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 3))
nimbra680PowerSupplyTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 4))
nimbra680FanTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 5))
nimbra680ModuleTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6))
nimbra680PowerSupplyTypesPCU = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 4, 1))
nimbra680PowerSupplyTypesPSU = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 4, 2))
nimbra680FanTypesFan = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 5, 1))
nimbra680ModuleTypesMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 1))
nimbra680ModuleTypesMgmtControlModule = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 1, 1))
nimbra680ModuleTypesIf = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2))
nimbra680ModuleTypesIfTrunk4xOC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 1))
nimbra680ModuleTypesIfTrunk4xOC12 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 2))
nimbra680ModuleTypesIfTrunk2xOC48 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 3))
nimbra680ModuleTypesIfTrunk4xOC48 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 4))
nimbra680ModuleTypesIfTrunkOC192 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 5))
nimbra680ModuleTypesIfTrunk6xIP = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 6))
nimbra680ModuleTypesSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 3))
nimbra680ModuleTypesSwitch40Gbps = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 3, 1))
nimbra680ModuleTypesSwitch80Gbps = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 3, 2))
nimbra680ModuleTypesSwitch160Gbps = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 3, 3))
nimbra680ModuleTypesAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4))
nimbra680ModuleTypesAccess8xHDSDI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 1))
nimbra680ModuleTypesAccess8xGbE = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 2))
nimbra680ModuleTypesAccess8xASI = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 3))
nimbra680ModuleTypesAccess8x3Gbps = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 4))
nimbra680ModuleTypesAccess8xJPEG2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 5))
nimbra680ModuleTypesAccess8xVideo = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 6))
nimbra680ModuleTypesAccess8xASIAES = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 7))
nimbra680ModuleTypesAccess2x10GbE = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 8))
nimbra680ModuleTypesAux = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 5))
nimbra680ModuleTypesAuxGPIO = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 5, 1))
nimbra680ThermometerTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 7))
nimbra680Thermometer = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 1, 10, 7, 1))
netiGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 2))
netiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 3))
nimbravision = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 3, 1))
prodNimbra230 = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 3, 2))
netiCaps = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 4))
netiReqs = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 5))
netiExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6))
netiExperimentalReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 1))
netiExperimentalGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 2))
netiExperimentalProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 3))
netiExperimentalCaps = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 4))
netiExperimentalReqs = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 5))
mibBuilder.exportSymbols("NETI-COMMON-MIB", nimbravision=nimbravision, nimbra680ModuleTypesIf=nimbra680ModuleTypesIf, nimbraOneModuleTypesDtm150Right=nimbraOneModuleTypesDtm150Right, nimbra380=nimbra380, nimbra140=nimbra140, nimbra340ModuleTypesAux=nimbra340ModuleTypesAux, nimbraOneModuleTypesTrunk3xIP=nimbraOneModuleTypesTrunk3xIP, nimbra380ModuleTypesAccess=nimbra380ModuleTypesAccess, nimbra290PowerSupplyTypes=nimbra290PowerSupplyTypes, nimbra340ModuleTypesAccess4xOC3=nimbra340ModuleTypesAccess4xOC3, nimbraOneModuleTypesMgmtControlModule=nimbraOneModuleTypesMgmtControlModule, nimbraOneModuleTypesAccessE1=nimbraOneModuleTypesAccessE1, nimbra230=nimbra230, nimbra340ThermometerTypes=nimbra340ThermometerTypes, nimbraOneModuleTypes=nimbraOneModuleTypes, netiExperimentalCaps=netiExperimentalCaps, nimbra680ModuleTypesIfTrunk4xOC48=nimbra680ModuleTypesIfTrunk4xOC48, nimbra680ModuleTypesAccess8xHDSDI=nimbra680ModuleTypesAccess8xHDSDI, nimbra340ModuleTypesAccess=nimbra340ModuleTypesAccess, nimbra680ModuleTypesAccess8xGbE=nimbra680ModuleTypesAccess8xGbE, nimbra340ModuleTypesAccessSDI=nimbra340ModuleTypesAccessSDI, nimbraOneModuleTypesAccessVideo270Left=nimbraOneModuleTypesAccessVideo270Left, nimbra101=nimbra101, nimbra340Thermometer=nimbra340Thermometer, nimbraOneContainerTypes=nimbraOneContainerTypes, nimbra680ModuleTypesAccess8xJPEG2000=nimbra680ModuleTypesAccess8xJPEG2000, nimbra210=nimbra210, nimbra680PowerSupplyTypesPCU=nimbra680PowerSupplyTypesPCU, nimbraOneModuleTypesAccessE1Right=nimbraOneModuleTypesAccessE1Right, nimbra340ModuleTypesTrunk1Gbps=nimbra340ModuleTypesTrunk1Gbps, nimbraOneModuleTypesDtm850ShortHaulLeft=nimbraOneModuleTypesDtm850ShortHaulLeft, nimbraOneModuleTypesAccess8xAESEBU=nimbraOneModuleTypesAccess8xAESEBU, nimbraOneModuleTypesDtm1000ShortHaulLeft=nimbraOneModuleTypesDtm1000ShortHaulLeft, nimbraOneModuleTypesDtm=nimbraOneModuleTypesDtm, nimbraOneModuleTypesAux=nimbraOneModuleTypesAux, nimbra360ModuleTypesDtm=nimbra360ModuleTypesDtm, nimbraOneModuleTypesTrunkOC12=nimbraOneModuleTypesTrunkOC12, nimbraOneBackplaneTypes=nimbraOneBackplaneTypes, nimbra340ModuleTypesAccessHDSDI=nimbra340ModuleTypesAccessHDSDI, nimbraVA210DCV1=nimbraVA210DCV1, netiReg=netiReg, nimbra360=nimbra360, nimbra688=nimbra688, nimbra340ChassisTypes=nimbra340ChassisTypes, nimbra340=nimbra340, nimbraOneModuleTypesAccess8xEth=nimbraOneModuleTypesAccess8xEth, nimbraOneBaseUnit=nimbraOneBaseUnit, nimbraOneFan=nimbraOneFan, nimbra390=nimbra390, nimbra340ModuleTypesTrunkDS3=nimbra340ModuleTypesTrunkDS3, netiCaps=netiCaps, nimbra680ThermometerTypes=nimbra680ThermometerTypes, nimbra680ModuleTypesAuxGPIO=nimbra680ModuleTypesAuxGPIO, nimbra680ModuleTypesAccess8xASI=nimbra680ModuleTypesAccess8xASI, nimbra240=nimbra240, netiExperimentalReg=netiExperimentalReg, nimbraOneModuleTypesTrunk4xOC3=nimbraOneModuleTypesTrunk4xOC3, nimbra680PowerSupplyTypesPSU=nimbra680PowerSupplyTypesPSU, nimbraOneModuleTypesAccessEthernet8pLeft=nimbraOneModuleTypesAccessEthernet8pLeft, nimbraOneModuleTypesAccess8xASI=nimbraOneModuleTypesAccess8xASI, nimbra680ModuleTypesIfTrunk4xOC12=nimbra680ModuleTypesIfTrunk4xOC12, nimbra340ModuleTypesAccessASI=nimbra340ModuleTypesAccessASI, nimbraOnePowerSupply=nimbraOnePowerSupply, nimbraVA220=nimbraVA220, nimbra680ChassisTypes=nimbra680ChassisTypes, nimbra220=nimbra220, nimbraOneBackplane=nimbraOneBackplane, nimbraOneModuleTypesTrunk1Gbps=nimbraOneModuleTypesTrunk1Gbps, nimbra680ContainerTypes=nimbra680ContainerTypes, netiExperimental=netiExperimental, nimbra680ModuleTypesIfTrunk6xIP=nimbra680ModuleTypesIfTrunk6xIP, nimbraOnePowerSupplyTypes=nimbraOnePowerSupplyTypes, nimbraOneModuleTypesAccessT1Right=nimbraOneModuleTypesAccessT1Right, nimbra680ModuleTypesIfTrunk2xOC48=nimbra680ModuleTypesIfTrunk2xOC48, nimbra291=nimbra291, nimbraOneModuleTypesAccessE1Left=nimbraOneModuleTypesAccessE1Left, nimbraOneModuleTypesAccessGigabitEthernet=nimbraOneModuleTypesAccessGigabitEthernet, nimbra680ModuleTypesAccess2x10GbE=nimbra680ModuleTypesAccess2x10GbE, nimbraOneModuleTypesAccess4xOC3=nimbraOneModuleTypesAccess4xOC3, nimbra360Gold=nimbra360Gold, netinsight=netinsight, nimbraOneModuleTypesTrunkAccess=nimbraOneModuleTypesTrunkAccess, nimbraOneModuleTypesDtm1000LongHaulLeft=nimbraOneModuleTypesDtm1000LongHaulLeft, nimbra680Thermometer=nimbra680Thermometer, nimbra340ModuleTypesTrunkOC48=nimbra340ModuleTypesTrunkOC48, nimbra340ModuleTypesAccess8xASI=nimbra340ModuleTypesAccess8xASI, nimbraOneModuleTypesMgmt=nimbraOneModuleTypesMgmt, nimbraOneModuleTypesAccess=nimbraOneModuleTypesAccess, nimbra340ModuleTypesAuxGPIO=nimbra340ModuleTypesAuxGPIO, nimbraOneModuleTypesAccessGbE=nimbraOneModuleTypesAccessGbE, nimbraOneModuleTypesAccessEthernet8pRight=nimbraOneModuleTypesAccessEthernet8pRight, nimbraOneModuleTypesAccessASI=nimbraOneModuleTypesAccessASI, netiRegGeneric=netiRegGeneric, nimbra340HD=nimbra340HD, netiExperimentalGeneric=netiExperimentalGeneric, nimbra340ModuleTypesTrunkAccess4xDS3E3=nimbra340ModuleTypesTrunkAccess4xDS3E3, nimbraOneModuleTypesDtm1000ShortHaulRight=nimbraOneModuleTypesDtm1000ShortHaulRight, nimbra340ModuleTypesTrunk3xIP=nimbra340ModuleTypesTrunk3xIP, nimbra340ModuleTypesAccess8xEth=nimbra340ModuleTypesAccess8xEth, nimbra680ModuleTypesAccess8xASIAES=nimbra680ModuleTypesAccess8xASIAES, nimbra290PowerUnit=nimbra290PowerUnit, nimbraOneModuleTypesDtm850LongHaulRight=nimbraOneModuleTypesDtm850LongHaulRight, nimbra680ModuleTypesAccess8xVideo=nimbra680ModuleTypesAccess8xVideo, nimbra310=nimbra310, nimbra340ModuleTypesTrunkOC3=nimbra340ModuleTypesTrunkOC3, nimbraOneModuleTypesAccessT1Left=nimbraOneModuleTypesAccessT1Left, nimbra680ModuleTypesMgmt=nimbra680ModuleTypesMgmt, nimbraOneThermometer=nimbraOneThermometer, nimbra380ModuleTypesAccess8xGbE=nimbra380ModuleTypesAccess8xGbE, nimbraOneModuleTypesDtm150Left=nimbraOneModuleTypesDtm150Left, nimbraOneChassisTypes=nimbraOneChassisTypes, nimbra680ModuleTypesSwitch160Gbps=nimbra680ModuleTypesSwitch160Gbps, nimbraOneSlot=nimbraOneSlot, nimbraOneModuleTypesTrunkAccess4xDS3E3=nimbraOneModuleTypesTrunkAccess4xDS3E3, nimbra680ModuleTypesAccess8x3Gbps=nimbra680ModuleTypesAccess8x3Gbps, nimbraVA210FV=nimbraVA210FV, netiExperimentalProducts=netiExperimentalProducts, nimbraOneModuleTypesAccessVideo270Right=nimbraOneModuleTypesAccessVideo270Right, nimbra290BaseUnit=nimbra290BaseUnit, nimbraOneModuleTypesAuxGPIO=nimbraOneModuleTypesAuxGPIO, nimbra680PowerSupplyTypes=nimbra680PowerSupplyTypes, nimbra680FanTypesFan=nimbra680FanTypesFan, netiReqs=netiReqs, nimbra680ModuleTypesAccess=nimbra680ModuleTypesAccess, nimbra130=nimbra130, nimbra320=nimbra320, nimbraVA210=nimbraVA210, nimbra340PowerSupplyTypes=nimbra340PowerSupplyTypes, nimbra340ModuleTypesAccess8xAESEBU=nimbra340ModuleTypesAccess8xAESEBU, nimbra680ModuleTypesSwitch80Gbps=nimbra680ModuleTypesSwitch80Gbps, nimbra680ModuleTypesSwitch=nimbra680ModuleTypesSwitch, nimbra340FanTypes=nimbra340FanTypes, nimbra680ModuleTypesIfTrunkOC192=nimbra680ModuleTypesIfTrunkOC192, nimbraOneModuleTypesTrunkOC3=nimbraOneModuleTypesTrunkOC3, nimbraOneModuleTypesAccessASIRight=nimbraOneModuleTypesAccessASIRight, nimbraOneModuleTypesAccessSDI=nimbraOneModuleTypesAccessSDI, nimbraOneThermometerTypes=nimbraOneThermometerTypes, nimbra340ModuleTypesTrunk4xOC3=nimbra340ModuleTypesTrunk4xOC3, nimbra680FanTypes=nimbra680FanTypes, nimbra290FanTypes=nimbra290FanTypes, nimbraOneModuleTypesDtm850ShortHaulRight=nimbraOneModuleTypesDtm850ShortHaulRight, nimbra680ModuleTypesMgmtControlModule=nimbra680ModuleTypesMgmtControlModule, nimbraOneFanTypes=nimbraOneFanTypes, nimbraOneModuleTypesAccessASILeft=nimbraOneModuleTypesAccessASILeft, nimbra290ChassisTypes=nimbra290ChassisTypes, nimbraOneModuleTypesDtm622=nimbraOneModuleTypesDtm622, nimbraOneModuleTypesTrunkOC48=nimbraOneModuleTypesTrunkOC48, nimbra640=nimbra640, nimbra680=nimbra680, nimbra680ModuleTypesIfTrunk4xOC3=nimbra680ModuleTypesIfTrunk4xOC3, nimbraOneModuleTypesDtm1000LongHaulRight=nimbraOneModuleTypesDtm1000LongHaulRight, nimbra340ContainerTypes=nimbra340ContainerTypes, nimbra680ModuleTypesAux=nimbra680ModuleTypesAux, prodNimbra230=prodNimbra230, FaultStatus=FaultStatus, nimbra340ModuleTypes=nimbra340ModuleTypes, nimbra290Fan=nimbra290Fan, nimbra340ModuleTypesMgmtControlModule=nimbra340ModuleTypesMgmtControlModule, nimbra340ModuleTypesAccessE1=nimbra340ModuleTypesAccessE1, nimbraOne=nimbraOne, netiProducts=netiProducts, netiExperimentalReqs=netiExperimentalReqs, nimbraOneModuleTypesAccessT1=nimbraOneModuleTypesAccessT1, nimbra340ModuleTypesDtm=nimbra340ModuleTypesDtm, nimbra340ModuleTypesAccessGbE=nimbra340ModuleTypesAccessGbE, netiGeneric=netiGeneric, nimbraVA210DCV2=nimbraVA210DCV2, nimbra340ModuleTypesAccess8xSDI=nimbra340ModuleTypesAccess8xSDI, nimbra680ModuleTypes=nimbra680ModuleTypes, nimbra340ModuleTypesAccessT1=nimbra340ModuleTypesAccessT1, nimbraTwo=nimbraTwo, nimbra680ModuleTypesSwitch40Gbps=nimbra680ModuleTypesSwitch40Gbps, nimbra360ModuleTypesTrunkFunction=nimbra360ModuleTypesTrunkFunction, nimbra340ModuleTypesMgmt=nimbra340ModuleTypesMgmt, PYSNMP_MODULE_ID=netinsight, nimbraOneModuleTypesDtm850LongHaulLeft=nimbraOneModuleTypesDtm850LongHaulLeft, nimbra340ModuleTypesTrunkOC12=nimbra340ModuleTypesTrunkOC12, nimbra290=nimbra290, nimbraOneModuleTypesTrunkDS3=nimbraOneModuleTypesTrunkDS3, nimbra340ModuleTypesTrunkAccess=nimbra340ModuleTypesTrunkAccess)

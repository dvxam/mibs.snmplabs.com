#
# PySNMP MIB module LHX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LHX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
InetAddress, InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysContact, sysName, sysLocation = mibBuilder.importSymbols("SNMPv2-MIB", "sysContact", "sysName", "sysLocation")
enterprises, TimeTicks, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Counter32, Gauge32, Bits, iso, Integer32, Counter64, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "TimeTicks", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Counter32", "Gauge32", "Bits", "iso", "Integer32", "Counter64", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
raritan = ModuleIdentity((1, 3, 6, 1, 4, 1, 13742))
raritan.setRevisions(('2015-01-05 00:00', '2013-07-24 00:00', '2012-08-13 00:00', '2011-05-03 00:00',))
if mibBuilder.loadTexts: raritan.setLastUpdated('201501050000Z')
if mibBuilder.loadTexts: raritan.setOrganization('Raritan')
lhxgw = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 0))
configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 1))
measurements = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 2))
conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 3))
lhx = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3))
gwSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4))
trapInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0))
compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 3, 1))
groups = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 3, 2))
class OperationalStateEnumeration(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disconnected", 0), ("offline", 1), ("online", 2))

class GwSensorTypeEnumeration(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("airTemperature", 0), ("waterTemperature", 1), ("fanSpeed", 2), ("doorContact", 3), ("valvePosition", 4))

class SensorUnitsEnumeration(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("none", -1), ("other", 0), ("volt", 1), ("amp", 2), ("watt", 3), ("voltamp", 4), ("wattHour", 5), ("voltampHour", 6), ("degreeC", 7), ("hertz", 8), ("percent", 9), ("meterpersec", 10), ("pascal", 11), ("psi", 12), ("g", 13), ("degreeF", 14), ("feet", 15), ("inches", 16), ("cm", 17), ("meters", 18), ("rpm", 19))

class SensorStateEnumeration(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unavailable", -1), ("open", 0), ("closed", 1), ("belowLowerCritical", 2), ("belowLowerWarning", 3), ("normal", 4), ("aboveUpperWarning", 5), ("aboveUpperCritical", 6), ("on", 7), ("off", 8), ("detected", 9), ("notDetected", 10), ("alarmed", 11))

lhxSensorFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 1)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"), ("LHX-MIB", "probeId"))
if mibBuilder.loadTexts: lhxSensorFailure.setStatus('current')
lhxFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 2)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"), ("LHX-MIB", "fanId"))
if mibBuilder.loadTexts: lhxFanFailure.setStatus('current')
lhxPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 3)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"), ("LHX-MIB", "powerSupplyId"))
if mibBuilder.loadTexts: lhxPowerSupplyFailure.setStatus('current')
lhxThresholdAirOutlet = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 4)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxThresholdAirOutlet.setStatus('current')
lhxThresholdAirInlet = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 5)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxThresholdAirInlet.setStatus('current')
lhxThresholdWaterInlet = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 6)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxThresholdWaterInlet.setStatus('current')
lhxDoorOpened = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 7)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxDoorOpened.setStatus('current')
lhxMaximumCoolingRequest = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 8)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxMaximumCoolingRequest.setStatus('current')
lhxEmergencyCooling = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 9)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxEmergencyCooling.setStatus('current')
lhxWaterLeak = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 10)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxWaterLeak.setStatus('current')
lhxThresholdHumidity = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 11)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxThresholdHumidity.setStatus('current')
lhxExternalWaterCoolingFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 12)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxExternalWaterCoolingFailure.setStatus('current')
lhxThresholdWaterOutlet = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 13)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxThresholdWaterOutlet.setStatus('current')
lhxParameterDataLoss = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 14)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxParameterDataLoss.setStatus('current')
lhxStBusError = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 15)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxStBusError.setStatus('current')
lhxCollectiveFault = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 16)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxCollectiveFault.setStatus('current')
gwSensorStateChange = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 17)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "portId"), ("LHX-MIB", "sensorTypeId"), ("LHX-MIB", "sensorId"), ("LHX-MIB", "probeId"), ("LHX-MIB", "measurementsSensorTimeStamp"), ("LHX-MIB", "measurementsSensorValue"), ("LHX-MIB", "measurementsSensorState"), ("LHX-MIB", "oldSensorState"))
if mibBuilder.loadTexts: gwSensorStateChange.setStatus('current')
gwLhxOperationalStateChange = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 18)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "portId"), ("LHX-MIB", "operationalState"), ("LHX-MIB", "oldOperationalState"))
if mibBuilder.loadTexts: gwLhxOperationalStateChange.setStatus('current')
lhxVoltageLow = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 19)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxVoltageLow.setStatus('current')
lhxBaseElectronicsFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 20)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxBaseElectronicsFailure.setStatus('current')
lhxCondenserPumpFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 9, 0, 21)).setObjects(("LHX-MIB", "deviceName"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "agentInetPortNumber"), ("LHX-MIB", "portId"))
if mibBuilder.loadTexts: lhxCondenserPumpFailure.setStatus('current')
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: deviceName.setStatus('current')
deviceInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: deviceInetAddressType.setStatus('current')
deviceInetIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: deviceInetIPAddress.setStatus('current')
lhxErrorCode = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: lhxErrorCode.setStatus('current')
portId = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: portId.setStatus('current')
probeId = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: probeId.setStatus('current')
fanId = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fanId.setStatus('current')
powerSupplyId = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 8), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: powerSupplyId.setStatus('current')
oldSensorState = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 9), SensorStateEnumeration()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: oldSensorState.setStatus('current')
sensorTypeId = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 10), GwSensorTypeEnumeration()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sensorTypeId.setStatus('current')
sensorId = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sensorId.setStatus('current')
oldOperationalState = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 12), OperationalStateEnumeration()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oldOperationalState.setStatus('current')
agentInetPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 13), InetPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: agentInetPortNumber.setStatus('current')
portCount = MibScalar((1, 3, 6, 1, 4, 1, 13742, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portCount.setStatus('current')
sensorCountTable = MibTable((1, 3, 6, 1, 4, 1, 13742, 9, 1, 2), )
if mibBuilder.loadTexts: sensorCountTable.setStatus('current')
sensorCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13742, 9, 1, 2, 1), ).setIndexNames((0, "LHX-MIB", "portIdx"), (0, "LHX-MIB", "sensorTypeIdx"))
if mibBuilder.loadTexts: sensorCountEntry.setStatus('current')
sensorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorCount.setStatus('current')
lhxConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1), )
if mibBuilder.loadTexts: lhxConfigurationTable.setStatus('current')
lhxConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1), ).setIndexNames((0, "LHX-MIB", "portIdx"))
if mibBuilder.loadTexts: lhxConfigurationEntry.setStatus('current')
operationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 1), OperationalStateEnumeration()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: operationalState.setStatus('current')
setpointVentilators = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setpointVentilators.setStatus('current')
setpointWaterValve = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setpointWaterValve.setStatus('current')
defaultFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: defaultFanSpeed.setStatus('current')
maximumCoolingState = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 5), TruthValue().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maximumCoolingState.setStatus('current')
alertState = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 6), TruthValue().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alertState.setStatus('current')
model = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: model.setStatus('current')
fwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwVersion.setStatus('current')
sensorConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1), )
if mibBuilder.loadTexts: sensorConfigurationTable.setStatus('current')
sensorConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1), ).setIndexNames((0, "LHX-MIB", "portIdx"), (0, "LHX-MIB", "sensorTypeIdx"), (0, "LHX-MIB", "sensorIdx"))
if mibBuilder.loadTexts: sensorConfigurationEntry.setStatus('current')
portIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: portIdx.setStatus('current')
sensorTypeIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: sensorTypeIdx.setStatus('current')
sensorIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: sensorIdx.setStatus('current')
sensorLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorLabel.setStatus('current')
sensorUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 5), SensorUnitsEnumeration()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorUnit.setStatus('current')
sensorDecimalDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorDecimalDigits.setStatus('current')
sensorMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorMaximum.setStatus('current')
sensorMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorMinimum.setStatus('current')
sensorHysteresis = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorHysteresis.setStatus('current')
sensorLowerCriticalThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorLowerCriticalThreshold.setStatus('current')
sensorLowerWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorLowerWarningThreshold.setStatus('current')
sensorUpperCriticalThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorUpperCriticalThreshold.setStatus('current')
sensorUpperWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorUpperWarningThreshold.setStatus('current')
sensorEnabledThresholds = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 14), Bits().clone(namedValues=NamedValues(("lowerCritical", 0), ("lowerWarning", 1), ("upperWarning", 2), ("upperCritical", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorEnabledThresholds.setStatus('current')
sensorThresholdMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorThresholdMaximum.setStatus('current')
sensorThresholdMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorThresholdMinimum.setStatus('current')
sensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorName.setStatus('current')
sensorMeasurementsTable = MibTable((1, 3, 6, 1, 4, 1, 13742, 9, 2, 1), )
if mibBuilder.loadTexts: sensorMeasurementsTable.setStatus('current')
sensorMeasurementsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1), ).setIndexNames((0, "LHX-MIB", "portIdx"), (0, "LHX-MIB", "sensorTypeIdx"), (0, "LHX-MIB", "sensorIdx"))
if mibBuilder.loadTexts: sensorMeasurementsEntry.setStatus('current')
measurementsSensorIsAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: measurementsSensorIsAvailable.setStatus('current')
measurementsSensorState = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1, 2), SensorStateEnumeration()).setMaxAccess("readonly")
if mibBuilder.loadTexts: measurementsSensorState.setStatus('current')
measurementsSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: measurementsSensorValue.setStatus('current')
measurementsSensorTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: measurementsSensorTimeStamp.setStatus('current')
complianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 13742, 9, 3, 1, 1)).setObjects(("LHX-MIB", "configurationGroup"), ("LHX-MIB", "measurementsGroup"), ("LHX-MIB", "trapInformationGroup"), ("LHX-MIB", "trapsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    complianceRev1 = complianceRev1.setStatus('current')
configurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13742, 9, 3, 2, 1)).setObjects(("LHX-MIB", "portCount"), ("LHX-MIB", "portId"), ("LHX-MIB", "operationalState"), ("LHX-MIB", "sensorCount"), ("LHX-MIB", "sensorLabel"), ("LHX-MIB", "sensorUnit"), ("LHX-MIB", "sensorDecimalDigits"), ("LHX-MIB", "sensorMaximum"), ("LHX-MIB", "sensorMinimum"), ("LHX-MIB", "sensorHysteresis"), ("LHX-MIB", "sensorLowerCriticalThreshold"), ("LHX-MIB", "sensorLowerWarningThreshold"), ("LHX-MIB", "sensorUpperCriticalThreshold"), ("LHX-MIB", "sensorUpperWarningThreshold"), ("LHX-MIB", "sensorEnabledThresholds"), ("LHX-MIB", "setpointVentilators"), ("LHX-MIB", "setpointWaterValve"), ("LHX-MIB", "defaultFanSpeed"), ("LHX-MIB", "maximumCoolingState"), ("LHX-MIB", "alertState"), ("LHX-MIB", "sensorThresholdMaximum"), ("LHX-MIB", "sensorThresholdMinimum"), ("LHX-MIB", "model"), ("LHX-MIB", "fwVersion"), ("LHX-MIB", "sensorName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configurationGroup = configurationGroup.setStatus('current')
measurementsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13742, 9, 3, 2, 2)).setObjects(("LHX-MIB", "measurementsSensorIsAvailable"), ("LHX-MIB", "measurementsSensorState"), ("LHX-MIB", "measurementsSensorValue"), ("LHX-MIB", "measurementsSensorTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    measurementsGroup = measurementsGroup.setStatus('current')
trapInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13742, 9, 3, 2, 3)).setObjects(("LHX-MIB", "deviceName"), ("LHX-MIB", "deviceInetAddressType"), ("LHX-MIB", "deviceInetIPAddress"), ("LHX-MIB", "lhxErrorCode"), ("LHX-MIB", "portId"), ("LHX-MIB", "probeId"), ("LHX-MIB", "fanId"), ("LHX-MIB", "powerSupplyId"), ("LHX-MIB", "oldSensorState"), ("LHX-MIB", "sensorTypeId"), ("LHX-MIB", "sensorId"), ("LHX-MIB", "oldOperationalState"), ("LHX-MIB", "agentInetPortNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapInformationGroup = trapInformationGroup.setStatus('current')
trapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13742, 9, 3, 2, 4)).setObjects(("LHX-MIB", "lhxSensorFailure"), ("LHX-MIB", "lhxFanFailure"), ("LHX-MIB", "lhxPowerSupplyFailure"), ("LHX-MIB", "lhxThresholdAirOutlet"), ("LHX-MIB", "lhxThresholdAirInlet"), ("LHX-MIB", "lhxThresholdWaterInlet"), ("LHX-MIB", "lhxDoorOpened"), ("LHX-MIB", "lhxMaximumCoolingRequest"), ("LHX-MIB", "lhxEmergencyCooling"), ("LHX-MIB", "lhxWaterLeak"), ("LHX-MIB", "lhxThresholdHumidity"), ("LHX-MIB", "lhxExternalWaterCoolingFailure"), ("LHX-MIB", "lhxThresholdWaterOutlet"), ("LHX-MIB", "lhxParameterDataLoss"), ("LHX-MIB", "lhxStBusError"), ("LHX-MIB", "lhxCondenserPumpFailure"), ("LHX-MIB", "gwSensorStateChange"), ("LHX-MIB", "gwLhxOperationalStateChange"), ("LHX-MIB", "lhxCollectiveFault"), ("LHX-MIB", "lhxVoltageLow"), ("LHX-MIB", "lhxBaseElectronicsFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapsGroup = trapsGroup.setStatus('current')
mibBuilder.exportSymbols("LHX-MIB", sensorHysteresis=sensorHysteresis, PYSNMP_MODULE_ID=raritan, sensorTypeIdx=sensorTypeIdx, portId=portId, configurationGroup=configurationGroup, setpointVentilators=setpointVentilators, sensorThresholdMaximum=sensorThresholdMaximum, lhxWaterLeak=lhxWaterLeak, portIdx=portIdx, configuration=configuration, lhxConfigurationEntry=lhxConfigurationEntry, agentInetPortNumber=agentInetPortNumber, lhxPowerSupplyFailure=lhxPowerSupplyFailure, lhxFanFailure=lhxFanFailure, sensorTypeId=sensorTypeId, measurementsSensorState=measurementsSensorState, lhxThresholdAirOutlet=lhxThresholdAirOutlet, trapsGroup=trapsGroup, measurementsSensorTimeStamp=measurementsSensorTimeStamp, sensorConfigurationTable=sensorConfigurationTable, sensorMeasurementsTable=sensorMeasurementsTable, deviceInetIPAddress=deviceInetIPAddress, fanId=fanId, lhxSensorFailure=lhxSensorFailure, lhxCollectiveFault=lhxCollectiveFault, measurements=measurements, sensorConfigurationEntry=sensorConfigurationEntry, lhxParameterDataLoss=lhxParameterDataLoss, gwLhxOperationalStateChange=gwLhxOperationalStateChange, oldSensorState=oldSensorState, lhxConfigurationTable=lhxConfigurationTable, sensorCountEntry=sensorCountEntry, lhxVoltageLow=lhxVoltageLow, sensorLowerCriticalThreshold=sensorLowerCriticalThreshold, gwSensors=gwSensors, lhxThresholdWaterInlet=lhxThresholdWaterInlet, trapInformation=trapInformation, lhxThresholdHumidity=lhxThresholdHumidity, traps=traps, lhxThresholdWaterOutlet=lhxThresholdWaterOutlet, gwSensorStateChange=gwSensorStateChange, deviceName=deviceName, lhxgw=lhxgw, complianceRev1=complianceRev1, sensorThresholdMinimum=sensorThresholdMinimum, sensorLabel=sensorLabel, sensorName=sensorName, lhx=lhx, lhxMaximumCoolingRequest=lhxMaximumCoolingRequest, lhxErrorCode=lhxErrorCode, sensorId=sensorId, probeId=probeId, powerSupplyId=powerSupplyId, compliances=compliances, measurementsSensorIsAvailable=measurementsSensorIsAvailable, lhxEmergencyCooling=lhxEmergencyCooling, sensorCount=sensorCount, conformance=conformance, deviceInetAddressType=deviceInetAddressType, maximumCoolingState=maximumCoolingState, SensorUnitsEnumeration=SensorUnitsEnumeration, sensorEnabledThresholds=sensorEnabledThresholds, measurementsGroup=measurementsGroup, lhxThresholdAirInlet=lhxThresholdAirInlet, lhxDoorOpened=lhxDoorOpened, portCount=portCount, sensorUpperWarningThreshold=sensorUpperWarningThreshold, lhxStBusError=lhxStBusError, sensorCountTable=sensorCountTable, raritan=raritan, GwSensorTypeEnumeration=GwSensorTypeEnumeration, model=model, alertState=alertState, fwVersion=fwVersion, oldOperationalState=oldOperationalState, operationalState=operationalState, measurementsSensorValue=measurementsSensorValue, SensorStateEnumeration=SensorStateEnumeration, lhxCondenserPumpFailure=lhxCondenserPumpFailure, setpointWaterValve=setpointWaterValve, sensorUnit=sensorUnit, lhxExternalWaterCoolingFailure=lhxExternalWaterCoolingFailure, groups=groups, lhxBaseElectronicsFailure=lhxBaseElectronicsFailure, sensorIdx=sensorIdx, sensorMinimum=sensorMinimum, sensorLowerWarningThreshold=sensorLowerWarningThreshold, trapInformationGroup=trapInformationGroup, sensorUpperCriticalThreshold=sensorUpperCriticalThreshold, sensorMeasurementsEntry=sensorMeasurementsEntry, defaultFanSpeed=defaultFanSpeed, sensorMaximum=sensorMaximum, sensorDecimalDigits=sensorDecimalDigits, OperationalStateEnumeration=OperationalStateEnumeration)

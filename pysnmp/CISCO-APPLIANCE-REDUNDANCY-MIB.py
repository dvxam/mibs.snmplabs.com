#
# PySNMP MIB module CISCO-APPLIANCE-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-APPLIANCE-REDUNDANCY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, IpAddress, ObjectIdentity, TimeTicks, ModuleIdentity, Gauge32, MibIdentifier, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Gauge32", "MibIdentifier", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Bits", "Unsigned32")
TextualConvention, TimeInterval, TruthValue, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeInterval", "TruthValue", "DisplayString", "DateAndTime")
ciscoApplianceRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 458))
if mibBuilder.loadTexts: ciscoApplianceRedundancyMIB.setLastUpdated('200412230000Z')
if mibBuilder.loadTexts: ciscoApplianceRedundancyMIB.setOrganization('Cisco Systems, Inc.')
ciscoApplRedundancyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 458, 1))
carConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1))
carSwitchOverObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2))
class CarRedundancyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("notConfigured", 1), ("starting", 2), ("active", 3), ("preStandby", 4), ("standby", 5), ("activeLostStandby", 6), ("activeLostNetwork", 7), ("standbyLostNetwork", 8))

class CarSwitchOverReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("lossConnWithActive", 1), ("forcedSwitchOver", 2), ("unknown", 3))

carRedundancySyncInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 1), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carRedundancySyncInterval.setStatus('current')
carRedundancyCheckInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 2), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carRedundancyCheckInterval.setStatus('current')
carRedundancyState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 3), CarRedundancyState().clone('notConfigured')).setMaxAccess("readonly")
if mibBuilder.loadTexts: carRedundancyState.setStatus('current')
carNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: carNotificationEnabled.setStatus('current')
carHAAddressTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5), )
if mibBuilder.loadTexts: carHAAddressTable.setStatus('current')
carHAAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-APPLIANCE-REDUNDANCY-MIB", "carHAAddrTableIndex"))
if mibBuilder.loadTexts: carHAAddressEntry.setStatus('current')
carHAAddrTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: carHAAddrTableIndex.setStatus('current')
carVirtualAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carVirtualAddressType.setStatus('current')
carVirtualAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carVirtualAddress.setStatus('current')
carMyAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carMyAddressType.setStatus('current')
carMyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carMyAddress.setStatus('current')
carPeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carPeerAddressType.setStatus('current')
carPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carPeerAddress.setStatus('current')
carLastSwitchOverReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 1), CarSwitchOverReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carLastSwitchOverReason.setStatus('current')
carLastSwitchOverTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carLastSwitchOverTime.setStatus('current')
carTotalSwitchOvers = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carTotalSwitchOvers.setStatus('current')
carMaxSwitchOverHistoryRecords = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024)).clone(20)).setMaxAccess("readonly")
if mibBuilder.loadTexts: carMaxSwitchOverHistoryRecords.setStatus('current')
carSwitchOverHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5), )
if mibBuilder.loadTexts: carSwitchOverHistoryTable.setStatus('current')
carSwitchOverHistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1), ).setIndexNames((0, "CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistTableIndex"))
if mibBuilder.loadTexts: carSwitchOverHistEntry.setStatus('current')
carSWHistTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: carSWHistTableIndex.setStatus('current')
carSWHistActiveNodeAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carSWHistActiveNodeAddressType.setStatus('current')
carSWHistActiveNodeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carSWHistActiveNodeAddress.setStatus('current')
carSWHistStandbyNodeAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carSWHistStandbyNodeAddressType.setStatus('current')
carSWHistStandbyNodeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carSWHistStandbyNodeAddress.setStatus('current')
carSWHistEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carSWHistEventTime.setStatus('current')
carSWHistEventReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 7), CarSwitchOverReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carSWHistEventReason.setStatus('current')
carHAMIBNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 458, 2))
carHAMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 458, 2, 0))
carSwitchOverNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 458, 2, 0, 1)).setObjects(("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistEventTime"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistEventReason"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistActiveNodeAddressType"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistActiveNodeAddress"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistStandbyNodeAddressType"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistStandbyNodeAddress"))
if mibBuilder.loadTexts: carSwitchOverNotification.setStatus('current')
ciscoHAMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 458, 3))
ciscoHAMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 1))
ciscoHAMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 2))
ciscoHAMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 1, 1)).setObjects(("CISCO-APPLIANCE-REDUNDANCY-MIB", "ciscoHAConfigDataGroup"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "ciscoHASwitchOverDataGroup"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "ciscoHAExceptionNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHAMIBCompliance = ciscoHAMIBCompliance.setStatus('current')
ciscoHAConfigDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 2, 1)).setObjects(("CISCO-APPLIANCE-REDUNDANCY-MIB", "carVirtualAddressType"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carVirtualAddress"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carMyAddressType"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carMyAddress"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carPeerAddressType"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carPeerAddress"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carRedundancySyncInterval"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carRedundancyCheckInterval"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carRedundancyState"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHAConfigDataGroup = ciscoHAConfigDataGroup.setStatus('current')
ciscoHASwitchOverDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 2, 2)).setObjects(("CISCO-APPLIANCE-REDUNDANCY-MIB", "carLastSwitchOverReason"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carLastSwitchOverTime"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carTotalSwitchOvers"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carMaxSwitchOverHistoryRecords"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistActiveNodeAddressType"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistActiveNodeAddress"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistStandbyNodeAddressType"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistStandbyNodeAddress"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistEventTime"), ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistEventReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHASwitchOverDataGroup = ciscoHASwitchOverDataGroup.setStatus('current')
ciscoHAExceptionNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 2, 3)).setObjects(("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSwitchOverNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHAExceptionNotifGroup = ciscoHAExceptionNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-APPLIANCE-REDUNDANCY-MIB", carSwitchOverNotification=carSwitchOverNotification, carVirtualAddressType=carVirtualAddressType, ciscoHAMIBCompliance=ciscoHAMIBCompliance, carHAMIBNotifPrefix=carHAMIBNotifPrefix, ciscoHAConfigDataGroup=ciscoHAConfigDataGroup, carConfigObjects=carConfigObjects, carHAAddressEntry=carHAAddressEntry, carRedundancySyncInterval=carRedundancySyncInterval, carSwitchOverHistEntry=carSwitchOverHistEntry, PYSNMP_MODULE_ID=ciscoApplianceRedundancyMIB, ciscoApplRedundancyMIBObjects=ciscoApplRedundancyMIBObjects, carSwitchOverHistoryTable=carSwitchOverHistoryTable, carNotificationEnabled=carNotificationEnabled, carMaxSwitchOverHistoryRecords=carMaxSwitchOverHistoryRecords, carSwitchOverObjects=carSwitchOverObjects, ciscoHASwitchOverDataGroup=ciscoHASwitchOverDataGroup, carSWHistEventReason=carSWHistEventReason, carVirtualAddress=carVirtualAddress, carHAAddrTableIndex=carHAAddrTableIndex, carPeerAddressType=carPeerAddressType, carRedundancyState=carRedundancyState, ciscoApplianceRedundancyMIB=ciscoApplianceRedundancyMIB, carTotalSwitchOvers=carTotalSwitchOvers, ciscoHAMIBCompliances=ciscoHAMIBCompliances, carHAMIBNotifications=carHAMIBNotifications, carSWHistActiveNodeAddressType=carSWHistActiveNodeAddressType, carSWHistTableIndex=carSWHistTableIndex, carSWHistEventTime=carSWHistEventTime, carLastSwitchOverTime=carLastSwitchOverTime, carSWHistStandbyNodeAddressType=carSWHistStandbyNodeAddressType, carSWHistStandbyNodeAddress=carSWHistStandbyNodeAddress, carMyAddressType=carMyAddressType, ciscoHAMIBGroups=ciscoHAMIBGroups, carMyAddress=carMyAddress, carRedundancyCheckInterval=carRedundancyCheckInterval, carLastSwitchOverReason=carLastSwitchOverReason, carPeerAddress=carPeerAddress, CarSwitchOverReason=CarSwitchOverReason, carHAAddressTable=carHAAddressTable, ciscoHAExceptionNotifGroup=ciscoHAExceptionNotifGroup, carSWHistActiveNodeAddress=carSWHistActiveNodeAddress, ciscoHAMIBConformance=ciscoHAMIBConformance, CarRedundancyState=CarRedundancyState)

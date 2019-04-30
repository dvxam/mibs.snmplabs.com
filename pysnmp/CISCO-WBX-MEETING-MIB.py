#
# PySNMP MIB module CISCO-WBX-MEETING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WBX-MEETING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, NotificationType, IpAddress, Integer32, Counter32, Gauge32, MibIdentifier, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "IpAddress", "Integer32", "Counter32", "Gauge32", "MibIdentifier", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "iso", "ObjectIdentity")
AutonomousType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "DisplayString")
ciscoWebExMeetingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 809))
ciscoWebExMeetingMIB.setRevisions(('2013-05-29 00:00',))
if mibBuilder.loadTexts: ciscoWebExMeetingMIB.setLastUpdated('201305290000Z')
if mibBuilder.loadTexts: ciscoWebExMeetingMIB.setOrganization('Cisco Systems Inc.')
ciscoWebExMeetingMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 809, 0))
ciscoWebExMeetingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 809, 1))
ciscoWebExMeetingMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 809, 2))
class CiscoWebExCommSysResource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("cpu", 0), ("memory", 1), ("swap", 2), ("fileDescriptor", 3), ("disk", 4))

class CiscoWebExCommSysResMonitoringStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("closed", 0), ("open", 1))

ciscoWebExCommInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 1))
ciscoWebExCommSystemResource = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2))
cwCommSystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommSystemVersion.setStatus('current')
cwCommSystemObjectID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 1, 2), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommSystemObjectID.setStatus('current')
cwCommCPUUsageObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1))
if mibBuilder.loadTexts: cwCommCPUUsageObject.setStatus('current')
cwCommCPUTotalUsage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUTotalUsage.setStatus('current')
cwCommCPUUsageWindow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setUnits('Minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwCommCPUUsageWindow.setStatus('current')
cwCommCPUTotalNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUTotalNumber.setStatus('current')
cwCommCPUUsageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4), )
if mibBuilder.loadTexts: cwCommCPUUsageTable.setStatus('current')
cwCommCPUUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1), ).setIndexNames((0, "CISCO-WBX-MEETING-MIB", "cwCommCPUIndex"))
if mibBuilder.loadTexts: cwCommCPUUsageEntry.setStatus('current')
cwCommCPUIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: cwCommCPUIndex.setStatus('current')
cwCommCPUName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUName.setStatus('current')
cwCommCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsage.setStatus('current')
cwCommCPUUsageUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsageUser.setStatus('current')
cwCommCPUUsageNice = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsageNice.setStatus('current')
cwCommCPUUsageSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsageSystem.setStatus('current')
cwCommCPUUsageIdle = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsageIdle.setStatus('current')
cwCommCPUUsageIOWait = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsageIOWait.setStatus('current')
cwCommCPUUsageIRQ = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsageIRQ.setStatus('current')
cwCommCPUUsageSoftIRQ = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsageSoftIRQ.setStatus('current')
cwCommCPUUsageSteal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsageSteal.setStatus('current')
cwCommCPUUsageCapacitySubTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUUsageCapacitySubTotal.setStatus('current')
cwCommCPUMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 5), CiscoWebExCommSysResMonitoringStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUMonitoringStatus.setStatus('current')
cwCommCPUCapacityTotal = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommCPUCapacityTotal.setStatus('current')
cwCommMEMUsageObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 2))
if mibBuilder.loadTexts: cwCommMEMUsageObject.setStatus('current')
cwCommMEMUsage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 2, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommMEMUsage.setStatus('current')
cwCommMEMMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 2, 2), CiscoWebExCommSysResMonitoringStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommMEMMonitoringStatus.setStatus('current')
cwCommMEMTotal = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 2, 3), Gauge32()).setUnits('MBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommMEMTotal.setStatus('current')
cwCommMEMSwapUsageObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 3))
if mibBuilder.loadTexts: cwCommMEMSwapUsageObject.setStatus('current')
cwCommMEMSwapUsage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 3, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommMEMSwapUsage.setStatus('current')
cwCommMEMSwapMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 3, 2), CiscoWebExCommSysResMonitoringStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommMEMSwapMonitoringStatus.setStatus('current')
cwCommSysResourceNotificationObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4))
if mibBuilder.loadTexts: cwCommSysResourceNotificationObject.setStatus('current')
cwCommNotificationHostAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cwCommNotificationHostAddressType.setStatus('current')
cwCommNotificationHostAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cwCommNotificationHostAddress.setStatus('current')
cwCommNotificationResName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 3), CiscoWebExCommSysResource()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cwCommNotificationResName.setStatus('current')
cwCommNotificationResValue = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cwCommNotificationResValue.setStatus('current')
cwCommNotificationSeqNum = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 5), Counter32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cwCommNotificationSeqNum.setStatus('current')
cwCommDiskUsageObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5))
if mibBuilder.loadTexts: cwCommDiskUsageObject.setStatus('current')
cwCommDiskUsageCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommDiskUsageCount.setStatus('current')
cwCommDiskUsageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2), )
if mibBuilder.loadTexts: cwCommDiskUsageTable.setStatus('current')
cwCommDiskUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1), ).setIndexNames((0, "CISCO-WBX-MEETING-MIB", "cwCommDiskUsageIndex"))
if mibBuilder.loadTexts: cwCommDiskUsageEntry.setStatus('current')
cwCommDiskUsageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: cwCommDiskUsageIndex.setStatus('current')
cwCommDiskPartitionName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommDiskPartitionName.setStatus('current')
cwCommDiskUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommDiskUsage.setStatus('current')
cwCommDiskTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommDiskTotal.setStatus('current')
cwCommDiskMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 3), CiscoWebExCommSysResMonitoringStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwCommDiskMonitoringStatus.setStatus('current')
cwCommSystemResourceUsageNormalEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 809, 0, 1)).setObjects(("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddressType"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddress"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResName"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResValue"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationSeqNum"))
if mibBuilder.loadTexts: cwCommSystemResourceUsageNormalEvent.setStatus('current')
cwCommSystemResourceUsageMinorEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 809, 0, 2)).setObjects(("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddressType"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddress"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResName"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResValue"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationSeqNum"))
if mibBuilder.loadTexts: cwCommSystemResourceUsageMinorEvent.setStatus('current')
cwCommSystemResourceUsageMajorEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 809, 0, 3)).setObjects(("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddressType"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddress"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResName"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResValue"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationSeqNum"))
if mibBuilder.loadTexts: cwCommSystemResourceUsageMajorEvent.setStatus('current')
cwCommMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 1))
cwCommMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 1, 1)).setObjects(("CISCO-WBX-MEETING-MIB", "ciscoWebExCommInfoGroup"), ("CISCO-WBX-MEETING-MIB", "ciscoWebExCommSystemResourceGroup"), ("CISCO-WBX-MEETING-MIB", "ciscoWebExMeetingMIBNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwCommMIBCompliance = cwCommMIBCompliance.setStatus('current')
cwCommMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 2))
ciscoWebExCommInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 2, 1)).setObjects(("CISCO-WBX-MEETING-MIB", "cwCommSystemVersion"), ("CISCO-WBX-MEETING-MIB", "cwCommSystemObjectID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWebExCommInfoGroup = ciscoWebExCommInfoGroup.setStatus('current')
ciscoWebExCommSystemResourceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 2, 2)).setObjects(("CISCO-WBX-MEETING-MIB", "cwCommCPUTotalUsage"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageWindow"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUTotalNumber"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUName"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsage"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUMonitoringStatus"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageUser"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageNice"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageSystem"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageIdle"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageIOWait"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageIRQ"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageSoftIRQ"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageSteal"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageCapacitySubTotal"), ("CISCO-WBX-MEETING-MIB", "cwCommCPUCapacityTotal"), ("CISCO-WBX-MEETING-MIB", "cwCommMEMUsage"), ("CISCO-WBX-MEETING-MIB", "cwCommMEMMonitoringStatus"), ("CISCO-WBX-MEETING-MIB", "cwCommMEMSwapUsage"), ("CISCO-WBX-MEETING-MIB", "cwCommMEMSwapMonitoringStatus"), ("CISCO-WBX-MEETING-MIB", "cwCommMEMTotal"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddressType"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddress"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResName"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResValue"), ("CISCO-WBX-MEETING-MIB", "cwCommNotificationSeqNum"), ("CISCO-WBX-MEETING-MIB", "cwCommDiskUsageCount"), ("CISCO-WBX-MEETING-MIB", "cwCommDiskPartitionName"), ("CISCO-WBX-MEETING-MIB", "cwCommDiskUsage"), ("CISCO-WBX-MEETING-MIB", "cwCommDiskTotal"), ("CISCO-WBX-MEETING-MIB", "cwCommDiskMonitoringStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWebExCommSystemResourceGroup = ciscoWebExCommSystemResourceGroup.setStatus('current')
ciscoWebExMeetingMIBNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 2, 3)).setObjects(("CISCO-WBX-MEETING-MIB", "cwCommSystemResourceUsageNormalEvent"), ("CISCO-WBX-MEETING-MIB", "cwCommSystemResourceUsageMinorEvent"), ("CISCO-WBX-MEETING-MIB", "cwCommSystemResourceUsageMajorEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWebExMeetingMIBNotifsGroup = ciscoWebExMeetingMIBNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WBX-MEETING-MIB", CiscoWebExCommSysResource=CiscoWebExCommSysResource, cwCommMEMUsage=cwCommMEMUsage, ciscoWebExCommInfo=ciscoWebExCommInfo, cwCommCPUUsageIRQ=cwCommCPUUsageIRQ, cwCommCPUUsageCapacitySubTotal=cwCommCPUUsageCapacitySubTotal, cwCommNotificationHostAddressType=cwCommNotificationHostAddressType, CiscoWebExCommSysResMonitoringStatus=CiscoWebExCommSysResMonitoringStatus, cwCommSystemResourceUsageNormalEvent=cwCommSystemResourceUsageNormalEvent, cwCommCPUUsageNice=cwCommCPUUsageNice, ciscoWebExMeetingMIBNotifs=ciscoWebExMeetingMIBNotifs, cwCommNotificationResValue=cwCommNotificationResValue, cwCommCPUUsageUser=cwCommCPUUsageUser, cwCommSystemVersion=cwCommSystemVersion, cwCommDiskPartitionName=cwCommDiskPartitionName, cwCommMEMMonitoringStatus=cwCommMEMMonitoringStatus, cwCommCPUUsageIdle=cwCommCPUUsageIdle, cwCommMIBCompliances=cwCommMIBCompliances, cwCommDiskUsageCount=cwCommDiskUsageCount, cwCommCPUCapacityTotal=cwCommCPUCapacityTotal, cwCommMIBGroups=cwCommMIBGroups, cwCommMEMTotal=cwCommMEMTotal, cwCommMEMSwapUsage=cwCommMEMSwapUsage, cwCommSystemResourceUsageMinorEvent=cwCommSystemResourceUsageMinorEvent, cwCommDiskMonitoringStatus=cwCommDiskMonitoringStatus, cwCommMEMSwapUsageObject=cwCommMEMSwapUsageObject, cwCommSystemObjectID=cwCommSystemObjectID, cwCommCPUUsageSystem=cwCommCPUUsageSystem, cwCommCPUUsageWindow=cwCommCPUUsageWindow, cwCommCPUIndex=cwCommCPUIndex, cwCommSystemResourceUsageMajorEvent=cwCommSystemResourceUsageMajorEvent, cwCommCPUUsageSoftIRQ=cwCommCPUUsageSoftIRQ, cwCommDiskUsageTable=cwCommDiskUsageTable, cwCommCPUUsageObject=cwCommCPUUsageObject, cwCommCPUUsageEntry=cwCommCPUUsageEntry, ciscoWebExMeetingMIB=ciscoWebExMeetingMIB, cwCommMEMUsageObject=cwCommMEMUsageObject, cwCommNotificationHostAddress=cwCommNotificationHostAddress, cwCommNotificationResName=cwCommNotificationResName, ciscoWebExMeetingMIBNotifsGroup=ciscoWebExMeetingMIBNotifsGroup, cwCommDiskTotal=cwCommDiskTotal, ciscoWebExCommSystemResourceGroup=ciscoWebExCommSystemResourceGroup, cwCommDiskUsageIndex=cwCommDiskUsageIndex, cwCommDiskUsage=cwCommDiskUsage, ciscoWebExCommSystemResource=ciscoWebExCommSystemResource, cwCommMEMSwapMonitoringStatus=cwCommMEMSwapMonitoringStatus, cwCommCPUMonitoringStatus=cwCommCPUMonitoringStatus, cwCommDiskUsageEntry=cwCommDiskUsageEntry, ciscoWebExMeetingMIBConform=ciscoWebExMeetingMIBConform, cwCommSysResourceNotificationObject=cwCommSysResourceNotificationObject, cwCommCPUTotalNumber=cwCommCPUTotalNumber, cwCommCPUUsageTable=cwCommCPUUsageTable, cwCommCPUUsageIOWait=cwCommCPUUsageIOWait, cwCommMIBCompliance=cwCommMIBCompliance, ciscoWebExCommInfoGroup=ciscoWebExCommInfoGroup, cwCommDiskUsageObject=cwCommDiskUsageObject, cwCommCPUUsageSteal=cwCommCPUUsageSteal, ciscoWebExMeetingMIBObjects=ciscoWebExMeetingMIBObjects, PYSNMP_MODULE_ID=ciscoWebExMeetingMIB, cwCommCPUUsage=cwCommCPUUsage, cwCommNotificationSeqNum=cwCommNotificationSeqNum, cwCommCPUTotalUsage=cwCommCPUTotalUsage, cwCommCPUName=cwCommCPUName)

#
# PySNMP MIB module PULSESECURE-PSG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PULSESECURE-PSG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, MibIdentifier, Bits, Integer32, Unsigned32, IpAddress, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises, Counter64, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "MibIdentifier", "Bits", "Integer32", "Unsigned32", "IpAddress", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises", "Counter64", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pulsesecure_gateway = ModuleIdentity((1, 3, 6, 1, 4, 1, 12532)).setLabel("pulsesecure-gateway")
pulsesecure_gateway.setRevisions(('2016-07-07 16:10',))
if mibBuilder.loadTexts: pulsesecure_gateway.setLastUpdated('201607071610Z')
if mibBuilder.loadTexts: pulsesecure_gateway.setOrganization('Pulse Secure')
logFullPercent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logFullPercent.setStatus('current')
signedInWebUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signedInWebUsers.setStatus('current')
signedInMailUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signedInMailUsers.setStatus('current')
blockedIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 4), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: blockedIP.setStatus('current')
authServerName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 5), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: authServerName.setStatus('current')
productName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('current')
productVersion = MibScalar((1, 3, 6, 1, 4, 1, 12532, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productVersion.setStatus('current')
fileName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 8), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fileName.setStatus('current')
meetingUserCount = MibScalar((1, 3, 6, 1, 4, 1, 12532, 9), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: meetingUserCount.setStatus('current')
iveCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveCpuUtil.setStatus('current')
iveMemoryUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveMemoryUtil.setStatus('current')
iveConcurrentUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveConcurrentUsers.setStatus('current')
clusterConcurrentUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterConcurrentUsers.setStatus('current')
iveTotalHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveTotalHits.setStatus('current')
iveFileHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveFileHits.setStatus('current')
iveWebHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveWebHits.setStatus('current')
iveAppletHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveAppletHits.setStatus('current')
ivetermHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ivetermHits.setStatus('current')
iveSAMHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveSAMHits.setStatus('current')
iveNCHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveNCHits.setStatus('current')
meetingHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meetingHits.setStatus('current')
meetingCount = MibScalar((1, 3, 6, 1, 4, 1, 12532, 22), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: meetingCount.setStatus('current')
logName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 23), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logName.setStatus('current')
iveSwapUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveSwapUtil.setStatus('current')
diskFullPercent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 25), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskFullPercent.setStatus('current')
blockedIPList = MibTable((1, 3, 6, 1, 4, 1, 12532, 26), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: blockedIPList.setStatus('current')
ipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12532, 26, 1), ).setIndexNames((0, "PULSESECURE-PSG-MIB", "ipIndex"))
if mibBuilder.loadTexts: ipEntry.setStatus('current')
ipIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12532, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipIndex.setStatus('current')
ipValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12532, 26, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipValue.setStatus('current')
logID = MibScalar((1, 3, 6, 1, 4, 1, 12532, 27), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logID.setStatus('current')
logType = MibScalar((1, 3, 6, 1, 4, 1, 12532, 28), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logType.setStatus('current')
logDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 29), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logDescription.setStatus('current')
ivsName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 30), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ivsName.setStatus('deprecated')
ocspResponderURL = MibScalar((1, 3, 6, 1, 4, 1, 12532, 31), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ocspResponderURL.setStatus('current')
fanDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 32), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fanDescription.setStatus('current')
psDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 33), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: psDescription.setStatus('current')
raidDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 34), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: raidDescription.setStatus('current')
clusterName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 35), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clusterName.setStatus('current')
nodeList = MibScalar((1, 3, 6, 1, 4, 1, 12532, 36), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nodeList.setStatus('current')
vipType = MibScalar((1, 3, 6, 1, 4, 1, 12532, 37), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vipType.setStatus('current')
currentVIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 38), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: currentVIP.setStatus('current')
newVIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 39), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: newVIP.setStatus('current')
nicEvent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 40), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nicEvent.setStatus('current')
nodeName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 41), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nodeName.setStatus('current')
iveTemperature = MibScalar((1, 3, 6, 1, 4, 1, 12532, 42), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveTemperature.setStatus('current')
iveVPNTunnels = MibScalar((1, 3, 6, 1, 4, 1, 12532, 43), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveVPNTunnels.setStatus('current')
iveSSLConnections = MibScalar((1, 3, 6, 1, 4, 1, 12532, 44), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveSSLConnections.setStatus('current')
esapVersion = MibScalar((1, 3, 6, 1, 4, 1, 12532, 45), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esapVersion.setStatus('current')
vipChangeReason = MibScalar((1, 3, 6, 1, 4, 1, 12532, 46), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vipChangeReason.setStatus('current')
processName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 47), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: processName.setStatus('current')
iveTotalSignedInUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 48), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveTotalSignedInUsers.setStatus('current')
vpnACLSPercentage = MibScalar((1, 3, 6, 1, 4, 1, 12532, 49), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpnACLSPercentage.setStatus('current')
vpnACLSCount = MibScalar((1, 3, 6, 1, 4, 1, 12532, 50), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpnACLSCount.setStatus('current')
blockedIPv6 = MibScalar((1, 3, 6, 1, 4, 1, 12532, 51), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: blockedIPv6.setStatus('current')
iveTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 251))
iveLogNearlyFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 4)).setObjects(("PULSESECURE-PSG-MIB", "logFullPercent"), ("PULSESECURE-PSG-MIB", "logName"))
if mibBuilder.loadTexts: iveLogNearlyFull.setStatus('current')
iveLogFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 5)).setObjects(("PULSESECURE-PSG-MIB", "logName"))
if mibBuilder.loadTexts: iveLogFull.setStatus('current')
iveMaxConcurrentUsersSignedIn = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 6)).setObjects(("PULSESECURE-PSG-MIB", "iveConcurrentUsers"))
if mibBuilder.loadTexts: iveMaxConcurrentUsersSignedIn.setStatus('current')
iveTooManyFailedLoginAttempts = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 7)).setObjects(("PULSESECURE-PSG-MIB", "blockedIP"))
if mibBuilder.loadTexts: iveTooManyFailedLoginAttempts.setStatus('current')
externalAuthServerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 8)).setObjects(("PULSESECURE-PSG-MIB", "authServerName"))
if mibBuilder.loadTexts: externalAuthServerUnreachable.setStatus('current')
iveStart = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 9))
if mibBuilder.loadTexts: iveStart.setStatus('current')
iveShutdown = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 10))
if mibBuilder.loadTexts: iveShutdown.setStatus('current')
iveReboot = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 11))
if mibBuilder.loadTexts: iveReboot.setStatus('current')
archiveServerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 12))
if mibBuilder.loadTexts: archiveServerUnreachable.setStatus('current')
archiveServerLoginFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 13))
if mibBuilder.loadTexts: archiveServerLoginFailed.setStatus('current')
archiveFileTransferFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 14)).setObjects(("PULSESECURE-PSG-MIB", "fileName"))
if mibBuilder.loadTexts: archiveFileTransferFailed.setStatus('current')
meetingUserLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 15)).setObjects(("PULSESECURE-PSG-MIB", "meetingUserCount"))
if mibBuilder.loadTexts: meetingUserLimit.setStatus('current')
iveRestart = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 16))
if mibBuilder.loadTexts: iveRestart.setStatus('current')
meetingLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 17)).setObjects(("PULSESECURE-PSG-MIB", "meetingCount"))
if mibBuilder.loadTexts: meetingLimit.setStatus('current')
iveDiskNearlyFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 18)).setObjects(("PULSESECURE-PSG-MIB", "diskFullPercent"))
if mibBuilder.loadTexts: iveDiskNearlyFull.setStatus('current')
iveDiskFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 19))
if mibBuilder.loadTexts: iveDiskFull.setStatus('current')
logMessageTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 20)).setObjects(("PULSESECURE-PSG-MIB", "logID"), ("PULSESECURE-PSG-MIB", "logType"), ("PULSESECURE-PSG-MIB", "logDescription"))
if mibBuilder.loadTexts: logMessageTrap.setStatus('current')
memUtilNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 21)).setObjects(("PULSESECURE-PSG-MIB", "iveMemoryUtil"))
if mibBuilder.loadTexts: memUtilNotify.setStatus('current')
cpuUtilNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 22)).setObjects(("PULSESECURE-PSG-MIB", "iveCpuUtil"))
if mibBuilder.loadTexts: cpuUtilNotify.setStatus('current')
swapUtilNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 23)).setObjects(("PULSESECURE-PSG-MIB", "iveSwapUtil"))
if mibBuilder.loadTexts: swapUtilNotify.setStatus('current')
iveMaxConcurrentUsersVirtualSystem = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 24)).setObjects(("PULSESECURE-PSG-MIB", "ivsName"))
if mibBuilder.loadTexts: iveMaxConcurrentUsersVirtualSystem.setStatus('deprecated')
ocspResponderConnectionFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 25)).setObjects(("PULSESECURE-PSG-MIB", "ocspResponderURL"))
if mibBuilder.loadTexts: ocspResponderConnectionFailed.setStatus('current')
iveFanNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 26)).setObjects(("PULSESECURE-PSG-MIB", "fanDescription"))
if mibBuilder.loadTexts: iveFanNotify.setStatus('current')
ivePowerSupplyNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 27)).setObjects(("PULSESECURE-PSG-MIB", "psDescription"))
if mibBuilder.loadTexts: ivePowerSupplyNotify.setStatus('current')
iveRaidNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 28)).setObjects(("PULSESECURE-PSG-MIB", "raidDescription"))
if mibBuilder.loadTexts: iveRaidNotify.setStatus('current')
iveClusterDisableNodeTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 29)).setObjects(("PULSESECURE-PSG-MIB", "clusterName"), ("PULSESECURE-PSG-MIB", "nodeList"))
if mibBuilder.loadTexts: iveClusterDisableNodeTrap.setStatus('current')
iveClusterChangedVIPTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 30)).setObjects(("PULSESECURE-PSG-MIB", "vipType"), ("PULSESECURE-PSG-MIB", "currentVIP"), ("PULSESECURE-PSG-MIB", "newVIP"))
if mibBuilder.loadTexts: iveClusterChangedVIPTrap.setStatus('current')
iveNetExternalInterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 31)).setObjects(("PULSESECURE-PSG-MIB", "nicEvent"))
if mibBuilder.loadTexts: iveNetExternalInterfaceDownTrap.setStatus('current')
iveClusterDeleteTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 32)).setObjects(("PULSESECURE-PSG-MIB", "nodeName"))
if mibBuilder.loadTexts: iveClusterDeleteTrap.setStatus('current')
iveNetInternalInterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 33)).setObjects(("PULSESECURE-PSG-MIB", "nicEvent"))
if mibBuilder.loadTexts: iveNetInternalInterfaceDownTrap.setStatus('current')
iveNetManagementInterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 34)).setObjects(("PULSESECURE-PSG-MIB", "nicEvent"))
if mibBuilder.loadTexts: iveNetManagementInterfaceDownTrap.setStatus('current')
iveTemperatureNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 35)).setObjects(("PULSESECURE-PSG-MIB", "iveTemperature"))
if mibBuilder.loadTexts: iveTemperatureNotify.setStatus('current')
iveVIPNodeChanged = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 36)).setObjects(("PULSESECURE-PSG-MIB", "nodeName"), ("PULSESECURE-PSG-MIB", "vipChangeReason"))
if mibBuilder.loadTexts: iveVIPNodeChanged.setStatus('current')
iveProcessesNearMaxLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 37)).setObjects(("PULSESECURE-PSG-MIB", "processName"))
if mibBuilder.loadTexts: iveProcessesNearMaxLimit.setStatus('current')
iveProcessesReachedMaxLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 38)).setObjects(("PULSESECURE-PSG-MIB", "processName"))
if mibBuilder.loadTexts: iveProcessesReachedMaxLimit.setStatus('current')
iveACLsNearMaxLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 39)).setObjects(("PULSESECURE-PSG-MIB", "vpnACLSPercentage"))
if mibBuilder.loadTexts: iveACLsNearMaxLimit.setStatus('current')
iveACLsCrossedMaxLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 40)).setObjects(("PULSESECURE-PSG-MIB", "vpnACLSCount"))
if mibBuilder.loadTexts: iveACLsCrossedMaxLimit.setStatus('current')
iveTooManyFailedLoginAttemptsIPv6 = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 41)).setObjects(("PULSESECURE-PSG-MIB", "blockedIPv6"))
if mibBuilder.loadTexts: iveTooManyFailedLoginAttemptsIPv6.setStatus('current')
iveSAProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252))
iveICProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253))
iveMAGProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254))
iveVAProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255))
ivePSAProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256))
iveProductMAG2600 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 1))
iveProductMAG4610 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 2))
iveProductSM160 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 3))
iveProductSM360 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 4))
iveProductVASPE = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255, 1))
iveProductVADTE = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255, 2))
iveProductPSA300 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 1))
iveProductPSA3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 2))
iveProductPSA5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 3))
iveProductPSA7000f = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 4))
iveProductPSA7000c = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 5))
iveProductPSA10000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 6))
iveMAG2600 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 1, 1))
iveMAG4610 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 2, 1))
iveMAGSM160 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 3, 1))
iveMAGSM360 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 4, 1))
iveVASPE = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255, 1, 1))
iveVADTE = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255, 2, 1))
ivePSA300 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 1, 1))
ivePSA3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 2, 1))
ivePSA5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 3, 1))
ivePSA7000f = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 4, 1))
ivePSA7000c = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 5, 1))
ivePSA10000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 6, 1))
mibBuilder.exportSymbols("PULSESECURE-PSG-MIB", vipType=vipType, logType=logType, signedInWebUsers=signedInWebUsers, iveFanNotify=iveFanNotify, archiveServerUnreachable=archiveServerUnreachable, iveMAGSM160=iveMAGSM160, iveProductMAG4610=iveProductMAG4610, fanDescription=fanDescription, iveLogNearlyFull=iveLogNearlyFull, iveSAMHits=iveSAMHits, iveProcessesNearMaxLimit=iveProcessesNearMaxLimit, iveTooManyFailedLoginAttemptsIPv6=iveTooManyFailedLoginAttemptsIPv6, iveProductSM160=iveProductSM160, iveProductVADTE=iveProductVADTE, logName=logName, iveMaxConcurrentUsersVirtualSystem=iveMaxConcurrentUsersVirtualSystem, memUtilNotify=memUtilNotify, externalAuthServerUnreachable=externalAuthServerUnreachable, iveClusterDeleteTrap=iveClusterDeleteTrap, esapVersion=esapVersion, iveProductPSA5000=iveProductPSA5000, ivePSA3000=ivePSA3000, nodeList=nodeList, PYSNMP_MODULE_ID=pulsesecure_gateway, logFullPercent=logFullPercent, signedInMailUsers=signedInMailUsers, vipChangeReason=vipChangeReason, archiveServerLoginFailed=archiveServerLoginFailed, meetingHits=meetingHits, diskFullPercent=diskFullPercent, authServerName=authServerName, ivePowerSupplyNotify=ivePowerSupplyNotify, logID=logID, iveTemperatureNotify=iveTemperatureNotify, nodeName=nodeName, currentVIP=currentVIP, vpnACLSCount=vpnACLSCount, nicEvent=nicEvent, swapUtilNotify=swapUtilNotify, ivePSA10000=ivePSA10000, meetingLimit=meetingLimit, iveSAProduct=iveSAProduct, blockedIPv6=blockedIPv6, iveNCHits=iveNCHits, meetingUserCount=meetingUserCount, iveTotalSignedInUsers=iveTotalSignedInUsers, pulsesecure_gateway=pulsesecure_gateway, iveConcurrentUsers=iveConcurrentUsers, fileName=fileName, blockedIPList=blockedIPList, iveProductPSA10000=iveProductPSA10000, iveClusterChangedVIPTrap=iveClusterChangedVIPTrap, iveMAGProduct=iveMAGProduct, logDescription=logDescription, iveProductSM360=iveProductSM360, iveSSLConnections=iveSSLConnections, iveFileHits=iveFileHits, iveWebHits=iveWebHits, iveTooManyFailedLoginAttempts=iveTooManyFailedLoginAttempts, iveTemperature=iveTemperature, productName=productName, iveProductPSA7000c=iveProductPSA7000c, iveRaidNotify=iveRaidNotify, ipIndex=ipIndex, iveRestart=iveRestart, meetingUserLimit=meetingUserLimit, iveProcessesReachedMaxLimit=iveProcessesReachedMaxLimit, iveMAG2600=iveMAG2600, iveMemoryUtil=iveMemoryUtil, logMessageTrap=logMessageTrap, newVIP=newVIP, archiveFileTransferFailed=archiveFileTransferFailed, iveClusterDisableNodeTrap=iveClusterDisableNodeTrap, iveStart=iveStart, iveACLsCrossedMaxLimit=iveACLsCrossedMaxLimit, iveSwapUtil=iveSwapUtil, iveTotalHits=iveTotalHits, ivePSA7000c=ivePSA7000c, iveICProduct=iveICProduct, iveVAProduct=iveVAProduct, ivePSAProduct=ivePSAProduct, meetingCount=meetingCount, blockedIP=blockedIP, ocspResponderURL=ocspResponderURL, cpuUtilNotify=cpuUtilNotify, iveAppletHits=iveAppletHits, iveMaxConcurrentUsersSignedIn=iveMaxConcurrentUsersSignedIn, ivetermHits=ivetermHits, iveDiskNearlyFull=iveDiskNearlyFull, iveVIPNodeChanged=iveVIPNodeChanged, clusterConcurrentUsers=clusterConcurrentUsers, iveVADTE=iveVADTE, iveACLsNearMaxLimit=iveACLsNearMaxLimit, iveProductVASPE=iveProductVASPE, iveProductMAG2600=iveProductMAG2600, iveLogFull=iveLogFull, vpnACLSPercentage=vpnACLSPercentage, iveTraps=iveTraps, iveProductPSA3000=iveProductPSA3000, iveProductPSA7000f=iveProductPSA7000f, raidDescription=raidDescription, iveNetExternalInterfaceDownTrap=iveNetExternalInterfaceDownTrap, ivePSA7000f=ivePSA7000f, processName=processName, iveCpuUtil=iveCpuUtil, clusterName=clusterName, ipValue=ipValue, iveVASPE=iveVASPE, iveMAGSM360=iveMAGSM360, ivePSA300=ivePSA300, iveNetManagementInterfaceDownTrap=iveNetManagementInterfaceDownTrap, iveMAG4610=iveMAG4610, productVersion=productVersion, ivsName=ivsName, psDescription=psDescription, iveShutdown=iveShutdown, ocspResponderConnectionFailed=ocspResponderConnectionFailed, iveProductPSA300=iveProductPSA300, ipEntry=ipEntry, iveReboot=iveReboot, iveNetInternalInterfaceDownTrap=iveNetInternalInterfaceDownTrap, ivePSA5000=ivePSA5000, iveVPNTunnels=iveVPNTunnels, iveDiskFull=iveDiskFull)

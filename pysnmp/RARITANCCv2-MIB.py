#
# PySNMP MIB module RARITANCCv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RARITANCCv2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
internet, Bits, MibIdentifier, Counter64, IpAddress, Counter32, TimeTicks, Unsigned32, mgmt, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, NotificationType, Gauge32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "internet", "Bits", "MibIdentifier", "Counter64", "IpAddress", "Counter32", "TimeTicks", "Unsigned32", "mgmt", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "NotificationType", "Gauge32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
raritan = ModuleIdentity((1, 3, 6, 1, 4, 1, 13742))
raritan.setRevisions(('2011-04-11 11:08',))
if mibBuilder.loadTexts: raritan.setLastUpdated('201104111108Z')
if mibBuilder.loadTexts: raritan.setOrganization('Raritan Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 1))
enterpriseManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 1, 1))
commandCenter = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1))
ccObject = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0))
ccNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1))
ccObjectName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccObjectName.setStatus('current')
ccObjectInstance = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccObjectInstance.setStatus('current')
ccUserName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccUserName.setStatus('current')
ccUserSessionId = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccUserSessionId.setStatus('current')
ccUserNameInitiated = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccUserNameInitiated.setStatus('current')
ccUserNameTerminated = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccUserNameTerminated.setStatus('current')
ccImageType = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccImageType.setStatus('current')
ccImageVersion = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccImageVersion.setStatus('current')
ccImageVersionStatus = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("success", 1), ("failure", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccImageVersionStatus.setStatus('current')
ccUserWhoAdded = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccUserWhoAdded.setStatus('current')
ccUserWhoDeleted = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccUserWhoDeleted.setStatus('current')
ccUserWhoModified = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccUserWhoModified.setStatus('current')
ccNodeName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccNodeName.setStatus('current')
ccLanCard = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccLanCard.setStatus('current')
ccHardDisk = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccHardDisk.setStatus('current')
ccSessionType = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("serial", 1), ("kvm", 2), ("powerOutlet", 3), ("admin", 4), ("diagnostics", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccSessionType.setStatus('current')
ccClusterState = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("standAlone", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccClusterState.setStatus('current')
ccLeafNodeName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 18), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccLeafNodeName.setStatus('current')
ccLeafNodeIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 19), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccLeafNodeIPAddress.setStatus('current')
ccLeafNodeFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 20), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccLeafNodeFirmwareVersion.setStatus('current')
ccScheduledTaskDescription = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 21), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccScheduledTaskDescription.setStatus('current')
ccScheduledTaskFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 22), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccScheduledTaskFailureReason.setStatus('current')
ccDiagnosticConsoleMAX_ACCESSLevel = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 23), DisplayString()).setLabel("ccDiagnosticConsoleMAX-ACCESSLevel").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccDiagnosticConsoleMAX_ACCESSLevel.setStatus('current')
ccDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 24), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccDeviceName.setStatus('current')
ccUserGroupName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 25), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccUserGroupName.setStatus('current')
ccBannerChanges = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("modified", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccBannerChanges.setStatus('current')
ccMOTDChanges = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("modified", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccMOTDChanges.setStatus('current')
ccOldNumberOfOutlets = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 28), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccOldNumberOfOutlets.setStatus('current')
ccNewNumberOfOutlets = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 29), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccNewNumberOfOutlets.setStatus('current')
ccSystemMonitorNotificationLevel = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 30), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccSystemMonitorNotificationLevel.setStatus('current')
ccSystemMonitorNotificationMessage = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 31), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccSystemMonitorNotificationMessage.setStatus('current')
ccDominionPXFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 32), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccDominionPXFirmwareVersion.setStatus('current')
ccClusterPeer = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 33), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccClusterPeer.setStatus('current')
ccClusterOperation = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 34), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccClusterOperation.setStatus('current')
ccClusterOperationStatus = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("success", 1), ("failure", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccClusterOperationStatus.setStatus('current')
ccTransferOperation = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("export", 1), ("import", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccTransferOperation.setStatus('current')
ccFileType = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 37), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccFileType.setStatus('current')
ccLicensedFeature = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 38), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccLicensedFeature.setStatus('current')
ccLicenseServer = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 39), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccLicenseServer.setStatus('current')
ccPortName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 41), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccPortName.setStatus('current')
ccLicenseTerminatedReason = MibScalar((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 0, 40), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccLicenseTerminatedReason.setStatus('current')
ccUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 1)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccClusterState"))
if mibBuilder.loadTexts: ccUnavailable.setStatus('current')
ccAvailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 2)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccClusterState"))
if mibBuilder.loadTexts: ccAvailable.setStatus('current')
ccUserLogin = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 3)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"))
if mibBuilder.loadTexts: ccUserLogin.setStatus('current')
ccUserLogout = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 4)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"))
if mibBuilder.loadTexts: ccUserLogout.setStatus('current')
ccSPortConnectionStarted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 5)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccSessionType"), ("RARITANCCv2-MIB", "ccUserSessionId"), ("RARITANCCv2-MIB", "ccNodeName"), ("RARITANCCv2-MIB", "ccPortName"))
if mibBuilder.loadTexts: ccSPortConnectionStarted.setStatus('current')
ccPortConnectionStopped = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 6)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccSessionType"), ("RARITANCCv2-MIB", "ccUserSessionId"), ("RARITANCCv2-MIB", "ccNodeName"), ("RARITANCCv2-MIB", "ccPortName"))
if mibBuilder.loadTexts: ccPortConnectionStopped.setStatus('current')
ccPortConnectionTerminated = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 7)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserNameInitiated"), ("RARITANCCv2-MIB", "ccUserNameTerminated"), ("RARITANCCv2-MIB", "ccSessionType"), ("RARITANCCv2-MIB", "ccUserSessionId"), ("RARITANCCv2-MIB", "ccNodeName"), ("RARITANCCv2-MIB", "ccPortName"))
if mibBuilder.loadTexts: ccPortConnectionTerminated.setStatus('current')
ccImageUpgradeStarted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 8)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccImageType"), ("RARITANCCv2-MIB", "ccImageVersion"))
if mibBuilder.loadTexts: ccImageUpgradeStarted.setStatus('current')
ccImageUpgradeResults = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 9)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccImageType"), ("RARITANCCv2-MIB", "ccImageVersion"), ("RARITANCCv2-MIB", "ccImageVersionStatus"))
if mibBuilder.loadTexts: ccImageUpgradeResults.setStatus('current')
ccUserAdded = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 10)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccUserWhoAdded"))
if mibBuilder.loadTexts: ccUserAdded.setStatus('current')
ccUserDeleted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 11)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccUserWhoDeleted"))
if mibBuilder.loadTexts: ccUserDeleted.setStatus('current')
ccUserModified = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 12)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccUserWhoModified"))
if mibBuilder.loadTexts: ccUserModified.setStatus('current')
ccUserAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 13)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"))
if mibBuilder.loadTexts: ccUserAuthenticationFailure.setStatus('current')
ccRootPasswordChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 14)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserWhoModified"))
if mibBuilder.loadTexts: ccRootPasswordChanged.setStatus('current')
ccLanCardFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 15)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLanCard"), ("RARITANCCv2-MIB", "ccClusterState"))
if mibBuilder.loadTexts: ccLanCardFailure.setStatus('current')
ccHardDiskFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 16)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccHardDisk"), ("RARITANCCv2-MIB", "ccClusterState"))
if mibBuilder.loadTexts: ccHardDiskFailure.setStatus('current')
ccLeafNodeUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 17)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLeafNodeName"), ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
if mibBuilder.loadTexts: ccLeafNodeUnavailable.setStatus('current')
ccLeafNodeAvailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 18)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLeafNodeName"), ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
if mibBuilder.loadTexts: ccLeafNodeAvailable.setStatus('current')
ccIncompatibleDeviceFirmware = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 19)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"), ("RARITANCCv2-MIB", "ccLeafNodeFirmwareVersion"))
if mibBuilder.loadTexts: ccIncompatibleDeviceFirmware.setStatus('current')
ccDeviceUpgrade = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 20)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"), ("RARITANCCv2-MIB", "ccLeafNodeFirmwareVersion"), ("RARITANCCv2-MIB", "ccImageVersionStatus"))
if mibBuilder.loadTexts: ccDeviceUpgrade.setStatus('current')
ccEnterMaintenanceMode = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 21)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"))
if mibBuilder.loadTexts: ccEnterMaintenanceMode.setStatus('current')
ccExitMaintenanceMode = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 22)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"))
if mibBuilder.loadTexts: ccExitMaintenanceMode.setStatus('current')
ccUserLockedOut = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 23)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"))
if mibBuilder.loadTexts: ccUserLockedOut.setStatus('current')
ccDeviceAddedAfterCCNOCNotification = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 24)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccDeviceName"), ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
if mibBuilder.loadTexts: ccDeviceAddedAfterCCNOCNotification.setStatus('current')
ccScheduledTaskExecutionFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 25)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccScheduledTaskDescription"), ("RARITANCCv2-MIB", "ccScheduledTaskFailureReason"))
if mibBuilder.loadTexts: ccScheduledTaskExecutionFailure.setStatus('current')
ccDiagnosticConsoleLogin = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 26)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccDiagnosticConsoleMAX_ACCESSLevel"))
if mibBuilder.loadTexts: ccDiagnosticConsoleLogin.setStatus('current')
ccDiagnosticConsoleLogout = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 27)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccDiagnosticConsoleMAX_ACCESSLevel"))
if mibBuilder.loadTexts: ccDiagnosticConsoleLogout.setStatus('current')
ccNOCAvailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 28)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
if mibBuilder.loadTexts: ccNOCAvailable.setStatus('current')
ccNOCUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 29)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
if mibBuilder.loadTexts: ccNOCUnavailable.setStatus('current')
ccUserGroupAdded = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 30)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserGroupName"), ("RARITANCCv2-MIB", "ccUserWhoAdded"))
if mibBuilder.loadTexts: ccUserGroupAdded.setStatus('current')
ccUserGroupDeleted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 31)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserGroupName"), ("RARITANCCv2-MIB", "ccUserWhoDeleted"))
if mibBuilder.loadTexts: ccUserGroupDeleted.setStatus('current')
ccUserGroupModified = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 32)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserGroupName"), ("RARITANCCv2-MIB", "ccUserWhoModified"))
if mibBuilder.loadTexts: ccUserGroupModified.setStatus('current')
ccSuperuserNameChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 33)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserWhoModified"))
if mibBuilder.loadTexts: ccSuperuserNameChanged.setStatus('current')
ccSuperuserPasswordChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 34)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserWhoModified"))
if mibBuilder.loadTexts: ccSuperuserPasswordChanged.setStatus('current')
ccLoginBannerChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 35)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserWhoModified"), ("RARITANCCv2-MIB", "ccBannerChanges"))
if mibBuilder.loadTexts: ccLoginBannerChanged.setStatus('current')
ccMOTDChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 36)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserWhoModified"), ("RARITANCCv2-MIB", "ccMOTDChanges"))
if mibBuilder.loadTexts: ccMOTDChanged.setStatus('current')
ccDominionPXReplaced = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 37)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccOldNumberOfOutlets"), ("RARITANCCv2-MIB", "ccNewNumberOfOutlets"))
if mibBuilder.loadTexts: ccDominionPXReplaced.setStatus('current')
ccSystemMonitorNotification = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 38)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccSystemMonitorNotificationLevel"), ("RARITANCCv2-MIB", "ccSystemMonitorNotificationMessage"))
if mibBuilder.loadTexts: ccSystemMonitorNotification.setStatus('current')
ccNeighborhoodActivated = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 39)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"))
if mibBuilder.loadTexts: ccNeighborhoodActivated.setStatus('current')
ccNeighborhoodUpdated = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 40)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"))
if mibBuilder.loadTexts: ccNeighborhoodUpdated.setStatus('current')
ccDominionPXFirmwareChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 41)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccDominionPXFirmwareVersion"))
if mibBuilder.loadTexts: ccDominionPXFirmwareChanged.setStatus('current')
ccClusterFailover = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 42)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccClusterPeer"))
if mibBuilder.loadTexts: ccClusterFailover.setStatus('current')
ccClusterBackupFailed = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 43)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccClusterPeer"))
if mibBuilder.loadTexts: ccClusterBackupFailed.setStatus('current')
ccClusterWaitingPeerDetected = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 44)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccClusterPeer"))
if mibBuilder.loadTexts: ccClusterWaitingPeerDetected.setStatus('current')
ccClusterAction = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 45)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccClusterOperation"), ("RARITANCCv2-MIB", "ccClusterOperationStatus"))
if mibBuilder.loadTexts: ccClusterAction.setStatus('current')
ccCSVFileTransferred = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 46)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccFileType"), ("RARITANCCv2-MIB", "ccTransferOperation"))
if mibBuilder.loadTexts: ccCSVFileTransferred.setStatus('current')
ccPIQUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 47)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLeafNodeName"), ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
if mibBuilder.loadTexts: ccPIQUnavailable.setStatus('current')
ccPIQAvailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 48)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLeafNodeName"), ("RARITANCCv2-MIB", "ccLeafNodeIPAddress"))
if mibBuilder.loadTexts: ccPIQAvailable.setStatus('current')
ccLicenseServerUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 49)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLicenseServer"))
if mibBuilder.loadTexts: ccLicenseServerUnavailable.setStatus('current')
ccLicenseServerFailover = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 50)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLicenseServer"))
if mibBuilder.loadTexts: ccLicenseServerFailover.setStatus('current')
ccLicenseServerAvailable = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 51)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLicenseServer"))
if mibBuilder.loadTexts: ccLicenseServerAvailable.setStatus('current')
ccLicenseTerminated = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 52)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"))
if mibBuilder.loadTexts: ccLicenseTerminated.setStatus('current')
ccAddLicenseFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 53)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"))
if mibBuilder.loadTexts: ccAddLicenseFailure.setStatus('current')
ccAddFeatureFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 54)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLicensedFeature"))
if mibBuilder.loadTexts: ccAddFeatureFailure.setStatus('current')
ccLicenseTerminatedWithReason = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 55)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccLicenseTerminatedReason"))
if mibBuilder.loadTexts: ccLicenseTerminatedWithReason.setStatus('current')
ccUserPasswordChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 1, 1, 1, 1, 56)).setObjects(("RARITANCCv2-MIB", "ccObjectName"), ("RARITANCCv2-MIB", "ccObjectInstance"), ("RARITANCCv2-MIB", "ccUserName"), ("RARITANCCv2-MIB", "ccUserWhoModified"))
if mibBuilder.loadTexts: ccUserPasswordChanged.setStatus('current')
mibBuilder.exportSymbols("RARITANCCv2-MIB", ccNeighborhoodUpdated=ccNeighborhoodUpdated, ccNeighborhoodActivated=ccNeighborhoodActivated, ccUserAdded=ccUserAdded, ccMOTDChanges=ccMOTDChanges, ccLicenseServerFailover=ccLicenseServerFailover, ccMOTDChanged=ccMOTDChanged, ccUserWhoDeleted=ccUserWhoDeleted, ccEnterMaintenanceMode=ccEnterMaintenanceMode, ccClusterState=ccClusterState, ccNOCAvailable=ccNOCAvailable, ccSessionType=ccSessionType, ccUserGroupModified=ccUserGroupModified, ccTransferOperation=ccTransferOperation, ccUserAuthenticationFailure=ccUserAuthenticationFailure, ccUserNameInitiated=ccUserNameInitiated, ccLanCard=ccLanCard, ccLeafNodeFirmwareVersion=ccLeafNodeFirmwareVersion, ccDeviceUpgrade=ccDeviceUpgrade, ccDiagnosticConsoleMAX_ACCESSLevel=ccDiagnosticConsoleMAX_ACCESSLevel, ccClusterWaitingPeerDetected=ccClusterWaitingPeerDetected, ccScheduledTaskFailureReason=ccScheduledTaskFailureReason, ccSystemMonitorNotificationMessage=ccSystemMonitorNotificationMessage, ccFileType=ccFileType, ccDeviceAddedAfterCCNOCNotification=ccDeviceAddedAfterCCNOCNotification, ccUserName=ccUserName, ccObject=ccObject, ccClusterOperation=ccClusterOperation, ccDominionPXFirmwareVersion=ccDominionPXFirmwareVersion, ccClusterFailover=ccClusterFailover, ccClusterPeer=ccClusterPeer, ccImageUpgradeResults=ccImageUpgradeResults, ccLicenseServerAvailable=ccLicenseServerAvailable, ccLeafNodeName=ccLeafNodeName, ccAvailable=ccAvailable, ccObjectInstance=ccObjectInstance, ccIncompatibleDeviceFirmware=ccIncompatibleDeviceFirmware, ccUserGroupAdded=ccUserGroupAdded, ccUnavailable=ccUnavailable, ccSuperuserNameChanged=ccSuperuserNameChanged, ccPIQUnavailable=ccPIQUnavailable, ccUserWhoModified=ccUserWhoModified, ccLicenseTerminated=ccLicenseTerminated, ccNewNumberOfOutlets=ccNewNumberOfOutlets, ccUserPasswordChanged=ccUserPasswordChanged, commandCenter=commandCenter, ccHardDisk=ccHardDisk, products=products, ccPortConnectionTerminated=ccPortConnectionTerminated, ccDominionPXFirmwareChanged=ccDominionPXFirmwareChanged, ccDeviceName=ccDeviceName, enterpriseManagement=enterpriseManagement, ccImageVersion=ccImageVersion, ccClusterOperationStatus=ccClusterOperationStatus, ccNOCUnavailable=ccNOCUnavailable, ccUserGroupName=ccUserGroupName, ccLoginBannerChanged=ccLoginBannerChanged, ccSuperuserPasswordChanged=ccSuperuserPasswordChanged, ccObjectName=ccObjectName, ccCSVFileTransferred=ccCSVFileTransferred, ccUserLogout=ccUserLogout, ccOldNumberOfOutlets=ccOldNumberOfOutlets, ccUserModified=ccUserModified, ccImageType=ccImageType, ccUserGroupDeleted=ccUserGroupDeleted, ccNotify=ccNotify, ccSystemMonitorNotificationLevel=ccSystemMonitorNotificationLevel, ccUserLockedOut=ccUserLockedOut, ccPortConnectionStopped=ccPortConnectionStopped, ccDiagnosticConsoleLogin=ccDiagnosticConsoleLogin, ccLeafNodeAvailable=ccLeafNodeAvailable, ccLicensedFeature=ccLicensedFeature, ccPIQAvailable=ccPIQAvailable, ccUserNameTerminated=ccUserNameTerminated, PYSNMP_MODULE_ID=raritan, ccHardDiskFailure=ccHardDiskFailure, ccNodeName=ccNodeName, raritan=raritan, ccSPortConnectionStarted=ccSPortConnectionStarted, ccImageUpgradeStarted=ccImageUpgradeStarted, ccUserLogin=ccUserLogin, ccExitMaintenanceMode=ccExitMaintenanceMode, ccLeafNodeIPAddress=ccLeafNodeIPAddress, ccRootPasswordChanged=ccRootPasswordChanged, ccScheduledTaskExecutionFailure=ccScheduledTaskExecutionFailure, ccUserWhoAdded=ccUserWhoAdded, ccLicenseTerminatedReason=ccLicenseTerminatedReason, ccBannerChanges=ccBannerChanges, ccAddFeatureFailure=ccAddFeatureFailure, ccClusterAction=ccClusterAction, ccDiagnosticConsoleLogout=ccDiagnosticConsoleLogout, ccUserDeleted=ccUserDeleted, ccScheduledTaskDescription=ccScheduledTaskDescription, ccLicenseServer=ccLicenseServer, ccClusterBackupFailed=ccClusterBackupFailed, ccImageVersionStatus=ccImageVersionStatus, ccLeafNodeUnavailable=ccLeafNodeUnavailable, ccPortName=ccPortName, ccUserSessionId=ccUserSessionId, ccLicenseServerUnavailable=ccLicenseServerUnavailable, ccLicenseTerminatedWithReason=ccLicenseTerminatedWithReason, ccDominionPXReplaced=ccDominionPXReplaced, ccSystemMonitorNotification=ccSystemMonitorNotification, ccLanCardFailure=ccLanCardFailure, ccAddLicenseFailure=ccAddLicenseFailure)

#
# PySNMP MIB module WWP-LEOS-RAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-RAPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Gauge32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, Counter64, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter64", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString, MacAddress, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress", "TruthValue", "RowStatus")
wwpModules, wwpModulesLeos = mibBuilder.importSymbols("WWP-SMI", "wwpModules", "wwpModulesLeos")
wwpLeosRapsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47))
wwpLeosRapsMIB.setRevisions(('2010-09-16 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpLeosRapsMIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: wwpLeosRapsMIB.setLastUpdated('201009161700Z')
if mibBuilder.loadTexts: wwpLeosRapsMIB.setOrganization('Ciena, Inc')
if mibBuilder.loadTexts: wwpLeosRapsMIB.setContactInfo(' Mib Meister 115 North Sullivan Road Spokane Valley, WA 99037 USA Phone: +1 509 242 9000 Email: support@ciena.com')
if mibBuilder.loadTexts: wwpLeosRapsMIB.setDescription('The MIB module for the WWP RAPSMib specific information.')
wwpLeosRapsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1))
wwpLeosRapsGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1))
wwpLeosRapsLogicalRing = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2))
wwpLeosRapsVirtualRing = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3))
wwpLeosRapsVirtualRingMember = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4))
wwpLeosRapsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 2))
wwpLeosRapsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 2, 0))
wwpLeosRapsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 3))
wwpLeosRapsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 3, 1))
wwpLeosRapsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 3, 2))
wwpLeosRapsGlobalAttrs = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1))
wwpLeosRapsState = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsState.setDescription('This object represents the global ring-protection state.')
wwpLeosRapsNodeId = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsNodeId.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsNodeId.setDescription('Node Id.')
wwpLeosRapsEtherType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsEtherType.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsEtherType.setDescription('This object represents the etype value that is used in B-Tag section of RAPS encapsulation..')
wwpLeosRapsNumberOfRings = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsNumberOfRings.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsNumberOfRings.setDescription('Number of logical rings.')
wwpLeosRapsLogicalRingTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1), )
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingTable.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingTable.setDescription('Table of Logical Rings.')
wwpLeosRapsLogicalRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1), ).setIndexNames((0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsLogicalRingIndex"))
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEntry.setDescription('Raps logical ring entry in the logical ring table.')
wwpLeosRapsLogicalRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)))
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingIndex.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingIndex.setDescription('Logical Ring Index.')
wwpLeosRapsLogicalRingName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingName.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingName.setDescription('The name of the logical ring.')
wwpLeosRapsLogicalRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingId.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingId.setDescription('Logical Ring ID.')
wwpLeosRapsLogicalRingGuardTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000)).clone(500)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingGuardTime.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingGuardTime.setDescription('Guard time.')
wwpLeosRapsLogicalRingWtr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)).clone(5)).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWtr.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWtr.setDescription('Wait to restore time.')
wwpLeosRapsLogicalRingWtb = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 6), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWtb.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWtb.setDescription('This object shows Wait To Block time configured for this logical ring.')
wwpLeosRapsLogicalRingWestPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWestPortId.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWestPortId.setDescription('West link port ID')
wwpLeosRapsLogicalRingWestHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWestHoldOffTime.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWestHoldOffTime.setDescription('Holdoff time.')
wwpLeosRapsLogicalRingWestForce = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWestForce.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWestForce.setDescription('This object represents a logial ring link to force switch state.')
wwpLeosRapsLogicalRingWestCfmService = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWestCfmService.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingWestCfmService.setDescription('This object add a CFM service to a logical ring link.')
wwpLeosRapsLogicalRingEastPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEastPortId.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEastPortId.setDescription('East link port ID')
wwpLeosRapsLogicalRingEastHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEastHoldOffTime.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEastHoldOffTime.setDescription('Holdoff time.')
wwpLeosRapsLogicalRingEastForce = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEastForce.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEastForce.setDescription('This object set a logial ring link to force switch state.')
wwpLeosRapsLogicalRingEastCfmService = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEastCfmService.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingEastCfmService.setDescription('This object add a CFM service to a logical ring link.')
wwpLeosRapsLogicalRingNumberOfVirtualRings = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingNumberOfVirtualRings.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsLogicalRingNumberOfVirtualRings.setDescription(' This object shows number of virtual rings in this logical ring.')
wwpLeosRapsVirtualRingTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1), )
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingTable.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingTable.setDescription('Table of Virtual Rings.')
wwpLeosRapsVirtualRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1), ).setIndexNames((0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingIndex"))
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEntry.setDescription('Raps Virtual ring entry in the Virtual ring table.')
wwpLeosRapsVirtualRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240)))
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingIndex.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingIndex.setDescription('Virtual Ring Index.')
wwpLeosRapsVirtualRingName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingName.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingName.setDescription('The name of the virtual ring.')
wwpLeosRapsVirtualRingVid = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingVid.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingVid.setDescription('Virtual Ring VID.')
wwpLeosRapsVirtualRingLogicalRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingLogicalRingId.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingLogicalRingId.setDescription('ID of the logical ring which this virtual ring belongs to.')
wwpLeosRapsVirtualRingMel = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMel.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMel.setDescription('This object represents the Maintenance Group Level of a virtual ring.')
wwpLeosRapsVirtualRingRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingRevertive.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingRevertive.setDescription('This object indicates if a virtual ring is revertive or not.')
wwpLeosRapsVirtualRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("adminDisabled", 1), ("ok", 2), ("protecting", 3), ("recovering", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingState.setDescription('This object shows the current state of a virtual ring.')
wwpLeosRapsVirtualRingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("clear", 1), ("localSignalFail", 2), ("localForceSwitch", 3), ("remoteOrOtherPortSignalFail", 4), ("remoteOrOtherPortForceSwitch", 5), ("provisioningMismatch", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingStatus.setDescription('This object shows the current status of a virtual ring.')
wwpLeosRapsVirtualRingAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("clear", 1), ("protectionSwitching", 2), ("provisionMismatch", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingAlarm.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingAlarm.setDescription('This object shows the current alarm status of a virtual ring.')
wwpLeosRapsVirtualRingNumOfSwitchOvers = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingNumOfSwitchOvers.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingNumOfSwitchOvers.setDescription('This object shows the number of protection switching that has occurred for this virtual ring.')
wwpLeosRapsVirtualRingUptimeFromLastFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 11), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingUptimeFromLastFailure.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingUptimeFromLastFailure.setDescription('This object shows the up time from the last failure for this virtual ring.')
wwpLeosRapsVirtualRingTotalDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 12), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingTotalDownTime.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingTotalDownTime.setDescription('This object shows the total down time for this virtual ring.')
wwpLeosRapsVirtualRingWestPortRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("owner", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortRpl.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortRpl.setDescription("This object RPL ownership for virtual ring's west link.")
wwpLeosRapsVirtualRingWestPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("forwarding", 2), ("blocked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortState.setDescription("This object show the virtual ring's west link state.")
wwpLeosRapsVirtualRingWestPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("oK", 1), ("down", 2), ("ccmFailure", 3), ("localForceSwitch", 4), ("remoteForceSwitch", 5), ("remoteSignalFailure", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortStatus.setDescription("This object show the virtual ring's west link status.")
wwpLeosRapsVirtualRingWestPortNrRxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortNrRxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortNrRxd.setDescription('This object shows number of No Request received on the west link.')
wwpLeosRapsVirtualRingWestPortNrTxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortNrTxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortNrTxd.setDescription('This object shows number of No Request transmitted on the west link.')
wwpLeosRapsVirtualRingWestPortSfRxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortSfRxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortSfRxd.setDescription('This object shows number of Signal Failures received on the west link.')
wwpLeosRapsVirtualRingWestPortSfTxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortSfTxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortSfTxd.setDescription('This object shows number of Signal Failures transmitted on the west link.')
wwpLeosRapsVirtualRingWestPortFsRxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortFsRxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortFsRxd.setDescription('This object shows number of Force Switch received on the west link.')
wwpLeosRapsVirtualRingWestPortFsTxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortFsTxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortFsTxd.setDescription('This object shows number of Force Switch transmitted on the west link.')
wwpLeosRapsVirtualRingWestPortNrRbRxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortNrRbRxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortNrRbRxd.setDescription('This object shows number of No Request RPL Blocked received on the west link.')
wwpLeosRapsVirtualRingWestPortNrRbTxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortNrRbTxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingWestPortNrRbTxd.setDescription('This object shows number of No No Request RPL Blocked transmitted on the west link.')
wwpLeosRapsVirtualRingEastPortRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("owner", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortRpl.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortRpl.setDescription("This object RPL ownership for virtual ring's east link.")
wwpLeosRapsVirtualRingEastPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("forwarding", 2), ("blocked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortState.setDescription("This object show the virtual ring's east link state.")
wwpLeosRapsVirtualRingEastPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ok", 1), ("down", 2), ("ccmFailure", 3), ("localForceSwitch", 4), ("remoteForceSwitch", 5), ("remoteSignalFailure", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortStatus.setDescription("This object show the virtual ring's east link status.")
wwpLeosRapsVirtualRingEastPortNrRxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortNrRxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortNrRxd.setDescription('This object shows number of No Request received on the east link.')
wwpLeosRapsVirtualRingEastPortNrTxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortNrTxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortNrTxd.setDescription('This object shows number of No Request transmitted on the east link.')
wwpLeosRapsVirtualRingEastPortSfRxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortSfRxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortSfRxd.setDescription('This object shows number of Signal Failures received on the east link.')
wwpLeosRapsVirtualRingEastPortSfTxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortSfTxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortSfTxd.setDescription('This object shows number of Signal Failures transmitted on the east link.')
wwpLeosRapsVirtualRingEastPortFsRxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortFsRxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortFsRxd.setDescription('This object shows number of Force Switch received on the east link.')
wwpLeosRapsVirtualRingEastPortFsTxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortFsTxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortFsTxd.setDescription('This object shows number of Force Switch transmitted on the east link.')
wwpLeosRapsVirtualRingEastPortNrRbRxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortNrRbRxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortNrRbRxd.setDescription('This object shows number of No Request RPL Blocked received on the east link.')
wwpLeosRapsVirtualRingEastPortNrRbTxd = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortNrRbTxd.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingEastPortNrRbTxd.setDescription('This object shows number of No No Request RPL Blocked transmitted on the east link.')
wwpLeosRapsVirtualRingType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("majorRing", 1), ("subRing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingType.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingType.setDescription('This object represents the virtual ring type.')
wwpLeosRapsVirtualRingSubRingPortTerm = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noTerminate", 1), ("westPortTerminate", 2), ("eastPortTerminate", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingSubRingPortTerm.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingSubRingPortTerm.setDescription('This object represents the virtual sub ring termination port.')
wwpLeosRapsVirtualRingMemberTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 1), )
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberTable.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberTable.setDescription('Table of Virtual Ring VLAN members.')
wwpLeosRapsVirtualRingMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 1, 1), ).setIndexNames((0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingIndex"), (0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingMemberVlanId"))
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberEntry.setDescription('Raps Virtual ring member entry in the Virtual ring table.')
wwpLeosRapsVirtualRingMemberVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberVlanId.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberVlanId.setDescription('Raps Virtual ring member entry in the Virtual ring table.')
wwpLeosRapsVirtualRingMemberVsTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 2), )
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberVsTable.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberVsTable.setDescription('Table of Virtual Ring members.')
wwpLeosRapsVirtualRingMemberVsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 2, 1), ).setIndexNames((0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingIndex"), (0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingMemberVsId"))
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberVsEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberVsEntry.setDescription('Raps Virtual ring member entry in the Virtual ring table.')
wwpLeosRapsVirtualRingMemberVsId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberVsId.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsVirtualRingMemberVsId.setDescription('Raps Virtual ring member entry in the Virtual ring table.')
wwpLeosRapsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 2, 0, 1)).setObjects(("WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingName"), ("WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingAlarm"))
if mibBuilder.loadTexts: wwpLeosRapsAlarm.setStatus('current')
if mibBuilder.loadTexts: wwpLeosRapsAlarm.setDescription('A alarm notification is sent when a ring detects Provisioning-Mismatch, Protection-Switch-Active or when the condition clears.')
mibBuilder.exportSymbols("WWP-LEOS-RAPS-MIB", wwpLeosRapsLogicalRingWestCfmService=wwpLeosRapsLogicalRingWestCfmService, wwpLeosRapsLogicalRingEastCfmService=wwpLeosRapsLogicalRingEastCfmService, wwpLeosRapsVirtualRingEastPortState=wwpLeosRapsVirtualRingEastPortState, wwpLeosRapsVirtualRingMemberVsId=wwpLeosRapsVirtualRingMemberVsId, wwpLeosRapsVirtualRingStatus=wwpLeosRapsVirtualRingStatus, wwpLeosRapsVirtualRingTotalDownTime=wwpLeosRapsVirtualRingTotalDownTime, wwpLeosRapsVirtualRingEastPortNrRbRxd=wwpLeosRapsVirtualRingEastPortNrRbRxd, wwpLeosRapsVirtualRingMember=wwpLeosRapsVirtualRingMember, wwpLeosRapsLogicalRingWestForce=wwpLeosRapsLogicalRingWestForce, wwpLeosRapsVirtualRingWestPortNrRbTxd=wwpLeosRapsVirtualRingWestPortNrRbTxd, wwpLeosRapsVirtualRingMemberVlanId=wwpLeosRapsVirtualRingMemberVlanId, PYSNMP_MODULE_ID=wwpLeosRapsMIB, wwpLeosRapsMIBObjects=wwpLeosRapsMIBObjects, wwpLeosRapsVirtualRingAlarm=wwpLeosRapsVirtualRingAlarm, wwpLeosRapsVirtualRingWestPortState=wwpLeosRapsVirtualRingWestPortState, wwpLeosRapsVirtualRingWestPortFsTxd=wwpLeosRapsVirtualRingWestPortFsTxd, wwpLeosRapsVirtualRingEastPortNrRbTxd=wwpLeosRapsVirtualRingEastPortNrRbTxd, wwpLeosRapsLogicalRingEastForce=wwpLeosRapsLogicalRingEastForce, wwpLeosRapsVirtualRingEastPortRpl=wwpLeosRapsVirtualRingEastPortRpl, wwpLeosRapsLogicalRingTable=wwpLeosRapsLogicalRingTable, wwpLeosRapsVirtualRingNumOfSwitchOvers=wwpLeosRapsVirtualRingNumOfSwitchOvers, wwpLeosRapsLogicalRing=wwpLeosRapsLogicalRing, wwpLeosRapsVirtualRingWestPortNrTxd=wwpLeosRapsVirtualRingWestPortNrTxd, wwpLeosRapsLogicalRingEastPortId=wwpLeosRapsLogicalRingEastPortId, wwpLeosRapsVirtualRingWestPortStatus=wwpLeosRapsVirtualRingWestPortStatus, wwpLeosRapsVirtualRingState=wwpLeosRapsVirtualRingState, wwpLeosRapsVirtualRingEastPortSfRxd=wwpLeosRapsVirtualRingEastPortSfRxd, wwpLeosRapsLogicalRingEastHoldOffTime=wwpLeosRapsLogicalRingEastHoldOffTime, wwpLeosRapsLogicalRingGuardTime=wwpLeosRapsLogicalRingGuardTime, wwpLeosRapsVirtualRingType=wwpLeosRapsVirtualRingType, wwpLeosRapsMIBCompliances=wwpLeosRapsMIBCompliances, wwpLeosRapsLogicalRingId=wwpLeosRapsLogicalRingId, wwpLeosRapsVirtualRingMemberVsEntry=wwpLeosRapsVirtualRingMemberVsEntry, wwpLeosRapsVirtualRingWestPortRpl=wwpLeosRapsVirtualRingWestPortRpl, wwpLeosRapsVirtualRingWestPortSfRxd=wwpLeosRapsVirtualRingWestPortSfRxd, wwpLeosRapsLogicalRingWestPortId=wwpLeosRapsLogicalRingWestPortId, wwpLeosRapsVirtualRingVid=wwpLeosRapsVirtualRingVid, wwpLeosRapsVirtualRingWestPortSfTxd=wwpLeosRapsVirtualRingWestPortSfTxd, wwpLeosRapsMIBNotifications=wwpLeosRapsMIBNotifications, wwpLeosRapsVirtualRingEastPortFsTxd=wwpLeosRapsVirtualRingEastPortFsTxd, wwpLeosRapsGlobal=wwpLeosRapsGlobal, wwpLeosRapsVirtualRingEntry=wwpLeosRapsVirtualRingEntry, wwpLeosRapsLogicalRingWtb=wwpLeosRapsLogicalRingWtb, wwpLeosRapsVirtualRingName=wwpLeosRapsVirtualRingName, wwpLeosRapsVirtualRingTable=wwpLeosRapsVirtualRingTable, wwpLeosRapsVirtualRingIndex=wwpLeosRapsVirtualRingIndex, wwpLeosRapsVirtualRingEastPortStatus=wwpLeosRapsVirtualRingEastPortStatus, wwpLeosRapsVirtualRingRevertive=wwpLeosRapsVirtualRingRevertive, wwpLeosRapsVirtualRingWestPortNrRbRxd=wwpLeosRapsVirtualRingWestPortNrRbRxd, wwpLeosRapsLogicalRingName=wwpLeosRapsLogicalRingName, wwpLeosRapsVirtualRingMel=wwpLeosRapsVirtualRingMel, wwpLeosRapsVirtualRingWestPortNrRxd=wwpLeosRapsVirtualRingWestPortNrRxd, wwpLeosRapsLogicalRingIndex=wwpLeosRapsLogicalRingIndex, wwpLeosRapsAlarm=wwpLeosRapsAlarm, wwpLeosRapsMIB=wwpLeosRapsMIB, wwpLeosRapsMIBConformance=wwpLeosRapsMIBConformance, wwpLeosRapsGlobalAttrs=wwpLeosRapsGlobalAttrs, wwpLeosRapsLogicalRingNumberOfVirtualRings=wwpLeosRapsLogicalRingNumberOfVirtualRings, wwpLeosRapsVirtualRing=wwpLeosRapsVirtualRing, wwpLeosRapsLogicalRingWtr=wwpLeosRapsLogicalRingWtr, wwpLeosRapsLogicalRingWestHoldOffTime=wwpLeosRapsLogicalRingWestHoldOffTime, wwpLeosRapsVirtualRingWestPortFsRxd=wwpLeosRapsVirtualRingWestPortFsRxd, wwpLeosRapsMIBGroups=wwpLeosRapsMIBGroups, wwpLeosRapsLogicalRingEntry=wwpLeosRapsLogicalRingEntry, wwpLeosRapsVirtualRingEastPortSfTxd=wwpLeosRapsVirtualRingEastPortSfTxd, wwpLeosRapsNumberOfRings=wwpLeosRapsNumberOfRings, wwpLeosRapsVirtualRingEastPortFsRxd=wwpLeosRapsVirtualRingEastPortFsRxd, wwpLeosRapsVirtualRingSubRingPortTerm=wwpLeosRapsVirtualRingSubRingPortTerm, wwpLeosRapsNodeId=wwpLeosRapsNodeId, wwpLeosRapsVirtualRingEastPortNrTxd=wwpLeosRapsVirtualRingEastPortNrTxd, wwpLeosRapsMIBNotificationPrefix=wwpLeosRapsMIBNotificationPrefix, wwpLeosRapsVirtualRingEastPortNrRxd=wwpLeosRapsVirtualRingEastPortNrRxd, wwpLeosRapsVirtualRingMemberEntry=wwpLeosRapsVirtualRingMemberEntry, wwpLeosRapsVirtualRingMemberTable=wwpLeosRapsVirtualRingMemberTable, wwpLeosRapsVirtualRingMemberVsTable=wwpLeosRapsVirtualRingMemberVsTable, wwpLeosRapsState=wwpLeosRapsState, wwpLeosRapsVirtualRingUptimeFromLastFailure=wwpLeosRapsVirtualRingUptimeFromLastFailure, wwpLeosRapsEtherType=wwpLeosRapsEtherType, wwpLeosRapsVirtualRingLogicalRingId=wwpLeosRapsVirtualRingLogicalRingId)
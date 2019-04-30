#
# PySNMP MIB module CISCOSB-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-TRAPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
rldot1dStpTrapVrblVID, rldot1dStpTrapVrblifIndex = mibBuilder.importSymbols("CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID", "rldot1dStpTrapVrblifIndex")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, TimeTicks, Gauge32, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, ObjectIdentity, ModuleIdentity, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "TimeTicks", "Gauge32", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rndNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0))
rndNotifications.setRevisions(('2010-06-25 00:00',))
if mibBuilder.loadTexts: rndNotifications.setLastUpdated('201006250000Z')
if mibBuilder.loadTexts: rndNotifications.setOrganization('Cisco Small Business')
rxOverflowHWFault = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 3)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rxOverflowHWFault.setStatus('current')
txOverflowHWFault = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 4)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: txOverflowHWFault.setStatus('current')
routeTableOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 5)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: routeTableOverflow.setStatus('current')
resetRequired = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 10)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: resetRequired.setStatus('current')
endTftp = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 12)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: endTftp.setStatus('current')
abortTftp = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 13)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: abortTftp.setStatus('current')
startTftp = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 14)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: startTftp.setStatus('current')
faultBackUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 23)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: faultBackUp.setStatus('current')
mainLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 24)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: mainLinkUp.setStatus('current')
ipxRipTblOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 36)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: ipxRipTblOverflow.setStatus('current')
ipxSapTblOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 37)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: ipxSapTblOverflow.setStatus('current')
facsAccessVoilation = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 49)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: facsAccessVoilation.setStatus('current')
autoConfigurationCompleted = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 50)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: autoConfigurationCompleted.setStatus('current')
forwardingTabOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 51)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: forwardingTabOverflow.setStatus('current')
framRelaySwitchConnectionUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 53)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: framRelaySwitchConnectionUp.setStatus('current')
framRelaySwitchConnectionDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 54)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: framRelaySwitchConnectionDown.setStatus('current')
errorsDuringInit = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 61)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: errorsDuringInit.setStatus('current')
vlanDynPortAdded = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 66)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynPortAdded.setStatus('current')
vlanDynPortRemoved = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 67)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynPortRemoved.setStatus('current')
rsSDclientsTableOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 68)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsSDclientsTableOverflow.setStatus('current')
rsSDinactiveServer = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 69)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsSDinactiveServer.setStatus('current')
rsIpZhrConnectionsTableOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 70)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsIpZhrConnectionsTableOverflow.setStatus('current')
rsIpZhrReqStaticConnNotAccepted = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 71)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsIpZhrReqStaticConnNotAccepted.setStatus('current')
rsIpZhrVirtualIpAsSource = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 72)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsIpZhrVirtualIpAsSource.setStatus('current')
rsIpZhrNotAllocVirtualIp = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 73)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsIpZhrNotAllocVirtualIp.setStatus('current')
rsSnmpSetRequestInSpecialCfgState = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 74)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsSnmpSetRequestInSpecialCfgState.setStatus('current')
rsPingCompletion = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 136)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsPingCompletion.setStatus('current')
pppSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 137)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: pppSecurityViolation.setStatus('current')
frDLCIStatudChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 138)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: frDLCIStatudChange.setStatus('current')
papFailedCommunication = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 139)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: papFailedCommunication.setStatus('current')
chapFailedCommunication = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 140)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: chapFailedCommunication.setStatus('current')
rsWSDRedundancySwitch = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 141)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsWSDRedundancySwitch.setStatus('current')
rsDhcpAllocationFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 142)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsDhcpAllocationFailure.setStatus('current')
rlIpFftStnOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 145)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpFftStnOverflow.setStatus('current')
rlIpFftSubOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 146)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpFftSubOverflow.setStatus('current')
rlIpxFftStnOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 147)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpxFftStnOverflow.setStatus('current')
rlIpxFftSubOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 148)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpxFftSubOverflow.setStatus('current')
rlIpmFftOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 149)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpmFftOverflow.setStatus('current')
rlPhysicalDescriptionChanged = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 150)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlPhysicalDescriptionChanged.setStatus('current')
rldot1dStpPortStateForwarding = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 151)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"), ("CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"), ("CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
if mibBuilder.loadTexts: rldot1dStpPortStateForwarding.setStatus('current')
rldot1dStpPortStateNotForwarding = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 152)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"), ("CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"), ("CISCOSB-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
if mibBuilder.loadTexts: rldot1dStpPortStateNotForwarding.setStatus('current')
rlPolicyDropPacketTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 153)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlPolicyDropPacketTrap.setStatus('current')
rlPolicyForwardPacketTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 154)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlPolicyForwardPacketTrap.setStatus('current')
rlIgmpProxyTableOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 156)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIgmpProxyTableOverflow.setStatus('current')
rlIgmpV1MsgReceived = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 157)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIgmpV1MsgReceived.setStatus('current')
rlVrrpEntriesDeleted = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 158)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlVrrpEntriesDeleted.setStatus('current')
rlHotSwapTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 159)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlHotSwapTrap.setStatus('current')
rlTrunkPortAddedTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 160)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlTrunkPortAddedTrap.setStatus('current')
rlTrunkPortRemovedTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 161)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlTrunkPortRemovedTrap.setStatus('current')
rlTrunkPortNotCapableTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 162)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlTrunkPortNotCapableTrap.setStatus('current')
rlLockPortTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 170)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlLockPortTrap.setStatus('current')
vlanDynVlanAdded = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 171)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynVlanAdded.setStatus('current')
vlanDynVlanRemoved = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 172)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynVlanRemoved.setStatus('current')
vlanDynamicToStatic = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 173)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynamicToStatic.setStatus('current')
vlanStaticToDynamic = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 174)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanStaticToDynamic.setStatus('current')
dstrSysLog = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 175)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: dstrSysLog.setStatus('current')
rlEnvMonFanStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 176)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlEnvMonFanStateChange.setStatus('current')
rlEnvMonPowerSupplyStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 177)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlEnvMonPowerSupplyStateChange.setStatus('current')
rlStackStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 178)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackStateChange.setStatus('current')
rlEnvMonTemperatureRisingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 179)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlEnvMonTemperatureRisingAlarm.setStatus('current')
rlBrgMacAddFailedTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 183)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlBrgMacAddFailedTrap.setStatus('current')
rldot1xPortStatusAuthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 184)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xPortStatusAuthorizedTrap.setStatus('current')
rldot1xPortStatusUnauthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 185)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xPortStatusUnauthorizedTrap.setStatus('current')
swIfTablePortLock = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 192)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: swIfTablePortLock.setStatus('current')
swIfTablePortUnLock = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 193)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: swIfTablePortUnLock.setStatus('current')
rlAAAUserLocked = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 194)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlAAAUserLocked.setStatus('current')
bpduGuardPortSuspended = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 202)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: bpduGuardPortSuspended.setStatus('current')
rldot1xSupplicantMacAuthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 203)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xSupplicantMacAuthorizedTrap.setStatus('current')
rldot1xSupplicantMacUnauthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 204)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xSupplicantMacUnauthorizedTrap.setStatus('current')
stpLoopbackDetection = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 205)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: stpLoopbackDetection.setStatus('current')
stpLoopbackDetectionResolved = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 206)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: stpLoopbackDetectionResolved.setStatus('current')
loopbackDetectionPortSuspended = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 207)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: loopbackDetectionPortSuspended.setStatus('current')
rlPortSuspended = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 213)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlPortSuspended.setStatus('current')
rlSpecialBpduDbOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 214)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlSpecialBpduDbOverflow.setStatus('current')
rldot1xSupplicantLoggedOutTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 215)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xSupplicantLoggedOutTrap.setStatus('current')
rldot1xPortControlModeNotAutoTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 216)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xPortControlModeNotAutoTrap.setStatus('current')
rlEeeLldpMultipleNeighbours = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 217)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlEeeLldpMultipleNeighbours.setStatus('current')
rlEeeLldpSingleNeighbour = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 218)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlEeeLldpSingleNeighbour.setStatus('current')
rldot1xSupplicantQuietPeriodTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 219)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xSupplicantQuietPeriodTrap.setStatus('current')
rlStackVersionUpgradeTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 222)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackVersionUpgradeTrap.setStatus('current')
rlStackVersionDowngradeTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 223)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackVersionDowngradeTrap.setStatus('current')
pseInrushPort = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 240)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: pseInrushPort.setStatus('current')
rlStormControlMinRateTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 241)).setObjects(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"), ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStormControlMinRateTrap.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-TRAPS-MIB", resetRequired=resetRequired, rldot1dStpPortStateForwarding=rldot1dStpPortStateForwarding, rlTrunkPortNotCapableTrap=rlTrunkPortNotCapableTrap, rsPingCompletion=rsPingCompletion, rldot1xSupplicantLoggedOutTrap=rldot1xSupplicantLoggedOutTrap, vlanDynamicToStatic=vlanDynamicToStatic, rlSpecialBpduDbOverflow=rlSpecialBpduDbOverflow, vlanDynPortAdded=vlanDynPortAdded, rlStackStateChange=rlStackStateChange, rlVrrpEntriesDeleted=rlVrrpEntriesDeleted, vlanDynVlanRemoved=vlanDynVlanRemoved, facsAccessVoilation=facsAccessVoilation, rlStackVersionUpgradeTrap=rlStackVersionUpgradeTrap, rlIpmFftOverflow=rlIpmFftOverflow, rlTrunkPortAddedTrap=rlTrunkPortAddedTrap, rsSDinactiveServer=rsSDinactiveServer, errorsDuringInit=errorsDuringInit, vlanDynPortRemoved=vlanDynPortRemoved, chapFailedCommunication=chapFailedCommunication, rlEnvMonPowerSupplyStateChange=rlEnvMonPowerSupplyStateChange, rlEeeLldpSingleNeighbour=rlEeeLldpSingleNeighbour, ipxSapTblOverflow=ipxSapTblOverflow, rlTrunkPortRemovedTrap=rlTrunkPortRemovedTrap, rlPortSuspended=rlPortSuspended, rlStormControlMinRateTrap=rlStormControlMinRateTrap, rldot1xSupplicantMacUnauthorizedTrap=rldot1xSupplicantMacUnauthorizedTrap, vlanDynVlanAdded=vlanDynVlanAdded, stpLoopbackDetectionResolved=stpLoopbackDetectionResolved, rsIpZhrVirtualIpAsSource=rsIpZhrVirtualIpAsSource, rsIpZhrNotAllocVirtualIp=rsIpZhrNotAllocVirtualIp, rlIpxFftSubOverflow=rlIpxFftSubOverflow, rlIpxFftStnOverflow=rlIpxFftStnOverflow, rldot1xSupplicantMacAuthorizedTrap=rldot1xSupplicantMacAuthorizedTrap, rlAAAUserLocked=rlAAAUserLocked, rlPolicyDropPacketTrap=rlPolicyDropPacketTrap, rsDhcpAllocationFailure=rsDhcpAllocationFailure, framRelaySwitchConnectionDown=framRelaySwitchConnectionDown, stpLoopbackDetection=stpLoopbackDetection, routeTableOverflow=routeTableOverflow, forwardingTabOverflow=forwardingTabOverflow, abortTftp=abortTftp, pppSecurityViolation=pppSecurityViolation, frDLCIStatudChange=frDLCIStatudChange, vlanStaticToDynamic=vlanStaticToDynamic, ipxRipTblOverflow=ipxRipTblOverflow, startTftp=startTftp, rsIpZhrReqStaticConnNotAccepted=rsIpZhrReqStaticConnNotAccepted, rlIgmpProxyTableOverflow=rlIgmpProxyTableOverflow, rlLockPortTrap=rlLockPortTrap, rsSnmpSetRequestInSpecialCfgState=rsSnmpSetRequestInSpecialCfgState, rlIpFftSubOverflow=rlIpFftSubOverflow, faultBackUp=faultBackUp, bpduGuardPortSuspended=bpduGuardPortSuspended, rxOverflowHWFault=rxOverflowHWFault, rndNotifications=rndNotifications, rlEeeLldpMultipleNeighbours=rlEeeLldpMultipleNeighbours, rlPhysicalDescriptionChanged=rlPhysicalDescriptionChanged, rldot1dStpPortStateNotForwarding=rldot1dStpPortStateNotForwarding, txOverflowHWFault=txOverflowHWFault, rldot1xPortStatusUnauthorizedTrap=rldot1xPortStatusUnauthorizedTrap, rldot1xPortStatusAuthorizedTrap=rldot1xPortStatusAuthorizedTrap, PYSNMP_MODULE_ID=rndNotifications, rlBrgMacAddFailedTrap=rlBrgMacAddFailedTrap, rldot1xSupplicantQuietPeriodTrap=rldot1xSupplicantQuietPeriodTrap, mainLinkUp=mainLinkUp, dstrSysLog=dstrSysLog, rlIpFftStnOverflow=rlIpFftStnOverflow, framRelaySwitchConnectionUp=framRelaySwitchConnectionUp, rlStackVersionDowngradeTrap=rlStackVersionDowngradeTrap, loopbackDetectionPortSuspended=loopbackDetectionPortSuspended, rlEnvMonTemperatureRisingAlarm=rlEnvMonTemperatureRisingAlarm, endTftp=endTftp, rlIgmpV1MsgReceived=rlIgmpV1MsgReceived, pseInrushPort=pseInrushPort, rldot1xPortControlModeNotAutoTrap=rldot1xPortControlModeNotAutoTrap, rlHotSwapTrap=rlHotSwapTrap, papFailedCommunication=papFailedCommunication, rsSDclientsTableOverflow=rsSDclientsTableOverflow, rsWSDRedundancySwitch=rsWSDRedundancySwitch, swIfTablePortUnLock=swIfTablePortUnLock, rlPolicyForwardPacketTrap=rlPolicyForwardPacketTrap, rsIpZhrConnectionsTableOverflow=rsIpZhrConnectionsTableOverflow, rlEnvMonFanStateChange=rlEnvMonFanStateChange, autoConfigurationCompleted=autoConfigurationCompleted, swIfTablePortLock=swIfTablePortLock)

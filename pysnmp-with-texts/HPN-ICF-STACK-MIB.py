#
# PySNMP MIB module HPN-ICF-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-STACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:41:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, Unsigned32, iso, Bits, Integer32, Counter64, ObjectIdentity, Counter32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Unsigned32", "iso", "Bits", "Integer32", "Counter64", "ObjectIdentity", "Counter32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfStack = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91))
hpnicfStack.setRevisions(('2008-04-30 16:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfStack.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfStack.setLastUpdated('200804301650Z')
if mibBuilder.loadTexts: hpnicfStack.setOrganization('')
if mibBuilder.loadTexts: hpnicfStack.setContactInfo('')
if mibBuilder.loadTexts: hpnicfStack.setDescription('This MIB is used to manage STM (Stack Topology Management) information for IRF (Intelligent Resilient Framework) device. This MIB is applicable to IRF-capable products. Some objects in this MIB may be used only for some specific products, so users should refer to the related documents to acquire more detailed information.')
hpnicfStackGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1))
hpnicfStackMaxMember = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackMaxMember.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackMaxMember.setDescription('The maximum number of members in a stack.')
hpnicfStackMemberNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackMemberNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackMemberNum.setDescription('The number of members currently in a stack.')
hpnicfStackMaxConfigPriority = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackMaxConfigPriority.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackMaxConfigPriority.setDescription('The highest priority that can be configured for a member in a stack.')
hpnicfStackAutoUpdate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfStackAutoUpdate.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackAutoUpdate.setDescription('The function for automatically updating the image from the master to a device that is attempting to join the stack. When a new device tries to join a stack, STM verifies the image consistency between the joining device and the master. If the joining device uses a different image version than the master, the function updates the joining device with the image of the master. When this function is disabled, the new device can not join the stack if it uses a different software version than the master. disabled: disable auto update function enabled: enable auto update function')
hpnicfStackMacPersistence = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notPersist", 1), ("persistForSixMin", 2), ("persistForever", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfStackMacPersistence.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackMacPersistence.setDescription('The mode of bridge MAC address persistence. When a stack starts, the bridge MAC address of the master is used as that of the stack. When the master leaves the stack, the bridge MAC address of the stack changes depending on the mode of bridge MAC address persistence. notPersist: The bridge MAC address of the new master is used as that of the stack immediately. persistForSixMin: The original bridge MAC address will be reserved for six minutes. In this period, if the master that has left rejoins the stack, the bridge MAC address of the stack will not change. If the old master does not rejoin the stack within this period, the bridge MAC address of the new master will be used as that of the stack. persistForever: Whether the master leaves or not, the bridge MAC address of the stack will never change.')
hpnicfStackLinkDelayInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setUnits('millisecond').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfStackLinkDelayInterval.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackLinkDelayInterval.setDescription('Delay for stack ports to report a link down event. If the link comes up before the delay timer expires, the stack port will not report the link down event. If the link is not recovered before the delay timer expires, the stack port will report the change. If the delay is set to 0, the stack ports will report a link down event without delay. 0: no delay 1-30000(ms): delay time')
hpnicfStackTopology = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("chainConn", 1), ("ringConn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackTopology.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackTopology.setDescription('Stack topology. chainConn: daisy-chain connection ringConn: ring connection')
hpnicfStackDeviceConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2), )
if mibBuilder.loadTexts: hpnicfStackDeviceConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackDeviceConfigTable.setDescription('This table contains objects to manage device information in a stack.')
hpnicfStackDeviceConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpnicfStackDeviceConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackDeviceConfigEntry.setDescription('This table contains objects to manage device information in a stack.')
hpnicfStackMemberID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackMemberID.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackMemberID.setDescription('The member ID of the device in a stack.')
hpnicfStackConfigMemberID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfStackConfigMemberID.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackConfigMemberID.setDescription('The configured member ID of the device. The valid value ranges from 1 to the value in hpnicfStackMaxMember. The configured member ID will take effect at a reboot if it is unique within the stack.')
hpnicfStackPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfStackPriority.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPriority.setDescription('The priority of a device in the stack. The valid value ranges from 1 to the value in hpnicfStackMaxConfigPriority.')
hpnicfStackPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackPortNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPortNum.setDescription('The number of stack ports enabled in a device.')
hpnicfStackPortMaxNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackPortMaxNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPortMaxNum.setDescription('The maximum number of stack ports in a device.')
hpnicfStackBoardConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 3), )
if mibBuilder.loadTexts: hpnicfStackBoardConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackBoardConfigTable.setDescription('This table contains objects to manage MPU information for a stack.')
hpnicfStackBoardConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpnicfStackBoardConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackBoardConfigEntry.setDescription('This table contains objects to manage MPU information for a stack.')
hpnicfStackBoardRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("slave", 1), ("master", 2), ("loading", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackBoardRole.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackBoardRole.setDescription('The role of the MPU in a stack. slave: Standby MPU master: Master MPU loading: Standby MPU is loading the software image from the master. other: other')
hpnicfStackBoardBelongtoMember = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackBoardBelongtoMember.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackBoardBelongtoMember.setDescription('Member ID of the device that holds the current board.')
hpnicfStackPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4), )
if mibBuilder.loadTexts: hpnicfStackPortInfoTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPortInfoTable.setDescription('This table contains objects to manage stack port information for IRF stacked devices.')
hpnicfStackPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1), ).setIndexNames((0, "HPN-ICF-STACK-MIB", "hpnicfStackMemberID"), (0, "HPN-ICF-STACK-MIB", "hpnicfStackPortIndex"))
if mibBuilder.loadTexts: hpnicfStackPortInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPortInfoEntry.setDescription('This table contains objects to manage stack port information for IRF stacked devices.')
hpnicfStackPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfStackPortIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPortIndex.setDescription('The index of a stack port of the device.')
hpnicfStackPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackPortEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPortEnable.setDescription("The status of a stack port of the device. If no physical ports are added to the stack port, its status is 'disabled'. If the stack port has physical ports, its status is 'enabled'. disabled: The stack port is disabled. enabled: The stack port is enabled.")
hpnicfStackPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("silent", 3), ("disabled", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackPortStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPortStatus.setDescription('The link status of a stack port on the device. up: A physical link is present on the stack port. down: No physical link is present on the stack port. silent: The link state of the stack port is up, but the port cannot transmit or receive traffic. disabled: The stack port does not contain physical links.')
hpnicfStackNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackNeighbor.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackNeighbor.setDescription("The member ID of the stack port's neighbor. 0 means no neighbor exists.")
hpnicfStackPortForwardingPath = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfStackPortForwardingPath.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPortForwardingPath.setDescription("List of egress member IDs on a stack port. Each member device uses the egress member ID lists to choose the outgoing stack port for known unicast frames to be sent out of other member devices. The egress member ID lists are comma separated. A zero-length string means no egress members exist. For example: In a ring stack of 1-2-3-4-5-7-1, if hpnicfStackPortForwardingPath.1.1 returns '7,5,4', IRF-port 1/1 will be the outgoing port for frames to reach members 7, 5, and 4 from member 1.")
hpnicfStackPhyPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 5), )
if mibBuilder.loadTexts: hpnicfStackPhyPortInfoTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPhyPortInfoTable.setDescription('This table contains objects to manage information about physical ports that can be used for IRF stacking.')
hpnicfStackPhyPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpnicfStackPhyPortInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPhyPortInfoEntry.setDescription('This table contains objects to manage information about physical ports that can be used for IRF stacking.')
hpnicfStackBelongtoPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 5, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfStackBelongtoPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackBelongtoPort.setDescription('The index of the stack port to which the physical port is added. 0 means the physical port is not added to any stack port. The value will take effect when IRF is enabled on the device.')
hpnicfStackTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6))
hpnicfStackTrapOjbects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0))
hpnicfStackPortLinkStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 1)).setObjects(("HPN-ICF-STACK-MIB", "hpnicfStackMemberID"), ("HPN-ICF-STACK-MIB", "hpnicfStackPortIndex"), ("HPN-ICF-STACK-MIB", "hpnicfStackPortStatus"))
if mibBuilder.loadTexts: hpnicfStackPortLinkStatusChange.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackPortLinkStatusChange.setDescription('The hpnicfStackPortLinkStatusChange trap indicates that the link status of the stack port has changed.')
hpnicfStackTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 2)).setObjects(("HPN-ICF-STACK-MIB", "hpnicfStackTopology"))
if mibBuilder.loadTexts: hpnicfStackTopologyChange.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackTopologyChange.setDescription('The hpnicfStackTopologyChange trap indicates that the topology type of the IRF stack has changed.')
hpnicfStackMadBfdChangeNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfStackMadBfdChangeNormal.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackMadBfdChangeNormal.setDescription('The hpnicfStackMadBfdChangeNormal trap indicates that the BFD MAD function changed to the normal state.')
hpnicfStackMadBfdChangeFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfStackMadBfdChangeFailure.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackMadBfdChangeFailure.setDescription('The hpnicfStackMadBfdChangeFailure trap indicates that the BFD MAD function changed to the failure state.')
hpnicfStackMadLacpChangeNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 5)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfStackMadLacpChangeNormal.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackMadLacpChangeNormal.setDescription('The hpnicfStackMadLacpChangeNormal trap indicates that the LACP MAD function changed to the normal state.')
hpnicfStackMadLacpChangeFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91, 6, 0, 6)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfStackMadLacpChangeFailure.setStatus('current')
if mibBuilder.loadTexts: hpnicfStackMadLacpChangeFailure.setDescription('The hpnicfStackMadLacpChangeFailure trap indicates that the LACP MAD function changed to the failure state.')
mibBuilder.exportSymbols("HPN-ICF-STACK-MIB", hpnicfStackPortInfoEntry=hpnicfStackPortInfoEntry, hpnicfStackBelongtoPort=hpnicfStackBelongtoPort, PYSNMP_MODULE_ID=hpnicfStack, hpnicfStackMadBfdChangeNormal=hpnicfStackMadBfdChangeNormal, hpnicfStackTrapOjbects=hpnicfStackTrapOjbects, hpnicfStackMaxMember=hpnicfStackMaxMember, hpnicfStackPortForwardingPath=hpnicfStackPortForwardingPath, hpnicfStackTopologyChange=hpnicfStackTopologyChange, hpnicfStackPortLinkStatusChange=hpnicfStackPortLinkStatusChange, hpnicfStackPortMaxNum=hpnicfStackPortMaxNum, hpnicfStackNeighbor=hpnicfStackNeighbor, hpnicfStack=hpnicfStack, hpnicfStackPortStatus=hpnicfStackPortStatus, hpnicfStackTrap=hpnicfStackTrap, hpnicfStackMaxConfigPriority=hpnicfStackMaxConfigPriority, hpnicfStackMadLacpChangeNormal=hpnicfStackMadLacpChangeNormal, hpnicfStackTopology=hpnicfStackTopology, hpnicfStackBoardBelongtoMember=hpnicfStackBoardBelongtoMember, hpnicfStackConfigMemberID=hpnicfStackConfigMemberID, hpnicfStackMacPersistence=hpnicfStackMacPersistence, hpnicfStackPhyPortInfoEntry=hpnicfStackPhyPortInfoEntry, hpnicfStackMadBfdChangeFailure=hpnicfStackMadBfdChangeFailure, hpnicfStackPriority=hpnicfStackPriority, hpnicfStackPortNum=hpnicfStackPortNum, hpnicfStackPortIndex=hpnicfStackPortIndex, hpnicfStackMadLacpChangeFailure=hpnicfStackMadLacpChangeFailure, hpnicfStackPortEnable=hpnicfStackPortEnable, hpnicfStackMemberNum=hpnicfStackMemberNum, hpnicfStackBoardConfigTable=hpnicfStackBoardConfigTable, hpnicfStackBoardConfigEntry=hpnicfStackBoardConfigEntry, hpnicfStackDeviceConfigTable=hpnicfStackDeviceConfigTable, hpnicfStackLinkDelayInterval=hpnicfStackLinkDelayInterval, hpnicfStackMemberID=hpnicfStackMemberID, hpnicfStackAutoUpdate=hpnicfStackAutoUpdate, hpnicfStackBoardRole=hpnicfStackBoardRole, hpnicfStackPhyPortInfoTable=hpnicfStackPhyPortInfoTable, hpnicfStackDeviceConfigEntry=hpnicfStackDeviceConfigEntry, hpnicfStackGlobalConfig=hpnicfStackGlobalConfig, hpnicfStackPortInfoTable=hpnicfStackPortInfoTable)

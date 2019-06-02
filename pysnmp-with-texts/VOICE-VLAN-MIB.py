#
# PySNMP MIB module VOICE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VOICE-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
PortList, VlanIdOrNone = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "VlanIdOrNone")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter32, Bits, Gauge32, Unsigned32, Integer32, TimeTicks, NotificationType, iso, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter32", "Bits", "Gauge32", "Unsigned32", "Integer32", "TimeTicks", "NotificationType", "iso", "IpAddress", "Counter64")
DisplayString, DateAndTime, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "MacAddress", "RowStatus", "TextualConvention")
swVoiceVLANMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 74))
if mibBuilder.loadTexts: swVoiceVLANMIB.setLastUpdated('0910210000Z')
if mibBuilder.loadTexts: swVoiceVLANMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swVoiceVLANMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swVoiceVLANMIB.setDescription('The Voice VLAN module MIB for the proprietary enterprise.')
swVoiceVlanCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 74, 1))
swVoiceVlanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 74, 2))
swVoiceVlanMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 74, 3))
swVoiceVlanId = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 1), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swVoiceVlanId.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanId.setDescription('The VLAN ID of the voice VLAN. The voice VLAN is used to asssign VLAN for untagged voice packets. If the value zero is for display only and not configurable, which means there is no voice VLAN on the switch.')
swVoivceVlanGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swVoivceVlanGlobalState.setStatus('current')
if mibBuilder.loadTexts: swVoivceVlanGlobalState.setDescription('This object indicates the global status of the Voice VLAN. if we enable the voice vlan, we should set the vid first.')
swVoiceVlanPriority = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swVoiceVlanPriority.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanPriority.setDescription('The priority for the voice VLAN ,which is used to distinguish the QoS of the voice traffic from data traffic.')
swVoiceVlanAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swVoiceVlanAgingTime.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanAgingTime.setDescription('The aging time for the voice VLAN ,which is used to remove a port from a voice VLAN when the working mode is auto.')
swVoiceVlanLogState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swVoiceVlanLogState.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanLogState.setDescription(' This object indicates the voice VLAN log state.')
swVoiceVlanMemberPortlist = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVoiceVlanMemberPortlist.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanMemberPortlist.setDescription("The voice VLAN's member ports.")
swVoiceVlanDynamicPortlist = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVoiceVlanDynamicPortlist.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanDynamicPortlist.setDescription("The voice VLAN's member ports that dynamically joined the voice VLAN from a learned voice device.")
swVoiceVlanDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3), )
if mibBuilder.loadTexts: swVoiceVlanDeviceTable.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanDeviceTable.setDescription("The Management information of a voice VLAN member ports'device.")
swVoiceVlanDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1), ).setIndexNames((0, "VOICE-VLAN-MIB", "swVoiceVlanPort"), (0, "VOICE-VLAN-MIB", "swVoiceVlanDeviceAddr"))
if mibBuilder.loadTexts: swVoiceVlanDeviceEntry.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanDeviceEntry.setDescription('The information from the voice device connected to the switch.')
swVoiceVlanPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVoiceVlanPort.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanPort.setDescription("The voice device's connected port.")
swVoiceVlanDeviceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVoiceVlanDeviceAddr.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanDeviceAddr.setDescription('The voice device MAC address.')
swVoiceVlanDeviceStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVoiceVlanDeviceStartTime.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanDeviceStartTime.setDescription('The time the voice device first connected to the switch.')
swVoiceVlanDeviceActiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVoiceVlanDeviceActiveTime.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanDeviceActiveTime.setDescription('The active time of the voice device.')
swVoiceVlanOuiTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1), )
if mibBuilder.loadTexts: swVoiceVlanOuiTable.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanOuiTable.setDescription('The Management information of the voice VLAN OUI.')
swVoiceVlanOuiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1), ).setIndexNames((0, "VOICE-VLAN-MIB", "swVoiceVlanOuiAddr"))
if mibBuilder.loadTexts: swVoiceVlanOuiEntry.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanOuiEntry.setDescription('The management information of the OUI of a voice VLAN domain. An OUI contains information about the type of ip-phone .that can make use of the OUI to check the voice traffic .')
swVoiceVlanOuiAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVoiceVlanOuiAddr.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanOuiAddr.setDescription('The address of the OUI referring to this SwVoiceVlanOuiEntry.')
swVoiceVlanOuiMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swVoiceVlanOuiMask.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanOuiMask.setDescription('The OUI mask indicates the valid bit of the OUI address.')
swVoiceVlanOuiDes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swVoiceVlanOuiDes.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanOuiDes.setDescription('The description of the OUI.')
swVoiceVlanOuiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swVoiceVlanOuiRowStatus.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanOuiRowStatus.setDescription('This object indicates the status of this entry.')
swVoiceVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2), )
if mibBuilder.loadTexts: swVoiceVlanPortTable.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanPortTable.setDescription('The Management of the voice VLAN function on all bridge ports. Some ports are not member ports of a voice VLAN, but they may be added in auto mode, so this function enables both current voice VLAN member ports and non-VLAN member ports to be managed.')
swVoiceVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2, 1), ).setIndexNames((0, "VOICE-VLAN-MIB", "swVoiceVlanPortNumber"))
if mibBuilder.loadTexts: swVoiceVlanPortEntry.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanPortEntry.setDescription('The Management of the voice VLAN function on ports')
swVoiceVlanPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVoiceVlanPortNumber.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanPortNumber.setDescription('Bridge ports, can be configured with voice VLAN function.')
swVoiceVlanPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swVoiceVlanPortState.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanPortState.setDescription('Port state here indicates whether the port supports the voice VLAN function, we can enable/disable voice vlan function on port.')
swVoiceVlanPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swVoiceVlanPortMode.setStatus('current')
if mibBuilder.loadTexts: swVoiceVlanPortMode.setDescription('Port mode just indicates which mode of voice VLAN function is supported by port. If in auto mode ,the port can be added in to voice vlan automatically when it connect a ip-phone,else the port just added by mannual.')
mibBuilder.exportSymbols("VOICE-VLAN-MIB", PYSNMP_MODULE_ID=swVoiceVLANMIB, swVoiceVlanOuiAddr=swVoiceVlanOuiAddr, swVoiceVlanDeviceEntry=swVoiceVlanDeviceEntry, swVoiceVlanOuiRowStatus=swVoiceVlanOuiRowStatus, swVoiceVlanPortEntry=swVoiceVlanPortEntry, swVoiceVLANMIB=swVoiceVLANMIB, swVoiceVlanAgingTime=swVoiceVlanAgingTime, swVoiceVlanCtrl=swVoiceVlanCtrl, swVoiceVlanPortTable=swVoiceVlanPortTable, swVoiceVlanPort=swVoiceVlanPort, swVoiceVlanOuiEntry=swVoiceVlanOuiEntry, swVoiceVlanOuiTable=swVoiceVlanOuiTable, swVoiceVlanDynamicPortlist=swVoiceVlanDynamicPortlist, swVoiceVlanMgmt=swVoiceVlanMgmt, swVoiceVlanOuiMask=swVoiceVlanOuiMask, swVoiceVlanInfo=swVoiceVlanInfo, swVoiceVlanLogState=swVoiceVlanLogState, swVoiceVlanOuiDes=swVoiceVlanOuiDes, swVoivceVlanGlobalState=swVoivceVlanGlobalState, swVoiceVlanDeviceTable=swVoiceVlanDeviceTable, swVoiceVlanPortMode=swVoiceVlanPortMode, swVoiceVlanPortNumber=swVoiceVlanPortNumber, swVoiceVlanPortState=swVoiceVlanPortState, swVoiceVlanMemberPortlist=swVoiceVlanMemberPortlist, swVoiceVlanDeviceAddr=swVoiceVlanDeviceAddr, swVoiceVlanDeviceStartTime=swVoiceVlanDeviceStartTime, swVoiceVlanPriority=swVoiceVlanPriority, swVoiceVlanDeviceActiveTime=swVoiceVlanDeviceActiveTime, swVoiceVlanId=swVoiceVlanId)
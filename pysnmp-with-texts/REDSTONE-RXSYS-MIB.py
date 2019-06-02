#
# PySNMP MIB module REDSTONE-RXSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-RXSYS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
RsEnable, = mibBuilder.importSymbols("REDSTONE-TC", "RsEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Counter64, iso, MibIdentifier, ObjectIdentity, Unsigned32, ModuleIdentity, Gauge32, IpAddress, Integer32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Counter64", "iso", "MibIdentifier", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Gauge32", "IpAddress", "Integer32", "TimeTicks", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rsRXSysMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 17))
rsRXSysMIB.setRevisions(('1999-07-12 00:00', '1999-07-02 00:00', '1999-04-22 00:00', '1998-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsRXSysMIB.setRevisionsDescriptions(('MIB objects for managing RX1400/RX700 systems.', "Added 'ce1' enumeration to RsSysCardType and rsRxSysPortType.", 'Added new enumerations to RsSysCardType and rsRxSysPortType.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: rsRXSysMIB.setLastUpdated('9907120000Z')
if mibBuilder.loadTexts: rsRXSysMIB.setOrganization('Redstone Communications, Inc.')
if mibBuilder.loadTexts: rsRXSysMIB.setContactInfo('Redstone Communications, Inc. 5 Carlisle Road Westford MA 01886 USA +1-978-692-1999 mib@redstonecom.com')
if mibBuilder.loadTexts: rsRXSysMIB.setDescription("Added 'ct1' enumeration to RsSysCardType and rsRxSysPortType.")
rsRXSysTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 0))
rsRXSysObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1))
rsRXSysConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 2))
rsRXSysGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 1))
rsRXSysFabric = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 2))
rsRXSysNvs = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 3))
rsRXSysSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4))
rsRXSysPort = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5))
rsRXSysPower = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6))
rsRXSysTemperature = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7))
class RsSysCardType(TextualConvention, Integer32):
    description = 'The type of card in a system slot: unknown Unknown type. srp Switch/Route Processor. ct3 Channelized T3. oc3 OC-3 (SONET/SDH). ut3Atm Unchannelized T3 (ATM service). ut3Frame Unchannelized T3 (Frame service). ue3Atm Unchannelized E3 (ATM service). ue3Frame Uncahnnelized E3 (Frame service). ce1 Channelized E1. ct1 Channelized T1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 0), ("srp", 1), ("ct3", 2), ("oc3", 3), ("ut3Atm", 4), ("ut3Frame", 5), ("ue3Atm", 6), ("ue3Frame", 7), ("ce1", 8), ("ct1", 9))

rsRXSysChassisRev = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysChassisRev.setStatus('current')
if mibBuilder.loadTexts: rsRXSysChassisRev.setDescription('Chassis revision number. If unknown, the value 255 is reported.')
rsRXSysSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSwVersion.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSwVersion.setDescription('Currently executing operational software version.')
rsRXSysSwBuildDate = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSwBuildDate.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSwBuildDate.setDescription('Build date of currently executing operational software version.')
rsRXSysFabricSpeed = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 2, 1), Integer32()).setUnits('gigabits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysFabricSpeed.setStatus('current')
if mibBuilder.loadTexts: rsRXSysFabricSpeed.setDescription('Speed of switching fabric, in gigabits per second.')
rsRXSysFabricRev = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysFabricRev.setStatus('current')
if mibBuilder.loadTexts: rsRXSysFabricRev.setDescription('Fabric revision number. If unknown, the value 255 is reported.')
rsRXSysNvsStatus = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("notPresent", 0), ("writeProtected", 1), ("volumeError", 2), ("nearCapacity", 3), ("ok", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysNvsStatus.setStatus('current')
if mibBuilder.loadTexts: rsRXSysNvsStatus.setDescription('Status of non-volatile storage (NVS): notPresent NVS is not installed. writeProtected NVS is write-protected. volumeError Status poll of NVS failed. nearCapacity Utilization exceeds 85% of NVS capacity. ok NVS is operational, none of the preceding conditions apply.')
rsRXSysNvsCapacity = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 3, 2), Integer32()).setUnits('megabytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysNvsCapacity.setStatus('current')
if mibBuilder.loadTexts: rsRXSysNvsCapacity.setDescription('Capacity of NVS storage in megabytes.')
rsRXSysNvsUtilPct = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysNvsUtilPct.setStatus('current')
if mibBuilder.loadTexts: rsRXSysNvsUtilPct.setDescription('Percentage of NVS storage used. A value of -1 indicates NVS utilization is unknown.')
rsRXSysSlotCount = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotCount.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotCount.setDescription('The number of slots in the system.')
rsRXSysSlotTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2), )
if mibBuilder.loadTexts: rsRXSysSlotTable.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotTable.setDescription('Table of system slots.')
rsRXSysSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1), ).setIndexNames((0, "REDSTONE-RXSYS-MIB", "rsRXSysSlotIndex"))
if mibBuilder.loadTexts: rsRXSysSlotEntry.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotEntry.setDescription('A table entry describing contents of a system slot.')
rsRXSysSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rsRXSysSlotIndex.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotIndex.setDescription('Slot number. NOTE: Port numbers are zero-based.')
rsRXSysSlotDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotDescr.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotDescr.setDescription('Textual description of the card.')
rsRXSysSlotCurrentCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 3), RsSysCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotCurrentCardType.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotCurrentCardType.setDescription("Type of card actually in the slot. This could be different from the type reported in rsRXSysSlotExpectedCardType, in which case it may be necessary to set rsRXSysSlotControl to 'flush' before this card can be made operational.")
rsRXSysSlotRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotRev.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotRev.setDescription('Revision number of the card. If unknown, the value 255 is reported.')
rsRXSysSlotAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 5), RsEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsRXSysSlotAdminStatus.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotAdminStatus.setDescription('Exerts administrative control to enable/disable the slot.')
rsRXSysSlotOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("empty", 1), ("disabled", 2), ("failed", 3), ("booting", 4), ("initializing", 5), ("online", 6), ("standby", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotOperStatus.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotOperStatus.setDescription('Status of the card.')
rsRXSysSlotDisableReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 0), ("unknown", 1), ("assessing", 2), ("admin", 3), ("cardMismatch", 4), ("fabricLimit", 5), ("imageError", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotDisableReason.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotDisableReason.setDescription('Indicates the condition causing the slot to be disabled: none Value when card is not disabled. unknown Unknown reason for disablement. assessing The slot content is being assessed (transient initialization state). admin The slot is administratively disabled. cardMismatch The current card type conflicts with configuration associated with a different card type that previously occupied the slot. fabricLimit Card resource requirements exceed available fabric capacity. imageError Software image for card is missing or invalid.')
rsRXSysSlotExpectedCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 8), RsSysCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotExpectedCardType.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotExpectedCardType.setDescription("Type of card associated with this slot through prior presence. After the card is removed, this association persists (and inhibits operation of a different card type in this slot, if one is inserted) until rsRXSysSlotControl is set to 'flush'.")
rsRXSysSlotControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noOperation", 0), ("flush", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsRXSysSlotControl.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotControl.setDescription('Administrative control of this slot: noOperation Setting this value has no effect. flush Flushes configuration associated with a card type that previously occupied this slot. Used to explicitly confirm that the slot is now empty, or contains a different card type. Card must be disabled when this value is asserted. See description for rsRXSysSlotDisableReason. reset Resets the slot.')
rsRXSysSlotCpuUtilPct = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotCpuUtilPct.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotCpuUtilPct.setDescription('Percentage of CPU utilization. A value of -1 indicates the utilization is unknown.')
rsRXSysSlotMemUtilPct = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotMemUtilPct.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotMemUtilPct.setDescription('Percentage of memory utilization. A value of -1 indicates the utilization is unknown.')
rsRXSysSlotIoaPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotIoaPresent.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotIoaPresent.setDescription("Indicates whether the card's corresponding I/O adapter is present.")
rsRXSysSlotPortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotPortCount.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotPortCount.setDescription('Number of physical ports for the EXPECTED card type for this slot. NOTE: In event of a card mismatch in this slot, the port count for the CURRENT card in this slot is not recognized/reported until the configuration for the EXPECTED card is explicitly flushed via rsRXSysSlotControl.')
rsRXSysSlotLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysSlotLastChange.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotLastChange.setDescription('The value of sysUpTime when the value of rsRXSysSlotOperStatus last changed.')
rsRXSysPortTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1), )
if mibBuilder.loadTexts: rsRXSysPortTable.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPortTable.setDescription('Table of system physical ports. The information in this table reflects the ports for the EXPECTED card type in each slot; in event of a card mismatch, this table permits navigation of the existing configuration of the expected card type.')
rsRXSysPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1), ).setIndexNames((0, "REDSTONE-RXSYS-MIB", "rsRXSysSlotIndex"), (0, "REDSTONE-RXSYS-MIB", "rsRXSysPortIndex"))
if mibBuilder.loadTexts: rsRXSysPortEntry.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPortEntry.setDescription('A table entry describing a physical port of the system.')
rsRXSysPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rsRXSysPortIndex.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPortIndex.setDescription('Port number of this physical port, relative to the slot in which it resides. Each physical port is uniquely distinguished by its slot/port pair. NOTE: Port numbers are zero-based.')
rsRXSysPortDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysPortDescr.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPortDescr.setDescription('Textual description of this port.')
rsRXSysPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unknown", 0), ("eth", 1), ("ct3", 2), ("oc3c", 3), ("ut3Atm", 4), ("ut3Frame", 5), ("ue3Atm", 6), ("ue3Frame", 7), ("ce1", 8), ("ct1", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysPortType.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPortType.setDescription('Type of the physical port: unknown Unknown port type. eth Ethernet. ct3 Channelized T3. oc3c OC-3c (SONET/SDH). ut3Atm Unchannelized T3 (ATM service). ut3Frame Unchannelized T3 (Frame service). ue3Atm Unchannelized E3 (ATM service). ue3Frame Unchannelized E3 (Frame service). ce1 Channelized E1. ct1 Channelized T1.')
rsRXSysPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPortIfIndex.setDescription('The ifIndex of the Interfaces MIB ifTable entry corresponding to this physical port; if zero, the ifIndex is unknown or does not exist.')
rsRXSysPowerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1), )
if mibBuilder.loadTexts: rsRXSysPowerTable.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPowerTable.setDescription('Table of system power elements.')
rsRXSysPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1, 1), ).setIndexNames((0, "REDSTONE-RXSYS-MIB", "rsRXSysPowerIndex"))
if mibBuilder.loadTexts: rsRXSysPowerEntry.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPowerEntry.setDescription('A table entry describing status of a system power element.')
rsRXSysPowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rsRXSysPowerIndex.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPowerIndex.setDescription('Arbitrary integer index to distinguish entries in this table.')
rsRXSysPowerDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysPowerDescr.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPowerDescr.setDescription('Textual description of this power element.')
rsRXSysPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysPowerStatus.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPowerStatus.setDescription('The status of the power element: inactive No power available from this element. active Power available from this element.')
rsRXSysTempFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("failed", 0), ("ok", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysTempFanStatus.setStatus('current')
if mibBuilder.loadTexts: rsRXSysTempFanStatus.setDescription('Status of fan tray.')
rsRXSysTempTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2), )
if mibBuilder.loadTexts: rsRXSysTempTable.setStatus('current')
if mibBuilder.loadTexts: rsRXSysTempTable.setDescription('Table of system temperature sensors. Sensors are distributed across the chassis, at least one sensor per populated slot.')
rsRXSysTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1), ).setIndexNames((0, "REDSTONE-RXSYS-MIB", "rsRXSysSlotIndex"), (0, "REDSTONE-RXSYS-MIB", "rsRXSysTempIndex"))
if mibBuilder.loadTexts: rsRXSysTempEntry.setStatus('current')
if mibBuilder.loadTexts: rsRXSysTempEntry.setDescription('A table entry describing status of a temperature sensor.')
rsRXSysTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rsRXSysTempIndex.setStatus('current')
if mibBuilder.loadTexts: rsRXSysTempIndex.setDescription('Arbitrary integer index to distinguish sensors associated with the same chassis slot.')
rsRXSysTempDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysTempDescr.setStatus('current')
if mibBuilder.loadTexts: rsRXSysTempDescr.setDescription('Textual description of this sensor.')
rsRXSysTempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("failed", 1), ("tooLow", 2), ("nominal", 3), ("tooHigh", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysTempStatus.setStatus('current')
if mibBuilder.loadTexts: rsRXSysTempStatus.setDescription('The status of a temperature sensor: unknown Unknown. failed Failed. tooLow Below nominal range. nominal Within nominal range. tooHigh Above nominal range.')
rsRXSysTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1, 4), Integer32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRXSysTempValue.setStatus('current')
if mibBuilder.loadTexts: rsRXSysTempValue.setDescription('The temperature measured by this sensor in degrees Celsius. This measurement is valid only if the value of the corresponding rsRXSysTempStatus is nominal.')
rsRXSysSlotOperStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2773, 2, 17, 0, 1)).setObjects(("REDSTONE-RXSYS-MIB", "rsRXSysSlotCurrentCardType"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotAdminStatus"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotOperStatus"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotDisableReason"))
if mibBuilder.loadTexts: rsRXSysSlotOperStatusChange.setStatus('current')
if mibBuilder.loadTexts: rsRXSysSlotOperStatusChange.setDescription('Reports a status change for a slot. This trap is generated on a transition into a stable state (online or disabled) or on a transition out of online.')
rsRXSysPowerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2773, 2, 17, 0, 2)).setObjects(("REDSTONE-RXSYS-MIB", "rsRXSysPowerStatus"))
if mibBuilder.loadTexts: rsRXSysPowerStatusChange.setStatus('current')
if mibBuilder.loadTexts: rsRXSysPowerStatusChange.setDescription('Reports a change in the status of a power element.')
rsRXSysTempFanStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2773, 2, 17, 0, 3)).setObjects(("REDSTONE-RXSYS-MIB", "rsRXSysTempFanStatus"))
if mibBuilder.loadTexts: rsRXSysTempFanStatusChange.setStatus('current')
if mibBuilder.loadTexts: rsRXSysTempFanStatusChange.setDescription('Reports a change in the status of the fan tray.')
rsRXSysTempStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2773, 2, 17, 0, 4)).setObjects(("REDSTONE-RXSYS-MIB", "rsRXSysTempStatus"))
if mibBuilder.loadTexts: rsRXSysTempStatusChange.setStatus('current')
if mibBuilder.loadTexts: rsRXSysTempStatusChange.setDescription('Reports a change in the status of a temperature sensor.')
rsRXSysCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 2, 1))
rsRXSysGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 17, 2, 2))
rsRXSysCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 17, 2, 1, 1)).setObjects(("REDSTONE-RXSYS-MIB", "rsRXSysGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRXSysCompliance = rsRXSysCompliance.setStatus('current')
if mibBuilder.loadTexts: rsRXSysCompliance.setDescription('The compliance statement for entities which implement the Redstone System MIB.')
rsRXSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 17, 2, 2, 1)).setObjects(("REDSTONE-RXSYS-MIB", "rsRXSysChassisRev"), ("REDSTONE-RXSYS-MIB", "rsRXSysSwVersion"), ("REDSTONE-RXSYS-MIB", "rsRXSysSwBuildDate"), ("REDSTONE-RXSYS-MIB", "rsRXSysFabricSpeed"), ("REDSTONE-RXSYS-MIB", "rsRXSysFabricRev"), ("REDSTONE-RXSYS-MIB", "rsRXSysNvsStatus"), ("REDSTONE-RXSYS-MIB", "rsRXSysNvsCapacity"), ("REDSTONE-RXSYS-MIB", "rsRXSysNvsUtilPct"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotCount"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotDescr"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotCurrentCardType"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotRev"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotAdminStatus"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotOperStatus"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotDisableReason"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotExpectedCardType"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotControl"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotCpuUtilPct"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotMemUtilPct"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotIoaPresent"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotPortCount"), ("REDSTONE-RXSYS-MIB", "rsRXSysSlotLastChange"), ("REDSTONE-RXSYS-MIB", "rsRXSysPortDescr"), ("REDSTONE-RXSYS-MIB", "rsRXSysPortType"), ("REDSTONE-RXSYS-MIB", "rsRXSysPortIfIndex"), ("REDSTONE-RXSYS-MIB", "rsRXSysPowerDescr"), ("REDSTONE-RXSYS-MIB", "rsRXSysPowerStatus"), ("REDSTONE-RXSYS-MIB", "rsRXSysTempFanStatus"), ("REDSTONE-RXSYS-MIB", "rsRXSysTempDescr"), ("REDSTONE-RXSYS-MIB", "rsRXSysTempStatus"), ("REDSTONE-RXSYS-MIB", "rsRXSysTempValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRXSysGroup = rsRXSysGroup.setStatus('current')
if mibBuilder.loadTexts: rsRXSysGroup.setDescription('A collection of management objects pertaining to system capabilities in a Redstone product.')
mibBuilder.exportSymbols("REDSTONE-RXSYS-MIB", rsRXSysNvsUtilPct=rsRXSysNvsUtilPct, rsRXSysPortEntry=rsRXSysPortEntry, rsRXSysTrap=rsRXSysTrap, RsSysCardType=RsSysCardType, rsRXSysSlotRev=rsRXSysSlotRev, rsRXSysPowerStatus=rsRXSysPowerStatus, rsRXSysPortDescr=rsRXSysPortDescr, rsRXSysGroup=rsRXSysGroup, rsRXSysSlotAdminStatus=rsRXSysSlotAdminStatus, rsRXSysSlotIoaPresent=rsRXSysSlotIoaPresent, rsRXSysPortIndex=rsRXSysPortIndex, rsRXSysSlotTable=rsRXSysSlotTable, rsRXSysNvsStatus=rsRXSysNvsStatus, rsRXSysPowerEntry=rsRXSysPowerEntry, rsRXSysGroups=rsRXSysGroups, rsRXSysCompliances=rsRXSysCompliances, rsRXSysTemperature=rsRXSysTemperature, rsRXSysTempIndex=rsRXSysTempIndex, rsRXSysGeneral=rsRXSysGeneral, rsRXSysTempDescr=rsRXSysTempDescr, rsRXSysCompliance=rsRXSysCompliance, rsRXSysSlotOperStatus=rsRXSysSlotOperStatus, rsRXSysSlotCpuUtilPct=rsRXSysSlotCpuUtilPct, rsRXSysTempStatusChange=rsRXSysTempStatusChange, rsRXSysFabricRev=rsRXSysFabricRev, rsRXSysSlotMemUtilPct=rsRXSysSlotMemUtilPct, rsRXSysSlotExpectedCardType=rsRXSysSlotExpectedCardType, rsRXSysSlotCurrentCardType=rsRXSysSlotCurrentCardType, rsRXSysSlotPortCount=rsRXSysSlotPortCount, rsRXSysFabric=rsRXSysFabric, rsRXSysTempValue=rsRXSysTempValue, rsRXSysPowerDescr=rsRXSysPowerDescr, rsRXSysPowerIndex=rsRXSysPowerIndex, PYSNMP_MODULE_ID=rsRXSysMIB, rsRXSysFabricSpeed=rsRXSysFabricSpeed, rsRXSysSwBuildDate=rsRXSysSwBuildDate, rsRXSysSlotIndex=rsRXSysSlotIndex, rsRXSysNvsCapacity=rsRXSysNvsCapacity, rsRXSysPortTable=rsRXSysPortTable, rsRXSysTempFanStatus=rsRXSysTempFanStatus, rsRXSysSlot=rsRXSysSlot, rsRXSysSlotDescr=rsRXSysSlotDescr, rsRXSysPower=rsRXSysPower, rsRXSysMIB=rsRXSysMIB, rsRXSysSlotLastChange=rsRXSysSlotLastChange, rsRXSysTempTable=rsRXSysTempTable, rsRXSysPowerStatusChange=rsRXSysPowerStatusChange, rsRXSysSlotCount=rsRXSysSlotCount, rsRXSysSlotControl=rsRXSysSlotControl, rsRXSysTempStatus=rsRXSysTempStatus, rsRXSysPortIfIndex=rsRXSysPortIfIndex, rsRXSysObjects=rsRXSysObjects, rsRXSysPortType=rsRXSysPortType, rsRXSysChassisRev=rsRXSysChassisRev, rsRXSysPowerTable=rsRXSysPowerTable, rsRXSysSwVersion=rsRXSysSwVersion, rsRXSysPort=rsRXSysPort, rsRXSysSlotOperStatusChange=rsRXSysSlotOperStatusChange, rsRXSysTempEntry=rsRXSysTempEntry, rsRXSysSlotDisableReason=rsRXSysSlotDisableReason, rsRXSysConformance=rsRXSysConformance, rsRXSysTempFanStatusChange=rsRXSysTempFanStatusChange, rsRXSysNvs=rsRXSysNvs, rsRXSysSlotEntry=rsRXSysSlotEntry)
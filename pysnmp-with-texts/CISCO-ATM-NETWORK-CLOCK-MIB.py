#
# PySNMP MIB module CISCO-ATM-NETWORK-CLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-NETWORK-CLOCK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PhysicalIndex, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, TimeTicks, iso, ModuleIdentity, MibIdentifier, Unsigned32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "TimeTicks", "iso", "ModuleIdentity", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Bits", "Counter32")
DisplayString, TruthValue, TextualConvention, RowStatus, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus", "TimeStamp")
ciscoAtmNetworkClockMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 121))
ciscoAtmNetworkClockMIB.setRevisions(('2008-02-18 00:00', '2001-12-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmNetworkClockMIB.setRevisionsDescriptions(('The SYNTAX of following objects changed from INTEGER to Integer32. cncNcdpMessageInterval, cncNcdpHoldTime ,cncNcdpPriority , CncNcdpAtmEntry ,cncNcdpAdminWeight,cncNcdpVpi, cncNcdpVci .', 'Intial MIB version.',))
if mibBuilder.loadTexts: ciscoAtmNetworkClockMIB.setLastUpdated('200802180000Z')
if mibBuilder.loadTexts: ciscoAtmNetworkClockMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoAtmNetworkClockMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive, San Jose CA 95134-1706. USA Tel: +1 800 553-NETS E-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmNetworkClockMIB.setDescription("The MIB module for management of network clock distribution and the Network Clock Distribution Protocol (NCDP) in Cisco devices. In the context of this MIB 'network clock' refers to the clock signal that is used to time the physical interfaces. Network clock distribution refers to the distribution of a clock signal through a device and between devices for use by the physical interfaces. (See Bell Communications Research, GR-1244-CORE, 'Clocks for the Synchronized Network: Common Generic Criteria' and Bell Communications Research, GR-436-CORE, 'Digital Network Synchronization Plan'). NCDP is used to configure the network clocking hardware of the platform on which an NCDP entity exists. The underlying network clocking hardware in turn distributes a clock signal through the device for use by the physical interfaces. When all of the interfaces that support synchronous clock recovery in a network are timed to one master clock signal, the network is said to be synchronized. NCDP protocol entities residing on adjacent devices cooperate through the exchange of protocol messages to construct a spanning network clock distribution tree. The tree preserves the synchronous digital hierarchy. After NCDP has determined that its algorithm has converged it superimposes the clock distribution tree on the underlying network and the result is a synchronized network.")
ciscoAtmNetworkClockMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 1))
cncGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1))
cncManualSource = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2))
cncNcdpSource = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3))
cncNcdp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4))
class CncStratum(TextualConvention, Integer32):
    description = "The stratum level associated with a source of network clock or a device. (See American National Standards Institute, ANSI T1.101, 'Synchronization Interface for Digital Networks' and Bell Communications Research, GR-436-CORE, 'Digital Network Synchronization Plan' for more detailed information.)"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("s1", 1), ("s2e", 2), ("s2", 3), ("s3e", 4), ("s3", 5), ("s4e", 6), ("s4", 7), ("other", 8))

class CncHealth(TextualConvention, Integer32):
    description = "The health of a source of network clock. A value of 'good' indicates that a given source of network clock is known by the managed system to be good. A value of 'bad' indicates that a given source of network clock is known by the managed system to be bad. A value of 'unknown' indicates that the health of the source of network clock is unknown to the managed system."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("good", 1), ("bad", 2), ("unknown", 3))

cncDistributionMethod = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ncdp", 1), ("manual", 2))).clone('manual')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cncDistributionMethod.setStatus('current')
if mibBuilder.loadTexts: cncDistributionMethod.setDescription("The method used to distribute network clock for the device. When the mode of operation is 'ncdp', the services provided by the NCDP entity are in use. When this is the case, NCDP entities residing on adjacent nodes exchange protocol messages that are used by the resident NCDP entity to select clock source such that a network-wide clock distribution tree is constructed. When the mode of operation is manual, the NCDP entity is not in use and sources of network clock are statically configured. When this is the case, the construction of a network-wide clock distribution tree is done manually by a network administrator or NMS application.")
cncNotificationOnChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cncNotificationOnChange.setStatus('current')
if mibBuilder.loadTexts: cncNotificationOnChange.setDescription("The value of this object determines whether a notification should be generated due to a change in the device's root clock source (given by the value of cncRootClockSource). A value of 'true' enables the generation of notifications; 'false' disables notification generation.")
cncNodeStratum = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 3), CncStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cncNodeStratum.setStatus('current')
if mibBuilder.loadTexts: cncNodeStratum.setDescription("The stratum at which the device exists in the Synchronous Digital Hierarchy (See American National Standards Institute, ANSI T1.101, 'Synchronization Interface for Digital Networks' and Bell Communications Research, GR-436-CORE, 'Digital Network Synchronization Plan' for more detailed information regarding stratum.). The resident NCDP entity uses the value of this object to enforce the network clock distribution stratum hierarchy. This object is only used by the NCDP protocol entity.")
cncNcdpMaxDiameter = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cncNcdpMaxDiameter.setStatus('current')
if mibBuilder.loadTexts: cncNcdpMaxDiameter.setDescription('The maximum possible height of a network clock distribution tree in the network. (Alternatively this is known as the maximum diameter of the network of devices that are participating in NCDP.) If all of the nodes in the network are participating in the protocol then the maximum height of the network clock distribution tree is exactly the maximum diameter of the network. If a proper subset of the nodes are participating in the NCDP then the maximum height of a network clock distribution tree is the maximum diameter of the subnetwork induced by the removal of the non-participating nodes and their associated links. The NCDP protocol entity uses the value of this object to determine when the NCDP algorithm has converged. All devices participating in NCDP within the bounds of the network must use the same value for maximum network diameter for the NCDP algorithm to operate properly. If the value of this object is set too small the resultant network may exhibit unstable clocking characteristics and may constantly switch clock sources. If the value is much larger than the network diameter, the algorithm will take longer to declare convergence than if the diameter were set closer to the actual maximum network diameter, the result being that it will take longer for the network to resynchronize after a switchover to a secondary clock source located on a secondary device. This object is only used by the NCDP protocol entity.')
cncNcdpMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(75, 60000)).clone(500)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cncNcdpMessageInterval.setStatus('current')
if mibBuilder.loadTexts: cncNcdpMessageInterval.setDescription('The interval at which NCDP configuration PDUs are to be generated. The message interval directly affects the convergence time of the NCDP algorithm. Convergence time is equal to the max network diameter * message interval + transmission delays + the time a configuration PDU is spent being processed in each device. Thus if transmission delays and processing delays are both close to 0, the convergence time is approximately ( max network diameter * message interval ) milliseconds. The value of cncNcdpHoldTime should normally match the value of this object. This object is only used by the NCDP protocol entity.')
cncNcdpHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(75, 60000)).clone(500)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cncNcdpHoldTime.setStatus('current')
if mibBuilder.loadTexts: cncNcdpHoldTime.setDescription('The delay between the transmission of NCDP configuration PDUs. The hold time is used to limit the transmission of NCDP configuration PDUs out of an interface to a maximum of one configuration PDU per hold time interval per interface. The value of this object should normally be set to match the value of cncNcdpMessageInterval. If the value of this object is higher than the value of cncNcdpMessageInterval, NCDP configuration PDUs will end up being propagated at the rate specified by the value of this object instead. This object is only used by the NCDP protocol entity.')
cncSourceChangeReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("lossOfLock", 2), ("lossOfActivity", 3), ("ncdpRestructure", 4), ("other", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cncSourceChangeReason.setStatus('current')
if mibBuilder.loadTexts: cncSourceChangeReason.setDescription("The reason for the most recent change of a source of network clock, as indicated by the change in the value of cncSourceChangeTimeStamp. 'none' indicates that the source of network clock has not changed. 'lossOfLock' indicates that the clock source was changed because the network clocking hardware lost lock on the previous network clock source. 'lossOfActivity' indicates that the clock source was changed because the network clocking hardware detected a loss of activity on the previous network clock source. 'ncdpRestructure' indicates that the NCDP entity has changed the clock source as a result of a network-wide network clock distribution tree restructuring process. When the reason for a clock switchover is none of the above, the value of this object is 'other'.")
cncSourceChangeTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cncSourceChangeTimeStamp.setStatus('current')
if mibBuilder.loadTexts: cncSourceChangeTimeStamp.setDescription('The value of sysUpTime when the most recent change of a source of network clock occurred. A value of 0 indicates that no such event has occurred since the instantiation of this object.')
cncRootClockSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 9), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cncRootClockSource.setStatus('current')
if mibBuilder.loadTexts: cncRootClockSource.setDescription('The entPhysicalIndex of the network clock source that is actively supplying network clock within the device.')
cncManualSourceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1), )
if mibBuilder.loadTexts: cncManualSourceTable.setStatus('current')
if mibBuilder.loadTexts: cncManualSourceTable.setDescription('A table of network clock sources available to the managed system.')
cncManualSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-ATM-NETWORK-CLOCK-MIB", "cncManualSourcePriority"))
if mibBuilder.loadTexts: cncManualSourceEntry.setStatus('current')
if mibBuilder.loadTexts: cncManualSourceEntry.setDescription("Network clock status and statistics for sources of network clock. When the value of cncDistributionMethod is 'manual', the managed system uses this table to select a source of network clock for the managed system. Within this table a physical entity that is a source of network clock is identified by cncManualSourceId. Table entries are indexed by priority (cncManualSourcePriority). A source of network clock for the device may be an oscillator local to the device, a Building Integrated Timing Supply (BITS) port or an interface that supports synchronous clock recovery. (BITS is explained in more detail in Bell Communications Research, GR-436-CORE, 'Digital Network Synchronization Plan'.) When the managed system initializes it creates a row for the device's default source of network clock, (the entry having cncManualSourcePriority with value 'default'). The only operations allowed on the columnar objects in this particular row are read operations. Other rows are created or destroyed by a management station or through the device's local management interface when a source of network clock is configured or removed. When a management station creates a row it creates it explicitly using RowStatus with either createAndGo or createAndWait. A row is not made active until a valid value for cncManualSourceId is supplied. A management station may perform a write operation on any columnar object while the row is active or not in service. The value of any instance of cncManualSourceId located in the table is unique except when the value refers to the device's default source of network clock; any instance of cncManualSourceId within the table may have this value at any time.")
cncManualSourcePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("default", 3))))
if mibBuilder.loadTexts: cncManualSourcePriority.setStatus('current')
if mibBuilder.loadTexts: cncManualSourcePriority.setDescription("A value used to identify a source of network clock available to the device's manual network clock selection algorithm.")
cncManualSourceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1, 2), PhysicalIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cncManualSourceId.setStatus('current')
if mibBuilder.loadTexts: cncManualSourceId.setDescription('The entPhysicalIndex that uniquely identifies a source of network clock within the managed system.')
cncManualSourceHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1, 3), CncHealth()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cncManualSourceHealth.setStatus('current')
if mibBuilder.loadTexts: cncManualSourceHealth.setDescription('The health of the clock source identified by cncManualSourceId.')
cncManualRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cncManualRowStatus.setStatus('current')
if mibBuilder.loadTexts: cncManualRowStatus.setDescription('The status of this conceptual row.')
cncNcdpSourceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1), )
if mibBuilder.loadTexts: cncNcdpSourceTable.setStatus('current')
if mibBuilder.loadTexts: cncNcdpSourceTable.setDescription('A table of configured network clock sources available to the managed system for use by the NCDP protocol entity.')
cncNcdpSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cncNcdpSourceEntry.setStatus('current')
if mibBuilder.loadTexts: cncNcdpSourceEntry.setDescription("Network clock status and statistics for sources of network clock identified by entPhysicalIndex and used by the managed system when the value of cncDistributionMethod is 'ncdp'. A source of network clock for the device may be an oscillator local to the device, a Building Integrated Timing Supply (BITS) port or an interface that supports synchronous clock recovery. (BITS is explained in more detail in Bell Communications Research, GR-436-CORE, 'Digital Network Synchronization Plan'.) The NCDP protocol entity selects one entry in this table to advertise as the best available clock source for the device. Cooperating NCDP protocol entities select the best available clock source among those advertised within the cooperating group and build a clock distribution tree rooted at that clock source. When the value of cncRootClockSource is used as an index into this table and the indicated clock source has cncNcdpBestClockSource with value 'true' then the indicated clock source is the root of some clock distribution tree. If only one such root exists on all participating devices in the network, then it is the root of a network wide clock distribution tree. When the managed system initializes it creates a row for the device's default source of network clock. This row cannot be destroyed by a management station. Within this row a write operation is only allowed on the cncNcdpPriority object; only read operations are allowed on all other columnar objects within this specific row. The status of this row is always active. The default source can always be found by issuing a read operation on the row within cncManualSourceTable indexed by 'default' (as the value of cncManualSourcePriority). The cncManualSourceId object contains the entPhysicalIndex of the default source of network clock and identifies it within this table. Other rows are created or destroyed by a management station or through the device's local management interface when a source of network clock is configured or removed. When a management station creates a row it creates it explicitly using RowStatus with either createAndGo or createAndWait. A row is not made active until all read-create objects not having default values are properly initialized. The values of cncNcdpPriority, cncNcdpStratum and cncNcdpPRSReference collectively describe a source of network clock, that is they are three components of a vector used as an input to the NCDP algorithm to make clock source selection decisions. The management station must make the row notInService before changing the values of any of these objects.")
cncNcdpBestClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cncNcdpBestClockSource.setStatus('current')
if mibBuilder.loadTexts: cncNcdpBestClockSource.setDescription('An indication of whether the NCDP entity is presently advertising this clock source as the best clock source available in this table.')
cncNcdpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cncNcdpPriority.setStatus('current')
if mibBuilder.loadTexts: cncNcdpPriority.setDescription('The network-wide priority of this clock source if configured as a source of network clock for NCDP. The highest priority clock source is that clock source having the lowest positive numeric value. The clock source with the highest priority is selected as the root of the clock distribution tree by the NCDP algorithm. If more that one clock source is configured with with the same priority the NCDP algorithm uses the value cncNcdpStratum as a tiebreaker.')
cncNcdpStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 3), CncStratum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cncNcdpStratum.setStatus('current')
if mibBuilder.loadTexts: cncNcdpStratum.setDescription("The stratum level associated with this clock source if configured as a source of network clock for NCDP. (See American National Standards Institute, ANSI T1.101, 'Synchronization Interface for Digital Networks' and Bell Communications Research, GR-436-CORE, 'Digital Network Synchronization Plan' for more detailed information regarding stratum.). If the value of this object is used as a tiebreaker by the NCDP protocol entity, the lower of the given values is the winner. If the values are the same, the value of cncNcdpPRSReference is used as a tiebreaker by the NCDP algorithm.")
cncNcdpPRSReference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("external", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cncNcdpPRSReference.setStatus('current')
if mibBuilder.loadTexts: cncNcdpPRSReference.setDescription("An value that identifies the primary reference source that the network clock available from this source is traceable to if configured as a source of network clock for NCDP. (See American National Standards Institute, ANSI T1.101, 'Synchronization Interface for Digital Networks' and Bell Communications Research, GR-436-CORE, 'Digital Network Synchronization Plan' for more detailed information regarding Primary Reference Sources.). If a source of network clock is an onboard oscillator local to the device it is 'internal' otherwise it is 'external'. If the value of this object is used as a tiebreaker by the NCDP algorithm,'external' wins over 'internal'. All 'external' sources of network clock are assumed to be traceable to the same PRS by the NCDP protocol entity.")
cncNcdpSourceHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 5), CncHealth()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cncNcdpSourceHealth.setStatus('current')
if mibBuilder.loadTexts: cncNcdpSourceHealth.setDescription('The health of the clock source associated with this row.')
cncNcdpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cncNcdpRowStatus.setStatus('current')
if mibBuilder.loadTexts: cncNcdpRowStatus.setDescription('The status of this conceptual row.')
cncNcdpAtmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1), )
if mibBuilder.loadTexts: cncNcdpAtmTable.setStatus('current')
if mibBuilder.loadTexts: cncNcdpAtmTable.setDescription("A table containing the status of NCDP on the device's ATM interfaces.")
cncNcdpAtmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cncNcdpAtmEntry.setStatus('current')
if mibBuilder.loadTexts: cncNcdpAtmEntry.setDescription('An entry in the cncNcdpAtm table containing the status of Ncdp on an ATM interface. A row in this table is created by the managed system and disappears when the associated physical entity disappears. When a row is created all of the row objects are instantiated.')
cncNcdpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cncNcdpEnable.setStatus('current')
if mibBuilder.loadTexts: cncNcdpEnable.setDescription("An indication of whether NCDP is presently running on an interface. When NCDP is enabled for an interface, the interface is an active member of the clock distribution topology as seen by the NCDP protocol entity. After this object is instantiated by the agent the managed system initializes the value of this object to 'true' if it determines that the physical interface is an ATM Network-to-Network Interface (see ATM Forum Private Network-Network Interface Specification Version 1.0). In all other cases the managed system initializes the value of this object to 'false'.")
cncNcdpAdminWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777215)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cncNcdpAdminWeight.setStatus('current')
if mibBuilder.loadTexts: cncNcdpAdminWeight.setDescription('A weight metric used by the NCDP protocol entity and associated with a physical interface that supports synchronous clock recovery. When NCDP is enabled for the physical interface the value of this object is used by NCDP algorithms during tree computations. The lower the administrative weight, the more attractive the given link is to the NCDP algorithm. If the weight of a link is changed, it can cause the NCDP protocol entity to reconstruct the clock distribution tree.')
cncNcdpVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cncNcdpVpi.setStatus('current')
if mibBuilder.loadTexts: cncNcdpVpi.setDescription('The VPI value of the VCC supporting the NCDP entity at this ATM interface. If the values of cncNcdpVpi and cncNcdpVci are both equal to zero then the NCDP entity is not supported at this ATM interface.')
cncNcdpVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(34)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cncNcdpVci.setStatus('current')
if mibBuilder.loadTexts: cncNcdpVci.setDescription('The VCI value of the VCC supporting the NCDP entity at this ATM interface. If the values of cncNcdpVpi and cncNcdpVci are both equal to zero then the NCDP entity is not supported at this ATM interface.')
cncNcdpHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 5), CncHealth()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cncNcdpHealth.setStatus('current')
if mibBuilder.loadTexts: cncNcdpHealth.setDescription('The health of the clock source associated with this row.')
ciscoAtmNetworkClockNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 2))
ciscoAtmNetworkClockMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 2, 0))
cncNotifySourceChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 121, 2, 0, 1)).setObjects(("CISCO-ATM-NETWORK-CLOCK-MIB", "cncSourceChangeReason"))
if mibBuilder.loadTexts: cncNotifySourceChange.setStatus('current')
if mibBuilder.loadTexts: cncNotifySourceChange.setDescription("This notification indicates that the agent has detected a change in the device's root source of network clock. This notification is generated whenever there is a switchover from one clock source to another.")
ciscoAtmNetworkClockConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 3))
ciscoAtmNetworkClockMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 1))
ciscoAtmNetworkClockMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 2))
cncMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 1, 1)).setObjects(("CISCO-ATM-NETWORK-CLOCK-MIB", "cncGroup"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cncMIBCompliance = cncMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cncMIBCompliance.setDescription('The compliance statement for SNMPv2 entities which implement network clock distribution methods and NCDP.')
cncGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 2, 1)).setObjects(("CISCO-ATM-NETWORK-CLOCK-MIB", "cncDistributionMethod"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNotificationOnChange"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNodeStratum"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpMaxDiameter"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpMessageInterval"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpHoldTime"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncSourceChangeReason"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncSourceChangeTimeStamp"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncRootClockSource"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncManualSourceId"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncManualSourceHealth"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncManualRowStatus"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpBestClockSource"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpPriority"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpStratum"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpPRSReference"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpSourceHealth"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpRowStatus"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpEnable"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpAdminWeight"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpVpi"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpVci"), ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpHealth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cncGroup = cncGroup.setStatus('current')
if mibBuilder.loadTexts: cncGroup.setDescription('The cnc group of objects providing for management of network clock distribution and NCDP entities.')
cncNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 2, 2)).setObjects(("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNotifySourceChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cncNotificationGroup = cncNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cncNotificationGroup.setDescription('Conformance group for cnc notifications.')
mibBuilder.exportSymbols("CISCO-ATM-NETWORK-CLOCK-MIB", cncManualSourceId=cncManualSourceId, ciscoAtmNetworkClockNotificationPrefix=ciscoAtmNetworkClockNotificationPrefix, ciscoAtmNetworkClockConformance=ciscoAtmNetworkClockConformance, ciscoAtmNetworkClockMIBNotifications=ciscoAtmNetworkClockMIBNotifications, cncNcdpSourceEntry=cncNcdpSourceEntry, cncManualSourceEntry=cncManualSourceEntry, cncManualSourceHealth=cncManualSourceHealth, cncManualSourcePriority=cncManualSourcePriority, cncNcdpHealth=cncNcdpHealth, ciscoAtmNetworkClockMIB=ciscoAtmNetworkClockMIB, cncNcdpMaxDiameter=cncNcdpMaxDiameter, cncNcdp=cncNcdp, cncNcdpRowStatus=cncNcdpRowStatus, cncGroup=cncGroup, cncNcdpEnable=cncNcdpEnable, cncDistributionMethod=cncDistributionMethod, cncNcdpPRSReference=cncNcdpPRSReference, cncMIBCompliance=cncMIBCompliance, cncNcdpPriority=cncNcdpPriority, cncNcdpAdminWeight=cncNcdpAdminWeight, cncRootClockSource=cncRootClockSource, cncGlobal=cncGlobal, cncNcdpBestClockSource=cncNcdpBestClockSource, cncNcdpHoldTime=cncNcdpHoldTime, cncNcdpVpi=cncNcdpVpi, cncNotifySourceChange=cncNotifySourceChange, PYSNMP_MODULE_ID=ciscoAtmNetworkClockMIB, cncNotificationOnChange=cncNotificationOnChange, cncNcdpAtmEntry=cncNcdpAtmEntry, cncNcdpAtmTable=cncNcdpAtmTable, cncNcdpVci=cncNcdpVci, cncNcdpStratum=cncNcdpStratum, cncSourceChangeTimeStamp=cncSourceChangeTimeStamp, cncSourceChangeReason=cncSourceChangeReason, ciscoAtmNetworkClockMIBCompliances=ciscoAtmNetworkClockMIBCompliances, cncManualSource=cncManualSource, cncNcdpSourceHealth=cncNcdpSourceHealth, CncHealth=CncHealth, cncNcdpSource=cncNcdpSource, cncManualRowStatus=cncManualRowStatus, cncNodeStratum=cncNodeStratum, CncStratum=CncStratum, cncNcdpSourceTable=cncNcdpSourceTable, ciscoAtmNetworkClockMIBGroups=ciscoAtmNetworkClockMIBGroups, cncNotificationGroup=cncNotificationGroup, ciscoAtmNetworkClockMIBObjects=ciscoAtmNetworkClockMIBObjects, cncManualSourceTable=cncManualSourceTable, cncNcdpMessageInterval=cncNcdpMessageInterval)
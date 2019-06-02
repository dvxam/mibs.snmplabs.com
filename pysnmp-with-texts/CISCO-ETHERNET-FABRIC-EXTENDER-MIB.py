#
# PySNMP MIB module CISCO-ETHERNET-FABRIC-EXTENDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ETHERNET-FABRIC-EXTENDER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:57:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, Integer32, ObjectIdentity, Counter64, MibIdentifier, IpAddress, Counter32, Gauge32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "Integer32", "ObjectIdentity", "Counter64", "MibIdentifier", "IpAddress", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType")
RowStatus, TruthValue, DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TimeStamp", "TextualConvention")
ciscoEthernetFabricExtenderMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 691))
ciscoEthernetFabricExtenderMIB.setRevisions(('2009-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEthernetFabricExtenderMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEthernetFabricExtenderMIB.setLastUpdated('200902230000Z')
if mibBuilder.loadTexts: ciscoEthernetFabricExtenderMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoEthernetFabricExtenderMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-nexus5000@cisco.com')
if mibBuilder.loadTexts: ciscoEthernetFabricExtenderMIB.setDescription("The MIB module for configuring one or more fabric extenders to connect into a core switch. Since fabric extenders might not be manageable entities, this MIB is assumed to be instrumented on the core switch. A fabric extender may be hardwired or preconfigured with a list of uplink ports. These uplink ports are used to connect to a core switch. A fabric extender is assumed to be directly connected to its core switch. Each physical interface on the core switch is assumed to be connected to one and only one fabric extender. When an extender powers up, it runs a link local discovery protocol to find core switches. The extender puts all available self identification in its discovery report. The core switch, depending on configuration, uses the extenders identification to accept or deny an extender from connecting. A fabric extender may be connected to different core switches via different uplink ports. In that case, each core switch's instance of the MIB may refer to the same extender. Ports on core switch used to connect to extenders are known as Fabric ports. A fabric port may be a physical interface or a logical interface such as an EtherChannel. An extender may connect into a core switch via more than one fabric port. Non fabric ports on an extender are typically used to connect hosts/servers.")
ciscoEthernetFabricExtenderMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 691, 0))
ciscoEthernetFabricExtenderObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 691, 1))
ciscoEthernetFabricExtenderMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 691, 2))
cefexConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1))
class CiscoPortPinningMode(TextualConvention, Integer32):
    description = "This denotes the mode of re-pinning. Re-pinning defines how traffic forwarding is altered between fabric extender and its core switch in case of a fabric port state change. For fabric extenders that do not support local forwarding, they do not perform normal address learning and forwarding as a traditional 802.1d compliant bridge. A method named 'pinning' is used instead to dictate forwarding behavior. That means, traffic from a specific non fabric port is always forwarded to its pinned fabric port (no local forwarding). Each non fabric port is 'pinned' to one of the fabric ports. Load balancing aspects affecting pinned fabric port selection is dictated by internal implementation. If a particular fabric port fails, all the non fabric ports pinned to the failed fabric port may need to be moved to the remaining fabric ports, if any. Note that traffic distribution within a fabric EtherChannel does not utilize the 'pinning' method. The traditional hash of MAC address, IP address and TCP/UDP port is used to select fabric port within a fabric EtherChannel. It is planned that more enumeration will be introduced in subsequent updates. static(1) - If this mode is chosen, non fabric ports are not re-pinned to other fabric ports in case of fabric port failure."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("static", 1))

cefexBindingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1), )
if mibBuilder.loadTexts: cefexBindingTable.setStatus('current')
if mibBuilder.loadTexts: cefexBindingTable.setDescription("This table has the binding information of a 'Fabric Port' to 'Fabric Extender' on a 'Extender Core Switch'. Each entry in this table configures one fabric port. A core switch does not accept fabric extender connections into its fabric ports unless the extender matches an entry in this table. Once matched, the extender is identified by the instances of the cefexBindingExtenderIndex in the matching row. The matching criteria and values to match for each fabric extender are specified in a row in the cefexConfigTable. Each row in the cefexConfigTable is indexed by cefexBindingExtenderIndex. Each row in this table has an unique cefexBindingExtenderIndex value, therefore, providing the linkage between the two tables. It is expected that user first creates a row in the cefexConfigTable for a specific cefexBindingExtenderIndex, followed by creation of the corresponding row in this table for the same cefexBindingExtenderIndex.. If a row in this table is created and if there is no corresponding row created in the cefexConfigTable, then the agent will automatically create a row in the cefexConfigTable with instance of every object in this row initialized to the DEFVAL.")
cefexBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingInterfaceOnCoreSwitch"))
if mibBuilder.loadTexts: cefexBindingEntry.setStatus('current')
if mibBuilder.loadTexts: cefexBindingEntry.setDescription('There is one entry in this table for each core switch Interface that can be connected to an uplink interface of a fabric extender.')
cefexBindingInterfaceOnCoreSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cefexBindingInterfaceOnCoreSwitch.setStatus('current')
if mibBuilder.loadTexts: cefexBindingInterfaceOnCoreSwitch.setDescription('This object is the index that uniquely identifies an entry in the cefexBindingTable. The value of this object is an IfIndex to a fabric port. By creating a row in this table for a particular core switch interface, the user enables that core switch interface to accept a fabric extender. By default, a core switch interface does not have an entry in this table and consequently does not accept/respond to discovery requests from fabric extenders.')
cefexBindingExtenderIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 999))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cefexBindingExtenderIndex.setStatus('current')
if mibBuilder.loadTexts: cefexBindingExtenderIndex.setDescription('The value of cefexBindingExtenderIndex used as an Index into the cefexConfigTable to select the Fabric Extender configuration for this binding entry. However, a value in this table does not imply that an instance with this value exists in the cefexConfigTable. If an entry corresponding to the value of this object does not exist in cefexConfigTable, the system default behavior (using DEFVAL values for all the configuration objects as defined in cefexConfigTable) of the Fabric Extender is used for this binding entry. Since an extender may connect to a core switch via multiple interfaces or fabric ports, it is important all the binding entries configuring the same fabric extender are configured with the same extender Index. Every interface on different fabric extender connecting into the same core switch is differentiated by its extender id. To refer to a port on the extender, an example representation may be extender/slot/port. Extender id values 1-99 are reserved. For example, reserved values can be used to identify the core switch and its line cards in the extender/slot/port naming scheme. cefexBindingExtenderIndex identifies further attributes of a fabric extender via the cefexConfigTable. A user may choose to identify a fabric extender by specifying its value of cefexConfigExtendername and/or other attributes.')
cefexBindingCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefexBindingCreationTime.setStatus('current')
if mibBuilder.loadTexts: cefexBindingCreationTime.setDescription("The timestamp of this entry's creation time.")
cefexBindingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cefexBindingRowStatus.setStatus('current')
if mibBuilder.loadTexts: cefexBindingRowStatus.setDescription('The status of this conceptual row.')
cefexConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2), )
if mibBuilder.loadTexts: cefexConfigTable.setStatus('current')
if mibBuilder.loadTexts: cefexConfigTable.setDescription('This table facilitates configuration applicable to an entire fabric extender.')
cefexConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingExtenderIndex"))
if mibBuilder.loadTexts: cefexConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cefexConfigEntry.setDescription('There is one entry in this table for each fabric extender configured on the core switch.')
cefexConfigExtenderName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cefexConfigExtenderName.setStatus('current')
if mibBuilder.loadTexts: cefexConfigExtenderName.setDescription("This object specifies a human readable string representing the name of the 'Extender'. Note that default value of this object will be the string 'FEXxxxx' where xxxx is value of cefexBindingExtenderIndex expressed as 4 digits. For example, if cefexBindingExtenderIndex is 123, the default value of this object is 'FEX0123'. This object allows the user to identify the extender with an appropriate name.")
cefexConfigSerialNumCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cefexConfigSerialNumCheck.setStatus('current')
if mibBuilder.loadTexts: cefexConfigSerialNumCheck.setDescription("This object specifies if the serial number check is enabled for this extender or not. If the value of this object is 'true', then the core switch rejects any extender except for the one with serial number string specified by cefexConfigSerialNum. If the value of this object is 'false', then the core switch accept any extender.")
cefexConfigSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cefexConfigSerialNum.setStatus('current')
if mibBuilder.loadTexts: cefexConfigSerialNum.setDescription("This object allows the user to identify a fabric extender's Serial Number String. This object is relevant if cefexBindingSerialNumCheck is true. Zero is not a valid length for this object if cefexBindingSerialNumCheck is true.")
cefexConfigPinningFailOverMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 4), CiscoPortPinningMode().clone('static')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cefexConfigPinningFailOverMode.setStatus('current')
if mibBuilder.loadTexts: cefexConfigPinningFailOverMode.setDescription('This object allows the user to identify the fabric port failure handling method when pinning is used.')
cefexConfigPinningMaxLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cefexConfigPinningMaxLinks.setStatus('current')
if mibBuilder.loadTexts: cefexConfigPinningMaxLinks.setDescription('This object allows the user to identify number of fabric ports to be used in distribution of pinned non fabric ports. As described above, pinning is the forwarding model used for fabric extenders that do not support local forwarding. Traffic from a non fabric port is forwarded to one fabric port. Selection of non fabric port pinning to fabric ports is distributed as evenly as possible across fabric ports. This object allows administrator to configure number of fabric ports that should be used for pinning non fabric ports.')
cefexConfigCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefexConfigCreationTime.setStatus('current')
if mibBuilder.loadTexts: cefexConfigCreationTime.setDescription("The timestamp when the value of the corresponding instance of 'cefexConfigRowStatus' is made active. If an user modifies objects in this table, the new values are immediately activated. Depending on the object changed, an accepted fabric extender may become not acceptable. As a result, the fabric extender may be disconnected from the core switch.")
cefexConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cefexConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: cefexConfigRowStatus.setDescription('The status of this conceptual row. A row in this table becomes active immediately upon creation.')
cEthernetFabricExtenderMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 691, 2, 1))
cEthernetFabricExtenderMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 691, 2, 2))
cEthernetFabricExtenderMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 691, 2, 1, 1)).setObjects(("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingConformanceObjects"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEthernetFabricExtenderMIBCompliance = cEthernetFabricExtenderMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cEthernetFabricExtenderMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-ETHERNET-FABRIC-EXTENDER-MIB mib.')
cefexBindingConformanceObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 691, 2, 2, 1)).setObjects(("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingExtenderIndex"), ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingCreationTime"), ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingRowStatus"), ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigExtenderName"), ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigSerialNumCheck"), ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigSerialNum"), ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigPinningFailOverMode"), ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigPinningMaxLinks"), ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigCreationTime"), ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefexBindingConformanceObjects = cefexBindingConformanceObjects.setStatus('current')
if mibBuilder.loadTexts: cefexBindingConformanceObjects.setDescription('A collection of objects related to Fabric Extender binding to core switch.')
mibBuilder.exportSymbols("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", cefexBindingConformanceObjects=cefexBindingConformanceObjects, cefexConfigPinningFailOverMode=cefexConfigPinningFailOverMode, cefexConfig=cefexConfig, PYSNMP_MODULE_ID=ciscoEthernetFabricExtenderMIB, cefexConfigCreationTime=cefexConfigCreationTime, cefexBindingEntry=cefexBindingEntry, cefexConfigTable=cefexConfigTable, ciscoEthernetFabricExtenderMIBConformance=ciscoEthernetFabricExtenderMIBConformance, cefexBindingTable=cefexBindingTable, cefexBindingRowStatus=cefexBindingRowStatus, CiscoPortPinningMode=CiscoPortPinningMode, cEthernetFabricExtenderMIBCompliances=cEthernetFabricExtenderMIBCompliances, cefexConfigEntry=cefexConfigEntry, cefexConfigSerialNum=cefexConfigSerialNum, ciscoEthernetFabricExtenderMIBNotifs=ciscoEthernetFabricExtenderMIBNotifs, cefexConfigSerialNumCheck=cefexConfigSerialNumCheck, cefexConfigPinningMaxLinks=cefexConfigPinningMaxLinks, cEthernetFabricExtenderMIBCompliance=cEthernetFabricExtenderMIBCompliance, ciscoEthernetFabricExtenderObjects=ciscoEthernetFabricExtenderObjects, ciscoEthernetFabricExtenderMIB=ciscoEthernetFabricExtenderMIB, cEthernetFabricExtenderMIBGroups=cEthernetFabricExtenderMIBGroups, cefexBindingCreationTime=cefexBindingCreationTime, cefexConfigExtenderName=cefexConfigExtenderName, cefexConfigRowStatus=cefexConfigRowStatus, cefexBindingInterfaceOnCoreSwitch=cefexBindingInterfaceOnCoreSwitch, cefexBindingExtenderIndex=cefexBindingExtenderIndex)
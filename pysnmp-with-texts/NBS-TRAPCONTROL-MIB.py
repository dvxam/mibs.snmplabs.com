#
# PySNMP MIB module NBS-TRAPCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-TRAPCONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:17:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, nbs = mibBuilder.importSymbols("NBS-CMMC-MIB", "InterfaceIndex", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Unsigned32, Integer32, ObjectIdentity, iso, MibIdentifier, Counter32, NotificationType, Gauge32, ModuleIdentity, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Unsigned32", "Integer32", "ObjectIdentity", "iso", "MibIdentifier", "Counter32", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsTrapControlMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 209))
if mibBuilder.loadTexts: nbsTrapControlMib.setLastUpdated('200903300119Z')
if mibBuilder.loadTexts: nbsTrapControlMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsTrapControlMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsTrapControlMib.setDescription('MIB to specify which SNMP Notifications (Traps) are supported, and for which interfaces (ports) each should be sent.')
nbsTrapListGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 209, 1))
if mibBuilder.loadTexts: nbsTrapListGrp.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListGrp.setDescription('List of SNMP Notifications (Traps) emitted by Agent')
nbsTrapIfGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 209, 2))
if mibBuilder.loadTexts: nbsTrapIfGrp.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfGrp.setDescription('List of interfaces managed by Agent')
nbsTrapListTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 209, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTableSize.setDescription('The number of entries in nbsTrapListTable.')
nbsTrapListTable = MibTable((1, 3, 6, 1, 4, 1, 629, 209, 1, 2), )
if mibBuilder.loadTexts: nbsTrapListTable.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTable.setDescription('A table to list SNMP Notifications emitted by Agent')
nbsTrapListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1), ).setIndexNames((0, "NBS-TRAPCONTROL-MIB", "nbsTrapListIndex"))
if mibBuilder.loadTexts: nbsTrapListEntry.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListEntry.setDescription('Describes a particular SNMP Notification/Trap.')
nbsTrapListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: nbsTrapListIndex.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListIndex.setDescription('Agent-generated unique ID. Numbering is contiguous and starts from 1.')
nbsTrapListTrapMib = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapMib.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTrapMib.setDescription('The name of the mib where this SNMP Notification is defined. An example would be IF-MIB.')
nbsTrapListTrapName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapName.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTrapName.setDescription('Trap Name; the name given in the NOTIFICATION-TYPE definition. An example would be linkUp')
nbsTrapListTrapDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapDescription.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTrapDescription.setDescription("Brief explanation of this SNMP Notification. Agent may use the first 100 characters of the DESCRIPTION clause from the Notification's MIB definition.")
nbsTrapListTrapOID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapOID.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTrapOID.setDescription('The sysObjectId, as reported in the enterprise field of the SNMPv1 trap PDU')
nbsTrapIfTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 209, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapIfTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfTableSize.setDescription('The number of entries in nbsTrapIfTable.')
nbsTrapIfTable = MibTable((1, 3, 6, 1, 4, 1, 629, 209, 2, 2), )
if mibBuilder.loadTexts: nbsTrapIfTable.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfTable.setDescription('A list of all interfaces managed by Agent, and which traps to send for each.')
nbsTrapIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1), ).setIndexNames((0, "NBS-TRAPCONTROL-MIB", "nbsTrapIfIndex"))
if mibBuilder.loadTexts: nbsTrapIfEntry.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfEntry.setDescription('Indicates traps for a particular interface.')
nbsTrapIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsTrapIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfIndex.setDescription('The ifIndex from the Mib2 ifTable.')
nbsTrapIfTrapsCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapIfTrapsCaps.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfTrapsCaps.setDescription('Bitmask indicating which SNMP Notifications are supported for this interface. Bit 0 is reserved. Subsequent bits refer to the nbsTrapListTable. Bit 1 corresponds to the first table entry, Bit 2 to the second entry, and so on. A bit is set (1) if that SNMP Notification can be sent for this interface, and cleared (0) if unavailable. OCTET STRING bitmasks count the leftmost bit (MSB) as 0.')
nbsTrapIfTrapsSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsTrapIfTrapsSelect.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfTrapsSelect.setDescription('Bitmask administrating which SNMP Notifications should be sent for this interface. Bit 0 is reserved. Subsequent bits refer to the nbsTrapListTable. Bit 1 corresponds to the first table entry, Bit 2 to the second entry, and so on. A bit is set (1) if that SNMP Notification should be emitted for this interface, and cleared (0) if it should be suppressed. OCTET STRING bitmasks count the leftmost bit (MSB) as 0.')
mibBuilder.exportSymbols("NBS-TRAPCONTROL-MIB", nbsTrapListIndex=nbsTrapListIndex, nbsTrapListEntry=nbsTrapListEntry, nbsTrapListTrapDescription=nbsTrapListTrapDescription, nbsTrapListGrp=nbsTrapListGrp, nbsTrapControlMib=nbsTrapControlMib, nbsTrapIfGrp=nbsTrapIfGrp, nbsTrapListTrapName=nbsTrapListTrapName, nbsTrapListTrapOID=nbsTrapListTrapOID, nbsTrapIfTableSize=nbsTrapIfTableSize, nbsTrapIfIndex=nbsTrapIfIndex, nbsTrapIfTrapsSelect=nbsTrapIfTrapsSelect, nbsTrapIfEntry=nbsTrapIfEntry, nbsTrapListTable=nbsTrapListTable, nbsTrapListTrapMib=nbsTrapListTrapMib, nbsTrapIfTable=nbsTrapIfTable, PYSNMP_MODULE_ID=nbsTrapControlMib, nbsTrapListTableSize=nbsTrapListTableSize, nbsTrapIfTrapsCaps=nbsTrapIfTrapsCaps)
#
# PySNMP MIB module ASCEND-MIBALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBALARM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Bits, MibIdentifier, IpAddress, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Bits", "MibIdentifier", "IpAddress", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibalarmProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 33))
mibalarmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 33, 1), )
if mibBuilder.loadTexts: mibalarmProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibalarmProfileTable.setDescription('A list of mibalarmProfile profile entries.')
mibalarmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1), ).setIndexNames((0, "ASCEND-MIBALARM-MIB", "alarmProfile-Name"))
if mibBuilder.loadTexts: mibalarmProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibalarmProfileEntry.setDescription('A mibalarmProfile entry containing objects that maps to the parameters of mibalarmProfile profile.')
alarmProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 1), DisplayString()).setLabel("alarmProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmProfile_Name.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Name.setDescription('The name consists of a null terminated ascii string supplied by the user')
alarmProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("alarmProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Enabled.setDescription('TRUE if the alarm profile is enabled, otherwise FALSE.')
alarmProfile_Event = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("lineStateChange", 1), ("slotStateChange", 2), ("primarySwitchover", 3), ("powerFailure", 4), ("fanFailure", 5), ("secondaryControllerStateChange", 6), ("inputRelayClosed", 7), ("inputRelayOpen", 8), ("lowTemperatureTrigger", 9), ("highTemperatureTrigger", 10), ("dpramCbusFailure", 11)))).setLabel("alarmProfile-Event").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_Event.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Event.setDescription('Alarm event type')
alarmProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("alarmProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
alarmProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("alarmProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
alarmProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 6), Integer32()).setLabel("alarmProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
alarmProfile_Action_AlarmLedMinor = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setLabel("alarmProfile-Action-AlarmLedMinor").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_Action_AlarmLedMinor.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Action_AlarmLedMinor.setDescription('The LED that indicates a minor alarm')
alarmProfile_Action_AlarmLedMajor = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setLabel("alarmProfile-Action-AlarmLedMajor").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_Action_AlarmLedMajor.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Action_AlarmLedMajor.setDescription('The LED that indicates a major alarm')
alarmProfile_Action_AlarmRelayMinor = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setLabel("alarmProfile-Action-AlarmRelayMinor").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_Action_AlarmRelayMinor.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Action_AlarmRelayMinor.setDescription('The relay that is set for a minor alarm')
alarmProfile_Action_AlarmRelayMinorDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 10), Integer32()).setLabel("alarmProfile-Action-AlarmRelayMinorDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_Action_AlarmRelayMinorDuration.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Action_AlarmRelayMinorDuration.setDescription('The duration in seconds for which the minor relay is set')
alarmProfile_Action_AlarmRelayMajor = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setLabel("alarmProfile-Action-AlarmRelayMajor").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_Action_AlarmRelayMajor.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Action_AlarmRelayMajor.setDescription('The relay that is set for a major alarm')
alarmProfile_Action_AlarmRelayMajorDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 12), Integer32()).setLabel("alarmProfile-Action-AlarmRelayMajorDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_Action_AlarmRelayMajorDuration.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Action_AlarmRelayMajorDuration.setDescription('The duration in seconds for which the major relay is set')
alarmProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("alarmProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: alarmProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBALARM-MIB", DisplayString=DisplayString, alarmProfile_Name=alarmProfile_Name, alarmProfile_Action_AlarmRelayMinorDuration=alarmProfile_Action_AlarmRelayMinorDuration, mibalarmProfile=mibalarmProfile, alarmProfile_Action_AlarmLedMajor=alarmProfile_Action_AlarmLedMajor, mibalarmProfileTable=mibalarmProfileTable, alarmProfile_Action_o=alarmProfile_Action_o, alarmProfile_Action_AlarmRelayMajor=alarmProfile_Action_AlarmRelayMajor, alarmProfile_Enabled=alarmProfile_Enabled, alarmProfile_Action_AlarmRelayMinor=alarmProfile_Action_AlarmRelayMinor, alarmProfile_PhysicalAddress_ItemNumber=alarmProfile_PhysicalAddress_ItemNumber, alarmProfile_PhysicalAddress_Slot=alarmProfile_PhysicalAddress_Slot, alarmProfile_Action_AlarmLedMinor=alarmProfile_Action_AlarmLedMinor, alarmProfile_Event=alarmProfile_Event, alarmProfile_Action_AlarmRelayMajorDuration=alarmProfile_Action_AlarmRelayMajorDuration, alarmProfile_PhysicalAddress_Shelf=alarmProfile_PhysicalAddress_Shelf, mibalarmProfileEntry=mibalarmProfileEntry)

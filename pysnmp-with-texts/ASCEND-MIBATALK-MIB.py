#
# PySNMP MIB module ASCEND-MIBATALK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATALK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Gauge32, ObjectIdentity, Bits, Counter32, MibIdentifier, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Gauge32", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibatalkGlobalProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 36))
mibatalkInterfaceProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 35))
mibatalkGlobalProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 36, 1), )
if mibBuilder.loadTexts: mibatalkGlobalProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibatalkGlobalProfileTable.setDescription('A list of mibatalkGlobalProfile profile entries.')
mibatalkGlobalProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1), ).setIndexNames((0, "ASCEND-MIBATALK-MIB", "atalkGlobalProfile-Index-o"))
if mibBuilder.loadTexts: mibatalkGlobalProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibatalkGlobalProfileEntry.setDescription('A mibatalkGlobalProfile entry containing objects that maps to the parameters of mibatalkGlobalProfile profile.')
atalkGlobalProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1, 1), Integer32()).setLabel("atalkGlobalProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkGlobalProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkGlobalProfile_Index_o.setDescription('')
atalkGlobalProfile_AtalkDialinPoolStart = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1, 2), Integer32()).setLabel("atalkGlobalProfile-AtalkDialinPoolStart").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkGlobalProfile_AtalkDialinPoolStart.setStatus('mandatory')
if mibBuilder.loadTexts: atalkGlobalProfile_AtalkDialinPoolStart.setDescription('The Net range start of the dialin pool shared by the wan interfaces.')
atalkGlobalProfile_AtalkDialinPoolEnd = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1, 3), Integer32()).setLabel("atalkGlobalProfile-AtalkDialinPoolEnd").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkGlobalProfile_AtalkDialinPoolEnd.setStatus('mandatory')
if mibBuilder.loadTexts: atalkGlobalProfile_AtalkDialinPoolEnd.setDescription('The Net range end of the dialin pool shared by the wan interfaces.')
atalkGlobalProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atalkGlobalProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkGlobalProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkGlobalProfile_Action_o.setDescription('')
mibatalkInterfaceProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 35, 1), )
if mibBuilder.loadTexts: mibatalkInterfaceProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibatalkInterfaceProfileTable.setDescription('A list of mibatalkInterfaceProfile profile entries.')
mibatalkInterfaceProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1), ).setIndexNames((0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-Shelf-o"), (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-Slot-o"), (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-Item-o"), (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-LogicalItem-o"))
if mibBuilder.loadTexts: mibatalkInterfaceProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibatalkInterfaceProfileEntry.setDescription('A mibatalkInterfaceProfile entry containing objects that maps to the parameters of mibatalkInterfaceProfile profile.')
atalkInterfaceProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 1), Integer32()).setLabel("atalkInterfaceProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkInterfaceProfile_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_Shelf_o.setDescription('')
atalkInterfaceProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 2), Integer32()).setLabel("atalkInterfaceProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkInterfaceProfile_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_Slot_o.setDescription('')
atalkInterfaceProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 3), Integer32()).setLabel("atalkInterfaceProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkInterfaceProfile_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_Item_o.setDescription('')
atalkInterfaceProfile_LogicalItem_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 4), Integer32()).setLabel("atalkInterfaceProfile-LogicalItem-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkInterfaceProfile_LogicalItem_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_LogicalItem_o.setDescription('')
atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("atalkInterfaceProfile-InterfaceAddress-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("atalkInterfaceProfile-InterfaceAddress-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 7), Integer32()).setLabel("atalkInterfaceProfile-InterfaceAddress-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
atalkInterfaceProfile_InterfaceAddress_LogicalItem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 8), Integer32()).setLabel("atalkInterfaceProfile-InterfaceAddress-LogicalItem").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_InterfaceAddress_LogicalItem.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_InterfaceAddress_LogicalItem.setDescription('A number that specifies an addressable logical entity within the context of a physical address.')
atalkInterfaceProfile_AtalkRoutingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atalkInterfaceProfile-AtalkRoutingEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkRoutingEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkRoutingEnabled.setDescription('Allow Appletalk routing and ARA connections.')
atalkInterfaceProfile_HintZone = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 10), DisplayString()).setLabel("atalkInterfaceProfile-HintZone").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_HintZone.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_HintZone.setDescription('The default zone that the MAX will come up in.')
atalkInterfaceProfile_AtalkRouter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("atalkRouterOff", 1), ("atalkRouterSeed", 2), ("atalkRouterNonSeed", 3)))).setLabel("atalkInterfaceProfile-AtalkRouter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkRouter.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkRouter.setDescription('The type of AppleTalk Router to enable.')
atalkInterfaceProfile_AtalkNetStart = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 12), Integer32()).setLabel("atalkInterfaceProfile-AtalkNetStart").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkNetStart.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkNetStart.setDescription('The start of the AppleTalk Net number range.')
atalkInterfaceProfile_AtalkNetEnd = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 13), Integer32()).setLabel("atalkInterfaceProfile-AtalkNetEnd").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkNetEnd.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkNetEnd.setDescription('The end of the AppleTalk Net number range.')
atalkInterfaceProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atalkInterfaceProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_Action_o.setDescription('')
mibatalkInterfaceProfile_AtalkZoneListTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 35, 2), ).setLabel("mibatalkInterfaceProfile-AtalkZoneListTable")
if mibBuilder.loadTexts: mibatalkInterfaceProfile_AtalkZoneListTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibatalkInterfaceProfile_AtalkZoneListTable.setDescription('A list of mibatalkInterfaceProfile__atalk_Zone_List profile entries.')
mibatalkInterfaceProfile_AtalkZoneListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1), ).setLabel("mibatalkInterfaceProfile-AtalkZoneListEntry").setIndexNames((0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-Shelf-o"), (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-Slot-o"), (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-Item-o"), (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-LogicalItem-o"), (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-Index-o"))
if mibBuilder.loadTexts: mibatalkInterfaceProfile_AtalkZoneListEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibatalkInterfaceProfile_AtalkZoneListEntry.setDescription('A mibatalkInterfaceProfile__atalk_Zone_List entry containing objects that maps to the parameters of mibatalkInterfaceProfile__atalk_Zone_List profile.')
atalkInterfaceProfile_AtalkZoneList_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 1), Integer32()).setLabel("atalkInterfaceProfile-AtalkZoneList-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_Shelf_o.setDescription('')
atalkInterfaceProfile_AtalkZoneList_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 2), Integer32()).setLabel("atalkInterfaceProfile-AtalkZoneList-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_Slot_o.setDescription('')
atalkInterfaceProfile_AtalkZoneList_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 3), Integer32()).setLabel("atalkInterfaceProfile-AtalkZoneList-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_Item_o.setDescription('')
atalkInterfaceProfile_AtalkZoneList_LogicalItem_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 4), Integer32()).setLabel("atalkInterfaceProfile-AtalkZoneList-LogicalItem-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_LogicalItem_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_LogicalItem_o.setDescription('')
atalkInterfaceProfile_AtalkZoneList_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 5), Integer32()).setLabel("atalkInterfaceProfile-AtalkZoneList-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList_Index_o.setDescription('')
atalkInterfaceProfile_AtalkZoneList = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 6), DisplayString()).setLabel("atalkInterfaceProfile-AtalkZoneList").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList.setStatus('mandatory')
if mibBuilder.loadTexts: atalkInterfaceProfile_AtalkZoneList.setDescription('The Zone List for an AppleTalk seed router.')
mibBuilder.exportSymbols("ASCEND-MIBATALK-MIB", mibatalkInterfaceProfile_AtalkZoneListEntry=mibatalkInterfaceProfile_AtalkZoneListEntry, mibatalkGlobalProfileEntry=mibatalkGlobalProfileEntry, atalkInterfaceProfile_AtalkZoneList_Item_o=atalkInterfaceProfile_AtalkZoneList_Item_o, atalkInterfaceProfile_AtalkZoneList_Slot_o=atalkInterfaceProfile_AtalkZoneList_Slot_o, atalkGlobalProfile_AtalkDialinPoolStart=atalkGlobalProfile_AtalkDialinPoolStart, atalkGlobalProfile_Action_o=atalkGlobalProfile_Action_o, mibatalkGlobalProfile=mibatalkGlobalProfile, atalkInterfaceProfile_AtalkZoneList=atalkInterfaceProfile_AtalkZoneList, atalkInterfaceProfile_AtalkZoneList_Index_o=atalkInterfaceProfile_AtalkZoneList_Index_o, atalkInterfaceProfile_Item_o=atalkInterfaceProfile_Item_o, atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber=atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber, mibatalkInterfaceProfile=mibatalkInterfaceProfile, atalkInterfaceProfile_AtalkZoneList_Shelf_o=atalkInterfaceProfile_AtalkZoneList_Shelf_o, DisplayString=DisplayString, atalkInterfaceProfile_Action_o=atalkInterfaceProfile_Action_o, atalkInterfaceProfile_Slot_o=atalkInterfaceProfile_Slot_o, mibatalkInterfaceProfileEntry=mibatalkInterfaceProfileEntry, atalkInterfaceProfile_HintZone=atalkInterfaceProfile_HintZone, atalkInterfaceProfile_AtalkRoutingEnabled=atalkInterfaceProfile_AtalkRoutingEnabled, mibatalkGlobalProfileTable=mibatalkGlobalProfileTable, atalkInterfaceProfile_AtalkZoneList_LogicalItem_o=atalkInterfaceProfile_AtalkZoneList_LogicalItem_o, atalkInterfaceProfile_LogicalItem_o=atalkInterfaceProfile_LogicalItem_o, atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf=atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf, atalkGlobalProfile_AtalkDialinPoolEnd=atalkGlobalProfile_AtalkDialinPoolEnd, atalkInterfaceProfile_AtalkNetStart=atalkInterfaceProfile_AtalkNetStart, atalkInterfaceProfile_Shelf_o=atalkInterfaceProfile_Shelf_o, atalkInterfaceProfile_AtalkRouter=atalkInterfaceProfile_AtalkRouter, atalkInterfaceProfile_InterfaceAddress_LogicalItem=atalkInterfaceProfile_InterfaceAddress_LogicalItem, mibatalkInterfaceProfileTable=mibatalkInterfaceProfileTable, mibatalkInterfaceProfile_AtalkZoneListTable=mibatalkInterfaceProfile_AtalkZoneListTable, atalkGlobalProfile_Index_o=atalkGlobalProfile_Index_o, atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot=atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot, atalkInterfaceProfile_AtalkNetEnd=atalkInterfaceProfile_AtalkNetEnd)
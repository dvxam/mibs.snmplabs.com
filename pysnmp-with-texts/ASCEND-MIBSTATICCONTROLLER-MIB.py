#
# PySNMP MIB module ASCEND-MIBSTATICCONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSTATICCONTROLLER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, iso, IpAddress, Counter32, TimeTicks, Unsigned32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "iso", "IpAddress", "Counter32", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibmibProfControllerStatic = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 30))
mibmibProfControllerStaticTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 30, 1), )
if mibBuilder.loadTexts: mibmibProfControllerStaticTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfControllerStaticTable.setDescription('A list of mibmibProfControllerStatic profile entries.')
mibmibProfControllerStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 30, 1, 1), ).setIndexNames((0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-Index-o"))
if mibBuilder.loadTexts: mibmibProfControllerStaticEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfControllerStaticEntry.setDescription('A mibmibProfControllerStatic entry containing objects that maps to the parameters of mibmibProfControllerStatic profile.')
mibProfControllerStatic_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 1, 1, 1), Integer32()).setLabel("mibProfControllerStatic-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfControllerStatic_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_Index_o.setDescription('')
mibProfControllerStatic_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfControllerStatic-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_Action_o.setDescription('')
mibmibProfControllerStatic_AtmParameters_OutgoingShaperTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 30, 2), ).setLabel("mibmibProfControllerStatic-AtmParameters-OutgoingShaperTable")
if mibBuilder.loadTexts: mibmibProfControllerStatic_AtmParameters_OutgoingShaperTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfControllerStatic_AtmParameters_OutgoingShaperTable.setDescription('A list of mibmibProfControllerStatic__atm_parameters__outgoing_shaper profile entries.')
mibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1), ).setLabel("mibmibProfControllerStatic-AtmParameters-OutgoingShaperEntry").setIndexNames((0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-AtmParameters-OutgoingShaper-Index-o"), (0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-AtmParameters-OutgoingShaper-Index1-o"))
if mibBuilder.loadTexts: mibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry.setDescription('A mibmibProfControllerStatic__atm_parameters__outgoing_shaper entry containing objects that maps to the parameters of mibmibProfControllerStatic__atm_parameters__outgoing_shaper profile.')
mibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 1), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingShaper-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o.setDescription('')
mibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 2), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingShaper-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o.setDescription('')
mibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 3), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingShaper-QueueIndex").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex.setDescription('0: this shaper is inactive. Non-0: identifies the queue (of an outgoing trunk port) whose bandwidth with the specified VPI will be shaped by this shaper. Condition: queue must have already been properly configured. Limit: at most 1 shaper per VPI.')
mibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 4), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingShaper-Vpi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi.setDescription('Designate the VPI whose bandwidth to be shaped.')
mibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 5), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingShaper-Bandwidth").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth.setDescription('Bandwidth (in KBits/sec) to shape.')
mibmibProfControllerStatic_AtmParameters_OutgoingQueueTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 30, 3), ).setLabel("mibmibProfControllerStatic-AtmParameters-OutgoingQueueTable")
if mibBuilder.loadTexts: mibmibProfControllerStatic_AtmParameters_OutgoingQueueTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfControllerStatic_AtmParameters_OutgoingQueueTable.setDescription('A list of mibmibProfControllerStatic__atm_parameters__outgoing_queue profile entries.')
mibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1), ).setLabel("mibmibProfControllerStatic-AtmParameters-OutgoingQueueEntry").setIndexNames((0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-AtmParameters-OutgoingQueue-Index-o"), (0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-AtmParameters-OutgoingQueue-Index1-o"))
if mibBuilder.loadTexts: mibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry.setDescription('A mibmibProfControllerStatic__atm_parameters__outgoing_queue entry containing objects that maps to the parameters of mibmibProfControllerStatic__atm_parameters__outgoing_queue profile.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 1), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o.setDescription('')
mibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 2), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o.setDescription('')
mibProfControllerStatic_AtmParameters_OutgoingQueue_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Active.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Active.setDescription('yes: this queue (of outgoing ATM cells) is active.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 4), DisplayString()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Name.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Name.setDescription('For future use. The current design does not use this name attribute but instead references a LIM slot, CM, or trunk port by its physical-address. We may in the future support referencing a LIM slot, CM, or trunk port by its name as well as by its physical-address. This name attribute consists of a null-terminated ASCII string; is read-only; and defaults to the ASCII form of physical-address.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 7), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-Cbr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr.setDescription('yes: this queue supports ATM constant-bit-rate traffic. Condition: if active=yes, at least one (might be more) of cbr, real-time-vbr, non-real-time-vbr, and ubr must also be yes. Limit: at least 1, and at most 2 active queues for each ATM service category.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-RealTimeVbr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr.setDescription('yes: this queue supports ATM real-time-variable-bit-rate traffic. Condition: if active=yes, at least one (might be more) of cbr, real-time-vbr, non-real-time-vbr, and ubr must also be yes. Limit: at least 1, and at most 2 active queues for each ATM service category.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-NonRealTimeVbr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr.setDescription('yes: this queue supports ATM non-real-time-variable-bit-rate traffic. Condition: if active=yes, at least one (might be more) of cbr, real-time-vbr, non-real-time-vbr, and ubr must also be yes. Limit: at least 1, and at most 2 active queues for each ATM service category.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-Ubr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr.setDescription('yes: this queue supports ATM unspecified-bit-rate traffic. Condition: if active=yes, at least one (might be more) of cbr, real-time-vbr, non-real-time-vbr, and ubr must also be yes. Limit: at least 1, and at most 2 active queues for each ATM service category.')
mibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 12), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-HighPriorityWeight").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight.setDescription("Sets the weight of this queue on the high-priority scheduler. This relative weight determines how much of the scheduler's work cycle this queue should receive relative to other queues on the same scheduler. Condition: if active=yes, either high- or low-priority-weight must be non-0. Limit: total weights per scheduler must be <= 128.")
mibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 13), Integer32()).setLabel("mibProfControllerStatic-AtmParameters-OutgoingQueue-LowPriorityWeight").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight.setDescription("Sets the weight of this queue on the low-priority scheduler. This relative weight determines how much of the scheduler's work cycle this queue should receive relative to other queues on the same scheduler. Condition: if active=yes, either high- or low-priority-weight must be non-0. Limit: total weights per scheduler must be <= 128.")
mibBuilder.exportSymbols("ASCEND-MIBSTATICCONTROLLER-MIB", mibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex=mibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex, mibmibProfControllerStatic_AtmParameters_OutgoingQueueTable=mibmibProfControllerStatic_AtmParameters_OutgoingQueueTable, mibProfControllerStatic_Index_o=mibProfControllerStatic_Index_o, DisplayString=DisplayString, mibmibProfControllerStatic=mibmibProfControllerStatic, mibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth=mibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth, mibProfControllerStatic_AtmParameters_OutgoingQueue_Name=mibProfControllerStatic_AtmParameters_OutgoingQueue_Name, mibProfControllerStatic_Action_o=mibProfControllerStatic_Action_o, mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr=mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr, mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf=mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf, mibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry=mibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry, mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr=mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr, mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr=mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr, mibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight=mibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight, mibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry=mibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry, mibmibProfControllerStaticEntry=mibmibProfControllerStaticEntry, mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber=mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber, mibmibProfControllerStatic_AtmParameters_OutgoingShaperTable=mibmibProfControllerStatic_AtmParameters_OutgoingShaperTable, mibmibProfControllerStaticTable=mibmibProfControllerStaticTable, mibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o=mibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o, mibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o=mibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o, mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr=mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr, mibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi=mibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi, mibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o=mibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o, mibProfControllerStatic_AtmParameters_OutgoingQueue_Active=mibProfControllerStatic_AtmParameters_OutgoingQueue_Active, mibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight=mibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight, mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot=mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot, mibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o=mibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o)
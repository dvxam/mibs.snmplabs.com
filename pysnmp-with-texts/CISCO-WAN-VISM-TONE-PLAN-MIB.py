#
# PySNMP MIB module CISCO-WAN-VISM-TONE-PLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-TONE-PLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Counter32, IpAddress, Unsigned32, MibIdentifier, NotificationType, Integer32, TimeTicks, Bits, iso, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "TimeTicks", "Bits", "iso", "ModuleIdentity", "ObjectIdentity")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
vismTonePlanGrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 24))
vismTonePlanGrpMIB.setRevisions(('2003-12-17 00:00', '2003-04-23 00:00', '2002-07-19 00:00', '2001-12-26 00:00', '2001-08-05 00:00', '2001-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vismTonePlanGrpMIB.setRevisionsDescriptions(('1. Remove default value from vismEventCode object. 2. Change default value of vismFreqMaxDelay object from 3 to 10. 3. Change default value of vismMinOnCadence object from 3 to 20. 4. Change default value of vismMaxOffCadence object from 5 to 450. 5. Remove default value from vismFrequency1 object. 6. Remove default value from vismFrequency2 object. 7. Remove default value from vismFreqOnCadence object. 8. Change default value of seqToneMaximumGapDuration object from 10 to 15. 9. Change SYNTAX INTEGER to Integer32 except for enumerated integers in vismConfigToneDetectEntry. 10. Clarify description of object. ', ' Added Object vismConfigToneDetect (Programmable Tone) under vismTonePlan ', 'Give tonePlanIndex a range (1..1000) to be compiled in new SMICNG compiler (ver2.2.11-beta). ', 'Description changes for tonePlanEntryStatus, tonePlanProvisionFlag, vismTonePlanEntry. ', 'Results from MIB external interfaces review. ', 'Initial draft. Created new VISM Tone Plan Group. ',))
if mibBuilder.loadTexts: vismTonePlanGrpMIB.setLastUpdated('200312170000Z')
if mibBuilder.loadTexts: vismTonePlanGrpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: vismTonePlanGrpMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: vismTonePlanGrpMIB.setDescription('The MIB module is defined to configure the programmable Tone Plan feature on VISM. ')
vismTonePlanGrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1))
vismTonePlan = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1))
vismTonePlanControlGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 1))
vismTonePlanTableGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2))
vismConfigToneDetectGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3))
vismSequentialToneDetectGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4))
tonePlanCurrentSize = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tonePlanCurrentSize.setStatus('current')
if mibBuilder.loadTexts: tonePlanCurrentSize.setDescription('This object specifies the number of entries in vismTonePlanTable. ')
vismTonePlanTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1), )
if mibBuilder.loadTexts: vismTonePlanTable.setStatus('current')
if mibBuilder.loadTexts: vismTonePlanTable.setDescription("This table contains configuration information about different Tone Plans. The first 32 entries of the table are 'provisionable' followed by an implementation specific number of 'builtIn' entries. ")
vismTonePlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanIndex"))
if mibBuilder.loadTexts: vismTonePlanEntry.setStatus('current')
if mibBuilder.loadTexts: vismTonePlanEntry.setDescription("An entry in the vismTonePlanTable. Each entry consists of configuration information for a specific Tone Plan. The vismTonePlanTable is of fixed size with a predefined number of entries, where each entry contains usable information or not depending upon the value of the tonePlanEntryStatus MIB object. The configuration is retained after VISM card reboots. tonePlanRegionName, tonePlanVersionNumber, and tonePlanFileName can be modified only if the tonePlanProvisionFlag is 'provisionable' and tonePlanEntryStatus is 'configured' when loading a new tone plan (see MIB object tonePlanEntryStatus below). After the new tone plan is loaded, these three MIB objects may not be modified. To change these objects, the entry in this table must be deleted, and all objects re-added with new corrected values. The rest of the entries of this table, (the 'builtIn' ones) cannot be modified after the table is build at reload time. ")
tonePlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: tonePlanIndex.setStatus('current')
if mibBuilder.loadTexts: tonePlanIndex.setDescription(' Serves as index to this table. However, the maximum entry allowed is specify in tonePlanCurrentSize. ')
tonePlanEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unused", 1), ("configured", 2), ("reloading", 3), ("lostFile", 4))).clone('unused')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tonePlanEntryStatus.setStatus('current')
if mibBuilder.loadTexts: tonePlanEntryStatus.setDescription(" This attribute specifies the status of this entry as to whether this entry (row) contains usable Tone Plan configuration information (object is set to 'configured'), or if it is empty (object is set to 'unused'), or if is temporarily (object is set to 'reloading') or permanently (object is set to 'lostFile') unusable. This tone plan information for this row can be used by a DS-1 line only if this object has a value of 'configured (2)'. To add a configured entry in the vismTonePlanTable table, there must be an existing empty row with its entry status set to 'unused(1)'. Then before this empty row in the vismTonePlanTable table can be changed to 'configured', it must, in one single operation, be given all the usable values necessary to be stored in the tonePlanRegionName, tonePlanVersionNumber and tonePlanFileName MIB objects for this row. In addition, those values for the tonePlanRegionName and tonePlanVersionNumber MIB objects pair must be unique with respect to every other row of the vismTonePlanTable. Then, as this existing empty row is set with all three valid entries for the tonePlanRegionName, tonePlanVersionNumber, and tonePlanFileName MIB objects, the Entry Status MIB object for this row will be finally, internally, set to 'configured(2)'. This final 'configured' status is the direct result of correctly setting these three MIB objects with valid data. In no case will an external manager be able to directly set this MIB object to 'configured(2)' by a SNMP set command, for such a single stand alone command will be rejected. Once a table entry is set to 'configured(2)' with valid tonePlanRegionName, tonePlanVersionNumber, and tonePlanFileName MIB objects for this row, then these MIB objects may not be modified by any subsequent SNMP set command. In the case where a row needs to have these objects changed, this entry must be cleared from the table (paragraph below) and a new entry added by the add process above. Once an entry exists in the vismTonePlanTable table it may be cleared and set to unused by setting this MIB object to 'unused(1)'. But before the entry status of any entry in this table can be set to 'unused(1)', there is a check to make sure there is no vismDsx1TonePlanRegion MIB object and vismDsx1TonePlanVersion MIB object pair in the dsx1VismCnfGrpTable MIB table that may point to or refer to this table entry (row) with its unique tonePlanRegionName and tonePlanVersionNumber. Once the entry status of an entry in this table is set to 'unused(1)', all the other MIB objects for this table row are set to defaults or to NULL. Once an entry is 'configured', if a subsequent card reset occurs the VISM card will attempt to restore all of the configuration information by doing the normal download of the latest MIB database, set all 'configured (2)' MIB objects to 'reloading (3)', and then do an automatic background process to retrieve all of the tone plan files from the server since they were not downloaded by the PXM. If this retrieval of the tone plan files succeeds then this MIB object will be set back to 'configured (2)'. If this file retrieval does not succeed, then this MIB object will be set to 'lostFile (4)'. In no way will an external manager be able to directly set this MIB object to 'reloading (3)' or 'lostFile (4)' by a SNMP set command. ")
tonePlanProvisionFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("builtIn", 1), ("provisionable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tonePlanProvisionFlag.setStatus('current')
if mibBuilder.loadTexts: tonePlanProvisionFlag.setDescription(" This attribute specifies whether this entry contains predefined Tone Plan configuration information from internal firmware code (object is set to 'builtIn') or if it has been configured with tone plan configuration information that has been downloaded from the PXM (object is set to unused). Only entries that are provisionable may have their tonePlanEntryStatus MIB object marked as unused in this table. BuiltIn entries may not be marked as unused. ")
tonePlanRegionName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tonePlanRegionName.setStatus('current')
if mibBuilder.loadTexts: tonePlanRegionName.setDescription(' The region (or country) for which this tone plan is defined. Any other entry in this table may have an identical name, but the combination of tonePlanRegionName and tonePlanVersionNumber must be unique. This field may be from 1 to 64 alphabetic, numeric, or underscore characters long, with no embedded spaces. A NULL entry will consist of a single space character of length one. ')
tonePlanVersionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tonePlanVersionNumber.setStatus('current')
if mibBuilder.loadTexts: tonePlanVersionNumber.setDescription(" This attribute specifies this entry's version number for a tone plan for a region. Multiple tone plans may be defined for each region, but each of these tone plans must have a unique tonePlanRegionName and tonePlanVersionNumber. When a new tone plan is added for a region, it should be added with a newer(larger) version number. Allowed values are in range (1..65535) but a value of zero being set in this object means that this object is a NULL entry. ")
tonePlanFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tonePlanFileName.setStatus('current')
if mibBuilder.loadTexts: tonePlanFileName.setDescription(" This is the name of a valid file stored on the TFTP server which contains the tone definitions. A missing or invalid file name will cause a failure in the configuration of this entry. If this entry points to a build-in tone plan predefined in firmware, then this name will be: 'BUILTIN'. Provisionable file names are not allowed to have the string 'BUILTIN' as their names. This field may be from 1 to 32 alphabetic, numeric, or underscore characters (no embedded spaces) long for a valid entry. A NULL entry will consist of a single space character of length one. ")
vismConfigToneDetectTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1), )
if mibBuilder.loadTexts: vismConfigToneDetectTable.setStatus('current')
if mibBuilder.loadTexts: vismConfigToneDetectTable.setDescription('This table contains the list of user configurable dual frequency tones that can be detected on VISM. The call agent can request the VISM to detect any of the tones defined in this table. Entries to this table can only be added or deleted, not modified. Individual parameters within a row cannot be changed without deleting and re-adding the entry. ')
vismConfigToneDetectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectNum"))
if mibBuilder.loadTexts: vismConfigToneDetectEntry.setStatus('current')
if mibBuilder.loadTexts: vismConfigToneDetectEntry.setDescription('This is the primary entry in the vismConfigToneDetectTable. Each entry references a User configurable dual frequency tones that can be detected on VISM. ')
vismConfigToneDetectNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismConfigToneDetectNum.setStatus('current')
if mibBuilder.loadTexts: vismConfigToneDetectNum.setDescription('This is the index of this table. Currently only tones 1 to 10 are used and call agent can request up to ten tones to be detected on different endpoints at any point in time. ')
vismEventCode = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismEventCode.setStatus('current')
if mibBuilder.loadTexts: vismEventCode.setDescription('This is the secondary index of this table. Call agent can request supervision tone detection indexed by this field. The values of event code are mapped from the subscriber line event codes defined in RFC2833. Currently VISM supports detection of only a handful of supervision tones like Ringing, Busy, Dial-Tone and SIT tones. ')
vismConfigToneDetectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismConfigToneDetectRowStatus.setStatus('current')
if mibBuilder.loadTexts: vismConfigToneDetectRowStatus.setDescription("Controls the creation and deletion of a Config Tone. An entry may be created using the 'createAndGo' option. When the row is successfully created, the vismConfigToneDetectRowStatus would be set to 'active' by the agent. An entry may be deleted by setting the vismConfigToneDetectRowStatus to 'destroy'. ")
vismFreqMaxDeviation = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 125)).clone(30)).setUnits('Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqMaxDeviation.setStatus('current')
if mibBuilder.loadTexts: vismFreqMaxDeviation.setDescription('Specifies the maximum frequency deviation to be used by VISM when detecting a specific dual frequency tone. Please refer the VISM configuration guide for standard values to be used for this field. ')
vismFreqMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setUnits('dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqMaxPower.setStatus('current')
if mibBuilder.loadTexts: vismFreqMaxPower.setDescription('Specifies the maximum frequency power to be used by VISM when detecting a specific dual frequency tone. Please refer the VISM configuration guide for standard values to be used for this field. ')
vismFreqMinPower = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 35)).clone(35)).setUnits('dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqMinPower.setStatus('current')
if mibBuilder.loadTexts: vismFreqMinPower.setDescription('Specifies the minimum frequency power to be used by VISM when detecting a specific dual frequency tone. Please refer the VISM configuration guide for standard values to be used for this field. ')
vismFreqPowerTwist = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(10)).setUnits('dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqPowerTwist.setStatus('current')
if mibBuilder.loadTexts: vismFreqPowerTwist.setDescription('Specifies the maximum frequency power twist permitted between the two frequencies used by VISM when detecting a dual frequency tone. Please refer the VISM configuration guide for standard values to be used for this field. ')
vismFreqMaxDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(10)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqMaxDelay.setStatus('current')
if mibBuilder.loadTexts: vismFreqMaxDelay.setDescription('Specifies the maximum frequency delay to be used by VISM when detecting a dual frequency tone. Please refer the VISM configuration guide for standard values to be used for this field. It is measured in units of 10ms. ')
vismMinOnCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 100)).clone(20)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismMinOnCadence.setStatus('current')
if mibBuilder.loadTexts: vismMinOnCadence.setDescription('Specifies the minimum tone cycle ON time that is necessary for the VISM to detect the dual frequency tone. The vismMinOnCadence has to be less than vismFreqOnCadence value. Please refer the VISM configuration guide for standard values to be used for this field. ')
vismMaxOffCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 5000)).clone(450)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismMaxOffCadence.setStatus('current')
if mibBuilder.loadTexts: vismMaxOffCadence.setDescription('Specifies the maximum tone cycle OFF time that is necessary for the VISM to detect the dual frequency tone. The vismMaxOffCadence should be greater than vismFreqOffCadence value. Please refer the VISM configuration guide for standard values to be used for this field. ')
vismFreqNumOfCadenceMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqNumOfCadenceMatch.setStatus('current')
if mibBuilder.loadTexts: vismFreqNumOfCadenceMatch.setDescription('Specifies the number of pairs of the dual frequency that needs to be detected. Currently ten pairs of frequency can be detected by the DSP. ')
vismFrequency1 = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800))).setUnits('Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFrequency1.setStatus('current')
if mibBuilder.loadTexts: vismFrequency1.setDescription('Specifies the 1st frequency component of the dual frequency to be detected by the VISM. ')
vismFrequency2 = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3800))).setUnits('Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFrequency2.setStatus('current')
if mibBuilder.loadTexts: vismFrequency2.setDescription('Specifies the 2nd frequency component of the dual frequency to be detected by the DSP. A value of 0 means this is a single frequency. The range of 1 to 279 is not a valid range in the DSP. ')
vismFreqOnCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 5000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqOnCadence.setStatus('current')
if mibBuilder.loadTexts: vismFreqOnCadence.setDescription('The On time in each cycle of the dual frequency to be detected by the DSP. The vismFreqOnCadence has to be less than vismMinOnCadence value. It is measured in units of 10ms. ')
vismFreqOffCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 5000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqOffCadence.setStatus('current')
if mibBuilder.loadTexts: vismFreqOffCadence.setDescription('The Off time in each cycle of the dual frequency to be detected by the DSP. The vismFreqOffCadence should be lesser than the vismMaxOffCadence value. It is measured in units of 10ms. ')
seqToneNumOfFrequencies = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneNumOfFrequencies.setStatus('current')
if mibBuilder.loadTexts: seqToneNumOfFrequencies.setDescription(' The number of single frequencies which have to be detected by the sequential tone detector command on VISM. The frequencies should specified below (seqToneFrequency1 to seqToneFrequency10). This number should correspond to the non-zero frequency values seqToneFrequency1 to seqToneFrequency10. ')
seqToneEventID = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(74)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneEventID.setStatus('current')
if mibBuilder.loadTexts: seqToneEventID.setDescription(' The eventID corresponding to the sequential frequency. Currently only supports Event 74 (SIT tone) ')
seqToneDurationOfEachTone = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534)).clone(33)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneDurationOfEachTone.setStatus('current')
if mibBuilder.loadTexts: seqToneDurationOfEachTone.setDescription(' Nominal tone duration of each single tone in counts of 10ms used with sequential tone detector on VISM DSP. ')
seqToneGapBetweenEachTone = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneGapBetweenEachTone.setStatus('current')
if mibBuilder.loadTexts: seqToneGapBetweenEachTone.setDescription(' Nominal silence gap duration between each tone in 10ms used with sequential tone detector on VISM DSP. ')
seqToneDurationDeviation = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneDurationDeviation.setStatus('current')
if mibBuilder.loadTexts: seqToneDurationDeviation.setDescription(' Tone duration deviation allowed in 10ms used with sequential tone detector on VISM DSP. ')
seqToneMaximumGapDuration = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneMaximumGapDuration.setStatus('current')
if mibBuilder.loadTexts: seqToneMaximumGapDuration.setDescription(' Maximum tone duration allowed in 10ms used with sequential tone detector on VISM DSP. ')
seqToneGapDurationDeviation = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneGapDurationDeviation.setStatus('current')
if mibBuilder.loadTexts: seqToneGapDurationDeviation.setDescription(' Tone duration deviation allowed in 10ms used with sequential tone detector on VISM DSP. ')
seqToneFreqDeviation = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFreqDeviation.setStatus('current')
if mibBuilder.loadTexts: seqToneFreqDeviation.setDescription(' Frequency deviation allowed (1 - 1000 Hz) used with sequential tone detector on VISM DSP. ')
seqTonePowerLevelCeiling = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 40)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqTonePowerLevelCeiling.setStatus('current')
if mibBuilder.loadTexts: seqTonePowerLevelCeiling.setDescription(' Maximum ceiling power level of the sequential frequency tone (absolute value in dBm) used with sequential tone detector on VISM DSP. Range from 0 to 40 (0 to -40dB) ')
seqTonePowerLevelFloor = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 40)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqTonePowerLevelFloor.setStatus('current')
if mibBuilder.loadTexts: seqTonePowerLevelFloor.setDescription(' Lowest (floor) power level of the sequential frequency tone (absolute value in dBm) used with sequential tone detector on VISM DSP. Range from 0 to 40 (0 to -40dB) ')
seqToneFrequency1 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(950)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency1.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency1.setDescription(' 1st frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
seqToneFrequency2 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(1400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency2.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency2.setDescription(' 2nd frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
seqToneFrequency3 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(1800)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency3.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency3.setDescription(' 3rd frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
seqToneFrequency4 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency4.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency4.setDescription(' 4th frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
seqToneFrequency5 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency5.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency5.setDescription(' 5th frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
seqToneFrequency6 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency6.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency6.setDescription(' 6th frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
seqToneFrequency7 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency7.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency7.setDescription(' 7th frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
seqToneFrequency8 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency8.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency8.setDescription(' 8th frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
seqToneFrequency9 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency9.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency9.setDescription(' 9th frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
seqToneFrequency10 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency10.setStatus('current')
if mibBuilder.loadTexts: seqToneFrequency10.setDescription(' 10th frequency in the SequentialTone to detect (280 - 3800), used with sequential tone detector on VISM DSP. ')
vismToneNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 2))
vismToneNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 2, 0))
vismTonePlanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 3))
vismTonePlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 1))
vismTonePlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2))
vismTonePlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 1, 1)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismTonePlanControlGroup"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismTonePlanTableGroup"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectTableGroup"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismSequentialToneDetectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismTonePlanMIBCompliance = vismTonePlanMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: vismTonePlanMIBCompliance.setDescription(' The complaince statement for VISM Tone Plan group which implements vismTonePlanGrp MIB.')
vismTonePlanControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 1)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanCurrentSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismTonePlanControlGroup = vismTonePlanControlGroup.setStatus('current')
if mibBuilder.loadTexts: vismTonePlanControlGroup.setDescription('This group contains objects related to control of VISM Tone Plan Table. ')
vismTonePlanTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 2)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanEntryStatus"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanProvisionFlag"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanRegionName"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanVersionNumber"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanFileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismTonePlanTableGroup = vismTonePlanTableGroup.setStatus('current')
if mibBuilder.loadTexts: vismTonePlanTableGroup.setDescription('This group contains objects related to configuration of VISM Tone Plan. ')
vismConfigToneDetectTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 3)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectNum"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismEventCode"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectRowStatus"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMaxDeviation"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMaxPower"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMinPower"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqPowerTwist"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMaxDelay"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismMinOnCadence"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismMaxOffCadence"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqNumOfCadenceMatch"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFrequency1"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFrequency2"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqOnCadence"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqOffCadence"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismConfigToneDetectTableGroup = vismConfigToneDetectTableGroup.setStatus('current')
if mibBuilder.loadTexts: vismConfigToneDetectTableGroup.setDescription('This group contains objects related to configuration of VISM dual frequency detect tones. ')
vismSequentialToneDetectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 4)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneNumOfFrequencies"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneEventID"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneDurationOfEachTone"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneGapBetweenEachTone"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneDurationDeviation"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneMaximumGapDuration"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneGapDurationDeviation"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFreqDeviation"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqTonePowerLevelCeiling"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqTonePowerLevelFloor"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency1"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency2"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency3"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency4"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency5"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency6"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency7"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency8"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency9"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency10"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismSequentialToneDetectGroup = vismSequentialToneDetectGroup.setStatus('current')
if mibBuilder.loadTexts: vismSequentialToneDetectGroup.setDescription('This group contains objects related to configuration of VISM sequential single frequency tone detection. ')
mibBuilder.exportSymbols("CISCO-WAN-VISM-TONE-PLAN-MIB", tonePlanCurrentSize=tonePlanCurrentSize, vismTonePlanGrpMIB=vismTonePlanGrpMIB, seqTonePowerLevelCeiling=seqTonePowerLevelCeiling, seqToneFrequency7=seqToneFrequency7, seqToneFrequency4=seqToneFrequency4, vismTonePlanControlGrp=vismTonePlanControlGrp, vismFrequency2=vismFrequency2, vismFreqOnCadence=vismFreqOnCadence, vismConfigToneDetectRowStatus=vismConfigToneDetectRowStatus, seqToneFrequency9=seqToneFrequency9, vismFreqNumOfCadenceMatch=vismFreqNumOfCadenceMatch, vismEventCode=vismEventCode, seqToneDurationOfEachTone=seqToneDurationOfEachTone, seqToneGapBetweenEachTone=seqToneGapBetweenEachTone, vismFreqMaxDeviation=vismFreqMaxDeviation, seqToneFreqDeviation=seqToneFreqDeviation, seqToneFrequency2=seqToneFrequency2, seqToneFrequency5=seqToneFrequency5, seqToneGapDurationDeviation=seqToneGapDurationDeviation, vismFreqMaxPower=vismFreqMaxPower, vismTonePlanMIBGroups=vismTonePlanMIBGroups, tonePlanRegionName=tonePlanRegionName, tonePlanVersionNumber=tonePlanVersionNumber, vismTonePlanMIBCompliance=vismTonePlanMIBCompliance, vismConfigToneDetectEntry=vismConfigToneDetectEntry, tonePlanEntryStatus=tonePlanEntryStatus, vismTonePlan=vismTonePlan, vismMaxOffCadence=vismMaxOffCadence, tonePlanProvisionFlag=tonePlanProvisionFlag, tonePlanIndex=tonePlanIndex, vismFreqPowerTwist=vismFreqPowerTwist, seqToneFrequency6=seqToneFrequency6, vismTonePlanTable=vismTonePlanTable, vismToneNotifications=vismToneNotifications, vismConfigToneDetectTableGroup=vismConfigToneDetectTableGroup, vismFreqMinPower=vismFreqMinPower, seqToneNumOfFrequencies=seqToneNumOfFrequencies, seqToneFrequency8=seqToneFrequency8, tonePlanFileName=tonePlanFileName, vismConfigToneDetectTable=vismConfigToneDetectTable, PYSNMP_MODULE_ID=vismTonePlanGrpMIB, seqToneFrequency3=seqToneFrequency3, vismConfigToneDetectGrp=vismConfigToneDetectGrp, vismToneNotificationPrefix=vismToneNotificationPrefix, vismConfigToneDetectNum=vismConfigToneDetectNum, vismTonePlanEntry=vismTonePlanEntry, vismTonePlanTableGrp=vismTonePlanTableGrp, vismTonePlanGrpMIBObjects=vismTonePlanGrpMIBObjects, seqToneEventID=seqToneEventID, vismFreqMaxDelay=vismFreqMaxDelay, seqToneDurationDeviation=seqToneDurationDeviation, seqToneMaximumGapDuration=seqToneMaximumGapDuration, seqToneFrequency1=seqToneFrequency1, vismTonePlanMIBCompliances=vismTonePlanMIBCompliances, vismTonePlanTableGroup=vismTonePlanTableGroup, vismMinOnCadence=vismMinOnCadence, vismTonePlanMIBConformance=vismTonePlanMIBConformance, vismFreqOffCadence=vismFreqOffCadence, seqTonePowerLevelFloor=seqTonePowerLevelFloor, seqToneFrequency10=seqToneFrequency10, vismSequentialToneDetectGrp=vismSequentialToneDetectGrp, vismSequentialToneDetectGroup=vismSequentialToneDetectGroup, vismTonePlanControlGroup=vismTonePlanControlGroup, vismFrequency1=vismFrequency1)

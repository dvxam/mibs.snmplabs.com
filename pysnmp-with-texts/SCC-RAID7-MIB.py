#
# PySNMP MIB module SCC-RAID7-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCC-RAID7-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
raid7mib, = mibBuilder.importSymbols("SCC-ENTERPRISE-MIB", "raid7mib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, MibIdentifier, IpAddress, Integer32, NotificationType, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Counter64, Gauge32, TimeTicks, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "MibIdentifier", "IpAddress", "Integer32", "NotificationType", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Counter64", "Gauge32", "TimeTicks", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
raid7Sys = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2, 1, 1))
raid7Memory = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2, 1, 2))
raid7Host = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3))
raid7Drive = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4))
raid7Env = MibIdentifier((1, 3, 6, 1, 4, 1, 1386, 2, 1, 5))
raid7SysVersion = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7SysVersion.setStatus('mandatory')
if mibBuilder.loadTexts: raid7SysVersion.setDescription('Describes the revision level of the running RAID7 Operating System; this is not really an IP address - but the revision is expressed as 4 decimal numbers so the IpAddress type is convenient.')
raid7TotalMem = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7TotalMem.setStatus('mandatory')
if mibBuilder.loadTexts: raid7TotalMem.setDescription('The number of kilobytes of memory present')
raid7GoodMem = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7GoodMem.setStatus('mandatory')
if mibBuilder.loadTexts: raid7GoodMem.setDescription('The number of kilobytes of memory judged good by self-test')
raid7MemAvail = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7MemAvail.setStatus('mandatory')
if mibBuilder.loadTexts: raid7MemAvail.setDescription('The number of kilobytes of memory currently in use.')
raid7CacheHitPercent = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7CacheHitPercent.setStatus('mandatory')
if mibBuilder.loadTexts: raid7CacheHitPercent.setDescription('The system-wide percentage of operations satisfied from the RAID7 system cache. This does not include any operations satisfied from cache in channel adapters, or cache built into the physical drives.')
raid7BlockTable = MibTable((1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 5), )
if mibBuilder.loadTexts: raid7BlockTable.setStatus('mandatory')
if mibBuilder.loadTexts: raid7BlockTable.setDescription('This table shows how the host transfer block sizes have been distributed - it can be used to tune system performance (see the RAID 7 User Guide).')
raid7BlockEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 5, 1), ).setIndexNames((0, "SCC-RAID7-MIB", "raid7BlockSize"))
if mibBuilder.loadTexts: raid7BlockEntry.setStatus('mandatory')
if mibBuilder.loadTexts: raid7BlockEntry.setDescription('Information specific to blocks of a given size.')
raid7BlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7BlockSize.setStatus('mandatory')
if mibBuilder.loadTexts: raid7BlockSize.setDescription('Size of the blocks.')
raid7NumBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 5, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7NumBlocks.setStatus('mandatory')
if mibBuilder.loadTexts: raid7NumBlocks.setDescription('Number of blocks of this size.')
raid7NumHostChannels = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7NumHostChannels.setStatus('mandatory')
if mibBuilder.loadTexts: raid7NumHostChannels.setDescription('The number of functional Host I/O Channels.')
raid7ChannelTable = MibTable((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2), )
if mibBuilder.loadTexts: raid7ChannelTable.setStatus('mandatory')
if mibBuilder.loadTexts: raid7ChannelTable.setDescription('A table describing each of the Host I/O Channels')
raid7ChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1), ).setIndexNames((0, "SCC-RAID7-MIB", "raid7ChannelNumber"))
if mibBuilder.loadTexts: raid7ChannelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: raid7ChannelEntry.setDescription('Information specific to a given Host I/O Channel')
raid7ChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7ChannelNumber.setStatus('mandatory')
if mibBuilder.loadTexts: raid7ChannelNumber.setDescription('The number of this Host I/O Channel')
raid7ChannelTransferRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7ChannelTransferRate.setStatus('mandatory')
if mibBuilder.loadTexts: raid7ChannelTransferRate.setDescription('A measure of the data transfer speed on this channel during recent transfers (does not include the idle time on the channel between transfers in the calculation).')
raid7ChannelTransactionRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7ChannelTransactionRate.setStatus('mandatory')
if mibBuilder.loadTexts: raid7ChannelTransactionRate.setDescription('A measure of the number I/O operations per second on this channel.')
raid7ChannelErrorMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7ChannelErrorMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: raid7ChannelErrorMsgs.setDescription('The number of error messages on this channel; see the RAID7 console and the User Guide.')
raid7ChannelLastKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 11, 14))).clone(namedValues=NamedValues(("noSense", 0), ("recoveredError", 1), ("notReady", 2), ("mediumError", 3), ("hardwareError", 4), ("illegalRequest", 5), ("unitAttention", 6), ("abortedCommand", 11), ("miscompare", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7ChannelLastKey.setStatus('mandatory')
if mibBuilder.loadTexts: raid7ChannelLastKey.setDescription('The most recently reported SCSI Key value')
raid7ChannelLastSense = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 8, 12, 17, 23, 24, 26, 27, 28, 29, 32, 33, 34, 36, 37, 38, 41, 47, 49, 61, 64, 67, 68, 69, 70, 72, 73))).clone(namedValues=NamedValues(("noAddSense", 0), ("noIndexSectSignal", 1), ("noSeekComplete", 2), ("writeFault", 3), ("driveNotReady", 4), ("communicationFailure", 8), ("writeError", 12), ("readError", 17), ("retries", 23), ("retriesAndECC", 24), ("listLengthError", 26), ("syncError", 27), ("defectListNotFound", 28), ("verifyMiscompare", 29), ("invalidCommand", 32), ("invalidBlockAddress", 33), ("illegalFunction", 34), ("invalidFieldCDB", 36), ("invalidLUN", 37), ("invalidField", 38), ("resetCondition", 41), ("initClearQ", 47), ("mediaFormat", 49), ("invalidIdentify", 61), ("diagnosticFailure", 64), ("messageRejectError", 67), ("internalFailure", 68), ("selectFailure", 69), ("parityError", 70), ("initiatorDetectedError", 72), ("illegalMessage", 73)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7ChannelLastSense.setStatus('mandatory')
if mibBuilder.loadTexts: raid7ChannelLastSense.setDescription('The last SCSI Sense reported.')
raid7NumDrives = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7NumDrives.setStatus('mandatory')
if mibBuilder.loadTexts: raid7NumDrives.setDescription('The number of drives installed in the RAID7 system')
raid7NumDataDrives = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7NumDataDrives.setStatus('mandatory')
if mibBuilder.loadTexts: raid7NumDataDrives.setDescription('The number of drives being used as data drives; this may not be equal to the total of the drives in the following objects.')
raid7NumParityDrives = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7NumParityDrives.setStatus('mandatory')
if mibBuilder.loadTexts: raid7NumParityDrives.setDescription('The number of drives being used to store parity information.')
raid7NumStandbyDrives = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7NumStandbyDrives.setStatus('mandatory')
if mibBuilder.loadTexts: raid7NumStandbyDrives.setDescription('The number of drives available for reconstructing data from a failed drive.')
raid7NumFailedDrives = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7NumFailedDrives.setStatus('mandatory')
if mibBuilder.loadTexts: raid7NumFailedDrives.setDescription('The number of drives whos raid7DriveState is either reconstructing or failed.')
raid7DriveTable = MibTable((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6), )
if mibBuilder.loadTexts: raid7DriveTable.setStatus('mandatory')
if mibBuilder.loadTexts: raid7DriveTable.setDescription('A list of drive entries, one for each physical drive; this may be a sparse table.')
raid7DriveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1), ).setIndexNames((0, "SCC-RAID7-MIB", "raid7DriveNumber"))
if mibBuilder.loadTexts: raid7DriveEntry.setStatus('mandatory')
if mibBuilder.loadTexts: raid7DriveEntry.setDescription('Information specific to a single drive.')
raid7DriveNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7DriveNumber.setStatus('mandatory')
if mibBuilder.loadTexts: raid7DriveNumber.setDescription('Drive number of this drive.')
raid7DriveState = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("data", 1), ("parity", 2), ("standby", 3), ("rebuilding", 4), ("reformatting", 5), ("failed", 6), ("dataAndParity", 7), ("unknown", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7DriveState.setStatus('mandatory')
if mibBuilder.loadTexts: raid7DriveState.setDescription('State of this drive.')
raid7DriveActivity = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7DriveActivity.setStatus('mandatory')
if mibBuilder.loadTexts: raid7DriveActivity.setDescription('This is letter indicating the most recent operation reported for the drive. See the RAID7 User Guide for values and thier meanings.')
raid7DriveWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7DriveWrites.setStatus('mandatory')
if mibBuilder.loadTexts: raid7DriveWrites.setDescription('Number of write operations to this drive.')
raid7DriveReads = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7DriveReads.setStatus('mandatory')
if mibBuilder.loadTexts: raid7DriveReads.setDescription('Number of read operations to this drive; does not include operations satisfied from RAID7 system or channel cache, but does include those satisfied from any cache within the drive.')
raid7DriveTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7DriveTimeOuts.setStatus('mandatory')
if mibBuilder.loadTexts: raid7DriveTimeOuts.setDescription('The number of SCSI operations timed out on the drive.')
raid7DriveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7DriveErrors.setStatus('mandatory')
if mibBuilder.loadTexts: raid7DriveErrors.setDescription('Number of errors reported by the drive')
raid7DriveUp = NotificationType((1, 3, 6, 1, 4, 1, 1386, 2, 1) + (0,1)).setObjects(("SCC-RAID7-MIB", "raid7DriveNumber"), ("SCC-RAID7-MIB", "raid7DriveState"))
if mibBuilder.loadTexts: raid7DriveUp.setDescription('This trap is sent whenever the state for a drive changes to data or parity from any other value. An equivalent poll would be to poll raid7NumberDrives and raid7FailedDrives and then read the raid7DriveTable when one of them changes.')
raid7DriveDown = NotificationType((1, 3, 6, 1, 4, 1, 1386, 2, 1) + (0,2)).setObjects(("SCC-RAID7-MIB", "raid7DriveNumber"), ("SCC-RAID7-MIB", "raid7DriveState"))
if mibBuilder.loadTexts: raid7DriveDown.setDescription('This trap is sent whenever the state for a drive changes from data or parity to any other value. An equivalent poll would be to poll raid7NumberDrives and raid7FailedDrives and then read the raid7DriveTable when one of them changes.')
raid7EnvironmentStatus = MibScalar((1, 3, 6, 1, 4, 1, 1386, 2, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("operational", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raid7EnvironmentStatus.setStatus('mandatory')
if mibBuilder.loadTexts: raid7EnvironmentStatus.setDescription("The 'failure' indicates that one or more power supplies or fans in the unit have failed.")
raid7EnvironmentFailure = NotificationType((1, 3, 6, 1, 4, 1, 1386, 2, 1) + (0,3)).setObjects(("SCC-RAID7-MIB", "raid7EnvironmentStatus"))
if mibBuilder.loadTexts: raid7EnvironmentFailure.setDescription('This trap is sent when the value of raid7EnvironmentStatus changes to failure.')
mibBuilder.exportSymbols("SCC-RAID7-MIB", raid7Sys=raid7Sys, raid7ChannelEntry=raid7ChannelEntry, raid7NumFailedDrives=raid7NumFailedDrives, raid7EnvironmentFailure=raid7EnvironmentFailure, raid7DriveNumber=raid7DriveNumber, raid7DriveActivity=raid7DriveActivity, raid7ChannelErrorMsgs=raid7ChannelErrorMsgs, raid7DriveState=raid7DriveState, raid7BlockSize=raid7BlockSize, raid7DriveEntry=raid7DriveEntry, raid7Memory=raid7Memory, raid7DriveErrors=raid7DriveErrors, raid7DriveWrites=raid7DriveWrites, raid7ChannelTable=raid7ChannelTable, raid7NumBlocks=raid7NumBlocks, raid7DriveDown=raid7DriveDown, raid7CacheHitPercent=raid7CacheHitPercent, raid7NumHostChannels=raid7NumHostChannels, raid7BlockEntry=raid7BlockEntry, raid7DriveReads=raid7DriveReads, raid7TotalMem=raid7TotalMem, raid7ChannelNumber=raid7ChannelNumber, raid7Drive=raid7Drive, raid7ChannelTransferRate=raid7ChannelTransferRate, raid7ChannelTransactionRate=raid7ChannelTransactionRate, raid7DriveUp=raid7DriveUp, raid7ChannelLastKey=raid7ChannelLastKey, raid7NumParityDrives=raid7NumParityDrives, raid7NumDataDrives=raid7NumDataDrives, raid7DriveTable=raid7DriveTable, raid7Host=raid7Host, raid7NumDrives=raid7NumDrives, raid7DriveTimeOuts=raid7DriveTimeOuts, raid7EnvironmentStatus=raid7EnvironmentStatus, raid7NumStandbyDrives=raid7NumStandbyDrives, raid7SysVersion=raid7SysVersion, raid7ChannelLastSense=raid7ChannelLastSense, raid7GoodMem=raid7GoodMem, raid7Env=raid7Env, raid7BlockTable=raid7BlockTable, raid7MemAvail=raid7MemAvail)
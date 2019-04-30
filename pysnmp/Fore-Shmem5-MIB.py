#
# PySNMP MIB module Fore-Shmem5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Shmem5-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
EntryStatus, = mibBuilder.importSymbols("Fore-Common-MIB", "EntryStatus")
AAL5CountingMode, shmem = mibBuilder.importSymbols("Fore-Switch-MIB", "AAL5CountingMode", "shmem")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, IpAddress, Counter32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, iso, Gauge32, Bits, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "IpAddress", "Counter32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "iso", "Gauge32", "Bits", "Counter64", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
shmem5Group = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13))
if mibBuilder.loadTexts: shmem5Group.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: shmem5Group.setOrganization('FORE')
netmodShmem5Table = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1), )
if mibBuilder.loadTexts: netmodShmem5Table.setStatus('current')
netmodShmem5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1), ).setIndexNames((0, "Fore-Shmem5-MIB", "nShmem5Index"))
if mibBuilder.loadTexts: netmodShmem5Entry.setStatus('current')
nShmem5Index = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: nShmem5Index.setStatus('current')
nShmem5CellMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5CellMemorySize.setStatus('current')
nShmem5TableMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5TableMemorySize.setStatus('current')
nShmem5SchedulerMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5SchedulerMemorySize.setStatus('current')
nShmem5SharedMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5SharedMemorySize.setStatus('current')
nShmem5DupListUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5DupListUsed.setStatus('current')
nShmem5CurrMcastConns = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5CurrMcastConns.setStatus('current')
nShmem5CurrUcastConns = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5CurrUcastConns.setStatus('current')
nShmem5CellsBuffered = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5CellsBuffered.setStatus('current')
nShmem5DuplicationListSize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5DuplicationListSize.setStatus('current')
nShmem5McastConns = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nShmem5McastConns.setStatus('current')
nShmem5UcastConns = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5UcastConns.setStatus('current')
nShmem5ConfEfciOn = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5ConfEfciOn.setStatus('current')
nShmem5ConfEfciOff = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5ConfEfciOff.setStatus('current')
nShmem5AAL5CountingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 16), AAL5CountingMode().clone('packet-counting')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5AAL5CountingMode.setStatus('current')
nShmem5AAl5CountingModeOverride = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5AAl5CountingModeOverride.setStatus('current')
nShmem5OverbookingHw = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5OverbookingHw.setStatus('current')
bufferClassShmem5Table = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2), )
if mibBuilder.loadTexts: bufferClassShmem5Table.setStatus('current')
bufferClassShmem5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1), ).setIndexNames((0, "Fore-Shmem5-MIB", "bcShmem5Index"), (0, "Fore-Shmem5-MIB", "bcShmem5BufferClassIndex"))
if mibBuilder.loadTexts: bufferClassShmem5Entry.setStatus('current')
bcShmem5Index = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: bcShmem5Index.setStatus('current')
bcShmem5BufferClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: bcShmem5BufferClassIndex.setStatus('current')
bcShmem5Status = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 3), EntryStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bcShmem5Status.setStatus('current')
bcShmem5Name = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bcShmem5Name.setStatus('current')
bcShmem5EpdThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 5), Integer32().clone(90)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bcShmem5EpdThreshold.setStatus('current')
bufferClassAssignShmem5Table = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3), )
if mibBuilder.loadTexts: bufferClassAssignShmem5Table.setStatus('current')
bufferClassAssignShmem5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1), ).setIndexNames((0, "Fore-Shmem5-MIB", "bcaShmem5Index"), (0, "Fore-Shmem5-MIB", "bcaShmem5ServCategory"), (0, "Fore-Shmem5-MIB", "bcaShmem5ServSubCategory"))
if mibBuilder.loadTexts: bufferClassAssignShmem5Entry.setStatus('current')
bcaShmem5Index = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: bcaShmem5Index.setStatus('current')
bcaShmem5ServCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: bcaShmem5ServCategory.setStatus('current')
bcaShmem5ServSubCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: bcaShmem5ServSubCategory.setStatus('current')
bcaShmem5Status = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 4), EntryStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bcaShmem5Status.setStatus('current')
bcaShmem5BuffClass = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bcaShmem5BuffClass.setStatus('current')
ifBufferClassShmem5Table = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4), )
if mibBuilder.loadTexts: ifBufferClassShmem5Table.setStatus('current')
ifBufferClassShmem5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1), ).setIndexNames((0, "Fore-Shmem5-MIB", "ibShmem5Index"), (0, "Fore-Shmem5-MIB", "ibShmem5If"), (0, "Fore-Shmem5-MIB", "ibShmem5Buffer"))
if mibBuilder.loadTexts: ifBufferClassShmem5Entry.setStatus('current')
ibShmem5Index = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: ibShmem5Index.setStatus('current')
ibShmem5If = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: ibShmem5If.setStatus('current')
ibShmem5Buffer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 3), Integer32())
if mibBuilder.loadTexts: ibShmem5Buffer.setStatus('current')
ibShmem5Qsize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibShmem5Qsize.setStatus('current')
ibShmem5CLP01Thresh = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibShmem5CLP01Thresh.setStatus('current')
ibShmem5CLP1Thresh = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibShmem5CLP1Thresh.setStatus('current')
ibShmem5TxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibShmem5TxCells.setStatus('current')
ibShmem5CLP01Loss = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibShmem5CLP01Loss.setStatus('current')
ibShmem5CLP1Loss = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibShmem5CLP1Loss.setStatus('current')
ibShmem5EPDLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibShmem5EPDLoss.setStatus('current')
ibShmem5PPDLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibShmem5PPDLoss.setStatus('current')
ibShmem5OverflowLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibShmem5OverflowLoss.setStatus('current')
ibShmem5CurrentQsize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibShmem5CurrentQsize.setStatus('current')
ibShmem5MaxQsize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibShmem5MaxQsize.setStatus('current')
ibShmem5IfName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibShmem5IfName.setStatus('current')
netmodShmem5CustomBCSTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5), )
if mibBuilder.loadTexts: netmodShmem5CustomBCSTable.setStatus('current')
netmodShmem5CustomBCSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1), ).setIndexNames((0, "Fore-Shmem5-MIB", "nShmem5CustomBCSIndex"), (0, "Fore-Shmem5-MIB", "nShmem5CustomBCSValue"))
if mibBuilder.loadTexts: netmodShmem5CustomBCSEntry.setStatus('current')
nShmem5CustomBCSIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: nShmem5CustomBCSIndex.setStatus('current')
nShmem5CustomBCSValue = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: nShmem5CustomBCSValue.setStatus('current')
nShmem5CustomBCSWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5CustomBCSWeight.setStatus('current')
nShmem5CustomBCSBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5CustomBCSBuffer.setStatus('current')
nShmem5CustomBCSRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5CustomBCSRowStatus.setStatus('current')
netmodShmem5CustomBCSGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 6))
nShmem5CustomBCSState = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nShmem5CustomBCSState.setStatus('current')
mibBuilder.exportSymbols("Fore-Shmem5-MIB", nShmem5ConfEfciOff=nShmem5ConfEfciOff, ibShmem5IfName=ibShmem5IfName, shmem5Group=shmem5Group, nShmem5CustomBCSRowStatus=nShmem5CustomBCSRowStatus, netmodShmem5Table=netmodShmem5Table, nShmem5CustomBCSIndex=nShmem5CustomBCSIndex, nShmem5SchedulerMemorySize=nShmem5SchedulerMemorySize, nShmem5OverbookingHw=nShmem5OverbookingHw, nShmem5CellMemorySize=nShmem5CellMemorySize, netmodShmem5CustomBCSGroup=netmodShmem5CustomBCSGroup, bufferClassAssignShmem5Table=bufferClassAssignShmem5Table, bcShmem5BufferClassIndex=bcShmem5BufferClassIndex, nShmem5CurrUcastConns=nShmem5CurrUcastConns, netmodShmem5Entry=netmodShmem5Entry, netmodShmem5CustomBCSTable=netmodShmem5CustomBCSTable, nShmem5TableMemorySize=nShmem5TableMemorySize, bcaShmem5Index=bcaShmem5Index, bcShmem5Name=bcShmem5Name, bcaShmem5ServCategory=bcaShmem5ServCategory, nShmem5DupListUsed=nShmem5DupListUsed, ibShmem5If=ibShmem5If, ibShmem5CLP01Thresh=ibShmem5CLP01Thresh, ibShmem5EPDLoss=ibShmem5EPDLoss, bufferClassAssignShmem5Entry=bufferClassAssignShmem5Entry, nShmem5ConfEfciOn=nShmem5ConfEfciOn, PYSNMP_MODULE_ID=shmem5Group, netmodShmem5CustomBCSEntry=netmodShmem5CustomBCSEntry, nShmem5CustomBCSBuffer=nShmem5CustomBCSBuffer, nShmem5CustomBCSValue=nShmem5CustomBCSValue, nShmem5Index=nShmem5Index, bcaShmem5ServSubCategory=bcaShmem5ServSubCategory, ibShmem5Buffer=ibShmem5Buffer, bufferClassShmem5Table=bufferClassShmem5Table, bufferClassShmem5Entry=bufferClassShmem5Entry, ibShmem5CLP1Thresh=ibShmem5CLP1Thresh, ibShmem5MaxQsize=ibShmem5MaxQsize, nShmem5CustomBCSState=nShmem5CustomBCSState, nShmem5McastConns=nShmem5McastConns, nShmem5DuplicationListSize=nShmem5DuplicationListSize, ibShmem5TxCells=ibShmem5TxCells, ifBufferClassShmem5Entry=ifBufferClassShmem5Entry, nShmem5CustomBCSWeight=nShmem5CustomBCSWeight, nShmem5CellsBuffered=nShmem5CellsBuffered, ibShmem5CLP01Loss=ibShmem5CLP01Loss, nShmem5SharedMemorySize=nShmem5SharedMemorySize, bcShmem5Index=bcShmem5Index, bcaShmem5BuffClass=bcaShmem5BuffClass, ibShmem5PPDLoss=ibShmem5PPDLoss, bcaShmem5Status=bcaShmem5Status, bcShmem5Status=bcShmem5Status, bcShmem5EpdThreshold=bcShmem5EpdThreshold, ifBufferClassShmem5Table=ifBufferClassShmem5Table, ibShmem5CurrentQsize=ibShmem5CurrentQsize, nShmem5CurrMcastConns=nShmem5CurrMcastConns, nShmem5AAl5CountingModeOverride=nShmem5AAl5CountingModeOverride, nShmem5AAL5CountingMode=nShmem5AAL5CountingMode, ibShmem5Qsize=ibShmem5Qsize, ibShmem5OverflowLoss=ibShmem5OverflowLoss, ibShmem5CLP1Loss=ibShmem5CLP1Loss, ibShmem5Index=ibShmem5Index, nShmem5UcastConns=nShmem5UcastConns)
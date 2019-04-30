#
# PySNMP MIB module HUAWEI-TASK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-TASK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Counter64, Gauge32, NotificationType, ObjectIdentity, Bits, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter64", "Gauge32", "NotificationType", "ObjectIdentity", "Bits", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwTask = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27))
hwTask.setRevisions(('2014-09-25 00:00', '2003-07-31 00:00',))
if mibBuilder.loadTexts: hwTask.setLastUpdated('201409250000Z')
if mibBuilder.loadTexts: hwTask.setOrganization('Huawei Technologies Co.,Ltd.')
class HwTaskStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6, 8, 17, 21, 33, 37, 65, 69, 128, 256, 513, 517))
    namedValues = NamedValues(("normalready", 0), ("block", 1), ("sleep", 2), ("suspend", 4), ("blockAndSuspend", 5), ("sleptAndSuspend", 6), ("running", 8), ("queueblock", 17), ("queueblockAndSuspend", 21), ("semaphoreblock", 33), ("semaphoreblockAandSuspend", 37), ("eventblock", 65), ("eventblockAndSuspend", 69), ("prioblock", 128), ("preemptready", 256), ("writequeueblock", 513), ("writequeueblockAndSuspend", 517))

hwTaskObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1))
hwTaskTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1), )
if mibBuilder.loadTexts: hwTaskTable.setStatus('current')
hwTaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1), ).setIndexNames((0, "HUAWEI-TASK-MIB", "hwTaskIndex"), (0, "HUAWEI-TASK-MIB", "hwTaskID"))
if mibBuilder.loadTexts: hwTaskEntry.setStatus('current')
hwTaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 1), Gauge32())
if mibBuilder.loadTexts: hwTaskIndex.setStatus('current')
hwTaskID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 2), Gauge32())
if mibBuilder.loadTexts: hwTaskID.setStatus('current')
hwTaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTaskName.setStatus('current')
hwTaskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 4), HwTaskStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTaskStatus.setStatus('current')
hwTaskCpuUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTaskCpuUsage.setStatus('current')
hwTaskuSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 6), Gauge32()).setUnits('millseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTaskuSecs.setStatus('current')
hwKeyTaskTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2), )
if mibBuilder.loadTexts: hwKeyTaskTable.setStatus('current')
hwKeyTaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1), ).setIndexNames((0, "HUAWEI-TASK-MIB", "hwKeyTaskIndex"), (0, "HUAWEI-TASK-MIB", "hwKeyTaskID"))
if mibBuilder.loadTexts: hwKeyTaskEntry.setStatus('current')
hwKeyTaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hwKeyTaskIndex.setStatus('current')
hwKeyTaskID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: hwKeyTaskID.setStatus('current')
hwKeyTaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwKeyTaskName.setStatus('current')
hwKeyTaskCpuUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwKeyTaskCpuUsage.setStatus('current')
hwTaskNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 2))
hwTaskConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3))
hwTaskCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 1))
hwTaskCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 1, 1)).setObjects(("HUAWEI-TASK-MIB", "hwTaskGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTaskCompliance = hwTaskCompliance.setStatus('current')
hwTaskGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 2))
hwTaskGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 2, 1)).setObjects(("HUAWEI-TASK-MIB", "hwTaskName"), ("HUAWEI-TASK-MIB", "hwTaskStatus"), ("HUAWEI-TASK-MIB", "hwTaskCpuUsage"), ("HUAWEI-TASK-MIB", "hwTaskuSecs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTaskGroup = hwTaskGroup.setStatus('current')
hwKeyTaskGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 2, 2)).setObjects(("HUAWEI-TASK-MIB", "hwKeyTaskName"), ("HUAWEI-TASK-MIB", "hwKeyTaskCpuUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwKeyTaskGroup = hwKeyTaskGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-TASK-MIB", hwKeyTaskName=hwKeyTaskName, PYSNMP_MODULE_ID=hwTask, hwKeyTaskCpuUsage=hwKeyTaskCpuUsage, hwTaskGroup=hwTaskGroup, hwTaskCompliances=hwTaskCompliances, hwTaskName=hwTaskName, hwKeyTaskIndex=hwKeyTaskIndex, hwTask=hwTask, hwKeyTaskTable=hwKeyTaskTable, hwKeyTaskEntry=hwKeyTaskEntry, hwKeyTaskID=hwKeyTaskID, hwTaskID=hwTaskID, hwTaskStatus=hwTaskStatus, hwTaskuSecs=hwTaskuSecs, hwTaskCpuUsage=hwTaskCpuUsage, hwTaskIndex=hwTaskIndex, hwTaskGroups=hwTaskGroups, hwTaskConformance=hwTaskConformance, hwTaskObjects=hwTaskObjects, hwTaskTable=hwTaskTable, hwTaskEntry=hwTaskEntry, hwTaskNotifications=hwTaskNotifications, hwKeyTaskGroup=hwKeyTaskGroup, hwTaskCompliance=hwTaskCompliance, HwTaskStatusType=HwTaskStatusType)

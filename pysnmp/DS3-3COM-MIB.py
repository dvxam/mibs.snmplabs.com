#
# PySNMP MIB module DS3-3COM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DS3-3COM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:39:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, TimeTicks, Counter64, Unsigned32, enterprises, ModuleIdentity, Counter32, MibIdentifier, ObjectIdentity, NotificationType, experimental = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "ModuleIdentity", "Counter32", "MibIdentifier", "ObjectIdentity", "NotificationType", "experimental")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usr = MibIdentifier((1, 3, 6, 1, 4, 1, 429))
nas = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1))
ds3 = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 44))
ds3Cfg = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 44, 1))
ds3CfgTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1), )
if mibBuilder.loadTexts: ds3CfgTable.setStatus('mandatory')
ds3CfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1, 1), ).setIndexNames((0, "DS3-3COM-MIB", "ds3CfgIndex"))
if mibBuilder.loadTexts: ds3CfgEntry.setStatus('mandatory')
ds3CfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3CfgIndex.setStatus('mandatory')
ds3CfgXmitLineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("twoHundredTwentyFive", 1), ("fourHundredFifty", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3CfgXmitLineBuildOut.setStatus('mandatory')
ds3CfgMonitorPortSource = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(29, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))).clone(namedValues=NamedValues(("spanBITS", 29), ("spanLine1", 1), ("spanLine2", 2), ("spanLine3", 3), ("spanLine4", 4), ("spanLine5", 5), ("spanLine6", 6), ("spanLine7", 7), ("spanLine8", 8), ("spanLine9", 9), ("spanLine10", 10), ("spanLine11", 11), ("spanLine12", 12), ("spanLine13", 13), ("spanLine14", 14), ("spanLine15", 15), ("spanLine16", 16), ("spanLine17", 17), ("spanLine18", 18), ("spanLine19", 19), ("spanLine20", 20), ("spanLine21", 21), ("spanLine22", 22), ("spanLine23", 23), ("spanLine24", 24), ("spanLine25", 25), ("spanLine26", 26), ("spanLine27", 27), ("spanLine28", 28)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3CfgMonitorPortSource.setStatus('mandatory')
ds3Current = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 44, 2))
ds3CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1), )
if mibBuilder.loadTexts: ds3CurrentTable.setStatus('mandatory')
ds3CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1), ).setIndexNames((0, "DS3-3COM-MIB", "ds3CurrentIndex"))
if mibBuilder.loadTexts: ds3CurrentEntry.setStatus('mandatory')
ds3CurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentIndex.setStatus('mandatory')
ds3CurrentFCPs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentFCPs.setStatus('mandatory')
ds3CurrentFCCPs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentFCCPs.setStatus('mandatory')
ds3CurrentSESLs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentSESLs.setStatus('mandatory')
ds3CurrentUASCPs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentUASCPs.setStatus('mandatory')
ds3Interval = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 44, 3))
ds3IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1), )
if mibBuilder.loadTexts: ds3IntervalTable.setStatus('mandatory')
ds3IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1), ).setIndexNames((0, "DS3-3COM-MIB", "ds3IntervalIndex"), (0, "DS3-3COM-MIB", "ds3IntervalNumber"))
if mibBuilder.loadTexts: ds3IntervalEntry.setStatus('mandatory')
ds3IntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalIndex.setStatus('mandatory')
ds3IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalNumber.setStatus('mandatory')
ds3IntervalSESLs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalSESLs.setStatus('mandatory')
ds3IntervalCVCPs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalCVCPs.setStatus('mandatory')
ds3IntervalUASCPs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalUASCPs.setStatus('mandatory')
ds3Total = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 44, 4))
ds3TotalTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1), )
if mibBuilder.loadTexts: ds3TotalTable.setStatus('mandatory')
ds3TotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1), ).setIndexNames((0, "DS3-3COM-MIB", "ds3TotalIndex"))
if mibBuilder.loadTexts: ds3TotalEntry.setStatus('mandatory')
ds3TotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalIndex.setStatus('mandatory')
ds3TotalSESLs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalSESLs.setStatus('mandatory')
ds3TotalCVCPs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalCVCPs.setStatus('mandatory')
ds3TotalUASCPs = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalUASCPs.setStatus('mandatory')
ds3TrapEnable = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 44, 5))
ds3TrapEnableTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 44, 5, 1), )
if mibBuilder.loadTexts: ds3TrapEnableTable.setStatus('mandatory')
ds3TrapEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 44, 5, 1, 1), ).setIndexNames((0, "DS3-3COM-MIB", "ds3TrapEnableIndex"))
if mibBuilder.loadTexts: ds3TrapEnableEntry.setStatus('mandatory')
ds3TrapEnableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TrapEnableIndex.setStatus('mandatory')
ds3LineStatusChangeTE = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3LineStatusChangeTE.setStatus('mandatory')
ds3TrapObj = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 44, 6))
ds3TrapObjTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 44, 6, 1), )
if mibBuilder.loadTexts: ds3TrapObjTable.setStatus('mandatory')
ds3TrapObjEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 44, 6, 1, 1), ).setIndexNames((0, "DS3-3COM-MIB", "ds3TrapObjIndex"))
if mibBuilder.loadTexts: ds3TrapObjEntry.setStatus('mandatory')
ds3TrapObjIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TrapObjIndex.setStatus('mandatory')
ds3StatusObjString = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 44, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50)))
if mibBuilder.loadTexts: ds3StatusObjString.setStatus('mandatory')
mibBuilder.exportSymbols("DS3-3COM-MIB", ds3IntervalTable=ds3IntervalTable, ds3CfgEntry=ds3CfgEntry, ds3IntervalIndex=ds3IntervalIndex, ds3LineStatusChangeTE=ds3LineStatusChangeTE, ds3TrapObj=ds3TrapObj, ds3TotalCVCPs=ds3TotalCVCPs, ds3CurrentEntry=ds3CurrentEntry, ds3CurrentTable=ds3CurrentTable, ds3TotalUASCPs=ds3TotalUASCPs, ds3IntervalUASCPs=ds3IntervalUASCPs, ds3CurrentIndex=ds3CurrentIndex, ds3TrapEnable=ds3TrapEnable, ds3IntervalEntry=ds3IntervalEntry, ds3CurrentUASCPs=ds3CurrentUASCPs, ds3TotalIndex=ds3TotalIndex, ds3TotalEntry=ds3TotalEntry, ds3CurrentSESLs=ds3CurrentSESLs, usr=usr, ds3TrapObjIndex=ds3TrapObjIndex, ds3TotalSESLs=ds3TotalSESLs, ds3TrapObjTable=ds3TrapObjTable, ds3=ds3, ds3CfgIndex=ds3CfgIndex, ds3IntervalNumber=ds3IntervalNumber, ds3StatusObjString=ds3StatusObjString, ds3CfgMonitorPortSource=ds3CfgMonitorPortSource, nas=nas, ds3CurrentFCPs=ds3CurrentFCPs, ds3TrapObjEntry=ds3TrapObjEntry, ds3Cfg=ds3Cfg, ds3IntervalSESLs=ds3IntervalSESLs, ds3CurrentFCCPs=ds3CurrentFCCPs, ds3IntervalCVCPs=ds3IntervalCVCPs, ds3TrapEnableTable=ds3TrapEnableTable, ds3CfgXmitLineBuildOut=ds3CfgXmitLineBuildOut, ds3Current=ds3Current, ds3TrapEnableEntry=ds3TrapEnableEntry, ds3TotalTable=ds3TotalTable, ds3TrapEnableIndex=ds3TrapEnableIndex, ds3CfgTable=ds3CfgTable, ds3Total=ds3Total, ds3Interval=ds3Interval)

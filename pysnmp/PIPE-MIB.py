#
# PySNMP MIB module PIPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PIPE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
neStatistics, = mibBuilder.importSymbols("NE-STAT-MIB", "neStatistics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, ModuleIdentity, Counter32, Unsigned32, IpAddress, TimeTicks, Gauge32, NotificationType, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress", "TimeTicks", "Gauge32", "NotificationType", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pipeStatMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2603, 1, 2))
pipeStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1))
pipeStatTable = MibTable((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1), )
if mibBuilder.loadTexts: pipeStatTable.setStatus('mandatory')
pipeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1), ).setIndexNames((0, "PIPE-MIB", "pipePosition"), (0, "PIPE-MIB", "pipeInstancePosition"))
if mibBuilder.loadTexts: pipeEntry.setStatus('mandatory')
pipePosition = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipePosition.setStatus('mandatory')
pipeInstancePosition = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeInstancePosition.setStatus('mandatory')
pipeName = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeName.setStatus('mandatory')
pipeByteCountIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeByteCountIn.setStatus('mandatory')
pipeByteCountOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeByteCountOut.setStatus('mandatory')
pipeByteCountTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeByteCountTotal.setStatus('mandatory')
pipeLiveConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeLiveConnections.setStatus('mandatory')
pipeNewConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeNewConnections.setStatus('mandatory')
pipePacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipePacketsIn.setStatus('mandatory')
pipePacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipePacketsOut.setStatus('mandatory')
pipePacketsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipePacketsTotal.setStatus('mandatory')
mibBuilder.exportSymbols("PIPE-MIB", pipeByteCountIn=pipeByteCountIn, pipeInstancePosition=pipeInstancePosition, pipeByteCountTotal=pipeByteCountTotal, pipeStatTable=pipeStatTable, pipePacketsTotal=pipePacketsTotal, pipeStatMIB=pipeStatMIB, pipeEntry=pipeEntry, pipeStat=pipeStat, pipePacketsOut=pipePacketsOut, pipeByteCountOut=pipeByteCountOut, pipeNewConnections=pipeNewConnections, pipePosition=pipePosition, pipeName=pipeName, pipePacketsIn=pipePacketsIn, pipeLiveConnections=pipeLiveConnections)

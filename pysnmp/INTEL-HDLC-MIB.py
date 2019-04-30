#
# PySNMP MIB module INTEL-HDLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-HDLC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:43:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, Unsigned32, MibIdentifier, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Gauge32, IpAddress, TimeTicks, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Unsigned32", "MibIdentifier", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Gauge32", "IpAddress", "TimeTicks", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hdlc = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 30))
hdlcMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 30, 1))
hdlcMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1), )
if mibBuilder.loadTexts: hdlcMonitorTable.setStatus('mandatory')
hdlcMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1), ).setIndexNames((0, "INTEL-HDLC-MIB", "hdlcMonitorIndex"))
if mibBuilder.loadTexts: hdlcMonitorEntry.setStatus('mandatory')
hdlcMonitorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorIndex.setStatus('mandatory')
hdlcMonitorReceiverChecksumErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorReceiverChecksumErrors.setStatus('mandatory')
hdlcMonitorReceiverGiants = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorReceiverGiants.setStatus('mandatory')
hdlcMonitorReceiverDwarves = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorReceiverDwarves.setStatus('mandatory')
hdlcMonitorReceiverAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorReceiverAborts.setStatus('mandatory')
hdlcMonitorReceiverOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorReceiverOverruns.setStatus('mandatory')
hdlcMonitorReceiverMisalignments = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorReceiverMisalignments.setStatus('mandatory')
hdlcMonitorTransmitterUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorTransmitterUnderruns.setStatus('mandatory')
hdlcMonitorReceiverAsyncParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorReceiverAsyncParityErrors.setStatus('mandatory')
hdlcMonitorReceiverAsyncFramingErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorReceiverAsyncFramingErrors.setStatus('mandatory')
hdlcMonitorReceiverAsyncBreaks = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 30, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdlcMonitorReceiverAsyncBreaks.setStatus('mandatory')
mibBuilder.exportSymbols("INTEL-HDLC-MIB", hdlcMonitorEntry=hdlcMonitorEntry, hdlcMonitorTransmitterUnderruns=hdlcMonitorTransmitterUnderruns, hdlcMonitorReceiverAsyncBreaks=hdlcMonitorReceiverAsyncBreaks, hdlcMonitorReceiverAsyncFramingErrors=hdlcMonitorReceiverAsyncFramingErrors, hdlc=hdlc, hdlcMonitorTable=hdlcMonitorTable, hdlcMonitorReceiverChecksumErrors=hdlcMonitorReceiverChecksumErrors, hdlcMonitorReceiverOverruns=hdlcMonitorReceiverOverruns, hdlcMonitorIndex=hdlcMonitorIndex, hdlcMonitor=hdlcMonitor, hdlcMonitorReceiverDwarves=hdlcMonitorReceiverDwarves, hdlcMonitorReceiverAsyncParityErrors=hdlcMonitorReceiverAsyncParityErrors, hdlcMonitorReceiverMisalignments=hdlcMonitorReceiverMisalignments, hdlcMonitorReceiverGiants=hdlcMonitorReceiverGiants, hdlcMonitorReceiverAborts=hdlcMonitorReceiverAborts)

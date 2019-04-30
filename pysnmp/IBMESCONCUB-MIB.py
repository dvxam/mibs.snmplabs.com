#
# PySNMP MIB module IBMESCONCUB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBMESCONCUB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:39:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, Unsigned32, Counter32, Counter64, IpAddress, iso, Gauge32, enterprises, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Unsigned32", "Counter32", "Counter64", "IpAddress", "iso", "Gauge32", "enterprises", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "TimeTicks")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
ibmIROCescon = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14))
esconPortData = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1))
esconLinkData = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2))
esconStationData = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3))
esconConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 4))
esconPortTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1), )
if mibBuilder.loadTexts: esconPortTable.setStatus('mandatory')
esconPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: esconPortEntry.setStatus('mandatory')
esconPortInFiberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inLoff", 1), ("inOls", 2), ("inIdle", 3), ("inUnknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconPortInFiberStatus.setStatus('mandatory')
esconPortOutFiberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("outDisableReq", 1), ("outDisableForced", 2), ("outLoffForced", 3), ("outOls", 4), ("outOlsForced", 5), ("outEnable", 6), ("outError", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconPortOutFiberStatus.setStatus('mandatory')
esconLinkTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1), )
if mibBuilder.loadTexts: esconLinkTable.setStatus('mandatory')
esconLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "IBMESCONCUB-MIB", "esconLinkHostLinkAddress"), (0, "IBMESCONCUB-MIB", "esconLinkControlUnitAddress"), (0, "IBMESCONCUB-MIB", "esconLinkPartitionNumber"))
if mibBuilder.loadTexts: esconLinkEntry.setStatus('mandatory')
esconLinkHostLinkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconLinkHostLinkAddress.setStatus('mandatory')
esconLinkControlUnitAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconLinkControlUnitAddress.setStatus('mandatory')
esconLinkPartitionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconLinkPartitionNumber.setStatus('mandatory')
esconLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hlpNotEstab", 1), ("hlpEstab", 2), ("hlpError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconLinkStatus.setStatus('mandatory')
esconStationTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1), )
if mibBuilder.loadTexts: esconStationTable.setStatus('mandatory')
esconStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "IBMESCONCUB-MIB", "esconStationHostLinkAddress"), (0, "IBMESCONCUB-MIB", "esconStationControlUnitAddress"), (0, "IBMESCONCUB-MIB", "esconStationPartitionNumber"), (0, "IBMESCONCUB-MIB", "esconStationDeviceAddress"))
if mibBuilder.loadTexts: esconStationEntry.setStatus('mandatory')
esconStationHostLinkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconStationHostLinkAddress.setStatus('mandatory')
esconStationControlUnitAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconStationControlUnitAddress.setStatus('mandatory')
esconStationPartitionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconStationPartitionNumber.setStatus('mandatory')
esconStationDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconStationDeviceAddress.setStatus('mandatory')
esconStationState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("idle", 1), ("cpDefined", 2), ("cpReset", 3), ("cpActive", 4), ("cpDelete", 5), ("cpAbend", 6), ("cldpWait", 7), ("cldpDefinedl", 8), ("cldpError", 9), ("cldpLoad", 10), ("cldpDump", 11), ("deletePending", 12), ("deleted", 13), ("cpXidExpected", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationState.setStatus('mandatory')
esconStationAttentionDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 420))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esconStationAttentionDelay.setStatus('mandatory')
esconStationAttentionTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 840))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esconStationAttentionTimeOut.setStatus('mandatory')
esconStationMaxBfru = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationMaxBfru.setStatus('mandatory')
esconStationUnitSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationUnitSize.setStatus('mandatory')
esconStationMaxMsgSizeReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esconStationMaxMsgSizeReceived.setStatus('mandatory')
esconStationMaxMsgSizeSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esconStationMaxMsgSizeSent.setStatus('mandatory')
esconStationDataPacketsOkReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationDataPacketsOkReceived.setStatus('mandatory')
esconStationDataPacketsKoReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationDataPacketsKoReceived.setStatus('mandatory')
esconStationDataPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationDataPacketsSent.setStatus('mandatory')
esconStationTotalFramesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationTotalFramesSent.setStatus('mandatory')
esconStationDataPacketsRetransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationDataPacketsRetransmitted.setStatus('mandatory')
esconStationPositiveAckDataPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationPositiveAckDataPackets.setStatus('mandatory')
esconStationSecondChanceAttentions = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationSecondChanceAttentions.setStatus('mandatory')
esconStationCommandsRetried = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationCommandsRetried.setStatus('mandatory')
mibBuilder.exportSymbols("IBMESCONCUB-MIB", esconLinkControlUnitAddress=esconLinkControlUnitAddress, esconStationTotalFramesSent=esconStationTotalFramesSent, esconLinkStatus=esconLinkStatus, esconLinkEntry=esconLinkEntry, esconStationCommandsRetried=esconStationCommandsRetried, esconLinkData=esconLinkData, esconPortData=esconPortData, esconStationMaxMsgSizeSent=esconStationMaxMsgSizeSent, esconStationPartitionNumber=esconStationPartitionNumber, esconStationTable=esconStationTable, esconStationHostLinkAddress=esconStationHostLinkAddress, esconStationControlUnitAddress=esconStationControlUnitAddress, esconStationAttentionTimeOut=esconStationAttentionTimeOut, esconStationState=esconStationState, esconPortInFiberStatus=esconPortInFiberStatus, esconStationAttentionDelay=esconStationAttentionDelay, esconStationUnitSize=esconStationUnitSize, esconStationSecondChanceAttentions=esconStationSecondChanceAttentions, esconStationDataPacketsKoReceived=esconStationDataPacketsKoReceived, esconStationDataPacketsSent=esconStationDataPacketsSent, esconLinkHostLinkAddress=esconLinkHostLinkAddress, esconPortOutFiberStatus=esconPortOutFiberStatus, esconStationData=esconStationData, esconStationDeviceAddress=esconStationDeviceAddress, esconStationEntry=esconStationEntry, esconStationPositiveAckDataPackets=esconStationPositiveAckDataPackets, esconLinkTable=esconLinkTable, esconStationMaxMsgSizeReceived=esconStationMaxMsgSizeReceived, esconPortEntry=esconPortEntry, ibmIROCescon=ibmIROCescon, esconStationDataPacketsRetransmitted=esconStationDataPacketsRetransmitted, esconPortTable=esconPortTable, esconLinkPartitionNumber=esconLinkPartitionNumber, esconStationDataPacketsOkReceived=esconStationDataPacketsOkReceived, esconStationMaxBfru=esconStationMaxBfru, esconConformance=esconConformance)

#
# PySNMP MIB module BIANCA-BRICK-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-PING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
DisplayString, = mibBuilder.importSymbols("RFC1158-MIB", "DisplayString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, IpAddress, NotificationType, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Gauge32, iso, Integer32, Bits, TimeTicks, enterprises, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "NotificationType", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Gauge32", "iso", "Integer32", "Bits", "TimeTicks", "enterprises", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
biboip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5))
biboping = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5, 27))
biboPingTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1), )
if mibBuilder.loadTexts: biboPingTable.setStatus('mandatory')
biboPingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-PING-MIB", "biboPingIndex"))
if mibBuilder.loadTexts: biboPingEntry.setStatus('mandatory')
biboPingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboPingIndex.setStatus('mandatory')
biboPingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notinservice", 2), ("notready", 3), ("createandgo", 4), ("createandwait", 5), ("delete", 6))).clone('createandwait')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboPingStatus.setStatus('mandatory')
biboPingCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboPingCompleted.setStatus('mandatory')
biboPingSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboPingSourceAddress.setStatus('mandatory')
biboPingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboPingAddress.setStatus('mandatory')
biboPingPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboPingPacketCount.setStatus('mandatory')
biboPingPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8, 4096)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboPingPacketSize.setStatus('mandatory')
biboPingPacketTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboPingPacketTimeout.setStatus('mandatory')
biboPingReceivedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboPingReceivedPackets.setStatus('mandatory')
biboPingMinRoundTrip = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboPingMinRoundTrip.setStatus('mandatory')
biboPingMaxRoundTrip = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboPingMaxRoundTrip.setStatus('mandatory')
biboPingAvgRoundTrip = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboPingAvgRoundTrip.setStatus('mandatory')
biboPingTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboPingTTL.setStatus('mandatory')
biboPingTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboPingTOS.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-PING-MIB", biboPingPacketCount=biboPingPacketCount, bintec=bintec, biboPingPacketSize=biboPingPacketSize, biboPingTTL=biboPingTTL, biboPingStatus=biboPingStatus, biboPingTOS=biboPingTOS, biboPingEntry=biboPingEntry, biboPingPacketTimeout=biboPingPacketTimeout, biboPingCompleted=biboPingCompleted, biboPingAvgRoundTrip=biboPingAvgRoundTrip, biboPingTable=biboPingTable, biboPingMinRoundTrip=biboPingMinRoundTrip, biboPingAddress=biboPingAddress, biboPingReceivedPackets=biboPingReceivedPackets, biboPingSourceAddress=biboPingSourceAddress, biboPingMaxRoundTrip=biboPingMaxRoundTrip, biboping=biboping, biboPingIndex=biboPingIndex, bibo=bibo, biboip=biboip)

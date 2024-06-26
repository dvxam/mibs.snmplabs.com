#
# PySNMP MIB module XYPLEX-IEEE-HUB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYPLEX-IEEE-HUB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:40:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, IpAddress, Bits, Counter64, Gauge32, ModuleIdentity, NotificationType, iso, TimeTicks, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "IpAddress", "Bits", "Counter64", "Gauge32", "ModuleIdentity", "NotificationType", "iso", "TimeTicks", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xyplex = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
ieeeHub = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001))
hmBasicCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1))
hmSelfTestCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 2))
hmPerfMonCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 3))
hmAddrTrackCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 4))
hmBadBitClockCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 5))
hmBasicHubTable = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1))
hmBasicHubEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1))
hubID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubID.setStatus('mandatory')
hubGroupCapacity = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubGroupCapacity.setStatus('mandatory')
hubGroupMap = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubGroupMap.setStatus('mandatory')
hmBasicGroupTable = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2))
hmBasicGroupEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1))
groupHubID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupHubID.setStatus('mandatory')
groupID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupID.setStatus('mandatory')
groupNumberOfPorts = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupNumberOfPorts.setStatus('mandatory')
hmBasicPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3), )
if mibBuilder.loadTexts: hmBasicPortTable.setStatus('mandatory')
hmBasicPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1), ).setIndexNames((0, "XYPLEX-IEEE-HUB-MIB", "portHubBasicID"))
if mibBuilder.loadTexts: hmBasicPortEntry.setStatus('mandatory')
portHubBasicID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portHubBasicID.setStatus('mandatory')
portGroupBasicID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portGroupBasicID.setStatus('mandatory')
portBasicID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portBasicID.setStatus('mandatory')
portType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("repeater", 2), ("tenBASE-FAsync", 3), ("tenBASE-FSynch", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portType.setStatus('mandatory')
portAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portAdminState.setStatus('mandatory')
portAutoPartitionState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("notAutoPartitioned", 2), ("autoPartitioned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portAutoPartitionState.setStatus('mandatory')
hmSelfTestHubTable = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1))
hmSelfTestHubEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1))
hubSelfTestID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubSelfTestID.setStatus('mandatory')
hubResetTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubResetTimeStamp.setStatus('mandatory')
hubHealthState = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubHealthState.setStatus('mandatory')
hubHealthText = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubHealthText.setStatus('mandatory')
hubHealthData = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubHealthData.setStatus('mandatory')
hubSystemResetting = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notResetting", 1), ("resetting", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hubSystemResetting.setStatus('mandatory')
hubResetting = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notResetting", 1), ("resetting", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hubResetting.setStatus('mandatory')
hubExecutingSelfTest = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSelfTesting", 1), ("selfTesting", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hubExecutingSelfTest.setStatus('mandatory')
hmPerfMonRelayTable = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1))
hmPerfMonRelayEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1))
relayHubPerfID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: relayHubPerfID.setStatus('mandatory')
relayPerfID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: relayPerfID.setStatus('mandatory')
relayTotalCollisions = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relayTotalCollisions.setStatus('mandatory')
hmPerfMonPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2), )
if mibBuilder.loadTexts: hmPerfMonPortTable.setStatus('mandatory')
hmPerfMonPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1), )
if mibBuilder.loadTexts: hmPerfMonPortEntry.setStatus('mandatory')
portHubPerfID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portHubPerfID.setStatus('mandatory')
portGroupPerfID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portGroupPerfID.setStatus('mandatory')
portPerfID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPerfID.setStatus('mandatory')
portReadableFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portReadableFrames.setStatus('mandatory')
portReadableOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portReadableOctets.setStatus('mandatory')
portPygmys = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPygmys.setStatus('mandatory')
portRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRunts.setStatus('mandatory')
portFrameCheckSeqErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFrameCheckSeqErrs.setStatus('mandatory')
portAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portAlignmentErrors.setStatus('mandatory')
portFramesTooLong = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFramesTooLong.setStatus('mandatory')
portAutoPartitionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portAutoPartitionCount.setStatus('mandatory')
hmAddrTrackPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1), )
if mibBuilder.loadTexts: hmAddrTrackPortTable.setStatus('mandatory')
hmAddrTrackPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1), )
if mibBuilder.loadTexts: hmAddrTrackPortEntry.setStatus('mandatory')
portHubAddrID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portHubAddrID.setStatus('mandatory')
portGroupAddrID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portGroupAddrID.setStatus('mandatory')
portAddrID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portAddrID.setStatus('mandatory')
portLastSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portLastSourceAddress.setStatus('mandatory')
portSourceAddrChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portSourceAddrChanges.setStatus('mandatory')
hmBadBitClockPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1), )
if mibBuilder.loadTexts: hmBadBitClockPortTable.setStatus('mandatory')
hmBadBitClockPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1), )
if mibBuilder.loadTexts: hmBadBitClockPortEntry.setStatus('mandatory')
portHubClockID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portHubClockID.setStatus('mandatory')
portGroupClockID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portGroupClockID.setStatus('mandatory')
portClockID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portClockID.setStatus('mandatory')
portOutOfSpecBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOutOfSpecBitRate.setStatus('mandatory')
mibBuilder.exportSymbols("XYPLEX-IEEE-HUB-MIB", relayTotalCollisions=relayTotalCollisions, portAddrID=portAddrID, hmSelfTestCapability=hmSelfTestCapability, groupNumberOfPorts=groupNumberOfPorts, portHubPerfID=portHubPerfID, portHubAddrID=portHubAddrID, hubResetTimeStamp=hubResetTimeStamp, portGroupPerfID=portGroupPerfID, hmBasicPortTable=hmBasicPortTable, portGroupAddrID=portGroupAddrID, portSourceAddrChanges=portSourceAddrChanges, hmBadBitClockCapability=hmBadBitClockCapability, portType=portType, hmPerfMonPortEntry=hmPerfMonPortEntry, portFrameCheckSeqErrs=portFrameCheckSeqErrs, ieeeHub=ieeeHub, hubResetting=hubResetting, hubHealthText=hubHealthText, hmBasicHubTable=hmBasicHubTable, hubSelfTestID=hubSelfTestID, hmAddrTrackCapability=hmAddrTrackCapability, hmBadBitClockPortTable=hmBadBitClockPortTable, hubID=hubID, hubGroupMap=hubGroupMap, hmPerfMonRelayTable=hmPerfMonRelayTable, portLastSourceAddress=portLastSourceAddress, portAdminState=portAdminState, portReadableOctets=portReadableOctets, hmAddrTrackPortTable=hmAddrTrackPortTable, portGroupBasicID=portGroupBasicID, relayHubPerfID=relayHubPerfID, hmPerfMonPortTable=hmPerfMonPortTable, hmBasicPortEntry=hmBasicPortEntry, hmSelfTestHubEntry=hmSelfTestHubEntry, hubHealthData=hubHealthData, relayPerfID=relayPerfID, portPygmys=portPygmys, portAlignmentErrors=portAlignmentErrors, portFramesTooLong=portFramesTooLong, portAutoPartitionCount=portAutoPartitionCount, hmBadBitClockPortEntry=hmBadBitClockPortEntry, portHubClockID=portHubClockID, portPerfID=portPerfID, hmPerfMonRelayEntry=hmPerfMonRelayEntry, xyplex=xyplex, portOutOfSpecBitRate=portOutOfSpecBitRate, hmBasicGroupEntry=hmBasicGroupEntry, hmBasicHubEntry=hmBasicHubEntry, portGroupClockID=portGroupClockID, portRunts=portRunts, hmBasicGroupTable=hmBasicGroupTable, portBasicID=portBasicID, portReadableFrames=portReadableFrames, hmAddrTrackPortEntry=hmAddrTrackPortEntry, hubHealthState=hubHealthState, hubGroupCapacity=hubGroupCapacity, portClockID=portClockID, hubExecutingSelfTest=hubExecutingSelfTest, portHubBasicID=portHubBasicID, groupID=groupID, hubSystemResetting=hubSystemResetting, groupHubID=groupHubID, hmBasicCapability=hmBasicCapability, portAutoPartitionState=portAutoPartitionState, hmPerfMonCapability=hmPerfMonCapability, hmSelfTestHubTable=hmSelfTestHubTable)

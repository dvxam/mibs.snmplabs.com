#
# PySNMP MIB module ISD2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ISD2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:57:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
scanet, = mibBuilder.importSymbols("SCANET-MIB", "scanet")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, iso, MibIdentifier, Bits, ModuleIdentity, Integer32, ObjectIdentity, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "iso", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32", "ObjectIdentity", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
isd2 = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 48))
isd2SigChan = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 48, 1))
isd2Dchan = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 48, 2))
isd2Phys = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 48, 3))
isd2CallCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 48, 4))
isd2SigChanTable = MibTable((1, 3, 6, 1, 4, 1, 208, 48, 1, 1), )
if mibBuilder.loadTexts: isd2SigChanTable.setStatus('mandatory')
if mibBuilder.loadTexts: isd2SigChanTable.setDescription('Table containing configuration and operational parameters for all ISDN Signalling Channels on this managed device.')
isd2SigChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1), ).setIndexNames((0, "ISD2-MIB", "isd2SigChanIfIndex"))
if mibBuilder.loadTexts: isd2SigChanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: isd2SigChanEntry.setDescription('An entry in the ISDN Signalling Channel Table.')
isd2SigChanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2SigChanIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: isd2SigChanIfIndex.setDescription('Interface index for this signalling channel.')
isd2SigChanL2State = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("teiUnassigned", 1), ("assignAwaitTei", 2), ("establishAwaitTei", 3), ("teiAssigned", 4), ("awaitEstablishment", 5), ("awaitRelease", 6), ("multipleFrameEstablished", 7), ("timerRecovery", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2SigChanL2State.setStatus('mandatory')
if mibBuilder.loadTexts: isd2SigChanL2State.setDescription('Signalling layer-2 state (Q.921).')
isd2SigChanCES = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2SigChanCES.setStatus('mandatory')
if mibBuilder.loadTexts: isd2SigChanCES.setDescription('Connection Endpoint Suffix (CES) for this signalling channel.')
isd2SigChanSAPI = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2SigChanSAPI.setStatus('mandatory')
if mibBuilder.loadTexts: isd2SigChanSAPI.setDescription('Service Access Point Identifier (SAPI) for this signalling channel')
isd2SigChanCallCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2SigChanCallCollisions.setStatus('mandatory')
if mibBuilder.loadTexts: isd2SigChanCallCollisions.setDescription('The number of calls over this signalling channel which failed because of collision.')
isd2SigChanAddressCheckFails = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2SigChanAddressCheckFails.setStatus('mandatory')
if mibBuilder.loadTexts: isd2SigChanAddressCheckFails.setDescription('The number of incoming calls over this signalling channel which were refused because of address mismatch.')
isd2DchanTable = MibTable((1, 3, 6, 1, 4, 1, 208, 48, 2, 1), )
if mibBuilder.loadTexts: isd2DchanTable.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanTable.setDescription('Table containing statistics for all ISDN D-Channels on this managed device.')
isd2DchanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1), ).setIndexNames((0, "ISD2-MIB", "isd2DchanIfIndex"))
if mibBuilder.loadTexts: isd2DchanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanEntry.setDescription('An entry in the ISDN D-Channel Table.')
isd2DchanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanIfIndex.setDescription('The Ifindex of this D-channel.')
isd2DchanRxShort = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxShort.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxShort.setDescription('The number of frames received which were discarded due to the frame length being too short.')
isd2DchanRxLong = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxLong.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxLong.setDescription('The number of frames received which were discarded due to the frame length being too long.')
isd2DchanRxCRCerror = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxCRCerror.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxCRCerror.setDescription('The number of frames received which were discarded due to Cyclic Redundancy Check (CRC) errors. This figure indicates the number of bit errors occuring over the WAN link.')
isd2DchanRxResidual = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxResidual.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxResidual.setDescription('The number of times the frame contained residual bits. This should not occur.')
isd2DchanRxAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxAborts.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxAborts.setDescription("The number of times the High-Level Data Link Control (HDLC) 'Abort' signal was received, indicating that the received packet should be ignored.")
isd2DchanRxOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxOverrun.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxOverrun.setDescription('The number of frames which were lost due to bus overload within the router. This should not occur.')
isd2DchanRxLostSync = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxLostSync.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxLostSync.setDescription('The number of frames which were lost due to drop of signal on the line.')
isd2DchanRxBufferLack = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxBufferLack.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxBufferLack.setDescription('The number of received frames which were lost due to RAM (buffer) overload within the router.')
isd2DchanRxApplnotready = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxApplnotready.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxApplnotready.setDescription('The number of received frames which were discarded since there was a temporary situation with no upper layer to receive the frame.')
isd2DchanRxUnknownProto = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanRxUnknownProto.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanRxUnknownProto.setDescription('The number of incoming frames which were discarded due to unknown protocol field.')
isd2DchanTxDiscardedProto = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanTxDiscardedProto.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanTxDiscardedProto.setDescription('The number of protocol frames for transmission which were lost due to RAM (buffer) overload within the router.')
isd2DchanTxDiscardedData = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanTxDiscardedData.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanTxDiscardedData.setDescription('The number of data frames for transmission which were lost due to RAM (buffer) overload within the router.')
isd2DchanTxUnderrun = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanTxUnderrun.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanTxUnderrun.setDescription('The number of frames for transmission that were not successfully transmitted due to CPU (processor) overload within the router.')
isd2DchanTxCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2DchanTxCollision.setStatus('mandatory')
if mibBuilder.loadTexts: isd2DchanTxCollision.setDescription('The number of outgoing frames which were discarded due to collisions that occured during transmission.')
isd2PhysTable = MibTable((1, 3, 6, 1, 4, 1, 208, 48, 3, 1), )
if mibBuilder.loadTexts: isd2PhysTable.setStatus('mandatory')
if mibBuilder.loadTexts: isd2PhysTable.setDescription('Table containing physical layer status for all ISDN ports on this managed device.')
isd2PhysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 48, 3, 1, 1), ).setIndexNames((0, "ISD2-MIB", "isd2PhysIfIndex"))
if mibBuilder.loadTexts: isd2PhysEntry.setStatus('mandatory')
if mibBuilder.loadTexts: isd2PhysEntry.setDescription('An entry in the ISDN physical layer Table.')
isd2PhysIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2PhysIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: isd2PhysIfIndex.setDescription('IfIndex for this ISDN port.')
isd2PhysL1State = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 100, 101, 102, 103, 104, 105, 106))).clone(namedValues=NamedValues(("inactive", 1), ("sensing", 2), ("deactivated", 3), ("awaitingSignal", 4), ("identifyingInput", 5), ("synchronized", 6), ("activated", 7), ("lostFraming", 8), ("lossOfPower", 100), ("operational", 101), ("fault1", 102), ("fault2", 103), ("fault3", 104), ("fault4", 105), ("powerOn", 106)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2PhysL1State.setStatus('mandatory')
if mibBuilder.loadTexts: isd2PhysL1State.setDescription('Physical layer state for this ISDN port.')
isd2PhysL1Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("noCableInserted", 1), ("lossOfSignal", 2), ("txCableNotConnected", 3), ("alarmIndicationSignal", 4), ("remoteAlarmIndication", 5), ("noMultiFrameAlignment", 6), ("noBasicFrameAlignment", 7), ("noSyncPattern", 8), ("ncrc4", 9), ("crce0", 10), ("crce1", 11), ("ebit0", 12), ("ebit1", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2PhysL1Alarm.setStatus('mandatory')
if mibBuilder.loadTexts: isd2PhysL1Alarm.setDescription('Primary Rate Interface alarm for this ISDN port. This entry is unused for BRI. 0 means noDetectedProblem')
isd2CallCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 208, 48, 4, 1), )
if mibBuilder.loadTexts: isd2CallCtrlTable.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlTable.setDescription('Table containing configuration and operational parameters for all ISDN links on this managed device.')
isd2CallCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1), ).setIndexNames((0, "ISD2-MIB", "isd2CallCtrlSigchanIfIndex"))
if mibBuilder.loadTexts: isd2CallCtrlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlEntry.setDescription('An entry in the ISDN link Table.')
isd2CallCtrlSigchanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlSigchanIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlSigchanIfIndex.setDescription('Interface index for the current signalling-channel associated with this link. The index is zero if no signalling-channel is associated.')
isd2CallCtrlBchanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlBchanIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlBchanIfIndex.setDescription('Interface index for the current B-channel associated with this link. The index is zero if no B-channel is allocated.')
isd2CallCtrlLocalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(22, 22)).setFixedLength(22)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlLocalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlLocalNumber.setDescription('The local ISDN number for this link.')
isd2CallCtrlLocalSubaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlLocalSubaddr.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlLocalSubaddr.setDescription('The local ISDN subaddress for this link.')
isd2CallCtrlRemoteNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(22, 22)).setFixedLength(22)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlRemoteNumber.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlRemoteNumber.setDescription('The ISDN number the current or last call is or was connected to.')
isd2CallCtrlRemoteSubaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlRemoteSubaddr.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlRemoteSubaddr.setDescription('The ISDN subaddress the current or last call is or was connected to.')
isd2CallCtrlL3State = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47))).clone(namedValues=NamedValues(("callInit", 1), ("overlapSending", 2), ("outCallProc", 3), ("callDelivered", 4), ("undef5", 5), ("callPresent", 6), ("callReceived", 7), ("connectRequest", 8), ("inCallProc", 9), ("callActive", 10), ("disconnectRequest", 11), ("disconnectInd", 12), ("passiveAwaitingConf", 13), ("callPassive", 14), ("suspendRequest", 15), ("undef16", 16), ("resumeRequest", 17), ("undef18", 18), ("releaseRequest", 19), ("registerRequest", 20), ("cancelRequest", 21), ("undef22", 22), ("undef23", 23), ("undef24", 24), ("overlapReceive", 25), ("idleState", 26), ("establishWait", 27), ("asaiTr1State", 28), ("u10HoldRequest", 29), ("u10TransferRequest", 30), ("u10ConferenceRequest", 31), ("u10ReconnectRequest", 32), ("u10AwaitingDisc", 33), ("u10CallOnHold", 34), ("deactivated", 35), ("reactivateRequested", 36), ("deactivateRequested", 37), ("ni1HoldReqU3", 38), ("ni1HoldReqU4", 39), ("ni1HoldReqU10", 40), ("ni1RetrieveU3", 41), ("ni1RetrieveU4", 42), ("ni1RetrieveU10", 43), ("ni1HoldActiveU3", 44), ("ni1HoldActiveU4", 45), ("ni1HoldActiveU10", 46), ("broadcastState", 47)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlL3State.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlL3State.setDescription('Signalling layer-3 state (Q.931 and custom). 0 means nullState.')
isd2CallCtrlCallRef = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlCallRef.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlCallRef.setDescription('Signalling layer-3 call reference (Q.931).')
isd2CallCtrlChannelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlChannelNum.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlChannelNum.setDescription('The current B-channel number associated with this link.')
isd2CallCtrlOutCallsConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlOutCallsConnected.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlOutCallsConnected.setDescription('The number of outgoing calls on this link which were actually connected.')
isd2CallCtrlOutCallsFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlOutCallsFailed.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlOutCallsFailed.setDescription('The number of outgoing calls on this link which failed.')
isd2CallCtrlInCallsConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlInCallsConnected.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlInCallsConnected.setDescription('The number of incoming calls on this link which were actually connected.')
isd2CallCtrlInCallsRefused = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlInCallsRefused.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlInCallsRefused.setDescription('The number of incoming calls on this link which were refused.')
isd2CallCtrlCallCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlCallCollisions.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlCallCollisions.setDescription('The number of calls on this link which failed because of collision.')
isd2CallCtrlCauseCode = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlCauseCode.setReference('- Bellcore SR-NWT-001953, Generic Guidelines for ISDN Terminal Equipment On Basic Access Interfaces, chapter 5.2.5.8. - Bellcore SR-NWT-002343, ISDN Primary Rate Interface Generic Guidelines for Customer Premises Equipment, chapter 8.2.5.8. - ITU-T Q.931, Appendix I. - ITU-T X.25, CAUSE and DIAGNOSTIC field values. - German Telekom FTZ 1TR6, chapter 3.2.3.4.4.4.')
if mibBuilder.loadTexts: isd2CallCtrlCauseCode.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlCauseCode.setDescription('The encoded network cause value associated with the last call. This object will be updated whenever a call is started or cleared. The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. Some references for possible cause values are given below.')
isd2CallCtrlLocationCode = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlLocationCode.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlLocationCode.setDescription('The encoded network cause location value associated with the last call. This object will be updated whenever a call is started or cleared.')
isd2CallCtrlCauseText = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(100, 100)).setFixedLength(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: isd2CallCtrlCauseText.setStatus('mandatory')
if mibBuilder.loadTexts: isd2CallCtrlCauseText.setDescription('ASCII text describing the reason for the last call termination. This object will be updated whenever a call is started or cleared.')
mibBuilder.exportSymbols("ISD2-MIB", isd2CallCtrlOutCallsFailed=isd2CallCtrlOutCallsFailed, isd2CallCtrlLocalSubaddr=isd2CallCtrlLocalSubaddr, isd2Phys=isd2Phys, isd2=isd2, isd2DchanRxUnknownProto=isd2DchanRxUnknownProto, isd2DchanTxUnderrun=isd2DchanTxUnderrun, isd2CallCtrlL3State=isd2CallCtrlL3State, isd2CallCtrlCauseCode=isd2CallCtrlCauseCode, isd2CallCtrlSigchanIfIndex=isd2CallCtrlSigchanIfIndex, isd2SigChanIfIndex=isd2SigChanIfIndex, isd2DchanRxAborts=isd2DchanRxAborts, isd2SigChanAddressCheckFails=isd2SigChanAddressCheckFails, isd2CallCtrlLocalNumber=isd2CallCtrlLocalNumber, isd2CallCtrlChannelNum=isd2CallCtrlChannelNum, isd2PhysL1Alarm=isd2PhysL1Alarm, isd2DchanRxApplnotready=isd2DchanRxApplnotready, isd2DchanTxDiscardedData=isd2DchanTxDiscardedData, isd2CallCtrlTable=isd2CallCtrlTable, isd2CallCtrlLocationCode=isd2CallCtrlLocationCode, isd2CallCtrlInCallsConnected=isd2CallCtrlInCallsConnected, isd2DchanRxOverrun=isd2DchanRxOverrun, isd2PhysL1State=isd2PhysL1State, isd2DchanEntry=isd2DchanEntry, isd2DchanRxLostSync=isd2DchanRxLostSync, isd2PhysTable=isd2PhysTable, isd2CallCtrlRemoteNumber=isd2CallCtrlRemoteNumber, isd2SigChanSAPI=isd2SigChanSAPI, isd2PhysIfIndex=isd2PhysIfIndex, isd2CallCtrlInCallsRefused=isd2CallCtrlInCallsRefused, isd2DchanRxCRCerror=isd2DchanRxCRCerror, isd2SigChanTable=isd2SigChanTable, isd2SigChanCES=isd2SigChanCES, isd2SigChanCallCollisions=isd2SigChanCallCollisions, isd2Dchan=isd2Dchan, isd2SigChanL2State=isd2SigChanL2State, isd2CallCtrl=isd2CallCtrl, isd2CallCtrlCallRef=isd2CallCtrlCallRef, isd2DchanTxDiscardedProto=isd2DchanTxDiscardedProto, isd2DchanRxBufferLack=isd2DchanRxBufferLack, isd2DchanRxLong=isd2DchanRxLong, isd2CallCtrlCallCollisions=isd2CallCtrlCallCollisions, isd2DchanTxCollision=isd2DchanTxCollision, isd2CallCtrlRemoteSubaddr=isd2CallCtrlRemoteSubaddr, isd2DchanTable=isd2DchanTable, isd2DchanRxResidual=isd2DchanRxResidual, isd2CallCtrlBchanIfIndex=isd2CallCtrlBchanIfIndex, isd2CallCtrlCauseText=isd2CallCtrlCauseText, isd2DchanRxShort=isd2DchanRxShort, isd2SigChan=isd2SigChan, isd2DchanIfIndex=isd2DchanIfIndex, isd2CallCtrlEntry=isd2CallCtrlEntry, isd2PhysEntry=isd2PhysEntry, isd2CallCtrlOutCallsConnected=isd2CallCtrlOutCallsConnected, isd2SigChanEntry=isd2SigChanEntry)
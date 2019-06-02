#
# PySNMP MIB module OLD-CISCO-VINES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OLD-CISCO-VINES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:32:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
temporary, = mibBuilder.importSymbols("CISCO-SMI", "temporary")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Gauge32, ModuleIdentity, Bits, TimeTicks, ObjectIdentity, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Gauge32", "ModuleIdentity", "Bits", "TimeTicks", "ObjectIdentity", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tmpvines = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 3, 5))
vinesInput = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesInput.setStatus('mandatory')
if mibBuilder.loadTexts: vinesInput.setDescription('Total input count of number of Vines packets.')
vinesOutput = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesOutput.setStatus('mandatory')
if mibBuilder.loadTexts: vinesOutput.setDescription('Total count of number of Vines output packets.')
vinesLocaldest = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesLocaldest.setStatus('mandatory')
if mibBuilder.loadTexts: vinesLocaldest.setDescription('Total count of Vines input packets for this host.')
vinesForwarded = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesForwarded.setStatus('mandatory')
if mibBuilder.loadTexts: vinesForwarded.setDescription('Total count of number of Vines packets forwarded.')
vinesBcastin = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesBcastin.setStatus('mandatory')
if mibBuilder.loadTexts: vinesBcastin.setDescription('Total count of number of Vines input broadcast packets.')
vinesBcastout = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesBcastout.setStatus('mandatory')
if mibBuilder.loadTexts: vinesBcastout.setDescription('Total count of number of Vines output broadcast packets.')
vinesBcastfwd = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesBcastfwd.setStatus('mandatory')
if mibBuilder.loadTexts: vinesBcastfwd.setDescription('Total count of number of Vines broadcast packets forwarded.')
vinesNotlan = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesNotlan.setStatus('mandatory')
if mibBuilder.loadTexts: vinesNotlan.setDescription('Total count of number of Vines broadcast packets not forwarded to all interfaces because the LAN ONLY bit was set.')
vinesNotgt4800 = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesNotgt4800.setStatus('mandatory')
if mibBuilder.loadTexts: vinesNotgt4800.setDescription('Total count of number of Vines broadcast packets not forwarded to all interfaces because the OVER 4800 BPS bit was set.')
vinesNocharges = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesNocharges.setStatus('mandatory')
if mibBuilder.loadTexts: vinesNocharges.setDescription('Total count of number of Vines broadcast packets not forwarded to all interfaces because the NO CHARGES only bit was set.')
vinesFormaterror = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesFormaterror.setStatus('mandatory')
if mibBuilder.loadTexts: vinesFormaterror.setDescription('Total count of number of Vines input packets with header errors.')
vinesCksumerr = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesCksumerr.setStatus('mandatory')
if mibBuilder.loadTexts: vinesCksumerr.setDescription('Total count of number of Vines input packets with checksum errors.')
vinesHopcount = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesHopcount.setStatus('mandatory')
if mibBuilder.loadTexts: vinesHopcount.setDescription('Total count of number of Vines input packets that have exceeded the maximum hop count.')
vinesNoroute = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesNoroute.setStatus('mandatory')
if mibBuilder.loadTexts: vinesNoroute.setDescription('Total count of number of Vines packets dropped due to no route.')
vinesEncapsfailed = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesEncapsfailed.setStatus('mandatory')
if mibBuilder.loadTexts: vinesEncapsfailed.setDescription('Total count of number of Vines packets dropped due to output encapsulation failed.')
vinesUnknown = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesUnknown.setStatus('mandatory')
if mibBuilder.loadTexts: vinesUnknown.setDescription('Total count of number of unknown Vines input packets.')
vinesIcpIn = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIcpIn.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIcpIn.setDescription('Total count of number of Vines ICP packets received.')
vinesIcpOut = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIcpOut.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIcpOut.setDescription('Total count of number of Vines ICP packets generaed.')
vinesMetricOut = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesMetricOut.setStatus('mandatory')
if mibBuilder.loadTexts: vinesMetricOut.setDescription('Total count of number of Vines ICP Metric Notification packets generated.')
vinesMacEchoIn = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesMacEchoIn.setStatus('mandatory')
if mibBuilder.loadTexts: vinesMacEchoIn.setDescription('Total count of number of Vines MAC level Echo packets received.')
vinesMacEchoOut = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesMacEchoOut.setStatus('mandatory')
if mibBuilder.loadTexts: vinesMacEchoOut.setDescription('Total count of number of Vines MAC level Echo packets generated.')
vinesEchoIn = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesEchoIn.setStatus('mandatory')
if mibBuilder.loadTexts: vinesEchoIn.setDescription('Total count of number of Vines Echo packets received.')
vinesEchoOut = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesEchoOut.setStatus('mandatory')
if mibBuilder.loadTexts: vinesEchoOut.setDescription('Total count of number of Vines Echo packets generated.')
vinesProxyCnt = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesProxyCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesProxyCnt.setDescription('Total count of proxy packets sent.')
vinesProxyReplyCnt = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesProxyReplyCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesProxyReplyCnt.setDescription('Total count of responses to proxy packets.')
vinesNet = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesNet.setStatus('mandatory')
if mibBuilder.loadTexts: vinesNet.setDescription('Vines network number of this router.')
vinesSubNet = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesSubNet.setStatus('mandatory')
if mibBuilder.loadTexts: vinesSubNet.setDescription('Vines sub-network number of this router.')
vinesClient = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 5, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesClient.setStatus('mandatory')
if mibBuilder.loadTexts: vinesClient.setDescription('Next Vines client sub-network number to be assigned by this router.')
vinesIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 3, 5, 29), )
if mibBuilder.loadTexts: vinesIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTable.setDescription('Vines interface table')
vinesIfTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vinesIfTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTableEntry.setDescription('VINES interface table')
vinesIfMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfMetric.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfMetric.setDescription('Vines protocol metric value.')
vinesIfEnctype = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfEnctype.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfEnctype.setDescription('Vines protocol default encapsulation')
vinesIfAccesslist = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfAccesslist.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfAccesslist.setDescription('Vines protocol outgoing access list number.')
vinesIfPropagate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("neverPropagate", 1), ("alwaysPropagate", 2), ("dynamicPropagate", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfPropagate.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfPropagate.setDescription("Vines protocol 'propagate' enabled.")
vinesIfArpEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfArpEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfArpEnabled.setDescription('Vines protocol arp replies enabled.')
vinesIfServerless = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("neverSvrless", 1), ("dynamicSvrless", 2), ("alwaysSvrless", 3), ("alwaysBcastSvrless", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfServerless.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfServerless.setDescription('Vines protocol serverless support enabled.')
vinesIfRedirectInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRedirectInterval.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRedirectInterval.setDescription('Vines protocol redirect interval (in ms).')
vinesIfSplitDisabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfSplitDisabled.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfSplitDisabled.setDescription('Vines protocol split horizon disabled')
vinesIfLineup = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfLineup.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfLineup.setDescription('Vines protocol line up/down.')
vinesIfFastokay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfFastokay.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfFastokay.setDescription('Vines protocol fast switching supported.')
vinesIfRouteCache = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRouteCache.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRouteCache.setDescription('Vines protocol fast switching requested')
vinesIfRxNotEnabledCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxNotEnabledCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxNotEnabledCnt.setDescription('Vines protocol count of input packets discarded because interface not configured.')
vinesIfRxFormatErrorCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxFormatErrorCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxFormatErrorCnt.setDescription('Vines protocol count of input packets with format errors.')
vinesIfRxLocalDestCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxLocalDestCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxLocalDestCnt.setDescription('Vines protocol count of input packets destined for this router.')
vinesIfRxBcastinCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxBcastinCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxBcastinCnt.setDescription('Vines protocol input broadcast count.')
vinesIfRxForwardedCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxForwardedCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxForwardedCnt.setDescription('Vines protocol count of input packets forwarded to another interface.')
vinesIfRxNoRouteCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxNoRouteCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxNoRouteCnt.setDescription('Vines protocol count of input packets dropped because there was no route to the destination.')
vinesIfRxZeroHopCountCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxZeroHopCountCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxZeroHopCountCnt.setDescription('Vines protocol count of input packets dropped due to a zero hop count.')
vinesIfRxChecksumErrorCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxChecksumErrorCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxChecksumErrorCnt.setDescription('Vines protocol count of input packets with checksum errors.')
vinesIfRxArp0Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxArp0Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxArp0Cnt.setDescription('Vines protocol count of input ARP Query Request messages.')
vinesIfRxArp1Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxArp1Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxArp1Cnt.setDescription('Vines protocol count of input ARP Query Response messages.')
vinesIfRxArp2Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxArp2Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxArp2Cnt.setDescription('Vines protocol count of input ARP Assignment Request messages.')
vinesIfRxArp3Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxArp3Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxArp3Cnt.setDescription('Vines protocol count of input ARP Assignment Response messages.')
vinesIfRxArpIllegalCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxArpIllegalCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxArpIllegalCnt.setDescription('Vines protocol count of input illegal ARP messages.')
vinesIfRxIcpErrorCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxIcpErrorCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxIcpErrorCnt.setDescription('Vines protocol count of input ICP error messages.')
vinesIfRxIcpMetricCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxIcpMetricCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxIcpMetricCnt.setDescription('Vines protocol count of input ICP metric messages.')
vinesIfRxIcpIllegalCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxIcpIllegalCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxIcpIllegalCnt.setDescription('Vines protocol count of input illegal ICP messages.')
vinesIfRxIpcCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxIpcCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxIpcCnt.setDescription('Vines protocol count of input IPC messages.')
vinesIfRxRtp0Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxRtp0Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxRtp0Cnt.setDescription('Vines protocol count of input RTP type 0 messages.')
vinesIfRxRtp1Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxRtp1Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxRtp1Cnt.setDescription('Vines protocol count of input RTP Request messages.')
vinesIfRxRtp2Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxRtp2Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxRtp2Cnt.setDescription('Vines protocol count of input RTP type 2 messages.')
vinesIfRxRtp3Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxRtp3Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxRtp3Cnt.setDescription('Vines protocol count of input RTP type 3 messages.')
vinesIfRxRtp4Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxRtp4Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxRtp4Cnt.setDescription('Vines protocol count of input RTP Update messages.')
vinesIfRxRtp5Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxRtp5Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxRtp5Cnt.setDescription('Vines protocol count of input RTP Response messages.')
vinesIfRxRtp6Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxRtp6Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxRtp6Cnt.setDescription('Vines protocol count of input RTP Redirect messages.')
vinesIfRxRtpIllegalCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxRtpIllegalCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxRtpIllegalCnt.setDescription('Vines protocol count of input illegal RTP messages.')
vinesIfRxSppCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxSppCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxSppCnt.setDescription('Vines protocol count of input SPP messages.')
vinesIfRxIpUnknownCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxIpUnknownCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxIpUnknownCnt.setDescription('Vines protocol count of input packets of unknown Vines protocols.')
vinesIfRxIpcUnknownCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxIpcUnknownCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxIpcUnknownCnt.setDescription('Vines protocol count of input packets of unknown Vines IPC ports.')
vinesIfRxBcastHelperedCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxBcastHelperedCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxBcastHelperedCnt.setDescription('Vines protocol count of input packets helpered to another server.')
vinesIfRxBcastForwardedCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxBcastForwardedCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxBcastForwardedCnt.setDescription('Vines protocol input broadcast forwarded to other interface(s).')
vinesIfRxBcastDuplicateCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxBcastDuplicateCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxBcastDuplicateCnt.setDescription('Vines protocol input duplicate broadcast count.')
vinesIfRxEchoCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxEchoCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxEchoCnt.setDescription('Vines protocol count of input IPC echo messages.')
vinesIfRxMacEchoCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxMacEchoCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxMacEchoCnt.setDescription('Vines protocol count of input MAC layer echo frames.')
vinesIfRxProxyReplyCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfRxProxyReplyCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfRxProxyReplyCnt.setDescription('Vines protocol count of responses to proxy packets.')
vinesIfTxUnicastCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxUnicastCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxUnicastCnt.setDescription('Vines protocol unicast packets generated.')
vinesIfTxBcastCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxBcastCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxBcastCnt.setDescription('Vines protocol broadcast packets generated.')
vinesIfTxForwardedCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 53), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxForwardedCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxForwardedCnt.setDescription('Vines protocol count of forwarded packets.')
vinesIfTxFailedEncapsCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 54), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxFailedEncapsCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxFailedEncapsCnt.setDescription('Vines protocol output encapsulation failures.')
vinesIfTxFailedAccessCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 55), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxFailedAccessCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxFailedAccessCnt.setDescription('Vines protocol output access list failures.')
vinesIfTxFailedDownCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 56), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxFailedDownCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxFailedDownCnt.setDescription('Vines protocol output interface down count.')
vinesIfTxNotBcastToSourceCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 57), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxNotBcastToSourceCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxNotBcastToSourceCnt.setDescription('Vines protocol output broadcast not sent because interfaceleads back to the source.')
vinesIfTxNotBcastNotlanCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 58), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxNotBcastNotlanCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxNotBcastNotlanCnt.setDescription("Vines protocol output broadcast not sent due to 'Lan Only' class.")
vinesIfTxNotBcastNotgt4800Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 59), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxNotBcastNotgt4800Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxNotBcastNotgt4800Cnt.setDescription("Vines protocol output broadcast not sent due to 'High Speed' class.")
vinesIfTxNotBcastPpchargeCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 60), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxNotBcastPpchargeCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxNotBcastPpchargeCnt.setDescription("Vines protocol output broadcast not sent due to 'No Charges' class.")
vinesIfTxBcastForwardedCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 61), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxBcastForwardedCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxBcastForwardedCnt.setDescription('Vines protocol output broadcast forwarded from another interface.')
vinesIfTxBcastHelperedCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxBcastHelperedCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxBcastHelperedCnt.setDescription('Vines protocol output broadcast helpered to a vines server.')
vinesIfTxArp0Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxArp0Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxArp0Cnt.setDescription('Vines protocol count of output ARP Query Request messages.')
vinesIfTxArp1Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 64), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxArp1Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxArp1Cnt.setDescription('Vines protocol count of output ARP Query Response messages.')
vinesIfTxArp2Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 65), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxArp2Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxArp2Cnt.setDescription('Vines protocol count of output ARP Assignment Request messages.')
vinesIfTxArp3Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 66), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxArp3Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxArp3Cnt.setDescription('Vines protocol count of input ARP Assignment Response messages.')
vinesIfTxIcpErrorCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 67), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxIcpErrorCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxIcpErrorCnt.setDescription('Vines protocol count of output IPC Error messages.')
vinesIfTxIcpMetricCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 68), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxIcpMetricCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxIcpMetricCnt.setDescription('Vines protocol count of output IPC metric messages.')
vinesIfTxIpcCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 69), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxIpcCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxIpcCnt.setDescription('Vines protocol count of output ICP messages.')
vinesIfTxRtp0Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 70), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxRtp0Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxRtp0Cnt.setDescription('Vines protocol count of output RTP type 0 messages.')
vinesIfTxRtp1Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 71), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxRtp1Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxRtp1Cnt.setDescription('Vines protocol count of output RTP Request messages.')
vinesIfTxRtp2Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 72), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxRtp2Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxRtp2Cnt.setDescription('Vines protocol count of output RTP type 2 messages.')
vinesIfTxRtp3Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 73), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxRtp3Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxRtp3Cnt.setDescription('Vines protocol count of output RTP type 3 messages.')
vinesIfTxRtp4Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 74), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxRtp4Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxRtp4Cnt.setDescription('Vines protocol count of output RTP Update messages.')
vinesIfTxRtp5Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 75), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxRtp5Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxRtp5Cnt.setDescription('Vines protocol count of output RTP Response messages.')
vinesIfTxRtp6Cnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 76), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxRtp6Cnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxRtp6Cnt.setDescription('Vines protocol count of output RTP Redirect messages.')
vinesIfTxSppCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 77), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxSppCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxSppCnt.setDescription('Vines protocol count of output SPP messages.')
vinesIfTxEchoCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 78), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxEchoCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxEchoCnt.setDescription('Vines protocol count of output IPC echo messages.')
vinesIfTxMacEchoCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 79), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxMacEchoCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxMacEchoCnt.setDescription('Vines protocol count of output IPCMAC layer echo frames.')
vinesIfTxProxyCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 80), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfTxProxyCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfTxProxyCnt.setDescription('Vines protocol count of proxy packets sent.')
vinesIfInputRouterFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 81), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfInputRouterFilter.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfInputRouterFilter.setDescription('Vines protocol filter on received routing information source address.')
vinesIfInputNetworkFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 82), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfInputNetworkFilter.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfInputNetworkFilter.setDescription('Vines protocol filter on received routing information content.')
vinesIfOutputNetworkFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 83), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vinesIfOutputNetworkFilter.setStatus('mandatory')
if mibBuilder.loadTexts: vinesIfOutputNetworkFilter.setDescription('Vines protocol filter on transmitted routing information content.')
mibBuilder.exportSymbols("OLD-CISCO-VINES-MIB", vinesIfRxArp1Cnt=vinesIfRxArp1Cnt, vinesIfRxNotEnabledCnt=vinesIfRxNotEnabledCnt, vinesIfTxRtp1Cnt=vinesIfTxRtp1Cnt, vinesNocharges=vinesNocharges, vinesMetricOut=vinesMetricOut, vinesIfRxRtpIllegalCnt=vinesIfRxRtpIllegalCnt, vinesForwarded=vinesForwarded, vinesIcpIn=vinesIcpIn, vinesNoroute=vinesNoroute, vinesEncapsfailed=vinesEncapsfailed, vinesIfRxBcastDuplicateCnt=vinesIfRxBcastDuplicateCnt, vinesIfRxZeroHopCountCnt=vinesIfRxZeroHopCountCnt, vinesIfTxNotBcastNotlanCnt=vinesIfTxNotBcastNotlanCnt, vinesLocaldest=vinesLocaldest, vinesProxyReplyCnt=vinesProxyReplyCnt, vinesIfRxSppCnt=vinesIfRxSppCnt, vinesIfRxIcpMetricCnt=vinesIfRxIcpMetricCnt, vinesOutput=vinesOutput, vinesIfTxNotBcastPpchargeCnt=vinesIfTxNotBcastPpchargeCnt, vinesIfTxIpcCnt=vinesIfTxIpcCnt, vinesIfEnctype=vinesIfEnctype, vinesClient=vinesClient, vinesIfRxArp2Cnt=vinesIfRxArp2Cnt, vinesIfRxIpcCnt=vinesIfRxIpcCnt, vinesIfMetric=vinesIfMetric, vinesIfTxBcastHelperedCnt=vinesIfTxBcastHelperedCnt, vinesIfPropagate=vinesIfPropagate, vinesIfTxMacEchoCnt=vinesIfTxMacEchoCnt, vinesIfTxSppCnt=vinesIfTxSppCnt, vinesMacEchoOut=vinesMacEchoOut, vinesIfRxNoRouteCnt=vinesIfRxNoRouteCnt, vinesIfRxRtp5Cnt=vinesIfRxRtp5Cnt, tmpvines=tmpvines, vinesIfRxIpcUnknownCnt=vinesIfRxIpcUnknownCnt, vinesIfRxMacEchoCnt=vinesIfRxMacEchoCnt, vinesEchoOut=vinesEchoOut, vinesIfTxFailedDownCnt=vinesIfTxFailedDownCnt, vinesIfTxArp2Cnt=vinesIfTxArp2Cnt, vinesIfRxArpIllegalCnt=vinesIfRxArpIllegalCnt, vinesIfInputRouterFilter=vinesIfInputRouterFilter, vinesIfRxRtp0Cnt=vinesIfRxRtp0Cnt, vinesIfRxLocalDestCnt=vinesIfRxLocalDestCnt, vinesIfRxProxyReplyCnt=vinesIfRxProxyReplyCnt, vinesFormaterror=vinesFormaterror, vinesIfTxRtp0Cnt=vinesIfTxRtp0Cnt, vinesIfTxRtp4Cnt=vinesIfTxRtp4Cnt, vinesIfTxForwardedCnt=vinesIfTxForwardedCnt, vinesIfTxIcpErrorCnt=vinesIfTxIcpErrorCnt, vinesNotlan=vinesNotlan, vinesIfTxBcastCnt=vinesIfTxBcastCnt, vinesIfRxRtp6Cnt=vinesIfRxRtp6Cnt, vinesIfRxFormatErrorCnt=vinesIfRxFormatErrorCnt, vinesIfTableEntry=vinesIfTableEntry, vinesIfRxIcpErrorCnt=vinesIfRxIcpErrorCnt, vinesIfRxArp3Cnt=vinesIfRxArp3Cnt, vinesBcastin=vinesBcastin, vinesIfTxNotBcastNotgt4800Cnt=vinesIfTxNotBcastNotgt4800Cnt, vinesIfTxArp0Cnt=vinesIfTxArp0Cnt, vinesIfTxFailedEncapsCnt=vinesIfTxFailedEncapsCnt, vinesNotgt4800=vinesNotgt4800, vinesEchoIn=vinesEchoIn, vinesIfAccesslist=vinesIfAccesslist, vinesIfTable=vinesIfTable, vinesIfFastokay=vinesIfFastokay, vinesIfInputNetworkFilter=vinesIfInputNetworkFilter, vinesProxyCnt=vinesProxyCnt, vinesIfRouteCache=vinesIfRouteCache, vinesIfRxBcastHelperedCnt=vinesIfRxBcastHelperedCnt, vinesIfOutputNetworkFilter=vinesIfOutputNetworkFilter, vinesIfTxRtp2Cnt=vinesIfTxRtp2Cnt, vinesIfTxEchoCnt=vinesIfTxEchoCnt, vinesIfTxNotBcastToSourceCnt=vinesIfTxNotBcastToSourceCnt, vinesIfRxRtp2Cnt=vinesIfRxRtp2Cnt, vinesIfRxRtp1Cnt=vinesIfRxRtp1Cnt, vinesIfRxEchoCnt=vinesIfRxEchoCnt, vinesInput=vinesInput, vinesIfArpEnabled=vinesIfArpEnabled, vinesIfSplitDisabled=vinesIfSplitDisabled, vinesIfRxRtp3Cnt=vinesIfRxRtp3Cnt, vinesIfRxChecksumErrorCnt=vinesIfRxChecksumErrorCnt, vinesIfTxArp3Cnt=vinesIfTxArp3Cnt, vinesIfTxIcpMetricCnt=vinesIfTxIcpMetricCnt, vinesIfTxRtp3Cnt=vinesIfTxRtp3Cnt, vinesIfRxArp0Cnt=vinesIfRxArp0Cnt, vinesIfTxArp1Cnt=vinesIfTxArp1Cnt, vinesBcastfwd=vinesBcastfwd, vinesIcpOut=vinesIcpOut, vinesIfRxIcpIllegalCnt=vinesIfRxIcpIllegalCnt, vinesIfTxRtp5Cnt=vinesIfTxRtp5Cnt, vinesIfRxBcastinCnt=vinesIfRxBcastinCnt, vinesBcastout=vinesBcastout, vinesMacEchoIn=vinesMacEchoIn, vinesIfTxProxyCnt=vinesIfTxProxyCnt, vinesIfRedirectInterval=vinesIfRedirectInterval, vinesNet=vinesNet, vinesIfRxRtp4Cnt=vinesIfRxRtp4Cnt, vinesIfRxBcastForwardedCnt=vinesIfRxBcastForwardedCnt, vinesCksumerr=vinesCksumerr, vinesIfTxFailedAccessCnt=vinesIfTxFailedAccessCnt, vinesIfServerless=vinesIfServerless, vinesIfTxBcastForwardedCnt=vinesIfTxBcastForwardedCnt, vinesSubNet=vinesSubNet, vinesIfRxForwardedCnt=vinesIfRxForwardedCnt, vinesIfLineup=vinesIfLineup, vinesHopcount=vinesHopcount, vinesIfTxUnicastCnt=vinesIfTxUnicastCnt, vinesIfRxIpUnknownCnt=vinesIfRxIpUnknownCnt, vinesUnknown=vinesUnknown, vinesIfTxRtp6Cnt=vinesIfTxRtp6Cnt)
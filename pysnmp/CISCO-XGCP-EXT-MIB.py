#
# PySNMP MIB module CISCO-XGCP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-XGCP-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:05:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
CCallControlProfileIndex, cmgwIndex = mibBuilder.importSymbols("CISCO-MEDIA-GATEWAY-MIB", "CCallControlProfileIndex", "cmgwIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CountryCodeITU, = mibBuilder.importSymbols("CISCO-TC", "CountryCodeITU")
CXgcpRetryMethod, = mibBuilder.importSymbols("CISCO-XGCP-MIB", "CXgcpRetryMethod")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, ObjectIdentity, Counter64, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, IpAddress, Counter32, Integer32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Counter64", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "IpAddress", "Counter32", "Integer32", "MibIdentifier", "Bits")
TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
ciscoXgcpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 325))
ciscoXgcpExtMIB.setRevisions(('2003-01-30 00:00',))
if mibBuilder.loadTexts: ciscoXgcpExtMIB.setLastUpdated('200301300000Z')
if mibBuilder.loadTexts: ciscoXgcpExtMIB.setOrganization('Cisco Systems, Inc.')
cxgcpExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 325, 1))
cxgcpExtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1))
class DtmfRelayMode(TextualConvention, Integer32):
    reference = 'RFC2833, Section 3: RTP Payload Format for Named Telephone Events'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("dtmfRelayDisabled", 1), ("dtmfRelayCisco", 2), ("dtmfRelayNse", 3), ("dtmfRelayOutOfBand", 4), ("dtmfRelayNteGw", 5), ("dtmfRelayNteCa", 6), ("dtmfRelayInband", 7), ("dtmfRelayType3", 8))

class DtmfCodecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("dtmfCodecAll", 1), ("dtmfCodecLowRate", 2))

class CxeTerminalProviderCode(TextualConvention, OctetString):
    reference = 'ITU-T T.35 - Section 3.2 Terminal Provider Code'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
cxeCallCtrlConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1), )
if mibBuilder.loadTexts: cxeCallCtrlConfigTable.setStatus('current')
cxeCallCtrlConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"))
if mibBuilder.loadTexts: cxeCallCtrlConfigEntry.setStatus('current')
cxeCallCtrlControlServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(96)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlControlServiceType.setStatus('current')
cxeCallCtrlBearerServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(160)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlBearerServiceType.setStatus('current')
cxeCallCtrlVoIpDtmfRelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 3), DtmfRelayMode().clone('dtmfRelayDisabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlVoIpDtmfRelayMode.setStatus('current')
cxeCallCtrlVoIpDtmfCodec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 4), DtmfCodecType().clone('dtmfCodecAll')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlVoIpDtmfCodec.setStatus('current')
cxeCallCtrlVoAal2DtmfRelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 5), DtmfRelayMode().clone('dtmfRelayDisabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlVoAal2DtmfRelayMode.setStatus('current')
cxeCallCtrlVoAal2DtmfCodec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 6), DtmfCodecType().clone('dtmfCodecAll')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlVoAal2DtmfCodec.setStatus('current')
cxeCallCtrlTsePayload = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlTsePayload.setStatus('current')
cxeCallCtrlNetNseTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(250, 10000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlNetNseTimer.setStatus('current')
cxeCallCtrlRtcpRcvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setUnits('times').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlRtcpRcvTimer.setStatus('current')
cxeCallCtrlIgnoreAal2LcoCodec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlIgnoreAal2LcoCodec.setStatus('current')
cxeCallCtrlDigitMapOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dmOrderShortest", 1), ("dmOrderOrdered", 2))).clone('dmOrderShortest')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlDigitMapOrder.setStatus('current')
cxeCallCtrlT38Inhibited = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlT38Inhibited.setStatus('current')
cxeCallCtrlT38NseRspTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(250, 10000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlT38NseRspTimer.setStatus('current')
cxeCallCtrlT38FecEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 14), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlT38FecEnabled.setStatus('current')
cxeCallCtrlT38LsRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlT38LsRedundancy.setStatus('current')
cxeCallCtrlT38HsRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlT38HsRedundancy.setStatus('current')
cxeCallCtrlT38NsfCountryCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 17), CountryCodeITU().clone(173)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlT38NsfCountryCode.setStatus('current')
cxeCallCtrlT38NsfVendorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 18), CxeTerminalProviderCode().clone(hexValue="0051")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlT38NsfVendorCode.setStatus('current')
cxeCallCtrlVselDselFselSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 19), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlVselDselFselSupport.setStatus('current')
cxeCallCtrlDefaultBearTraffic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ipPvcAal5", 1), ("atmPvcAal2", 2), ("atmSvcAal2", 3), ("atmSvcAal1", 4))).clone('ipPvcAal5')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxeCallCtrlDefaultBearTraffic.setStatus('current')
cxeCallCtrlLastFailedMgcAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 21), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxeCallCtrlLastFailedMgcAddrType.setStatus('current')
cxeCallCtrlLastFailedMgcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 1, 1, 22), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxeCallCtrlLastFailedMgcAddress.setStatus('current')
cxeCallCtrlProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2), )
if mibBuilder.loadTexts: cxeCallCtrlProfileTable.setStatus('current')
cxeCallCtrlProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"), (0, "CISCO-XGCP-EXT-MIB", "cxeCcProfileIndex"))
if mibBuilder.loadTexts: cxeCallCtrlProfileEntry.setStatus('current')
cxeCcProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 1), CCallControlProfileIndex())
if mibBuilder.loadTexts: cxeCcProfileIndex.setStatus('current')
cxeCcProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileName.setStatus('current')
cxeCcProfileNumVifs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxeCcProfileNumVifs.setStatus('current')
cxeCcProfileMgcGrpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileMgcGrpNum.setStatus('current')
cxeCcProfileMgcAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 5), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileMgcAddrType.setStatus('current')
cxeCcProfileMgcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 6), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileMgcAddress.setStatus('current')
cxeCcProfileProtocolIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileProtocolIdx.setStatus('current')
cxeCcProfileXgcpRetryMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 8), CXgcpRetryMethod().clone('neverResetTimer')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileXgcpRetryMethod.setStatus('current')
cxeCcProfileRetryMax1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileRetryMax1.setStatus('current')
cxeCcProfileDnsLookupMax1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileDnsLookupMax1.setStatus('current')
cxeCcProfileRetryMax2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileRetryMax2.setStatus('current')
cxeCcProfileDnsLookupMax2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 12), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileDnsLookupMax2.setStatus('current')
cxeCcProfileMwiTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(16)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileMwiTimeout.setStatus('current')
cxeCcProfileTsmaxTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(20)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileTsmaxTimeout.setStatus('current')
cxeCcProfileTdinitTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(15)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileTdinitTimeout.setStatus('current')
cxeCcProfileTdminTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(15)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileTdminTimeout.setStatus('current')
cxeCcProfileTdmaxTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(600)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileTdmaxTimeout.setStatus('current')
cxeCcProfileTcritTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(4)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileTcritTimeout.setStatus('current')
cxeCcProfileTparTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(16)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileTparTimeout.setStatus('current')
cxeCcProfileThistTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileThistTimeout.setStatus('current')
cxeCcProfileRtTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(180)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileRtTimeout.setStatus('current')
cxeCcProfileRbkTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(180)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileRbkTimeout.setStatus('current')
cxeCcProfileCgTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(180)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileCgTimeout.setStatus('current')
cxeCcProfileBzTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileBzTimeout.setStatus('current')
cxeCcProfileDlTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(16)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileDlTimeout.setStatus('current')
cxeCcProfileSlTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(16)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileSlTimeout.setStatus('current')
cxeCcProfileRgTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(180)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileRgTimeout.setStatus('current')
cxeCcProfileRoTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileRoTimeout.setStatus('current')
cxeCcProfileCot1Timeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileCot1Timeout.setStatus('current')
cxeCcProfileCot2Timeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileCot2Timeout.setStatus('current')
cxeCcProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 32), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cxeCcProfileRowStatus.setStatus('current')
cxeCallCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 325, 2))
cxeCallCtrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 1))
cxeCallCtrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 2))
cxeCallCtrlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 1, 1)).setObjects(("CISCO-XGCP-EXT-MIB", "cxeCallCtrlGroup"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cxeCallCtrlMIBCompliance = cxeCallCtrlMIBCompliance.setStatus('current')
cxeCallCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 2, 1)).setObjects(("CISCO-XGCP-EXT-MIB", "cxeCallCtrlControlServiceType"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlBearerServiceType"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlVoIpDtmfRelayMode"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlVoIpDtmfCodec"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlVoAal2DtmfRelayMode"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlVoAal2DtmfCodec"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlTsePayload"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlNetNseTimer"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlRtcpRcvTimer"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlIgnoreAal2LcoCodec"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlDigitMapOrder"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlT38Inhibited"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlT38NseRspTimer"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlT38FecEnabled"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlT38LsRedundancy"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlT38HsRedundancy"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlT38NsfCountryCode"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlT38NsfVendorCode"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlVselDselFselSupport"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlDefaultBearTraffic"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlLastFailedMgcAddrType"), ("CISCO-XGCP-EXT-MIB", "cxeCallCtrlLastFailedMgcAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cxeCallCtrlGroup = cxeCallCtrlGroup.setStatus('current')
cxeCcProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 2, 2)).setObjects(("CISCO-XGCP-EXT-MIB", "cxeCcProfileName"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileNumVifs"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileMgcGrpNum"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileMgcAddrType"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileMgcAddress"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileProtocolIdx"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileXgcpRetryMethod"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRetryMax1"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileDnsLookupMax1"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRetryMax2"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileDnsLookupMax2"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileMwiTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTsmaxTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTdinitTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTdminTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTdmaxTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTcritTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTparTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileThistTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRtTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRbkTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileCgTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileBzTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileDlTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileSlTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRgTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRoTimeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileCot1Timeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileCot2Timeout"), ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cxeCcProfileGroup = cxeCcProfileGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-XGCP-EXT-MIB", cxeCcProfileRetryMax2=cxeCcProfileRetryMax2, cxeCcProfileTdmaxTimeout=cxeCcProfileTdmaxTimeout, cxeCcProfileTdminTimeout=cxeCcProfileTdminTimeout, cxeCallCtrlT38FecEnabled=cxeCallCtrlT38FecEnabled, cxeCallCtrlLastFailedMgcAddrType=cxeCallCtrlLastFailedMgcAddrType, cxeCcProfileRgTimeout=cxeCcProfileRgTimeout, cxeCallCtrlT38LsRedundancy=cxeCallCtrlT38LsRedundancy, cxeCcProfileTparTimeout=cxeCcProfileTparTimeout, cxeCallCtrlNetNseTimer=cxeCallCtrlNetNseTimer, cxeCallCtrlGroup=cxeCallCtrlGroup, cxeCallCtrlLastFailedMgcAddress=cxeCallCtrlLastFailedMgcAddress, cxeCcProfileName=cxeCcProfileName, cxeCallCtrlBearerServiceType=cxeCallCtrlBearerServiceType, cxeCcProfileRbkTimeout=cxeCcProfileRbkTimeout, cxeCcProfileTdinitTimeout=cxeCcProfileTdinitTimeout, cxeCcProfileCot2Timeout=cxeCcProfileCot2Timeout, cxeCcProfileRowStatus=cxeCcProfileRowStatus, ciscoXgcpExtMIB=ciscoXgcpExtMIB, cxeCallCtrlIgnoreAal2LcoCodec=cxeCallCtrlIgnoreAal2LcoCodec, cxeCallCtrlProfileTable=cxeCallCtrlProfileTable, cxeCallCtrlMIBCompliance=cxeCallCtrlMIBCompliance, cxeCallCtrlVoIpDtmfRelayMode=cxeCallCtrlVoIpDtmfRelayMode, cxeCallCtrlT38NseRspTimer=cxeCallCtrlT38NseRspTimer, cxeCcProfileMgcAddress=cxeCcProfileMgcAddress, cxgcpExtObjects=cxgcpExtObjects, cxeCallCtrlTsePayload=cxeCallCtrlTsePayload, cxeCcProfileTsmaxTimeout=cxeCcProfileTsmaxTimeout, cxeCallCtrlRtcpRcvTimer=cxeCallCtrlRtcpRcvTimer, cxeCcProfileCot1Timeout=cxeCcProfileCot1Timeout, cxeCcProfileCgTimeout=cxeCcProfileCgTimeout, cxeCallCtrlVselDselFselSupport=cxeCallCtrlVselDselFselSupport, cxeCcProfileIndex=cxeCcProfileIndex, cxeCallCtrlDefaultBearTraffic=cxeCallCtrlDefaultBearTraffic, cxeCallCtrlConfigEntry=cxeCallCtrlConfigEntry, cxeCallCtrlProfileEntry=cxeCallCtrlProfileEntry, cxeCcProfileRtTimeout=cxeCcProfileRtTimeout, cxeCallCtrlMIBCompliances=cxeCallCtrlMIBCompliances, cxeCcProfileMgcAddrType=cxeCcProfileMgcAddrType, cxeCallCtrlVoAal2DtmfRelayMode=cxeCallCtrlVoAal2DtmfRelayMode, cxeCcProfileMwiTimeout=cxeCcProfileMwiTimeout, cxeCcProfileTcritTimeout=cxeCcProfileTcritTimeout, cxeCallCtrlT38NsfCountryCode=cxeCallCtrlT38NsfCountryCode, cxeCallCtrlControlServiceType=cxeCallCtrlControlServiceType, cxeCcProfileDnsLookupMax2=cxeCcProfileDnsLookupMax2, cxeCcProfileGroup=cxeCcProfileGroup, cxgcpExtConfig=cxgcpExtConfig, cxeCcProfileDlTimeout=cxeCcProfileDlTimeout, cxeCcProfileRetryMax1=cxeCcProfileRetryMax1, cxeCallCtrlVoAal2DtmfCodec=cxeCallCtrlVoAal2DtmfCodec, cxeCcProfileXgcpRetryMethod=cxeCcProfileXgcpRetryMethod, cxeCallCtrlDigitMapOrder=cxeCallCtrlDigitMapOrder, cxeCallCtrlT38HsRedundancy=cxeCallCtrlT38HsRedundancy, cxeCcProfileMgcGrpNum=cxeCcProfileMgcGrpNum, cxeCcProfileDnsLookupMax1=cxeCcProfileDnsLookupMax1, cxeCcProfileBzTimeout=cxeCcProfileBzTimeout, cxeCcProfileProtocolIdx=cxeCcProfileProtocolIdx, DtmfRelayMode=DtmfRelayMode, cxeCcProfileRoTimeout=cxeCcProfileRoTimeout, cxeCcProfileThistTimeout=cxeCcProfileThistTimeout, cxeCcProfileSlTimeout=cxeCcProfileSlTimeout, CxeTerminalProviderCode=CxeTerminalProviderCode, cxeCcProfileNumVifs=cxeCcProfileNumVifs, cxeCallCtrlMIBConformance=cxeCallCtrlMIBConformance, cxeCallCtrlMIBGroups=cxeCallCtrlMIBGroups, cxeCallCtrlT38Inhibited=cxeCallCtrlT38Inhibited, PYSNMP_MODULE_ID=ciscoXgcpExtMIB, DtmfCodecType=DtmfCodecType, cxeCallCtrlVoIpDtmfCodec=cxeCallCtrlVoIpDtmfCodec, cxeCallCtrlConfigTable=cxeCallCtrlConfigTable, cxeCallCtrlT38NsfVendorCode=cxeCallCtrlT38NsfVendorCode)

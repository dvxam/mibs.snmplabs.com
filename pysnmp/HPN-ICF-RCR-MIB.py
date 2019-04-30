#
# PySNMP MIB module HPN-ICF-RCR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-RCR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:28:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, NotificationType, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Gauge32, IpAddress, Bits, Unsigned32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "NotificationType", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Gauge32", "IpAddress", "Bits", "Unsigned32", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfRcr = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48))
hpnicfRcr.setRevisions(('2005-06-28 19:36',))
if mibBuilder.loadTexts: hpnicfRcr.setLastUpdated('200506281936Z')
if mibBuilder.loadTexts: hpnicfRcr.setOrganization('')
hpnicfRcrMR = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1))
hpnicfRcrMRGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 1))
hpnicfRcrMRAllMaxUsedBandRate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrMRAllMaxUsedBandRate.setStatus('current')
hpnicfRcrMRAllMinUsedBandRate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrMRAllMinUsedBandRate.setStatus('current')
hpnicfRcrMRListenTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440))).setUnits('minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrMRListenTime.setStatus('current')
hpnicfRcrMRStateTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2), )
if mibBuilder.loadTexts: hpnicfRcrMRStateTable.setStatus('current')
hpnicfRcrMRStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-RCR-MIB", "hpnicfRcrMRName"))
if mibBuilder.loadTexts: hpnicfRcrMRStateEntry.setStatus('current')
hpnicfRcrMRName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpnicfRcrMRName.setStatus('current')
hpnicfRcrMRState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("controlled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrMRState.setStatus('current')
hpnicfRcrMRAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("md5", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrMRAuthType.setStatus('current')
hpnicfRcrMRAuthPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrMRAuthPwd.setStatus('current')
hpnicfRcrMROutIfStateTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3), )
if mibBuilder.loadTexts: hpnicfRcrMROutIfStateTable.setStatus('current')
hpnicfRcrMROutIfStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-RCR-MIB", "hpnicfRcrMRName"), (0, "HPN-ICF-RCR-MIB", "hpnicfRcrMROutIfName"))
if mibBuilder.loadTexts: hpnicfRcrMROutIfStateEntry.setStatus('current')
hpnicfRcrMROutIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 48)))
if mibBuilder.loadTexts: hpnicfRcrMROutIfName.setStatus('current')
hpnicfRcrMROutIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("notExist", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrMROutIfState.setStatus('current')
hpnicfRcrMROutIfMaxUsedBandRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrMROutIfMaxUsedBandRate.setStatus('current')
hpnicfRcrMROutIfMinUsedBandRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrMROutIfMinUsedBandRate.setStatus('current')
hpnicfRcrMROutIfUsedBandRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrMROutIfUsedBandRate.setStatus('current')
hpnicfRcrCR = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2))
hpnicfRcrCRGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1))
hpnicfRcrCRState = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("init", 2), ("active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrCRState.setStatus('current')
hpnicfRcrCRPortNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRPortNum.setStatus('current')
hpnicfRcrCRCtrlMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("control", 1), ("observe", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRCtrlMode.setStatus('current')
hpnicfRcrCRChooseMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("good", 1), ("best", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRChooseMode.setStatus('current')
hpnicfRcrCRKeepaliveTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setUnits('second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRKeepaliveTime.setStatus('current')
hpnicfRcrCRPolicyMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("prefix", 1), ("operation", 2), ("study", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRPolicyMode.setStatus('current')
hpnicfRcrCRStudyMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("maxThoughout", 1), ("maxDelay", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRStudyMode.setStatus('current')
hpnicfRcrCRStudyIpPrefixNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRStudyIpPrefixNum.setStatus('current')
hpnicfRcrCRIpPrefixLen = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)).clone(24)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRIpPrefixLen.setStatus('current')
hpnicfRcrCRRcrPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2), )
if mibBuilder.loadTexts: hpnicfRcrCRRcrPolicyTable.setStatus('current')
hpnicfRcrCRRcrPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRRcrPlyID"))
if mibBuilder.loadTexts: hpnicfRcrCRRcrPolicyEntry.setStatus('current')
hpnicfRcrCRRcrPlyID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfRcrCRRcrPlyID.setStatus('current')
hpnicfRcrCRRcrPlyMatchIPListName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRRcrPlyMatchIPListName.setStatus('current')
hpnicfRcrCRRcrPlyMatchStudyEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRRcrPlyMatchStudyEnable.setStatus('current')
hpnicfRcrCRRcrPlyMatchOperPlyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRRcrPlyMatchOperPlyName.setStatus('current')
hpnicfRcrCRRcrAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3000, 3999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRRcrAclNumber.setStatus('current')
hpnicfRcrCRRcrPlyDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setUnits('millisecond').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRRcrPlyDelayTime.setStatus('current')
hpnicfRcrCRRcrPlyLossRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRcrCRRcrPlyLossRate.setStatus('current')
hpnicfRcrCRMatPrefixPerfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3), )
if mibBuilder.loadTexts: hpnicfRcrCRMatPrefixPerfTable.setStatus('current')
hpnicfRcrCRMatPrefixPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRMatPrefPerfAddrType"), (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRMatPrefPerfDestIPAddr"), (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRMatPrefPerfDestMaskLen"))
if mibBuilder.loadTexts: hpnicfRcrCRMatPrefixPerfEntry.setStatus('current')
hpnicfRcrCRMatPrefPerfAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpnicfRcrCRMatPrefPerfAddrType.setStatus('current')
hpnicfRcrCRMatPrefPerfDestIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 2), InetAddress())
if mibBuilder.loadTexts: hpnicfRcrCRMatPrefPerfDestIPAddr.setStatus('current')
hpnicfRcrCRMatPrefPerfDestMaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)))
if mibBuilder.loadTexts: hpnicfRcrCRMatPrefPerfDestMaskLen.setStatus('current')
hpnicfRcrCRMatPrefPerfDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrCRMatPrefPerfDelayTime.setStatus('current')
hpnicfRcrCRMatPrefPerfLossRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrCRMatPrefPerfLossRate.setStatus('current')
hpnicfRcrCRMatPrefPerfThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 6), Integer32()).setUnits('kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrCRMatPrefPerfThroughput.setStatus('current')
hpnicfRcrCRAdjustPrefixTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4), )
if mibBuilder.loadTexts: hpnicfRcrCRAdjustPrefixTable.setStatus('current')
hpnicfRcrCRAdjustPrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1), ).setIndexNames((0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefDestAddrType"), (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefDestAddr"), (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefMaskLen"), (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefPreMRName"), (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefPreOutIfName"))
if mibBuilder.loadTexts: hpnicfRcrCRAdjustPrefixEntry.setStatus('current')
hpnicfRcrCRAdjuPrefDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpnicfRcrCRAdjuPrefDestAddrType.setStatus('current')
hpnicfRcrCRAdjuPrefDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 2), InetAddress())
if mibBuilder.loadTexts: hpnicfRcrCRAdjuPrefDestAddr.setStatus('current')
hpnicfRcrCRAdjuPrefMaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)))
if mibBuilder.loadTexts: hpnicfRcrCRAdjuPrefMaskLen.setStatus('current')
hpnicfRcrCRAdjuPrefPreMRName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpnicfRcrCRAdjuPrefPreMRName.setStatus('current')
hpnicfRcrCRAdjuPrefPreOutIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 48)))
if mibBuilder.loadTexts: hpnicfRcrCRAdjuPrefPreOutIfName.setStatus('current')
hpnicfRcrCRAdjuPrefCurMRName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrCRAdjuPrefCurMRName.setStatus('current')
hpnicfRcrCRAdjuPrefCurOutIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrCRAdjuPrefCurOutIfName.setStatus('current')
hpnicfRcrCRAdjuPrefPersistTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 8), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrCRAdjuPrefPersistTime.setStatus('current')
hpnicfRcrCRAdjuPrefAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 9), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRcrCRAdjuPrefAgeTime.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-RCR-MIB", hpnicfRcrCRAdjustPrefixTable=hpnicfRcrCRAdjustPrefixTable, hpnicfRcrCRChooseMode=hpnicfRcrCRChooseMode, hpnicfRcrCRAdjuPrefPersistTime=hpnicfRcrCRAdjuPrefPersistTime, hpnicfRcrMROutIfStateEntry=hpnicfRcrMROutIfStateEntry, hpnicfRcrCRAdjuPrefDestAddr=hpnicfRcrCRAdjuPrefDestAddr, hpnicfRcrCRAdjuPrefAgeTime=hpnicfRcrCRAdjuPrefAgeTime, hpnicfRcrMRAuthType=hpnicfRcrMRAuthType, hpnicfRcrMROutIfMaxUsedBandRate=hpnicfRcrMROutIfMaxUsedBandRate, hpnicfRcrCRIpPrefixLen=hpnicfRcrCRIpPrefixLen, hpnicfRcrCRRcrPlyID=hpnicfRcrCRRcrPlyID, hpnicfRcrMRName=hpnicfRcrMRName, hpnicfRcrCRAdjuPrefMaskLen=hpnicfRcrCRAdjuPrefMaskLen, hpnicfRcrCRAdjuPrefPreOutIfName=hpnicfRcrCRAdjuPrefPreOutIfName, PYSNMP_MODULE_ID=hpnicfRcr, hpnicfRcrMRGroup=hpnicfRcrMRGroup, hpnicfRcrCRRcrAclNumber=hpnicfRcrCRRcrAclNumber, hpnicfRcrCRGroup=hpnicfRcrCRGroup, hpnicfRcrMROutIfState=hpnicfRcrMROutIfState, hpnicfRcrCRAdjuPrefDestAddrType=hpnicfRcrCRAdjuPrefDestAddrType, hpnicfRcrCRPolicyMode=hpnicfRcrCRPolicyMode, hpnicfRcrCRRcrPlyMatchStudyEnable=hpnicfRcrCRRcrPlyMatchStudyEnable, hpnicfRcrMROutIfName=hpnicfRcrMROutIfName, hpnicfRcrCRMatPrefPerfThroughput=hpnicfRcrCRMatPrefPerfThroughput, hpnicfRcrCRStudyMode=hpnicfRcrCRStudyMode, hpnicfRcrCRKeepaliveTime=hpnicfRcrCRKeepaliveTime, hpnicfRcrCRRcrPolicyEntry=hpnicfRcrCRRcrPolicyEntry, hpnicfRcrMRStateTable=hpnicfRcrMRStateTable, hpnicfRcrCRMatPrefPerfDelayTime=hpnicfRcrCRMatPrefPerfDelayTime, hpnicfRcrCRCtrlMode=hpnicfRcrCRCtrlMode, hpnicfRcrMROutIfMinUsedBandRate=hpnicfRcrMROutIfMinUsedBandRate, hpnicfRcrCRMatPrefPerfDestMaskLen=hpnicfRcrCRMatPrefPerfDestMaskLen, hpnicfRcrCRRcrPlyMatchIPListName=hpnicfRcrCRRcrPlyMatchIPListName, hpnicfRcrCRPortNum=hpnicfRcrCRPortNum, hpnicfRcrCRAdjuPrefCurMRName=hpnicfRcrCRAdjuPrefCurMRName, hpnicfRcrMROutIfStateTable=hpnicfRcrMROutIfStateTable, hpnicfRcrMROutIfUsedBandRate=hpnicfRcrMROutIfUsedBandRate, hpnicfRcrMRStateEntry=hpnicfRcrMRStateEntry, hpnicfRcrCRAdjuPrefCurOutIfName=hpnicfRcrCRAdjuPrefCurOutIfName, hpnicfRcrCRRcrPlyLossRate=hpnicfRcrCRRcrPlyLossRate, hpnicfRcrCRMatPrefixPerfTable=hpnicfRcrCRMatPrefixPerfTable, hpnicfRcrCR=hpnicfRcrCR, hpnicfRcrCRAdjustPrefixEntry=hpnicfRcrCRAdjustPrefixEntry, hpnicfRcrMRAllMinUsedBandRate=hpnicfRcrMRAllMinUsedBandRate, hpnicfRcr=hpnicfRcr, hpnicfRcrMR=hpnicfRcrMR, hpnicfRcrCRMatPrefPerfLossRate=hpnicfRcrCRMatPrefPerfLossRate, hpnicfRcrMRState=hpnicfRcrMRState, hpnicfRcrMRAllMaxUsedBandRate=hpnicfRcrMRAllMaxUsedBandRate, hpnicfRcrCRAdjuPrefPreMRName=hpnicfRcrCRAdjuPrefPreMRName, hpnicfRcrMRListenTime=hpnicfRcrMRListenTime, hpnicfRcrCRStudyIpPrefixNum=hpnicfRcrCRStudyIpPrefixNum, hpnicfRcrCRRcrPlyMatchOperPlyName=hpnicfRcrCRRcrPlyMatchOperPlyName, hpnicfRcrCRRcrPlyDelayTime=hpnicfRcrCRRcrPlyDelayTime, hpnicfRcrCRState=hpnicfRcrCRState, hpnicfRcrMRAuthPwd=hpnicfRcrMRAuthPwd, hpnicfRcrCRMatPrefPerfDestIPAddr=hpnicfRcrCRMatPrefPerfDestIPAddr, hpnicfRcrCRMatPrefixPerfEntry=hpnicfRcrCRMatPrefixPerfEntry, hpnicfRcrCRRcrPolicyTable=hpnicfRcrCRRcrPolicyTable, hpnicfRcrCRMatPrefPerfAddrType=hpnicfRcrCRMatPrefPerfAddrType)

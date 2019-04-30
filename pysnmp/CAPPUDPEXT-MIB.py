#
# PySNMP MIB module CAPPUDPEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAPPUDPEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
cappUdpExt, = mibBuilder.importSymbols("APENT-MIB", "cappUdpExt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, Counter32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Gauge32, iso, Bits, ModuleIdentity, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Gauge32", "iso", "Bits", "ModuleIdentity", "Counter64", "Integer32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
apCappUdpExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 52, 1))
if mibBuilder.loadTexts: apCappUdpExtMib.setLastUpdated('9707202000Z')
if mibBuilder.loadTexts: apCappUdpExtMib.setOrganization('ArrowPoint Communications Inc.')
apCappUdpState = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 52, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apCappUdpState.setStatus('current')
apCappUdpSecureAll = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 52, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apCappUdpSecureAll.setStatus('current')
apCappUdpPort = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 52, 4), Integer32().clone(5002)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apCappUdpPort.setStatus('current')
apCappUdpDropFrames = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 52, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCappUdpDropFrames.setStatus('current')
apCappUdpReceiveFrames = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 52, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCappUdpReceiveFrames.setStatus('current')
apCappUdpTransmitFrames = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 52, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCappUdpTransmitFrames.setStatus('current')
apCappUdpDropBytes = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 52, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCappUdpDropBytes.setStatus('current')
apCappUdpReceiveBytes = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 52, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCappUdpReceiveBytes.setStatus('current')
apCappUdpTransmitBytes = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 52, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCappUdpTransmitBytes.setStatus('current')
apCappUdpOptionsTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 52, 11), )
if mibBuilder.loadTexts: apCappUdpOptionsTable.setStatus('current')
apCappUdpOptionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1), ).setIndexNames((0, "CAPPUDPEXT-MIB", "apCappUdpOptionsIpAddress"))
if mibBuilder.loadTexts: apCappUdpOptionsEntry.setStatus('current')
apCappUdpOptionsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCappUdpOptionsIpAddress.setStatus('current')
apCappUdpOptionsType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("encrypt-none", 0), ("encrypt-md5", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCappUdpOptionsType.setStatus('current')
apCappUdpOptionsSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCappUdpOptionsSecret.setStatus('current')
apCappUdpOptionsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCappUdpOptionsStatus.setStatus('current')
mibBuilder.exportSymbols("CAPPUDPEXT-MIB", apCappUdpTransmitFrames=apCappUdpTransmitFrames, apCappUdpState=apCappUdpState, apCappUdpOptionsEntry=apCappUdpOptionsEntry, apCappUdpOptionsIpAddress=apCappUdpOptionsIpAddress, apCappUdpTransmitBytes=apCappUdpTransmitBytes, apCappUdpSecureAll=apCappUdpSecureAll, PYSNMP_MODULE_ID=apCappUdpExtMib, apCappUdpExtMib=apCappUdpExtMib, apCappUdpReceiveFrames=apCappUdpReceiveFrames, apCappUdpReceiveBytes=apCappUdpReceiveBytes, apCappUdpOptionsType=apCappUdpOptionsType, apCappUdpPort=apCappUdpPort, apCappUdpOptionsStatus=apCappUdpOptionsStatus, apCappUdpOptionsSecret=apCappUdpOptionsSecret, apCappUdpDropFrames=apCappUdpDropFrames, apCappUdpDropBytes=apCappUdpDropBytes, apCappUdpOptionsTable=apCappUdpOptionsTable)
#
# PySNMP MIB module AT-DHCPSN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-DHCPSN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, Counter64, ObjectIdentity, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Unsigned32, iso, NotificationType, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Counter64", "ObjectIdentity", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Unsigned32", "iso", "NotificationType", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atDhcpsn = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537))
atDhcpsn.setRevisions(('2010-09-07 00:00', '2010-06-14 04:45', '2010-02-09 01:30', '2009-12-10 01:30',))
if mibBuilder.loadTexts: atDhcpsn.setLastUpdated('201009070000Z')
if mibBuilder.loadTexts: atDhcpsn.setOrganization('Allied Telesis, Inc')
atDhcpsnEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 0))
atDhcpsnTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 0, 1)).setObjects(("AT-DHCPSN-MIB", "atDhcpsnIfIndex"), ("AT-DHCPSN-MIB", "atDhcpsnVid"), ("AT-DHCPSN-MIB", "atDhcpsnSmac"), ("AT-DHCPSN-MIB", "atDhcpsnOpcode"), ("AT-DHCPSN-MIB", "atDhcpsnCiaddr"), ("AT-DHCPSN-MIB", "atDhcpsnYiaddr"), ("AT-DHCPSN-MIB", "atDhcpsnGiaddr"), ("AT-DHCPSN-MIB", "atDhcpsnSiaddr"), ("AT-DHCPSN-MIB", "atDhcpsnChaddr"), ("AT-DHCPSN-MIB", "atDhcpsnVioType"))
if mibBuilder.loadTexts: atDhcpsnTrap.setStatus('current')
atArpsecTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 0, 2)).setObjects(("AT-DHCPSN-MIB", "atArpsecIfIndex"), ("AT-DHCPSN-MIB", "atArpsecClientIP"), ("AT-DHCPSN-MIB", "atArpsecSrcMac"), ("AT-DHCPSN-MIB", "atArpsecVid"), ("AT-DHCPSN-MIB", "atArpsecVioType"))
if mibBuilder.loadTexts: atArpsecTrap.setStatus('current')
atDhcpsnVariablesTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1), )
if mibBuilder.loadTexts: atDhcpsnVariablesTable.setStatus('current')
atDhcpsnVariablesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1), ).setIndexNames((0, "AT-DHCPSN-MIB", "atDhcpsnIfIndex"))
if mibBuilder.loadTexts: atDhcpsnVariablesEntry.setStatus('current')
atDhcpsnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnIfIndex.setStatus('current')
atDhcpsnVid = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnVid.setStatus('current')
atDhcpsnSmac = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnSmac.setStatus('current')
atDhcpsnOpcode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bootpRequest", 1), ("bootpReply", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnOpcode.setStatus('current')
atDhcpsnCiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnCiaddr.setStatus('current')
atDhcpsnYiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnYiaddr.setStatus('current')
atDhcpsnGiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnGiaddr.setStatus('current')
atDhcpsnSiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnSiaddr.setStatus('current')
atDhcpsnChaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnChaddr.setStatus('current')
atDhcpsnVioType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("invalidBootp", 1), ("invalidDhcpAck", 2), ("invalidDhcpRelDec", 3), ("invalidIp", 4), ("maxBindExceeded", 5), ("opt82InsertErr", 6), ("opt82RxInvalid", 7), ("opt82RxUntrusted", 8), ("opt82TxUntrusted", 9), ("replyRxUntrusted", 10), ("srcMacChaddrMismatch", 11), ("staticEntryExisted", 12), ("dbAddErr", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnVioType.setStatus('current')
atArpsecVariablesTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2), )
if mibBuilder.loadTexts: atArpsecVariablesTable.setStatus('current')
atArpsecVariablesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1), ).setIndexNames((0, "AT-DHCPSN-MIB", "atArpsecIfIndex"))
if mibBuilder.loadTexts: atArpsecVariablesEntry.setStatus('current')
atArpsecIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecIfIndex.setStatus('current')
atArpsecClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecClientIP.setStatus('current')
atArpsecSrcMac = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecSrcMac.setStatus('current')
atArpsecVid = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecVid.setStatus('current')
atArpsecVioType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("srcIpNotFound", 1), ("badVLAN", 2), ("badPort", 3), ("srcIpNotAllocated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecVioType.setStatus('current')
mibBuilder.exportSymbols("AT-DHCPSN-MIB", atDhcpsn=atDhcpsn, atDhcpsnVariablesTable=atDhcpsnVariablesTable, atDhcpsnYiaddr=atDhcpsnYiaddr, atDhcpsnOpcode=atDhcpsnOpcode, atDhcpsnVioType=atDhcpsnVioType, atArpsecVioType=atArpsecVioType, atDhcpsnIfIndex=atDhcpsnIfIndex, atArpsecClientIP=atArpsecClientIP, atArpsecVid=atArpsecVid, atDhcpsnTrap=atDhcpsnTrap, atArpsecVariablesTable=atArpsecVariablesTable, PYSNMP_MODULE_ID=atDhcpsn, atDhcpsnSmac=atDhcpsnSmac, atDhcpsnCiaddr=atDhcpsnCiaddr, atDhcpsnChaddr=atDhcpsnChaddr, atArpsecIfIndex=atArpsecIfIndex, atDhcpsnVariablesEntry=atDhcpsnVariablesEntry, atDhcpsnVid=atDhcpsnVid, atDhcpsnSiaddr=atDhcpsnSiaddr, atArpsecVariablesEntry=atArpsecVariablesEntry, atArpsecSrcMac=atArpsecSrcMac, atDhcpsnEvents=atDhcpsnEvents, atArpsecTrap=atArpsecTrap, atDhcpsnGiaddr=atDhcpsnGiaddr)

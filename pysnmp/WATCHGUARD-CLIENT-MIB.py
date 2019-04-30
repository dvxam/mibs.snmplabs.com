#
# PySNMP MIB module WATCHGUARD-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WATCHGUARD-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, enterprises, Bits, Gauge32, ObjectIdentity, IpAddress, Counter32, NotificationType, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "Counter32", "NotificationType", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ModuleIdentity", "iso")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-SMI", "watchguard")
wgInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 6))
wgInfoModule.setRevisions(('2007-01-25 12:00',))
if mibBuilder.loadTexts: wgInfoModule.setLastUpdated('200701251200Z')
if mibBuilder.loadTexts: wgInfoModule.setOrganization('WatchGuard Technologies, Inc.')
wgClientMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 6, 2))
if mibBuilder.loadTexts: wgClientMIB.setStatus('current')
wgClientDHCPServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1))
if mibBuilder.loadTexts: wgClientDHCPServer.setStatus('current')
wgClientDHCPClient = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 6, 2, 2))
if mibBuilder.loadTexts: wgClientDHCPClient.setStatus('current')
wgClientPPPoEClient = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3))
if mibBuilder.loadTexts: wgClientPPPoEClient.setStatus('current')
wgClientDHCPServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("relay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerEnable.setStatus('current')
wgClientDHCPServerStartIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerStartIpAddress.setStatus('current')
wgClientDHCPServerEndIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerEndIpAddress.setStatus('current')
wgClientDHCPServerLeaseTime = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerLeaseTime.setStatus('current')
wgClientDHCPServerNum = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerNum.setStatus('current')
wgClientDHCPServerConnTable = MibTable((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6), )
if mibBuilder.loadTexts: wgClientDHCPServerConnTable.setStatus('current')
wgClientDHCPServerRelayServer = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerRelayServer.setStatus('current')
wgClientDHCPServerConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1), ).setIndexNames((0, "WATCHGUARD-CLIENT-MIB", "wgClientDHCPServerConnIPAddr"))
if mibBuilder.loadTexts: wgClientDHCPServerConnEntry.setStatus('current')
wgClientDHCPServerConnClientHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerConnClientHostName.setStatus('current')
wgClientDHCPServerConnIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerConnIPAddr.setStatus('current')
wgClientDHCPServerConnMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerConnMACAddr.setStatus('current')
wgClientDHCPServerConnLeaseTimeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerConnLeaseTimeStart.setStatus('current')
wgClientDHCPServerConnLeaseTimeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPServerConnLeaseTimeEnd.setStatus('current')
wgClientDHCPClientEnable = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPClientEnable.setStatus('current')
wgClientDHCPClientDomainName = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPClientDomainName.setStatus('current')
wgClientDHCPClientDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPClientDefaultGateway.setStatus('current')
wgClientDHCPClientDNSOne = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPClientDNSOne.setStatus('current')
wgClientDHCPClientDNSTwo = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientDHCPClientDNSTwo.setStatus('current')
wgClientPPPoEClientEnable = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientPPPoEClientEnable.setStatus('current')
wgClientPPPoEClientADSLStatus = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disconnect", 0), ("initialize", 1), ("establish", 2), ("authenticate", 3), ("network", 4), ("running", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientPPPoEClientADSLStatus.setStatus('current')
wgClientPPPoEClientLocalIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientPPPoEClientLocalIPAddr.setStatus('current')
wgClientPPPoEClientRemoteIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientPPPoEClientRemoteIPAddr.setStatus('current')
wgClientPPPoEClientNetMask = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientPPPoEClientNetMask.setStatus('current')
wgClientPPPoEClientDNSOne = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientPPPoEClientDNSOne.setStatus('current')
wgClientPPPoEClientDNSTwo = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientPPPoEClientDNSTwo.setStatus('current')
wgClientPPPoEADSLPeerMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientPPPoEADSLPeerMACAddr.setStatus('current')
wgClientPPPoEClientConnTime = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgClientPPPoEClientConnTime.setStatus('current')
mibBuilder.exportSymbols("WATCHGUARD-CLIENT-MIB", wgClientMIB=wgClientMIB, wgClientPPPoEClientEnable=wgClientPPPoEClientEnable, wgClientPPPoEClient=wgClientPPPoEClient, wgClientPPPoEClientNetMask=wgClientPPPoEClientNetMask, wgClientDHCPClientEnable=wgClientDHCPClientEnable, wgClientPPPoEClientDNSTwo=wgClientPPPoEClientDNSTwo, wgClientPPPoEClientADSLStatus=wgClientPPPoEClientADSLStatus, wgClientDHCPClient=wgClientDHCPClient, wgInfoModule=wgInfoModule, wgClientDHCPServerConnIPAddr=wgClientDHCPServerConnIPAddr, wgClientPPPoEClientDNSOne=wgClientPPPoEClientDNSOne, wgClientDHCPServerEnable=wgClientDHCPServerEnable, wgClientPPPoEClientRemoteIPAddr=wgClientPPPoEClientRemoteIPAddr, wgClientDHCPServerConnTable=wgClientDHCPServerConnTable, wgClientDHCPServerLeaseTime=wgClientDHCPServerLeaseTime, wgClientDHCPServerConnClientHostName=wgClientDHCPServerConnClientHostName, wgClientPPPoEClientConnTime=wgClientPPPoEClientConnTime, wgClientDHCPClientDefaultGateway=wgClientDHCPClientDefaultGateway, wgClientDHCPServerStartIpAddress=wgClientDHCPServerStartIpAddress, wgClientDHCPServerConnEntry=wgClientDHCPServerConnEntry, wgClientDHCPClientDNSTwo=wgClientDHCPClientDNSTwo, wgClientDHCPServerEndIpAddress=wgClientDHCPServerEndIpAddress, wgClientDHCPServerConnMACAddr=wgClientDHCPServerConnMACAddr, wgClientDHCPClientDNSOne=wgClientDHCPClientDNSOne, wgClientPPPoEClientLocalIPAddr=wgClientPPPoEClientLocalIPAddr, wgClientDHCPServerRelayServer=wgClientDHCPServerRelayServer, wgClientDHCPServerConnLeaseTimeEnd=wgClientDHCPServerConnLeaseTimeEnd, wgClientDHCPServerNum=wgClientDHCPServerNum, wgClientDHCPServer=wgClientDHCPServer, PYSNMP_MODULE_ID=wgInfoModule, wgClientDHCPServerConnLeaseTimeStart=wgClientDHCPServerConnLeaseTimeStart, wgClientDHCPClientDomainName=wgClientDHCPClientDomainName, wgClientPPPoEADSLPeerMACAddr=wgClientPPPoEADSLPeerMACAddr)

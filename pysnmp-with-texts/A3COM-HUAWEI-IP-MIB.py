#
# PySNMP MIB module A3COM-HUAWEI-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-IP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
hwLocal, hwInternetProtocol, huawei = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "hwLocal", "hwInternetProtocol", "huawei")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Integer32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Integer32", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rIp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1))
ipTooShorts = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTooShorts.setStatus('mandatory')
if mibBuilder.loadTexts: ipTooShorts.setDescription('The number of packets with invalid data length.')
ipTooSmalls = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTooSmalls.setStatus('mandatory')
if mibBuilder.loadTexts: ipTooSmalls.setDescription('The number of packets too small to contain IP packet.')
ipBadVersions = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadVersions.setStatus('mandatory')
if mibBuilder.loadTexts: ipBadVersions.setDescription('The number of packets with an IP version other than 4.')
ipBadChecksums = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadChecksums.setStatus('mandatory')
if mibBuilder.loadTexts: ipBadChecksums.setDescription('The number of packets with bad checksum.')
ipBadLens = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadLens.setStatus('mandatory')
if mibBuilder.loadTexts: ipBadLens.setDescription('The number of packets with invalid IP length.')
ipBadHeadLens = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadHeadLens.setStatus('mandatory')
if mibBuilder.loadTexts: ipBadHeadLens.setDescription('The number of packets with invalid IP header length.')
ipBadOptions = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipBadOptions.setStatus('mandatory')
if mibBuilder.loadTexts: ipBadOptions.setDescription('The number of packets discovered with errors in option processing.')
ipFragDroppeds = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFragDroppeds.setStatus('mandatory')
if mibBuilder.loadTexts: ipFragDroppeds.setDescription('The number of fragments dropped(duplicates or out of space).')
ipRawOuts = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRawOuts.setStatus('mandatory')
if mibBuilder.loadTexts: ipRawOuts.setDescription('The total number of raw ip packets generated.')
ipRouteBadRedirects = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteBadRedirects.setStatus('mandatory')
if mibBuilder.loadTexts: ipRouteBadRedirects.setDescription('The number of invalid redirect calls.')
ipRouteDynamics = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteDynamics.setStatus('mandatory')
if mibBuilder.loadTexts: ipRouteDynamics.setDescription('The number of routes created by redirects.')
ipRouteNewGateways = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteNewGateways.setStatus('mandatory')
if mibBuilder.loadTexts: ipRouteNewGateways.setDescription('The number of routes modified by redirects.')
ipRouteUnreachs = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteUnreachs.setStatus('mandatory')
if mibBuilder.loadTexts: ipRouteUnreachs.setDescription('The number of lookups that failed.')
ipRouteWilds = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteWilds.setStatus('mandatory')
if mibBuilder.loadTexts: ipRouteWilds.setDescription('The number of lookups matched by wildcard(never used.)')
mibBuilder.exportSymbols("A3COM-HUAWEI-IP-MIB", ipBadLens=ipBadLens, ipFragDroppeds=ipFragDroppeds, rIp=rIp, ipTooSmalls=ipTooSmalls, ipBadOptions=ipBadOptions, ipRouteBadRedirects=ipRouteBadRedirects, ipBadChecksums=ipBadChecksums, ipRawOuts=ipRawOuts, ipRouteDynamics=ipRouteDynamics, ipTooShorts=ipTooShorts, ipRouteWilds=ipRouteWilds, ipRouteNewGateways=ipRouteNewGateways, ipBadHeadLens=ipBadHeadLens, ipRouteUnreachs=ipRouteUnreachs, ipBadVersions=ipBadVersions)

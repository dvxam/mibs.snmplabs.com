#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:06:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
lhnModules, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnModules")
lhnNusCommonDNS, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonDNS")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, ModuleIdentity, TimeTicks, Counter64, Gauge32, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "MibIdentifier", "NotificationType", "Integer32")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
lhnNusCommonDNSModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1, 1, 3))
if mibBuilder.loadTexts: lhnNusCommonDNSModule.setLastUpdated('0106010000Z')
if mibBuilder.loadTexts: lhnNusCommonDNSModule.setOrganization('LeftHand Networks, Inc.')
if mibBuilder.loadTexts: lhnNusCommonDNSModule.setContactInfo(' Author: Jose Faria LeftHand Networks postal: 6185 Arapahoe Rd. Boulder, CO 80301 USA email: jfaria@lefthandnetworks.com phone: +1 303 449-4100 ')
if mibBuilder.loadTexts: lhnNusCommonDNSModule.setDescription('DNS items for NUS Devices')
dnsNameserverCount = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsNameserverCount.setStatus('current')
if mibBuilder.loadTexts: dnsNameserverCount.setDescription('Number of name servers for the NUS to use')
dnsMode = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("auto", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsMode.setStatus('current')
if mibBuilder.loadTexts: dnsMode.setDescription("Type of name servers to use. dnsNameserverCount would be zero if dnsMode is 'auto'")
dnsDomainName = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsDomainName.setStatus('current')
if mibBuilder.loadTexts: dnsDomainName.setDescription('dns domain name')
dnsNameserverTable = MibTable((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3), )
if mibBuilder.loadTexts: dnsNameserverTable.setStatus('current')
if mibBuilder.loadTexts: dnsNameserverTable.setDescription('A table of nameserver parameters for the NUS. The number of entries is given by dnsNameserverCount.')
dnsNameserverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1), ).setIndexNames((0, "LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB", "dnsIndex"))
if mibBuilder.loadTexts: dnsNameserverEntry.setStatus('current')
if mibBuilder.loadTexts: dnsNameserverEntry.setDescription('A row of dns server for the NUS.')
dnsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsIndex.setStatus('current')
if mibBuilder.loadTexts: dnsIndex.setDescription('index of nameserver')
dnsServer = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServer.setStatus('current')
if mibBuilder.loadTexts: dnsServer.setDescription('Server name or IP Address of nameserver')
dnsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsRowStatus.setStatus('current')
if mibBuilder.loadTexts: dnsRowStatus.setDescription('The row status')
dnsSuffixCount = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsSuffixCount.setStatus('current')
if mibBuilder.loadTexts: dnsSuffixCount.setDescription('Number of dns suffixes for the NUS to use')
dnsSuffixTable = MibTable((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6), )
if mibBuilder.loadTexts: dnsSuffixTable.setStatus('current')
if mibBuilder.loadTexts: dnsSuffixTable.setDescription('A table of domain suffixes for the NUS. The number of entries is given by dnsSuffixCount.')
dnsSuffixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1), ).setIndexNames((0, "LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB", "dnsSuffixIndex"))
if mibBuilder.loadTexts: dnsSuffixEntry.setStatus('current')
if mibBuilder.loadTexts: dnsSuffixEntry.setDescription('A row of dns suffix for the NUS.')
dnsSuffixIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsSuffixIndex.setStatus('current')
if mibBuilder.loadTexts: dnsSuffixIndex.setDescription('index of nameserver')
dnsSuffix = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsSuffix.setStatus('current')
if mibBuilder.loadTexts: dnsSuffix.setDescription('dns suffix')
dnsSuffixRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsSuffixRowStatus.setStatus('current')
if mibBuilder.loadTexts: dnsSuffixRowStatus.setDescription('The row status')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB", lhnNusCommonDNSModule=lhnNusCommonDNSModule, dnsMode=dnsMode, dnsSuffixTable=dnsSuffixTable, dnsDomainName=dnsDomainName, dnsNameserverEntry=dnsNameserverEntry, dnsNameserverCount=dnsNameserverCount, dnsSuffixIndex=dnsSuffixIndex, dnsIndex=dnsIndex, dnsSuffixCount=dnsSuffixCount, dnsSuffixEntry=dnsSuffixEntry, dnsRowStatus=dnsRowStatus, dnsSuffix=dnsSuffix, PYSNMP_MODULE_ID=lhnNusCommonDNSModule, dnsNameserverTable=dnsNameserverTable, dnsSuffixRowStatus=dnsSuffixRowStatus, dnsServer=dnsServer)
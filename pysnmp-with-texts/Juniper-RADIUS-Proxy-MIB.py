#
# PySNMP MIB module Juniper-RADIUS-Proxy-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-RADIUS-Proxy-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:04:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, iso, IpAddress, ModuleIdentity, Integer32, TimeTicks, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Counter64, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "IpAddress", "ModuleIdentity", "Integer32", "TimeTicks", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Counter64", "Unsigned32", "NotificationType")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
juniRadiusProxyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73))
juniRadiusProxyMIB.setRevisions(('2004-01-23 19:32',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniRadiusProxyMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniRadiusProxyMIB.setLastUpdated('200401231932Z')
if mibBuilder.loadTexts: juniRadiusProxyMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniRadiusProxyMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniRadiusProxyMIB.setDescription('The RADIUS Proxy MIB for the Juniper Networks enterprise.')
juniRadiusProxyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1))
juniRadiusGeneralProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 1))
juniRadiusAuthProxyCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2))
juniRadiusAcctProxyCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3))
juniRadiusProxyUdpChecksum = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRadiusProxyUdpChecksum.setStatus('current')
if mibBuilder.loadTexts: juniRadiusProxyUdpChecksum.setDescription('Enables/disables the checksum calculations on RADIUS UDP packets.')
juniRadiusAuthProxyCfgPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgPortNumber.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgPortNumber.setDescription('The UDP port the RADIUS authentication proxy server will use. The server will first be created, if necessary. A value of 0 indicates the server should be deleted.')
juniRadiusAuthProxyCfgClientTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2), )
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientTable.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientTable.setDescription('The table listing the clients with which the RADIUS authentication proxy server shares a secret.')
juniRadiusAuthProxyCfgClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1), ).setIndexNames((0, "Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgClientAddress"), (0, "Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgClientMask"))
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientEntry.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientEntry.setDescription('An entry (row) representing clients with which the RADIUS authentication proxy server shares a secret.')
juniRadiusAuthProxyCfgClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientAddress.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientAddress.setDescription("The IP Network Address of the RADIUS authentication proxy server's clients.")
juniRadiusAuthProxyCfgClientMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientMask.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientMask.setDescription("The IP Network Address Mask of the RADIUS authentication proxy server's clients.")
juniRadiusAuthProxyCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgRowStatus.setDescription("Supports 'createAndGo' and 'destroy' only.")
juniRadiusAuthProxyCfgClientKey = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientKey.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAuthProxyCfgClientKey.setDescription('The secret (RADIUS authenticator) used by the clients during exchanges with this authentication proxy server.')
juniRadiusAcctProxyCfgPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgPortNumber.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgPortNumber.setDescription('The UDP port the RADIUS accounting proxy server will use. The server will first be created, if necessary. A value of 0 indicates the server should be deleted.')
juniRadiusAcctProxyCfgClientTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2), )
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientTable.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientTable.setDescription('The table listing the clients with which the RADIUS accounting proxy server shares a secret.')
juniRadiusAcctProxyCfgClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1), ).setIndexNames((0, "Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgClientAddress"), (0, "Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgClientMask"))
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientEntry.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientEntry.setDescription('An entry (row) representing clients with which the RADIUS accounting proxy server shares a secret.')
juniRadiusAcctProxyCfgClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientAddress.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientAddress.setDescription("The IP Network Address of the RADIUS accounting proxy server's clients.")
juniRadiusAcctProxyCfgClientMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientMask.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientMask.setDescription("The IP Network Address Mask of the RADIUS accounting proxy server's clients.")
juniRadiusAcctProxyCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgRowStatus.setDescription("Supports 'createAndGo' and 'destroy' only.")
juniRadiusAcctProxyCfgClientKey = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientKey.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAcctProxyCfgClientKey.setDescription('The secret (RADIUS authenticator) used by the clients during exchanges with this accounting proxy server.')
juniRadiusProxyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2))
juniRadiusProxyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 1))
juniRadiusProxyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 2))
juniRadiusProxyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 1, 1)).setObjects(("Juniper-RADIUS-Proxy-MIB", "juniRadiusBasicProxyGroup"), ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyGroup"), ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusProxyCompliance = juniRadiusProxyCompliance.setStatus('current')
if mibBuilder.loadTexts: juniRadiusProxyCompliance.setDescription('The compliance statement for entities implementing the JUNOSe RADIUS Proxy Server MIB functionality.')
juniRadiusBasicProxyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 2, 1)).setObjects(("Juniper-RADIUS-Proxy-MIB", "juniRadiusProxyUdpChecksum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusBasicProxyGroup = juniRadiusBasicProxyGroup.setStatus('current')
if mibBuilder.loadTexts: juniRadiusBasicProxyGroup.setDescription('A collection of objects providing basic management of RADIUS Proxy Servers.')
juniRadiusAuthProxyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 2, 2)).setObjects(("Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgPortNumber"), ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgRowStatus"), ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgClientKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusAuthProxyGroup = juniRadiusAuthProxyGroup.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAuthProxyGroup.setDescription('A collection of objects providing management of RADIUS Authentication Proxy Servers.')
juniRadiusAcctProxyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 2, 3)).setObjects(("Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgPortNumber"), ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgRowStatus"), ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgClientKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusAcctProxyGroup = juniRadiusAcctProxyGroup.setStatus('current')
if mibBuilder.loadTexts: juniRadiusAcctProxyGroup.setDescription('A collection of objects providing management of RADIUS Accounting Proxy Servers.')
mibBuilder.exportSymbols("Juniper-RADIUS-Proxy-MIB", juniRadiusAcctProxyCfgClientTable=juniRadiusAcctProxyCfgClientTable, juniRadiusProxyMIBCompliances=juniRadiusProxyMIBCompliances, juniRadiusAcctProxyCfgClientKey=juniRadiusAcctProxyCfgClientKey, juniRadiusAcctProxyCfgPortNumber=juniRadiusAcctProxyCfgPortNumber, juniRadiusAuthProxyCfgClientAddress=juniRadiusAuthProxyCfgClientAddress, juniRadiusAuthProxyCfgRowStatus=juniRadiusAuthProxyCfgRowStatus, juniRadiusAuthProxyCfgClientMask=juniRadiusAuthProxyCfgClientMask, juniRadiusAuthProxyCfgClientEntry=juniRadiusAuthProxyCfgClientEntry, juniRadiusAcctProxyCfgClientEntry=juniRadiusAcctProxyCfgClientEntry, juniRadiusProxyMIBConformance=juniRadiusProxyMIBConformance, juniRadiusProxyMIBGroups=juniRadiusProxyMIBGroups, juniRadiusBasicProxyGroup=juniRadiusBasicProxyGroup, juniRadiusProxyMIB=juniRadiusProxyMIB, juniRadiusAuthProxyCfgClientTable=juniRadiusAuthProxyCfgClientTable, juniRadiusAcctProxyCfgClientMask=juniRadiusAcctProxyCfgClientMask, juniRadiusProxyUdpChecksum=juniRadiusProxyUdpChecksum, PYSNMP_MODULE_ID=juniRadiusProxyMIB, juniRadiusAcctProxyCfgRowStatus=juniRadiusAcctProxyCfgRowStatus, juniRadiusAcctProxyCfgClientAddress=juniRadiusAcctProxyCfgClientAddress, juniRadiusAuthProxyCfgClientKey=juniRadiusAuthProxyCfgClientKey, juniRadiusAcctProxyCfg=juniRadiusAcctProxyCfg, juniRadiusProxyCompliance=juniRadiusProxyCompliance, juniRadiusAuthProxyCfg=juniRadiusAuthProxyCfg, juniRadiusAuthProxyCfgPortNumber=juniRadiusAuthProxyCfgPortNumber, juniRadiusAcctProxyGroup=juniRadiusAcctProxyGroup, juniRadiusGeneralProxy=juniRadiusGeneralProxy, juniRadiusAuthProxyGroup=juniRadiusAuthProxyGroup, juniRadiusProxyObjects=juniRadiusProxyObjects)

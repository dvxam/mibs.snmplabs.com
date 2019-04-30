#
# PySNMP MIB module HPN-ICF-NVGRE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-NVGRE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:28:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, ModuleIdentity, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, TimeTicks, Bits, NotificationType, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "TimeTicks", "Bits", "NotificationType", "iso", "Integer32", "Gauge32")
TextualConvention, RowStatus, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "MacAddress")
hpnicfNvgre = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156))
hpnicfNvgre.setRevisions(('2014-03-11 09:00',))
if mibBuilder.loadTexts: hpnicfNvgre.setLastUpdated('201403110900Z')
if mibBuilder.loadTexts: hpnicfNvgre.setOrganization('')
hpnicfNvgreObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1))
hpnicfNvgreScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 1))
hpnicfNvgreNextNvgreID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNvgreNextNvgreID.setStatus('current')
hpnicfNvgreConfigured = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNvgreConfigured.setStatus('current')
hpnicfNvgreTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2), )
if mibBuilder.loadTexts: hpnicfNvgreTable.setStatus('current')
hpnicfNvgreEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreID"))
if mibBuilder.loadTexts: hpnicfNvgreEntry.setStatus('current')
hpnicfNvgreID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfNvgreID.setStatus('current')
hpnicfNvgreVsiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNvgreVsiIndex.setStatus('current')
hpnicfNvgreRemoteMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNvgreRemoteMacCount.setStatus('current')
hpnicfNvgreRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNvgreRowStatus.setStatus('current')
hpnicfNvgreTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3), )
if mibBuilder.loadTexts: hpnicfNvgreTunnelTable.setStatus('current')
hpnicfNvgreTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreID"), (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreTunnelID"))
if mibBuilder.loadTexts: hpnicfNvgreTunnelEntry.setStatus('current')
hpnicfNvgreTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfNvgreTunnelID.setStatus('current')
hpnicfNvgreTunnelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNvgreTunnelRowStatus.setStatus('current')
hpnicfNvgreTunnelOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNvgreTunnelOctets.setStatus('current')
hpnicfNvgreTunnelPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNvgreTunnelPackets.setStatus('current')
hpnicfNvgreTunnelBoundTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 4), )
if mibBuilder.loadTexts: hpnicfNvgreTunnelBoundTable.setStatus('current')
hpnicfNvgreTunnelBoundEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 4, 1), ).setIndexNames((0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreTunnelID"))
if mibBuilder.loadTexts: hpnicfNvgreTunnelBoundEntry.setStatus('current')
hpnicfNvgreTunnelBoundNvgreNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNvgreTunnelBoundNvgreNum.setStatus('current')
hpnicfNvgreMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5), )
if mibBuilder.loadTexts: hpnicfNvgreMacTable.setStatus('current')
hpnicfNvgreMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5, 1), ).setIndexNames((0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreVsiIndex"), (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreMacAddr"))
if mibBuilder.loadTexts: hpnicfNvgreMacEntry.setStatus('current')
hpnicfNvgreMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfNvgreMacAddr.setStatus('current')
hpnicfNvgreMacTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNvgreMacTunnelID.setStatus('current')
hpnicfNvgreMacType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("selfLearned", 1), ("staticConfigured", 2), ("protocolLearned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNvgreMacType.setStatus('current')
hpnicfNvgreStaticMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6), )
if mibBuilder.loadTexts: hpnicfNvgreStaticMacTable.setStatus('current')
hpnicfNvgreStaticMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6, 1), ).setIndexNames((0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreVsiIndex"), (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreStaticMacAddr"))
if mibBuilder.loadTexts: hpnicfNvgreStaticMacEntry.setStatus('current')
hpnicfNvgreStaticMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfNvgreStaticMacAddr.setStatus('current')
hpnicfNvgreStaticMacTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNvgreStaticMacTunnelID.setStatus('current')
hpnicfNvgreStaticMacRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNvgreStaticMacRowStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-NVGRE-MIB", hpnicfNvgreStaticMacTunnelID=hpnicfNvgreStaticMacTunnelID, hpnicfNvgreStaticMacRowStatus=hpnicfNvgreStaticMacRowStatus, hpnicfNvgreStaticMacAddr=hpnicfNvgreStaticMacAddr, hpnicfNvgreID=hpnicfNvgreID, hpnicfNvgreTunnelOctets=hpnicfNvgreTunnelOctets, hpnicfNvgreTunnelPackets=hpnicfNvgreTunnelPackets, hpnicfNvgreStaticMacEntry=hpnicfNvgreStaticMacEntry, hpnicfNvgreMacTunnelID=hpnicfNvgreMacTunnelID, hpnicfNvgreRemoteMacCount=hpnicfNvgreRemoteMacCount, hpnicfNvgreConfigured=hpnicfNvgreConfigured, hpnicfNvgreStaticMacTable=hpnicfNvgreStaticMacTable, PYSNMP_MODULE_ID=hpnicfNvgre, hpnicfNvgreMacAddr=hpnicfNvgreMacAddr, hpnicfNvgreTunnelEntry=hpnicfNvgreTunnelEntry, hpnicfNvgreVsiIndex=hpnicfNvgreVsiIndex, hpnicfNvgreMacType=hpnicfNvgreMacType, hpnicfNvgreTunnelBoundEntry=hpnicfNvgreTunnelBoundEntry, hpnicfNvgreEntry=hpnicfNvgreEntry, hpnicfNvgreTunnelID=hpnicfNvgreTunnelID, hpnicfNvgreNextNvgreID=hpnicfNvgreNextNvgreID, hpnicfNvgre=hpnicfNvgre, hpnicfNvgreMacTable=hpnicfNvgreMacTable, hpnicfNvgreObjects=hpnicfNvgreObjects, hpnicfNvgreMacEntry=hpnicfNvgreMacEntry, hpnicfNvgreTunnelBoundTable=hpnicfNvgreTunnelBoundTable, hpnicfNvgreScalarGroup=hpnicfNvgreScalarGroup, hpnicfNvgreRowStatus=hpnicfNvgreRowStatus, hpnicfNvgreTunnelTable=hpnicfNvgreTunnelTable, hpnicfNvgreTunnelBoundNvgreNum=hpnicfNvgreTunnelBoundNvgreNum, hpnicfNvgreTunnelRowStatus=hpnicfNvgreTunnelRowStatus, hpnicfNvgreTable=hpnicfNvgreTable)
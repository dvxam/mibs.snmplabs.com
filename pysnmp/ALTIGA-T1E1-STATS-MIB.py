#
# PySNMP MIB module ALTIGA-T1E1-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-T1E1-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alT1E1MibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alT1E1MibModule")
alStatsT1E1, alT1E1Group = mibBuilder.importSymbols("ALTIGA-MIB", "alStatsT1E1", "alT1E1Group")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, NotificationType, Counter32, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, TimeTicks, Bits, Gauge32, ModuleIdentity, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "TimeTicks", "Bits", "Gauge32", "ModuleIdentity", "Unsigned32", "MibIdentifier")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
altigaT1E1StatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 38, 2))
altigaT1E1StatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaT1E1StatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaT1E1StatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsT1E1Global = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 1))
alT1E1StatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2), )
if mibBuilder.loadTexts: alT1E1StatsTable.setStatus('current')
alT1E1StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1), ).setIndexNames((0, "ALTIGA-T1E1-STATS-MIB", "alT1E1StatsSlot"), (0, "ALTIGA-T1E1-STATS-MIB", "alT1E1StatsConn"))
if mibBuilder.loadTexts: alT1E1StatsEntry.setStatus('current')
alT1E1StatsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alT1E1StatsRowStatus.setStatus('current')
alT1E1StatsSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsSlot.setStatus('current')
alT1E1StatsConn = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsConn.setStatus('current')
alT1E1StatsLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("init", 1), ("up", 2), ("red", 3), ("blue", 4), ("yellow", 5), ("loopback", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsLineStatus.setStatus('current')
alT1E1StatsElapsedSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsElapsedSecs.setStatus('current')
alT1E1StatsBPVs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsBPVs.setStatus('current')
alT1E1StatsESs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsESs.setStatus('current')
alT1E1StatsSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsSESs.setStatus('current')
alT1E1StatsBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsBESs.setStatus('current')
alT1E1StatsSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsSEFSs.setStatus('current')
alT1E1StatsUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsUASs.setStatus('current')
alT1E1StatsLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsLCVs.setStatus('current')
alT1E1StatsCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsCSSs.setStatus('current')
alT1E1StatsDMs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsDMs.setStatus('current')
alT1E1StatsPCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsPCVs.setStatus('current')
alT1E1StatsLESs = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alT1E1StatsLESs.setStatus('current')
altigaT1E1StatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 38, 2, 1))
altigaT1E1StatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 38, 2, 1, 1))
altigaT1E1StatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 38, 2, 1, 1, 1)).setObjects(("ALTIGA-T1E1-STATS-MIB", "altigaT1E1StatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaT1E1StatsMibCompliance = altigaT1E1StatsMibCompliance.setStatus('current')
altigaT1E1StatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 33, 2)).setObjects(("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsRowStatus"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsSlot"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsConn"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsLineStatus"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsElapsedSecs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsBPVs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsESs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsSESs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsBESs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsSEFSs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsUASs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsLCVs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsCSSs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsDMs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsPCVs"), ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsLESs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaT1E1StatsGroup = altigaT1E1StatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-T1E1-STATS-MIB", altigaT1E1StatsMibCompliance=altigaT1E1StatsMibCompliance, altigaT1E1StatsMibModule=altigaT1E1StatsMibModule, alT1E1StatsBPVs=alT1E1StatsBPVs, PYSNMP_MODULE_ID=altigaT1E1StatsMibModule, alT1E1StatsESs=alT1E1StatsESs, alT1E1StatsRowStatus=alT1E1StatsRowStatus, altigaT1E1StatsGroup=altigaT1E1StatsGroup, alT1E1StatsSlot=alT1E1StatsSlot, alT1E1StatsLESs=alT1E1StatsLESs, altigaT1E1StatsMibCompliances=altigaT1E1StatsMibCompliances, alT1E1StatsSESs=alT1E1StatsSESs, alT1E1StatsUASs=alT1E1StatsUASs, alT1E1StatsElapsedSecs=alT1E1StatsElapsedSecs, altigaT1E1StatsMibConformance=altigaT1E1StatsMibConformance, alStatsT1E1Global=alStatsT1E1Global, alT1E1StatsCSSs=alT1E1StatsCSSs, alT1E1StatsLineStatus=alT1E1StatsLineStatus, alT1E1StatsTable=alT1E1StatsTable, alT1E1StatsDMs=alT1E1StatsDMs, alT1E1StatsConn=alT1E1StatsConn, alT1E1StatsSEFSs=alT1E1StatsSEFSs, alT1E1StatsPCVs=alT1E1StatsPCVs, alT1E1StatsEntry=alT1E1StatsEntry, alT1E1StatsBESs=alT1E1StatsBESs, alT1E1StatsLCVs=alT1E1StatsLCVs)

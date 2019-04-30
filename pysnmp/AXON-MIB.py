#
# PySNMP MIB module AXON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AXON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:16:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ModuleIdentity, Gauge32, ObjectIdentity, MibIdentifier, Bits, Counter32, Unsigned32, iso, Integer32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ModuleIdentity", "Gauge32", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "Unsigned32", "iso", "Integer32", "NotificationType", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
directory = MibIdentifier((1, 3, 6, 1, 1))
mgmt = MibIdentifier((1, 3, 6, 1, 2))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
mib_2 = MibIdentifier((1, 3, 6, 1, 2, 1)).setLabel("mib-2")
axon = MibIdentifier((1, 3, 6, 1, 4, 1, 370))
clone = MibIdentifier((1, 3, 6, 1, 4, 1, 370, 1))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 370, 2))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 370, 2, 1))
application = MibIdentifier((1, 3, 6, 1, 4, 1, 370, 3))
axFddi = MibIdentifier((1, 3, 6, 1, 4, 1, 370, 4))
axFddiStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 370, 4, 1))
axFddiHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 370, 4, 2))
fddiStatsTable = MibTable((1, 3, 6, 1, 4, 1, 370, 4, 1, 1), )
if mibBuilder.loadTexts: fddiStatsTable.setStatus('mandatory')
fddiStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1), ).setIndexNames((0, "AXON-MIB", "fddiStatsIndex"))
if mibBuilder.loadTexts: fddiStatsEntry.setStatus('mandatory')
fddiStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsIndex.setStatus('mandatory')
fddiStatsDataSource = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddiStatsDataSource.setStatus('mandatory')
fddiStatsDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsDropEvents.setStatus('mandatory')
fddiStatsOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsOctets.setStatus('mandatory')
fddiStatsPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts.setStatus('mandatory')
fddiStatsBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsBroadcastPkts.setStatus('mandatory')
fddiStatsMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsMulticastPkts.setStatus('mandatory')
fddiStatsErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsErrors.setStatus('mandatory')
fddiStatsPkts22Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts22Octets.setStatus('mandatory')
fddiStatsPkts23to63Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts23to63Octets.setStatus('mandatory')
fddiStatsPkts64to127Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts64to127Octets.setStatus('mandatory')
fddiStatsPkts128to255Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts128to255Octets.setStatus('mandatory')
fddiStatsPkts256to511Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts256to511Octets.setStatus('mandatory')
fddiStatsPkts512to1023Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts512to1023Octets.setStatus('mandatory')
fddiStatsPkts1024to2047Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts1024to2047Octets.setStatus('mandatory')
fddiStatsPkts2048to4095Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts2048to4095Octets.setStatus('mandatory')
fddiStatsPkts4096to4500Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsPkts4096to4500Octets.setStatus('mandatory')
fddiStatsTNEG = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsTNEG.setStatus('mandatory')
fddiStatsTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsTokens.setStatus('mandatory')
fddiStatsSMTs = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsSMTs.setStatus('mandatory')
fddiStatsClaims = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsClaims.setStatus('mandatory')
fddiStatsDirBeacons = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsDirBeacons.setStatus('mandatory')
fddiStatsBeacons = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsBeacons.setStatus('mandatory')
fddiStatsBeaconAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 24), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsBeaconAddr.setStatus('mandatory')
fddiStatsDirBeaconAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 25), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsDirBeaconAddr.setStatus('mandatory')
fddiStatsClaimAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 26), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsClaimAddr.setStatus('mandatory')
fddiStatsRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsRingState.setStatus('mandatory')
fddiStatsOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 28), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddiStatsOwner.setStatus('mandatory')
fddiStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 29), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddiStatsStatus.setStatus('mandatory')
fddiStatsOtherPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsOtherPkts.setStatus('mandatory')
fddiStatsOtherOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiStatsOtherOctets.setStatus('mandatory')
fddiHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 370, 4, 2, 5), )
if mibBuilder.loadTexts: fddiHistoryTable.setStatus('mandatory')
fddiHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1), ).setIndexNames((0, "AXON-MIB", "fddiHistoryIndex"), (0, "AXON-MIB", "fddiHistorySampleIndex"))
if mibBuilder.loadTexts: fddiHistoryEntry.setStatus('mandatory')
fddiHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryIndex.setStatus('mandatory')
fddiHistorySampleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistorySampleIndex.setStatus('mandatory')
fddiHistoryIntervalStart = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryIntervalStart.setStatus('mandatory')
fddiHistoryDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryDropEvents.setStatus('mandatory')
fddiHistoryOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryOctets.setStatus('mandatory')
fddiHistoryPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts.setStatus('mandatory')
fddiHistoryBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryBroadcastPkts.setStatus('mandatory')
fddiHistoryMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryMulticastPkts.setStatus('mandatory')
fddiHistoryErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryErrors.setStatus('mandatory')
fddiHistoryPkts22Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts22Octets.setStatus('mandatory')
fddiHistoryPkts23to63Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts23to63Octets.setStatus('mandatory')
fddiHistoryPkts64to127Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts64to127Octets.setStatus('mandatory')
fddiHistoryPkts128to255Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts128to255Octets.setStatus('mandatory')
fddiHistoryPkts256to511Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts256to511Octets.setStatus('mandatory')
fddiHistoryPkts512to1023Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts512to1023Octets.setStatus('mandatory')
fddiHistoryPkts1024to2047Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts1024to2047Octets.setStatus('mandatory')
fddiHistoryPkts2048to4095Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts2048to4095Octets.setStatus('mandatory')
fddiHistoryPkts4096to4500Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryPkts4096to4500Octets.setStatus('mandatory')
fddiHistoryUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryUtilization.setStatus('mandatory')
fddiHistoryTNEG = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryTNEG.setStatus('mandatory')
fddiHistoryMeanTRT = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryMeanTRT.setStatus('mandatory')
fddiHistorySMTs = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistorySMTs.setStatus('mandatory')
fddiHistoryClaims = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryClaims.setStatus('mandatory')
fddiHistoryDirBeacons = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryDirBeacons.setStatus('mandatory')
fddiHistoryBeacons = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryBeacons.setStatus('mandatory')
fddiHistoryRingStateChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiHistoryRingStateChanges.setStatus('mandatory')
mibBuilder.exportSymbols("AXON-MIB", fddiHistorySMTs=fddiHistorySMTs, product=product, fddiHistoryPkts512to1023Octets=fddiHistoryPkts512to1023Octets, fddiHistoryPkts23to63Octets=fddiHistoryPkts23to63Octets, fddiStatsPkts256to511Octets=fddiStatsPkts256to511Octets, fddiStatsDropEvents=fddiStatsDropEvents, fddiHistorySampleIndex=fddiHistorySampleIndex, fddiStatsBeaconAddr=fddiStatsBeaconAddr, fddiStatsPkts2048to4095Octets=fddiStatsPkts2048to4095Octets, fddiStatsOtherPkts=fddiStatsOtherPkts, fddiHistoryTNEG=fddiHistoryTNEG, fddiStatsPkts22Octets=fddiStatsPkts22Octets, fddiHistoryBeacons=fddiHistoryBeacons, common=common, fddiStatsEntry=fddiStatsEntry, axFddiStatistics=axFddiStatistics, fddiHistoryPkts22Octets=fddiHistoryPkts22Octets, fddiStatsPkts=fddiStatsPkts, fddiHistoryIndex=fddiHistoryIndex, fddiStatsPkts64to127Octets=fddiStatsPkts64to127Octets, fddiStatsRingState=fddiStatsRingState, fddiHistoryEntry=fddiHistoryEntry, fddiHistoryMulticastPkts=fddiHistoryMulticastPkts, private=private, fddiStatsPkts128to255Octets=fddiStatsPkts128to255Octets, fddiStatsTNEG=fddiStatsTNEG, fddiStatsBeacons=fddiStatsBeacons, fddiStatsOtherOctets=fddiStatsOtherOctets, axon=axon, fddiStatsDataSource=fddiStatsDataSource, dod=dod, org=org, internet=internet, fddiHistoryIntervalStart=fddiHistoryIntervalStart, fddiHistoryClaims=fddiHistoryClaims, fddiHistoryUtilization=fddiHistoryUtilization, mgmt=mgmt, fddiStatsBroadcastPkts=fddiStatsBroadcastPkts, fddiStatsPkts23to63Octets=fddiStatsPkts23to63Octets, fddiStatsTokens=fddiStatsTokens, enterprises=enterprises, fddiHistoryOctets=fddiHistoryOctets, fddiHistoryPkts256to511Octets=fddiHistoryPkts256to511Octets, mib_2=mib_2, fddiStatsMulticastPkts=fddiStatsMulticastPkts, fddiStatsOwner=fddiStatsOwner, axFddiHistory=axFddiHistory, experimental=experimental, fddiStatsSMTs=fddiStatsSMTs, fddiHistoryPkts128to255Octets=fddiHistoryPkts128to255Octets, fddiHistoryBroadcastPkts=fddiHistoryBroadcastPkts, fddiHistoryErrors=fddiHistoryErrors, fddiHistoryPkts1024to2047Octets=fddiHistoryPkts1024to2047Octets, fddiStatsErrors=fddiStatsErrors, fddiStatsPkts4096to4500Octets=fddiStatsPkts4096to4500Octets, axFddi=axFddi, fddiHistoryMeanTRT=fddiHistoryMeanTRT, clone=clone, directory=directory, fddiHistoryTable=fddiHistoryTable, fddiHistoryRingStateChanges=fddiHistoryRingStateChanges, fddiStatsClaimAddr=fddiStatsClaimAddr, fddiHistoryPkts64to127Octets=fddiHistoryPkts64to127Octets, fddiStatsTable=fddiStatsTable, fddiHistoryPkts4096to4500Octets=fddiHistoryPkts4096to4500Octets, fddiStatsDirBeacons=fddiStatsDirBeacons, fddiStatsPkts512to1023Octets=fddiStatsPkts512to1023Octets, fddiStatsStatus=fddiStatsStatus, fddiHistoryPkts2048to4095Octets=fddiHistoryPkts2048to4095Octets, fddiStatsOctets=fddiStatsOctets, fddiStatsIndex=fddiStatsIndex, fddiHistoryDirBeacons=fddiHistoryDirBeacons, application=application, fddiHistoryPkts=fddiHistoryPkts, fddiStatsPkts1024to2047Octets=fddiStatsPkts1024to2047Octets, fddiHistoryDropEvents=fddiHistoryDropEvents, fddiStatsDirBeaconAddr=fddiStatsDirBeaconAddr, fddiStatsClaims=fddiStatsClaims)
#
# PySNMP MIB module ChrComPmOpticsOTS-SNK-Current-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmOpticsOTS-SNK-Current-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmOptics, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmOptics")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, IpAddress, iso, TimeTicks, Counter32, ObjectIdentity, Integer32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "IpAddress", "iso", "TimeTicks", "Counter32", "ObjectIdentity", "Integer32", "NotificationType", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmOpticsOTS_SNK_CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1), ).setLabel("chrComPmOpticsOTS-SNK-CurrentTable")
if mibBuilder.loadTexts: chrComPmOpticsOTS_SNK_CurrentTable.setStatus('current')
chrComPmOpticsOTS_SNK_CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1), ).setLabel("chrComPmOpticsOTS-SNK-CurrentEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComPmOpticsOTS_SNK_CurrentEntry.setStatus('current')
chrComPmOpticsSuspectedIntrvl = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setStatus('current')
chrComPmOpticsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setStatus('current')
chrComPmOpticsSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setStatus('current')
chrComPmOpticsORS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsORS.setStatus('current')
chrComPmOpticsSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSES.setStatus('current')
chrComPmOpticsUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsUAS.setStatus('current')
chrComPmOpticsMean = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMean.setStatus('current')
chrComPmOpticsMax = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMax.setStatus('current')
chrComPmOpticsMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMin.setStatus('current')
chrComPmOpticsSD = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSD.setStatus('current')
chrComPmOpticsThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmOpticsThresholdProfIndex.setStatus('current')
chrComPmOpticsResetCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmOpticsResetCountersAction.setStatus('current')
mibBuilder.exportSymbols("ChrComPmOpticsOTS-SNK-Current-MIB", chrComPmOpticsORS=chrComPmOpticsORS, chrComPmOpticsElapsedTime=chrComPmOpticsElapsedTime, chrComPmOpticsMean=chrComPmOpticsMean, chrComPmOpticsSuspectedIntrvl=chrComPmOpticsSuspectedIntrvl, chrComPmOpticsOTS_SNK_CurrentTable=chrComPmOpticsOTS_SNK_CurrentTable, chrComPmOpticsResetCountersAction=chrComPmOpticsResetCountersAction, chrComPmOpticsOTS_SNK_CurrentEntry=chrComPmOpticsOTS_SNK_CurrentEntry, chrComPmOpticsMin=chrComPmOpticsMin, chrComPmOpticsSES=chrComPmOpticsSES, chrComPmOpticsUAS=chrComPmOpticsUAS, chrComPmOpticsMax=chrComPmOpticsMax, chrComPmOpticsSuppressedIntrvls=chrComPmOpticsSuppressedIntrvls, chrComPmOpticsThresholdProfIndex=chrComPmOpticsThresholdProfIndex, chrComPmOpticsSD=chrComPmOpticsSD)
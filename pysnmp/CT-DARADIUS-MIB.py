#
# PySNMP MIB module CT-DARADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-DARADIUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:12:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Integer32, Unsigned32, TimeTicks, Gauge32, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Integer32", "Unsigned32", "TimeTicks", "Gauge32", "IpAddress", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctSSA = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497))
daRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24))
daRadiusConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1))
daRadiusGeneralConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1))
daRadiusStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2))
daRadiusGeneralStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 1))
daRadiusgcEnabled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daRadiusgcEnabled.setStatus('mandatory')
daRadiusgcAuthNumRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daRadiusgcAuthNumRetries.setStatus('mandatory')
daRadiusgcAuthSecsBtwnRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daRadiusgcAuthSecsBtwnRetries.setStatus('mandatory')
daRadiusgcAcctNumRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daRadiusgcAcctNumRetries.setStatus('mandatory')
gcAcctSecsBtwnRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gcAcctSecsBtwnRetries.setStatus('mandatory')
daRadiusServerCfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2), )
if mibBuilder.loadTexts: daRadiusServerCfgTable.setStatus('mandatory')
daRadiusServerCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1), ).setIndexNames((0, "CT-DARADIUS-MIB", "scIndex"))
if mibBuilder.loadTexts: daRadiusServerCfgEntry.setStatus('mandatory')
scIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primaryAuthentication", 1), ("secondaryAuthentication", 2), ("primaryAccounting", 3), ("secondaryAccounting", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scIndex.setStatus('mandatory')
scStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scStatus.setStatus('mandatory')
scIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scIpAddress.setStatus('mandatory')
scSharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scSharedSecret.setStatus('mandatory')
scUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scUdpPort.setStatus('mandatory')
gsInDiscards = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gsInDiscards.setStatus('mandatory')
gsInErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gsInErrors.setStatus('mandatory')
daRadiusServerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2), )
if mibBuilder.loadTexts: daRadiusServerStatsTable.setStatus('mandatory')
daRadiusServerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1), ).setIndexNames((0, "CT-DARADIUS-MIB", "ssIndex"))
if mibBuilder.loadTexts: daRadiusServerStatsEntry.setStatus('mandatory')
ssIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primaryAuthentication", 1), ("secondaryAuthentication", 2), ("primaryAccounting", 3), ("secondaryAccounting", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIndex.setStatus('mandatory')
ssInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssInPkts.setStatus('mandatory')
ssInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssInDiscards.setStatus('mandatory')
ssInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssInErrors.setStatus('mandatory')
ssOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssOutPkts.setStatus('mandatory')
ssOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssOutErrors.setStatus('mandatory')
ssResponseTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssResponseTimeouts.setStatus('mandatory')
mibBuilder.exportSymbols("CT-DARADIUS-MIB", daRadiusServerStatsEntry=daRadiusServerStatsEntry, gsInErrors=gsInErrors, ssIndex=ssIndex, daRadius=daRadius, scIndex=scIndex, scIpAddress=scIpAddress, ssInPkts=ssInPkts, daRadiusServerCfgTable=daRadiusServerCfgTable, ssOutErrors=ssOutErrors, ssInErrors=ssInErrors, ssOutPkts=ssOutPkts, daRadiusgcAcctNumRetries=daRadiusgcAcctNumRetries, daRadiusStats=daRadiusStats, daRadiusGeneralStats=daRadiusGeneralStats, scStatus=scStatus, daRadiusServerStatsTable=daRadiusServerStatsTable, daRadiusGeneralConfig=daRadiusGeneralConfig, ssInDiscards=ssInDiscards, scUdpPort=scUdpPort, daRadiusServerCfgEntry=daRadiusServerCfgEntry, ctSSA=ctSSA, daRadiusConfig=daRadiusConfig, daRadiusgcEnabled=daRadiusgcEnabled, gcAcctSecsBtwnRetries=gcAcctSecsBtwnRetries, daRadiusgcAuthNumRetries=daRadiusgcAuthNumRetries, gsInDiscards=gsInDiscards, daRadiusgcAuthSecsBtwnRetries=daRadiusgcAuthSecsBtwnRetries, ssResponseTimeouts=ssResponseTimeouts, scSharedSecret=scSharedSecret)

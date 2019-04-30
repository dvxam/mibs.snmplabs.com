#
# PySNMP MIB module LanMgr-Mib-II-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LanMgr-Mib-II-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:58:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, ObjectIdentity, Unsigned32, Integer32, Bits, Counter32, NotificationType, TimeTicks, Gauge32, Counter64, MibIdentifier, enterprises, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Integer32", "Bits", "Counter32", "NotificationType", "TimeTicks", "Gauge32", "Counter64", "MibIdentifier", "enterprises", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lanmanager = MibIdentifier((1, 3, 6, 1, 4, 1, 77))
lanmgr_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 77, 1)).setLabel("lanmgr-2")
common = MibIdentifier((1, 3, 6, 1, 4, 1, 77, 1, 1))
server = MibIdentifier((1, 3, 6, 1, 4, 1, 77, 1, 2))
workstation = MibIdentifier((1, 3, 6, 1, 4, 1, 77, 1, 3))
domain = MibIdentifier((1, 3, 6, 1, 4, 1, 77, 1, 4))
comVersionMaj = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comVersionMaj.setStatus('mandatory')
comVersionMin = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comVersionMin.setStatus('mandatory')
comType = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comType.setStatus('mandatory')
comStatStart = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comStatStart.setStatus('mandatory')
comStatNumNetIOs = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comStatNumNetIOs.setStatus('mandatory')
comStatFiNetIOs = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comStatFiNetIOs.setStatus('mandatory')
comStatFcNetIOs = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comStatFcNetIOs.setStatus('mandatory')
svDescription = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svDescription.setStatus('mandatory')
svSvcNumber = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSvcNumber.setStatus('mandatory')
svSvcTable = MibTable((1, 3, 6, 1, 4, 1, 77, 1, 2, 3), )
if mibBuilder.loadTexts: svSvcTable.setStatus('mandatory')
svSvcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1), ).setIndexNames((0, "LanMgr-Mib-II-MIB", "svSvcName"))
if mibBuilder.loadTexts: svSvcEntry.setStatus('mandatory')
svSvcName = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSvcName.setStatus('mandatory')
svSvcInstalledState = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("uninstalled", 1), ("install-pending", 2), ("uninstall-pending", 3), ("installed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSvcInstalledState.setStatus('mandatory')
svSvcOperatingState = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("continue-pending", 2), ("pause-pending", 3), ("paused", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSvcOperatingState.setStatus('mandatory')
svSvcCanBeUninstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cannot-be-uninstalled", 1), ("can-be-uninstalled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSvcCanBeUninstalled.setStatus('mandatory')
svSvcCanBePaused = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cannot-be-paused", 1), ("can-be-paused", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSvcCanBePaused.setStatus('mandatory')
svStatOpens = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatOpens.setStatus('mandatory')
svStatDevOpens = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatDevOpens.setStatus('mandatory')
svStatQueuedJobs = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatQueuedJobs.setStatus('mandatory')
svStatSOpens = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatSOpens.setStatus('mandatory')
svStatErrorOuts = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatErrorOuts.setStatus('mandatory')
svStatPwErrors = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatPwErrors.setStatus('mandatory')
svStatPermErrors = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatPermErrors.setStatus('mandatory')
svStatSysErrors = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatSysErrors.setStatus('mandatory')
svStatSentBytes = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatSentBytes.setStatus('mandatory')
svStatRcvdBytes = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatRcvdBytes.setStatus('mandatory')
svStatAvResponse = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatAvResponse.setStatus('mandatory')
svSecurityMode = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("share-level", 1), ("user-level", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSecurityMode.setStatus('mandatory')
svUsers = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svUsers.setStatus('mandatory')
svStatReqBufsNeeded = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatReqBufsNeeded.setStatus('mandatory')
svStatBigBufsNeeded = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svStatBigBufsNeeded.setStatus('mandatory')
svSessionNumber = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSessionNumber.setStatus('mandatory')
svSessionTable = MibTable((1, 3, 6, 1, 4, 1, 77, 1, 2, 20), )
if mibBuilder.loadTexts: svSessionTable.setStatus('mandatory')
svSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1), ).setIndexNames((0, "LanMgr-Mib-II-MIB", "svSesClientName"), (0, "LanMgr-Mib-II-MIB", "svSesUserName"))
if mibBuilder.loadTexts: svSessionEntry.setStatus('mandatory')
svSesClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSesClientName.setStatus('mandatory')
svSesUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSesUserName.setStatus('mandatory')
svSesNumOpens = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSesNumOpens.setStatus('mandatory')
svSesTime = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSesTime.setStatus('mandatory')
svSesIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSesIdleTime.setStatus('mandatory')
svSesClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("down-level", 1), ("dos-lm", 2), ("dos-lm-2", 3), ("os2-lm-1", 4), ("os2-lm-2", 5), ("dos-lm-2-1", 6), ("os2-lm-2-1", 7), ("afp-1-1", 8), ("afp-2-0", 9), ("nt-3-1", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSesClientType.setStatus('mandatory')
svSesState = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("deleted", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svSesState.setStatus('mandatory')
svAutoDisconnects = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svAutoDisconnects.setStatus('mandatory')
svDisConTime = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svDisConTime.setStatus('mandatory')
svAuditLogSize = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svAuditLogSize.setStatus('mandatory')
svUserNumber = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svUserNumber.setStatus('mandatory')
svUserTable = MibTable((1, 3, 6, 1, 4, 1, 77, 1, 2, 25), )
if mibBuilder.loadTexts: svUserTable.setStatus('mandatory')
svUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 77, 1, 2, 25, 1), ).setIndexNames((0, "LanMgr-Mib-II-MIB", "svUserName"))
if mibBuilder.loadTexts: svUserEntry.setStatus('mandatory')
svUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 25, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svUserName.setStatus('mandatory')
svShareNumber = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svShareNumber.setStatus('mandatory')
svShareTable = MibTable((1, 3, 6, 1, 4, 1, 77, 1, 2, 27), )
if mibBuilder.loadTexts: svShareTable.setStatus('mandatory')
svShareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 77, 1, 2, 27, 1), ).setIndexNames((0, "LanMgr-Mib-II-MIB", "svShareName"))
if mibBuilder.loadTexts: svShareEntry.setStatus('mandatory')
svShareName = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 27, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svShareName.setStatus('mandatory')
svSharePath = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 27, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svSharePath.setStatus('mandatory')
svShareComment = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 27, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svShareComment.setStatus('mandatory')
svPrintQNumber = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 2, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svPrintQNumber.setStatus('mandatory')
svPrintQTable = MibTable((1, 3, 6, 1, 4, 1, 77, 1, 2, 29), )
if mibBuilder.loadTexts: svPrintQTable.setStatus('mandatory')
svPrintQEntry = MibTableRow((1, 3, 6, 1, 4, 1, 77, 1, 2, 29, 1), ).setIndexNames((0, "LanMgr-Mib-II-MIB", "svPrintQName"))
if mibBuilder.loadTexts: svPrintQEntry.setStatus('mandatory')
svPrintQName = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 29, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svPrintQName.setStatus('mandatory')
svPrintQNumJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 2, 29, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svPrintQNumJobs.setStatus('mandatory')
wkstaStatSessStarts = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wkstaStatSessStarts.setStatus('mandatory')
wkstaStatSessFails = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wkstaStatSessFails.setStatus('mandatory')
wkstaStatUses = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wkstaStatUses.setStatus('mandatory')
wkstaStatUseFails = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wkstaStatUseFails.setStatus('mandatory')
wkstaStatAutoRecs = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wkstaStatAutoRecs.setStatus('mandatory')
wkstaErrorLogSize = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 3, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wkstaErrorLogSize.setStatus('mandatory')
wkstaUseNumber = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wkstaUseNumber.setStatus('mandatory')
wkstaUseTable = MibTable((1, 3, 6, 1, 4, 1, 77, 1, 3, 8), )
if mibBuilder.loadTexts: wkstaUseTable.setStatus('mandatory')
wkstaUseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 77, 1, 3, 8, 1), ).setIndexNames((0, "LanMgr-Mib-II-MIB", "useLocalName"), (0, "LanMgr-Mib-II-MIB", "useRemote"))
if mibBuilder.loadTexts: wkstaUseEntry.setStatus('mandatory')
useLocalName = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 3, 8, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: useLocalName.setStatus('mandatory')
useRemote = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 3, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: useRemote.setStatus('mandatory')
useStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 3, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("use-ok", 1), ("use-paused", 2), ("use-session-lost", 3), ("use-network-error", 4), ("use-connecting", 5), ("use-reconnecting", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: useStatus.setStatus('mandatory')
domPrimaryDomain = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: domPrimaryDomain.setStatus('mandatory')
domLogonDomain = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: domLogonDomain.setStatus('mandatory')
domOtherDomainNumber = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: domOtherDomainNumber.setStatus('mandatory')
domOtherDomainTable = MibTable((1, 3, 6, 1, 4, 1, 77, 1, 4, 4), )
if mibBuilder.loadTexts: domOtherDomainTable.setStatus('mandatory')
domOtherDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 77, 1, 4, 4, 1), ).setIndexNames((0, "LanMgr-Mib-II-MIB", "domOtherName"))
if mibBuilder.loadTexts: domOtherDomainEntry.setStatus('mandatory')
domOtherName = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 4, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: domOtherName.setStatus('mandatory')
domServerNumber = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 4, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: domServerNumber.setStatus('mandatory')
domServerTable = MibTable((1, 3, 6, 1, 4, 1, 77, 1, 4, 6), )
if mibBuilder.loadTexts: domServerTable.setStatus('mandatory')
domServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 77, 1, 4, 6, 1), ).setIndexNames((0, "LanMgr-Mib-II-MIB", "domServerName"))
if mibBuilder.loadTexts: domServerEntry.setStatus('mandatory')
domServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 4, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: domServerName.setStatus('mandatory')
domLogonNumber = MibScalar((1, 3, 6, 1, 4, 1, 77, 1, 4, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: domLogonNumber.setStatus('mandatory')
domLogonTable = MibTable((1, 3, 6, 1, 4, 1, 77, 1, 4, 8), )
if mibBuilder.loadTexts: domLogonTable.setStatus('mandatory')
domLogonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 77, 1, 4, 8, 1), ).setIndexNames((0, "LanMgr-Mib-II-MIB", "domLogonUser"), (0, "LanMgr-Mib-II-MIB", "domLogonMachine"))
if mibBuilder.loadTexts: domLogonEntry.setStatus('mandatory')
domLogonUser = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 4, 8, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: domLogonUser.setStatus('mandatory')
domLogonMachine = MibTableColumn((1, 3, 6, 1, 4, 1, 77, 1, 4, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: domLogonMachine.setStatus('mandatory')
mibBuilder.exportSymbols("LanMgr-Mib-II-MIB", svSesUserName=svSesUserName, svDisConTime=svDisConTime, svShareComment=svShareComment, svDescription=svDescription, svSvcInstalledState=svSvcInstalledState, svSvcEntry=svSvcEntry, svPrintQEntry=svPrintQEntry, svPrintQName=svPrintQName, svUsers=svUsers, lanmanager=lanmanager, svStatSOpens=svStatSOpens, svPrintQNumber=svPrintQNumber, svShareName=svShareName, comStatNumNetIOs=comStatNumNetIOs, svSesNumOpens=svSesNumOpens, domOtherDomainNumber=domOtherDomainNumber, wkstaStatUses=wkstaStatUses, domOtherName=domOtherName, domLogonNumber=domLogonNumber, svSvcNumber=svSvcNumber, svStatBigBufsNeeded=svStatBigBufsNeeded, server=server, svShareNumber=svShareNumber, common=common, wkstaStatAutoRecs=wkstaStatAutoRecs, comType=comType, useLocalName=useLocalName, svSharePath=svSharePath, comStatFcNetIOs=comStatFcNetIOs, wkstaStatUseFails=wkstaStatUseFails, svSessionEntry=svSessionEntry, svStatOpens=svStatOpens, svSvcTable=svSvcTable, domOtherDomainEntry=domOtherDomainEntry, comVersionMaj=comVersionMaj, svAuditLogSize=svAuditLogSize, wkstaUseEntry=wkstaUseEntry, svStatPermErrors=svStatPermErrors, useStatus=useStatus, svShareEntry=svShareEntry, domServerEntry=domServerEntry, svStatReqBufsNeeded=svStatReqBufsNeeded, useRemote=useRemote, lanmgr_2=lanmgr_2, svStatPwErrors=svStatPwErrors, domServerTable=domServerTable, svSvcOperatingState=svSvcOperatingState, svStatDevOpens=svStatDevOpens, svStatAvResponse=svStatAvResponse, svStatQueuedJobs=svStatQueuedJobs, svSesState=svSesState, svSvcName=svSvcName, svStatErrorOuts=svStatErrorOuts, wkstaUseNumber=wkstaUseNumber, svSecurityMode=svSecurityMode, svUserTable=svUserTable, svSesClientType=svSesClientType, svUserEntry=svUserEntry, comStatFiNetIOs=comStatFiNetIOs, wkstaStatSessStarts=wkstaStatSessStarts, comStatStart=comStatStart, svStatSentBytes=svStatSentBytes, wkstaStatSessFails=wkstaStatSessFails, domLogonDomain=domLogonDomain, svSessionNumber=svSessionNumber, svPrintQTable=svPrintQTable, svSesTime=svSesTime, svPrintQNumJobs=svPrintQNumJobs, domPrimaryDomain=domPrimaryDomain, svSvcCanBeUninstalled=svSvcCanBeUninstalled, domLogonTable=domLogonTable, domLogonUser=domLogonUser, domServerName=domServerName, domLogonMachine=domLogonMachine, domLogonEntry=domLogonEntry, svStatRcvdBytes=svStatRcvdBytes, domOtherDomainTable=domOtherDomainTable, wkstaUseTable=wkstaUseTable, svUserName=svUserName, svStatSysErrors=svStatSysErrors, comVersionMin=comVersionMin, svSessionTable=svSessionTable, workstation=workstation, svSvcCanBePaused=svSvcCanBePaused, svAutoDisconnects=svAutoDisconnects, domServerNumber=domServerNumber, svUserNumber=svUserNumber, svSesIdleTime=svSesIdleTime, wkstaErrorLogSize=wkstaErrorLogSize, svSesClientName=svSesClientName, domain=domain, svShareTable=svShareTable)

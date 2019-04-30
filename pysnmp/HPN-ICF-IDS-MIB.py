#
# PySNMP MIB module HPN-ICF-IDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-IDS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, ObjectIdentity, Gauge32, iso, MibIdentifier, NotificationType, Integer32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "ObjectIdentity", "Gauge32", "iso", "MibIdentifier", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfIDSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1))
if mibBuilder.loadTexts: hpnicfIDSMib.setLastUpdated('200507141942Z')
if mibBuilder.loadTexts: hpnicfIDSMib.setOrganization('')
hpnicfIds = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47))
hpnicfIDSTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1))
hpnicfIDSTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1))
hpnicfIDSTrapIPFragmentQueueLen = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapIPFragmentQueueLen.setStatus('current')
hpnicfIDSTrapStatSessionTabLen = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapStatSessionTabLen.setStatus('current')
hpnicfIDSTrapIPAddressType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapIPAddressType.setStatus('current')
hpnicfIDSTrapIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapIPAddress.setStatus('current')
hpnicfIDSTrapUserName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapUserName.setStatus('current')
hpnicfIDSTrapLoginType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("telnet", 1), ("ssh", 2), ("web", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapLoginType.setStatus('current')
hpnicfIDSTrapUpgradeType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("programme", 1), ("crb", 2), ("vrb", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapUpgradeType.setStatus('current')
hpnicfIDSTrapCRLName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapCRLName.setStatus('current')
hpnicfIDSTrapCertName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapCertName.setStatus('current')
hpnicfIDSTrapDetectRuleID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 10), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapDetectRuleID.setStatus('current')
hpnicfIDSTrapEngineID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 11), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapEngineID.setStatus('current')
hpnicfIDSTrapFileName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapFileName.setStatus('current')
hpnicfIDSTrapCfgLineInFile = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 13), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapCfgLineInFile.setStatus('current')
hpnicfIDSTrapReasonForError = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIDSTrapReasonForError.setStatus('current')
hpnicfIDSTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2))
hpnicfIDSTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0))
hpnicfIDSTrapIPFragQueueFull = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 1)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPFragmentQueueLen"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapIPFragQueueFull.setStatus('current')
hpnicfIDSTrapStatSessTabFull = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 2)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapStatSessionTabLen"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapStatSessTabFull.setStatus('current')
hpnicfIDSTrapDetectRuleParseFail = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 3)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapDetectRuleID"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapEngineID"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapDetectRuleParseFail.setStatus('current')
hpnicfIDSTrapDBConnLost = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 4)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPAddressType"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPAddress"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapDBConnLost.setStatus('current')
hpnicfIDSTrapCRLNeedUpdate = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 5)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapCRLName"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapCRLNeedUpdate.setStatus('current')
hpnicfIDSTrapCertOverdue = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 6)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapCertName"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapCertOverdue.setStatus('current')
hpnicfIDSTrapTooManyLoginFail = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 7)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapUserName"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPAddressType"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPAddress"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapLoginType"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapTooManyLoginFail.setStatus('current')
hpnicfIDSTrapUpgradeError = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 8)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapUpgradeType"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapUpgradeError.setStatus('current')
hpnicfIDSTrapFileAccessError = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 9)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapFileName"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapFileAccessError.setStatus('current')
hpnicfIDSTrapConsArithMemLow = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 10)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapConsArithMemLow.setStatus('current')
hpnicfIDSTrapSSRAMOperFail = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 11)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapSSRAMOperFail.setStatus('current')
hpnicfIDSTrapPacketProcessDisorder = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 12)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
if mibBuilder.loadTexts: hpnicfIDSTrapPacketProcessDisorder.setStatus('current')
hpnicfIDSTrapCfgFileFormatError = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 13)).setObjects(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapFileName"), ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapCfgLineInFile"))
if mibBuilder.loadTexts: hpnicfIDSTrapCfgFileFormatError.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-IDS-MIB", hpnicfIDSTrapInfo=hpnicfIDSTrapInfo, hpnicfIDSTrapFileName=hpnicfIDSTrapFileName, hpnicfIDSTrapUserName=hpnicfIDSTrapUserName, hpnicfIDSTrapLoginType=hpnicfIDSTrapLoginType, hpnicfIDSTrapIPAddressType=hpnicfIDSTrapIPAddressType, hpnicfIDSTrapCRLName=hpnicfIDSTrapCRLName, hpnicfIDSTrapDBConnLost=hpnicfIDSTrapDBConnLost, hpnicfIDSTrapIPAddress=hpnicfIDSTrapIPAddress, hpnicfIDSTrapIPFragQueueFull=hpnicfIDSTrapIPFragQueueFull, hpnicfIDSTrapEngineID=hpnicfIDSTrapEngineID, hpnicfIDSTrapStatSessTabFull=hpnicfIDSTrapStatSessTabFull, hpnicfIDSTrapUpgradeType=hpnicfIDSTrapUpgradeType, hpnicfIDSTrapCertOverdue=hpnicfIDSTrapCertOverdue, hpnicfIDSTrap=hpnicfIDSTrap, hpnicfIDSTrapCfgFileFormatError=hpnicfIDSTrapCfgFileFormatError, hpnicfIDSTrapDetectRuleID=hpnicfIDSTrapDetectRuleID, hpnicfIds=hpnicfIds, hpnicfIDSMib=hpnicfIDSMib, hpnicfIDSTrapReasonForError=hpnicfIDSTrapReasonForError, hpnicfIDSTrapUpgradeError=hpnicfIDSTrapUpgradeError, hpnicfIDSTrapSSRAMOperFail=hpnicfIDSTrapSSRAMOperFail, hpnicfIDSTrapDetectRuleParseFail=hpnicfIDSTrapDetectRuleParseFail, PYSNMP_MODULE_ID=hpnicfIDSMib, hpnicfIDSTrapPacketProcessDisorder=hpnicfIDSTrapPacketProcessDisorder, hpnicfIDSTrapCertName=hpnicfIDSTrapCertName, hpnicfIDSTrapStatSessionTabLen=hpnicfIDSTrapStatSessionTabLen, hpnicfIDSTrapTooManyLoginFail=hpnicfIDSTrapTooManyLoginFail, hpnicfIDSTrapIPFragmentQueueLen=hpnicfIDSTrapIPFragmentQueueLen, hpnicfIDSTrapCRLNeedUpdate=hpnicfIDSTrapCRLNeedUpdate, hpnicfIDSTrapPrefix=hpnicfIDSTrapPrefix, hpnicfIDSTrapFileAccessError=hpnicfIDSTrapFileAccessError, hpnicfIDSTrapConsArithMemLow=hpnicfIDSTrapConsArithMemLow, hpnicfIDSTrapCfgLineInFile=hpnicfIDSTrapCfgLineInFile, hpnicfIDSTrapGroup=hpnicfIDSTrapGroup)

#
# PySNMP MIB module A3Com-Sdlc-r1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-SDLC-R1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:53:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifOperStatus, ifAdminStatus, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifOperStatus", "ifAdminStatus", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, enterprises, Integer32, Counter64, NotificationType, NotificationType, iso, MibIdentifier, Gauge32, ModuleIdentity, ObjectIdentity, TimeTicks, Counter32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "enterprises", "Integer32", "Counter64", "NotificationType", "NotificationType", "iso", "MibIdentifier", "Gauge32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Counter32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
sdlc = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 25))
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

sdlcPortGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 25, 1))
sdlcLSGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 25, 2))
sdlcMapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 25, 3))
sdlcPortAdminTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1), )
if mibBuilder.loadTexts: sdlcPortAdminTable.setStatus('mandatory')
sdlcPortAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sdlcPortAdminEntry.setStatus('mandatory')
sdlcPortAdminName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortAdminName.setStatus('mandatory')
sdlcPortAdminRole = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("negotiable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcPortAdminRole.setStatus('mandatory')
sdlcPortAdminType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leased", 1), ("switched", 2))).clone('leased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcPortAdminType.setStatus('mandatory')
sdlcPortAdminTopology = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pointToPoint", 1), ("multipoint", 2))).clone('pointToPoint')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcPortAdminTopology.setStatus('mandatory')
sdlcPortAdminACTIVTO = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcPortAdminACTIVTO.setStatus('mandatory')
sdlcPortAdminPAUSE = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 6), TimeTicks().clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcPortAdminPAUSE.setStatus('mandatory')
sdlcPortAdminSlowPollTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 7), TimeTicks().clone(2000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcPortAdminSlowPollTimer.setStatus('mandatory')
sdlcPortOperTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2), )
if mibBuilder.loadTexts: sdlcPortOperTable.setStatus('mandatory')
sdlcPortOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sdlcPortOperEntry.setStatus('mandatory')
sdlcPortOperName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperName.setStatus('mandatory')
sdlcPortOperRole = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("undefined", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperRole.setStatus('mandatory')
sdlcPortOperType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leased", 1), ("switched", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperType.setStatus('mandatory')
sdlcPortOperTopology = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pointToPoint", 1), ("multipoint", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperTopology.setStatus('mandatory')
sdlcPortOperACTIVTO = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperACTIVTO.setStatus('mandatory')
sdlcPortOperPAUSE = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperPAUSE.setStatus('mandatory')
sdlcPortOperSlowPollMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("servlim", 1), ("pollpause", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperSlowPollMethod.setStatus('mandatory')
sdlcPortOperSlowPollTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperSlowPollTimer.setStatus('mandatory')
sdlcPortOperLastFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperLastFailTime.setStatus('mandatory')
sdlcPortOperLastFailCause = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("undefined", 1), ("physical", 2))).clone('undefined')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortOperLastFailCause.setStatus('mandatory')
sdlcPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3), )
if mibBuilder.loadTexts: sdlcPortStatsTable.setStatus('mandatory')
sdlcPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sdlcPortStatsEntry.setStatus('mandatory')
sdlcPortStatsPhysicalFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortStatsPhysicalFailures.setStatus('mandatory')
sdlcPortStatsInvalidAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortStatsInvalidAddresses.setStatus('mandatory')
sdlcPortStatsDwarfFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcPortStatsDwarfFrames.setStatus('mandatory')
sdlcLSAdminTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1), )
if mibBuilder.loadTexts: sdlcLSAdminTable.setStatus('mandatory')
sdlcLSAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3Com-Sdlc-r1-MIB", "sdlcLSAddress"))
if mibBuilder.loadTexts: sdlcLSAdminEntry.setStatus('mandatory')
sdlcLSAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcLSAddress.setStatus('mandatory')
sdlcLSAdminName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcLSAdminName.setStatus('mandatory')
sdlcLSAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2))).clone('active')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcLSAdminState.setStatus('mandatory')
sdlcLSAdminMAXDATA = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSAdminMAXDATA.setStatus('mandatory')
sdlcLSAdminREPLYTO = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 5), TimeTicks().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcLSAdminREPLYTO.setStatus('mandatory')
sdlcLSAdminMAXIN = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSAdminMAXIN.setStatus('mandatory')
sdlcLSAdminMAXOUT = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcLSAdminMAXOUT.setStatus('mandatory')
sdlcLSAdminMODULO = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8, 128))).clone(namedValues=NamedValues(("eight", 8), ("onetwentyeight", 128))).clone('eight')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSAdminMODULO.setStatus('mandatory')
sdlcLSAdminRETRIESm = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)).clone(15)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSAdminRETRIESm.setStatus('mandatory')
sdlcLSAdminRETRIESt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 10), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcLSAdminRETRIESt.setStatus('mandatory')
sdlcLSAdminRETRIESn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcLSAdminRETRIESn.setStatus('mandatory')
sdlcLSAdminRNRLIMIT = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 12), TimeTicks().clone(18000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcLSAdminRNRLIMIT.setStatus('mandatory')
sdlcLSAdminDATMODE = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half", 1), ("full", 2))).clone('half')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSAdminDATMODE.setStatus('mandatory')
sdlcLSAdminGPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcLSAdminGPoll.setStatus('mandatory')
sdlcLSAdminSimRim = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2))).clone('no')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSAdminSimRim.setStatus('mandatory')
sdlcLSOperTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2), )
if mibBuilder.loadTexts: sdlcLSOperTable.setStatus('mandatory')
sdlcLSOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3Com-Sdlc-r1-MIB", "sdlcLSAddress"))
if mibBuilder.loadTexts: sdlcLSOperEntry.setStatus('mandatory')
sdlcLSOperName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperName.setStatus('mandatory')
sdlcLSOperRole = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("undefined", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperRole.setStatus('mandatory')
sdlcLSOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("discontacted", 1), ("contactPending", 2), ("contacted", 3), ("discontactPending", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperState.setStatus('mandatory')
sdlcLSOperMAXDATA = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperMAXDATA.setStatus('mandatory')
sdlcLSOperREPLYTO = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperREPLYTO.setStatus('mandatory')
sdlcLSOperMAXIN = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperMAXIN.setStatus('mandatory')
sdlcLSOperMAXOUT = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperMAXOUT.setStatus('mandatory')
sdlcLSOperMODULO = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8, 128))).clone(namedValues=NamedValues(("eight", 8), ("onetwentyeight", 128))).clone('eight')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperMODULO.setStatus('mandatory')
sdlcLSOperRETRIESm = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperRETRIESm.setStatus('mandatory')
sdlcLSOperRETRIESt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperRETRIESt.setStatus('mandatory')
sdlcLSOperRETRIESn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperRETRIESn.setStatus('mandatory')
sdlcLSOperRNRLIMIT = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperRNRLIMIT.setStatus('mandatory')
sdlcLSOperDATMODE = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half", 1), ("full", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperDATMODE.setStatus('mandatory')
sdlcLSOperLastFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperLastFailTime.setStatus('mandatory')
sdlcLSOperLastFailCause = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("undefined", 1), ("rxFRMR", 2), ("txFRMR", 3), ("noResponse", 4), ("protocolErr", 5), ("noActivity", 6), ("rnrLimit", 7), ("retriesExpired", 8))).clone('undefined')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperLastFailCause.setStatus('mandatory')
sdlcLSOperLastFailCtrlIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperLastFailCtrlIn.setStatus('mandatory')
sdlcLSOperLastFailCtrlOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperLastFailCtrlOut.setStatus('mandatory')
sdlcLSOperLastFailFRMRInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperLastFailFRMRInfo.setStatus('mandatory')
sdlcLSOperLastFailREPLYTOs = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperLastFailREPLYTOs.setStatus('mandatory')
sdlcLSOperGPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperGPoll.setStatus('mandatory')
sdlcLSOperSimRim = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2))).clone('no')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSOperSimRim.setStatus('mandatory')
sdlcLSStatsTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3), )
if mibBuilder.loadTexts: sdlcLSStatsTable.setStatus('mandatory')
sdlcLSStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3Com-Sdlc-r1-MIB", "sdlcLSAddress"))
if mibBuilder.loadTexts: sdlcLSStatsEntry.setStatus('mandatory')
sdlcLSStatsBLUsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsBLUsIn.setStatus('mandatory')
sdlcLSStatsBLUsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsBLUsOut.setStatus('mandatory')
sdlcLSStatsOctetsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsOctetsIn.setStatus('mandatory')
sdlcLSStatsOctetsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsOctetsOut.setStatus('mandatory')
sdlcLSStatsPollsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsPollsOut.setStatus('mandatory')
sdlcLSStatsPollRspsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsPollRspsOut.setStatus('mandatory')
sdlcLSStatsLocalBusies = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsLocalBusies.setStatus('mandatory')
sdlcLSStatsRemoteBusies = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsRemoteBusies.setStatus('mandatory')
sdlcLSStatsIFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsIFramesIn.setStatus('mandatory')
sdlcLSStatsIFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsIFramesOut.setStatus('mandatory')
sdlcLSStatsRetransmits = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsRetransmits.setStatus('mandatory')
sdlcLSStatsIOctetsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsIOctetsIn.setStatus('mandatory')
sdlcLSStatsIOctetsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsIOctetsOut.setStatus('mandatory')
sdlcLSStatsUIFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsUIFramesIn.setStatus('mandatory')
sdlcLSStatsUIFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsUIFramesOut.setStatus('mandatory')
sdlcLSStatsXIDsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsXIDsIn.setStatus('mandatory')
sdlcLSStatsXIDsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsXIDsOut.setStatus('mandatory')
sdlcLSStatsTESTsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsTESTsIn.setStatus('mandatory')
sdlcLSStatsTESTsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsTESTsOut.setStatus('mandatory')
sdlcLSStatsREJsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsREJsIn.setStatus('mandatory')
sdlcLSStatsREJsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsREJsOut.setStatus('mandatory')
sdlcLSStatsFRMRsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsFRMRsIn.setStatus('mandatory')
sdlcLSStatsFRMRsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsFRMRsOut.setStatus('mandatory')
sdlcLSStatsSIMsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsSIMsIn.setStatus('mandatory')
sdlcLSStatsSIMsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsSIMsOut.setStatus('mandatory')
sdlcLSStatsRIMsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsRIMsIn.setStatus('mandatory')
sdlcLSStatsRIMsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsRIMsOut.setStatus('mandatory')
sdlcLSStatsProtocolErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsProtocolErrs.setStatus('mandatory')
sdlcLSStatsActivityTOs = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsActivityTOs.setStatus('mandatory')
sdlcLSStatsRNRLIMITs = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsRNRLIMITs.setStatus('mandatory')
sdlcLSStatsRetriesExps = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcLSStatsRetriesExps.setStatus('mandatory')
sdlcMapTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1), )
if mibBuilder.loadTexts: sdlcMapTable.setStatus('mandatory')
pysmiFakeCol1000 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1) + (1000, ), Integer32())
sdlcMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1), ).setIndexNames((0, "A3Com-Sdlc-r1-MIB", "pysmiFakeCol1000"))
if mibBuilder.loadTexts: sdlcMapEntry.setStatus('mandatory')
sdlcMapPollAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcMapPollAddress.setStatus('mandatory')
sdlcMapLocalMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcMapLocalMacAddress.setStatus('mandatory')
sdlcMapLocalSap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcMapLocalSap.setStatus('mandatory')
sdlcMapRemoteMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcMapRemoteMacAddress.setStatus('mandatory')
sdlcMapRemoteSap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcMapRemoteSap.setStatus('mandatory')
sdlcMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcMapName.setStatus('mandatory')
sdlcMapPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcMapPortState.setStatus('mandatory')
sdlcMapLSState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcMapLSState.setStatus('mandatory')
sdlcPortStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 43, 2, 25) + (0,1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("A3Com-Sdlc-r1-MIB", "sdlcPortOperLastFailTime"), ("A3Com-Sdlc-r1-MIB", "sdlcPortOperLastFailCause"))
sdlcLSStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 43, 2, 25) + (0,2)).setObjects(("IF-MIB", "ifIndex"), ("A3Com-Sdlc-r1-MIB", "sdlcLSAddress"), ("A3Com-Sdlc-r1-MIB", "sdlcLSOperState"), ("A3Com-Sdlc-r1-MIB", "sdlcLSAdminState"), ("A3Com-Sdlc-r1-MIB", "sdlcLSOperLastFailTime"), ("A3Com-Sdlc-r1-MIB", "sdlcLSOperLastFailCause"), ("A3Com-Sdlc-r1-MIB", "sdlcLSOperLastFailFRMRInfo"), ("A3Com-Sdlc-r1-MIB", "sdlcLSOperLastFailCtrlIn"), ("A3Com-Sdlc-r1-MIB", "sdlcLSOperLastFailCtrlOut"), ("A3Com-Sdlc-r1-MIB", "sdlcLSOperLastFailREPLYTOs"))
mibBuilder.exportSymbols("A3Com-Sdlc-r1-MIB", sdlcPortOperPAUSE=sdlcPortOperPAUSE, sdlcPortStatsInvalidAddresses=sdlcPortStatsInvalidAddresses, sdlcPortStatsEntry=sdlcPortStatsEntry, sdlcPortOperLastFailTime=sdlcPortOperLastFailTime, sdlcLSOperLastFailFRMRInfo=sdlcLSOperLastFailFRMRInfo, sdlcPortOperLastFailCause=sdlcPortOperLastFailCause, sdlcLSOperDATMODE=sdlcLSOperDATMODE, sdlcLSStatsFRMRsIn=sdlcLSStatsFRMRsIn, sdlcLSOperRNRLIMIT=sdlcLSOperRNRLIMIT, sdlcPortOperSlowPollMethod=sdlcPortOperSlowPollMethod, sdlcMapRemoteSap=sdlcMapRemoteSap, sdlcLSAdminMAXIN=sdlcLSAdminMAXIN, sdlcLSStatsSIMsIn=sdlcLSStatsSIMsIn, sdlcLSStatsLocalBusies=sdlcLSStatsLocalBusies, sdlcLSOperMAXIN=sdlcLSOperMAXIN, sdlcLSStatsIOctetsOut=sdlcLSStatsIOctetsOut, sdlcPortAdminEntry=sdlcPortAdminEntry, sdlcLSStatsRetriesExps=sdlcLSStatsRetriesExps, sdlcLSOperGPoll=sdlcLSOperGPoll, sdlcPortOperRole=sdlcPortOperRole, sdlcLSAdminRETRIESn=sdlcLSAdminRETRIESn, sdlcLSStatsIFramesOut=sdlcLSStatsIFramesOut, sdlcLSAdminRETRIESt=sdlcLSAdminRETRIESt, sdlcPortOperName=sdlcPortOperName, sdlcLSStatsOctetsOut=sdlcLSStatsOctetsOut, sdlcPortAdminRole=sdlcPortAdminRole, sdlcLSStatsRetransmits=sdlcLSStatsRetransmits, sdlcMapPortState=sdlcMapPortState, sdlcLSOperMODULO=sdlcLSOperMODULO, sdlcLSStatsIFramesIn=sdlcLSStatsIFramesIn, sdlcMapLSState=sdlcMapLSState, sdlcPortAdminType=sdlcPortAdminType, sdlcPortAdminName=sdlcPortAdminName, sdlcLSOperREPLYTO=sdlcLSOperREPLYTO, sdlcMapTable=sdlcMapTable, sdlcLSAdminSimRim=sdlcLSAdminSimRim, sdlcLSStatsRIMsIn=sdlcLSStatsRIMsIn, sdlcLSOperEntry=sdlcLSOperEntry, pysmiFakeCol1000=pysmiFakeCol1000, sdlcPortStatsTable=sdlcPortStatsTable, sdlcLSStatsBLUsOut=sdlcLSStatsBLUsOut, sdlcLSStatsUIFramesIn=sdlcLSStatsUIFramesIn, sdlcPortOperEntry=sdlcPortOperEntry, sdlcLSOperRETRIESn=sdlcLSOperRETRIESn, sdlcMapLocalSap=sdlcMapLocalSap, sdlcPortOperTable=sdlcPortOperTable, sdlcLSStatsEntry=sdlcLSStatsEntry, sdlcLSAdminTable=sdlcLSAdminTable, sdlcMapEntry=sdlcMapEntry, sdlcLSAdminREPLYTO=sdlcLSAdminREPLYTO, sdlcLSAdminMAXDATA=sdlcLSAdminMAXDATA, sdlcLSOperMAXDATA=sdlcLSOperMAXDATA, sdlcLSOperSimRim=sdlcLSOperSimRim, sdlcPortStatusChange=sdlcPortStatusChange, sdlcLSOperTable=sdlcLSOperTable, sdlcLSStatsRemoteBusies=sdlcLSStatsRemoteBusies, sdlcPortAdminPAUSE=sdlcPortAdminPAUSE, sdlcLSAdminMODULO=sdlcLSAdminMODULO, a3com=a3com, sdlcPortAdminSlowPollTimer=sdlcPortAdminSlowPollTimer, sdlcPortStatsDwarfFrames=sdlcPortStatsDwarfFrames, sdlcLSAdminEntry=sdlcLSAdminEntry, sdlcLSAdminRNRLIMIT=sdlcLSAdminRNRLIMIT, brouterMIB=brouterMIB, sdlcLSStatsIOctetsIn=sdlcLSStatsIOctetsIn, sdlcMapPollAddress=sdlcMapPollAddress, sdlcLSAdminName=sdlcLSAdminName, sdlcLSStatsUIFramesOut=sdlcLSStatsUIFramesOut, sdlcLSStatsActivityTOs=sdlcLSStatsActivityTOs, sdlcLSStatsBLUsIn=sdlcLSStatsBLUsIn, sdlcPortGroup=sdlcPortGroup, sdlcLSOperLastFailTime=sdlcLSOperLastFailTime, sdlcLSOperLastFailCtrlOut=sdlcLSOperLastFailCtrlOut, sdlcLSStatsPollRspsOut=sdlcLSStatsPollRspsOut, sdlcLSAdminGPoll=sdlcLSAdminGPoll, sdlcLSStatsREJsIn=sdlcLSStatsREJsIn, sdlcPortStatsPhysicalFailures=sdlcPortStatsPhysicalFailures, sdlcPortOperTopology=sdlcPortOperTopology, sdlcMapLocalMacAddress=sdlcMapLocalMacAddress, sdlcLSAddress=sdlcLSAddress, sdlcMapRemoteMacAddress=sdlcMapRemoteMacAddress, sdlcLSOperLastFailCtrlIn=sdlcLSOperLastFailCtrlIn, sdlcPortOperType=sdlcPortOperType, sdlcLSStatsSIMsOut=sdlcLSStatsSIMsOut, sdlcLSOperState=sdlcLSOperState, sdlcLSStatsTESTsIn=sdlcLSStatsTESTsIn, sdlcLSAdminState=sdlcLSAdminState, sdlcLSOperName=sdlcLSOperName, sdlcLSStatsProtocolErrs=sdlcLSStatsProtocolErrs, sdlcPortOperACTIVTO=sdlcPortOperACTIVTO, sdlcLSStatsTESTsOut=sdlcLSStatsTESTsOut, sdlcLSOperLastFailCause=sdlcLSOperLastFailCause, sdlcLSOperMAXOUT=sdlcLSOperMAXOUT, sdlcLSOperRole=sdlcLSOperRole, sdlcMapName=sdlcMapName, sdlcLSStatsRIMsOut=sdlcLSStatsRIMsOut, sdlcLSOperLastFailREPLYTOs=sdlcLSOperLastFailREPLYTOs, sdlcLSStatsRNRLIMITs=sdlcLSStatsRNRLIMITs, MacAddress=MacAddress, sdlcLSAdminMAXOUT=sdlcLSAdminMAXOUT, sdlcLSAdminDATMODE=sdlcLSAdminDATMODE, sdlcLSAdminRETRIESm=sdlcLSAdminRETRIESm, sdlcLSStatsXIDsOut=sdlcLSStatsXIDsOut, sdlcLSStatusChange=sdlcLSStatusChange, sdlcLSStatsPollsOut=sdlcLSStatsPollsOut, sdlcMapGroup=sdlcMapGroup, sdlcPortAdminACTIVTO=sdlcPortAdminACTIVTO, sdlc=sdlc, sdlcLSGroup=sdlcLSGroup, sdlcLSStatsOctetsIn=sdlcLSStatsOctetsIn, sdlcLSOperRETRIESm=sdlcLSOperRETRIESm, sdlcPortAdminTopology=sdlcPortAdminTopology, sdlcPortOperSlowPollTimer=sdlcPortOperSlowPollTimer, sdlcLSStatsFRMRsOut=sdlcLSStatsFRMRsOut, sdlcLSStatsTable=sdlcLSStatsTable, sdlcPortAdminTable=sdlcPortAdminTable, sdlcLSOperRETRIESt=sdlcLSOperRETRIESt, sdlcLSStatsXIDsIn=sdlcLSStatsXIDsIn, sdlcLSStatsREJsOut=sdlcLSStatsREJsOut)
#
# PySNMP MIB module CISCO-AUTH-FRAMEWORK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AUTH-FRAMEWORK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
CnnEouPostureTokenString, = mibBuilder.importSymbols("CISCO-NAC-TC-MIB", "CnnEouPostureTokenString")
VlanIndexOrZero, = mibBuilder.importSymbols("CISCO-PRIVATE-VLAN-MIB", "VlanIndexOrZero")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, ifName = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifName")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, IpAddress, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, MibIdentifier, ObjectIdentity, Counter64, Integer32, Bits, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter64", "Integer32", "Bits", "iso", "NotificationType")
TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
ciscoAuthFrameworkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 656))
ciscoAuthFrameworkMIB.setRevisions(('2013-08-23 00:00', '2010-11-17 00:00', '2010-04-01 00:00', '2009-04-20 00:00', '2008-10-24 00:00', '2008-08-25 00:00',))
if mibBuilder.loadTexts: ciscoAuthFrameworkMIB.setLastUpdated('201308230000Z')
if mibBuilder.loadTexts: ciscoAuthFrameworkMIB.setOrganization('Cisco Systems Inc.')
ciscoAuthFrameworkMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 0))
ciscoAuthFrameworkMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 1))
ciscoAuthFrameworkMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 2))
ciscoAuthFrameworkSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1))
ciscoAuthFrwkAuthenticator = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2))
ciscoAuthFrameworkEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3))
ciscoAuthFrameworkSession = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4))
ciscoAuthFrwkNotifControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 5))
ciscoAuthFrwkNotifInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 6))
class CiscoAuthControlledDirections(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("both", 0), ("in", 1))

class CiscoAuthControlledPortControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forceUnauthorized", 1), ("auto", 2), ("forceAuthorized", 3))

class CiscoAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("dot1x", 2), ("macAuthBypass", 3), ("webAuth", 4))

class CiscoAuthMethodList(TextualConvention, OctetString):
    status = 'current'

class CiscoAuthHostMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("singleHost", 1), ("multiHost", 2), ("multiAuth", 3), ("multiDomain", 4))

cafAaaNoRespRecoveryDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 1), Unsigned32()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafAaaNoRespRecoveryDelay.setStatus('current')
cafAuthMethodRegTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2), )
if mibBuilder.loadTexts: cafAuthMethodRegTable.setStatus('current')
cafAuthMethodRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethod"))
if mibBuilder.loadTexts: cafAuthMethodRegEntry.setStatus('current')
cafAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2, 1, 1), CiscoAuthMethod())
if mibBuilder.loadTexts: cafAuthMethod.setStatus('current')
cafAuthMethodDefaultPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafAuthMethodDefaultPriority.setStatus('current')
cafAuthMethodDefaultExecOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafAuthMethodDefaultExecOrder.setStatus('current')
cafMacMoveMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("permit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafMacMoveMode.setStatus('current')
cafCoABouncePortCommandIgnoreEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafCoABouncePortCommandIgnoreEnabled.setStatus('current')
cafCoADisablePortCommandIgnoreEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafCoADisablePortCommandIgnoreEnabled.setStatus('current')
cafPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1), )
if mibBuilder.loadTexts: cafPortConfigTable.setStatus('current')
cafPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cafPortConfigEntry.setStatus('current')
cafPortControlledDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 1), CiscoAuthControlledDirections()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortControlledDirection.setStatus('current')
cafPortFallBackProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortFallBackProfile.setStatus('current')
cafPortAuthHostMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 3), CiscoAuthHostMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortAuthHostMode.setStatus('current')
cafPortPreAuthOpenAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortPreAuthOpenAccess.setStatus('current')
cafPortAuthorizeControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 5), CiscoAuthControlledPortControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortAuthorizeControl.setStatus('current')
cafPortReauthEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortReauthEnabled.setStatus('current')
cafPortReauthInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 7), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortReauthInterval.setStatus('current')
cafPortRestartInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortRestartInterval.setStatus('current')
cafPortInactivityTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortInactivityTimeout.setStatus('current')
cafPortViolationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("restrict", 1), ("shutdown", 2), ("protect", 3), ("replace", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortViolationAction.setStatus('current')
cafPortMethodTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2), )
if mibBuilder.loadTexts: cafPortMethodTable.setStatus('current')
cafPortMethodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cafPortMethodEntry.setStatus('current')
cafPortMethodAdminExecOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 1), CiscoAuthMethodList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortMethodAdminExecOrder.setStatus('current')
cafPortMethodAdminPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 2), CiscoAuthMethodList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafPortMethodAdminPriority.setStatus('current')
cafPortMethodAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 3), CiscoAuthMethodList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafPortMethodAvailable.setStatus('current')
cafPortMethodOperExecOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 4), CiscoAuthMethodList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafPortMethodOperExecOrder.setStatus('current')
cafPortMethodOperPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 5), CiscoAuthMethodList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafPortMethodOperPriority.setStatus('current')
cafAuthFailedEventPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1), )
if mibBuilder.loadTexts: cafAuthFailedEventPortTable.setStatus('current')
cafAuthFailedEventPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cafAuthFailedEventPortEntry.setStatus('current')
cafAuthFailedMaxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafAuthFailedMaxRetry.setStatus('current')
cafAuthFailedNoActionEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafAuthFailedNoActionEnabled.setStatus('current')
cafAuthFailedAuthorizedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafAuthFailedAuthorizedVlan.setStatus('current')
cafAuthFailedNextMethodEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafAuthFailedNextMethodEnabled.setStatus('current')
cafSecurityViolationClient = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 6, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cafSecurityViolationClient.setStatus('current')
cafAuthFailClient = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 6, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cafAuthFailClient.setStatus('current')
cafClientNoRespEventPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 2), )
if mibBuilder.loadTexts: cafClientNoRespEventPortTable.setStatus('current')
cafClientNoRespEventPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cafClientNoRespEventPortEntry.setStatus('current')
cafClientNoRespNoActionEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafClientNoRespNoActionEnabled.setStatus('current')
cafClientNoRespAuthorizedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafClientNoRespAuthorizedVlan.setStatus('current')
cafServerEventPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3), )
if mibBuilder.loadTexts: cafServerEventPortTable.setStatus('current')
cafServerEventPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cafServerEventPortEntry.setStatus('current')
cafServerDeadNoActionEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafServerDeadNoActionEnabled.setStatus('current')
cafServerDeadRemainAuthorized = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafServerDeadRemainAuthorized.setStatus('current')
cafServerDeadAuthorizedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafServerDeadAuthorizedVlan.setStatus('current')
cafServerAliveAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("reinitialize", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafServerAliveAction.setStatus('current')
cafSessionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1), )
if mibBuilder.loadTexts: cafSessionTable.setStatus('current')
cafSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (1, "CISCO-AUTH-FRAMEWORK-MIB", "cafSessionId"))
if mibBuilder.loadTexts: cafSessionEntry.setStatus('current')
cafSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cafSessionId.setStatus('current')
cafSessionClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionClientMacAddress.setStatus('current')
cafSessionClientAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionClientAddrType.setStatus('current')
cafSessionClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionClientAddress.setStatus('current')
cafSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("idle", 1), ("running", 2), ("noMethod", 3), ("authenticationSuccess", 4), ("authenticationFailed", 5), ("authorizationSuccess", 6), ("authorizationFailed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionStatus.setStatus('current')
cafSessionDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("data", 2), ("voice", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionDomain.setStatus('current')
cafSessionAuthHostMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 7), CiscoAuthHostMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionAuthHostMode.setStatus('current')
cafSessionControlledDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 8), CiscoAuthControlledDirections()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionControlledDirection.setStatus('current')
cafSessionPostureToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 9), CnnEouPostureTokenString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionPostureToken.setStatus('current')
cafSessionAuthUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionAuthUserName.setStatus('current')
cafSessionClientFramedIpPool = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionClientFramedIpPool.setStatus('current')
cafSessionAuthorizedBy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionAuthorizedBy.setStatus('current')
cafSessionCriticalTimeLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 13), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionCriticalTimeLeft.setStatus('current')
cafSessionAuthVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 14), VlanIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionAuthVlan.setStatus('current')
cafSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 15), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionTimeout.setStatus('current')
cafSessionTimeLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 16), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionTimeLeft.setStatus('current')
cafSessionTimeoutAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("terminate", 2), ("reauthenticate", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionTimeoutAction.setStatus('current')
cafSessionInactivityTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 18), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionInactivityTimeout.setStatus('current')
cafSessionInactivityTimeLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 19), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionInactivityTimeLeft.setStatus('current')
cafSessionReauth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 20), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafSessionReauth.setStatus('current')
cafSessionTerminate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 21), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafSessionTerminate.setStatus('current')
cafSessionVlanGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 22), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionVlanGroupName.setStatus('current')
cafSessionMethodsInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 2), )
if mibBuilder.loadTexts: cafSessionMethodsInfoTable.setStatus('current')
cafSessionMethodsInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-AUTH-FRAMEWORK-MIB", "cafSessionId"), (0, "CISCO-AUTH-FRAMEWORK-MIB", "cafSessionMethod"))
if mibBuilder.loadTexts: cafSessionMethodsInfoEntry.setStatus('current')
cafSessionMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 2, 1, 1), CiscoAuthMethod())
if mibBuilder.loadTexts: cafSessionMethod.setStatus('current')
cafSessionMethodState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notRun", 1), ("running", 2), ("failedOver", 3), ("authcSuccess", 4), ("authcFailed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cafSessionMethodState.setStatus('current')
cafSecurityViolationNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 5, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafSecurityViolationNotifEnable.setStatus('current')
cafAuthFailNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 5, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cafAuthFailNotifEnable.setStatus('current')
cafSecurityViolationNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 656, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationClient"))
if mibBuilder.loadTexts: cafSecurityViolationNotif.setStatus('current')
cafAuthFailNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 656, 0, 2)).setObjects(("IF-MIB", "ifName"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailClient"))
if mibBuilder.loadTexts: cafAuthFailNotif.setStatus('current')
ciscoAuthFrameworkMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1))
ciscoAuthFrameworkMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2))
ciscoAuthFrameworkMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1, 1)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethodRegGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthPortConfigGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionMethodInfoGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAaaNoRespRecoveryDelayGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafClientNoRespEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecViolationNotifEnableGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationNotifGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAuthFrameworkMIBCompliance = ciscoAuthFrameworkMIBCompliance.setStatus('deprecated')
ciscoAuthFrameworkMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1, 2)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethodRegGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthPortConfigGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionMethodInfoGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAaaNoRespRecoveryDelayGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafClientNoRespEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecViolationNotifEnableGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationNotifGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationClientGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionVlanGroupNameGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAuthFrameworkMIBCompliance2 = ciscoAuthFrameworkMIBCompliance2.setStatus('deprecated')
ciscoAuthFrameworkMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1, 3)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethodRegGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthPortConfigGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionMethodInfoGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAaaNoRespRecoveryDelayGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafClientNoRespEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecViolationNotifEnableGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationNotifGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationClientGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionVlanGroupNameGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafMacMoveConfigGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafCoACommandConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAuthFrameworkMIBCompliance3 = ciscoAuthFrameworkMIBCompliance3.setStatus('deprecated')
ciscoAuthFrameworkMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1, 4)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethodRegGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthPortConfigGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionMethodInfoGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAaaNoRespRecoveryDelayGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafClientNoRespEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerEventGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecViolationNotifEnableGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationNotifGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationClientGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionVlanGroupNameGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafMacMoveConfigGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafCoACommandConfigGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailNotifGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailNotifEnableGroup"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAuthFrameworkMIBCompliance4 = ciscoAuthFrameworkMIBCompliance4.setStatus('current')
cafAuthMethodRegGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 1)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethodDefaultPriority"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethodDefaultExecOrder"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafAuthMethodRegGroup = cafAuthMethodRegGroup.setStatus('current')
cafAaaNoRespRecoveryDelayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 2)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAaaNoRespRecoveryDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafAaaNoRespRecoveryDelayGroup = cafAaaNoRespRecoveryDelayGroup.setStatus('current')
cafAuthPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 3)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafPortControlledDirection"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortFallBackProfile"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortAuthHostMode"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortPreAuthOpenAccess"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortAuthorizeControl"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortReauthEnabled"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortReauthInterval"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortRestartInterval"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortInactivityTimeout"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortViolationAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafAuthPortConfigGroup = cafAuthPortConfigGroup.setStatus('current')
cafPortMethodGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 4)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodAdminExecOrder"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodAdminPriority"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodAvailable"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodOperExecOrder"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodOperPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafPortMethodGroup = cafPortMethodGroup.setStatus('current')
cafAuthFailedEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 5)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedMaxRetry"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedNoActionEnabled"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedAuthorizedVlan"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedNextMethodEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafAuthFailedEventGroup = cafAuthFailedEventGroup.setStatus('current')
cafClientNoRespEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 6)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafClientNoRespNoActionEnabled"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafClientNoRespAuthorizedVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafClientNoRespEventGroup = cafClientNoRespEventGroup.setStatus('current')
cafServerEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 7)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafServerDeadNoActionEnabled"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerDeadRemainAuthorized"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerDeadAuthorizedVlan"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerAliveAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafServerEventGroup = cafServerEventGroup.setStatus('current')
cafSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 8)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionClientMacAddress"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionClientAddrType"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionClientAddress"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionDomain"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionStatus"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionAuthHostMode"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionControlledDirection"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionPostureToken"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionAuthUserName"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionClientFramedIpPool"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionAuthorizedBy"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionCriticalTimeLeft"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionAuthVlan"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionTimeout"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionTimeLeft"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionTimeoutAction"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionInactivityTimeout"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionInactivityTimeLeft"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionReauth"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionTerminate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafSessionGroup = cafSessionGroup.setStatus('current')
cafSessionMethodInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 9)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionMethodState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafSessionMethodInfoGroup = cafSessionMethodInfoGroup.setStatus('current')
cafSecViolationNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 10)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafSecViolationNotifEnableGroup = cafSecViolationNotifEnableGroup.setStatus('current')
cafSecurityViolationNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 11)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafSecurityViolationNotifGroup = cafSecurityViolationNotifGroup.setStatus('current')
cafSecurityViolationClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 12)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationClient"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafSecurityViolationClientGroup = cafSecurityViolationClientGroup.setStatus('current')
cafSessionVlanGroupNameGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 13)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionVlanGroupName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafSessionVlanGroupNameGroup = cafSessionVlanGroupNameGroup.setStatus('current')
cafMacMoveConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 14)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafMacMoveMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafMacMoveConfigGroup = cafMacMoveConfigGroup.setStatus('current')
cafCoACommandConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 15)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafCoABouncePortCommandIgnoreEnabled"), ("CISCO-AUTH-FRAMEWORK-MIB", "cafCoADisablePortCommandIgnoreEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCoACommandConfigGroup = cafCoACommandConfigGroup.setStatus('current')
cafAuthFailNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 16)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafAuthFailNotifGroup = cafAuthFailNotifGroup.setStatus('current')
cafAuthFailNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 17)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafAuthFailNotifEnableGroup = cafAuthFailNotifEnableGroup.setStatus('current')
cafAuthFailClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 18)).setObjects(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailClient"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafAuthFailClientGroup = cafAuthFailClientGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-AUTH-FRAMEWORK-MIB", cafSessionDomain=cafSessionDomain, CiscoAuthMethod=CiscoAuthMethod, cafPortMethodTable=cafPortMethodTable, CiscoAuthControlledDirections=CiscoAuthControlledDirections, cafServerDeadNoActionEnabled=cafServerDeadNoActionEnabled, cafServerAliveAction=cafServerAliveAction, cafSessionAuthorizedBy=cafSessionAuthorizedBy, ciscoAuthFrwkNotifInfo=ciscoAuthFrwkNotifInfo, cafAuthPortConfigGroup=cafAuthPortConfigGroup, cafSecurityViolationNotifGroup=cafSecurityViolationNotifGroup, cafPortMethodGroup=cafPortMethodGroup, cafSessionClientAddress=cafSessionClientAddress, cafSessionEntry=cafSessionEntry, cafAuthFailNotif=cafAuthFailNotif, cafAuthMethodDefaultPriority=cafAuthMethodDefaultPriority, cafAuthFailNotifGroup=cafAuthFailNotifGroup, cafClientNoRespEventPortTable=cafClientNoRespEventPortTable, ciscoAuthFrwkAuthenticator=ciscoAuthFrwkAuthenticator, cafAuthFailedEventPortEntry=cafAuthFailedEventPortEntry, cafPortConfigTable=cafPortConfigTable, cafSessionTerminate=cafSessionTerminate, cafSessionClientAddrType=cafSessionClientAddrType, cafSessionMethodInfoGroup=cafSessionMethodInfoGroup, ciscoAuthFrameworkMIBNotifs=ciscoAuthFrameworkMIBNotifs, ciscoAuthFrameworkMIBObjects=ciscoAuthFrameworkMIBObjects, ciscoAuthFrwkNotifControl=ciscoAuthFrwkNotifControl, cafSecViolationNotifEnableGroup=cafSecViolationNotifEnableGroup, cafSessionId=cafSessionId, cafClientNoRespAuthorizedVlan=cafClientNoRespAuthorizedVlan, cafPortReauthEnabled=cafPortReauthEnabled, cafPortMethodAdminPriority=cafPortMethodAdminPriority, ciscoAuthFrameworkMIBCompliance2=ciscoAuthFrameworkMIBCompliance2, cafSecurityViolationNotifEnable=cafSecurityViolationNotifEnable, cafPortFallBackProfile=cafPortFallBackProfile, cafPortMethodEntry=cafPortMethodEntry, cafSecurityViolationClientGroup=cafSecurityViolationClientGroup, cafServerEventPortTable=cafServerEventPortTable, cafMacMoveConfigGroup=cafMacMoveConfigGroup, cafPortMethodAdminExecOrder=cafPortMethodAdminExecOrder, cafCoABouncePortCommandIgnoreEnabled=cafCoABouncePortCommandIgnoreEnabled, cafServerDeadRemainAuthorized=cafServerDeadRemainAuthorized, cafPortConfigEntry=cafPortConfigEntry, cafAuthFailNotifEnableGroup=cafAuthFailNotifEnableGroup, ciscoAuthFrameworkMIBCompliance4=ciscoAuthFrameworkMIBCompliance4, cafClientNoRespEventGroup=cafClientNoRespEventGroup, cafPortRestartInterval=cafPortRestartInterval, cafSessionMethodsInfoEntry=cafSessionMethodsInfoEntry, cafSessionReauth=cafSessionReauth, ciscoAuthFrameworkMIBConform=ciscoAuthFrameworkMIBConform, cafPortInactivityTimeout=cafPortInactivityTimeout, cafPortAuthorizeControl=cafPortAuthorizeControl, cafSessionTable=cafSessionTable, cafSessionStatus=cafSessionStatus, cafSessionTimeoutAction=cafSessionTimeoutAction, cafClientNoRespNoActionEnabled=cafClientNoRespNoActionEnabled, cafAuthFailedNextMethodEnabled=cafAuthFailedNextMethodEnabled, ciscoAuthFrameworkEvent=ciscoAuthFrameworkEvent, cafSessionGroup=cafSessionGroup, cafPortMethodAvailable=cafPortMethodAvailable, cafServerDeadAuthorizedVlan=cafServerDeadAuthorizedVlan, cafAuthFailClientGroup=cafAuthFailClientGroup, cafClientNoRespEventPortEntry=cafClientNoRespEventPortEntry, cafPortViolationAction=cafPortViolationAction, cafSessionMethodState=cafSessionMethodState, cafAuthMethodRegEntry=cafAuthMethodRegEntry, cafServerEventGroup=cafServerEventGroup, cafAuthMethodDefaultExecOrder=cafAuthMethodDefaultExecOrder, cafPortPreAuthOpenAccess=cafPortPreAuthOpenAccess, cafAuthFailClient=cafAuthFailClient, cafPortAuthHostMode=cafPortAuthHostMode, cafAuthFailedNoActionEnabled=cafAuthFailedNoActionEnabled, ciscoAuthFrameworkMIB=ciscoAuthFrameworkMIB, cafSessionTimeout=cafSessionTimeout, cafCoACommandConfigGroup=cafCoACommandConfigGroup, CiscoAuthHostMode=CiscoAuthHostMode, cafSessionTimeLeft=cafSessionTimeLeft, cafSecurityViolationNotif=cafSecurityViolationNotif, CiscoAuthControlledPortControl=CiscoAuthControlledPortControl, cafAuthMethodRegTable=cafAuthMethodRegTable, PYSNMP_MODULE_ID=ciscoAuthFrameworkMIB, cafPortMethodOperPriority=cafPortMethodOperPriority, ciscoAuthFrameworkSystem=ciscoAuthFrameworkSystem, cafAuthFailNotifEnable=cafAuthFailNotifEnable, cafSessionVlanGroupName=cafSessionVlanGroupName, cafSessionControlledDirection=cafSessionControlledDirection, ciscoAuthFrameworkMIBGroups=ciscoAuthFrameworkMIBGroups, cafAaaNoRespRecoveryDelayGroup=cafAaaNoRespRecoveryDelayGroup, cafSessionAuthVlan=cafSessionAuthVlan, cafSessionPostureToken=cafSessionPostureToken, cafAuthMethodRegGroup=cafAuthMethodRegGroup, cafAuthMethod=cafAuthMethod, cafPortMethodOperExecOrder=cafPortMethodOperExecOrder, cafAuthFailedEventPortTable=cafAuthFailedEventPortTable, cafSessionClientMacAddress=cafSessionClientMacAddress, ciscoAuthFrameworkSession=ciscoAuthFrameworkSession, cafPortControlledDirection=cafPortControlledDirection, cafSessionInactivityTimeout=cafSessionInactivityTimeout, cafAuthFailedAuthorizedVlan=cafAuthFailedAuthorizedVlan, ciscoAuthFrameworkMIBCompliance=ciscoAuthFrameworkMIBCompliance, cafSessionAuthUserName=cafSessionAuthUserName, cafSessionVlanGroupNameGroup=cafSessionVlanGroupNameGroup, cafSessionCriticalTimeLeft=cafSessionCriticalTimeLeft, cafSessionInactivityTimeLeft=cafSessionInactivityTimeLeft, cafAaaNoRespRecoveryDelay=cafAaaNoRespRecoveryDelay, cafAuthFailedMaxRetry=cafAuthFailedMaxRetry, cafMacMoveMode=cafMacMoveMode, cafPortReauthInterval=cafPortReauthInterval, cafSessionAuthHostMode=cafSessionAuthHostMode, cafSessionClientFramedIpPool=cafSessionClientFramedIpPool, cafAuthFailedEventGroup=cafAuthFailedEventGroup, cafSessionMethod=cafSessionMethod, cafCoADisablePortCommandIgnoreEnabled=cafCoADisablePortCommandIgnoreEnabled, cafServerEventPortEntry=cafServerEventPortEntry, cafSecurityViolationClient=cafSecurityViolationClient, cafSessionMethodsInfoTable=cafSessionMethodsInfoTable, ciscoAuthFrameworkMIBCompliance3=ciscoAuthFrameworkMIBCompliance3, ciscoAuthFrameworkMIBCompliances=ciscoAuthFrameworkMIBCompliances, CiscoAuthMethodList=CiscoAuthMethodList)

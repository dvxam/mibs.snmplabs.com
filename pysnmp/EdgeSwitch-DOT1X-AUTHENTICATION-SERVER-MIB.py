#
# PySNMP MIB module EdgeSwitch-DOT1X-AUTHENTICATION-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-DOT1X-AUTHENTICATION-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:56:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, Integer32, TimeTicks, MibIdentifier, NotificationType, Counter64, Unsigned32, IpAddress, iso, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Integer32", "TimeTicks", "MibIdentifier", "NotificationType", "Counter64", "Unsigned32", "IpAddress", "iso", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
fastPathdot1xAuthenticationServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49))
fastPathdot1xAuthenticationServer.setRevisions(('2011-01-26 00:00', '2009-11-12 00:00',))
if mibBuilder.loadTexts: fastPathdot1xAuthenticationServer.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathdot1xAuthenticationServer.setOrganization('Broadcom Inc')
agentDot1xAuthServUserConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1))
agentDot1xAuthServUserConfigCreate = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigCreate.setStatus('current')
agentDot1xAuthServUserConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2), )
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigTable.setStatus('current')
agentDot1xAuthServUserConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1), ).setIndexNames((0, "EdgeSwitch-DOT1X-AUTHENTICATION-SERVER-MIB", "agentDot1xAuthServUserIndex"))
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigEntry.setStatus('current')
agentDot1xAuthServUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)))
if mibBuilder.loadTexts: agentDot1xAuthServUserIndex.setStatus('current')
agentDot1xAuthServUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserName.setStatus('current')
agentDot1xAuthServUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserPassword.setStatus('current')
agentDot1xAuthServUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserStatus.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-DOT1X-AUTHENTICATION-SERVER-MIB", agentDot1xAuthServUserConfigCreate=agentDot1xAuthServUserConfigCreate, agentDot1xAuthServUserName=agentDot1xAuthServUserName, agentDot1xAuthServUserConfigGroup=agentDot1xAuthServUserConfigGroup, agentDot1xAuthServUserStatus=agentDot1xAuthServUserStatus, PYSNMP_MODULE_ID=fastPathdot1xAuthenticationServer, agentDot1xAuthServUserPassword=agentDot1xAuthServUserPassword, agentDot1xAuthServUserConfigTable=agentDot1xAuthServUserConfigTable, agentDot1xAuthServUserIndex=agentDot1xAuthServUserIndex, agentDot1xAuthServUserConfigEntry=agentDot1xAuthServUserConfigEntry, fastPathdot1xAuthenticationServer=fastPathdot1xAuthenticationServer)

#
# PySNMP MIB module EATON-EMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EATON-EMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:59:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
xupsEnvironment, = mibBuilder.importSymbols("EATON-OIDS", "xupsEnvironment")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, TimeTicks, ModuleIdentity, iso, Unsigned32, MibIdentifier, Gauge32, NotificationType, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "TimeTicks", "ModuleIdentity", "iso", "Unsigned32", "MibIdentifier", "Gauge32", "NotificationType", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eatonEMPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 534, 1, 6, 0))
eatonEMPMIB.setRevisions(('2007-03-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eatonEMPMIB.setRevisionsDescriptions(('Initial Version of eatonEMPMIB.',))
if mibBuilder.loadTexts: eatonEMPMIB.setLastUpdated('200703120000Z')
if mibBuilder.loadTexts: eatonEMPMIB.setOrganization('Eaton Corporation')
if mibBuilder.loadTexts: eatonEMPMIB.setContactInfo('Eaton Power Quality Technical Support (PQTS) group www.eaton.com/powerxpert Technical Resource Center phone numbers United States: 1.800.843.9433 or 919.870.3028 Canada: 1.800.461.9166 ext. 260 All other countries: Call your local service representative.')
if mibBuilder.loadTexts: eatonEMPMIB.setDescription('The MIB module for Eaton Environment Monitoring Probes (EMP). The elements of this MIB have been extracted from the Eaton PowerMIB and placed in this separate MIB file for convenience. Copyright (C) Eaton Corporation (2007).')
xupsEnvRemoteTemp = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 200))).setUnits('degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsEnvRemoteTemp.setStatus('current')
if mibBuilder.loadTexts: xupsEnvRemoteTemp.setDescription("The reading of an EMP's temperature sensor.")
xupsEnvRemoteHumidity = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsEnvRemoteHumidity.setStatus('current')
if mibBuilder.loadTexts: xupsEnvRemoteHumidity.setDescription("The reading of an EMP's humidity sensor.")
xupsEnvNumContacts = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsEnvNumContacts.setStatus('current')
if mibBuilder.loadTexts: xupsEnvNumContacts.setDescription('The number of Contacts in the xupsContactSenseTable. This object indicates the number of rows in the xupsContactSenseTable.')
xupsContactSenseTable = MibTable((1, 3, 6, 1, 4, 1, 534, 1, 6, 8), )
if mibBuilder.loadTexts: xupsContactSenseTable.setStatus('current')
if mibBuilder.loadTexts: xupsContactSenseTable.setDescription('A list of Contact Sensing table entries. The number of entries is given by the value of xupsEnvNumContacts.')
xupsContactsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1), ).setIndexNames((0, "EATON-EMP-MIB", "xupsContactIndex"))
if mibBuilder.loadTexts: xupsContactsTableEntry.setStatus('current')
if mibBuilder.loadTexts: xupsContactsTableEntry.setDescription('An entry containing information applicable to a particular Contact input.')
xupsContactIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsContactIndex.setStatus('current')
if mibBuilder.loadTexts: xupsContactIndex.setDescription('The Contact identifier; identical to the Contact Number. This object is not-accessible to MIB browsers, but had to be changed to read-only to satisfy SMIv2 syntax checkers if it is included in traps.')
xupsContactType = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normallyOpen", 1), ("normallyClosed", 2), ("anyChange", 3), ("notUsed", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsContactType.setStatus('current')
if mibBuilder.loadTexts: xupsContactType.setDescription("The normal state for this contact. The 'other' (not 'Normally') state is the Active state for generating the xupstdContactActiveNotice trap. If anyChange(3) is selected, then this trap is sent any time the contact changes to either Open or Closed. No traps are sent if the Contact is set to notUsed(4). In many cases, the configuration for Contacts may be done by other means, so this object may be read-only.")
xupsContactState = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("openWithNotice", 3), ("closedWithNotice", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xupsContactState.setStatus('current')
if mibBuilder.loadTexts: xupsContactState.setDescription('The current state of the Contact input; the value is based on the open/closed input state and the setting for xupsContactType. When entering the openWithNotice(3) and closedWithNotice(4) states, no entries added to the xupsAlarmTable, but the xupstdContactActiveNotice trap is sent.')
xupsContactDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsContactDescr.setStatus('current')
if mibBuilder.loadTexts: xupsContactDescr.setDescription('A label identifying the Contact. This object should be set by the administrator.')
xupsEnvRemoteTempLowerLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 200))).setUnits('degrees Centigrade').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsEnvRemoteTempLowerLimit.setStatus('current')
if mibBuilder.loadTexts: xupsEnvRemoteTempLowerLimit.setDescription('The Lower Limit of the EMP temperature; if xupsEnvRemoteTemp falls below this value, the xupsRemoteTempBad alarm will occur.')
xupsEnvRemoteTempUpperLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 200))).setUnits('degrees Centigrade').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsEnvRemoteTempUpperLimit.setStatus('current')
if mibBuilder.loadTexts: xupsEnvRemoteTempUpperLimit.setDescription('The Upper Limit of the EMP temperature; if xupsEnvRemoteTemp rises above this value, the xupsRemoteTempBad alarm will occur. This value should be greater than xupsEnvRemoteTempLowerLimit.')
xupsEnvRemoteHumidityLowerLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsEnvRemoteHumidityLowerLimit.setStatus('current')
if mibBuilder.loadTexts: xupsEnvRemoteHumidityLowerLimit.setDescription('The Lower Limit of the EMP humidity reading; if xupsEnvRemoteHumidity falls below this value, the xupsRemoteHumidityBad alarm will occur.')
xupsEnvRemoteHumidityUpperLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 1, 6, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xupsEnvRemoteHumidityUpperLimit.setStatus('current')
if mibBuilder.loadTexts: xupsEnvRemoteHumidityUpperLimit.setDescription('The Upper Limit of the EMP humidity reading; if xupsEnvRemoteHumidity rises above this value, the xupsRemoteHumidityBad alarm will occur. This value should be greater than xupsEnvRemoteHumidityLowerLimit.')
eatonEMPConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2))
eatonEMPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2, 1)).setObjects(("EATON-EMP-MIB", "xupsEnvRemoteTemp"), ("EATON-EMP-MIB", "xupsEnvRemoteHumidity"), ("EATON-EMP-MIB", "xupsEnvRemoteTempLowerLimit"), ("EATON-EMP-MIB", "xupsEnvRemoteTempUpperLimit"), ("EATON-EMP-MIB", "xupsEnvRemoteHumidityLowerLimit"), ("EATON-EMP-MIB", "xupsEnvRemoteHumidityUpperLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eatonEMPGroup = eatonEMPGroup.setStatus('current')
if mibBuilder.loadTexts: eatonEMPGroup.setDescription('The EMP scalar objects.')
eatonEMPTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2, 2)).setObjects(("EATON-EMP-MIB", "xupsEnvNumContacts"), ("EATON-EMP-MIB", "xupsContactIndex"), ("EATON-EMP-MIB", "xupsContactType"), ("EATON-EMP-MIB", "xupsContactState"), ("EATON-EMP-MIB", "xupsContactDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eatonEMPTableGroup = eatonEMPTableGroup.setStatus('current')
if mibBuilder.loadTexts: eatonEMPTableGroup.setDescription('The EMP Contacts Table objects.')
eatonEMPSimpleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2, 4)).setObjects(("EATON-EMP-MIB", "eatonEMPGroup"), ("EATON-EMP-MIB", "eatonEMPTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eatonEMPSimpleCompliance = eatonEMPSimpleCompliance.setStatus('current')
if mibBuilder.loadTexts: eatonEMPSimpleCompliance.setDescription('The compliance statement for a normal EMP.')
mibBuilder.exportSymbols("EATON-EMP-MIB", xupsEnvRemoteHumidityUpperLimit=xupsEnvRemoteHumidityUpperLimit, xupsContactDescr=xupsContactDescr, xupsEnvRemoteHumidityLowerLimit=xupsEnvRemoteHumidityLowerLimit, xupsEnvNumContacts=xupsEnvNumContacts, xupsContactsTableEntry=xupsContactsTableEntry, xupsEnvRemoteHumidity=xupsEnvRemoteHumidity, eatonEMPGroup=eatonEMPGroup, xupsContactIndex=xupsContactIndex, eatonEMPTableGroup=eatonEMPTableGroup, eatonEMPSimpleCompliance=eatonEMPSimpleCompliance, xupsEnvRemoteTemp=xupsEnvRemoteTemp, xupsEnvRemoteTempUpperLimit=xupsEnvRemoteTempUpperLimit, xupsContactType=xupsContactType, xupsEnvRemoteTempLowerLimit=xupsEnvRemoteTempLowerLimit, eatonEMPConformance=eatonEMPConformance, xupsContactState=xupsContactState, PYSNMP_MODULE_ID=eatonEMPMIB, xupsContactSenseTable=xupsContactSenseTable, eatonEMPMIB=eatonEMPMIB)
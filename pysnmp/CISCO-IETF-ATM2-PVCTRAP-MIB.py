#
# PySNMP MIB module CISCO-IETF-ATM2-PVCTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-ATM2-PVCTRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
atmInterfaceConfEntry, atmVclVci, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmInterfaceConfEntry", "atmVclVci", "atmVclVpi")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Gauge32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Counter64, Unsigned32, Counter32, iso, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Counter64", "Unsigned32", "Counter32", "iso", "Bits", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "TruthValue")
ciscoIetfAtm2PvctrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 29))
if mibBuilder.loadTexts: ciscoIetfAtm2PvctrapMIB.setLastUpdated('9802030000Z')
if mibBuilder.loadTexts: ciscoIetfAtm2PvctrapMIB.setOrganization('Cisco Systems, Inc.')
atm2MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 1))
atm2MIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 2))
atmInterfaceExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14), )
if mibBuilder.loadTexts: atmInterfaceExtTable.setStatus('current')
atmInterfaceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1), )
atmInterfaceConfEntry.registerAugmentions(("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmInterfaceExtEntry"))
atmInterfaceExtEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
if mibBuilder.loadTexts: atmInterfaceExtEntry.setStatus('current')
atmIntfPvcFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmIntfPvcFailures.setStatus('current')
atmIntfCurrentlyFailingPVcls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 22), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmIntfCurrentlyFailingPVcls.setStatus('current')
atmIntfPvcFailuresTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 23), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmIntfPvcFailuresTrapEnable.setStatus('current')
atmIntfPvcNotificationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmIntfPvcNotificationInterval.setStatus('current')
atmPreviouslyFailedPVclInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPreviouslyFailedPVclInterval.setStatus('current')
atmCurrentlyFailingPVclTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21), )
if mibBuilder.loadTexts: atmCurrentlyFailingPVclTable.setStatus('current')
atmCurrentlyFailingPVclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: atmCurrentlyFailingPVclEntry.setStatus('current')
atmCurrentlyFailingPVclTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCurrentlyFailingPVclTimeStamp.setStatus('current')
atmPreviouslyFailedPVclTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPreviouslyFailedPVclTimeStamp.setStatus('current')
atmPvcTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 2, 1))
atmPvcTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 2, 1, 0))
atmIntfPvcFailuresTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 29, 2, 1, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailures"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfCurrentlyFailingPVcls"))
if mibBuilder.loadTexts: atmIntfPvcFailuresTrap.setStatus('current')
atm2MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 3))
atm2MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 1))
atm2MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 2))
atm2MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 2, 1)).setObjects(("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmSwitchServcHostGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atm2MIBCompliance = atm2MIBCompliance.setStatus('current')
atmSwitchServcHostGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 1, 1)).setObjects(("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailures"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfCurrentlyFailingPVcls"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailuresTrapEnable"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcNotificationInterval"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmPreviouslyFailedPVclInterval"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmCurrentlyFailingPVclTimeStamp"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmPreviouslyFailedPVclTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSwitchServcHostGroup = atmSwitchServcHostGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-ATM2-PVCTRAP-MIB", atmIntfPvcFailures=atmIntfPvcFailures, atm2MIBGroups=atm2MIBGroups, atmCurrentlyFailingPVclEntry=atmCurrentlyFailingPVclEntry, atm2MIBConformance=atm2MIBConformance, atmPvcTraps=atmPvcTraps, atmCurrentlyFailingPVclTimeStamp=atmCurrentlyFailingPVclTimeStamp, PYSNMP_MODULE_ID=ciscoIetfAtm2PvctrapMIB, atm2MIBCompliances=atm2MIBCompliances, atmPreviouslyFailedPVclInterval=atmPreviouslyFailedPVclInterval, atmIntfPvcFailuresTrapEnable=atmIntfPvcFailuresTrapEnable, atmPvcTrapsPrefix=atmPvcTrapsPrefix, atmInterfaceExtEntry=atmInterfaceExtEntry, atmPreviouslyFailedPVclTimeStamp=atmPreviouslyFailedPVclTimeStamp, ciscoIetfAtm2PvctrapMIB=ciscoIetfAtm2PvctrapMIB, atm2MIBCompliance=atm2MIBCompliance, atm2MIBObjects=atm2MIBObjects, atmInterfaceExtTable=atmInterfaceExtTable, atmIntfPvcNotificationInterval=atmIntfPvcNotificationInterval, atmIntfCurrentlyFailingPVcls=atmIntfCurrentlyFailingPVcls, atmSwitchServcHostGroup=atmSwitchServcHostGroup, atm2MIBTraps=atm2MIBTraps, atmIntfPvcFailuresTrap=atmIntfPvcFailuresTrap, atmCurrentlyFailingPVclTable=atmCurrentlyFailingPVclTable)

#
# PySNMP MIB module NSMAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NSMAIL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Counter64, NotificationType, Counter32, iso, Unsigned32, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, TimeTicks, enterprises, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Counter64", "NotificationType", "Counter32", "iso", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "TimeTicks", "enterprises", "Bits")
DisplayString, TimeInterval, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeInterval", "TextualConvention")
netscape = MibIdentifier((1, 3, 6, 1, 4, 1, 1450))
nsmail = ModuleIdentity((1, 3, 6, 1, 4, 1, 1450, 5))
if mibBuilder.loadTexts: nsmail.setLastUpdated('9706021700Z')
if mibBuilder.loadTexts: nsmail.setOrganization('Netscape Communications Corp.')
nsmailEntityInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1450, 5, 1))
nsmailEntityDescr = MibScalar((1, 3, 6, 1, 4, 1, 1450, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsmailEntityDescr.setStatus('mandatory')
nsmailEntityVers = MibScalar((1, 3, 6, 1, 4, 1, 1450, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsmailEntityVers.setStatus('mandatory')
nsmailEntityOrg = MibScalar((1, 3, 6, 1, 4, 1, 1450, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsmailEntityOrg.setStatus('mandatory')
nsmailEntityLocation = MibScalar((1, 3, 6, 1, 4, 1, 1450, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsmailEntityLocation.setStatus('mandatory')
nsmailEntityContact = MibScalar((1, 3, 6, 1, 4, 1, 1450, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsmailEntityContact.setStatus('mandatory')
nsmailEntityName = MibScalar((1, 3, 6, 1, 4, 1, 1450, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsmailEntityName.setStatus('mandatory')
mtaTable = MibTable((1, 3, 6, 1, 4, 1, 1450, 5, 2), )
if mibBuilder.loadTexts: mtaTable.setStatus('mandatory')
mtaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1), ).setIndexNames((0, "NSMAIL-MIB", "mtaId"))
if mibBuilder.loadTexts: mtaEntry.setStatus('mandatory')
mtaReceivedMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaReceivedMessages.setStatus('mandatory')
mtaStoredMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaStoredMessages.setStatus('mandatory')
mtaTransmittedMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaTransmittedMessages.setStatus('mandatory')
mtaReceivedVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaReceivedVolume.setStatus('mandatory')
mtaStoredVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaStoredVolume.setStatus('mandatory')
mtaTransmittedVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaTransmittedVolume.setStatus('mandatory')
mtaReceivedRecipients = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaReceivedRecipients.setStatus('mandatory')
mtaStoredRecipients = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaStoredRecipients.setStatus('mandatory')
mtaTransmittedRecipients = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaTransmittedRecipients.setStatus('mandatory')
mtaId = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaId.setStatus('mandatory')
nsMailServerDown = NotificationType((1, 3, 6, 1, 4, 1, 1450) + (0,5001)).setObjects(("NSMAIL-MIB", "nsmailEntityDescr"), ("NSMAIL-MIB", "nsmailEntityVers"), ("NSMAIL-MIB", "nsmailEntityLocation"), ("NSMAIL-MIB", "nsmailEntityContact"))
nsMailServerStart = NotificationType((1, 3, 6, 1, 4, 1, 1450) + (0,5002)).setObjects(("NSMAIL-MIB", "nsmailEntityDescr"), ("NSMAIL-MIB", "nsmailEntityVers"), ("NSMAIL-MIB", "nsmailEntityLocation"))
nsMailServerNoResponse = NotificationType((1, 3, 6, 1, 4, 1, 1450) + (0,5003)).setObjects(("NSMAIL-MIB", "nsmailEntityDescr"), ("NSMAIL-MIB", "nsmailEntityVers"), ("NSMAIL-MIB", "nsmailEntityLocation"), ("NSMAIL-MIB", "nsmailEntityContact"))
mibBuilder.exportSymbols("NSMAIL-MIB", mtaTransmittedMessages=mtaTransmittedMessages, PYSNMP_MODULE_ID=nsmail, nsmailEntityContact=nsmailEntityContact, mtaStoredMessages=mtaStoredMessages, nsmailEntityLocation=nsmailEntityLocation, mtaReceivedMessages=mtaReceivedMessages, mtaReceivedRecipients=mtaReceivedRecipients, mtaEntry=mtaEntry, mtaStoredVolume=mtaStoredVolume, mtaId=mtaId, nsmailEntityOrg=nsmailEntityOrg, nsmailEntityName=nsmailEntityName, mtaTable=mtaTable, nsmailEntityInfo=nsmailEntityInfo, nsmailEntityVers=nsmailEntityVers, nsmail=nsmail, nsmailEntityDescr=nsmailEntityDescr, netscape=netscape, mtaStoredRecipients=mtaStoredRecipients, mtaTransmittedRecipients=mtaTransmittedRecipients, nsMailServerNoResponse=nsMailServerNoResponse, mtaTransmittedVolume=mtaTransmittedVolume, nsMailServerDown=nsMailServerDown, mtaReceivedVolume=mtaReceivedVolume, nsMailServerStart=nsMailServerStart)

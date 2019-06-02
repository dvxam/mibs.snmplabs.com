#
# PySNMP MIB module CISCO-ISDNU-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ISDNU-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:03:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, ModuleIdentity, Counter32, MibIdentifier, Gauge32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, iso, NotificationType, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Counter32", "MibIdentifier", "Gauge32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "iso", "NotificationType", "Counter64", "Integer32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoIsdnuIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 18))
if mibBuilder.loadTexts: ciscoIsdnuIfMIB.setLastUpdated('9603180000Z')
if mibBuilder.loadTexts: ciscoIsdnuIfMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIsdnuIfMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-isdn@cisco.com')
if mibBuilder.loadTexts: ciscoIsdnuIfMIB.setDescription('ISDN BRI integrated U Interface MIB module. This MIB manages the ISDN BRI integrated U Interface in the router. ')
ciuIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 18, 1))
ciuInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1))
ciuIfExternalSTPort = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2))
ciuIfMIBNotificationEnables = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 3))
ciuIfStaticConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 1), )
if mibBuilder.loadTexts: ciuIfStaticConfigTable.setStatus('current')
if mibBuilder.loadTexts: ciuIfStaticConfigTable.setDescription('The ISDN BRI integrated U interface Static Configuration Table. It contains items that are statically configured by reading configuration from hardware and can not be changed by end user without physically changing the U Interface.')
ciuIfStaticConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ciuIfStaticConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ciuIfStaticConfigEntry.setDescription('An entry in the static configuration table for each ISDN BRI integrated U interface.')
ciuIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("addOnU", 2), ("onBoardU", 3), ("onBoardIntegUandSTPort", 4), ("addOnIntegUandSTPort", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuIfType.setStatus('current')
if mibBuilder.loadTexts: ciuIfType.setDescription('Specifies the type of ISDN BRI integrated U interface. other - none of the following. addOnU - An add-On card with ISDN BRI integrated U interface. onBoardU - An on board ISDN BRI integrated U interface onBoardIntegUandSTPort - An on board BRI integrated U interface with external S/T ports. addOnIntegUandSTPort - An add-on card with ISDN BRI integrated U interface and S/T port. ')
ciuIfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2), )
if mibBuilder.loadTexts: ciuIfStatusTable.setStatus('current')
if mibBuilder.loadTexts: ciuIfStatusTable.setDescription('The ISDN BRI integrated U interface Status Table. Contains information about the status of the ISDN U interface, including the error statistics and current active EOC (Embedded operations channel) commands from CO (Central office). ')
ciuIfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ciuIfStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ciuIfStatusEntry.setDescription('An entry in the status table for each ISDN BRI integrated U interface.')
ciuIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("activated", 1), ("activationPending", 2), ("deactivated", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuIfStatus.setStatus('current')
if mibBuilder.loadTexts: ciuIfStatus.setDescription('This object contains the operation status of the ISDN BRI integrated U interface. activated - The ISDN U interface is activated. The interface is active and data can be transmitted and received through the interface. activationPending - The ISDN U interface is in activation pending state. Either the CO or the router has initiated activation of U interface, but activation has not yet completed. Data cannot be transmitted or received. deactivated - The ISDN U interface is deactivated. The ISDN line to the CO is deactivated. Data cannot be transmitted or received on the ISDN U interface. ')
ciuIfEocCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuIfEocCommand.setReference('ANSI T1.601-1992: Sections 8.3 Embedded operations channel (eoc) functions')
if mibBuilder.loadTexts: ciuIfEocCommand.setStatus('current')
if mibBuilder.loadTexts: ciuIfEocCommand.setDescription('The last EOC command sent by Central Office; the ECO command supports operations communications needs between the network and ISDN U interface.')
ciuIfOverHeadBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuIfOverHeadBits.setReference('ANSI T1.601-1992: Sections 8.2 Overhead bit functions')
if mibBuilder.loadTexts: ciuIfOverHeadBits.setStatus('current')
if mibBuilder.loadTexts: ciuIfOverHeadBits.setDescription('This object describes 5 attributes of Overhead bits. The Overhead bits contains the ISDN U interface transceiver operations and maintenance functions that are handled by M4, M5 and M6 bits in the superframe. These bits are described as follows: act - start-up bit; this bit is set to binary ONE by the network as a part of the start-up sequence to communicate readiness for layer-2 communication. dea - turn-off bit; this bit is set to binary ZERO by the network to communicate to the NT its intention to turn off. febe - Far End Block Error bit; this bit is set to binary ONE if there are no error in the superframe and binary ZERO if the superframe contains an error. uoa - U interface only activation bit; This bit is set to binary ONE if the S/T interface should be activated. Otherwise, this bit should be set to binary ZERO. aib - Alarm indication bit; this bit is set to binary ONE if the transmission path for D, B1, and B2 channels has been established all the way to the local exchange. Otherwise, this bit is set to binary ZERO. ')
ciuIfFebeErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuIfFebeErrors.setStatus('current')
if mibBuilder.loadTexts: ciuIfFebeErrors.setDescription('Number of Far End Block Errors (FEBE) detected since last boot. Whenever the CO (Central Office) receives a block of data from the router with a CRC error, the FEBE count is incremented by one.')
ciuIfNebeErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuIfNebeErrors.setStatus('current')
if mibBuilder.loadTexts: ciuIfNebeErrors.setDescription('Number of Near End Block Errors (NEBE) detected since last boot. Whenever the U transceiver receives a block of data with a CRC error, the NEBE count is incremented by one.')
ciuIfLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("type2Loopback", 2), ("type3Loopback", 3), ("ntQuietMode", 4), ("ilmtMode", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuIfLoopStatus.setReference('ANSI T1.601-1992: Sections 6.5 NT maintence modes')
if mibBuilder.loadTexts: ciuIfLoopStatus.setStatus('current')
if mibBuilder.loadTexts: ciuIfLoopStatus.setDescription('Current ISDN BRI integrated U interface Loop status and NT maintenance mode. The definition of maintenance modes are as follows: none - The U interface is not in either Loopback or maintenance mode. type2Loopback - Type 2 (CO to U interface) Loopback mode; this mode is set to perform the loopback between CO and the ISDN BRI integrated U interface. type3Loopback - Type 3 (processor to U interface) Loopback mode; this mode is set by router to perform the loopback between the router processor and the ISDN BRI integrated U interface. ntQuietMode - NT quiet mode; this mode is set by CO for metallic loop tests. In the NT quiet mode, the ISDN U interface will not attempt a start-up or will not initiate transmission during metallic loop tests conducted by the network. ilmtMode - Insertion loss measurement test (ILMT); this mode is set by CO for the Insertion loss measurement test. The insertion loss measurement test will cause a known test signal to be generated by the NT. This test will be used in network measurements of DSL (Digital Subscriber Line) transmission characteristics. ')
ciuIfExternalSTPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2, 1), )
if mibBuilder.loadTexts: ciuIfExternalSTPortStatusTable.setStatus('current')
if mibBuilder.loadTexts: ciuIfExternalSTPortStatusTable.setDescription('The external S/T port status table. It contains the operation status of the external ISDN S/T ports.')
ciuIfExternalSTPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ISDNU-IF-MIB", "ciuIfExternalSTPortNumber"))
if mibBuilder.loadTexts: ciuIfExternalSTPortStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ciuIfExternalSTPortStatusEntry.setDescription('An entry in the status table for each external ISDN S/T port.')
ciuIfExternalSTPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: ciuIfExternalSTPortNumber.setStatus('current')
if mibBuilder.loadTexts: ciuIfExternalSTPortNumber.setDescription('The external ISDN S/T port number.')
ciuIfExternalSTPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("activated", 1), ("activationPending", 2), ("deactivated", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuIfExternalSTPortStatus.setStatus('current')
if mibBuilder.loadTexts: ciuIfExternalSTPortStatus.setDescription('This object contains the operation status of the external ISDN S/T port. activated - The external ISDN S/T port is activated. The port is active and data can be transmitted and received on the port. activationPending - The external ISDN S/T port is in activation pending state. Either the CO or the router has initiated activation of the port, but activation has not yet completed. Data cannot be transmitted or received. deactivated - The external ISDN S/T port is deactivated. Either no ISDN device is attached to the external S/T port or the ISDN line to the CO is deactivated. Data cannot be transmitted or received on the S/T port. ')
ciuIfEnableULoopStatusNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciuIfEnableULoopStatusNotification.setStatus('current')
if mibBuilder.loadTexts: ciuIfEnableULoopStatusNotification.setDescription('Indicates whether or not an ISDN BRI integrated U interface Loop status notification (ciuIfLoopStatusNotification) will be generated by this router.')
ciuIfMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 18, 2))
ciuIfMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 18, 2, 0))
ciuIfLoopStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 18, 2, 0, 1)).setObjects(("CISCO-ISDNU-IF-MIB", "ciuIfLoopStatus"))
if mibBuilder.loadTexts: ciuIfLoopStatusNotification.setStatus('current')
if mibBuilder.loadTexts: ciuIfLoopStatusNotification.setDescription(' A ciuIfLoopStatusNotification is sent when there is a change in ciscoIsdnuIfLoopStatus object. The status change occurs when the ISDN BRI integrated U interface enters into or exits from Loopback or Maintenance modes. ')
ciuIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 18, 3))
ciuIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 18, 3, 1))
ciuIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 18, 3, 2))
ciuIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 18, 3, 1, 1)).setObjects(("CISCO-ISDNU-IF-MIB", "ciuIfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuIfMIBCompliance = ciuIfMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciuIfMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco ISDN BRI integrated U interface MIB')
ciuIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 18, 3, 2, 1)).setObjects(("CISCO-ISDNU-IF-MIB", "ciuIfType"), ("CISCO-ISDNU-IF-MIB", "ciuIfStatus"), ("CISCO-ISDNU-IF-MIB", "ciuIfEocCommand"), ("CISCO-ISDNU-IF-MIB", "ciuIfOverHeadBits"), ("CISCO-ISDNU-IF-MIB", "ciuIfFebeErrors"), ("CISCO-ISDNU-IF-MIB", "ciuIfNebeErrors"), ("CISCO-ISDNU-IF-MIB", "ciuIfLoopStatus"), ("CISCO-ISDNU-IF-MIB", "ciuIfExternalSTPortStatus"), ("CISCO-ISDNU-IF-MIB", "ciuIfEnableULoopStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuIfMIBGroup = ciuIfMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciuIfMIBGroup.setDescription('The collection of objects providing information about the Cisco ISDN BRI integrated U interface.')
mibBuilder.exportSymbols("CISCO-ISDNU-IF-MIB", ciuInterface=ciuInterface, ciuIfStatusEntry=ciuIfStatusEntry, ciuIfFebeErrors=ciuIfFebeErrors, ciuIfExternalSTPortStatus=ciuIfExternalSTPortStatus, ciuIfMIBConformance=ciuIfMIBConformance, ciuIfMIBGroup=ciuIfMIBGroup, ciuIfMIBCompliance=ciuIfMIBCompliance, ciuIfObjects=ciuIfObjects, ciuIfMIBNotifications=ciuIfMIBNotifications, ciuIfStatus=ciuIfStatus, ciuIfExternalSTPortNumber=ciuIfExternalSTPortNumber, ciuIfStatusTable=ciuIfStatusTable, ciuIfMIBGroups=ciuIfMIBGroups, ciuIfEocCommand=ciuIfEocCommand, ciuIfMIBNotificationEnables=ciuIfMIBNotificationEnables, ciuIfMIBCompliances=ciuIfMIBCompliances, ciuIfType=ciuIfType, ciuIfMIBNotificationPrefix=ciuIfMIBNotificationPrefix, ciscoIsdnuIfMIB=ciscoIsdnuIfMIB, ciuIfExternalSTPortStatusTable=ciuIfExternalSTPortStatusTable, ciuIfEnableULoopStatusNotification=ciuIfEnableULoopStatusNotification, ciuIfLoopStatusNotification=ciuIfLoopStatusNotification, ciuIfLoopStatus=ciuIfLoopStatus, ciuIfStaticConfigEntry=ciuIfStaticConfigEntry, ciuIfExternalSTPort=ciuIfExternalSTPort, ciuIfOverHeadBits=ciuIfOverHeadBits, ciuIfExternalSTPortStatusEntry=ciuIfExternalSTPortStatusEntry, ciuIfNebeErrors=ciuIfNebeErrors, PYSNMP_MODULE_ID=ciscoIsdnuIfMIB, ciuIfStaticConfigTable=ciuIfStaticConfigTable)
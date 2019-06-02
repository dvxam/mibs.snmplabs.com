#
# PySNMP MIB module IBM-SVC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBM-SVC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:51:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, enterprises, TimeTicks, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, iso, Bits, IpAddress, NotificationType, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "enterprises", "TimeTicks", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "iso", "Bits", "IpAddress", "NotificationType", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm2145TSVE = ModuleIdentity((1, 3, 6, 1, 4, 1, 2, 6, 190))
ibm2145TSVE.setRevisions(('2017-01-12 00:00', '2016-11-01 00:00', '2016-07-14 00:00', '2016-04-28 00:00', '2016-01-22 00:00', '2015-11-25 00:00', '2015-04-17 00:00', '2014-09-01 00:00', '2013-09-24 00:00', '2013-09-24 00:00', '2013-09-24 00:00', '2012-11-06 00:00', '2012-04-19 00:00', '2011-05-26 00:00', '2011-05-26 00:00', '2010-05-07 00:00', '2009-09-01 00:00', '2008-05-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibm2145TSVE.setRevisionsDescriptions(('IBM San Volume Controller MIB for SVC 7.8.1 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.8.1 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 7.8.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.8.0 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 7.7.1 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.7.1 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 7.7.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.7.0 release. The tsveIDAL object has been defined since the previous release.', 'IBM San Volume Controller MIB for SVC 7.6.1 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.6.1 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 7.6.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.6.0 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 7.5.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.5.0 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 7.4.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.4.0 release. There have been no additional objects defined. A typo was fixed in the derived type name SnmpAdminString of the tsveOBJN object definition.', 'IBM San Volume Controller MIB for SVC 7.3.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.3.0 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 7.2.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.2.0 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 7.1.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 7.1.0 release. The tsveOBJN object has been defined since the previous release.', 'IBM San Volume Controller MIB for SVC 6.4.1 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 6.4.1 release. The tsveMPNO object has been defined since the previous release.', 'IBM San Volume Controller MIB for SVC 6.4.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 6.4.0 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 6.3.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 6.3.0 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 6.2.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 6.2.0 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 6.1.0 The SVC MIB has been renamed to indicate that it is for SVC Lodestone 6.1.0 release. There have been no additional objects defined.', 'IBM San Volume Controller MIB for SVC 5.1.0 The SVC MIB has been extensively tidied within this release. The MIB label has been corrected to IBM-SVC-MIB. This name will be maintained in future releases. There have been no additional objects defined.', 'IBM TSVE MIB for SVC 4.3.1 A number of previous TSVE (SVC) MIB revisions exist. The tsveADD1, tsveADD2 and tsveCOPY objects have been defined since the original release.',))
if mibBuilder.loadTexts: ibm2145TSVE.setLastUpdated('201701120000Z')
if mibBuilder.loadTexts: ibm2145TSVE.setOrganization('IBM SSG')
if mibBuilder.loadTexts: ibm2145TSVE.setContactInfo('Contact IBM Support')
if mibBuilder.loadTexts: ibm2145TSVE.setDescription('This file defines the private IBM SAN Volume Controller (previously TSVE) MIB extensions used to receive traps from SVC ')
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibm2145TSVEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 190, 4))
ibm2145TSVEConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 190, 5))
tsveETrap = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 190, 1)).setObjects(("IBM-SVC-MIB", "tsveMACH"), ("IBM-SVC-MIB", "tsveSERI"), ("IBM-SVC-MIB", "tsveERRI"), ("IBM-SVC-MIB", "tsveERRC"), ("IBM-SVC-MIB", "tsveSWVE"), ("IBM-SVC-MIB", "tsveFRUP"), ("IBM-SVC-MIB", "tsveCLUS"), ("IBM-SVC-MIB", "tsveNODE"), ("IBM-SVC-MIB", "tsveERRS"), ("IBM-SVC-MIB", "tsveTIME"), ("IBM-SVC-MIB", "tsveOBJT"), ("IBM-SVC-MIB", "tsveOBJI"), ("IBM-SVC-MIB", "tsveADD1"), ("IBM-SVC-MIB", "tsveADD2"), ("IBM-SVC-MIB", "tsveCOPY"), ("IBM-SVC-MIB", "tsveMPNO"), ("IBM-SVC-MIB", "tsveOBJN"), ("IBM-SVC-MIB", "tsveIDAL"))
if mibBuilder.loadTexts: tsveETrap.setStatus('current')
if mibBuilder.loadTexts: tsveETrap.setDescription('tsve error trap')
tsveWTrap = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 190, 2)).setObjects(("IBM-SVC-MIB", "tsveMACH"), ("IBM-SVC-MIB", "tsveSERI"), ("IBM-SVC-MIB", "tsveERRI"), ("IBM-SVC-MIB", "tsveERRC"), ("IBM-SVC-MIB", "tsveSWVE"), ("IBM-SVC-MIB", "tsveFRUP"), ("IBM-SVC-MIB", "tsveCLUS"), ("IBM-SVC-MIB", "tsveNODE"), ("IBM-SVC-MIB", "tsveERRS"), ("IBM-SVC-MIB", "tsveTIME"), ("IBM-SVC-MIB", "tsveOBJT"), ("IBM-SVC-MIB", "tsveOBJI"), ("IBM-SVC-MIB", "tsveADD1"), ("IBM-SVC-MIB", "tsveADD2"), ("IBM-SVC-MIB", "tsveCOPY"), ("IBM-SVC-MIB", "tsveMPNO"), ("IBM-SVC-MIB", "tsveOBJN"), ("IBM-SVC-MIB", "tsveIDAL"))
if mibBuilder.loadTexts: tsveWTrap.setStatus('current')
if mibBuilder.loadTexts: tsveWTrap.setDescription('tsve warning trap')
tsveITrap = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 190, 3)).setObjects(("IBM-SVC-MIB", "tsveMACH"), ("IBM-SVC-MIB", "tsveSERI"), ("IBM-SVC-MIB", "tsveERRI"), ("IBM-SVC-MIB", "tsveERRC"), ("IBM-SVC-MIB", "tsveSWVE"), ("IBM-SVC-MIB", "tsveFRUP"), ("IBM-SVC-MIB", "tsveCLUS"), ("IBM-SVC-MIB", "tsveNODE"), ("IBM-SVC-MIB", "tsveERRS"), ("IBM-SVC-MIB", "tsveTIME"), ("IBM-SVC-MIB", "tsveOBJT"), ("IBM-SVC-MIB", "tsveOBJI"), ("IBM-SVC-MIB", "tsveADD1"), ("IBM-SVC-MIB", "tsveADD2"), ("IBM-SVC-MIB", "tsveCOPY"), ("IBM-SVC-MIB", "tsveMPNO"), ("IBM-SVC-MIB", "tsveOBJN"), ("IBM-SVC-MIB", "tsveIDAL"))
if mibBuilder.loadTexts: tsveITrap.setStatus('current')
if mibBuilder.loadTexts: tsveITrap.setDescription('tsve information trap')
tsveMACH = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 1), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveMACH.setStatus('current')
if mibBuilder.loadTexts: tsveMACH.setDescription('IBM TSVE machine type')
tsveSERI = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveSERI.setStatus('current')
if mibBuilder.loadTexts: tsveSERI.setDescription('IBM TSVE serial number')
tsveERRI = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveERRI.setStatus('current')
if mibBuilder.loadTexts: tsveERRI.setDescription('IBM TSVE error ID')
tsveERRC = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 4), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveERRC.setStatus('current')
if mibBuilder.loadTexts: tsveERRC.setDescription('IBM TSVE error code')
tsveSWVE = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 5), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveSWVE.setStatus('current')
if mibBuilder.loadTexts: tsveSWVE.setDescription('IBM TSVE software version')
tsveFRUP = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 6), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveFRUP.setStatus('current')
if mibBuilder.loadTexts: tsveFRUP.setDescription('IBM TSVE FRU part number')
tsveCLUS = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 7), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveCLUS.setStatus('current')
if mibBuilder.loadTexts: tsveCLUS.setDescription('IBM TSVE cluster name')
tsveNODE = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 8), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveNODE.setStatus('current')
if mibBuilder.loadTexts: tsveNODE.setDescription('IBM TSVE node identifier')
tsveERRS = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 9), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveERRS.setStatus('current')
if mibBuilder.loadTexts: tsveERRS.setDescription('IBM TSVE error sequence number')
tsveTIME = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 10), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveTIME.setStatus('current')
if mibBuilder.loadTexts: tsveTIME.setDescription('IBM TSVE last error time stamp')
tsveOBJT = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 11), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveOBJT.setStatus('current')
if mibBuilder.loadTexts: tsveOBJT.setDescription('IBM TSVE object type')
tsveOBJI = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 12), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveOBJI.setStatus('current')
if mibBuilder.loadTexts: tsveOBJI.setDescription('IBM TSVE object ID')
tsveADD1 = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 13), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveADD1.setStatus('current')
if mibBuilder.loadTexts: tsveADD1.setDescription('IBM TSVE Additional data')
tsveADD2 = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 14), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveADD2.setStatus('current')
if mibBuilder.loadTexts: tsveADD2.setDescription('IBM TSVE Additional data')
tsveCOPY = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 15), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveCOPY.setStatus('current')
if mibBuilder.loadTexts: tsveCOPY.setDescription('IBM TSVE Copy ID')
tsveMPNO = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 16), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveMPNO.setStatus('current')
if mibBuilder.loadTexts: tsveMPNO.setDescription('IBM TSVE Machine Part Number')
tsveOBJN = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 17), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveOBJN.setStatus('current')
if mibBuilder.loadTexts: tsveOBJN.setDescription('IBM (orginally TSVE) object name')
tsveIDAL = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 18), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tsveIDAL.setStatus('current')
if mibBuilder.loadTexts: tsveIDAL.setDescription('IBM (orginally TSVE) cluster alias')
tsveCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 1))
tsveGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 2))
tsveCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 1, 1)).setObjects(("IBM-SVC-MIB", "tsveRequiredObjectsGroup"), ("IBM-SVC-MIB", "tsveNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tsveCompliance = tsveCompliance.setStatus('current')
if mibBuilder.loadTexts: tsveCompliance.setDescription('The compliance statement for the TSVE-MIB.')
tsveRequiredObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 2, 1)).setObjects(("IBM-SVC-MIB", "tsveMACH"), ("IBM-SVC-MIB", "tsveSERI"), ("IBM-SVC-MIB", "tsveERRI"), ("IBM-SVC-MIB", "tsveERRC"), ("IBM-SVC-MIB", "tsveSWVE"), ("IBM-SVC-MIB", "tsveFRUP"), ("IBM-SVC-MIB", "tsveCLUS"), ("IBM-SVC-MIB", "tsveNODE"), ("IBM-SVC-MIB", "tsveERRS"), ("IBM-SVC-MIB", "tsveTIME"), ("IBM-SVC-MIB", "tsveOBJT"), ("IBM-SVC-MIB", "tsveOBJI"), ("IBM-SVC-MIB", "tsveADD1"), ("IBM-SVC-MIB", "tsveADD2"), ("IBM-SVC-MIB", "tsveCOPY"), ("IBM-SVC-MIB", "tsveMPNO"), ("IBM-SVC-MIB", "tsveOBJN"), ("IBM-SVC-MIB", "tsveIDAL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tsveRequiredObjectsGroup = tsveRequiredObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: tsveRequiredObjectsGroup.setDescription('The objects defined in this MIB module that MUST be implemented by a compliant implementation.')
tsveNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 2, 2)).setObjects(("IBM-SVC-MIB", "tsveETrap"), ("IBM-SVC-MIB", "tsveWTrap"), ("IBM-SVC-MIB", "tsveITrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tsveNotifGroup = tsveNotifGroup.setStatus('current')
if mibBuilder.loadTexts: tsveNotifGroup.setDescription('All notifications defined in this MIB module MUST be implemented by a compliant implementation.')
mibBuilder.exportSymbols("IBM-SVC-MIB", tsveCLUS=tsveCLUS, ibm2145TSVEConformance=ibm2145TSVEConformance, tsveNODE=tsveNODE, tsveCOPY=tsveCOPY, tsveOBJI=tsveOBJI, ibm=ibm, tsveNotifGroup=tsveNotifGroup, PYSNMP_MODULE_ID=ibm2145TSVE, ibm2145TSVEObjects=ibm2145TSVEObjects, tsveERRS=tsveERRS, tsveFRUP=tsveFRUP, tsveIDAL=tsveIDAL, tsveITrap=tsveITrap, tsveTIME=tsveTIME, tsveETrap=tsveETrap, tsveMPNO=tsveMPNO, tsveSWVE=tsveSWVE, tsveCompliances=tsveCompliances, tsveRequiredObjectsGroup=tsveRequiredObjectsGroup, tsveERRC=tsveERRC, tsveOBJN=tsveOBJN, tsveERRI=tsveERRI, tsveCompliance=tsveCompliance, tsveSERI=tsveSERI, tsveMACH=tsveMACH, ibmProd=ibmProd, tsveADD1=tsveADD1, tsveGroups=tsveGroups, tsveOBJT=tsveOBJT, tsveWTrap=tsveWTrap, ibm2145TSVE=ibm2145TSVE, tsveADD2=tsveADD2)
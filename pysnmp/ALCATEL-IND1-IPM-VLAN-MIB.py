#
# PySNMP MIB module ALCATEL-IND1-IPM-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-IPM-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:02:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1IPMVlanMgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1IPMVlanMgt")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddressPrefixLength, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressPrefixLength", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Integer32, IpAddress, TimeTicks, NotificationType, Bits, Counter32, Unsigned32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "NotificationType", "Bits", "Counter32", "Unsigned32", "iso", "MibIdentifier")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1IPMVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIB.setLastUpdated('200707020000Z')
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIB.setOrganization('ALCATEL - Architects Of An Internet World')
alcatelIND1IPMVlanMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBObjects.setStatus('current')
alcatelIND1IPMVlanMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBConformance.setStatus('current')
alcatelIND1IPMVlanMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBGroups.setStatus('current')
alcatelIND1IPMVlanMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBCompliances.setStatus('current')
alaipmvVlanPort = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1))
alaipmvVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaipmvVlanPortTable.setStatus('current')
alaipmvVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortIPMVlanNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortType"))
if mibBuilder.loadTexts: alaipmvVlanPortEntry.setStatus('current')
alaipmvVlanPortIPMVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanPortIPMVlanNumber.setStatus('current')
alaipmvVlanPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanPortNumber.setStatus('current')
alaipmvVlanPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receiverPort", 1), ("senderPort", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanPortType.setStatus('current')
alaipmvVlanPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaipmvVlanPortRowStatus.setStatus('current')
alaipmvVlanIpAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2))
alaipmvVlanIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1), )
if mibBuilder.loadTexts: alaipmvVlanIpAddrTable.setStatus('current')
alaipmvVlanIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrVlanNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrType"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddress"))
if mibBuilder.loadTexts: alaipmvVlanIpAddrEntry.setStatus('current')
alaipmvVlanIpAddrVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanIpAddrVlanNumber.setStatus('current')
alaipmvVlanIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 2), InetAddressType().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanIpAddrType.setStatus('current')
alaipmvVlanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanIpAddress.setStatus('current')
alaipmvVlanIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaipmvVlanIpAddrRowStatus.setStatus('current')
alaipmvVlanCtagT = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3))
alaipmvVlanCtagTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1), )
if mibBuilder.loadTexts: alaipmvVlanCtagTable.setStatus('current')
alaipmvVlanCtagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanCtag"))
if mibBuilder.loadTexts: alaipmvVlanCtagEntry.setStatus('current')
alaipmvVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanNumber.setStatus('current')
alaipmvVlanCtag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanCtag.setStatus('current')
alaipmvVlanCtagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaipmvVlanCtagRowStatus.setStatus('current')
alaipmvVlanIpAddrMask = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 4))
alaipmvVlanIpAddrMaskTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2), )
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskTable.setStatus('current')
alaipmvVlanIpAddrMaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskVlanNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskType"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskAddress"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskPrefixLen"))
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskEntry.setStatus('current')
alaipmvVlanIpAddrMaskVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094)))
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskVlanNumber.setStatus('current')
alaipmvVlanIpAddrMaskType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 2), InetAddressType().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskType.setStatus('current')
alaipmvVlanIpAddrMaskAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskAddress.setStatus('current')
alaipmvVlanIpAddrMaskPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 4), InetAddressPrefixLength())
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskPrefixLen.setStatus('current')
alaipmvVlanIpAddrMaskRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskRowStatus.setStatus('current')
alcatelIND1IPMVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvlanPortGroup"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvlanIPAddressGroup"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvlanIPAddrMaskGroup"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvlanCtagGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1IPMVlanMIBCompliance = alcatelIND1IPMVlanMIBCompliance.setStatus('current')
alaipmvlanPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortIPMVlanNumber"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortNumber"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortType"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaipmvlanPortGroup = alaipmvlanPortGroup.setStatus('current')
alaipmvlanIPAddressGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrVlanNumber"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrType"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddress"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaipmvlanIPAddressGroup = alaipmvlanIPAddressGroup.setStatus('current')
alaipmvlanCtagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanNumber"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanCtag"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanCtagRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaipmvlanCtagGroup = alaipmvlanCtagGroup.setStatus('current')
alaipmvlanIPAddrMaskGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaipmvlanIPAddrMaskGroup = alaipmvlanIPAddrMaskGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-IPM-VLAN-MIB", alaipmvVlanCtagTable=alaipmvVlanCtagTable, alaipmvVlanIpAddrMaskTable=alaipmvVlanIpAddrMaskTable, alcatelIND1IPMVlanMIBObjects=alcatelIND1IPMVlanMIBObjects, alaipmvVlanPort=alaipmvVlanPort, alaipmvVlanIpAddrType=alaipmvVlanIpAddrType, alaipmvVlanCtagEntry=alaipmvVlanCtagEntry, alaipmvVlanIpAddrMaskType=alaipmvVlanIpAddrMaskType, alaipmvVlanIpAddrMaskPrefixLen=alaipmvVlanIpAddrMaskPrefixLen, alaipmvVlanIpAddrMaskRowStatus=alaipmvVlanIpAddrMaskRowStatus, alcatelIND1IPMVlanMIBCompliances=alcatelIND1IPMVlanMIBCompliances, alaipmvlanIPAddrMaskGroup=alaipmvlanIPAddrMaskGroup, alaipmvVlanIpAddr=alaipmvVlanIpAddr, alaipmvlanIPAddressGroup=alaipmvlanIPAddressGroup, PYSNMP_MODULE_ID=alcatelIND1IPMVlanMIB, alaipmvVlanIpAddrMaskVlanNumber=alaipmvVlanIpAddrMaskVlanNumber, alaipmvlanCtagGroup=alaipmvlanCtagGroup, alaipmvVlanPortType=alaipmvVlanPortType, alaipmvVlanIpAddrTable=alaipmvVlanIpAddrTable, alaipmvVlanCtag=alaipmvVlanCtag, alaipmvVlanIpAddress=alaipmvVlanIpAddress, alaipmvVlanPortRowStatus=alaipmvVlanPortRowStatus, alaipmvVlanIpAddrRowStatus=alaipmvVlanIpAddrRowStatus, alcatelIND1IPMVlanMIB=alcatelIND1IPMVlanMIB, alaipmvVlanIpAddrMaskAddress=alaipmvVlanIpAddrMaskAddress, alaipmvVlanPortNumber=alaipmvVlanPortNumber, alaipmvVlanPortEntry=alaipmvVlanPortEntry, alcatelIND1IPMVlanMIBCompliance=alcatelIND1IPMVlanMIBCompliance, alcatelIND1IPMVlanMIBGroups=alcatelIND1IPMVlanMIBGroups, alaipmvVlanCtagT=alaipmvVlanCtagT, alaipmvVlanIpAddrVlanNumber=alaipmvVlanIpAddrVlanNumber, alaipmvVlanPortTable=alaipmvVlanPortTable, alaipmvVlanNumber=alaipmvVlanNumber, alcatelIND1IPMVlanMIBConformance=alcatelIND1IPMVlanMIBConformance, alaipmvVlanIpAddrEntry=alaipmvVlanIpAddrEntry, alaipmvVlanCtagRowStatus=alaipmvVlanCtagRowStatus, alaipmvVlanIpAddrMaskEntry=alaipmvVlanIpAddrMaskEntry, alaipmvVlanIpAddrMask=alaipmvVlanIpAddrMask, alaipmvlanPortGroup=alaipmvlanPortGroup, alaipmvVlanPortIPMVlanNumber=alaipmvVlanPortIPMVlanNumber)

#
# PySNMP MIB module ALCATEL-IND1-IPM-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-IPM-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:17:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1IPMVlanMgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1IPMVlanMgt")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetAddressPrefixLength")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Counter32, ModuleIdentity, Bits, Counter64, NotificationType, IpAddress, ObjectIdentity, Unsigned32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Counter32", "ModuleIdentity", "Bits", "Counter64", "NotificationType", "IpAddress", "ObjectIdentity", "Unsigned32", "Integer32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
alcatelIND1IPMVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIB.setLastUpdated('200707020000Z')
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIB.setOrganization('ALCATEL - Architects Of An Internet World')
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIB.setContactInfo('Please consult with Customer Service to insure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIB.setDescription('The parameters for configuration of the IPM Vlan feature, including the association between ports and ipaddresses with vlans. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1IPMVlanMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBObjects.setDescription('Branch For IPM Vlan Managed Objects.')
alcatelIND1IPMVlanMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBConformance.setDescription('Branch For IPM Vlan Conformance Information.')
alcatelIND1IPMVlanMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBGroups.setDescription('Branch For IPM Vlan Units Of Conformance.')
alcatelIND1IPMVlanMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBCompliances.setDescription('Branch For IPM Vlan Compliance Statements.')
alaipmvVlanPort = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1))
alaipmvVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaipmvVlanPortTable.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanPortTable.setDescription('A table that contains port specific information for the IP Multicast VLAN. An entry is this table is created when a port is configured as a receiver / sender port for a IPMVLAN.')
alaipmvVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortIPMVlanNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortType"))
if mibBuilder.loadTexts: alaipmvVlanPortEntry.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanPortEntry.setDescription('A IPMV Port entry.')
alaipmvVlanPortIPMVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanPortIPMVlanNumber.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanPortIPMVlanNumber.setDescription('The VLAN number component of this IPMVLAN instance. Valid range from 2 to 4094.')
alaipmvVlanPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanPortNumber.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanPortNumber.setDescription('The port ifindex of the port which is associated to the IPMVLAN.')
alaipmvVlanPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receiverPort", 1), ("senderPort", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanPortType.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanPortType.setDescription('The type of this port associated to the IPMVLAN. receiverPort(1) is the receiver port associated to the IPMVLAN, senderPort(2) is the sender port associated to the IPMVLAN. In the VLAN Stacking environment, these ports are the VLAN Stacking ports. Configuration of IPMVLAN logical/physical receiver port on multiple IPMVlans, that are associated with same IPv4/IPv6 multicast group addresses are not allowed.')
alaipmvVlanPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaipmvVlanPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanPortRowStatus.setDescription('The status of this table entry. The values supported are CreateAndGo(4) and destroy(6), to create or delete the port as a receiver / sender port in an IPMVLAN. Of course the corresponding vlan and port must exist.')
alaipmvVlanIpAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2))
alaipmvVlanIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1), )
if mibBuilder.loadTexts: alaipmvVlanIpAddrTable.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrTable.setDescription('A list of IP addresses assigned to an IPMVLAN.')
alaipmvVlanIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrVlanNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrType"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddress"))
if mibBuilder.loadTexts: alaipmvVlanIpAddrEntry.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrEntry.setDescription('A IPMVLAN IP address entry.')
alaipmvVlanIpAddrVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanIpAddrVlanNumber.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrVlanNumber.setDescription('The VLAN number component of this IPMVLAN instance. Valid range from 2 to 4094.')
alaipmvVlanIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 2), InetAddressType().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanIpAddrType.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrType.setDescription('The IP address type.')
alaipmvVlanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanIpAddress.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddress.setDescription('The Multicast IP address based on the address type. This IP multicast group address can be associated to multiple IPMVLANs. Configuration of IPv4/IPv6 Multicast Group address on multiple IPMVlans, that are associated with same physical/logical receiver ports are not allowed.')
alaipmvVlanIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaipmvVlanIpAddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrRowStatus.setDescription('This is used to create or delete the Multicast IP address in an IPMVLAN. Of course the corresponding vlan must exist.')
alaipmvVlanCtagT = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3))
alaipmvVlanCtagTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1), )
if mibBuilder.loadTexts: alaipmvVlanCtagTable.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanCtagTable.setDescription(' A table that contains ipmvlan-ctag association for the IPMV feature.')
alaipmvVlanCtagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanCtag"))
if mibBuilder.loadTexts: alaipmvVlanCtagEntry.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanCtagEntry.setDescription('A IPMVLAN-Ctag entry.')
alaipmvVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanNumber.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanNumber.setDescription('The VLAN number component of this IPMVLAN instance. Valid range from 2 to 4094.')
alaipmvVlanCtag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaipmvVlanCtag.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanCtag.setDescription(" The customer vlan id associated to the IPMVLAN. This customer vlan id is unique and can't be associated to more than one IPM Vlan")
alaipmvVlanCtagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaipmvVlanCtagRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanCtagRowStatus.setDescription('The status of this table entry. The supported value for set are createAndGo (4) and destroy(6), to add or remove an IPMVLAN-ctag association.')
alaipmvVlanIpAddrMask = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 4))
alaipmvVlanIpAddrMaskTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2), )
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskTable.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskTable.setDescription('A list of IP addresses assigned to an IPMVLAN.')
alaipmvVlanIpAddrMaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskVlanNumber"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskType"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskAddress"), (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskPrefixLen"))
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskEntry.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskEntry.setDescription('A IPMVLAN IP address entry.')
alaipmvVlanIpAddrMaskVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094)))
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskVlanNumber.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskVlanNumber.setDescription('The VLAN number component of this IPMVLAN instance. Valid range from 2 to 4094.')
alaipmvVlanIpAddrMaskType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 2), InetAddressType().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskType.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskType.setDescription('The IP address type.The allowed values are ipv4(1) and ipv6(2).')
alaipmvVlanIpAddrMaskAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskAddress.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskAddress.setDescription('The Multicast IP address based on the address type indicated by alaipmvVlanIpAddrMaskType. This IP multicast group address can be associated to multiple IPMVLANs. alaipmvVlanIpAddrMaskPrefixLen is used to specify a mask. The host bits of the address should be zero.')
alaipmvVlanIpAddrMaskPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 4), InetAddressPrefixLength())
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskPrefixLen.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskPrefixLen.setDescription('The Multicast IP address-mask length based on the address type. It must be 0-32 for alaipmvVlanIpAddrMaskType ipv4 and 128 for alaipmvVlanIpAddrMaskType ipv6. The host bits of the address alaipmvVlanIpAddrMaskAddress should be zero.')
alaipmvVlanIpAddrMaskRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaipmvVlanIpAddrMaskRowStatus.setDescription('This is used to create or delete the Multicast IP address in an IPMVLAN. Of course the corresponding vlan must exist.')
alcatelIND1IPMVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvlanPortGroup"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvlanIPAddressGroup"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvlanIPAddrMaskGroup"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvlanCtagGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1IPMVlanMIBCompliance = alcatelIND1IPMVlanMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1IPMVlanMIBCompliance.setDescription('Compliance statement for IPM Vlan.')
alaipmvlanPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortIPMVlanNumber"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortNumber"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortType"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaipmvlanPortGroup = alaipmvlanPortGroup.setStatus('current')
if mibBuilder.loadTexts: alaipmvlanPortGroup.setDescription('Collection of objects for management of IPM Vlan Ports.')
alaipmvlanIPAddressGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrVlanNumber"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrType"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddress"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaipmvlanIPAddressGroup = alaipmvlanIPAddressGroup.setStatus('current')
if mibBuilder.loadTexts: alaipmvlanIPAddressGroup.setDescription('Collection of objects for management of IPM Vlan Address.')
alaipmvlanCtagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanNumber"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanCtag"), ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanCtagRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaipmvlanCtagGroup = alaipmvlanCtagGroup.setStatus('current')
if mibBuilder.loadTexts: alaipmvlanCtagGroup.setDescription('Collection of objects for management of IPM Vlan Address.')
alaipmvlanIPAddrMaskGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaipmvlanIPAddrMaskGroup = alaipmvlanIPAddrMaskGroup.setStatus('current')
if mibBuilder.loadTexts: alaipmvlanIPAddrMaskGroup.setDescription('Collection of objects for management of IPM Vlan Address.')
mibBuilder.exportSymbols("ALCATEL-IND1-IPM-VLAN-MIB", alaipmvVlanIpAddrMaskRowStatus=alaipmvVlanIpAddrMaskRowStatus, alaipmvVlanPortRowStatus=alaipmvVlanPortRowStatus, alaipmvVlanCtag=alaipmvVlanCtag, alaipmvVlanPort=alaipmvVlanPort, alaipmvVlanIpAddrType=alaipmvVlanIpAddrType, alaipmvlanIPAddressGroup=alaipmvlanIPAddressGroup, alaipmvVlanIpAddrMaskTable=alaipmvVlanIpAddrMaskTable, alaipmvlanCtagGroup=alaipmvlanCtagGroup, alcatelIND1IPMVlanMIB=alcatelIND1IPMVlanMIB, alaipmvVlanIpAddrTable=alaipmvVlanIpAddrTable, alaipmvlanPortGroup=alaipmvlanPortGroup, alcatelIND1IPMVlanMIBGroups=alcatelIND1IPMVlanMIBGroups, alaipmvVlanPortIPMVlanNumber=alaipmvVlanPortIPMVlanNumber, PYSNMP_MODULE_ID=alcatelIND1IPMVlanMIB, alaipmvVlanCtagRowStatus=alaipmvVlanCtagRowStatus, alaipmvVlanIpAddress=alaipmvVlanIpAddress, alaipmvVlanCtagEntry=alaipmvVlanCtagEntry, alaipmvVlanIpAddrMaskAddress=alaipmvVlanIpAddrMaskAddress, alcatelIND1IPMVlanMIBCompliances=alcatelIND1IPMVlanMIBCompliances, alaipmvVlanPortType=alaipmvVlanPortType, alaipmvVlanIpAddrMaskEntry=alaipmvVlanIpAddrMaskEntry, alaipmvVlanIpAddrMask=alaipmvVlanIpAddrMask, alaipmvVlanIpAddrEntry=alaipmvVlanIpAddrEntry, alaipmvVlanPortTable=alaipmvVlanPortTable, alaipmvVlanPortEntry=alaipmvVlanPortEntry, alaipmvVlanPortNumber=alaipmvVlanPortNumber, alaipmvlanIPAddrMaskGroup=alaipmvlanIPAddrMaskGroup, alaipmvVlanIpAddrMaskType=alaipmvVlanIpAddrMaskType, alaipmvVlanIpAddr=alaipmvVlanIpAddr, alaipmvVlanIpAddrMaskPrefixLen=alaipmvVlanIpAddrMaskPrefixLen, alaipmvVlanNumber=alaipmvVlanNumber, alaipmvVlanCtagTable=alaipmvVlanCtagTable, alaipmvVlanIpAddrRowStatus=alaipmvVlanIpAddrRowStatus, alaipmvVlanCtagT=alaipmvVlanCtagT, alaipmvVlanIpAddrMaskVlanNumber=alaipmvVlanIpAddrMaskVlanNumber, alaipmvVlanIpAddrVlanNumber=alaipmvVlanIpAddrVlanNumber, alcatelIND1IPMVlanMIBObjects=alcatelIND1IPMVlanMIBObjects, alcatelIND1IPMVlanMIBCompliance=alcatelIND1IPMVlanMIBCompliance, alcatelIND1IPMVlanMIBConformance=alcatelIND1IPMVlanMIBConformance)

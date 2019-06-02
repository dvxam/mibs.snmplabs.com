#
# PySNMP MIB module ALCATEL-IND1-DHCP-SRV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-DHCP-SRV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:17:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1DhcpSrv, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1DhcpSrv")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, ObjectIdentity, ModuleIdentity, Bits, MibIdentifier, NotificationType, Integer32, Counter32, Unsigned32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "ObjectIdentity", "ModuleIdentity", "Bits", "MibIdentifier", "NotificationType", "Integer32", "Counter32", "Unsigned32", "Gauge32", "Counter64")
DateAndTime, TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString", "MacAddress")
alcatelIND1DhcpSrvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1))
alcatelIND1DhcpSrvMIB.setRevisions(('2009-10-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIB.setRevisionsDescriptions(('The Dynamic Host Configuration Protocol (DHCP) provides a framework for passing configuration information to hosts on a TCPIP network. DHCP is based on the Bootstrap Protocol (BOOTP), adding the capability of automatic allocation of reusable network addresses and additional configuration options. This MIB provides the configuration information for DHCP Server.',))
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIB.setLastUpdated('200812100000Z')
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIB.setOrganization('Alcatel - Architects Of An Internet World')
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIB.setContactInfo('Please consult with Customer Service to insure the most appropriate version of this document is used with the products in question: Alcatel Internetworking, Incorporated (Division 1, Formerly XYLAN Corporation) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://www.ind.alcatel.com File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): For the Birds Of Prey Product Line DhcpSrv for dynamically assigning IP to clients. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2002 Alcatel Internetworking, Incorporated ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1DhcpSrvMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 0))
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBNotifications.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBNotifications.setDescription('Branch For DHCP Server Subsystem Notifications.')
alcatelIND1DhcpSrvMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1))
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBObjects.setDescription('Branch For DHCP Server Subsystem Managed Objects.')
alcatelIND1DhcpSrvMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 2))
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBConformance.setDescription('Branch for DhcpSrv Module MIB Subsystem Conformance Information.')
alcatelIND1DhcpSrvMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBGroups.setDescription('Branch for DhcpSrv Module MIB Subsystem Units of Conformance.')
alcatelIND1DhcpSrvMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBCompliances.setDescription('Branch for DhcpSrv Module MIB Subsystem Compliance Statements.')
alaDhcpSrvGlobalConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDhcpSrvGlobalConfigStatus.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvGlobalConfigStatus.setDescription('This object is used to enable(1) or disable(2) DHCP Server on the switch.')
alaDhcpSrvGlobalRestart = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("restart", 2))).clone('inactive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDhcpSrvGlobalRestart.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvGlobalRestart.setDescription('This object is used to restart(2) the DHCP Server on the switch. Default value is inactive(1) which user can not set.')
alaDhcpSrvGlobalClearStat = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("reset", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDhcpSrvGlobalClearStat.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvGlobalClearStat.setDescription('Defines the global clear statistics control for DHCP Server. default(1) - default value for this object, reset(2) - indicates that all statistic related to DHCP server in the system should get cleared.')
alaDhcpSrvLease = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 4))
alaDhcpSrvLeaseTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 4, 1), )
if mibBuilder.loadTexts: alaDhcpSrvLeaseTable.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseTable.setDescription('DHCP server lease table.')
alaDhcpSrvLeaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 4, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseInetAddressType"), (0, "ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseInetAddress"))
if mibBuilder.loadTexts: alaDhcpSrvLeaseEntry.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseEntry.setDescription('DHCP server lease entry.')
alaDhcpSrvLeaseInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 4, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: alaDhcpSrvLeaseInetAddressType.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseInetAddressType.setDescription('Thie object specifies the type of DHCP Server lease address. Currently only InetAddressIPv4(1) is supported.')
alaDhcpSrvLeaseInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 4, 1, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: alaDhcpSrvLeaseInetAddress.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseInetAddress.setDescription('This object specifies IP address assigned to the client.')
alaDhcpSrvLeaseMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 4, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDhcpSrvLeaseMACAddress.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseMACAddress.setDescription('MAC address assigned to the client.')
alaDhcpSrvLeaseLeaseGrant = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 4, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDhcpSrvLeaseLeaseGrant.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseLeaseGrant.setDescription('Lease granted time for the client.')
alaDhcpSrvLeaseLeaseExpiry = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 4, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDhcpSrvLeaseLeaseExpiry.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseLeaseExpiry.setDescription('Lease expiry of the client.')
alaDhcpSrvLeaseType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unavailable", 1), ("dynamic", 2), ("manual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDhcpSrvLeaseType.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseType.setDescription('Type of the lease.')
alaDhcpSrvTrapsObj = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 5))
alaDhcpSrvLeaseUtilizationThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 0, 1)).setObjects(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseThresholdStatus"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvSubnetDescriptor"))
if mibBuilder.loadTexts: alaDhcpSrvLeaseUtilizationThresholdTrap.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseUtilizationThresholdTrap.setDescription('When the lease utilization in a subnet exceeds or deceeds threshold value set by the application, a notification is sent to the Management Entity, with the DHCP Server lease utilization information.')
alaDhcpSrvLeaseThresholdStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("crossedBelow80Threshold", 1), ("crossedAbove80Threshold", 2), ("reached100Threshold", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaDhcpSrvLeaseThresholdStatus.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseThresholdStatus.setDescription('This object specifies the threshold status of subnet utilization.')
alaDhcpSrvSubnetDescriptor = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 1, 5, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaDhcpSrvSubnetDescriptor.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvSubnetDescriptor.setDescription('This object specifies the subnet Descriptor. If the subnet belongs to shared network, this object specifies the shared network name, else specifies the Subnet IP.')
alcatelIND1DhcpSrvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvGlobalConfigGroup"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseGroup"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvNotificationGroup"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseUtilizationThresholdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1DhcpSrvMIBCompliance = alcatelIND1DhcpSrvMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1DhcpSrvMIBCompliance.setDescription('Compliance statement for DHCP Server.')
alaDhcpSrvGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvGlobalConfigStatus"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvGlobalRestart"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvGlobalClearStat"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDhcpSrvGlobalConfigGroup = alaDhcpSrvGlobalConfigGroup.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvGlobalConfigGroup.setDescription('Collection of objects for management of DHCP Server Global Configuration.')
alaDhcpSrvLeaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseMACAddress"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseLeaseGrant"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseLeaseExpiry"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDhcpSrvLeaseGroup = alaDhcpSrvLeaseGroup.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseGroup.setDescription('Collection of objects for DHCP Server Lease Configuration.')
alaDhcpSrvNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseUtilizationThresholdTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDhcpSrvNotificationGroup = alaDhcpSrvNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvNotificationGroup.setDescription('Collection of objects for DHCP Server Trap information.')
alaDhcpSrvLeaseUtilizationThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseThresholdStatus"), ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvSubnetDescriptor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDhcpSrvLeaseUtilizationThresholdGroup = alaDhcpSrvLeaseUtilizationThresholdGroup.setStatus('current')
if mibBuilder.loadTexts: alaDhcpSrvLeaseUtilizationThresholdGroup.setDescription('When the lease utilization in a subnet exceeds or deceeds threshold value set by the application, a notification is sent to the Management Entity, with the DHCP Server lease utilization information.')
mibBuilder.exportSymbols("ALCATEL-IND1-DHCP-SRV-MIB", alcatelIND1DhcpSrvMIB=alcatelIND1DhcpSrvMIB, alcatelIND1DhcpSrvMIBConformance=alcatelIND1DhcpSrvMIBConformance, alaDhcpSrvGlobalConfigStatus=alaDhcpSrvGlobalConfigStatus, alaDhcpSrvLeaseTable=alaDhcpSrvLeaseTable, alaDhcpSrvGlobalConfigGroup=alaDhcpSrvGlobalConfigGroup, alaDhcpSrvLeaseEntry=alaDhcpSrvLeaseEntry, alaDhcpSrvLeaseThresholdStatus=alaDhcpSrvLeaseThresholdStatus, alaDhcpSrvLeaseLeaseGrant=alaDhcpSrvLeaseLeaseGrant, alaDhcpSrvLeaseGroup=alaDhcpSrvLeaseGroup, alaDhcpSrvTrapsObj=alaDhcpSrvTrapsObj, PYSNMP_MODULE_ID=alcatelIND1DhcpSrvMIB, alaDhcpSrvNotificationGroup=alaDhcpSrvNotificationGroup, alaDhcpSrvLeaseUtilizationThresholdGroup=alaDhcpSrvLeaseUtilizationThresholdGroup, alcatelIND1DhcpSrvMIBObjects=alcatelIND1DhcpSrvMIBObjects, alcatelIND1DhcpSrvMIBCompliance=alcatelIND1DhcpSrvMIBCompliance, alaDhcpSrvLeaseMACAddress=alaDhcpSrvLeaseMACAddress, alcatelIND1DhcpSrvMIBGroups=alcatelIND1DhcpSrvMIBGroups, alaDhcpSrvGlobalClearStat=alaDhcpSrvGlobalClearStat, alaDhcpSrvLeaseInetAddress=alaDhcpSrvLeaseInetAddress, alaDhcpSrvSubnetDescriptor=alaDhcpSrvSubnetDescriptor, alaDhcpSrvGlobalRestart=alaDhcpSrvGlobalRestart, alcatelIND1DhcpSrvMIBCompliances=alcatelIND1DhcpSrvMIBCompliances, alaDhcpSrvLeaseUtilizationThresholdTrap=alaDhcpSrvLeaseUtilizationThresholdTrap, alcatelIND1DhcpSrvMIBNotifications=alcatelIND1DhcpSrvMIBNotifications, alaDhcpSrvLeaseLeaseExpiry=alaDhcpSrvLeaseLeaseExpiry, alaDhcpSrvLeaseInetAddressType=alaDhcpSrvLeaseInetAddressType, alaDhcpSrvLease=alaDhcpSrvLease, alaDhcpSrvLeaseType=alaDhcpSrvLeaseType)
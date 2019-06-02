#
# PySNMP MIB module NOKIA-ALCHEMYOS-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-ALCHEMYOS-CLUSTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
alchemyOSTraps, cryptoCluster, alchemyOSModules = mibBuilder.importSymbols("NOKIA-ALCHEMYOS-MIB", "alchemyOSTraps", "cryptoCluster", "alchemyOSModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, MibIdentifier, ObjectIdentity, Gauge32, Integer32, Unsigned32, Counter64, iso, NotificationType, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "MibIdentifier", "ObjectIdentity", "Gauge32", "Integer32", "Unsigned32", "Counter64", "iso", "NotificationType", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nokiaAlchemyOSClusterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 45, 5, 2))
nokiaAlchemyOSClusterMIB.setRevisions(('2001-01-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nokiaAlchemyOSClusterMIB.setRevisionsDescriptions(('Cleanup.',))
if mibBuilder.loadTexts: nokiaAlchemyOSClusterMIB.setLastUpdated('200101180000Z')
if mibBuilder.loadTexts: nokiaAlchemyOSClusterMIB.setOrganization('Nokia Internet Communications.')
if mibBuilder.loadTexts: nokiaAlchemyOSClusterMIB.setContactInfo(' Nokia, Inc. Customer Support Postal: 100 Enterprise Way, Module B Scotts Valley, CA 95066 USA E-Mail: snmp-contact@cips.nokia.com')
if mibBuilder.loadTexts: nokiaAlchemyOSClusterMIB.setDescription('Cluster MIB module.')
clusterInfoName = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterInfoName.setStatus('current')
if mibBuilder.loadTexts: clusterInfoName.setDescription('The name of this cluster.')
clusterMemberInfoNumMembers = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterMemberInfoNumMembers.setStatus('current')
if mibBuilder.loadTexts: clusterMemberInfoNumMembers.setDescription('The number of members in this cluster.')
clusterAddrTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 3), )
if mibBuilder.loadTexts: clusterAddrTable.setStatus('current')
if mibBuilder.loadTexts: clusterAddrTable.setDescription('The list of IP addresses for this cluster.')
clusterAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 3, 1), ).setIndexNames((0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "clusterAddrIndex"))
if mibBuilder.loadTexts: clusterAddrEntry.setStatus('current')
if mibBuilder.loadTexts: clusterAddrEntry.setDescription('Cluster IP addresses.')
clusterAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterAddrIndex.setStatus('current')
if mibBuilder.loadTexts: clusterAddrIndex.setDescription('The index of the member list for this cluster.')
clusterInfoAddrs = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterInfoAddrs.setStatus('current')
if mibBuilder.loadTexts: clusterInfoAddrs.setDescription("The list of the cluster's IP addresses.")
clusterMemberTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4), )
if mibBuilder.loadTexts: clusterMemberTable.setStatus('current')
if mibBuilder.loadTexts: clusterMemberTable.setDescription('A list of information, one entry for each member of the cluster.')
clusterMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1), ).setIndexNames((0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "clusterMemberIndex"))
if mibBuilder.loadTexts: clusterMemberEntry.setStatus('current')
if mibBuilder.loadTexts: clusterMemberEntry.setDescription('A table entry containing information about a member of the cluster.')
clusterMemberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterMemberIndex.setStatus('current')
if mibBuilder.loadTexts: clusterMemberIndex.setDescription('A unique value for each member in the cluster. The value ranges between 1 and the value of clusterMemberInfoNumMembers.')
clusterMemberPrimaryIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterMemberPrimaryIPAddr.setStatus('current')
if mibBuilder.loadTexts: clusterMemberPrimaryIPAddr.setDescription("The member's primary IP address.")
clusterMemberWorkload = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterMemberWorkload.setStatus('current')
if mibBuilder.loadTexts: clusterMemberWorkload.setDescription("The member's workload.")
clusterMemberMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterMemberMaster.setStatus('current')
if mibBuilder.loadTexts: clusterMemberMaster.setDescription('Is this member the master.')
clusterMemberSecondaryIPAddrTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 5), )
if mibBuilder.loadTexts: clusterMemberSecondaryIPAddrTable.setStatus('current')
if mibBuilder.loadTexts: clusterMemberSecondaryIPAddrTable.setDescription('A table of secondary IP addresses for this cluster member.')
clusterMemberSecondaryIPAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 5, 1), ).setIndexNames((0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "clusterMemberIndex"), (0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "clusterMemberSecondaryIPAddrIndex"))
if mibBuilder.loadTexts: clusterMemberSecondaryIPAddrEntry.setStatus('current')
if mibBuilder.loadTexts: clusterMemberSecondaryIPAddrEntry.setDescription('List of the secondary (outside) addresses of the cluster members. This is only valid if this member is the master node of the cluster.')
clusterMemberSecondaryIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterMemberSecondaryIPAddr.setStatus('current')
if mibBuilder.loadTexts: clusterMemberSecondaryIPAddr.setDescription("One member of the cluster's secondary IP address.")
clusterMemberSecondaryIPAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: clusterMemberSecondaryIPAddrIndex.setStatus('current')
if mibBuilder.loadTexts: clusterMemberSecondaryIPAddrIndex.setDescription('Second index for clusterMemberSecondaryIPAddrTable. The first entry has index 1, the second 2, etc.')
processTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 6), )
if mibBuilder.loadTexts: processTable.setStatus('current')
if mibBuilder.loadTexts: processTable.setDescription('A table containing information on running processes/threads.')
processEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 6, 1), ).setIndexNames((0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "processIndex"))
if mibBuilder.loadTexts: processEntry.setStatus('current')
if mibBuilder.loadTexts: processEntry.setDescription('An entry containing a process/thread name.')
processIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processIndex.setStatus('current')
if mibBuilder.loadTexts: processIndex.setDescription('Reference Iindex for each process.')
processName = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 6, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processName.setStatus('current')
if mibBuilder.loadTexts: processName.setDescription('The process name.')
externalIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: externalIPAddress.setStatus('current')
if mibBuilder.loadTexts: externalIPAddress.setDescription('The external IP address.')
alchemyOSTrap0 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0))
if mibBuilder.loadTexts: alchemyOSTrap0.setStatus('current')
if mibBuilder.loadTexts: alchemyOSTrap0.setDescription('Trap.')
clusterMemberJoin = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 1))
if mibBuilder.loadTexts: clusterMemberJoin.setStatus('current')
if mibBuilder.loadTexts: clusterMemberJoin.setDescription('Signifies that a member node has joined the cluster.')
clusterMemberLeft = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 2))
if mibBuilder.loadTexts: clusterMemberLeft.setStatus('current')
if mibBuilder.loadTexts: clusterMemberLeft.setDescription('Signifies that a node has left the cluster.')
clusterMemberBecameMaster = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 3))
if mibBuilder.loadTexts: clusterMemberBecameMaster.setStatus('current')
if mibBuilder.loadTexts: clusterMemberBecameMaster.setDescription('Sent when a node has been made the master.')
cpuUtilExceeded = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 4))
if mibBuilder.loadTexts: cpuUtilExceeded.setStatus('current')
if mibBuilder.loadTexts: cpuUtilExceeded.setDescription('Sent when CPU utilisation exceeds defined limit.')
ioLoadExceeded = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 5))
if mibBuilder.loadTexts: ioLoadExceeded.setStatus('current')
if mibBuilder.loadTexts: ioLoadExceeded.setDescription('Sent when IO load exceeds defined limit.')
droppedUdpPacketsExceeded = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 6))
if mibBuilder.loadTexts: droppedUdpPacketsExceeded.setStatus('current')
if mibBuilder.loadTexts: droppedUdpPacketsExceeded.setDescription('Sent when UDP drop rate exceeds defined limit.')
memUsageExceeded = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 7))
if mibBuilder.loadTexts: memUsageExceeded.setStatus('current')
if mibBuilder.loadTexts: memUsageExceeded.setDescription('Sent when memory usage exceeds defined limit.')
droppedIpPacketsExceeded = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 8))
if mibBuilder.loadTexts: droppedIpPacketsExceeded.setStatus('current')
if mibBuilder.loadTexts: droppedIpPacketsExceeded.setDescription('Sent when IP packet drop rate exceeds defined limit.')
gatedConfigError = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 9))
if mibBuilder.loadTexts: gatedConfigError.setStatus('current')
if mibBuilder.loadTexts: gatedConfigError.setDescription('Sent when GATED detects errors in configuration and cannot proceed.')
informAddress = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 10)).setObjects(("NOKIA-ALCHEMYOS-CLUSTER-MIB", "externalIPAddress"))
if mibBuilder.loadTexts: informAddress.setStatus('current')
if mibBuilder.loadTexts: informAddress.setDescription('Sent to inform dynamic external interface address.')
mibBuilder.exportSymbols("NOKIA-ALCHEMYOS-CLUSTER-MIB", nokiaAlchemyOSClusterMIB=nokiaAlchemyOSClusterMIB, PYSNMP_MODULE_ID=nokiaAlchemyOSClusterMIB, clusterMemberEntry=clusterMemberEntry, processEntry=processEntry, informAddress=informAddress, externalIPAddress=externalIPAddress, ioLoadExceeded=ioLoadExceeded, clusterMemberMaster=clusterMemberMaster, clusterInfoAddrs=clusterInfoAddrs, clusterMemberBecameMaster=clusterMemberBecameMaster, clusterMemberSecondaryIPAddrEntry=clusterMemberSecondaryIPAddrEntry, clusterMemberLeft=clusterMemberLeft, memUsageExceeded=memUsageExceeded, droppedIpPacketsExceeded=droppedIpPacketsExceeded, clusterInfoName=clusterInfoName, clusterAddrIndex=clusterAddrIndex, processTable=processTable, clusterMemberPrimaryIPAddr=clusterMemberPrimaryIPAddr, clusterAddrEntry=clusterAddrEntry, clusterMemberJoin=clusterMemberJoin, clusterMemberIndex=clusterMemberIndex, droppedUdpPacketsExceeded=droppedUdpPacketsExceeded, alchemyOSTrap0=alchemyOSTrap0, clusterMemberSecondaryIPAddr=clusterMemberSecondaryIPAddr, clusterMemberInfoNumMembers=clusterMemberInfoNumMembers, processIndex=processIndex, clusterMemberSecondaryIPAddrTable=clusterMemberSecondaryIPAddrTable, clusterAddrTable=clusterAddrTable, clusterMemberWorkload=clusterMemberWorkload, clusterMemberTable=clusterMemberTable, cpuUtilExceeded=cpuUtilExceeded, gatedConfigError=gatedConfigError, processName=processName, clusterMemberSecondaryIPAddrIndex=clusterMemberSecondaryIPAddrIndex)
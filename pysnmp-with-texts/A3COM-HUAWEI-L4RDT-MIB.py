#
# PySNMP MIB module A3COM-HUAWEI-L4RDT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-L4RDT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, iso, ObjectIdentity, ModuleIdentity, NotificationType, Counter32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "iso", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Counter32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TruthValue, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention", "MacAddress")
h3cL4Redirect = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10))
if mibBuilder.loadTexts: h3cL4Redirect.setLastUpdated('200409210000Z')
if mibBuilder.loadTexts: h3cL4Redirect.setOrganization('Huawei 3Com Tech, Inc.')
if mibBuilder.loadTexts: h3cL4Redirect.setContactInfo('Platform Team Beijing Institute Huawei Tech, Inc.')
if mibBuilder.loadTexts: h3cL4Redirect.setDescription('See description above')
h3cL4RedirectCacheTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1), )
if mibBuilder.loadTexts: h3cL4RedirectCacheTable.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectCacheTable.setDescription('This table contains an entry for each Web Cache device that this unit is aware of.')
h3cL4RedirectCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-L4RDT-MIB", "h3cL4RedirectCacheIpAddress"))
if mibBuilder.loadTexts: h3cL4RedirectCacheEntry.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectCacheEntry.setDescription('Each row specifies a known Web Cache device.')
h3cL4RedirectCacheIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: h3cL4RedirectCacheIpAddress.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectCacheIpAddress.setDescription('This object specifies the IP address of the Web Cache device.')
h3cL4RedirectCacheRedirectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabledNotRedirecting", 1), ("enabledNoHealthChecker", 2), ("enabledHealthChecking", 3), ("enabledHealthCheckOKNotRedirecting", 4), ("enabledHealthCheckFailed", 5), ("enabledRedirecting", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectCacheRedirectionStatus.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectCacheRedirectionStatus.setDescription('This object returns the current state of traffic redirection to the cache. If redirection is disabled, this object shall return disabledNotRedirecting(1). If a unit cannot be selected to perform the cache health check, this object shall return enabledNoHealthChecker(2). If the software is determining if the cache is able to do redirection(this will happen when the redirection state transitions from disabled to enabled), this object shall return enabledHealthChecking(3). If the cache health check succeeded but the hardware is unable to support redirection to the cache port, this object shall return enabledHealthCheckOKNotRedirecting(4). If the latest health check of the cache has failed, this object shall return enabledHealthCheckFailed(5). If the cache is in use and traffic is being redirected to it, this object shall return enabledRedirecting(6). The default value is disabledNotRedirecting(1).')
h3cL4RedirectCachePort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCachePort.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectCachePort.setDescription('This object stores the ifIndex that identifies the port or link aggregation which provides the connection that leads to the cache. If only manual cache configuration is supported, this value must be supplied. The method of cache configuration can be ascertained by the presence or absence of the L4 manual cache configuration id within the 3com-352 MIB. The default value is 0.')
h3cL4RedirectCacheRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCacheRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectCacheRowStatus.setDescription('This object is used to create and remove Web Cache entries. The following are the valid values that may be written to RowStatus: Writing createAndGo(4) to the RowStatus of a non-existent row shall create a row with default values and shall set the row to active(1). If the row already exists, it shall be an error. Writing createAndWait(5) to the RowStatus of a non-existent row shall create a row with default values and shall set the row to notInService(2). If the row already exists, it shall be an error. Writing active(1) to the RowStatus of an existing row shall change the value of that row to active(1). Writing active(1) to the RowStatus of an existing row that is already active(1) shall not cause an error, the row shall remain active(1). If the row does not exist, it shall be an error. Writing notInService(2) to the RowStatus of an existing row shall change the value of that row to notInService(2). Writing notInService(2) to the RowStatus of an existing row that is already notInService(2) shall not cause an error, the row shall remain notInService(2). If the row does not exist, it shall be an error. Writing destroy(6) to the RowStatus of a non-existent row shall be an error. If the row exists, it shall be removed. Writing notReady(3) to the RowStatus of a non-existent row or to an existent row shall be an error. If the user does not supply values for the necessary objects, default values will be supplied. Attempts to create more entries than the hardware can support shall be rejected.')
h3cL4RedirectCacheMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCacheMacAddress.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectCacheMacAddress.setDescription('This object defines the MAC address of the attached Web cache device. If only manual configuration of the cache is supported, this value must be supplied. The method of cache configuration can be ascertained by the presence or absence of the L4 manual cache configuration id within the 3com-352 MIB. The default value is 0.')
h3cL4RedirectCacheVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCacheVlan.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectCacheVlan.setDescription('This object specifies the VLAN which the cache port belongs to.')
h3cL4RedirectCacheTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectCacheTcpPort.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectCacheTcpPort.setDescription('This object specifies the TCP port number that is being redirected ')
h3cL4RedirectIpExclusionTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2), )
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionTable.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionTable.setDescription('This table lists the IP addresses and subnetworks that Web Cache redirection is not supported for. Some devices may not support addition to this table.')
h3cL4RedirectIpExclusionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-L4RDT-MIB", "h3cL4RedirectIpExclusionIpAddress"))
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionEntry.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionEntry.setDescription('Each row contains an IP address or a IP subnetwork that is being excluded from the redirection.')
h3cL4RedirectIpExclusionIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionIpAddress.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionIpAddress.setDescription('This object specifies the IP address or the subnetwork address that is to be excluded.')
h3cL4RedirectIpExclusionMaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionMaskLen.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionMaskLen.setDescription('This object provides the number of bits in the subnetwork mask. This mask shall be applied to the excludeIP address to determine the subnetwork that is to be excluded. A value of 32 implies that the excludeIP address refers to an individual host. The default value is 32.')
h3cL4RedirectIpExclusionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectIpExclusionRowStatus.setDescription('This object is used to add rows to the Exclusion Table. The following are the valid values that may be written to RowStatus: Writing createAndGo(4) to the RowStatus of a non-existent row shall create a new row. The new row shall be active(1). If the row exists, it shall be an error. Writing createAndWait(5) to the RowStatus of a non-existent row or to an existent row shall be an error. Writing active(1) to the RowStatus of an existing row shall change the value of that row to active(1). Writing active(1) to the RowStatus of an existing row that is already active(1) shall not cause an error, the row shall remain active(1). If the row does not exist, it shall be an error. Writing notInService(2) to the RowStatus of an existing row shall change the value of that row to notInService(2). Writing notInService(2) to the RowStatus of an existing row that is already notInService(2) shall not cause an error, the row shall remain notInService(2). If the row does not exist, it shall be an error. Writing destroy(6) to the RowStatus of a non-existent row shall be an error. If the row exists, it shall be removed. Writing notReady(3) to the RowStatus of a non-existent row or to an existent row shall be an error. Attempts to create more entries than the hardware can support shall be rejected.')
h3cL4RedirectVlanTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 3), )
if mibBuilder.loadTexts: h3cL4RedirectVlanTable.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectVlanTable.setDescription('This table contains a row for each VLAN of the packet which need to be redirected to the Web cache.')
h3cL4RedirectVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-L4RDT-MIB", "h3cL4RedirectVlanID"))
if mibBuilder.loadTexts: h3cL4RedirectVlanEntry.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectVlanEntry.setDescription('Each row specifies a VLAN of the packet which need to be redirected to the Web cache.')
h3cL4RedirectVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cL4RedirectVlanID.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectVlanID.setDescription('This object specifies the VLAN ID of the packet which need to be redirected to the Web cache.')
h3cL4RedirectVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cL4RedirectVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectVlanRowStatus.setDescription('This object allows ports to be added and removed from the table. The following are the valid values that may be written to RowStatus: Writing createAndGo(4) to the RowStatus of a non-existent row shall create a new row. The new row shall be active(1). If the row exists, it shall be an error. Writing createAndWait(5) to the RowStatus of a non-existent row or to an existent row shall be an error. Writing active(1) to the RowStatus of an existing row shall change the value of that row to active(1). Writing active(1) to the RowStatus of an existing row that is already active(1) shall not cause an error, the row shall remain active(1). If the row does not exist, it shall be an error. Writing notInService(2) to the RowStatus of a non-existent row or to an existent row shall be an error. Writing destroy(6) to the RowStatus of a non-existent row shall be an error. If the row exists, it shall be removed. Writing notReady(3) to the RowStatus of a non-existent row or to an existent row shall be an error. Attempts to create more entries than the hardware can support shall be rejected.')
h3cL4RedirectInformationString = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectInformationString.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectInformationString.setDescription('This object shall contain the string generated as a result of a Layer 4 Redirection configuration. It shall contain either a string describing successful configuration or a string describing unsuccessful configuration. This length of this string shall be no longer than 80 characters.')
h3cL4RedirectFreeCacheEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectFreeCacheEntries.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectFreeCacheEntries.setDescription('This object indicates the number of entries that may still be added to the h3cL4RedirectCacheTable.')
h3cL4RedirectFreeIpExclusionEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectFreeIpExclusionEntries.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectFreeIpExclusionEntries.setDescription('This object indicates the number of entries that may still be added to the h3cL4RedirectIpExclusionTable.')
h3cL4RedirectFreeVlanEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 10, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL4RedirectFreeVlanEntries.setStatus('current')
if mibBuilder.loadTexts: h3cL4RedirectFreeVlanEntries.setDescription('This object indicates the number of entries that may still be added to the h3cL4RedirectVlanTable.')
mibBuilder.exportSymbols("A3COM-HUAWEI-L4RDT-MIB", h3cL4RedirectIpExclusionRowStatus=h3cL4RedirectIpExclusionRowStatus, h3cL4RedirectCacheRedirectionStatus=h3cL4RedirectCacheRedirectionStatus, h3cL4RedirectCacheTable=h3cL4RedirectCacheTable, PYSNMP_MODULE_ID=h3cL4Redirect, h3cL4RedirectIpExclusionTable=h3cL4RedirectIpExclusionTable, h3cL4RedirectCacheRowStatus=h3cL4RedirectCacheRowStatus, h3cL4RedirectIpExclusionMaskLen=h3cL4RedirectIpExclusionMaskLen, h3cL4RedirectVlanID=h3cL4RedirectVlanID, h3cL4RedirectFreeVlanEntries=h3cL4RedirectFreeVlanEntries, h3cL4RedirectCacheEntry=h3cL4RedirectCacheEntry, h3cL4RedirectCacheVlan=h3cL4RedirectCacheVlan, h3cL4RedirectIpExclusionEntry=h3cL4RedirectIpExclusionEntry, h3cL4RedirectVlanRowStatus=h3cL4RedirectVlanRowStatus, h3cL4RedirectCacheTcpPort=h3cL4RedirectCacheTcpPort, h3cL4RedirectVlanEntry=h3cL4RedirectVlanEntry, h3cL4RedirectCachePort=h3cL4RedirectCachePort, h3cL4RedirectVlanTable=h3cL4RedirectVlanTable, h3cL4Redirect=h3cL4Redirect, h3cL4RedirectIpExclusionIpAddress=h3cL4RedirectIpExclusionIpAddress, h3cL4RedirectInformationString=h3cL4RedirectInformationString, h3cL4RedirectCacheIpAddress=h3cL4RedirectCacheIpAddress, h3cL4RedirectCacheMacAddress=h3cL4RedirectCacheMacAddress, h3cL4RedirectFreeCacheEntries=h3cL4RedirectFreeCacheEntries, h3cL4RedirectFreeIpExclusionEntries=h3cL4RedirectFreeIpExclusionEntries)
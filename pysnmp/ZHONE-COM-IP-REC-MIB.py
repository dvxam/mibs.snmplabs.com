#
# PySNMP MIB module ZHONE-COM-IP-REC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-IP-REC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:11:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
AtmVpIdentifier, AtmVcIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier", "AtmVcIdentifier")
InterfaceIndex, ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, ObjectIdentity, Bits, IpAddress, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Unsigned32, iso, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ObjectIdentity", "Bits", "IpAddress", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Unsigned32", "iso", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ZhoneRDIndex, = mibBuilder.importSymbols("ZHONE-COM-IP-RD-MIB", "ZhoneRDIndex")
zhoneIp, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneIp", "zhoneModules")
ZhoneAdminString, ZhoneRowStatus = mibBuilder.importSymbols("Zhone-TC", "ZhoneAdminString", "ZhoneRowStatus")
ipRecord = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 59))
ipRecord.setRevisions(('2010-09-01 09:17', '2010-05-04 02:24', '2008-06-27 08:14', '2006-02-17 17:37', '2006-01-23 09:26', '2005-07-20 17:22', '2004-07-21 08:46', '2004-05-27 09:56', '2004-04-28 14:02', '2003-04-18 10:03', '2002-04-17 16:48', '2002-02-11 16:57', '2001-10-30 10:44', '2001-06-06 16:00', '2001-03-15 10:28', '2001-02-26 13:58', '2001-02-13 11:13', '2001-01-19 18:16', '2001-01-17 16:18', '2000-11-20 10:18', '2000-10-05 15:12', '2000-09-15 14:30', '2000-09-12 10:06',))
if mibBuilder.loadTexts: ipRecord.setLastUpdated('201008310224Z')
if mibBuilder.loadTexts: ipRecord.setOrganization('Zhone Technologies, Inc.')
ipRecordObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9))
if mibBuilder.loadTexts: ipRecordObjects.setStatus('current')
ipInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2), )
if mibBuilder.loadTexts: ipInterfaceTable.setStatus('current')
ipInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ipInterfaceEntry.setStatus('current')
ipIfLgId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfLgId.setStatus('obsolete')
ipIfVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 2), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfVpi.setStatus('current')
ipIfVci = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 3), AtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfVci.setStatus('current')
ipIfRDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 4), ZhoneRDIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfRDIndex.setStatus('current')
ipIfDhcp = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noDhcp", 1), ("dhcpClient", 2), ("dhcpServer", 3), ("dhcpBoth", 4))).clone('noDhcp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfDhcp.setStatus('deprecated')
ipIfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 6), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfAddr.setStatus('current')
ipIfNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 7), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfNetMask.setStatus('current')
ipIfBcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 8), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfBcastAddr.setStatus('current')
ipIfDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 9), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfDestAddr.setStatus('current')
ipIfFarEndAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 10), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfFarEndAddr.setStatus('current')
ipIfMru = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 11), Unsigned32().clone(1500)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfMru.setStatus('current')
ipIfReasmMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfReasmMaxSize.setStatus('current')
ipIfIngressFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 13), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfIngressFilterName.setStatus('deprecated')
ipIfEgressFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 14), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfEgressFilterName.setStatus('deprecated')
ipIfPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfPointToPoint.setStatus('current')
ipIfMcastEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 16), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfMcastEnabled.setStatus('current')
ipIfIpFwdEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 17), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfIpFwdEnabled.setStatus('current')
ipIfMcastFwdEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 18), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfMcastFwdEnabled.setStatus('current')
ipIfNATEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 19), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfNATEnabled.setStatus('current')
ipIfBcastEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 20), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfBcastEnabled.setStatus('current')
ipIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 21), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfRowStatus.setStatus('current')
ipIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfAdminStatus.setStatus('current')
ipIfIngressPacketRuleGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfIngressPacketRuleGroupIndex.setStatus('current')
ipIfEgressPacketRuleGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfEgressPacketRuleGroupIndex.setStatus('current')
ipIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 25), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfLowerIfIndex.setStatus('current')
ipIfPppEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 26), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfPppEnabled.setStatus('current')
ipAddrDynamic = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("static", 1), ("ppp", 2), ("dhcpclient", 3), ("unnumbered", 4), ("cpemgr", 5))).clone('static')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipAddrDynamic.setStatus('current')
dhcpServerEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 28), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpServerEnable.setStatus('current')
dhcpSubnetGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 29), Integer32().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpSubnetGroup.setStatus('current')
unnumberedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 30), Integer32().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unnumberedIndex.setStatus('current')
mcastControlList = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 31), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mcastControlList.setStatus('current')
vlanid = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanid.setStatus('current')
maxVideoStreams = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 33), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: maxVideoStreams.setStatus('current')
tosOption = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tosOptionDisable", 1), ("tosOptionOriginate", 2), ("tosOptionAll", 3))).clone('tosOptionDisable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tosOption.setStatus('current')
tosCOS = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 35), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tosCOS.setStatus('current')
vlanCOS = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanCOS.setStatus('current')
ipStagTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(33024, 33024), ValueRangeConstraint(34984, 34984), ValueRangeConstraint(37120, 37120), ValueRangeConstraint(37376, 37376), )).clone(33024)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipStagTPID.setStatus('current')
ipStagId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipStagId.setStatus('current')
ipStagIdCOS = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 39), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipStagIdCOS.setStatus('current')
ipOnDemandStatsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 40), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipOnDemandStatsEnabled.setStatus('current')
ipIfAliasTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5), )
if mibBuilder.loadTexts: ipIfAliasTable.setStatus('current')
ipIfAliasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ZHONE-COM-IP-REC-MIB", "ipIfAliasAddr"))
if mibBuilder.loadTexts: ipIfAliasEntry.setStatus('current')
ipIfAliasAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipIfAliasAddr.setStatus('current')
ipIfAliasRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1, 2), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfAliasRowStatus.setStatus('current')
ipIfAliasNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfAliasNetMask.setStatus('current')
ipIfAliasBcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1, 4), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipIfAliasBcastAddr.setStatus('current')
ipUnnumbered = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 10))
if mibBuilder.loadTexts: ipUnnumbered.setStatus('deprecated')
ipUnnumberedEnabled = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 10, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipUnnumberedEnabled.setStatus('deprecated')
ipUnnumberedInterfaceIndex = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 10, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipUnnumberedInterfaceIndex.setStatus('deprecated')
ipUnnumberedObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 4, 1, 14))
ipUnnumberedObjectNext = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipUnnumberedObjectNext.setStatus('current')
ipUnnumberedTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2), )
if mibBuilder.loadTexts: ipUnnumberedTable.setStatus('current')
ipUnnumberedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2, 1), ).setIndexNames((0, "ZHONE-COM-IP-REC-MIB", "ipUnnumberedIndex"))
if mibBuilder.loadTexts: ipUnnumberedEntry.setStatus('current')
ipUnnumberedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ipUnnumberedIndex.setStatus('current')
ipUnnumberedRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2, 1, 2), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipUnnumberedRowStatus.setStatus('current')
ipUnnumberedIfIName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2, 1, 3), InterfaceIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipUnnumberedIfIName.setStatus('current')
mibBuilder.exportSymbols("ZHONE-COM-IP-REC-MIB", ipIfPppEnabled=ipIfPppEnabled, ipIfRowStatus=ipIfRowStatus, ipIfBcastAddr=ipIfBcastAddr, vlanid=vlanid, ipIfLgId=ipIfLgId, ipIfDhcp=ipIfDhcp, ipIfAliasNetMask=ipIfAliasNetMask, PYSNMP_MODULE_ID=ipRecord, ipUnnumberedTable=ipUnnumberedTable, ipIfFarEndAddr=ipIfFarEndAddr, ipStagId=ipStagId, ipIfNATEnabled=ipIfNATEnabled, ipIfAdminStatus=ipIfAdminStatus, dhcpServerEnable=dhcpServerEnable, ipIfIngressPacketRuleGroupIndex=ipIfIngressPacketRuleGroupIndex, ipUnnumbered=ipUnnumbered, ipStagIdCOS=ipStagIdCOS, ipUnnumberedEnabled=ipUnnumberedEnabled, ipIfPointToPoint=ipIfPointToPoint, ipIfIpFwdEnabled=ipIfIpFwdEnabled, ipIfBcastEnabled=ipIfBcastEnabled, ipUnnumberedInterfaceIndex=ipUnnumberedInterfaceIndex, ipUnnumberedIndex=ipUnnumberedIndex, ipStagTPID=ipStagTPID, ipIfMcastFwdEnabled=ipIfMcastFwdEnabled, ipRecord=ipRecord, ipIfAliasTable=ipIfAliasTable, ipIfRDIndex=ipIfRDIndex, ipIfAliasAddr=ipIfAliasAddr, ipIfVci=ipIfVci, ipInterfaceEntry=ipInterfaceEntry, ipRecordObjects=ipRecordObjects, ipIfEgressPacketRuleGroupIndex=ipIfEgressPacketRuleGroupIndex, ipIfEgressFilterName=ipIfEgressFilterName, mcastControlList=mcastControlList, ipIfNetMask=ipIfNetMask, tosCOS=tosCOS, ipIfDestAddr=ipIfDestAddr, ipIfMcastEnabled=ipIfMcastEnabled, unnumberedIndex=unnumberedIndex, ipIfAliasRowStatus=ipIfAliasRowStatus, tosOption=tosOption, ipUnnumberedRowStatus=ipUnnumberedRowStatus, maxVideoStreams=maxVideoStreams, ipUnnumberedObjectNext=ipUnnumberedObjectNext, ipIfMru=ipIfMru, ipIfVpi=ipIfVpi, ipIfIngressFilterName=ipIfIngressFilterName, ipOnDemandStatsEnabled=ipOnDemandStatsEnabled, ipIfReasmMaxSize=ipIfReasmMaxSize, ipUnnumberedEntry=ipUnnumberedEntry, ipIfLowerIfIndex=ipIfLowerIfIndex, ipAddrDynamic=ipAddrDynamic, vlanCOS=vlanCOS, ipIfAliasBcastAddr=ipIfAliasBcastAddr, ipIfAliasEntry=ipIfAliasEntry, ipUnnumberedIfIName=ipUnnumberedIfIName, ipUnnumberedObjects=ipUnnumberedObjects, dhcpSubnetGroup=dhcpSubnetGroup, ipInterfaceTable=ipInterfaceTable, ipIfAddr=ipIfAddr)

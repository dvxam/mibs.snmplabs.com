#
# PySNMP MIB module WWP-LEOS-SYSLOG-COLLECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-SYSLOG-COLLECTOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, Bits, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, NotificationType, Integer32, MibIdentifier, ObjectIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Bits", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "iso")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosSyslogCollectorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21))
wwpLeosSyslogCollectorMIB.setRevisions(('2012-04-05 00:00', '2006-04-18 10:12', '2003-01-21 10:12',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpLeosSyslogCollectorMIB.setRevisionsDescriptions(('Add new MIB OIDs to support IP protocol version independent Inet addressing. New attributes include: wwpLeosSyslogCollectorResolvedInetAddrType and wwpLeosSyslogCollectorResolvedInetAddress.', ' Added new table wwpLeosSyslogCollectorSeverityTable to support syslog collector severity. Deprecated wwpLeosSyslogCollectorMinSeverity and wwpLeosSyslogCollectorMaxSeverity. ', 'Initial Creation',))
if mibBuilder.loadTexts: wwpLeosSyslogCollectorMIB.setLastUpdated('201204050000Z')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorMIB.setOrganization(' Ciena Inc')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorMIB.setContactInfo(' Mib Meister 115 North Sullivan Road Spokane Valley, WA 99037 USA Phone: +1 509 242 9000 Email: support@ciena.com')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorMIB.setDescription('A MIB module to manage syslog collectors on the LEOS based WWP products.')
class SyslogFacility(TextualConvention, Integer32):
    description = 'This textual convention enumerates the facilities that originate syslog messages. The value noMap(24) indicates that the appropriate facility will be provided by the individual applications on the managed entity. If this option is not available on a particular entity attempt set the facillity to this value will fail with an error-status of wrongValue.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("kernel", 0), ("user", 1), ("mail", 2), ("daemon", 3), ("auth", 4), ("syslog", 5), ("lpr", 6), ("news", 7), ("uucp", 8), ("cron", 9), ("authPriv", 10), ("ftp", 11), ("ntp", 12), ("security", 13), ("console", 14), ("clockd2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23), ("noMap", 24))

class SyslogSeverity(TextualConvention, Integer32):
    description = 'This textual convention enumerates the severity levels of syslog messages. The syslog protocol uses the values 0 (emergency), to 7 (debug).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 99))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("other", 99))

wwpLeosSyslogCollMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1))
wwpLeosSyslogSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 1))
wwpLeosSyslogColl = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2))
wwpLeosSyslogCollMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 2))
wwpLeosSyslogCollMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 2, 0))
wwpLeosSyslogCollMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 3))
wwpLeosSyslogCollMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 3, 1))
wwpLeosSyslogCollMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 3, 2))
wwpLeosSyslogEnable = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosSyslogEnable.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogEnable.setDescription('Specifies whether or not the syslog client is enabled. This is the system wide parameter and will overwrite any collector specific managed object to enable or disable the syslog client.')
wwpLeosSyslogCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1), )
if mibBuilder.loadTexts: wwpLeosSyslogCollectorTable.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorTable.setDescription('A table containing Syslog collector information. To create entries in this table use SNMP multiple set operation. wwpLeosSyslogCollectorAddr, wwpLeosSyslogIndex and wwpLeosSyslogCollectorStatus are required fields that needs to be set to create entry. To delete entry set wwpLeosSyslogCollectorStatus to destroy.')
wwpLeosSyslogCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1), ).setIndexNames((0, "WWP-LEOS-SYSLOG-COLLECTOR-MIB", "wwpLeosSyslogIndex"))
if mibBuilder.loadTexts: wwpLeosSyslogCollectorEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorEntry.setDescription('Defines the information pertaining to a syslog collector to which a syslog messages will be relayed. Entries within this table with an access level of read- create MUST be considered non-volatile and MUST be maintained across entity resets.')
wwpLeosSyslogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: wwpLeosSyslogIndex.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogIndex.setDescription('Specifies the unique index used to represent each row in the table.')
wwpLeosSyslogCollectorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorAddr.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorAddr.setDescription('The address for the Syslog message collector. It can be Host Name or IP Address.')
wwpLeosSyslogCollectorResolvedAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorResolvedAddr.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorResolvedAddr.setDescription('When wwpLeosSyslogCollectorAddr represents: Host name : The resolved address will either be Ipv4 address or Ipv6 address. Ipv4 address : The resolved address will be the same Ipv4 address. Ipv6 address : The resolved address will be the same Ipv6 address. When the resolved address represents: Ipv4 address : wwpLeosSyslogCollectorResolvedAddr will represent the resolved Ipv4 address. wwpLeosSyslogCollectorResolvedInetAddr used in conjunction with wwpLeosSyslogCollectorResolvedInetAddrType will represent the same Ipv4 address. Ipv6 address : wwpLeosSyslogCollectorResolvedAddr will represent 0.0.0.0. wwpLeosSyslogCollectorResolvedInetAddr used in conjunction with wwpLeosSyslogCollectorResolvedInetAddrType will represent the Ipv6 address.')
wwpLeosSyslogCollectorUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(514)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorUDPPort.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorUDPPort.setDescription('The port number on the destination to which the syslog message will be forwarded over the udp transport.')
wwpLeosSyslogCollectorFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 5), SyslogFacility().clone('daemon')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorFacility.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorFacility.setDescription('The syslog facility code that will be added to the messages forwarded to this collector.')
wwpLeosSyslogCollectorMinSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 6), SyslogSeverity().clone('alert')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorMinSeverity.setStatus('deprecated')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorMinSeverity.setDescription('Any syslog message with a severity less than the severity specified by this object will be ignored by the collector. note: severity level numeric values increase as their severity decreases, e.g. error(3) is more severe than debug(7).')
wwpLeosSyslogCollectorMaxSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 7), SyslogSeverity().clone('emergency')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorMaxSeverity.setStatus('deprecated')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorMaxSeverity.setDescription('Any syslog message with a severity greater than the severity specified by this object will be ignored by the collector. note: severity level numeric values increase as their severity decreases, e.g. error(3) is more severe than debug(7).')
wwpLeosSyslogCollectorUserAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorUserAdminState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorUserAdminState.setDescription('Specifies the admin state of the wwpLeosSyslogCollectorAddr configured by user.')
wwpLeosSyslogCollectorDhcpAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorDhcpAdminState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorDhcpAdminState.setDescription('Specifies the admin state of the wwpLeosSyslogCollectorAddr configured by DHCP.')
wwpLeosSyslogCollectorOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorOperState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorOperState.setDescription('Specifies the operational state of the wwpLeosSyslogCollectorAddr.')
wwpLeosSyslogCollectorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorStatus.setDescription("Used to manage the creation and deletion of the conceptual rows in this table. To create a row in this table, a manager must set this object to 'createAndGo' and specify at least wwpLeosSyslogIndex and wwpLeosSyslogCollectorAddr. To delete the entry set this object to 'destroy'.")
wwpLeosSyslogCollectorCustomPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorCustomPrefix.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorCustomPrefix.setDescription('Specifies the syslog custom prefix that will be prepended to all syslog log messages before device sends syslog messages to syslog collectors.')
wwpLeosSyslogCollectorResolvedInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 13), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorResolvedInetAddrType.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorResolvedInetAddrType.setDescription('Specifies the resolved IP address type . Used in conjunction with wwpLeosSyslogCollectorResolvedInetAddress. When set to : ipv4 : wwpLeosSyslogCollectorResolvedInetAddress should be compliant with InetAddressIPv4 ipv6 : wwpLeosSyslogCollectorResolvedInetAddress should be compliant with InetAddressIPv6 ')
wwpLeosSyslogCollectorResolvedInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 14), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorResolvedInetAddress.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorResolvedInetAddress.setDescription('Specifies the resolved ip address for given wwpLeosSyslogCollectorAddr. If wwpLeosSyslogCollectorAddr is set to host name then wwpLeosSyslogCollectorResolvedInetAddr will display the resolved IP address. If wwpLeosSyslogCollectorAddr is set to IP address then wwpLeosSyslogCollectorResolvedInetAddr will display same value as wwpLeosSyslogCollectorAddr. This OID should be used in conjuction with wwpLeosSyslogCollectorResolvedInetAddrType. ')
wwpLeosSyslogCollectorSeverityTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 2), )
if mibBuilder.loadTexts: wwpLeosSyslogCollectorSeverityTable.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorSeverityTable.setDescription('A table containing Syslog collector severity information. To create entries in this table following objects must be specified. - Indexes must be specified - To delete entry set wwpLeosSyslogCollectorStatus to destroy.')
wwpLeosSyslogCollectorSeverityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 2, 1), ).setIndexNames((0, "WWP-LEOS-SYSLOG-COLLECTOR-MIB", "wwpLeosSyslogIndex"), (0, "WWP-LEOS-SYSLOG-COLLECTOR-MIB", "wwpLeosSyslogCollectorSeverity"))
if mibBuilder.loadTexts: wwpLeosSyslogCollectorSeverityEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorSeverityEntry.setDescription('Defines the information pertaining to a syslog collector severity to which a syslog messages will be relayed. Syslog Collector will only receive messages of severity that exist in this table.')
wwpLeosSyslogCollectorSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 2, 1, 1), SyslogSeverity())
if mibBuilder.loadTexts: wwpLeosSyslogCollectorSeverity.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorSeverity.setDescription('This mib object specifies the severity of the syslog message that this collector should receive.')
wwpLeosSyslogCollectorSeverityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosSyslogCollectorSeverityRowStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLeosSyslogCollectorSeverityRowStatus.setDescription("Used to manage the creation and deletion of the conceptual rows in this table. To create a row in this table, a manager must set this object to 'createAndGo'. To delete the entry set this to 'destroy'.")
mibBuilder.exportSymbols("WWP-LEOS-SYSLOG-COLLECTOR-MIB", wwpLeosSyslogCollectorSeverityRowStatus=wwpLeosSyslogCollectorSeverityRowStatus, wwpLeosSyslogCollMIBConformance=wwpLeosSyslogCollMIBConformance, wwpLeosSyslogCollectorDhcpAdminState=wwpLeosSyslogCollectorDhcpAdminState, wwpLeosSyslogCollMIBGroups=wwpLeosSyslogCollMIBGroups, wwpLeosSyslogCollectorOperState=wwpLeosSyslogCollectorOperState, wwpLeosSyslogCollectorResolvedInetAddress=wwpLeosSyslogCollectorResolvedInetAddress, wwpLeosSyslogCollectorResolvedAddr=wwpLeosSyslogCollectorResolvedAddr, SyslogFacility=SyslogFacility, wwpLeosSyslogCollectorStatus=wwpLeosSyslogCollectorStatus, wwpLeosSyslogCollectorFacility=wwpLeosSyslogCollectorFacility, wwpLeosSyslogCollectorMinSeverity=wwpLeosSyslogCollectorMinSeverity, wwpLeosSyslogCollectorCustomPrefix=wwpLeosSyslogCollectorCustomPrefix, wwpLeosSyslogCollectorUserAdminState=wwpLeosSyslogCollectorUserAdminState, wwpLeosSyslogCollectorSeverity=wwpLeosSyslogCollectorSeverity, wwpLeosSyslogCollMIBCompliances=wwpLeosSyslogCollMIBCompliances, wwpLeosSyslogCollectorMIB=wwpLeosSyslogCollectorMIB, PYSNMP_MODULE_ID=wwpLeosSyslogCollectorMIB, wwpLeosSyslogCollectorTable=wwpLeosSyslogCollectorTable, wwpLeosSyslogColl=wwpLeosSyslogColl, wwpLeosSyslogCollectorMaxSeverity=wwpLeosSyslogCollectorMaxSeverity, wwpLeosSyslogIndex=wwpLeosSyslogIndex, wwpLeosSyslogCollectorUDPPort=wwpLeosSyslogCollectorUDPPort, wwpLeosSyslogCollectorAddr=wwpLeosSyslogCollectorAddr, wwpLeosSyslogCollectorResolvedInetAddrType=wwpLeosSyslogCollectorResolvedInetAddrType, wwpLeosSyslogCollMIBNotificationPrefix=wwpLeosSyslogCollMIBNotificationPrefix, wwpLeosSyslogSystem=wwpLeosSyslogSystem, wwpLeosSyslogCollectorSeverityTable=wwpLeosSyslogCollectorSeverityTable, wwpLeosSyslogCollectorSeverityEntry=wwpLeosSyslogCollectorSeverityEntry, wwpLeosSyslogCollMIBNotifications=wwpLeosSyslogCollMIBNotifications, SyslogSeverity=SyslogSeverity, wwpLeosSyslogCollMIBObjects=wwpLeosSyslogCollMIBObjects, wwpLeosSyslogEnable=wwpLeosSyslogEnable, wwpLeosSyslogCollectorEntry=wwpLeosSyslogCollectorEntry)

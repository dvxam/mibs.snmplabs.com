#
# PySNMP MIB module HUAWEI-IPHC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-IPHC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:45:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifIndex, ifName = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifName")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, iso, Counter32, Unsigned32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, IpAddress, ModuleIdentity, NotificationType, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Counter32", "Unsigned32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "IpAddress", "ModuleIdentity", "NotificationType", "TimeTicks", "Bits")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hwIphcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154))
if mibBuilder.loadTexts: hwIphcMIB.setLastUpdated('200707230000Z')
if mibBuilder.loadTexts: hwIphcMIB.setOrganization('Huawei Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwIphcMIB.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwIphcMIB.setDescription('HUAWEI-IPHC-MIB is a private MIB defined by Huawei. It describes the configurations, configuration status, and statistics of IP packet header compression. ')
class HWCompressType(TextualConvention, Integer32):
    description = 'The Compress type: withoutCompress(1), enableTcpCompress(2), enableRtpCompress(3), enableEcRtpCompress(4), enableUdpCompressOnly(5), enableUdpandRtpCompressOnly(6) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("withoutCompress", 1), ("enableTcpCompress", 2), ("enableRtpCompress", 3), ("enableEcRtpCompress", 4), ("enableUdpCompressOnly", 5), ("enableUdpandRtpCompressOnly", 6))

class HWCompressFormat(TextualConvention, Integer32):
    description = 'Compress packets in ietf-format(defined in RFC2507) or not '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ietf", 1), ("nonstandard", 2))

hwIphcInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1))
hwIphcTcpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1), )
if mibBuilder.loadTexts: hwIphcTcpConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpConfigTable.setDescription('This table is used to configure the parameters of IP/TCP header compression.')
hwIphcTcpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1), ).setIndexNames((0, "HUAWEI-IPHC-MIB", "hwIphcTcpIfIndex"))
if mibBuilder.loadTexts: hwIphcTcpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpConfigEntry.setDescription('An entry in this table.')
hwIphcTcpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hwIphcTcpIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpIfIndex.setDescription('Index of the interface enabled with IP/TCP header compression, the same as IfIndex of this interface. ')
hwIphcTcpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1, 2), HWCompressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwIphcTcpEnable.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpEnable.setDescription('Identifies whether IP/TCP header compression is enabled on the interface. The default value is 2.')
hwIphcTcpConnnectionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwIphcTcpConnnectionNumber.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpConnnectionNumber.setDescription('The maximum number of IP/TCP header compression sessions on the interface.The default value is 16.')
hwIphcTcpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwIphcTcpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpRowStatus.setDescription('Row status.')
hwIphcTcpConfigEffectTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 2), )
if mibBuilder.loadTexts: hwIphcTcpConfigEffectTable.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpConfigEffectTable.setDescription('This table lists the valid parameters of IP/TCP header compression on the interface after negotiation with the peer interface. ')
hwIphcTcpConfigEffectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 2, 1), ).setIndexNames((0, "HUAWEI-IPHC-MIB", "hwIphcTcpIfIndex"))
if mibBuilder.loadTexts: hwIphcTcpConfigEffectEntry.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpConfigEffectEntry.setDescription('An entry in this table.')
hwIphcTcpEffectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 2, 1, 1), HWCompressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpEffectEnable.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpEffectEnable.setDescription('Identifies whether the IP/TCP header compression is effective on the interface after negotiation with the peer interface. ')
hwIphcTcpEffectConnnectionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpEffectConnnectionNumber.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpEffectConnnectionNumber.setDescription('The maximum number of valid IP/TCP header compression sessions on the interface after negotiation with the peer interface. ')
hwIphcRtpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3), )
if mibBuilder.loadTexts: hwIphcRtpConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpConfigTable.setDescription('This table is used to configure the parameters of IP/UDP or IP/UDP/RTP header compression.')
hwIphcRtpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1), ).setIndexNames((0, "HUAWEI-IPHC-MIB", "hwIphcRtpIfIndex"))
if mibBuilder.loadTexts: hwIphcRtpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpConfigEntry.setDescription('An entry in this table.')
hwIphcRtpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hwIphcRtpIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpIfIndex.setDescription('Index of the interface enabled with IP/UDP or IP/UDP/RTP header compression, the same as IfIndex of this interface')
hwIphcRtpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 2), HWCompressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwIphcRtpEnable.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpEnable.setDescription('Identifies whether IP/UDP and IP/UDP/RTP header compression is enabled on the interface. ')
hwIphcRtpConnnectionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwIphcRtpConnnectionNumber.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpConnnectionNumber.setDescription('The maximum number of IP/UDP and IP/UDP/RTP header compression sessions on the interface.')
hwIphcRtpNValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwIphcRtpNValue.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpNValue.setDescription('The number of packet retransmissions when EcRTP is enabled on the interface.')
hwIphcRtpFormatType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 5), HWCompressFormat()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwIphcRtpFormatType.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpFormatType.setDescription('Compressed packet format supported by the interface. ')
hwIphcRtpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwIphcRtpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpRowStatus.setDescription('Row status.')
hwIphcRtpConfigEffectTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4), )
if mibBuilder.loadTexts: hwIphcRtpConfigEffectTable.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpConfigEffectTable.setDescription('This table lists the valid parameters of IP/UDP and IP/UDP/RTP header compression on the interface after negotiation with the peer interface. ')
hwIphcRtpConfigEffectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4, 1), ).setIndexNames((0, "HUAWEI-IPHC-MIB", "hwIphcRtpIfIndex"))
if mibBuilder.loadTexts: hwIphcRtpConfigEffectEntry.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpConfigEffectEntry.setDescription('An entry in this table.')
hwIphcRtpEffectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4, 1, 1), HWCompressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpEffectEnable.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpEffectEnable.setDescription('Identifies whether IP/UDP and IP/UDP/RTP header compression is effective on the interface after negotiation with the peer interface.')
hwIphcRtpEffectConnnectionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpEffectConnnectionNumber.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpEffectConnnectionNumber.setDescription('The maximum number of valid IP/UDP and IP/UDP/RTP header compression sessions on the interface.')
hwIphcRtpEffectNValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpEffectNValue.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpEffectNValue.setDescription('The number of packet retransmissions when EcRTP is enabled on the interface after negotiation with the peer interface.')
hwIphcStatisticsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2))
hwIphcTcpRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1), )
if mibBuilder.loadTexts: hwIphcTcpRunInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpRunInfoTable.setDescription('This table lists statistics on IP/TCP header compression.')
hwIphcTcpRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1), ).setIndexNames((0, "HUAWEI-IPHC-MIB", "hwIphcTcpIfIndex"))
if mibBuilder.loadTexts: hwIphcTcpRunInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpRunInfoEntry.setDescription('An entry in this table.')
hwIphcTcpSentTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpSentTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpSentTotalPackets.setDescription('Total number of sent packets with IP/TCP header.')
hwIphcTcpSentTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpSentTotalBytes.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpSentTotalBytes.setDescription('Total number of the bytes of sent packets with IP/TCP header.')
hwIphcTcpSentCompressPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpSentCompressPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpSentCompressPackets.setDescription('Number of compressed packets.')
hwIphcTcpSentCompressBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpSentCompressBytes.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpSentCompressBytes.setDescription('Number of the bytes of compressed packets with IP/TCP header.')
hwIphcTcpSavedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpSavedBytes.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpSavedBytes.setDescription('Number of the bytes saved after compression with IP/TCP header.')
hwIphcTcpCompressRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpCompressRatio.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpCompressRatio.setDescription('Compression ratio.')
hwIphcTcpReceivedTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpReceivedTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpReceivedTotalPackets.setDescription('Total number of received packets with IP/TCP header.')
hwIphcTcpReceivedCompressPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpReceivedCompressPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpReceivedCompressPackets.setDescription('Total number of received compressed packets with IP/TCP header.')
hwIphcTcpReceivedCompressErrorPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpReceivedCompressErrorPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpReceivedCompressErrorPackets.setDescription('Number of incorrectly-compressed packets with IP/TCP header.')
hwIphcTcpReceivedCompressDiscardPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcTcpReceivedCompressDiscardPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcTcpReceivedCompressDiscardPackets.setDescription('Number of the packets discarded due to failed decompression with IP/TCP header.')
hwIphcRtpRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2), )
if mibBuilder.loadTexts: hwIphcRtpRunInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpRunInfoTable.setDescription('This table lists statistics on IP/UDP or IP/UDP/RTP header compression.')
hwIphcRtpRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1), ).setIndexNames((0, "HUAWEI-IPHC-MIB", "hwIphcRtpIfIndex"))
if mibBuilder.loadTexts: hwIphcRtpRunInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpRunInfoEntry.setDescription('An entry in this table.')
hwIphcRtpSentTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpSentTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpSentTotalPackets.setDescription('Total number of sent packets with IP/UDP or IP/UDP/RTP header.')
hwIphcRtpSentTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpSentTotalBytes.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpSentTotalBytes.setDescription('Total number of the bytes of sent packets with IP/UDP or IP/UDP/RTP header.')
hwIphcRtpSentCompressPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpSentCompressPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpSentCompressPackets.setDescription('Number of sent compressed packets with IP/UDP or IP/UDP/RTP header.')
hwIphcRtpSentCompressBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpSentCompressBytes.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpSentCompressBytes.setDescription('Number of the bytes of sent compressed packets with IP/UDP or IP/UDP/RTP header.')
hwIphcRtpSavedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpSavedBytes.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpSavedBytes.setDescription('Number of saved bytes after compression with IP/UDP or IP/UDP/RTP header.')
hwIphcRtpCompressRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpCompressRatio.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpCompressRatio.setDescription('Compression ratio.')
hwIphcRtpReceivedTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpReceivedTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpReceivedTotalPackets.setDescription('Total number of received packets with IP/UDP or IP/UDP/RTP header.')
hwIphcRtpReceivedCompressPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpReceivedCompressPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpReceivedCompressPackets.setDescription('Total number of the bytes of received compressed packets with IP/UDP or IP/UDP/RTP header.')
hwIphcRtpReceivedCompressErrorPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpReceivedCompressErrorPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpReceivedCompressErrorPackets.setDescription('Number of received incorrectly-compressed packets with IP/UDP or IP/UDP/RTP header.')
hwIphcRtpReceivedCompressDiscardPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIphcRtpReceivedCompressDiscardPackets.setStatus('current')
if mibBuilder.loadTexts: hwIphcRtpReceivedCompressDiscardPackets.setDescription('Number of packets discarded due to failed compression with IP/UDP or IP/UDP/RTP header.')
hwIphcTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 3))
hwIphcContextError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 3, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwIphcContextError.setStatus('current')
if mibBuilder.loadTexts: hwIphcContextError.setDescription('During a specified period, the number of the CONTEXT_STATE packets received by the compressor exceeds the threshold. ')
hwIphcContextErrorResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 3, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwIphcContextErrorResume.setStatus('current')
if mibBuilder.loadTexts: hwIphcContextErrorResume.setDescription('During a specified period, the number of the CONTEXT_STATE packets received by the compressor restores to the normal state. ')
hwIphcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4))
hwIphcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 1))
hwIphcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 1, 1)).setObjects(("HUAWEI-IPHC-MIB", "hwIphcInfoGroup"), ("HUAWEI-IPHC-MIB", "hwIphcStatisticsGroup"), ("HUAWEI-IPHC-MIB", "hwIphcNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIphcCompliance = hwIphcCompliance.setStatus('current')
if mibBuilder.loadTexts: hwIphcCompliance.setDescription('The compliance statement for systems supporting the HUAWEI-IPHC-MIB.')
hwIphcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 2))
hwIphcInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 2, 1)).setObjects(("HUAWEI-IPHC-MIB", "hwIphcTcpEnable"), ("HUAWEI-IPHC-MIB", "hwIphcTcpConnnectionNumber"), ("HUAWEI-IPHC-MIB", "hwIphcTcpRowStatus"), ("HUAWEI-IPHC-MIB", "hwIphcTcpEffectEnable"), ("HUAWEI-IPHC-MIB", "hwIphcTcpEffectConnnectionNumber"), ("HUAWEI-IPHC-MIB", "hwIphcRtpEnable"), ("HUAWEI-IPHC-MIB", "hwIphcRtpConnnectionNumber"), ("HUAWEI-IPHC-MIB", "hwIphcRtpNValue"), ("HUAWEI-IPHC-MIB", "hwIphcRtpFormatType"), ("HUAWEI-IPHC-MIB", "hwIphcRtpRowStatus"), ("HUAWEI-IPHC-MIB", "hwIphcRtpEffectEnable"), ("HUAWEI-IPHC-MIB", "hwIphcRtpEffectConnnectionNumber"), ("HUAWEI-IPHC-MIB", "hwIphcRtpEffectNValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIphcInfoGroup = hwIphcInfoGroup.setStatus('current')
if mibBuilder.loadTexts: hwIphcInfoGroup.setDescription('Standard HUAWEI IPHC Configuration group.')
hwIphcStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 2, 2)).setObjects(("HUAWEI-IPHC-MIB", "hwIphcTcpSentTotalPackets"), ("HUAWEI-IPHC-MIB", "hwIphcTcpSentTotalBytes"), ("HUAWEI-IPHC-MIB", "hwIphcTcpSentCompressPackets"), ("HUAWEI-IPHC-MIB", "hwIphcTcpSentCompressBytes"), ("HUAWEI-IPHC-MIB", "hwIphcTcpSavedBytes"), ("HUAWEI-IPHC-MIB", "hwIphcTcpCompressRatio"), ("HUAWEI-IPHC-MIB", "hwIphcTcpReceivedTotalPackets"), ("HUAWEI-IPHC-MIB", "hwIphcTcpReceivedCompressPackets"), ("HUAWEI-IPHC-MIB", "hwIphcTcpReceivedCompressErrorPackets"), ("HUAWEI-IPHC-MIB", "hwIphcTcpReceivedCompressDiscardPackets"), ("HUAWEI-IPHC-MIB", "hwIphcRtpSentTotalPackets"), ("HUAWEI-IPHC-MIB", "hwIphcRtpSentTotalBytes"), ("HUAWEI-IPHC-MIB", "hwIphcRtpSentCompressPackets"), ("HUAWEI-IPHC-MIB", "hwIphcRtpSentCompressBytes"), ("HUAWEI-IPHC-MIB", "hwIphcRtpSavedBytes"), ("HUAWEI-IPHC-MIB", "hwIphcRtpCompressRatio"), ("HUAWEI-IPHC-MIB", "hwIphcRtpReceivedTotalPackets"), ("HUAWEI-IPHC-MIB", "hwIphcRtpReceivedCompressPackets"), ("HUAWEI-IPHC-MIB", "hwIphcRtpReceivedCompressErrorPackets"), ("HUAWEI-IPHC-MIB", "hwIphcRtpReceivedCompressDiscardPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIphcStatisticsGroup = hwIphcStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: hwIphcStatisticsGroup.setDescription('Standard HUAWEI IPHC Statistics group.')
hwIphcNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 2, 3)).setObjects(("HUAWEI-IPHC-MIB", "hwIphcContextError"), ("HUAWEI-IPHC-MIB", "hwIphcContextErrorResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIphcNotificationGroup = hwIphcNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwIphcNotificationGroup.setDescription('Standard HUAWEI IPHC Notification group.')
mibBuilder.exportSymbols("HUAWEI-IPHC-MIB", hwIphcTcpIfIndex=hwIphcTcpIfIndex, hwIphcTcpCompressRatio=hwIphcTcpCompressRatio, hwIphcRtpSentCompressBytes=hwIphcRtpSentCompressBytes, hwIphcRtpNValue=hwIphcRtpNValue, hwIphcRtpReceivedCompressPackets=hwIphcRtpReceivedCompressPackets, hwIphcTcpConnnectionNumber=hwIphcTcpConnnectionNumber, hwIphcInfoObjects=hwIphcInfoObjects, HWCompressFormat=HWCompressFormat, hwIphcStatisticsGroup=hwIphcStatisticsGroup, hwIphcRtpReceivedCompressDiscardPackets=hwIphcRtpReceivedCompressDiscardPackets, hwIphcGroups=hwIphcGroups, hwIphcRtpSavedBytes=hwIphcRtpSavedBytes, hwIphcNotificationGroup=hwIphcNotificationGroup, hwIphcRtpFormatType=hwIphcRtpFormatType, hwIphcRtpSentCompressPackets=hwIphcRtpSentCompressPackets, hwIphcTcpConfigEffectEntry=hwIphcTcpConfigEffectEntry, hwIphcTcpReceivedCompressPackets=hwIphcTcpReceivedCompressPackets, hwIphcContextErrorResume=hwIphcContextErrorResume, hwIphcTcpReceivedCompressDiscardPackets=hwIphcTcpReceivedCompressDiscardPackets, hwIphcTcpSentTotalPackets=hwIphcTcpSentTotalPackets, hwIphcRtpSentTotalBytes=hwIphcRtpSentTotalBytes, hwIphcTcpEffectEnable=hwIphcTcpEffectEnable, hwIphcRtpIfIndex=hwIphcRtpIfIndex, hwIphcRtpConfigEffectTable=hwIphcRtpConfigEffectTable, hwIphcTcpConfigEntry=hwIphcTcpConfigEntry, hwIphcTcpReceivedCompressErrorPackets=hwIphcTcpReceivedCompressErrorPackets, hwIphcInfoGroup=hwIphcInfoGroup, hwIphcRtpSentTotalPackets=hwIphcRtpSentTotalPackets, hwIphcTraps=hwIphcTraps, hwIphcTcpReceivedTotalPackets=hwIphcTcpReceivedTotalPackets, hwIphcMIB=hwIphcMIB, hwIphcRtpReceivedCompressErrorPackets=hwIphcRtpReceivedCompressErrorPackets, hwIphcCompliances=hwIphcCompliances, hwIphcTcpSentTotalBytes=hwIphcTcpSentTotalBytes, hwIphcRtpEffectNValue=hwIphcRtpEffectNValue, hwIphcTcpRunInfoEntry=hwIphcTcpRunInfoEntry, hwIphcTcpSentCompressPackets=hwIphcTcpSentCompressPackets, hwIphcRtpCompressRatio=hwIphcRtpCompressRatio, hwIphcTcpRowStatus=hwIphcTcpRowStatus, hwIphcStatisticsObjects=hwIphcStatisticsObjects, hwIphcTcpEnable=hwIphcTcpEnable, hwIphcRtpRowStatus=hwIphcRtpRowStatus, hwIphcRtpConfigEntry=hwIphcRtpConfigEntry, hwIphcRtpRunInfoTable=hwIphcRtpRunInfoTable, HWCompressType=HWCompressType, PYSNMP_MODULE_ID=hwIphcMIB, hwIphcTcpConfigEffectTable=hwIphcTcpConfigEffectTable, hwIphcTcpConfigTable=hwIphcTcpConfigTable, hwIphcRtpReceivedTotalPackets=hwIphcRtpReceivedTotalPackets, hwIphcConformance=hwIphcConformance, hwIphcRtpConfigTable=hwIphcRtpConfigTable, hwIphcTcpSavedBytes=hwIphcTcpSavedBytes, hwIphcRtpEffectEnable=hwIphcRtpEffectEnable, hwIphcTcpEffectConnnectionNumber=hwIphcTcpEffectConnnectionNumber, hwIphcRtpConnnectionNumber=hwIphcRtpConnnectionNumber, hwIphcContextError=hwIphcContextError, hwIphcTcpRunInfoTable=hwIphcTcpRunInfoTable, hwIphcRtpRunInfoEntry=hwIphcRtpRunInfoEntry, hwIphcCompliance=hwIphcCompliance, hwIphcRtpConfigEffectEntry=hwIphcRtpConfigEffectEntry, hwIphcRtpEnable=hwIphcRtpEnable, hwIphcTcpSentCompressBytes=hwIphcTcpSentCompressBytes, hwIphcRtpEffectConnnectionNumber=hwIphcRtpEffectConnnectionNumber)
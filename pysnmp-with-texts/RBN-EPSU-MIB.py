#
# PySNMP MIB module RBN-EPSU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-EPSU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, IpAddress, Bits, Gauge32, Counter64, Unsigned32, NotificationType, ObjectIdentity, TimeTicks, Integer32, iso, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Bits", "Gauge32", "Counter64", "Unsigned32", "NotificationType", "ObjectIdentity", "TimeTicks", "Integer32", "iso", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnEpsuMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 47))
rbnEpsuMIB.setRevisions(('2009-09-23 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnEpsuMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: rbnEpsuMIB.setLastUpdated('200909231200Z')
if mibBuilder.loadTexts: rbnEpsuMIB.setOrganization('Redback Networks, Inc.')
if mibBuilder.loadTexts: rbnEpsuMIB.setContactInfo(' Redback Networks, Inc. Postal: 300 Holger Way San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 ')
if mibBuilder.loadTexts: rbnEpsuMIB.setDescription('Evolved Packet System (EPS) user plane statistics.')
rbnEpsuStatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1))
rbnEpsuS1uGtp = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1))
rbnEpsuS1uDlPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 1), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uDlPktsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uDlPktsSent.setDescription('Total number of downlink GTP payload packets sent to eNodeBs over the S1-U interface.')
rbnEpsuS1uDlOctetsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 2), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uDlOctetsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uDlOctetsSent.setDescription('Total number of octets in downlink GTP payload packets sent to eNodeBs over the S1-U interface.')
rbnEpsuS1uDlPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 3), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uDlPktsDropped.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uDlPktsDropped.setDescription('Total number of downlink GTP payload packets dropped that should have been sent to eNodeBs over the S1-U interface.')
rbnEpsuS1uDlPolicingPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 4), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uDlPolicingPktsDropped.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uDlPolicingPktsDropped.setDescription('Total number of downlink GTP payload packets dropped due to MBR policing that should have been sent to eNodeBs over the S1-U interface.')
rbnEpsuS1uDlUeIdlePktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 5), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uDlUeIdlePktsDropped.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uDlUeIdlePktsDropped.setDescription('Total number of downlink GTP payload packets which should have been sent to eNodeBs over the S1-U interface but were dropped due to UE in the idle mode, or the buffer has become full, or the UE has not been activated in a timely manner.')
rbnEpsuS1uUlPktsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 6), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uUlPktsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uUlPktsRcvd.setDescription('Total number of uplink GTP payload packets received from eNodeBs over the S1-U interface')
rbnEpsuS1uUlOctetsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 7), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uUlOctetsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uUlOctetsRcvd.setDescription('Total number of octets in uplink GTP payload packets received from eNodeBs over the S1-U interface.')
rbnEpsuS1uUlPktsDiscarded = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 8), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uUlPktsDiscarded.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uUlPktsDiscarded.setDescription('Total number of discarded uplink payload GTP packets received from eNodeBs over the S1-U interface.')
rbnEpsuS1uUlBearerPktsDiscarded = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 9), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uUlBearerPktsDiscarded.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uUlBearerPktsDiscarded.setDescription('Total number of uplink payload GTP packets received from eNodeBs over the S1-U interface that were discarded due to bearer validation failure.')
rbnEpsuS1uUlPolicingPktsDiscarded = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 10), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS1uUlPolicingPktsDiscarded.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uUlPolicingPktsDiscarded.setDescription('Total number of uplink GTP payload packets received from eNodeBs over the S1-U interface that were discarded due to MBR policing.')
rbnEpsuSgwGtp = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2))
rbnEpsuS5S8GtpDlPktsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 1), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPktsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPktsRcvd.setDescription('Total number of downlink GTP payload packets received from the PGW over the S5/S8 interface.')
rbnEpsuS5S8GtpDlOctetsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 2), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlOctetsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlOctetsRcvd.setDescription('Total number of octets in downlink GTP payload packets received from the PGW over the S5/S8 interface.')
rbnEpsuS5S8GtpDlPktsDiscarded = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 3), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPktsDiscarded.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPktsDiscarded.setDescription('Total number of discarded downlink GTP payload packets received from the PGW over the S5/S8 interface.')
rbnEpsuS5S8GtpUlPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 4), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPktsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPktsSent.setDescription('Total number of uplink GTP payload packets sent tp the PGW over the S5/S8 interface.')
rbnEpsuS5S8GtpUlOctetsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 5), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlOctetsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlOctetsSent.setDescription('Total number of octets in uplink GTP payload packets sent to the PGW over the S5/S8 interface.')
rbnEpsuS5S8GtpUlPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 6), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPktsDropped.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPktsDropped.setDescription('Total number of dropped uplink GTP payload packets that should have been sent to the PGW over the S5/S8 interface.')
rbnEpsuPgwGtp = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3))
rbnEpsuS5S8GtpDlPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 1), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPktsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPktsSent.setDescription('Total number of downlink GTP payload packets sent to SGW over the S5/S8 interface.')
rbnEpsuS5S8GtpDlOctetsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 2), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlOctetsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlOctetsSent.setDescription('Total number of octets in downlink GTP payload packets sent to SGW over the S5/S8 interface.')
rbnEpsuS5S8GtpDlPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 3), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPktsDropped.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPktsDropped.setDescription('Total number of dropped downlink GTP payload packets that should have been sent to SGW over the S5/S8 interface.')
rbnEpsuS5S8GtpDlPolicingPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 4), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPolicingPktsDropped.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpDlPolicingPktsDropped.setDescription('Total number of downlink GTP payload packets dropped due to MBR policing that should have been sent to SGW over the S5/S8 interface.')
rbnEpsuS5S8GtpUlPktsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 5), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPktsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPktsRcvd.setDescription('Total number of uplink GTP payload packets received from SGW over the S5/S8 interface.')
rbnEpsuS5S8GtpUlOctetsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 6), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlOctetsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlOctetsRcvd.setDescription('Total number of octets in uplink GTP payload packets received from SGW over the S5/S8 interface.')
rbnEpsuS5S8GtpUlPktsDiscarded = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 7), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPktsDiscarded.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPktsDiscarded.setDescription('Total number of discarded uplink GTP payload packets received from SGW over the S5/S8 interface.')
rbnEpsuS5S8GtpUlBearerPktsDiscarded = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 8), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlBearerPktsDiscarded.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlBearerPktsDiscarded.setDescription('Total number of uplink GTP payload packets received from SGW over the S5/S8 interface that were discarded due to bearer validation failure.')
rbnEpsuS5S8GtpUlPolicingPktsDiscarded = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 9), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPolicingPktsDiscarded.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS5S8GtpUlPolicingPktsDiscarded.setDescription('Total number of uplink GTP payload packets received from SGW over the S5/S8 interface that were discarded due to MBR policiing.')
rbnEpsuSgi = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4))
rbnEpsuSgiDlPktsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 1), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiDlPktsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiDlPktsRcvd.setDescription('Total number of downlink user payload packets received over the SGi interface.')
rbnEpsuSgiDlOctetsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 2), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiDlOctetsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiDlOctetsRcvd.setDescription('Total number of octets in downlink user payload packets received over the SGi interface.')
rbnEpsuSgiDlV6PktsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 3), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiDlV6PktsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiDlV6PktsRcvd.setDescription('Total number of downlink IPv6 user payload packets received over the SGi interface.')
rbnEpsuSgiDlV6OctetsRcvd = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 4), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiDlV6OctetsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiDlV6OctetsRcvd.setDescription('Total number of octets in downlink IPv6 user payload packets received over the SGi interface.')
rbnEpsuSgiDlPktsDiscarded = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 5), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiDlPktsDiscarded.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiDlPktsDiscarded.setDescription('Total number of discarded downlink user payload packets received over the SGi interface.')
rbnEpsuSgiUlPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 6), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiUlPktsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiUlPktsSent.setDescription('Total number of uplink user payload packets sent over the SGi interface.')
rbnEpsuSgiUlOctetsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 7), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiUlOctetsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiUlOctetsSent.setDescription('Total number of octets in uplink user payload packets sent over the SGi interface.')
rbnEpsuSgiUlV6PktsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 8), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiUlV6PktsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiUlV6PktsSent.setDescription('Total number of uplink IPv6 user payload packets sent over the SGi interface.')
rbnEpsuSgiUlV6OctetsSent = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 9), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiUlV6OctetsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiUlV6OctetsSent.setDescription('Total number of octets in uplink user payload packets sent over the SGi interface.')
rbnEpsuSgiUlPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 10), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiUlPktsDropped.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiUlPktsDropped.setDescription('Total number of dropped uplink user payload packets that should have been sent over the SGi interface.')
rbnEpsuSgiApn = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5))
rbnEpsuSgiApnStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1), )
if mibBuilder.loadTexts: rbnEpsuSgiApnStatsTable.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnStatsTable.setDescription('This table contains the user payload packet counters per Access Point Name (APN).')
rbnEpsuSgiApnStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1), ).setIndexNames((0, "RBN-EPSU-MIB", "rbnEpsuSgiApnIndex"))
if mibBuilder.loadTexts: rbnEpsuSgiApnStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnStatsEntry.setDescription('The user payload packet counters for an APN.')
rbnEpsuSgiApnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rbnEpsuSgiApnIndex.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnIndex.setDescription('An integer value assigned to uniquely identify the entry.')
rbnEpsuSgiApnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnName.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnName.setDescription('The access point name (APN) associated with rbnEpsuSgiApnIndex.')
rbnEpsuSgiApnDlPktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 3), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnDlPktsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnDlPktsRcvd.setDescription('Total number of downlink user payload packets received over the SGi interface for the APN.')
rbnEpsuSgiApnDlOctetsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 4), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnDlOctetsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnDlOctetsRcvd.setDescription('Total number of octets in downlink user payload packets received over the SGi interface for the APN.')
rbnEpsuSgiApnDlPktsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 5), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnDlPktsDiscarded.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnDlPktsDiscarded.setDescription('Total number of discarded downlink user payload packets received over the SGi interface for the APN.')
rbnEpsuSgiApnUlPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 6), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnUlPktsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnUlPktsSent.setDescription('Total number of uplink user payload packets sent over the SGi interface for the APN.')
rbnEpsuSgiApnUlOctetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 7), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnUlOctetsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnUlOctetsSent.setDescription('Total number of octets in uplink user payload packets sent over the SGi interface for the APN.')
rbnEpsuSgiApnUlPktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 8), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnUlPktsDropped.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnUlPktsDropped.setDescription('Total number of dropped uplink payload GTP packets that should have been sent over the SGi interface for the APN.')
rbnEpsuSgiApnDlV6PktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 9), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnDlV6PktsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnDlV6PktsRcvd.setDescription('Total number of downlink IPv6 user payload packets received over the SGi interface for the APN.')
rbnEpsuSgiApnDlV6OctetsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 10), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnDlV6OctetsRcvd.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnDlV6OctetsRcvd.setDescription('Total number of octets in downlink IPv6 user payload packets received over the SGi interface for the APN.')
rbnEpsuSgiApnUlV6PktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 11), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnUlV6PktsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnUlV6PktsSent.setDescription('Total number of uplink IPv6 user payload packets sent over the SGi interface for the APN.')
rbnEpsuSgiApnUlV6OctetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 12), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEpsuSgiApnUlV6OctetsSent.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiApnUlV6OctetsSent.setDescription('Total number of octets in uplink IPv6 user payload packets sent over the SGi interface for the APN.')
rbnEpsuNotifcationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 0))
rbnEpsuMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 2))
rbnEpsuMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1))
rbnEpsuMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 2))
rbnEpsuS1uGtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 1)).setObjects(("RBN-EPSU-MIB", "rbnEpsuS1uDlPktsSent"), ("RBN-EPSU-MIB", "rbnEpsuS1uDlOctetsSent"), ("RBN-EPSU-MIB", "rbnEpsuS1uDlPktsDropped"), ("RBN-EPSU-MIB", "rbnEpsuS1uDlPolicingPktsDropped"), ("RBN-EPSU-MIB", "rbnEpsuS1uDlUeIdlePktsDropped"), ("RBN-EPSU-MIB", "rbnEpsuS1uUlPktsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuS1uUlOctetsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuS1uUlPktsDiscarded"), ("RBN-EPSU-MIB", "rbnEpsuS1uUlBearerPktsDiscarded"), ("RBN-EPSU-MIB", "rbnEpsuS1uUlPolicingPktsDiscarded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEpsuS1uGtpGroup = rbnEpsuS1uGtpGroup.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuS1uGtpGroup.setDescription('This object group contains counters for GTP on the S1-U interface')
rbnEpsuSgwGtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 2)).setObjects(("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPktsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlOctetsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPktsDiscarded"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPktsSent"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlOctetsSent"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPktsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEpsuSgwGtpGroup = rbnEpsuSgwGtpGroup.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgwGtpGroup.setDescription('This object group contains counters for GTP on the S5/S8 SGW inteface ')
rbnEpsuPgwGtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 3)).setObjects(("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPktsSent"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlOctetsSent"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPktsDropped"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPolicingPktsDropped"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPktsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlOctetsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPktsDiscarded"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlBearerPktsDiscarded"), ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPolicingPktsDiscarded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEpsuPgwGtpGroup = rbnEpsuPgwGtpGroup.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuPgwGtpGroup.setDescription('This object group contains counters for GTP on the S5/S8 PGW inteface')
rbnEpsuSgiGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 4)).setObjects(("RBN-EPSU-MIB", "rbnEpsuSgiDlPktsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuSgiDlOctetsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuSgiDlV6PktsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuSgiDlV6OctetsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuSgiDlPktsDiscarded"), ("RBN-EPSU-MIB", "rbnEpsuSgiUlPktsSent"), ("RBN-EPSU-MIB", "rbnEpsuSgiUlOctetsSent"), ("RBN-EPSU-MIB", "rbnEpsuSgiUlPktsDropped"), ("RBN-EPSU-MIB", "rbnEpsuSgiUlV6PktsSent"), ("RBN-EPSU-MIB", "rbnEpsuSgiUlV6OctetsSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEpsuSgiGroup = rbnEpsuSgiGroup.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuSgiGroup.setDescription('This object group contains counters for SGi inteface.')
rbnEspuSgiApnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 5)).setObjects(("RBN-EPSU-MIB", "rbnEpsuSgiApnName"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlPktsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlOctetsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlV6PktsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlV6OctetsRcvd"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlPktsDiscarded"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlPktsSent"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlOctetsSent"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlV6PktsSent"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlV6OctetsSent"), ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlPktsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEspuSgiApnGroup = rbnEspuSgiApnGroup.setStatus('current')
if mibBuilder.loadTexts: rbnEspuSgiApnGroup.setDescription('This object group contains counters for user payload packets per APN received on the SGi interface')
rbnEpsuMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 2, 1)).setObjects(("RBN-EPSU-MIB", "rbnEpsuS1uGtpGroup"), ("RBN-EPSU-MIB", "rbnEpsuSgwGtpGroup"), ("RBN-EPSU-MIB", "rbnEpsuPgwGtpGroup"), ("RBN-EPSU-MIB", "rbnEpsuSgiGroup"), ("RBN-EPSU-MIB", "rbnEspuSgiApnGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEpsuMIBCompliance = rbnEpsuMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnEpsuMIBCompliance.setDescription('The compliance statement for SNMP entities which support EPSU statistics')
mibBuilder.exportSymbols("RBN-EPSU-MIB", rbnEpsuMIBCompliance=rbnEpsuMIBCompliance, rbnEpsuS1uUlPolicingPktsDiscarded=rbnEpsuS1uUlPolicingPktsDiscarded, rbnEpsuS5S8GtpDlPktsRcvd=rbnEpsuS5S8GtpDlPktsRcvd, rbnEpsuS5S8GtpDlOctetsSent=rbnEpsuS5S8GtpDlOctetsSent, rbnEpsuS5S8GtpDlPktsDropped=rbnEpsuS5S8GtpDlPktsDropped, rbnEpsuSgiApnUlPktsSent=rbnEpsuSgiApnUlPktsSent, rbnEpsuS1uDlPolicingPktsDropped=rbnEpsuS1uDlPolicingPktsDropped, rbnEpsuSgiApnStatsEntry=rbnEpsuSgiApnStatsEntry, rbnEpsuPgwGtp=rbnEpsuPgwGtp, rbnEpsuSgiUlOctetsSent=rbnEpsuSgiUlOctetsSent, rbnEpsuStatMIBObjects=rbnEpsuStatMIBObjects, rbnEpsuSgiUlV6OctetsSent=rbnEpsuSgiUlV6OctetsSent, rbnEspuSgiApnGroup=rbnEspuSgiApnGroup, PYSNMP_MODULE_ID=rbnEpsuMIB, rbnEpsuS5S8GtpUlOctetsSent=rbnEpsuS5S8GtpUlOctetsSent, rbnEpsuSgiDlV6PktsRcvd=rbnEpsuSgiDlV6PktsRcvd, rbnEpsuSgiDlV6OctetsRcvd=rbnEpsuSgiDlV6OctetsRcvd, rbnEpsuSgiUlV6PktsSent=rbnEpsuSgiUlV6PktsSent, rbnEpsuSgiApnDlV6PktsRcvd=rbnEpsuSgiApnDlV6PktsRcvd, rbnEpsuMIBCompliances=rbnEpsuMIBCompliances, rbnEpsuS1uUlOctetsRcvd=rbnEpsuS1uUlOctetsRcvd, rbnEpsuS1uGtp=rbnEpsuS1uGtp, rbnEpsuSgiApnUlPktsDropped=rbnEpsuSgiApnUlPktsDropped, rbnEpsuS5S8GtpUlOctetsRcvd=rbnEpsuS5S8GtpUlOctetsRcvd, rbnEpsuS1uDlOctetsSent=rbnEpsuS1uDlOctetsSent, rbnEpsuMIB=rbnEpsuMIB, rbnEpsuS5S8GtpUlPolicingPktsDiscarded=rbnEpsuS5S8GtpUlPolicingPktsDiscarded, rbnEpsuSgi=rbnEpsuSgi, rbnEpsuSgiDlOctetsRcvd=rbnEpsuSgiDlOctetsRcvd, rbnEpsuS1uUlPktsRcvd=rbnEpsuS1uUlPktsRcvd, rbnEpsuS1uDlPktsDropped=rbnEpsuS1uDlPktsDropped, rbnEpsuSgiApnIndex=rbnEpsuSgiApnIndex, rbnEpsuSgiApnDlPktsDiscarded=rbnEpsuSgiApnDlPktsDiscarded, rbnEpsuSgiApnUlV6PktsSent=rbnEpsuSgiApnUlV6PktsSent, rbnEpsuSgwGtpGroup=rbnEpsuSgwGtpGroup, rbnEpsuS5S8GtpUlPktsDiscarded=rbnEpsuS5S8GtpUlPktsDiscarded, rbnEpsuMIBGroups=rbnEpsuMIBGroups, rbnEpsuS5S8GtpUlPktsRcvd=rbnEpsuS5S8GtpUlPktsRcvd, rbnEpsuSgiDlPktsDiscarded=rbnEpsuSgiDlPktsDiscarded, rbnEpsuSgiApnDlPktsRcvd=rbnEpsuSgiApnDlPktsRcvd, rbnEpsuSgiApn=rbnEpsuSgiApn, rbnEpsuS5S8GtpDlPktsDiscarded=rbnEpsuS5S8GtpDlPktsDiscarded, rbnEpsuSgiUlPktsDropped=rbnEpsuSgiUlPktsDropped, rbnEpsuS1uUlPktsDiscarded=rbnEpsuS1uUlPktsDiscarded, rbnEpsuS5S8GtpDlPktsSent=rbnEpsuS5S8GtpDlPktsSent, rbnEpsuS1uUlBearerPktsDiscarded=rbnEpsuS1uUlBearerPktsDiscarded, rbnEpsuS1uDlPktsSent=rbnEpsuS1uDlPktsSent, rbnEpsuS5S8GtpUlBearerPktsDiscarded=rbnEpsuS5S8GtpUlBearerPktsDiscarded, rbnEpsuPgwGtpGroup=rbnEpsuPgwGtpGroup, rbnEpsuSgiApnUlOctetsSent=rbnEpsuSgiApnUlOctetsSent, rbnEpsuS5S8GtpDlOctetsRcvd=rbnEpsuS5S8GtpDlOctetsRcvd, rbnEpsuSgiApnUlV6OctetsSent=rbnEpsuSgiApnUlV6OctetsSent, rbnEpsuMIBConformance=rbnEpsuMIBConformance, rbnEpsuSgiApnDlV6OctetsRcvd=rbnEpsuSgiApnDlV6OctetsRcvd, rbnEpsuS5S8GtpDlPolicingPktsDropped=rbnEpsuS5S8GtpDlPolicingPktsDropped, rbnEpsuSgiApnStatsTable=rbnEpsuSgiApnStatsTable, rbnEpsuNotifcationGroup=rbnEpsuNotifcationGroup, rbnEpsuS1uGtpGroup=rbnEpsuS1uGtpGroup, rbnEpsuSgiApnName=rbnEpsuSgiApnName, rbnEpsuS1uDlUeIdlePktsDropped=rbnEpsuS1uDlUeIdlePktsDropped, rbnEpsuS5S8GtpUlPktsSent=rbnEpsuS5S8GtpUlPktsSent, rbnEpsuSgiDlPktsRcvd=rbnEpsuSgiDlPktsRcvd, rbnEpsuSgiGroup=rbnEpsuSgiGroup, rbnEpsuS5S8GtpUlPktsDropped=rbnEpsuS5S8GtpUlPktsDropped, rbnEpsuSgiUlPktsSent=rbnEpsuSgiUlPktsSent, rbnEpsuSgiApnDlOctetsRcvd=rbnEpsuSgiApnDlOctetsRcvd, rbnEpsuSgwGtp=rbnEpsuSgwGtp)

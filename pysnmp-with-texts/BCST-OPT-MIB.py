#
# PySNMP MIB module BCST-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BCST-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, Unsigned32, ObjectIdentity, Integer32, NotificationType, Counter64, iso, ModuleIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Unsigned32", "ObjectIdentity", "Integer32", "NotificationType", "Counter64", "iso", "ModuleIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2))
class DisplayString(OctetString):
    pass

cdx6500GCTSVCBroadcastTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10), )
if mibBuilder.loadTexts: cdx6500GCTSVCBroadcastTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500GCTSVCBroadcastTable.setDescription('A list of Broadcast SBCO configuration entries.')
cdx6500bcstSBCOcfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1), ).setIndexNames((0, "BCST-OPT-MIB", "cdx6500bcstSBCOnum"))
if mibBuilder.loadTexts: cdx6500bcstSBCOcfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstSBCOcfgEntry.setDescription('The entries for the Broadcast SBCO table.')
cdx6500bcstSBCOnum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstSBCOnum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstSBCOnum.setDescription('Index for the Broadcast SBCO configuration table.')
cdx6500bcstSBCOnet = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstSBCOnet.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstSBCOnet.setDescription('The main channel subaddress of the Broadcast, BCST.')
cdx6500bcstSBCOcalledAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstSBCOcalledAddr.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstSBCOcalledAddr.setDescription('Call packets containing this called address will enable broadcast traffic for this net.')
cdx6500bcstSBCOcallingAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstSBCOcallingAddr.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstSBCOcallingAddr.setDescription('Call packets containing this calling address will enable broadcast traffic for this net.')
cdx6500bcstSBCOfacilities = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstSBCOfacilities.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstSBCOfacilities.setDescription('Call packets containing the facility bytes shown will enable broadcast traffic for this net.')
cdx6500bcstSBCOuserData = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstSBCOuserData.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstSBCOuserData.setDescription('Call packets containing the user data bytes shown will enable broadcast traffic for this net.')
cdx6500bcstSBCOdirection = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("called", 2), ("calling", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstSBCOdirection.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstSBCOdirection.setDescription('This specifies the direction in which broadcast traffic will be sent. Select options on this broadcast net as follows: none - no option specified called - send traffic towards the called address calling - send traffic towards the calling address Any combination of above specified by summing (e.g. called + calling).')
cdx6500bcstSBCOdestination = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("user", 1), ("bctp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstSBCOdestination.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstSBCOdestination.setDescription('This specifies who the destination is and what will happen to the broadcast message. Select options on this broadcast net as follows: user - end user to receive broadcast; implies stripping of the net identification byte. bctp - broadcast input port on adjacent node; net identification byte is not stripped.')
cdx6500GCTPVCBroadcastOutTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11), )
if mibBuilder.loadTexts: cdx6500GCTPVCBroadcastOutTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500GCTPVCBroadcastOutTable.setDescription('A list of BCST PBCO configuration entries.')
cdx6500bcstPBCOcfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1), ).setIndexNames((0, "BCST-OPT-MIB", "cdx6500bcstPBCOnum"))
if mibBuilder.loadTexts: cdx6500bcstPBCOcfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstPBCOcfgEntry.setDescription('The entries of cdx6500GCTPVCBroadcastOutTable')
cdx6500bcstPBCOnum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstPBCOnum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstPBCOnum.setDescription('Index for the BCST PBCO table.')
cdx6500bcstPBCOnet = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstPBCOnet.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstPBCOnet.setDescription('The configuration which follows will trigger broadcast traffic for this broadcast net.')
cdx6500bcstPBCOconnection = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstPBCOconnection.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstPBCOconnection.setDescription('Watch for connections destined to this channel. For example, a connection to port 1, channel 13 is P1(13), or a connection to port 2, station 4, channel 5 is P2S4(5).')
cdx6500bcstPBCOdestination = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 11, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bcstPBCOdestination.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bcstPBCOdestination.setDescription('Watch for connections destined to this channel. For example, a connection to port 1, channel 13 is P1(13), or a connection to port 2, station 4, channel 5 is P2S4(5).')
mibBuilder.exportSymbols("BCST-OPT-MIB", cdx6500bcstSBCOfacilities=cdx6500bcstSBCOfacilities, codex=codex, cdx6500bcstSBCOcalledAddr=cdx6500bcstSBCOcalledAddr, cdx6500bcstSBCOnet=cdx6500bcstSBCOnet, cdxProductSpecific=cdxProductSpecific, cdx6500bcstPBCOconnection=cdx6500bcstPBCOconnection, cdx6500=cdx6500, cdx6500CfgGeneralGroup=cdx6500CfgGeneralGroup, DisplayString=DisplayString, cdx6500bcstSBCOcallingAddr=cdx6500bcstSBCOcallingAddr, cdx6500Configuration=cdx6500Configuration, cdx6500bcstPBCOnum=cdx6500bcstPBCOnum, cdx6500bcstSBCOnum=cdx6500bcstSBCOnum, cdx6500GCTSVCBroadcastTable=cdx6500GCTSVCBroadcastTable, cdx6500bcstSBCOuserData=cdx6500bcstSBCOuserData, cdx6500bcstPBCOnet=cdx6500bcstPBCOnet, cdx6500bcstPBCOdestination=cdx6500bcstPBCOdestination, cdx6500bcstSBCOdestination=cdx6500bcstSBCOdestination, cdx6500GCTPVCBroadcastOutTable=cdx6500GCTPVCBroadcastOutTable, cdx6500bcstSBCOcfgEntry=cdx6500bcstSBCOcfgEntry, cdx6500bcstSBCOdirection=cdx6500bcstSBCOdirection, cdx6500bcstPBCOcfgEntry=cdx6500bcstPBCOcfgEntry)

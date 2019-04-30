#
# PySNMP MIB module Juniper-ERX-Registry (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ERX-Registry
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
juniAdmin, = mibBuilder.importSymbols("Juniper-Registry", "juniAdmin")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, NotificationType, TimeTicks, IpAddress, MibIdentifier, Gauge32, Unsigned32, Integer32, Counter32, iso, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "NotificationType", "TimeTicks", "IpAddress", "MibIdentifier", "Gauge32", "Unsigned32", "Integer32", "Counter32", "iso", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniErxRegistry = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2))
juniErxRegistry.setRevisions(('2006-07-22 05:43', '2006-06-23 16:07', '2006-04-03 10:43', '2006-05-02 14:53', '2006-04-12 13:05', '2006-03-31 13:12', '2006-02-28 08:22', '2005-09-21 15:48', '2004-05-25 18:32', '2003-11-12 20:20', '2003-11-12 19:30', '2003-07-17 21:07', '2002-10-21 15:00', '2002-10-16 18:50', '2002-10-10 18:51', '2002-05-08 12:34', '2002-05-07 14:05', '2001-08-20 16:08', '2001-06-12 18:27', '2001-06-04 20:11',))
if mibBuilder.loadTexts: juniErxRegistry.setLastUpdated('200607220543Z')
if mibBuilder.loadTexts: juniErxRegistry.setOrganization('Juniper Networks, Inc.')
juniErxEntPhysicalType = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1))
erxChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1))
if mibBuilder.loadTexts: erxChassis.setStatus('current')
erx700Chassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1, 1))
if mibBuilder.loadTexts: erx700Chassis.setStatus('current')
erx1400Chassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1, 2))
if mibBuilder.loadTexts: erx1400Chassis.setStatus('current')
erx1440Chassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1, 3))
if mibBuilder.loadTexts: erx1440Chassis.setStatus('current')
erx310ACChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1, 4))
if mibBuilder.loadTexts: erx310ACChassis.setStatus('current')
erx310DCChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1, 5))
if mibBuilder.loadTexts: erx310DCChassis.setStatus('current')
erxFanAssembly = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2))
if mibBuilder.loadTexts: erxFanAssembly.setStatus('current')
erx700FanAssembly = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2, 1))
if mibBuilder.loadTexts: erx700FanAssembly.setStatus('current')
erx1400FanAssembly = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2, 2))
if mibBuilder.loadTexts: erx1400FanAssembly.setStatus('current')
erx300FanAssembly = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2, 3))
if mibBuilder.loadTexts: erx300FanAssembly.setStatus('current')
erxPowerInput = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 3))
if mibBuilder.loadTexts: erxPowerInput.setStatus('current')
erxPdu = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 3, 1))
if mibBuilder.loadTexts: erxPdu.setStatus('current')
erx1440Pdu = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 3, 2))
if mibBuilder.loadTexts: erx1440Pdu.setStatus('current')
erx300ACPdu = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 3, 3))
if mibBuilder.loadTexts: erx300ACPdu.setStatus('current')
erx300DCPdu = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 3, 4))
if mibBuilder.loadTexts: erx300DCPdu.setStatus('current')
erxMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4))
if mibBuilder.loadTexts: erxMidplane.setStatus('current')
erx700Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 1))
if mibBuilder.loadTexts: erx700Midplane.setStatus('current')
erx1400Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 2))
if mibBuilder.loadTexts: erx1400Midplane.setStatus('current')
erx1Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 3))
if mibBuilder.loadTexts: erx1Plus1RedundantT1E1Midplane.setStatus('deprecated')
erx2Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 4))
if mibBuilder.loadTexts: erx2Plus1RedundantT1E1Midplane.setStatus('current')
erx3Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 5))
if mibBuilder.loadTexts: erx3Plus1RedundantT1E1Midplane.setStatus('current')
erx4Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 6))
if mibBuilder.loadTexts: erx4Plus1RedundantT1E1Midplane.setStatus('current')
erx5Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 7))
if mibBuilder.loadTexts: erx5Plus1RedundantT1E1Midplane.setStatus('current')
erx1Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 8))
if mibBuilder.loadTexts: erx1Plus1RedundantT3E3Midplane.setStatus('deprecated')
erx2Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 9))
if mibBuilder.loadTexts: erx2Plus1RedundantT3E3Midplane.setStatus('current')
erx3Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 10))
if mibBuilder.loadTexts: erx3Plus1RedundantT3E3Midplane.setStatus('current')
erx4Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 11))
if mibBuilder.loadTexts: erx4Plus1RedundantT3E3Midplane.setStatus('current')
erx5Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 12))
if mibBuilder.loadTexts: erx5Plus1RedundantT3E3Midplane.setStatus('current')
erx1Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 13))
if mibBuilder.loadTexts: erx1Plus1RedundantOcMidplane.setStatus('deprecated')
erx2Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 14))
if mibBuilder.loadTexts: erx2Plus1RedundantOcMidplane.setStatus('current')
erx3Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 15))
if mibBuilder.loadTexts: erx3Plus1RedundantOcMidplane.setStatus('deprecated')
erx4Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 16))
if mibBuilder.loadTexts: erx4Plus1RedundantOcMidplane.setStatus('deprecated')
erx5Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 17))
if mibBuilder.loadTexts: erx5Plus1RedundantOcMidplane.setStatus('current')
erx2Plus1Redundant12T3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 18))
if mibBuilder.loadTexts: erx2Plus1Redundant12T3E3Midplane.setStatus('current')
erx5Plus1Redundant12T3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 19))
if mibBuilder.loadTexts: erx5Plus1Redundant12T3E3Midplane.setStatus('current')
erx1440Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 20))
if mibBuilder.loadTexts: erx1440Midplane.setStatus('current')
erx300Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 21))
if mibBuilder.loadTexts: erx300Midplane.setStatus('current')
erx2Plus1RedundantCOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 22))
if mibBuilder.loadTexts: erx2Plus1RedundantCOcMidplane.setStatus('current')
erx5Plus1RedundantCOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 23))
if mibBuilder.loadTexts: erx5Plus1RedundantCOcMidplane.setStatus('current')
erxSrpModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5))
if mibBuilder.loadTexts: erxSrpModule.setStatus('current')
erxSrp5 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 1))
if mibBuilder.loadTexts: erxSrp5.setStatus('obsolete')
erxSrp10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 2))
if mibBuilder.loadTexts: erxSrp10.setStatus('deprecated')
erxSrp10Ecc = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 3))
if mibBuilder.loadTexts: erxSrp10Ecc.setStatus('current')
erxSrp40 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 4))
if mibBuilder.loadTexts: erxSrp40.setStatus('obsolete')
erxSrp5Plus = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 5))
if mibBuilder.loadTexts: erxSrp5Plus.setStatus('obsolete')
erxSrp40Plus = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 6))
if mibBuilder.loadTexts: erxSrp40Plus.setStatus('obsolete')
erxSrp310 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 7))
if mibBuilder.loadTexts: erxSrp310.setStatus('deprecated')
erxSrp40g2gEc2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 8))
if mibBuilder.loadTexts: erxSrp40g2gEc2.setStatus('current')
erxSrp10g1gEcc = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 9))
if mibBuilder.loadTexts: erxSrp10g1gEcc.setStatus('current')
erxSrp10g2gEcc = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 10))
if mibBuilder.loadTexts: erxSrp10g2gEcc.setStatus('current')
erxSrp5g1gEcc = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 11))
if mibBuilder.loadTexts: erxSrp5g1gEcc.setStatus('deprecated')
erxSrp5g2gEcc = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 12))
if mibBuilder.loadTexts: erxSrp5g2gEcc.setStatus('deprecated')
erxSrpIoAdapter = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 6))
if mibBuilder.loadTexts: erxSrpIoAdapter.setStatus('current')
erxSrpIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 6, 1))
if mibBuilder.loadTexts: erxSrpIoa.setStatus('current')
erxSrp310Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 6, 2))
if mibBuilder.loadTexts: erxSrp310Ioa.setStatus('current')
erxLineModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7))
if mibBuilder.loadTexts: erxLineModule.setStatus('current')
erxCt1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 1))
if mibBuilder.loadTexts: erxCt1.setStatus('obsolete')
erxCe1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 2))
if mibBuilder.loadTexts: erxCe1.setStatus('obsolete')
erxCt3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 4))
if mibBuilder.loadTexts: erxCt3.setStatus('obsolete')
erxT3Atm = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 5))
if mibBuilder.loadTexts: erxT3Atm.setStatus('obsolete')
erxT3Frame = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 6))
if mibBuilder.loadTexts: erxT3Frame.setStatus('obsolete')
erxE3Atm = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 7))
if mibBuilder.loadTexts: erxE3Atm.setStatus('obsolete')
erxE3Frame = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 8))
if mibBuilder.loadTexts: erxE3Frame.setStatus('obsolete')
erxOc3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 9))
if mibBuilder.loadTexts: erxOc3.setStatus('deprecated')
erxOc3Oc12Atm = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 10))
if mibBuilder.loadTexts: erxOc3Oc12Atm.setStatus('current')
erxOc3Oc12Pos = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 11))
if mibBuilder.loadTexts: erxOc3Oc12Pos.setStatus('current')
erxCOcx = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 12))
if mibBuilder.loadTexts: erxCOcx.setStatus('current')
erxFe2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 13))
if mibBuilder.loadTexts: erxFe2.setStatus('obsolete')
erxGeFe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 14))
if mibBuilder.loadTexts: erxGeFe.setStatus('current')
erxTunnelService = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 15))
if mibBuilder.loadTexts: erxTunnelService.setStatus('current')
erxHssi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 16))
if mibBuilder.loadTexts: erxHssi.setStatus('obsolete')
erxVts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 17))
if mibBuilder.loadTexts: erxVts.setStatus('current')
erxCt3P12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 18))
if mibBuilder.loadTexts: erxCt3P12.setStatus('current')
erxV35 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 19))
if mibBuilder.loadTexts: erxV35.setStatus('obsolete')
erxUt3E3Ocx = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 20))
if mibBuilder.loadTexts: erxUt3E3Ocx.setStatus('current')
erxOc48 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 21))
if mibBuilder.loadTexts: erxOc48.setStatus('current')
erxOc3Oc12Atm256M = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 22))
if mibBuilder.loadTexts: erxOc3Oc12Atm256M.setStatus('current')
erxGeFe256M = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 23))
if mibBuilder.loadTexts: erxGeFe256M.setStatus('current')
erxService = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 24))
if mibBuilder.loadTexts: erxService.setStatus('current')
erxOc3Hybrid = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 25))
if mibBuilder.loadTexts: erxOc3Hybrid.setStatus('current')
erxGe2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 26))
if mibBuilder.loadTexts: erxGe2.setStatus('current')
erxLineIoAdapter = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8))
if mibBuilder.loadTexts: erxLineIoAdapter.setStatus('current')
erxCt1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 1))
if mibBuilder.loadTexts: erxCt1Ioa.setStatus('obsolete')
erxCe1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 2))
if mibBuilder.loadTexts: erxCe1Ioa.setStatus('obsolete')
erxCe1TIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 3))
if mibBuilder.loadTexts: erxCe1TIoa.setStatus('obsolete')
erxCt3Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 4))
if mibBuilder.loadTexts: erxCt3Ioa.setStatus('obsolete')
erxE3Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 5))
if mibBuilder.loadTexts: erxE3Ioa.setStatus('current')
erxOc3Mm2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 6))
if mibBuilder.loadTexts: erxOc3Mm2Ioa.setStatus('deprecated')
erxOc3Sm2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 7))
if mibBuilder.loadTexts: erxOc3Sm2Ioa.setStatus('deprecated')
erxOc3Mm4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 8))
if mibBuilder.loadTexts: erxOc3Mm4Ioa.setStatus('current')
erxOc3SmIr4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 9))
if mibBuilder.loadTexts: erxOc3SmIr4Ioa.setStatus('current')
erxOc3SmLr4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 10))
if mibBuilder.loadTexts: erxOc3SmLr4Ioa.setStatus('current')
erxCOc3Mm4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 11))
if mibBuilder.loadTexts: erxCOc3Mm4Ioa.setStatus('current')
erxCOc3SmIr4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 12))
if mibBuilder.loadTexts: erxCOc3SmIr4Ioa.setStatus('current')
erxCOc3SmLr4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 13))
if mibBuilder.loadTexts: erxCOc3SmLr4Ioa.setStatus('current')
erxOc12Mm1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 14))
if mibBuilder.loadTexts: erxOc12Mm1Ioa.setStatus('current')
erxOc12SmIr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 15))
if mibBuilder.loadTexts: erxOc12SmIr1Ioa.setStatus('current')
erxOc12SmLr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 16))
if mibBuilder.loadTexts: erxOc12SmLr1Ioa.setStatus('current')
erxCOc12Mm1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 17))
if mibBuilder.loadTexts: erxCOc12Mm1Ioa.setStatus('current')
erxCOc12SmIr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 18))
if mibBuilder.loadTexts: erxCOc12SmIr1Ioa.setStatus('current')
erxCOc12SmLr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 19))
if mibBuilder.loadTexts: erxCOc12SmLr1Ioa.setStatus('current')
erxFe2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 20))
if mibBuilder.loadTexts: erxFe2Ioa.setStatus('obsolete')
erxFe8Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 21))
if mibBuilder.loadTexts: erxFe8Ioa.setStatus('current')
erxGeMm1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 22))
if mibBuilder.loadTexts: erxGeMm1Ioa.setStatus('deprecated')
erxGeSm1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 23))
if mibBuilder.loadTexts: erxGeSm1Ioa.setStatus('deprecated')
erxHssiIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 24))
if mibBuilder.loadTexts: erxHssiIoa.setStatus('obsolete')
erxCt3P12Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 25))
if mibBuilder.loadTexts: erxCt3P12Ioa.setStatus('current')
erxV35Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 26))
if mibBuilder.loadTexts: erxV35Ioa.setStatus('obsolete')
erxGeSfpIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 27))
if mibBuilder.loadTexts: erxGeSfpIoa.setStatus('current')
erxUe3P12Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 28))
if mibBuilder.loadTexts: erxUe3P12Ioa.setStatus('current')
erxT3Atm4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 29))
if mibBuilder.loadTexts: erxT3Atm4Ioa.setStatus('current')
erxCOc12Mm1ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 30))
if mibBuilder.loadTexts: erxCOc12Mm1ApsIoa.setStatus('current')
erxCOc12SmIr1ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 31))
if mibBuilder.loadTexts: erxCOc12SmIr1ApsIoa.setStatus('current')
erxCOc12SmLr1ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 32))
if mibBuilder.loadTexts: erxCOc12SmLr1ApsIoa.setStatus('current')
erxOc12Mm1ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 33))
if mibBuilder.loadTexts: erxOc12Mm1ApsIoa.setStatus('current')
erxOc12SmIr1ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 34))
if mibBuilder.loadTexts: erxOc12SmIr1ApsIoa.setStatus('current')
erxOc12SmLr1ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 35))
if mibBuilder.loadTexts: erxOc12SmLr1ApsIoa.setStatus('current')
erxCOc12AtmPosMm1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 36))
if mibBuilder.loadTexts: erxCOc12AtmPosMm1Ioa.setStatus('current')
erxCOc12AtmPosSmIr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 37))
if mibBuilder.loadTexts: erxCOc12AtmPosSmIr1Ioa.setStatus('current')
erxCOc12AtmPosSmLr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 38))
if mibBuilder.loadTexts: erxCOc12AtmPosSmLr1Ioa.setStatus('current')
erxCOc12AtmPosMm1ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 39))
if mibBuilder.loadTexts: erxCOc12AtmPosMm1ApsIoa.setStatus('current')
erxCOc12AtmPosSmIr1ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 40))
if mibBuilder.loadTexts: erxCOc12AtmPosSmIr1ApsIoa.setStatus('current')
erxCOc12AtmPosSmLr1ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 41))
if mibBuilder.loadTexts: erxCOc12AtmPosSmLr1ApsIoa.setStatus('current')
erxT1E1RedundantIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 42))
if mibBuilder.loadTexts: erxT1E1RedundantIoa.setStatus('current')
erxT3E3RedundantIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 43))
if mibBuilder.loadTexts: erxT3E3RedundantIoa.setStatus('current')
erxCt3RedundantIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 44))
if mibBuilder.loadTexts: erxCt3RedundantIoa.setStatus('current')
erxOcxRedundantIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 45))
if mibBuilder.loadTexts: erxOcxRedundantIoa.setStatus('current')
erxCOcxRedundantIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 46))
if mibBuilder.loadTexts: erxCOcxRedundantIoa.setStatus('current')
erxOc3Mm4ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 47))
if mibBuilder.loadTexts: erxOc3Mm4ApsIoa.setStatus('current')
erxOc3SmIr4ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 48))
if mibBuilder.loadTexts: erxOc3SmIr4ApsIoa.setStatus('current')
erxOc3SmLr4ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 49))
if mibBuilder.loadTexts: erxOc3SmLr4ApsIoa.setStatus('current')
erxOc48Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 50))
if mibBuilder.loadTexts: erxOc48Ioa.setStatus('current')
erxOc3Atm2Ge1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 51))
if mibBuilder.loadTexts: erxOc3Atm2Ge1Ioa.setStatus('current')
erxOc3Atm2Pos2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 52))
if mibBuilder.loadTexts: erxOc3Atm2Pos2Ioa.setStatus('current')
erxGe2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 53))
if mibBuilder.loadTexts: erxGe2Ioa.setStatus('current')
erxFe8FxIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 54))
if mibBuilder.loadTexts: erxFe8FxIoa.setStatus('current')
mibBuilder.exportSymbols("Juniper-ERX-Registry", erxOc12SmLr1Ioa=erxOc12SmLr1Ioa, erxCOc12SmIr1ApsIoa=erxCOc12SmIr1ApsIoa, erx1440Chassis=erx1440Chassis, erxSrp10=erxSrp10, erxV35Ioa=erxV35Ioa, erx5Plus1RedundantOcMidplane=erx5Plus1RedundantOcMidplane, erx5Plus1RedundantCOcMidplane=erx5Plus1RedundantCOcMidplane, erxFe2Ioa=erxFe2Ioa, erx4Plus1RedundantT3E3Midplane=erx4Plus1RedundantT3E3Midplane, erxOc3Hybrid=erxOc3Hybrid, erxFe8FxIoa=erxFe8FxIoa, erxCOc12Mm1Ioa=erxCOc12Mm1Ioa, erxOc3Mm2Ioa=erxOc3Mm2Ioa, erxE3Atm=erxE3Atm, erx1400Midplane=erx1400Midplane, erx5Plus1Redundant12T3E3Midplane=erx5Plus1Redundant12T3E3Midplane, erxCOc12SmLr1Ioa=erxCOc12SmLr1Ioa, erxFe8Ioa=erxFe8Ioa, erxGe2Ioa=erxGe2Ioa, erxPowerInput=erxPowerInput, erxSrp5g2gEcc=erxSrp5g2gEcc, erxSrp310Ioa=erxSrp310Ioa, erxUt3E3Ocx=erxUt3E3Ocx, erx300Midplane=erx300Midplane, erx700Midplane=erx700Midplane, erxOc3SmLr4Ioa=erxOc3SmLr4Ioa, erxCOc3SmLr4Ioa=erxCOc3SmLr4Ioa, erx2Plus1RedundantOcMidplane=erx2Plus1RedundantOcMidplane, erxGeSm1Ioa=erxGeSm1Ioa, erxSrp5=erxSrp5, erxCOc12AtmPosSmLr1ApsIoa=erxCOc12AtmPosSmLr1ApsIoa, erx5Plus1RedundantT1E1Midplane=erx5Plus1RedundantT1E1Midplane, erx300FanAssembly=erx300FanAssembly, erxGe2=erxGe2, erxOc12SmIr1Ioa=erxOc12SmIr1Ioa, erxHssi=erxHssi, erxCOc12Mm1ApsIoa=erxCOc12Mm1ApsIoa, erx700Chassis=erx700Chassis, erx2Plus1RedundantT3E3Midplane=erx2Plus1RedundantT3E3Midplane, erx2Plus1RedundantCOcMidplane=erx2Plus1RedundantCOcMidplane, erx2Plus1RedundantT1E1Midplane=erx2Plus1RedundantT1E1Midplane, erxT1E1RedundantIoa=erxT1E1RedundantIoa, erxVts=erxVts, erxCe1=erxCe1, erxOcxRedundantIoa=erxOcxRedundantIoa, erx2Plus1Redundant12T3E3Midplane=erx2Plus1Redundant12T3E3Midplane, erxCOc12AtmPosSmIr1ApsIoa=erxCOc12AtmPosSmIr1ApsIoa, erxCt1=erxCt1, erxT3Atm4Ioa=erxT3Atm4Ioa, erx700FanAssembly=erx700FanAssembly, erxOc3SmLr4ApsIoa=erxOc3SmLr4ApsIoa, erxCOcx=erxCOcx, erxOc12SmIr1ApsIoa=erxOc12SmIr1ApsIoa, erxGeSfpIoa=erxGeSfpIoa, erxSrp40Plus=erxSrp40Plus, erxT3E3RedundantIoa=erxT3E3RedundantIoa, juniErxRegistry=juniErxRegistry, erxT3Frame=erxT3Frame, erxOc3Oc12Pos=erxOc3Oc12Pos, erx4Plus1RedundantT1E1Midplane=erx4Plus1RedundantT1E1Midplane, erx300ACPdu=erx300ACPdu, erxOc48Ioa=erxOc48Ioa, erxOc3Oc12Atm256M=erxOc3Oc12Atm256M, erx3Plus1RedundantT3E3Midplane=erx3Plus1RedundantT3E3Midplane, erxLineModule=erxLineModule, erxCt3RedundantIoa=erxCt3RedundantIoa, erxSrp40=erxSrp40, erxSrp40g2gEc2=erxSrp40g2gEc2, erxFanAssembly=erxFanAssembly, erxOc48=erxOc48, erxCOc3Mm4Ioa=erxCOc3Mm4Ioa, erxHssiIoa=erxHssiIoa, erxMidplane=erxMidplane, erxOc3Oc12Atm=erxOc3Oc12Atm, juniErxEntPhysicalType=juniErxEntPhysicalType, erxFe2=erxFe2, erxGeMm1Ioa=erxGeMm1Ioa, erxCt3P12Ioa=erxCt3P12Ioa, erxOc3Mm4Ioa=erxOc3Mm4Ioa, erxCOc3SmIr4Ioa=erxCOc3SmIr4Ioa, erxCt3=erxCt3, erxCe1TIoa=erxCe1TIoa, erxCOc12SmLr1ApsIoa=erxCOc12SmLr1ApsIoa, erxTunnelService=erxTunnelService, erxCe1Ioa=erxCe1Ioa, erx300DCPdu=erx300DCPdu, erxOc3Sm2Ioa=erxOc3Sm2Ioa, erxOc3Mm4ApsIoa=erxOc3Mm4ApsIoa, erxCOcxRedundantIoa=erxCOcxRedundantIoa, erx1440Pdu=erx1440Pdu, erx310DCChassis=erx310DCChassis, erxLineIoAdapter=erxLineIoAdapter, erxOc12Mm1ApsIoa=erxOc12Mm1ApsIoa, erxSrp10g2gEcc=erxSrp10g2gEcc, erxCOc12AtmPosMm1Ioa=erxCOc12AtmPosMm1Ioa, erxSrpModule=erxSrpModule, erxCt3Ioa=erxCt3Ioa, erxOc3Atm2Pos2Ioa=erxOc3Atm2Pos2Ioa, erxSrp5g1gEcc=erxSrp5g1gEcc, erx4Plus1RedundantOcMidplane=erx4Plus1RedundantOcMidplane, erxSrp10g1gEcc=erxSrp10g1gEcc, erxCt3P12=erxCt3P12, erxOc12SmLr1ApsIoa=erxOc12SmLr1ApsIoa, erxCOc12AtmPosSmLr1Ioa=erxCOc12AtmPosSmLr1Ioa, erxSrp5Plus=erxSrp5Plus, erxSrp10Ecc=erxSrp10Ecc, erxUe3P12Ioa=erxUe3P12Ioa, erx3Plus1RedundantT1E1Midplane=erx3Plus1RedundantT1E1Midplane, erxGeFe=erxGeFe, erx1Plus1RedundantT3E3Midplane=erx1Plus1RedundantT3E3Midplane, erx1440Midplane=erx1440Midplane, erx1Plus1RedundantT1E1Midplane=erx1Plus1RedundantT1E1Midplane, erxOc3=erxOc3, erxPdu=erxPdu, erx1Plus1RedundantOcMidplane=erx1Plus1RedundantOcMidplane, erxGeFe256M=erxGeFe256M, erxSrpIoAdapter=erxSrpIoAdapter, erx1400FanAssembly=erx1400FanAssembly, erx1400Chassis=erx1400Chassis, erxSrpIoa=erxSrpIoa, erxCOc12SmIr1Ioa=erxCOc12SmIr1Ioa, erx5Plus1RedundantT3E3Midplane=erx5Plus1RedundantT3E3Midplane, erxSrp310=erxSrp310, erxE3Ioa=erxE3Ioa, erxV35=erxV35, erxService=erxService, erxCOc12AtmPosMm1ApsIoa=erxCOc12AtmPosMm1ApsIoa, erx3Plus1RedundantOcMidplane=erx3Plus1RedundantOcMidplane, erx310ACChassis=erx310ACChassis, erxCt1Ioa=erxCt1Ioa, erxCOc12AtmPosSmIr1Ioa=erxCOc12AtmPosSmIr1Ioa, erxOc3Atm2Ge1Ioa=erxOc3Atm2Ge1Ioa, erxOc12Mm1Ioa=erxOc12Mm1Ioa, PYSNMP_MODULE_ID=juniErxRegistry, erxOc3SmIr4Ioa=erxOc3SmIr4Ioa, erxChassis=erxChassis, erxT3Atm=erxT3Atm, erxE3Frame=erxE3Frame, erxOc3SmIr4ApsIoa=erxOc3SmIr4ApsIoa)
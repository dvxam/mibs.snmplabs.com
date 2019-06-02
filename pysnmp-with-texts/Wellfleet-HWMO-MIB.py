#
# PySNMP MIB module Wellfleet-HWMO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-HWMO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, MibIdentifier, NotificationType, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Integer32, Counter64, Unsigned32, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "MibIdentifier", "NotificationType", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Integer32", "Counter64", "Unsigned32", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfHardwareConfig, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfHardwareConfig")
wfMod = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 1, 3))
wfModState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("init", 1))))
if mibBuilder.loadTexts: wfModState.setStatus('mandatory')
if mibBuilder.loadTexts: wfModState.setDescription('State of this record')
wfModSlot = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 2), Integer32())
if mibBuilder.loadTexts: wfModSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfModSlot.setDescription('Instance of this record')
wfModIdOpt = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 3), Integer32())
if mibBuilder.loadTexts: wfModIdOpt.setStatus('mandatory')
if mibBuilder.loadTexts: wfModIdOpt.setDescription('actual module ID and Option')
wfModRev = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 4), Integer32())
if mibBuilder.loadTexts: wfModRev.setStatus('mandatory')
if mibBuilder.loadTexts: wfModRev.setDescription('actual module Revision')
wfModProm = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 5), Integer32())
if mibBuilder.loadTexts: wfModProm.setStatus('mandatory')
if mibBuilder.loadTexts: wfModProm.setDescription('module PROM')
wfModMidr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 6), Integer32())
if mibBuilder.loadTexts: wfModMidr.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMidr.setDescription('module ID register')
wfModMled = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 7), Integer32())
if mibBuilder.loadTexts: wfModMled.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMled.setDescription('module LED register')
wfModMisr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 8), Integer32())
if mibBuilder.loadTexts: wfModMisr.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMisr.setDescription('module MISR register')
wfModSnprom = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 9), Integer32())
if mibBuilder.loadTexts: wfModSnprom.setStatus('mandatory')
if mibBuilder.loadTexts: wfModSnprom.setDescription('module SNPROM')
wfModMadr1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 10), OctetString())
if mibBuilder.loadTexts: wfModMadr1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMadr1.setDescription('SNPROM MAC address connector 1')
wfModMadr2 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 11), OctetString())
if mibBuilder.loadTexts: wfModMadr2.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMadr2.setDescription('SNPROM MAC address connector 2')
wfModMadr3 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 12), OctetString())
if mibBuilder.loadTexts: wfModMadr3.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMadr3.setDescription('SNPROM MAC address connector 3')
wfModMadr4 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 13), OctetString())
if mibBuilder.loadTexts: wfModMadr4.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMadr4.setDescription('SNPROM MAC address connector 4')
wfModLance1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 14), Integer32())
if mibBuilder.loadTexts: wfModLance1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModLance1.setDescription('LANCE line 1')
wfModLance2 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 15), Integer32())
if mibBuilder.loadTexts: wfModLance2.setStatus('mandatory')
if mibBuilder.loadTexts: wfModLance2.setDescription('LANCE line 2')
wfModMk50251 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 16), Integer32())
if mibBuilder.loadTexts: wfModMk50251.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMk50251.setDescription('MK5025 line 1')
wfModMk50252 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 17), Integer32())
if mibBuilder.loadTexts: wfModMk50252.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMk50252.setDescription('MK5025 line 2')
wfModMk50253 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 18), Integer32())
if mibBuilder.loadTexts: wfModMk50253.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMk50253.setDescription('MK5025 line 3')
wfModMk50254 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 19), Integer32())
if mibBuilder.loadTexts: wfModMk50254.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMk50254.setDescription('MK5025 line 4')
wfModSicr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 20), Integer32())
if mibBuilder.loadTexts: wfModSicr.setStatus('mandatory')
if mibBuilder.loadTexts: wfModSicr.setDescription('SYNC interface control register')
wfModSbrr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 21), Integer32())
if mibBuilder.loadTexts: wfModSbrr.setStatus('mandatory')
if mibBuilder.loadTexts: wfModSbrr.setDescription('SYNC baudrate register')
wfMod8530 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 22), Integer32())
if mibBuilder.loadTexts: wfMod8530.setStatus('mandatory')
if mibBuilder.loadTexts: wfMod8530.setDescription('8530 DUART')
wfModCar = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 23), Integer32())
if mibBuilder.loadTexts: wfModCar.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCar.setDescription('CAM assembly register')
wfModDefaA = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 24), Integer32())
if mibBuilder.loadTexts: wfModDefaA.setStatus('mandatory')
if mibBuilder.loadTexts: wfModDefaA.setDescription('DEFA A chip')
wfModCamALock = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 25), Integer32())
if mibBuilder.loadTexts: wfModCamALock.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCamALock.setDescription('CAM A lock')
wfModCamAUnlock = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 26), Integer32())
if mibBuilder.loadTexts: wfModCamAUnlock.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCamAUnlock.setDescription('CAM A unlock')
wfModDefaB = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 27), Integer32())
if mibBuilder.loadTexts: wfModDefaB.setStatus('mandatory')
if mibBuilder.loadTexts: wfModDefaB.setDescription('DEFA B chip')
wfModCamBLock = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 28), Integer32())
if mibBuilder.loadTexts: wfModCamBLock.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCamBLock.setDescription('CAM B lock')
wfModCamBUnlock = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 29), Integer32())
if mibBuilder.loadTexts: wfModCamBUnlock.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCamBUnlock.setDescription('CAM B unlock')
wfModIlacc1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 30), Integer32())
if mibBuilder.loadTexts: wfModIlacc1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModIlacc1.setDescription('ILACC line 1')
wfModIlacc2 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 31), Integer32())
if mibBuilder.loadTexts: wfModIlacc2.setStatus('mandatory')
if mibBuilder.loadTexts: wfModIlacc2.setDescription('ILACC line 2')
wfModIlacc3 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 32), Integer32())
if mibBuilder.loadTexts: wfModIlacc3.setStatus('mandatory')
if mibBuilder.loadTexts: wfModIlacc3.setDescription('ILACC line 3')
wfModIlacc4 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 33), Integer32())
if mibBuilder.loadTexts: wfModIlacc4.setStatus('mandatory')
if mibBuilder.loadTexts: wfModIlacc4.setDescription('ILACC line 4')
wfModTms3801 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 34), Integer32())
if mibBuilder.loadTexts: wfModTms3801.setStatus('mandatory')
if mibBuilder.loadTexts: wfModTms3801.setDescription('TOKEN ring chip line 1')
wfModTms3802 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 35), Integer32())
if mibBuilder.loadTexts: wfModTms3802.setStatus('mandatory')
if mibBuilder.loadTexts: wfModTms3802.setDescription('TOKEN ring chip line 2')
wfModTocr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 36), Integer32())
if mibBuilder.loadTexts: wfModTocr.setStatus('mandatory')
if mibBuilder.loadTexts: wfModTocr.setDescription('TOKEN control register')
wfModTsra = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 37), Integer32())
if mibBuilder.loadTexts: wfModTsra.setStatus('mandatory')
if mibBuilder.loadTexts: wfModTsra.setDescription('TOKEN source route accelerator')
wfModMuxram1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 38), Integer32())
if mibBuilder.loadTexts: wfModMuxram1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMuxram1.setDescription('T1 mux RAM active')
wfModMuxram2 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 39), Integer32())
if mibBuilder.loadTexts: wfModMuxram2.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMuxram2.setDescription('T1 mux RAM inactive')
wfModTicr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 40), Integer32())
if mibBuilder.loadTexts: wfModTicr.setStatus('mandatory')
if mibBuilder.loadTexts: wfModTicr.setDescription('T1 interface control register')
wfModFramer1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 41), Integer32())
if mibBuilder.loadTexts: wfModFramer1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModFramer1.setDescription('T1 framer line 1')
wfModFramer2 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 42), Integer32())
if mibBuilder.loadTexts: wfModFramer2.setStatus('mandatory')
if mibBuilder.loadTexts: wfModFramer2.setDescription('T1 framer line 2')
wfModFsi1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 43), Integer32())
if mibBuilder.loadTexts: wfModFsi1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModFsi1.setDescription('FDDI FSI line 1')
wfModMac1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 44), Integer32())
if mibBuilder.loadTexts: wfModMac1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMac1.setDescription('FDDI MAC line 1')
wfModElmA1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 45), Integer32())
if mibBuilder.loadTexts: wfModElmA1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModElmA1.setDescription('FDDI ELM A line 1')
wfModElmB1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 46), Integer32())
if mibBuilder.loadTexts: wfModElmB1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModElmB1.setDescription('FDDI ELM B line 1')
wfModMcr1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 47), Integer32())
if mibBuilder.loadTexts: wfModMcr1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMcr1.setDescription('FDDI Module control register line 1')
wfModHssiFsi1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 48), Integer32())
if mibBuilder.loadTexts: wfModHssiFsi1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModHssiFsi1.setDescription('HSSI FSI line 1')
wfModHssiFsi2 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 49), Integer32())
if mibBuilder.loadTexts: wfModHssiFsi2.setStatus('mandatory')
if mibBuilder.loadTexts: wfModHssiFsi2.setDescription('HSSI FSI line 2')
wfModHssiUga1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 50), Integer32())
if mibBuilder.loadTexts: wfModHssiUga1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModHssiUga1.setDescription('HSSI UGA-330-2 line 1')
wfModHssiUga2 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 51), Integer32())
if mibBuilder.loadTexts: wfModHssiUga2.setStatus('mandatory')
if mibBuilder.loadTexts: wfModHssiUga2.setDescription('HSSI UGA-330-2 line 2')
wfModHicr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 52), Integer32())
if mibBuilder.loadTexts: wfModHicr.setStatus('mandatory')
if mibBuilder.loadTexts: wfModHicr.setDescription('HSSI Control Register address')
wfModHicrData = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 53), Integer32())
if mibBuilder.loadTexts: wfModHicrData.setStatus('mandatory')
if mibBuilder.loadTexts: wfModHicrData.setDescription('HSSI Last value written to the HICR')
wfModHlsr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 54), Integer32())
if mibBuilder.loadTexts: wfModHlsr.setStatus('mandatory')
if mibBuilder.loadTexts: wfModHlsr.setDescription('HSSI Line Status Register address')
wfModHlsrData = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 55), Integer32())
if mibBuilder.loadTexts: wfModHlsrData.setStatus('mandatory')
if mibBuilder.loadTexts: wfModHlsrData.setDescription('HSSI Last value read from HLSR')
wfModMCR0 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 56), Integer32())
if mibBuilder.loadTexts: wfModMCR0.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMCR0.setDescription('Module Control Register 0')
wfModMCR1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 57), Integer32())
if mibBuilder.loadTexts: wfModMCR1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMCR1.setDescription('Module Control Register 1')
wfModCcr0 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 58), Integer32())
if mibBuilder.loadTexts: wfModCcr0.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCcr0.setDescription('Command Control Register 0')
wfModCcr1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 59), Integer32())
if mibBuilder.loadTexts: wfModCcr1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCcr1.setDescription('Command Control Register 1')
wfModFcr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 60), Integer32())
if mibBuilder.loadTexts: wfModFcr.setStatus('mandatory')
if mibBuilder.loadTexts: wfModFcr.setDescription('Framer Command Register')
wfModMar0 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 61), Integer32())
if mibBuilder.loadTexts: wfModMar0.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMar0.setDescription('Munich action request 0')
wfModMar1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 62), Integer32())
if mibBuilder.loadTexts: wfModMar1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMar1.setDescription('Munich action request 1')
wfModBert = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 63), Integer32())
if mibBuilder.loadTexts: wfModBert.setStatus('mandatory')
if mibBuilder.loadTexts: wfModBert.setDescription('BERT Register')
wfModMgbc = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 64), Integer32())
if mibBuilder.loadTexts: wfModMgbc.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMgbc.setDescription('Module Global bus-error clear')
wfModClr0 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 65), Integer32())
if mibBuilder.loadTexts: wfModClr0.setStatus('mandatory')
if mibBuilder.loadTexts: wfModClr0.setDescription('Clear Munich interrupt 0')
wfModClr1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 66), Integer32())
if mibBuilder.loadTexts: wfModClr1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModClr1.setDescription('Clear Munich interrupt 1')
wfModCclk = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 67), Integer32())
if mibBuilder.loadTexts: wfModCclk.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCclk.setDescription('Clear external clock interrupt')
wfModCLoopup0 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 68), Integer32())
if mibBuilder.loadTexts: wfModCLoopup0.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCLoopup0.setDescription('Clear Port 0 loop up interrupt')
wfModCLoopup1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 69), Integer32())
if mibBuilder.loadTexts: wfModCLoopup1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCLoopup1.setDescription('Clear Port 1 loop up interrupt')
wfModCLoopdn0 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 70), Integer32())
if mibBuilder.loadTexts: wfModCLoopdn0.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCLoopdn0.setDescription('Clear Port 0 loop down interrupt')
wfModCLoopdn1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 71), Integer32())
if mibBuilder.loadTexts: wfModCLoopdn1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCLoopdn1.setDescription('Clear Port 1 loop down interrupt')
wfModDuart = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 72), Integer32())
if mibBuilder.loadTexts: wfModDuart.setStatus('mandatory')
if mibBuilder.loadTexts: wfModDuart.setDescription('8530 DUART')
wfModLEDC = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 73), Integer32())
if mibBuilder.loadTexts: wfModLEDC.setStatus('mandatory')
if mibBuilder.loadTexts: wfModLEDC.setDescription('LED control register')
wfModMadr5 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 74), OctetString())
if mibBuilder.loadTexts: wfModMadr5.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMadr5.setDescription('SNPROM MAC address connector 5 - IN Platform')
wfModDefaC = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 75), Integer32())
if mibBuilder.loadTexts: wfModDefaC.setStatus('mandatory')
if mibBuilder.loadTexts: wfModDefaC.setDescription('DEFA C chip - IN Platform')
wfModCamel1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 76), Integer32())
if mibBuilder.loadTexts: wfModCamel1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModCamel1.setDescription('IFDDI CAMEL line 1')
wfModTms3803 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 77), Integer32())
if mibBuilder.loadTexts: wfModTms3803.setStatus('mandatory')
if mibBuilder.loadTexts: wfModTms3803.setDescription('TOKEN ring chip line 3')
wfModTms3804 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 78), Integer32())
if mibBuilder.loadTexts: wfModTms3804.setStatus('mandatory')
if mibBuilder.loadTexts: wfModTms3804.setDescription('TOKEN ring chip line 4')
wfModMusicSRT1 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 79), Integer32())
if mibBuilder.loadTexts: wfModMusicSRT1.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMusicSRT1.setDescription('Music SRT chip line 1')
wfModMusicSRT2 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 80), Integer32())
if mibBuilder.loadTexts: wfModMusicSRT2.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMusicSRT2.setDescription('Music SRT chip line 2')
wfModMusicSRT3 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 81), Integer32())
if mibBuilder.loadTexts: wfModMusicSRT3.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMusicSRT3.setDescription('Music SRT chip line 3')
wfModMusicSRT4 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 82), Integer32())
if mibBuilder.loadTexts: wfModMusicSRT4.setStatus('mandatory')
if mibBuilder.loadTexts: wfModMusicSRT4.setDescription('Music SRT chip line 4')
wfModClrQ1Reset = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 83), Integer32())
if mibBuilder.loadTexts: wfModClrQ1Reset.setStatus('mandatory')
if mibBuilder.loadTexts: wfModClrQ1Reset.setDescription('Clear QUICC-1 reset')
wfModClrQ2Reset = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 84), Integer32())
if mibBuilder.loadTexts: wfModClrQ2Reset.setStatus('mandatory')
if mibBuilder.loadTexts: wfModClrQ2Reset.setDescription('Clear QUICC-2 reset')
wfModQ1Dram = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 85), Integer32())
if mibBuilder.loadTexts: wfModQ1Dram.setStatus('mandatory')
if mibBuilder.loadTexts: wfModQ1Dram.setDescription('QUICC-1 DRAM')
wfModQ2Dram = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 86), Integer32())
if mibBuilder.loadTexts: wfModQ2Dram.setStatus('mandatory')
if mibBuilder.loadTexts: wfModQ2Dram.setDescription('QUICC-2 DRAM')
wfModQ1DPram = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 87), Integer32())
if mibBuilder.loadTexts: wfModQ1DPram.setStatus('mandatory')
if mibBuilder.loadTexts: wfModQ1DPram.setDescription('QUICC-1 DPRAM')
wfModQ2DPram = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 88), Integer32())
if mibBuilder.loadTexts: wfModQ2DPram.setStatus('mandatory')
if mibBuilder.loadTexts: wfModQ2DPram.setDescription('QUICC-2 DPRAM')
wfModQ1StickyBit = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 89), Integer32())
if mibBuilder.loadTexts: wfModQ1StickyBit.setStatus('mandatory')
if mibBuilder.loadTexts: wfModQ1StickyBit.setDescription('QUICC-1 Sticky Bit Write Address base')
wfModQ2StickyBit = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 90), Integer32())
if mibBuilder.loadTexts: wfModQ2StickyBit.setStatus('mandatory')
if mibBuilder.loadTexts: wfModQ2StickyBit.setDescription('QUICC-2 Sticky Bit Write Address base')
wfModQ1Int7 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 91), Integer32())
if mibBuilder.loadTexts: wfModQ1Int7.setStatus('mandatory')
if mibBuilder.loadTexts: wfModQ1Int7.setDescription('QUICC-1 Interrupt COP high')
wfModQ2Int7 = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 92), Integer32())
if mibBuilder.loadTexts: wfModQ2Int7.setStatus('mandatory')
if mibBuilder.loadTexts: wfModQ2Int7.setDescription('QUICC-2 Interrupt COP high')
wfModApplyQ1Reset = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 93), Integer32())
if mibBuilder.loadTexts: wfModApplyQ1Reset.setStatus('mandatory')
if mibBuilder.loadTexts: wfModApplyQ1Reset.setDescription('Apply QUICC-1 reset')
wfModApplyQ2Reset = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 94), Integer32())
if mibBuilder.loadTexts: wfModApplyQ2Reset.setStatus('mandatory')
if mibBuilder.loadTexts: wfModApplyQ2Reset.setDescription('Apply QUICC-2 reset')
mibBuilder.exportSymbols("Wellfleet-HWMO-MIB", wfModMuxram1=wfModMuxram1, wfModLance2=wfModLance2, wfModSbrr=wfModSbrr, wfModDefaA=wfModDefaA, wfModQ2StickyBit=wfModQ2StickyBit, wfModQ1Int7=wfModQ1Int7, wfModMk50254=wfModMk50254, wfModMadr1=wfModMadr1, wfModTms3801=wfModTms3801, wfModTms3802=wfModTms3802, wfMod=wfMod, wfModClrQ2Reset=wfModClrQ2Reset, wfModLance1=wfModLance1, wfModMusicSRT4=wfModMusicSRT4, wfModQ2Int7=wfModQ2Int7, wfModTms3804=wfModTms3804, wfModMar1=wfModMar1, wfModIdOpt=wfModIdOpt, wfModCar=wfModCar, wfModCamel1=wfModCamel1, wfModSlot=wfModSlot, wfModMusicSRT2=wfModMusicSRT2, wfModMusicSRT1=wfModMusicSRT1, wfModCLoopup0=wfModCLoopup0, wfModClr1=wfModClr1, wfModSicr=wfModSicr, wfModDefaC=wfModDefaC, wfModTicr=wfModTicr, wfModDuart=wfModDuart, wfModQ1StickyBit=wfModQ1StickyBit, wfModTms3803=wfModTms3803, wfModCLoopdn0=wfModCLoopdn0, wfModHssiFsi1=wfModHssiFsi1, wfModApplyQ1Reset=wfModApplyQ1Reset, wfModProm=wfModProm, wfModMuxram2=wfModMuxram2, wfModApplyQ2Reset=wfModApplyQ2Reset, wfModMusicSRT3=wfModMusicSRT3, wfModMadr2=wfModMadr2, wfModHlsrData=wfModHlsrData, wfModDefaB=wfModDefaB, wfModMadr5=wfModMadr5, wfModIlacc2=wfModIlacc2, wfModCamBLock=wfModCamBLock, wfModMisr=wfModMisr, wfModMk50251=wfModMk50251, wfModHicr=wfModHicr, wfModMac1=wfModMac1, wfModFcr=wfModFcr, wfModMk50253=wfModMk50253, wfModClr0=wfModClr0, wfModMCR0=wfModMCR0, wfModQ2DPram=wfModQ2DPram, wfModIlacc1=wfModIlacc1, wfModState=wfModState, wfModIlacc3=wfModIlacc3, wfModTocr=wfModTocr, wfModHlsr=wfModHlsr, wfModMled=wfModMled, wfModTsra=wfModTsra, wfModHssiUga2=wfModHssiUga2, wfModMidr=wfModMidr, wfModClrQ1Reset=wfModClrQ1Reset, wfModHssiFsi2=wfModHssiFsi2, wfModCcr1=wfModCcr1, wfModMgbc=wfModMgbc, wfModHssiUga1=wfModHssiUga1, wfModCcr0=wfModCcr0, wfModMCR1=wfModMCR1, wfModBert=wfModBert, wfModMar0=wfModMar0, wfModCLoopdn1=wfModCLoopdn1, wfModLEDC=wfModLEDC, wfModElmB1=wfModElmB1, wfModIlacc4=wfModIlacc4, wfModCLoopup1=wfModCLoopup1, wfMod8530=wfMod8530, wfModQ1Dram=wfModQ1Dram, wfModFsi1=wfModFsi1, wfModRev=wfModRev, wfModCamAUnlock=wfModCamAUnlock, wfModFramer2=wfModFramer2, wfModMadr4=wfModMadr4, wfModMcr1=wfModMcr1, wfModQ2Dram=wfModQ2Dram, wfModSnprom=wfModSnprom, wfModElmA1=wfModElmA1, wfModHicrData=wfModHicrData, wfModCclk=wfModCclk, wfModMadr3=wfModMadr3, wfModQ1DPram=wfModQ1DPram, wfModMk50252=wfModMk50252, wfModCamALock=wfModCamALock, wfModCamBUnlock=wfModCamBUnlock, wfModFramer1=wfModFramer1)
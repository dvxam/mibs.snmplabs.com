#
# PySNMP MIB module ESSENTIAL-COMMUNICATIONS-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ESSENTIAL-COMMUNICATIONS-GLOBAL-REG
# Produced by pysmi-0.3.4 at Wed May  1 13:06:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Unsigned32, Integer32, enterprises, Gauge32, IpAddress, ModuleIdentity, iso, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "enterprises", "Gauge32", "IpAddress", "ModuleIdentity", "iso", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
essentialCommunications = MibIdentifier((1, 3, 6, 1, 4, 1, 2159))
ecRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1))
ecRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 1))
ecModules = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 1, 1))
ecGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 2))
ecProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 3))
ecAgentProfiles = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 4))
ecRequirements = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 5))
ecExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 6))
ecNICReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 1, 2))
ecMICReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 1, 3))
ecSwitchReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 1, 4))
pmicHIPPIReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 1, 3, 1))
smicHIPPISWLReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 1, 3, 2))
smicHIPPILWLReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 1, 3, 3))
ecEPS16Reg = MibIdentifier((1, 3, 6, 1, 4, 1, 2159, 1, 1, 4, 1))
mibBuilder.exportSymbols("ESSENTIAL-COMMUNICATIONS-GLOBAL-REG", ecRoot=ecRoot, ecEPS16Reg=ecEPS16Reg, ecSwitchReg=ecSwitchReg, ecRegistration=ecRegistration, ecGeneric=ecGeneric, ecModules=ecModules, essentialCommunications=essentialCommunications, ecProducts=ecProducts, ecAgentProfiles=ecAgentProfiles, ecRequirements=ecRequirements, ecMICReg=ecMICReg, smicHIPPILWLReg=smicHIPPILWLReg, ecExperimental=ecExperimental, smicHIPPISWLReg=smicHIPPISWLReg, pmicHIPPIReg=pmicHIPPIReg, ecNICReg=ecNICReg)

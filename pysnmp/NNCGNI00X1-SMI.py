#
# PySNMP MIB module NNCGNI00X1-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI00X1-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, enterprises, Counter32, Counter64, TimeTicks, MibIdentifier, NotificationType, ObjectIdentity, ModuleIdentity, Integer32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "enterprises", "Counter32", "Counter64", "TimeTicks", "MibIdentifier", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Integer32", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
newbridge = MibIdentifier((1, 3, 6, 1, 4, 1, 123))
nncDeviceIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1))
nncInterimMib = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 2))
nncExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3))
nncStandalone = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1, 1))
nnc8230 = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1, 1, 1))
nnc3604 = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1, 1, 2))
nnc8231 = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1, 1, 3))
nnc8251 = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1, 1, 4))
nnc3601 = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1, 1, 5))
nncIntegral = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1, 2))
nncITB = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 1, 2, 1))
nncExtSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 1))
nncExtEnvironmental = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 2))
nncExtRestart = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 3))
nncExtCodeSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 4))
nncExtNVM = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 5))
nncExtAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 6))
nncExtNetSynch = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 7))
nncExtPosition = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 8))
nncExtDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 9))
nncExtDs1 = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 10))
nncExtRptr = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 11))
nncExtProbe = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 12))
nncExtDiag = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 13))
nncExtSyncDataCct = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 14))
mibBuilder.exportSymbols("NNCGNI00X1-SMI", nnc3601=nnc3601, nnc3604=nnc3604, nncExtNVM=nncExtNVM, nncExtSystem=nncExtSystem, nnc8231=nnc8231, nncITB=nncITB, nncExtProbe=nncExtProbe, nncExtAlarm=nncExtAlarm, nncExtDevice=nncExtDevice, nncExtRptr=nncExtRptr, nnc8251=nnc8251, nncStandalone=nncStandalone, nncInterimMib=nncInterimMib, nncExtNetSynch=nncExtNetSynch, nnc8230=nnc8230, newbridge=newbridge, nncExtDs1=nncExtDs1, nncDeviceIDs=nncDeviceIDs, nncExtPosition=nncExtPosition, nncExtDiag=nncExtDiag, nncExtensions=nncExtensions, nncIntegral=nncIntegral, nncExtSyncDataCct=nncExtSyncDataCct, nncExtRestart=nncExtRestart, nncExtEnvironmental=nncExtEnvironmental, nncExtCodeSpace=nncExtCodeSpace)

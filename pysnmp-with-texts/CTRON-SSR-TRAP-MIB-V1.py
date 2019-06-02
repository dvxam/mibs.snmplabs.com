#
# PySNMP MIB module CTRON-SSR-TRAP-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SSR-TRAP-MIB-V1
# Produced by pysmi-0.3.4 at Wed May  1 12:31:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
sysHwPowerSupply, sysHwTemperature, sysHwFan, sysHwModuleSlotNumber = mibBuilder.importSymbols("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply", "sysHwTemperature", "sysHwFan", "sysHwModuleSlotNumber")
ssrTraps, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrTraps")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, ObjectIdentity, Bits, MibIdentifier, iso, NotificationType, ModuleIdentity, Integer32, Counter64, Unsigned32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ObjectIdentity", "Bits", "MibIdentifier", "iso", "NotificationType", "ModuleIdentity", "Integer32", "Counter64", "Unsigned32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
envPowerSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,1)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
if mibBuilder.loadTexts: envPowerSupplyFailed.setDescription('A power supply on the sending device has failed. The sysHwPowerSupply object identifies the failed supply. Poll sysHwPowerSupply to obtain current status of power supplies')
envPowerSupplyRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,2)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
if mibBuilder.loadTexts: envPowerSupplyRecovered.setDescription('A power supply on the sending device has recovered after failure. The sysHwPowerSupply object identifies the recovered supply. Poll sysHwPowerSupply to obtain current status of power supplies')
envFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,3)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
if mibBuilder.loadTexts: envFanFailed.setDescription('A Fan tray on the sending device has failed. The sysHwFan object identifies the failed fan tray. Poll sysHwFan to obtain current status.')
envFanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,4)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
if mibBuilder.loadTexts: envFanRecovered.setDescription('A Fan tray on the sending device has recovered after failure. The sysHwFan object identifies the recovered Fan tray. Poll sysHwFan to obtain current status.')
envTempExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,5)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
if mibBuilder.loadTexts: envTempExceeded.setDescription('A temperature inside the chassis on the sending device has exceeded normal operating temperature. The sysHwTemperature object identifies the current status. Poll sysHwTemperature to obtain current status.')
envTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,6)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
if mibBuilder.loadTexts: envTempNormal.setDescription('A temperature inside the chassis on the sending device has returned to normal operating temperature. The sysHwTemperature object identifies the current status. Poll sysHwTemperature to obtain current status.')
envHotSwapIn = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,7)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envHotSwapIn.setDescription('A module has been inserted into the chassis. sysHwModuleSlotNumber identifies the slot the module was inserted into. Poll sysHwLastHotSwapEvent to monitor hotswap events. ')
envHotSwapOut = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,8)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envHotSwapOut.setDescription('A module has been turned off or removed from the chassis. sysHwModuleSlotNumber identifies the slot the module was removed from. Poll sysHwLastHotSwapEvent to monitor hotswap events. ')
envBackupControlModuleOnline = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,9)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envBackupControlModuleOnline.setDescription('A backup control module that was in standby mode has taken over for a failed primary control module. Poll sysHwControlModuleBackupState for current state of backup control module. sysHwModuleSlotNumber is the index into the sysHwModuleTable for the now active control module.')
mibBuilder.exportSymbols("CTRON-SSR-TRAP-MIB-V1", envHotSwapOut=envHotSwapOut, envPowerSupplyRecovered=envPowerSupplyRecovered, envFanFailed=envFanFailed, envFanRecovered=envFanRecovered, envTempExceeded=envTempExceeded, envBackupControlModuleOnline=envBackupControlModuleOnline, envTempNormal=envTempNormal, envPowerSupplyFailed=envPowerSupplyFailed, envHotSwapIn=envHotSwapIn)
#
# PySNMP MIB module ZYXEL-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-LLDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, NotificationType, Gauge32, Unsigned32, IpAddress, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "Gauge32", "Unsigned32", "IpAddress", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelLldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43))
if mibBuilder.loadTexts: zyxelLldp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelLldp.setOrganization('Enterprise Solution ZyXEL')
zyxelLldpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 1))
zyxelLldpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2))
zyLldpState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLldpState.setStatus('current')
zyLldpRemoteInfoClear = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLldpRemoteInfoClear.setStatus('current')
zyLldpRemoteInfoClearPorts = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLldpRemoteInfoClearPorts.setStatus('current')
zyLldpStatisticsClear = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLldpStatisticsClear.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-LLDP-MIB", zyLldpStatisticsClear=zyLldpStatisticsClear, zyLldpRemoteInfoClear=zyLldpRemoteInfoClear, zyLldpRemoteInfoClearPorts=zyLldpRemoteInfoClearPorts, PYSNMP_MODULE_ID=zyxelLldp, zyxelLldpStatus=zyxelLldpStatus, zyxelLldpSetup=zyxelLldpSetup, zyLldpState=zyLldpState, zyxelLldp=zyxelLldp)
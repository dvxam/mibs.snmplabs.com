#
# PySNMP MIB module JUNIPER-JS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JS-SMI
# Produced by pysmi-0.3.4 at Wed May  1 13:58:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
jnxJsMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxJsMibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, iso, IpAddress, Gauge32, ModuleIdentity, Counter32, Bits, TimeTicks, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "iso", "IpAddress", "Gauge32", "ModuleIdentity", "Counter32", "Bits", "TimeTicks", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxJsSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1))
jnxJsIf = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1))
jnxJsAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2))
jnxJsCertificates = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3))
jnxJsPolicies = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4))
jnxJsIPSecVpn = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5))
jnxJsNAT = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7))
jnxJsScreening = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8))
jnxJsDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 9))
jnxJsDnsRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10))
jnxJsIdpRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11))
jnxJsSPUMonitoringRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12))
jnxJsUTMRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13))
jnxJsChassisCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14))
jnxVoip = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15))
jnxJsPacketMirror = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16))
jnxLsysSecurityProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17))
mibBuilder.exportSymbols("JUNIPER-JS-SMI", jnxJsSPUMonitoringRoot=jnxJsSPUMonitoringRoot, jnxJsIf=jnxJsIf, jnxJsScreening=jnxJsScreening, jnxJsUTMRoot=jnxJsUTMRoot, jnxJsChassisCluster=jnxJsChassisCluster, jnxLsysSecurityProfile=jnxLsysSecurityProfile, jnxJsDhcp=jnxJsDhcp, jnxJsNAT=jnxJsNAT, jnxJsIdpRoot=jnxJsIdpRoot, jnxJsSecurity=jnxJsSecurity, jnxVoip=jnxVoip, jnxJsDnsRoot=jnxJsDnsRoot, jnxJsPolicies=jnxJsPolicies, jnxJsPacketMirror=jnxJsPacketMirror, jnxJsCertificates=jnxJsCertificates, jnxJsAuth=jnxJsAuth, jnxJsIPSecVpn=jnxJsIPSecVpn)
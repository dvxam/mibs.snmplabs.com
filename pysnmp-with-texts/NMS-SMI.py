#
# PySNMP MIB module NMS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-SMI
# Produced by pysmi-0.3.4 at Wed May  1 14:21:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
pbn, = mibBuilder.importSymbols("PBN-ROOT", "pbn")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, iso, Gauge32, Counter64, Integer32, NotificationType, IpAddress, Counter32, ModuleIdentity, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "iso", "Gauge32", "Counter64", "Integer32", "NotificationType", "IpAddress", "Counter32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nms = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10))
if mibBuilder.loadTexts: nms.setStatus('current')
if mibBuilder.loadTexts: nms.setDescription('nms Products is the root OBJECT IDENTIFIER from which sysObjectID values are assigned.')
nmsProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 1))
if mibBuilder.loadTexts: nmsProducts.setStatus('current')
if mibBuilder.loadTexts: nmsProducts.setDescription('nms Products is the root OBJECT IDENTIFIER from which sysObjectID values are assigned.')
nmslocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 2))
if mibBuilder.loadTexts: nmslocal.setStatus('current')
if mibBuilder.loadTexts: nmslocal.setDescription('Subtree beneath which pre-10.2 MIBS were built.')
nmstemporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 3))
if mibBuilder.loadTexts: nmstemporary.setStatus('current')
if mibBuilder.loadTexts: nmstemporary.setDescription('Subtree beneath which pre-10.2 experiments were placed.')
nmsMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 9))
if mibBuilder.loadTexts: nmsMgmt.setStatus('current')
if mibBuilder.loadTexts: nmsMgmt.setDescription('nmsMgmt is the main subtree for new mib development.')
nmsModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 12))
if mibBuilder.loadTexts: nmsModules.setStatus('current')
if mibBuilder.loadTexts: nmsModules.setDescription('nmsModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
nmsPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 18))
if mibBuilder.loadTexts: nmsPolicyAuto.setStatus('current')
if mibBuilder.loadTexts: nmsPolicyAuto.setDescription('nmsPolicyAuto is the root of the nms-assigned OID subtree for OIDs which are automatically assigned for use in Policy Management.')
nmsPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 18, 2))
if mibBuilder.loadTexts: nmsPibToMib.setStatus('current')
if mibBuilder.loadTexts: nmsPibToMib.setDescription("nmsPibToMib is the root of the nms-assigned OID subtree for MIBs which are algorithmically generated/translated from nms PIBs with OIDs assigned under the nmsPIB subtree. These generated MIBs allow management entities (other the current Policy Server) to read the downloaded policy. By convention, for PIB 'nmsPIB.x', the generated MIB shall have the name 'nmsPibToMib.x'.")
nmsWorkGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 20))
if mibBuilder.loadTexts: nmsWorkGroup.setStatus('current')
if mibBuilder.loadTexts: nmsWorkGroup.setDescription('nmsWorkGroup is the main subtree for new mib development categorized by module function.')
nmsEPONGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 101))
if mibBuilder.loadTexts: nmsEPONGroup.setStatus('current')
if mibBuilder.loadTexts: nmsEPONGroup.setDescription('nmsEPONGroup is the main subtree for new epon mib .')
mibBuilder.exportSymbols("NMS-SMI", nmsProducts=nmsProducts, nms=nms, nmslocal=nmslocal, nmsPibToMib=nmsPibToMib, nmsPolicyAuto=nmsPolicyAuto, nmsEPONGroup=nmsEPONGroup, nmsModules=nmsModules, nmsMgmt=nmsMgmt, nmstemporary=nmstemporary, nmsWorkGroup=nmsWorkGroup)
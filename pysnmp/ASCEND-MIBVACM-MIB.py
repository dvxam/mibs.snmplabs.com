#
# PySNMP MIB module ASCEND-MIBVACM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBVACM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, ModuleIdentity, MibIdentifier, Counter64, iso, NotificationType, ObjectIdentity, Counter32, IpAddress, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "ModuleIdentity", "MibIdentifier", "Counter64", "iso", "NotificationType", "ObjectIdentity", "Counter32", "IpAddress", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibvacmSecurityGroupProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 135))
mibvacmViewTreeProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 137))
mibvacmAccessProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 136))
mibvacmSecurityGroupProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 135, 1), )
if mibBuilder.loadTexts: mibvacmSecurityGroupProfileTable.setStatus('mandatory')
mibvacmSecurityGroupProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1), ).setIndexNames((0, "ASCEND-MIBVACM-MIB", "vacmSecurityGroupProfile-SecurityProperties-SecurityModel"), (0, "ASCEND-MIBVACM-MIB", "vacmSecurityGroupProfile-SecurityProperties-SecurityName"))
if mibBuilder.loadTexts: mibvacmSecurityGroupProfileEntry.setStatus('mandatory')
vacmSecurityGroupProfile_SecurityProperties_SecurityModel = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 1), Integer32()).setLabel("vacmSecurityGroupProfile-SecurityProperties-SecurityModel").setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmSecurityGroupProfile_SecurityProperties_SecurityModel.setStatus('mandatory')
vacmSecurityGroupProfile_SecurityProperties_SecurityName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 2), OctetString()).setLabel("vacmSecurityGroupProfile-SecurityProperties-SecurityName").setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmSecurityGroupProfile_SecurityProperties_SecurityName.setStatus('mandatory')
vacmSecurityGroupProfile_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("vacmSecurityGroupProfile-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmSecurityGroupProfile_Active.setStatus('mandatory')
vacmSecurityGroupProfile_GroupName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 4), OctetString()).setLabel("vacmSecurityGroupProfile-GroupName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmSecurityGroupProfile_GroupName.setStatus('mandatory')
vacmSecurityGroupProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("vacmSecurityGroupProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmSecurityGroupProfile_Action_o.setStatus('mandatory')
mibvacmViewTreeProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 137, 1), )
if mibBuilder.loadTexts: mibvacmViewTreeProfileTable.setStatus('mandatory')
mibvacmViewTreeProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1), ).setIndexNames((0, "ASCEND-MIBVACM-MIB", "vacmViewTreeProfile-TreeProperties-ViewName"), (0, "ASCEND-MIBVACM-MIB", "vacmViewTreeProfile-TreeProperties-ViewTreeOid"))
if mibBuilder.loadTexts: mibvacmViewTreeProfileEntry.setStatus('mandatory')
vacmViewTreeProfile_TreeProperties_ViewName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 1), OctetString()).setLabel("vacmViewTreeProfile-TreeProperties-ViewName").setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmViewTreeProfile_TreeProperties_ViewName.setStatus('mandatory')
vacmViewTreeProfile_TreeProperties_ViewTreeOid = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 2), DisplayString()).setLabel("vacmViewTreeProfile-TreeProperties-ViewTreeOid").setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmViewTreeProfile_TreeProperties_ViewTreeOid.setStatus('mandatory')
vacmViewTreeProfile_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("vacmViewTreeProfile-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmViewTreeProfile_Active.setStatus('mandatory')
vacmViewTreeProfile_TreeOidMask = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 4), DisplayString()).setLabel("vacmViewTreeProfile-TreeOidMask").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmViewTreeProfile_TreeOidMask.setStatus('mandatory')
vacmViewTreeProfile_TreeType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("included", 2), ("excluded", 3)))).setLabel("vacmViewTreeProfile-TreeType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmViewTreeProfile_TreeType.setStatus('mandatory')
vacmViewTreeProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("vacmViewTreeProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmViewTreeProfile_Action_o.setStatus('mandatory')
mibvacmAccessProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 136, 1), )
if mibBuilder.loadTexts: mibvacmAccessProfileTable.setStatus('mandatory')
mibvacmAccessProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1), ).setIndexNames((0, "ASCEND-MIBVACM-MIB", "vacmAccessProfile-AccessProperties-GroupName"), (0, "ASCEND-MIBVACM-MIB", "vacmAccessProfile-AccessProperties-ContextPrefix"), (0, "ASCEND-MIBVACM-MIB", "vacmAccessProfile-AccessProperties-SecurityModel"), (0, "ASCEND-MIBVACM-MIB", "vacmAccessProfile-AccessProperties-SecurityLevel"))
if mibBuilder.loadTexts: mibvacmAccessProfileEntry.setStatus('mandatory')
vacmAccessProfile_AccessProperties_GroupName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 1), OctetString()).setLabel("vacmAccessProfile-AccessProperties-GroupName").setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmAccessProfile_AccessProperties_GroupName.setStatus('mandatory')
vacmAccessProfile_AccessProperties_ContextPrefix = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 2), OctetString()).setLabel("vacmAccessProfile-AccessProperties-ContextPrefix").setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmAccessProfile_AccessProperties_ContextPrefix.setStatus('mandatory')
vacmAccessProfile_AccessProperties_SecurityModel = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 3), Integer32()).setLabel("vacmAccessProfile-AccessProperties-SecurityModel").setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmAccessProfile_AccessProperties_SecurityModel.setStatus('mandatory')
vacmAccessProfile_AccessProperties_SecurityLevel = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 4), Integer32()).setLabel("vacmAccessProfile-AccessProperties-SecurityLevel").setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmAccessProfile_AccessProperties_SecurityLevel.setStatus('mandatory')
vacmAccessProfile_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("vacmAccessProfile-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmAccessProfile_Active.setStatus('mandatory')
vacmAccessProfile_MatchMethod = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("exactMatch", 2), ("prefixMatch", 3)))).setLabel("vacmAccessProfile-MatchMethod").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmAccessProfile_MatchMethod.setStatus('mandatory')
vacmAccessProfile_ReadViewName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 7), OctetString()).setLabel("vacmAccessProfile-ReadViewName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmAccessProfile_ReadViewName.setStatus('mandatory')
vacmAccessProfile_WriteViewName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 8), OctetString()).setLabel("vacmAccessProfile-WriteViewName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmAccessProfile_WriteViewName.setStatus('mandatory')
vacmAccessProfile_NotifyViewName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 9), OctetString()).setLabel("vacmAccessProfile-NotifyViewName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmAccessProfile_NotifyViewName.setStatus('mandatory')
vacmAccessProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("vacmAccessProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmAccessProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBVACM-MIB", vacmAccessProfile_Active=vacmAccessProfile_Active, vacmAccessProfile_AccessProperties_SecurityModel=vacmAccessProfile_AccessProperties_SecurityModel, mibvacmSecurityGroupProfileTable=mibvacmSecurityGroupProfileTable, vacmSecurityGroupProfile_Active=vacmSecurityGroupProfile_Active, mibvacmViewTreeProfileEntry=mibvacmViewTreeProfileEntry, mibvacmAccessProfile=mibvacmAccessProfile, mibvacmAccessProfileEntry=mibvacmAccessProfileEntry, vacmAccessProfile_Action_o=vacmAccessProfile_Action_o, vacmViewTreeProfile_Action_o=vacmViewTreeProfile_Action_o, vacmAccessProfile_ReadViewName=vacmAccessProfile_ReadViewName, mibvacmAccessProfileTable=mibvacmAccessProfileTable, vacmAccessProfile_MatchMethod=vacmAccessProfile_MatchMethod, vacmAccessProfile_AccessProperties_GroupName=vacmAccessProfile_AccessProperties_GroupName, DisplayString=DisplayString, vacmSecurityGroupProfile_SecurityProperties_SecurityModel=vacmSecurityGroupProfile_SecurityProperties_SecurityModel, vacmAccessProfile_WriteViewName=vacmAccessProfile_WriteViewName, mibvacmViewTreeProfileTable=mibvacmViewTreeProfileTable, vacmAccessProfile_AccessProperties_ContextPrefix=vacmAccessProfile_AccessProperties_ContextPrefix, mibvacmSecurityGroupProfileEntry=mibvacmSecurityGroupProfileEntry, vacmSecurityGroupProfile_SecurityProperties_SecurityName=vacmSecurityGroupProfile_SecurityProperties_SecurityName, vacmSecurityGroupProfile_GroupName=vacmSecurityGroupProfile_GroupName, vacmAccessProfile_AccessProperties_SecurityLevel=vacmAccessProfile_AccessProperties_SecurityLevel, vacmViewTreeProfile_TreeProperties_ViewTreeOid=vacmViewTreeProfile_TreeProperties_ViewTreeOid, vacmViewTreeProfile_Active=vacmViewTreeProfile_Active, vacmViewTreeProfile_TreeProperties_ViewName=vacmViewTreeProfile_TreeProperties_ViewName, mibvacmViewTreeProfile=mibvacmViewTreeProfile, vacmAccessProfile_NotifyViewName=vacmAccessProfile_NotifyViewName, mibvacmSecurityGroupProfile=mibvacmSecurityGroupProfile, vacmSecurityGroupProfile_Action_o=vacmSecurityGroupProfile_Action_o, vacmViewTreeProfile_TreeOidMask=vacmViewTreeProfile_TreeOidMask, vacmViewTreeProfile_TreeType=vacmViewTreeProfile_TreeType)

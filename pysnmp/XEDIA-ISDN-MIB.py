#
# PySNMP MIB module XEDIA-ISDN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-ISDN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
dialCtlPeerCfgEntry, = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "dialCtlPeerCfgEntry")
isdnBasicRateEntry, isdnSignalingEntry = mibBuilder.importSymbols("ISDN-MIB", "isdnBasicRateEntry", "isdnSignalingEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, ObjectIdentity, NotificationType, Gauge32, Unsigned32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, MibIdentifier, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "MibIdentifier", "IpAddress", "TimeTicks")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaIsdnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 37))
if mibBuilder.loadTexts: xediaIsdnMIB.setLastUpdated('9909032155Z')
if mibBuilder.loadTexts: xediaIsdnMIB.setOrganization('Xedia Corp.')
xisdnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 37, 1))
xisdnConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 37, 2))
xisdnTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 1), )
if mibBuilder.loadTexts: xisdnTable.setStatus('current')
xisdnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 1, 1), )
isdnBasicRateEntry.registerAugmentions(("XEDIA-ISDN-MIB", "xisdnEntry"))
xisdnEntry.setIndexNames(*isdnBasicRateEntry.getIndexNames())
if mibBuilder.loadTexts: xisdnEntry.setStatus('current')
xisdnLoopbackState = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xisdnLoopbackState.setStatus('current')
xisdnSignalingTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4), )
if mibBuilder.loadTexts: xisdnSignalingTable.setStatus('current')
xisdnSignalingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4, 1), )
isdnSignalingEntry.registerAugmentions(("XEDIA-ISDN-MIB", "xisdnSignalingEntry"))
xisdnSignalingEntry.setIndexNames(*isdnSignalingEntry.getIndexNames())
if mibBuilder.loadTexts: xisdnSignalingEntry.setStatus('current')
isdnSignalingCallingAddress2 = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingCallingAddress2.setStatus('current')
isdnEndpointSpid = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointSpid.setStatus('current')
isdnEndpointSpid2 = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 4, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointSpid2.setStatus('current')
xdialCtlPeerCfgTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 2), )
if mibBuilder.loadTexts: xdialCtlPeerCfgTable.setStatus('current')
xdialCtlPeerCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 2, 1), )
dialCtlPeerCfgEntry.registerAugmentions(("XEDIA-ISDN-MIB", "xdialCtlPeerCfgEntry"))
xdialCtlPeerCfgEntry.setIndexNames(*dialCtlPeerCfgEntry.getIndexNames())
if mibBuilder.loadTexts: xdialCtlPeerCfgEntry.setStatus('current')
xcallControl = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noOp", 1), ("connect", 2), ("disconnect", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcallControl.setStatus('current')
xnailedUp = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("b1", 2), ("b2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xnailedUp.setStatus('current')
xisdnVersion = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 37, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xisdnVersion.setStatus('current')
xisdnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 37, 2, 1))
xisdnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 37, 2, 2))
xisdnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 37, 2, 1, 1)).setObjects(("XEDIA-ISDN-MIB", "xisdnAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xisdnCompliance = xisdnCompliance.setStatus('current')
xisdnAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 37, 2, 2, 1)).setObjects(("XEDIA-ISDN-MIB", "xisdnLoopbackState"), ("XEDIA-ISDN-MIB", "xcallControl"), ("XEDIA-ISDN-MIB", "xnailedUp"), ("XEDIA-ISDN-MIB", "xisdnVersion"), ("XEDIA-ISDN-MIB", "isdnSignalingCallingAddress2"), ("XEDIA-ISDN-MIB", "isdnEndpointSpid"), ("XEDIA-ISDN-MIB", "isdnEndpointSpid2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xisdnAllGroup = xisdnAllGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-ISDN-MIB", xisdnObjects=xisdnObjects, xdialCtlPeerCfgTable=xdialCtlPeerCfgTable, xisdnAllGroup=xisdnAllGroup, xdialCtlPeerCfgEntry=xdialCtlPeerCfgEntry, xisdnGroups=xisdnGroups, isdnEndpointSpid=isdnEndpointSpid, PYSNMP_MODULE_ID=xediaIsdnMIB, xediaIsdnMIB=xediaIsdnMIB, xcallControl=xcallControl, isdnSignalingCallingAddress2=isdnSignalingCallingAddress2, xisdnSignalingEntry=xisdnSignalingEntry, xisdnCompliance=xisdnCompliance, xisdnEntry=xisdnEntry, xisdnCompliances=xisdnCompliances, xisdnSignalingTable=xisdnSignalingTable, xisdnTable=xisdnTable, xisdnVersion=xisdnVersion, isdnEndpointSpid2=isdnEndpointSpid2, xnailedUp=xnailedUp, xisdnLoopbackState=xisdnLoopbackState, xisdnConformance=xisdnConformance)

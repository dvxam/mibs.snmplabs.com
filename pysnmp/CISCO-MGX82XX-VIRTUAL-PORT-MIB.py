#
# PySNMP MIB module CISCO-MGX82XX-VIRTUAL-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGX82XX-VIRTUAL-PORT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
virtualInterface, = mibBuilder.importSymbols("BASIS-MIB", "virtualInterface")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, NotificationType, Counter64, Gauge32, MibIdentifier, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, IpAddress, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "NotificationType", "Counter64", "Gauge32", "MibIdentifier", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "IpAddress", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMgx82xxVirtualPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 38))
ciscoMgx82xxVirtualPortMIB.setRevisions(('2002-08-30 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxVirtualPortMIB.setLastUpdated('200208300000Z')
if mibBuilder.loadTexts: ciscoMgx82xxVirtualPortMIB.setOrganization('Cisco Systems, Inc.')
virtualInterfaceCnf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1))
virtualInterfaceCnt = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2))
virtualInterfaceQbinCnf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3))
virtualInterfaceQbinCnt = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4))
vrtlIntrConfigTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1), )
if mibBuilder.loadTexts: vrtlIntrConfigTable.setStatus('current')
vrtlIntrConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "configVrtlIntrNum"))
if mibBuilder.loadTexts: vrtlIntrConfigEntry.setStatus('current')
configVrtlIntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configVrtlIntrNum.setStatus('current')
vrtlIntrPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrPortNum.setStatus('current')
vrtlIntrState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrState.setStatus('current')
vrtlIntrMaxQueMem = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrMaxQueMem.setStatus('current')
vrtlIntrMinCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(103384, 353208))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrMinCellRate.setStatus('current')
vrtlIntrMaxCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(103384, 353208))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrMaxCellRate.setStatus('current')
vrtlIntrCurrConfigPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrCurrConfigPaths.setStatus('current')
vrtlIntrCounterTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1), )
if mibBuilder.loadTexts: vrtlIntrCounterTable.setStatus('current')
vrtlIntrCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "countVrtlIntrNum"))
if mibBuilder.loadTexts: vrtlIntrCounterEntry.setStatus('current')
countVrtlIntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: countVrtlIntrNum.setStatus('current')
vrtlIntrTotalCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrTotalCellCnt.setStatus('current')
vrtlIntrTotalQbinCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrTotalQbinCellCnt.setStatus('current')
vrtlIntrRxdValidOAMCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdValidOAMCellCnt.setStatus('current')
vrtlIntrRxdRmCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdRmCellCnt.setStatus('current')
vrtlIntrRxdClpUntaggedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdClpUntaggedCellCnt.setStatus('current')
vrtlIntrRxdClpTaggedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdClpTaggedCellCnt.setStatus('current')
vrtlIntrRxdClpUntaggedDiscardedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdClpUntaggedDiscardedCellCnt.setStatus('current')
vrtlIntrRxdClpTaggedDiscardedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdClpTaggedDiscardedCellCnt.setStatus('current')
vrtlIntrXmtdOAMCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrXmtdOAMCellCnt.setStatus('current')
vrtlIntrXmtdRmCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrXmtdRmCellCnt.setStatus('current')
vrtlIntrXmtdClpUntaggedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrXmtdClpUntaggedCellCnt.setStatus('current')
vrtlIntrXmtdClpTaggedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrXmtdClpTaggedCellCnt.setStatus('current')
vrtlIntrQbinConfigTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1), )
if mibBuilder.loadTexts: vrtlIntrQbinConfigTable.setStatus('current')
vrtlIntrQbinConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrNum"), (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrQbinNum"))
if mibBuilder.loadTexts: vrtlIntrQbinConfigEntry.setStatus('current')
queConfigVrtlIntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: queConfigVrtlIntrNum.setStatus('current')
queConfigVrtlIntrQbinNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: queConfigVrtlIntrQbinNum.setStatus('current')
vrtlIntrQbinState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinState.setStatus('current')
vrtlIntrQbinPri = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinPri.setStatus('current')
vrtlIntrQbinRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 353208))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinRate.setStatus('current')
vrtlIntrQbinDiscardSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("clpHysteresis", 1), ("frameDiscard", 3))).clone('clpHysteresis')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinDiscardSelection.setStatus('current')
vrtlIntrQbinMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinMaxThreshold.setStatus('current')
vrtlIntrQbinClpHiThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinClpHiThreshold.setStatus('current')
vrtlIntrQbinClpLoThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinClpLoThreshold.setStatus('current')
vrtlIntrQbinFrameDiscardThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinFrameDiscardThreshold.setStatus('current')
vrtlIntrQbinEfciThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinEfciThreshold.setStatus('current')
vrtlIntrQbinCounterTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1), )
if mibBuilder.loadTexts: vrtlIntrQbinCounterTable.setStatus('current')
vrtlIntrQbinCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConuterVrtlIntrNum"), (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queCounterVrtlIntrQbinNum"))
if mibBuilder.loadTexts: vrtlIntrQbinCounterEntry.setStatus('current')
queConuterVrtlIntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: queConuterVrtlIntrNum.setStatus('current')
queCounterVrtlIntrQbinNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: queCounterVrtlIntrQbinNum.setStatus('current')
vrtlIntrQbinCurrentCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrQbinCurrentCellCnt.setStatus('current')
vrtlIntrQbinRxdCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrQbinRxdCellCnt.setStatus('current')
vrtlIntrQbinTxdCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrQbinTxdCellCnt.setStatus('current')
vrtlIntrQbinDiscardedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrQbinDiscardedCellCnt.setStatus('current')
cmvPortMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 38, 2))
cmvPortMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1))
cmvPortMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 2))
cmvPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 2, 1)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "cmvPortConfGroup"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "cmvPortStatsGroup"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "cmvPortQbinConfGroup"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "cmvPortQbinStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortCompliance = cmvPortCompliance.setStatus('current')
cmvPortConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 1)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "configVrtlIntrNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrPortNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrState"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrMaxQueMem"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrMinCellRate"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrMaxCellRate"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrCurrConfigPaths"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortConfGroup = cmvPortConfGroup.setStatus('current')
cmvPortStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 2)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "countVrtlIntrNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrTotalCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrTotalQbinCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdValidOAMCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdRmCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpUntaggedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpTaggedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpUntaggedDiscardedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpTaggedDiscardedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdOAMCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdRmCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdClpUntaggedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdClpTaggedCellCnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortStatsGroup = cmvPortStatsGroup.setStatus('current')
cmvPortQbinConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 3)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrQbinNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinState"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinPri"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinRate"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinDiscardSelection"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinMaxThreshold"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinClpHiThreshold"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinClpLoThreshold"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinFrameDiscardThreshold"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinEfciThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortQbinConfGroup = cmvPortQbinConfGroup.setStatus('current')
cmvPortQbinStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 4)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConuterVrtlIntrNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queCounterVrtlIntrQbinNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinCurrentCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinRxdCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinTxdCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinDiscardedCellCnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortQbinStatsGroup = cmvPortQbinStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-VIRTUAL-PORT-MIB", vrtlIntrCounterEntry=vrtlIntrCounterEntry, vrtlIntrXmtdClpTaggedCellCnt=vrtlIntrXmtdClpTaggedCellCnt, vrtlIntrQbinDiscardSelection=vrtlIntrQbinDiscardSelection, vrtlIntrQbinCounterEntry=vrtlIntrQbinCounterEntry, vrtlIntrConfigTable=vrtlIntrConfigTable, vrtlIntrQbinConfigEntry=vrtlIntrQbinConfigEntry, vrtlIntrQbinTxdCellCnt=vrtlIntrQbinTxdCellCnt, virtualInterfaceQbinCnt=virtualInterfaceQbinCnt, virtualInterfaceCnf=virtualInterfaceCnf, vrtlIntrQbinCurrentCellCnt=vrtlIntrQbinCurrentCellCnt, vrtlIntrQbinDiscardedCellCnt=vrtlIntrQbinDiscardedCellCnt, cmvPortCompliance=cmvPortCompliance, cmvPortQbinConfGroup=cmvPortQbinConfGroup, vrtlIntrQbinClpHiThreshold=vrtlIntrQbinClpHiThreshold, configVrtlIntrNum=configVrtlIntrNum, countVrtlIntrNum=countVrtlIntrNum, vrtlIntrRxdClpUntaggedCellCnt=vrtlIntrRxdClpUntaggedCellCnt, queCounterVrtlIntrQbinNum=queCounterVrtlIntrQbinNum, vrtlIntrQbinFrameDiscardThreshold=vrtlIntrQbinFrameDiscardThreshold, vrtlIntrQbinState=vrtlIntrQbinState, cmvPortMIBCompliances=cmvPortMIBCompliances, vrtlIntrQbinClpLoThreshold=vrtlIntrQbinClpLoThreshold, vrtlIntrTotalQbinCellCnt=vrtlIntrTotalQbinCellCnt, PYSNMP_MODULE_ID=ciscoMgx82xxVirtualPortMIB, virtualInterfaceCnt=virtualInterfaceCnt, vrtlIntrCurrConfigPaths=vrtlIntrCurrConfigPaths, queConuterVrtlIntrNum=queConuterVrtlIntrNum, cmvPortConfGroup=cmvPortConfGroup, vrtlIntrTotalCellCnt=vrtlIntrTotalCellCnt, vrtlIntrRxdClpUntaggedDiscardedCellCnt=vrtlIntrRxdClpUntaggedDiscardedCellCnt, cmvPortMIBGroups=cmvPortMIBGroups, vrtlIntrState=vrtlIntrState, vrtlIntrQbinRate=vrtlIntrQbinRate, vrtlIntrMaxQueMem=vrtlIntrMaxQueMem, vrtlIntrQbinMaxThreshold=vrtlIntrQbinMaxThreshold, vrtlIntrRxdClpTaggedDiscardedCellCnt=vrtlIntrRxdClpTaggedDiscardedCellCnt, cmvPortQbinStatsGroup=cmvPortQbinStatsGroup, queConfigVrtlIntrNum=queConfigVrtlIntrNum, vrtlIntrXmtdClpUntaggedCellCnt=vrtlIntrXmtdClpUntaggedCellCnt, vrtlIntrQbinEfciThreshold=vrtlIntrQbinEfciThreshold, vrtlIntrRxdRmCellCnt=vrtlIntrRxdRmCellCnt, ciscoMgx82xxVirtualPortMIB=ciscoMgx82xxVirtualPortMIB, vrtlIntrCounterTable=vrtlIntrCounterTable, vrtlIntrRxdClpTaggedCellCnt=vrtlIntrRxdClpTaggedCellCnt, vrtlIntrQbinRxdCellCnt=vrtlIntrQbinRxdCellCnt, vrtlIntrXmtdOAMCellCnt=vrtlIntrXmtdOAMCellCnt, vrtlIntrConfigEntry=vrtlIntrConfigEntry, queConfigVrtlIntrQbinNum=queConfigVrtlIntrQbinNum, vrtlIntrXmtdRmCellCnt=vrtlIntrXmtdRmCellCnt, virtualInterfaceQbinCnf=virtualInterfaceQbinCnf, vrtlIntrQbinPri=vrtlIntrQbinPri, vrtlIntrMinCellRate=vrtlIntrMinCellRate, vrtlIntrMaxCellRate=vrtlIntrMaxCellRate, cmvPortStatsGroup=cmvPortStatsGroup, cmvPortMIBConformance=cmvPortMIBConformance, vrtlIntrRxdValidOAMCellCnt=vrtlIntrRxdValidOAMCellCnt, vrtlIntrQbinCounterTable=vrtlIntrQbinCounterTable, vrtlIntrPortNum=vrtlIntrPortNum, vrtlIntrQbinConfigTable=vrtlIntrQbinConfigTable)
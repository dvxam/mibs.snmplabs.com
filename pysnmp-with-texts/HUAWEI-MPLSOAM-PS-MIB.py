#
# PySNMP MIB module HUAWEI-MPLSOAM-PS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MPLSOAM-PS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:47:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hwMpls, = mibBuilder.importSymbols("HUAWEI-MIB", "hwMpls")
hwMplsTunnelSignalProto, = mibBuilder.importSymbols("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, MibIdentifier, IpAddress, Bits, Gauge32, ObjectIdentity, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "MibIdentifier", "IpAddress", "Bits", "Gauge32", "ObjectIdentity", "ModuleIdentity", "iso")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
hwMplsOam = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7))
if mibBuilder.loadTexts: hwMplsOam.setLastUpdated('200504271724Z')
if mibBuilder.loadTexts: hwMplsOam.setOrganization('Huawei Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwMplsOam.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwMplsOam.setDescription('The HUAWEI-MPLSOAM-MIB contains objects to configure OAM module. The Operation, Administration and Maintenance (OAM) is an effective means for decreasing the cost of network maintenance. The MPLS OAM is used to administrate and maintain MPLS. ')
hwMplsOamPs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1))
hwMplsPsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3))
hwMplsPsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1), )
if mibBuilder.loadTexts: hwMplsPsTable.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsTable.setDescription('This table specifies per-protection-group MPLS PS capability and associated information. ')
hwMplsPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1), ).setIndexNames((0, "HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsIndex"))
if mibBuilder.loadTexts: hwMplsPsEntry.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsEntry.setDescription('An entry in this table is created by an LSR for every protection group capable of supporting mpls ps.')
hwMplsPsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsIndex.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsIndex.setDescription('This is a unique index for an entry in the mplspsEntry. ')
hwMplsPsType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsType.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsType.setDescription('The type of protection switch,can be 1:1,1+1,shared mesh, packet 1+1,the default choice is 1:1. In the 1+1 architecture type, a protection LSP is dedicated to each working LSP with the working LSP bridged onto the protection LSP at the source of the protection domain. The traffic on working and protection LSPs is transmitted simultaneously to the sink of the protection domain, where a selection between the working and protection LSP is made, based on some predetermined criteria, such as defect indication. In the 1:1 architecture type, a protection LSP is dedicated to each working LSP. The working traffic is transmitted either by working or protection LSP. In the shared mesh architecture type, possible sharing of protection capacity between disjoint link, node in the network is achieved while guaranteeing recovery from a single failure. In the packet 1+1 architecture type, the traffic is transmitted simultaneously onto two possibly disjoint routed LSPs to the sink of the protection domain. Each pair of duplicate transmitted packets is assigned the same identifier (sequence number) but distinct from the other pairs of duplicate packets. At the sink of the protection domain packet level selection mechanism is employed to select one of the two possibly received copies of each packet. 1: 1:1 protection switching,; 2: 1+1 protection switching; 3: shared mesh protection swiching; 4: packet 1+1 protection switching. ')
hwMplsPsWorkTunnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsWorkTunnName.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsWorkTunnName.setDescription('The name of work-tunnel.')
hwMplsPsWorkTunnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsWorkTunnId.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsWorkTunnId.setDescription('Work-tunnel id(session-tunnel-id).')
hwMplsPsProtectTunnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsProtectTunnName.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsProtectTunnName.setDescription('The name of protect-tunnel.')
hwMplsPsProtectTunnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsProtectTunnId.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsProtectTunnId.setDescription('Protect-tunnel id(session-tunnel-id).')
hwMplsPsRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsRevertiveMode.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsRevertiveMode.setDescription('Revertive mode is a protection switching mode where revertive action (switch back to the working LSP) is taken after the working LSP is repaired.And switching does not occur in a non-revertive mode. 1: revertive; 2: non-revertive; ')
hwMplsPsWTR = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsWTR.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsWTR.setDescription('Wait to Restore timer is only applicable for the revertive mode and applies to a working LSP,It prevents reversion back to select the working LSP until the Wait to Restore timer has expired.The default value is 12 minutes.step is 30s.')
hwMplsPsHoldOff = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsHoldOff.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsHoldOff.setDescription('The time between declaration of signal degrade or signal fail, and the initialization of the protection switching algorithm. step is 100ms.maximum is 10s.')
hwMplsPsSwitchCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsSwitchCondition.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsSwitchCondition.setDescription('The current switch condition of the protection group. 1: clear,This command clears all of the externally initiated switch commands listed below; 2: lockout of protection,Fix the selector position on the working LSP,Prevents the selector from switching to the protection LSP when it is selecting the working LSP. Switches the selector from the protection to the working LSP when it is selecting the protection LSP; 3: forced protection,Switches the selector from the working LSP to the protection LSP (unless a higher priority switch request (i.e., LoP) is in effect); 4: signal fail,for 1:1,Signal Fail (SF) is declared when the source of the protection domain enters the Defect State by receiving a BDI packet (from the return LSP or out of band). 5: manual switch for working-lsp,Switches the selector from the working LSP to the protection LSP (unless an equal or higher priority switch request (i.e., LoP, FS, SF or MS) is in effect); 6: manual switch for protection-lsp,Switches the selector from the protection LSP to the working LSP (unless an equal or higher priority switch request (i.e., LoP, FS, SF or MS) is in effect). 7: WTR-timer; 8: HoldOff-timer; 9: Others; The pripority of the commands are: clear > lockout of protection > force switch > manual switch for working lsp = manual switch for protection lsp')
hwMplsPsWorkTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsWorkTunnelState.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsWorkTunnelState.setDescription('The state of working tunnel state in one protection group, whether it is in detection, 1: it is outof defect 2: it enters defect ')
hwMplsPsProtTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsProtTunnelState.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsProtTunnelState.setDescription('The state of protection tunnel state in one protection group, whether it is in detection, 1: it is outof defect 2: it enters defect')
hwMplsPsSwitchResult = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsSwitchResult.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsSwitchResult.setDescription('Which tunnel is used to transfer the data stream. 1: working-tunnel 2: protection-tunnel')
hwMplsPsCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgType.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsCfgType.setDescription('The type of protection switch which is configured. 1: 1:1 2: 1+1 3: shared mesh 4: packet 1:1')
hwMplsPsCfgProtectTunnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgProtectTunnId.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsCfgProtectTunnId.setDescription('Protect-tunnel id(session-tunnel-id).')
hwMplsPsCfgRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgRevertiveMode.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsCfgRevertiveMode.setDescription('Revertive mode is a protection switching mode where revertive action (switch back to the working LSP) is taken after the working LSP is repaired.And switching does not occur in a non-revertive mode. 1: revertive; 2: non-revertive; ')
hwMplsPsCfgWTR = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgWTR.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsCfgWTR.setDescription('Wait to Restore timer is only applicable for the revertive mode and applies to a working LSP,It prevents reversion back to select the working LSP until the Wait to Restore timer has expired.The default value is 12 minutes.step is 30s.')
hwMplsPsCfgHoldOff = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgHoldOff.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsCfgHoldOff.setDescription('The time between declaration of signal degrade or signal fail, and the initialization of the protection switching algorithm. step is 100ms.maximum is 10s.')
hwMplsPsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 19), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsRowStatus.setDescription('This variable is used to create, modify, and delete a row in this table. 1: active 2: not in service 3: not ready 4: create and go 5: create and wait 6: destroy')
hwTunnPsTrapOpen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTunnPsTrapOpen.setStatus('current')
if mibBuilder.loadTexts: hwTunnPsTrapOpen.setDescription('1:enable; 2:disable;')
hwMplsVCPsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3), )
if mibBuilder.loadTexts: hwMplsVCPsTable.setStatus('current')
if mibBuilder.loadTexts: hwMplsVCPsTable.setDescription('Description.')
hwMplsApsMismatchReason = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("bridge", 1), ("channel", 2), ("switching", 3), ("operation", 4), ("traffic", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMplsApsMismatchReason.setStatus('current')
if mibBuilder.loadTexts: hwMplsApsMismatchReason.setDescription('Indicates the alarm reason as below: 1. Bridge type mismatch, one side is 1:1 (Selector Bridge) protection, the other side is 1+1 (Permanent Bridge) protection; 2. Channel type mismatch, one side has APS channel, the other side has no APS channel; 3. Switching type mismatch, one side is bidirectional switching, the other side is unidirectional switching; 4. Operation type mismatch, one side is revertive operation, the other side is non-revertive operation; 5. Traffic request mismatch, one side selects working connection, the other side selects protection connection; ')
hwMplsVCPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1), ).setIndexNames((0, "HUAWEI-MPLSOAM-PS-MIB", "hwMplsVCPsIfIndex"))
if mibBuilder.loadTexts: hwMplsVCPsEntry.setStatus('current')
if mibBuilder.loadTexts: hwMplsVCPsEntry.setDescription('this table for these commands 1.mpls te protection tunnel XXX 2. mpls te reverse-lsp { lsp-name XXXX | lsr-id X.X.X.X tunnel-id x } 3. mpls te reserved-for-binding ')
hwMplsVCPsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsVCPsIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwMplsVCPsIfIndex.setDescription('Description.the index of working tunnel interface of Protection group ')
hwMplsVCPsTNLBinding = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsVCPsTNLBinding.setStatus('current')
if mibBuilder.loadTexts: hwMplsVCPsTNLBinding.setDescription("Description.it is used by command ' mpls te reserved-for-binding '")
hwMplsTeReverseLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsTeReverseLspName.setStatus('current')
if mibBuilder.loadTexts: hwMplsTeReverseLspName.setDescription("Description.it is used for command ' mpls te reverse-lsp lspname'")
hwMplsVcPsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsVcPsRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwMplsVcPsRowStatus.setDescription('Description. 1: active; 2: notInservice; 3: notReady; 4: CreateAndGo; 5: CreateAndWait; 6: destroy;')
hwMplsTeReverseLspLsrId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsTeReverseLspLsrId.setStatus('current')
if mibBuilder.loadTexts: hwMplsTeReverseLspLsrId.setDescription("Description.it is used for command ' mpls te reverse-lsp lsr-id X.X.X.X tunnel-id XX'")
hwMplsTeReverseLspTunnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsTeReverseLspTunnId.setStatus('current')
if mibBuilder.loadTexts: hwMplsTeReverseLspTunnId.setDescription("Description.it is used for command ' mpls te reverse-lsp lsr-id X.X.X.X tunnel-id XX'")
hwMplsPsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4))
hwMplsPsSwitchPtoW = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 1)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchResult"))
if mibBuilder.loadTexts: hwMplsPsSwitchPtoW.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsSwitchPtoW.setDescription('This notification is generated when switching from protection-lsp to working-lsp occured.')
hwMplsPsSwitchWtoP = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 2)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchResult"))
if mibBuilder.loadTexts: hwMplsPsSwitchWtoP.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsSwitchWtoP.setDescription('This notification is generated when switching from woking-lsp to protection-lsp occured. ')
hwMplsApsMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 3)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatchReason"))
if mibBuilder.loadTexts: hwMplsApsMismatch.setStatus('current')
if mibBuilder.loadTexts: hwMplsApsMismatch.setDescription(' Trap information indicates fully incompatible provisioning and working/protection configuration mismatch are detected by APS frame. ')
hwMplsApsMismatchRecovery = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 4)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatchReason"))
if mibBuilder.loadTexts: hwMplsApsMismatchRecovery.setStatus('current')
if mibBuilder.loadTexts: hwMplsApsMismatchRecovery.setDescription(' Trap information indicates fully incompatible provisioning and working/protection configuration mismatch recovery are detected by APS frame. ')
hwMplsApsLost = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 5)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
if mibBuilder.loadTexts: hwMplsApsLost.setStatus('current')
if mibBuilder.loadTexts: hwMplsApsLost.setDescription(' Tunnel protection group did not receive APS frames from protection tunnel. ')
hwMplsApsLostRecovery = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 6)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
if mibBuilder.loadTexts: hwMplsApsLostRecovery.setStatus('current')
if mibBuilder.loadTexts: hwMplsApsLostRecovery.setDescription(' Tunnel protection group received APS frames from protection tunnel. ')
hwMplsOamPsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100))
hwMplsOamPsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 1))
hwMplsOamPsGroupCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 1, 1)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsGroup"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVcPsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMplsOamPsGroupCompliance = hwMplsOamPsGroupCompliance.setStatus('current')
if mibBuilder.loadTexts: hwMplsOamPsGroupCompliance.setDescription('The compliance statement for mpls oam ps.')
hwMplsOamPsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2))
hwMplsPsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2, 1)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsType"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsRevertiveMode"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWTR"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsHoldOff"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchCondition"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnelState"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtTunnelState"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchResult"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgType"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgProtectTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgRevertiveMode"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgWTR"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgHoldOff"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsRowStatus"), ("HUAWEI-MPLSOAM-PS-MIB", "hwTunnPsTrapOpen"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVCPsIfIndex"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMplsPsGroup = hwMplsPsGroup.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsGroup.setDescription('The compliance statement for mpls oam ps management.')
hwMplsVcPsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2, 2)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVCPsTNLBinding"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsTeReverseLspName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVcPsRowStatus"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsTeReverseLspLsrId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsTeReverseLspTunnId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMplsVcPsGroup = hwMplsVcPsGroup.setStatus('current')
if mibBuilder.loadTexts: hwMplsVcPsGroup.setDescription('The compliance statement for mpls oam ps reverse lsp.')
hwMplsPsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2, 3)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchPtoW"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchWtoP"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatch"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatchRecovery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMplsPsNotificationGroup = hwMplsPsNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwMplsPsNotificationGroup.setDescription('Description.')
mibBuilder.exportSymbols("HUAWEI-MPLSOAM-PS-MIB", hwMplsApsMismatch=hwMplsApsMismatch, hwMplsPsProtectTunnName=hwMplsPsProtectTunnName, hwMplsPsWorkTunnId=hwMplsPsWorkTunnId, hwMplsVcPsRowStatus=hwMplsVcPsRowStatus, hwMplsApsMismatchRecovery=hwMplsApsMismatchRecovery, hwMplsPsSwitchResult=hwMplsPsSwitchResult, hwMplsPsWTR=hwMplsPsWTR, hwMplsOamPs=hwMplsOamPs, hwMplsTeReverseLspTunnId=hwMplsTeReverseLspTunnId, hwMplsOam=hwMplsOam, hwMplsVcPsGroup=hwMplsVcPsGroup, hwMplsVCPsIfIndex=hwMplsVCPsIfIndex, hwMplsPsCfgHoldOff=hwMplsPsCfgHoldOff, hwMplsPsTable=hwMplsPsTable, hwMplsPsRevertiveMode=hwMplsPsRevertiveMode, hwMplsPsWorkTunnelState=hwMplsPsWorkTunnelState, hwMplsApsLostRecovery=hwMplsApsLostRecovery, hwMplsPsCfgProtectTunnId=hwMplsPsCfgProtectTunnId, hwMplsPsSwitchWtoP=hwMplsPsSwitchWtoP, hwMplsPsIndex=hwMplsPsIndex, hwMplsPsSwitchPtoW=hwMplsPsSwitchPtoW, hwMplsOamPsCompliances=hwMplsOamPsCompliances, hwMplsApsLost=hwMplsApsLost, hwMplsPsObjects=hwMplsPsObjects, hwTunnPsTrapOpen=hwTunnPsTrapOpen, hwMplsTeReverseLspName=hwMplsTeReverseLspName, hwMplsPsType=hwMplsPsType, hwMplsPsNotifications=hwMplsPsNotifications, hwMplsPsWorkTunnName=hwMplsPsWorkTunnName, hwMplsPsEntry=hwMplsPsEntry, hwMplsPsRowStatus=hwMplsPsRowStatus, hwMplsPsProtectTunnId=hwMplsPsProtectTunnId, PYSNMP_MODULE_ID=hwMplsOam, hwMplsOamPsConformance=hwMplsOamPsConformance, hwMplsVCPsTable=hwMplsVCPsTable, hwMplsPsNotificationGroup=hwMplsPsNotificationGroup, hwMplsVCPsEntry=hwMplsVCPsEntry, hwMplsPsCfgRevertiveMode=hwMplsPsCfgRevertiveMode, hwMplsApsMismatchReason=hwMplsApsMismatchReason, hwMplsPsProtTunnelState=hwMplsPsProtTunnelState, hwMplsOamPsGroups=hwMplsOamPsGroups, hwMplsPsSwitchCondition=hwMplsPsSwitchCondition, hwMplsVCPsTNLBinding=hwMplsVCPsTNLBinding, hwMplsTeReverseLspLsrId=hwMplsTeReverseLspLsrId, hwMplsPsGroup=hwMplsPsGroup, hwMplsOamPsGroupCompliance=hwMplsOamPsGroupCompliance, hwMplsPsCfgWTR=hwMplsPsCfgWTR, hwMplsPsCfgType=hwMplsPsCfgType, hwMplsPsHoldOff=hwMplsPsHoldOff)
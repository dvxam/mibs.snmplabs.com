#
# PySNMP MIB module AcAtm (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AcAtm
# Produced by pysmi-0.3.4 at Wed May  1 11:33:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
AtmAddr, = mibBuilder.importSymbols("ATM-TC-MIB", "AtmAddr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Integer32, NotificationType, iso, ModuleIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, TimeTicks, ObjectIdentity, enterprises, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "NotificationType", "iso", "ModuleIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "TimeTicks", "ObjectIdentity", "enterprises", "MibIdentifier")
RowStatus, TextualConvention, DateAndTime, DisplayString, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DateAndTime", "DisplayString", "TAddress")
audioCodes = MibIdentifier((1, 3, 6, 1, 4, 1, 5003))
acRegistrations = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 7))
acGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 8))
acProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9))
acBoardMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10))
acAtm = ModuleIdentity((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6))
acAtm.setRevisions(('2003-10-16 00:00', '2006-03-21 10:48',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acAtm.setRevisionsDescriptions(('Initial version for acAtm mib ', 'Addition new table - remote gateway into the mib ',))
if mibBuilder.loadTexts: acAtm.setLastUpdated('200603211048Z')
if mibBuilder.loadTexts: acAtm.setOrganization('AudioCodes Ltd')
if mibBuilder.loadTexts: acAtm.setContactInfo('Postal: Support AudioCodes LTD 1 Hayarden Street Airport City Lod, ISRAEL 70151 Tel: 972-3-9764000 Fax: 972-3-9764040 Email: support@audiocodes.com Web: www.audiocodes.com')
if mibBuilder.loadTexts: acAtm.setDescription('The Audiocodes ATMMIB.')
acAtmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1))
atmGeneralParams = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 1))
atmGeneralParamsAtmDefaultApplicationType = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("aal1", 1), ("aal2-i-366-2", 2), ("aal2-umts", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmGeneralParamsAtmDefaultApplicationType.setStatus('current')
if mibBuilder.loadTexts: atmGeneralParamsAtmDefaultApplicationType.setDescription('This is the default application type used when the board cannot determine from the H248 add message which AAL type to use.')
atmGeneralParamsAtmTransmissionMode = MibScalar((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("sdh", 0), ("sonet", 1), ("none", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmGeneralParamsAtmTransmissionMode.setStatus('current')
if mibBuilder.loadTexts: atmGeneralParamsAtmTransmissionMode.setDescription('This is the ATM Port Optical Carrier type which indicates whether the European standard (SDH) is to be employed or the North American Standard (SONET)')
atmPort = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2))
atmPortTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1), )
if mibBuilder.loadTexts: atmPortTable.setStatus('current')
if mibBuilder.loadTexts: atmPortTable.setDescription('This table indicates general information about and alarm status of the ATM optical fiber ports. It is also used to configure the ATM address associated with the optical port and read that address.')
atmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1), ).setIndexNames((0, "AcAtm", "atmPortNumber"))
if mibBuilder.loadTexts: atmPortEntry.setStatus('current')
if mibBuilder.loadTexts: atmPortEntry.setDescription('')
atmPortAdministrativeState = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("shuttingDown", 1), ("unlocked", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortAdministrativeState.setStatus('current')
if mibBuilder.loadTexts: atmPortAdministrativeState.setDescription('This is the ATM Port Administrative State')
atmPortOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortOperationalState.setStatus('current')
if mibBuilder.loadTexts: atmPortOperationalState.setDescription('This is the Port Operational State')
atmPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("port0", 0), ("port1", 1), ("port2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortNumber.setStatus('current')
if mibBuilder.loadTexts: atmPortNumber.setDescription('This is the ATM Port Number')
atmPortAdminAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 4), AtmAddr().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortAdminAddress.setStatus('current')
if mibBuilder.loadTexts: atmPortAdminAddress.setDescription('This is the AdministrativeATM Port Address (20 octets in length - 40 hexadecimal characters). This address is manually configured.This address is used when ILMI is not available.')
atmPortOperationalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 5), AtmAddr().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortOperationalAddress.setStatus('current')
if mibBuilder.loadTexts: atmPortOperationalAddress.setDescription('This is the port ATM address currently in operation (i.e.:assigned to this port). This addressis set to atmPortAdminAddress if no ILMI address is registered. If an ILMI address is successfully registered, then atmPortOperationalAddress will be set to the ILMI one, though an administrative address may have already been configured. Thus ILMI address always takes precedence over the administrative one. If both the administrative and ILMI addresses are unavailable then the operational address is left empty. Refer to atmPortAddressMode for which address is operational.')
atmPortAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("cleared", 0), ("los", 1), ("ais", 2), ("rdi", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: atmPortAlarmStatus.setDescription('This is the ATM Port Alarm Status. The possible values are: cleared(0) - LOS, AIS and RDI conditions are not present los(1) - the LOS condition is present ais(2) - AIS condition is present (LOS condition is not present) rdi(4) - RDI condition is present (LOS and AIS conditions are not present) Note: Alarm conditions (from the SONET/SDH standard documents) are: LOS - Loss Of Signal AIS - Alarm Indication Signal RDI - Remote Defect Indication')
atmPortAddressMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("addrModeNone", 0), ("addrModeManual", 1), ("addrModeILMI", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortAddressMode.setStatus('current')
if mibBuilder.loadTexts: atmPortAddressMode.setDescription('The mode reflects the type of address in operation. addrModeNone(0) : No administrative address has been configured and no ILMI address has been registered. Thus no address is available to assign to the port. addrModeManual(1): An Administrative address has been configured and no ILMI address has been registered. Thus the port is assigned the manually configured address.addrModeILMI (2): An ILMI address has been registered. The port is assigned this address. The administrative address is ignored if it has been configured.')
atmRemoteGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3))
atmRemoteGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1), )
if mibBuilder.loadTexts: atmRemoteGatewayTable.setStatus('current')
if mibBuilder.loadTexts: atmRemoteGatewayTable.setDescription('This includes the destination remote Gateways (and RNC) that the Media Gateway would have signaling contact with.')
atmRemoteGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1), ).setIndexNames((0, "AcAtm", "atmRemoteGatewayIndex"))
if mibBuilder.loadTexts: atmRemoteGatewayEntry.setStatus('current')
if mibBuilder.loadTexts: atmRemoteGatewayEntry.setDescription('')
atmRemoteGatewayRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmRemoteGatewayRowStatus.setStatus('current')
if mibBuilder.loadTexts: atmRemoteGatewayRowStatus.setDescription('The RowStatus textual convention is used to manage the creation and deletion and active of conceptual rows.')
atmRemoteGatewayAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmRemoteGatewayAction.setStatus('current')
if mibBuilder.loadTexts: atmRemoteGatewayAction.setDescription('Development Pending -for future use')
atmRemoteGatewayActionResult = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmRemoteGatewayActionResult.setStatus('current')
if mibBuilder.loadTexts: atmRemoteGatewayActionResult.setDescription('Development Pending -future use')
atmRemoteGatewayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmRemoteGatewayIndex.setStatus('current')
if mibBuilder.loadTexts: atmRemoteGatewayIndex.setDescription('.')
atmRemoteGatewayName = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmRemoteGatewayName.setStatus('current')
if mibBuilder.loadTexts: atmRemoteGatewayName.setDescription('Remote Gateway name ')
atmRemoteGatewayNSAPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 6), AtmAddr().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmRemoteGatewayNSAPAddress.setStatus('current')
if mibBuilder.loadTexts: atmRemoteGatewayNSAPAddress.setDescription('This is the ATM Address associated with the remote Gateway to which this PVC connects (20 octets in length - 40 hexadecimal characters)')
atmRemoteGatewayALCAPInstanceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmRemoteGatewayALCAPInstanceNum.setStatus('current')
if mibBuilder.loadTexts: atmRemoteGatewayALCAPInstanceNum.setDescription('ALCAP Instance number associated with the remote Gateway ( 3G only)')
aal2PVC = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4))
aal2PVCTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1), )
if mibBuilder.loadTexts: aal2PVCTable.setStatus('current')
if mibBuilder.loadTexts: aal2PVCTable.setDescription('This table contains information referring to Permanent Virtual Channels connecting the AMS to the ATM Edge Switch.')
aal2PVCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1), ).setIndexNames((0, "AcAtm", "aal2PVCRemoteGatewayIndex"), (0, "AcAtm", "aal2PVCVCCIPATHID"))
if mibBuilder.loadTexts: aal2PVCEntry.setStatus('current')
if mibBuilder.loadTexts: aal2PVCEntry.setDescription('')
aal2PVCRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2PVCRowStatus.setStatus('current')
if mibBuilder.loadTexts: aal2PVCRowStatus.setDescription('The RowStatus textual convention is used to manage the creation and deletion and active of conceptual rows.')
aal2PVCAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("none", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2PVCAction.setStatus('current')
if mibBuilder.loadTexts: aal2PVCAction.setDescription('Development Pending - for future use')
aal2PVCActionResult = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("none", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2PVCActionResult.setStatus('current')
if mibBuilder.loadTexts: aal2PVCActionResult.setDescription('Development Pending - for future use')
aal2PVCRemoteGatewayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCRemoteGatewayIndex.setStatus('current')
if mibBuilder.loadTexts: aal2PVCRemoteGatewayIndex.setDescription('This is the gw index that associated with the remote Gateway table to which this PVC connects (20 octets in length - 40 hexadecimal characters)')
aal2PVCVCCIPATHID = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCVCCIPATHID.setStatus('current')
if mibBuilder.loadTexts: aal2PVCVCCIPATHID.setDescription('This is the range of Virtual Connection Channel Identifiers which is an end to end identifier for an AAL2 VC.')
aal2PVCPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("port0", 0), ("port1", 1), ("port2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCPortNumber.setStatus('current')
if mibBuilder.loadTexts: aal2PVCPortNumber.setDescription('This is the port number associated with the PVC')
aal2PVCVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCVpi.setStatus('current')
if mibBuilder.loadTexts: aal2PVCVpi.setDescription('This is the VPI assigned to the PVC')
aal2PVCVci = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCVci.setStatus('current')
if mibBuilder.loadTexts: aal2PVCVci.setDescription('This is the VCI assigned to the PVC')
aal2PVCMaxNumOfCid = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 248))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCMaxNumOfCid.setStatus('current')
if mibBuilder.loadTexts: aal2PVCMaxNumOfCid.setDescription('This is the maximum number of CIDs for the AAL2 PVC.')
aal2PVCNumOfCidInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 248))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2PVCNumOfCidInUse.setStatus('current')
if mibBuilder.loadTexts: aal2PVCNumOfCidInUse.setDescription('This is the number of CIDs for AAL2 PVC currently in use.')
aal2PVCServiceCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cbr", 1), ("rtVbr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCServiceCategory.setStatus('current')
if mibBuilder.loadTexts: aal2PVCServiceCategory.setDescription('This is the Service Category which is either CBR (Constant Bit Rate) or rtVBR (realtime Variable Bit Rate)')
aal2PVCPCR = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 49600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCPCR.setStatus('current')
if mibBuilder.loadTexts: aal2PVCPCR.setDescription('This is the peak cell rate (PCR) associated with the provisioned virtual channel (PVC). Includes bandwidth for all CIDs within the PVC')
aal2PVCSCR = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 49600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCSCR.setStatus('current')
if mibBuilder.loadTexts: aal2PVCSCR.setDescription('This is the sustained cell rate (SCR) associated with the provisioned virtual channel (PVC). Includes bandwidth for all CIDs within the PVC.')
aal2PVCMBS = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 4, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2PVCMBS.setStatus('current')
if mibBuilder.loadTexts: aal2PVCMBS.setDescription('This is the Maximum Burst Size (MBS) for the provisioned virtual channel (PVC).')
atmPortLoopbackConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5))
atmPortLoopbackConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1), )
if mibBuilder.loadTexts: atmPortLoopbackConfigTable.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigTable.setDescription('This table gives the Loopback Configuration associated with a given Optical Fiber Port number.')
atmPortLoopbackConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1), ).setIndexNames((0, "AcAtm", "atmPortLoopbackConfigPortNumber"))
if mibBuilder.loadTexts: atmPortLoopbackConfigEntry.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigEntry.setDescription('')
atmPortLoopbackConfigIsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigIsUsed.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigIsUsed.setDescription('This tells whether or not the port loopback is used. If the port is available on the board, this is yes.')
atmPortLoopbackConfigAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("none", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortLoopbackConfigAction.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigAction.setDescription('Development Pending - for future use')
atmPortLoopbackConfigActionResult = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("none", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortLoopbackConfigActionResult.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigActionResult.setDescription('Development Pending - for future use')
atmPortLoopbackConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("port0", 0), ("port1", 1), ("port2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigPortNumber.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigPortNumber.setDescription('The port number associated with the optical port which is being described. ')
atmPortLoopbackConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("uni", 1), ("vp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigMode.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigMode.setDescription('This is the mode in which the loopback will work: no loopback, UNI loopback, or Virtual Path loopback')
atmPortLoopbackConfigOutBoundVirtualPath = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigOutBoundVirtualPath.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigOutBoundVirtualPath.setDescription('If the atmLoopback mode is VP, this specifies the VP identity for the cells going toward the ATM edge switch')
atmPortLoopbackConfigInBoundVirtualPath = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigInBoundVirtualPath.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigInBoundVirtualPath.setDescription('If the atmLoopback mode is VP, this specifies the VP identity for the cells coming from the ATM edge switch')
atmPortLoopbackConfigVciRangeFirst = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(33, 2047))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigVciRangeFirst.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigVciRangeFirst.setDescription('If the atmLoopback mode is VP, this specifies the minimum VCI within the inbound and outbound VP which may be used.')
atmPortLoopbackConfigVciRangeLast = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(33, 2047))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigVciRangeLast.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigVciRangeLast.setDescription('If the atmLoopback mode is VP, this specifies the maximum VCI within the inbound and outbound VP which may be used.')
atmPortLoopbackConfigServiceCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cbr", 1), ("rtVbr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigServiceCategory.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigServiceCategory.setDescription('This category is limited to Constant Bit Rate (CBR) traffic or realtime Variable Bit Rate (rtVBR) for this release.')
atmPortLoopbackConfigPCR = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(171, 59600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigPCR.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigPCR.setDescription('This is the peak cell rate (PCR) associated with the switched virtual channel (SVC). This is used for Constant Bit Rate (CBR) traffic. For AAL2, this includes bandwidth for all CIDs within the SVC. For AAL1, there is only one channel per SVC (and no concept of a CID).')
atmPortLoopbackConfigSCR = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(171, 59600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigSCR.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigSCR.setDescription('This is the sustained cell rate (SCR) associated with the switched virtual channel (SVC). This is used for realtime Variable Bit Rate (rtVBR) traffice. For AAL2, this includes bandwidth for all CIDs within the SVC. For AAL1, there is only one channel per SVC (and no concept of a CID).')
atmPortLoopbackConfigMBS = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopbackConfigMBS.setStatus('current')
if mibBuilder.loadTexts: atmPortLoopbackConfigMBS.setDescription('This is the Maximum Burst Size (MBS) associated with the switched virtual channel (SVC). This is used in realtime Variable Bit Rate (rtVBR) traffice. The unit for this parameter is ATM cells.')
atmSvcProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6))
atmSvcProfileTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1), )
if mibBuilder.loadTexts: atmSvcProfileTable.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfileTable.setDescription('This table indicates information about profiles associated with the creation of each new AAL2 SVC.')
atmSvcProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1), ).setIndexNames((0, "AcAtm", "atmSvcProfileIndex"))
if mibBuilder.loadTexts: atmSvcProfileEntry.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfileEntry.setDescription('')
atmSvcProfileIsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcProfileIsUsed.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfileIsUsed.setDescription('This tells whether or not this SVC profile is used. If it is used, the value is yes.')
atmSvcProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 550))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcProfileIndex.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfileIndex.setDescription('Initially only one SVC Profile is supported. This parameter may be updated later as the table supports more profiles')
atmSvcProfileMaxNumOfCids = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 248))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcProfileMaxNumOfCids.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfileMaxNumOfCids.setDescription('The CIDs fall in the range of 8 to 255, so there are a maximum of 248 CIDs possible. The assignment of CID #8 may be received but not initiated. Assignments from the low end of the CID range should start with 9 as there are some vendors who use 8 for a special OAM purpose.')
atmSvcProfilePCR = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(171, 59600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcProfilePCR.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfilePCR.setDescription('This is the peak cell rate (PCR) associated with the switched virtual channel (SVC). This is used for Constant Bit Rate (CBR) traffic. For AAL2, this includes bandwidth for all CIDs within the SVC. For AAL1, there is only one channel per SVC (and no concept of a CID).')
atmSvcProfileSCR = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(171, 59600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcProfileSCR.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfileSCR.setDescription('This is the sustained cell rate (SCR) associated with the switched virtual channel (SVC). This is used for realtime Variable Bit Rate (rtVBR) traffice. For AAL2, this includes bandwidth for all CIDs within the SVC. For AAL1, there is only one channel per SVC (and no concept of a CID).')
atmSvcProfileMBS = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcProfileMBS.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfileMBS.setDescription('This is the Maximum Burst Size (MBS) associated with the switched virtual channel (SVC). This is used in realtime Variable Bit Rate (rtVBR) traffice. The unit for this parameter is ATM cells.')
atmSvcProfilePersistence = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcProfilePersistence.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfilePersistence.setDescription('This is the parameter which descirbes how long an AAL2 SVC will persist even when no CIDs are in use. Generally, this is on the order of 180 to 600 seconds. Non-persistent SVCs should have a value of 0.')
atmSvcProfileServiceCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 1, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cbr", 1), ("rtVbr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcProfileServiceCategory.setStatus('current')
if mibBuilder.loadTexts: atmSvcProfileServiceCategory.setDescription('This category is limited to Constant Bit Rate (CBR) traffic or realtime Variable Bit Rate (rtVBR) for this release.')
acAtmStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2))
atmSvcConnection = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1))
atmSvcConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1), )
if mibBuilder.loadTexts: atmSvcConnectionTable.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionTable.setDescription('This is the table which describes the read only characteristics of a given AAL1 or AAL2 SVC.')
atmSvcConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1), ).setIndexNames((0, "AcAtm", "atmSvcConnectionIndex"))
if mibBuilder.loadTexts: atmSvcConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionEntry.setDescription('')
atmSvcConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionIndex.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionIndex.setDescription('A unique index, that identifies the SVC on the system.')
atmSvcConnectionRemoteGatewayAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 2), AtmAddr().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionRemoteGatewayAddress.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionRemoteGatewayAddress.setDescription('This is the ATM Address associated with the remote Gateway to which this SVC connects (20 octets in length - 40 hexadecimal characters)')
atmSvcConnectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("port0", 0), ("port1", 1), ("port2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionPort.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionPort.setDescription('This is the port on which the SVC is connected')
atmSvcConnectionVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionVpi.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionVpi.setDescription('This is the VPI associated with the SVC')
atmSvcConnectionVci = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionVci.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionVci.setDescription('This is the VCI associated with the SVC')
atmSvcConnectionAALType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aal1", 1), ("aal2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionAALType.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionAALType.setDescription('This is the Adaptation Layer type. It is either AAL1 or AAL2.')
atmSvcConnectionDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("incoming", 0), ("outgoing", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionDirection.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionDirection.setDescription('This is the direction in which the SVC was setup. Incoming means the this end received the SETUP. Outgoing means this end sent the SETUP.')
atmSvcConnectionEecid = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionEecid.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionEecid.setDescription('This is the unique end to end identifier associated with the setup of AAL1 SVCs')
atmSvcConnectionVcci = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionVcci.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionVcci.setDescription('This is the unique identity of an SVC associated with an AAL2 connection')
atmSvcConnectionMaxNumOfCid = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 248))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionMaxNumOfCid.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionMaxNumOfCid.setDescription('This is the maximum number of CIDs for an AAL2 SVC.')
atmSvcConnectionNumOfCidInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 6, 2, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 248))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcConnectionNumOfCidInUse.setStatus('current')
if mibBuilder.loadTexts: atmSvcConnectionNumOfCidInUse.setDescription('This is the number of channel Ids currently in use in a given SVC.')
mibBuilder.exportSymbols("AcAtm", atmSvcConnectionVci=atmSvcConnectionVci, atmPortLoopbackConfigEntry=atmPortLoopbackConfigEntry, atmSvcConnectionEecid=atmSvcConnectionEecid, atmPortAddressMode=atmPortAddressMode, atmSvcConnectionNumOfCidInUse=atmSvcConnectionNumOfCidInUse, atmPortLoopbackConfigVciRangeFirst=atmPortLoopbackConfigVciRangeFirst, atmPortAlarmStatus=atmPortAlarmStatus, atmRemoteGatewayActionResult=atmRemoteGatewayActionResult, atmSvcConnectionVpi=atmSvcConnectionVpi, aal2PVC=aal2PVC, aal2PVCPCR=aal2PVCPCR, atmSvcProfileIndex=atmSvcProfileIndex, atmSvcProfile=atmSvcProfile, atmSvcProfileIsUsed=atmSvcProfileIsUsed, atmSvcConnectionTable=atmSvcConnectionTable, atmPortOperationalAddress=atmPortOperationalAddress, aal2PVCEntry=aal2PVCEntry, atmSvcConnectionIndex=atmSvcConnectionIndex, acAtmStatus=acAtmStatus, atmSvcProfilePersistence=atmSvcProfilePersistence, atmSvcConnectionMaxNumOfCid=atmSvcConnectionMaxNumOfCid, atmRemoteGatewayAction=atmRemoteGatewayAction, atmPortLoopbackConfigPortNumber=atmPortLoopbackConfigPortNumber, audioCodes=audioCodes, atmPortTable=atmPortTable, aal2PVCSCR=aal2PVCSCR, atmSvcConnection=atmSvcConnection, aal2PVCRowStatus=aal2PVCRowStatus, atmRemoteGatewayTable=atmRemoteGatewayTable, acProducts=acProducts, acAtm=acAtm, atmRemoteGatewayNSAPAddress=atmRemoteGatewayNSAPAddress, atmPortLoopbackConfig=atmPortLoopbackConfig, atmSvcProfileServiceCategory=atmSvcProfileServiceCategory, acRegistrations=acRegistrations, atmPortLoopbackConfigInBoundVirtualPath=atmPortLoopbackConfigInBoundVirtualPath, atmSvcConnectionEntry=atmSvcConnectionEntry, acGeneric=acGeneric, aal2PVCServiceCategory=aal2PVCServiceCategory, atmPortLoopbackConfigVciRangeLast=atmPortLoopbackConfigVciRangeLast, aal2PVCVci=aal2PVCVci, atmSvcProfileMBS=atmSvcProfileMBS, atmPortLoopbackConfigOutBoundVirtualPath=atmPortLoopbackConfigOutBoundVirtualPath, aal2PVCActionResult=aal2PVCActionResult, atmPortLoopbackConfigSCR=atmPortLoopbackConfigSCR, atmRemoteGatewayEntry=atmRemoteGatewayEntry, aal2PVCTable=aal2PVCTable, atmPortLoopbackConfigMBS=atmPortLoopbackConfigMBS, atmSvcConnectionVcci=atmSvcConnectionVcci, atmPortLoopbackConfigMode=atmPortLoopbackConfigMode, atmGeneralParams=atmGeneralParams, atmSvcConnectionDirection=atmSvcConnectionDirection, atmPortAdministrativeState=atmPortAdministrativeState, aal2PVCRemoteGatewayIndex=aal2PVCRemoteGatewayIndex, atmSvcProfilePCR=atmSvcProfilePCR, atmPortOperationalState=atmPortOperationalState, atmGeneralParamsAtmTransmissionMode=atmGeneralParamsAtmTransmissionMode, atmGeneralParamsAtmDefaultApplicationType=atmGeneralParamsAtmDefaultApplicationType, atmSvcConnectionRemoteGatewayAddress=atmSvcConnectionRemoteGatewayAddress, atmPortLoopbackConfigPCR=atmPortLoopbackConfigPCR, atmSvcConnectionPort=atmSvcConnectionPort, aal2PVCAction=aal2PVCAction, atmRemoteGatewayName=atmRemoteGatewayName, atmPortLoopbackConfigActionResult=atmPortLoopbackConfigActionResult, atmPortEntry=atmPortEntry, atmRemoteGatewayALCAPInstanceNum=atmRemoteGatewayALCAPInstanceNum, aal2PVCMBS=aal2PVCMBS, atmRemoteGatewayRowStatus=atmRemoteGatewayRowStatus, aal2PVCNumOfCidInUse=aal2PVCNumOfCidInUse, atmPortAdminAddress=atmPortAdminAddress, atmPort=atmPort, atmSvcProfileSCR=atmSvcProfileSCR, atmRemoteGatewayIndex=atmRemoteGatewayIndex, atmSvcProfileEntry=atmSvcProfileEntry, atmSvcConnectionAALType=atmSvcConnectionAALType, acAtmConfiguration=acAtmConfiguration, atmPortLoopbackConfigAction=atmPortLoopbackConfigAction, atmSvcProfileMaxNumOfCids=atmSvcProfileMaxNumOfCids, atmPortLoopbackConfigServiceCategory=atmPortLoopbackConfigServiceCategory, PYSNMP_MODULE_ID=acAtm, atmPortLoopbackConfigTable=atmPortLoopbackConfigTable, aal2PVCVpi=aal2PVCVpi, atmPortNumber=atmPortNumber, aal2PVCVCCIPATHID=aal2PVCVCCIPATHID, acBoardMibs=acBoardMibs, atmSvcProfileTable=atmSvcProfileTable, aal2PVCMaxNumOfCid=aal2PVCMaxNumOfCid, atmRemoteGateway=atmRemoteGateway, atmPortLoopbackConfigIsUsed=atmPortLoopbackConfigIsUsed, aal2PVCPortNumber=aal2PVCPortNumber)
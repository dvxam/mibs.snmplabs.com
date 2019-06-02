#
# PySNMP MIB module Nortel-Magellan-Passport-HuntGroupMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-HuntGroupMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:27:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
StorageType, DisplayString, Counter32, Integer32, Unsigned32, RowStatus = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "StorageType", "DisplayString", "Counter32", "Integer32", "Unsigned32", "RowStatus")
Link, AsciiString = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "Link", "AsciiString")
components, passportMIBs = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "components", "passportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity, IpAddress, Counter32, Integer32, Counter64, Unsigned32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity", "IpAddress", "Counter32", "Integer32", "Counter64", "Unsigned32", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
huntGroupMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130))
hg = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131))
hgRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1), )
if mibBuilder.loadTexts: hgRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgRowStatusTable.setDescription('This entry controls the addition and deletion of hg components.')
hgRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"))
if mibBuilder.loadTexts: hgRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgRowStatusEntry.setDescription('A single entry in the table represents a single hg component.')
hgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: hgRowStatus.setDescription('This variable is used as the basis for SNMP naming of hg components. These components can be added and deleted.')
hgComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: hgComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
hgStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: hgStorageType.setDescription('This variable represents the storage type value for the hg tables.')
hgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hgIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hgIndex.setDescription('This variable represents the index for the hg tables.')
hgCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 10), )
if mibBuilder.loadTexts: hgCidDataTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgCidDataTable.setDescription("This group contains the attribute for a component's Customer Identifier (CID). Refer to the attribute description for a detailed explanation of CIDs.")
hgCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"))
if mibBuilder.loadTexts: hgCidDataEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgCidDataEntry.setDescription('An entry in the hgCidDataTable.')
hgCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgCustomerIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: hgCustomerIdentifier.setDescription("This attribute holds the Customer Identifier (CID). Every component has a CID. If a component has a cid attribute, the component's CID is the provisioned value of that attribute; otherwise the component inherits the CID of its parent. The top- level component has a CID of 0. Every operator session also has a CID, which is the CID provisioned for the operator's user ID. An operator will see only the stream data for components having a matching CID. Also, the operator will be allowed to issue commands for only those components which have a matching CID. An operator CID of 0 is used to identify the Network Manager (referred to as 'NetMan' in DPN). This CID matches the CID of any component. Values 1 to 8191 inclusive (equivalent to 'basic CIDs' in DPN) may be assigned to specific customers.")
hgNsapAddressTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 11), )
if mibBuilder.loadTexts: hgNsapAddressTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgNsapAddressTable.setDescription('This group contains attributes common to all NSAP format addresses.')
hgNsapAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"))
if mibBuilder.loadTexts: hgNsapAddressEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgNsapAddressEntry.setDescription('An entry in the hgNsapAddressTable.')
hgAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgAddress.setStatus('mandatory')
if mibBuilder.loadTexts: hgAddress.setDescription('The address attribute specifies the numbering plan and digits which form a unique DNA identifier of the hunt group. The format of the address attribute is <numberingPlan>.<digits> where numbering plan is x for X.121 and e for E.164. An example X.121 address is x.12345678.')
hgProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12), )
if mibBuilder.loadTexts: hgProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgProvTable.setDescription('The Provisioned group contains the provisioned attributes of the hunt group.')
hgProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"))
if mibBuilder.loadTexts: hgProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgProvEntry.setDescription('An entry in the hgProvTable.')
hgLogicalProcessor = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgLogicalProcessor.setStatus('mandatory')
if mibBuilder.loadTexts: hgLogicalProcessor.setDescription('This attribute specifies the logical processor on which the hunt group process will execute. The Lp/n Eng Hgs component contains statistics for all hunt groups on the LP.')
hgSelectionPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("startFromZero", 0), ("rotary", 1), ("mostAvailable", 2))).clone('mostAvailable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgSelectionPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: hgSelectionPolicy.setDescription('The selectionPolicy attribute specifies the algorithm used to select a hunt group member. A value of startFromZero means that on a new call, the first available member starting from the member with the lowest instance value is selected. Subsequent hunts for the same call select the first available member starting from the previously chosen member. This algorithm is used when it is desirable to have the first member receive the majority of the calls and subsequent members only receive calls in overflow situations. A value of rotary means that on a new call, the first available member is selected starting from the member which received the last new call. Subsequent hunts for the same call select the first available member starting from the previously chosen member. This algorithm is used when it is desirable to loadspread the calls equally across the members. A value of mostAvailable means that on a new call, the most available member is selected based on the availability information received from the member. Subsequent hunts for the same call select the most available member starting from the previously chosen member. This algorithm is used when it is desirable to send each call to the member which has the highest probability of connecting it.')
hgMaxHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 63)).clone(63)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgMaxHuntAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: hgMaxHuntAttempts.setDescription('The maxHuntAttempts attribute specifies the maximum attempts allowed to hunt the call. Hunting ceases if either this maximum is exceeded or the member list is exhausted.')
hgAppendSuffixDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1))).clone('yes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgAppendSuffixDigits.setStatus('mandatory')
if mibBuilder.loadTexts: hgAppendSuffixDigits.setDescription('The appendSuffixDigits attribute specifies how suffix called address digits are handled. Suffix called address digits are any trailing digits, signalled in a call, beyond the provisioned hunt group address. If this attribute is set to yes, suffix digits are appended to the member address before the call is forwarded to the member. If it is set to no, suffix digits are not appended to the member address.')
hgStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20), )
if mibBuilder.loadTexts: hgStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
hgStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"))
if mibBuilder.loadTexts: hgStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgStateEntry.setDescription('An entry in the hgStateTable.')
hgAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: hgAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
hgOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: hgOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
hgUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: hgUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
hgOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21), )
if mibBuilder.loadTexts: hgOperationalTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgOperationalTable.setDescription('The Operational group contains the operational attributes of the hunt group.')
hgOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"))
if mibBuilder.loadTexts: hgOperationalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgOperationalEntry.setDescription('An entry in the hgOperationalTable.')
hgHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgHuntAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: hgHuntAttempts.setDescription('This attribute counts the total number of hunt attempts made by the hunt group. The count includes both initial and subsequent hunt attempts. This count is contained within the huntAttempts attribute of the Lp/n Eng Hgs component. This counter wraps to 0 when it exceeds its maximum value.')
hgFailedCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgFailedCalls.setStatus('mandatory')
if mibBuilder.loadTexts: hgFailedCalls.setDescription('This attribute counts the number of calls which could not be connected by any of the hunt group members. This could occur if the hunt group is locked or has exhausted its member list. If a call cannot be connected by the hunt group it is sent to call redirection. This counter wraps to 0 when it exceeds its maximum value.')
hgInitialHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgInitialHuntAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: hgInitialHuntAttempts.setDescription('This attribute counts the number of new (non-hunted) calls received by the hunt group which are forwarded to a member. This counter wraps to 0 when it exceeds its maximum value.')
hgAvailabilityUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgAvailabilityUpdates.setStatus('mandatory')
if mibBuilder.loadTexts: hgAvailabilityUpdates.setDescription('This attribute counts the number of availability update packets received by the hunt group from its members. This counter wraps to 0 when it exceeds its maximum value.')
hgMaxAddrLenExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgMaxAddrLenExceeded.setStatus('mandatory')
if mibBuilder.loadTexts: hgMaxAddrLenExceeded.setDescription('This attribute counts the number of times a member could not be selected to receive a call with suffix address digits because its DNA length would exceed the maximum of 14 digits with the suffix digits appended. This counter wraps to 0 when it exceeds its maximum value.')
hgBadPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgBadPackets.setStatus('mandatory')
if mibBuilder.loadTexts: hgBadPackets.setDescription('This attribute counts the number of unrecognizable packets received by the hunt group and discarded. This counter wraps to 0 when it exceeds its maximum value.')
hgHgM = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2))
hgHgMRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1), )
if mibBuilder.loadTexts: hgHgMRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMRowStatusTable.setDescription('This entry controls the addition and deletion of hgHgM components.')
hgHgMRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"), (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgHgMIndex"))
if mibBuilder.loadTexts: hgHgMRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMRowStatusEntry.setDescription('A single entry in the table represents a single hgHgM component.')
hgHgMRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgHgMRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMRowStatus.setDescription('This variable is used as the basis for SNMP naming of hgHgM components. These components can be added and deleted.')
hgHgMComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgHgMComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
hgHgMStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgHgMStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMStorageType.setDescription('This variable represents the storage type value for the hgHgM tables.')
hgHgMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63)))
if mibBuilder.loadTexts: hgHgMIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMIndex.setDescription('This variable represents the index for the hgHgM tables.')
hgHgMProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 10), )
if mibBuilder.loadTexts: hgHgMProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMProvTable.setDescription('The Provisioned group contains the provisioned attributes of the hunt group member.')
hgHgMProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"), (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgHgMIndex"))
if mibBuilder.loadTexts: hgHgMProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMProvEntry.setDescription('An entry in the hgHgMProvTable.')
hgHgMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 10, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgHgMAddress.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMAddress.setDescription('The address attribute specifies the numbering plan and digits which form a unique DNA identifier of the hunt group member. The format of the address attribute is <numberingPlan>.<digits> where numbering plan is x for X.121 and e for E.164. An example X.121 address is x.12345678.')
hgHgMStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11), )
if mibBuilder.loadTexts: hgHgMStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
hgHgMStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"), (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgHgMIndex"))
if mibBuilder.loadTexts: hgHgMStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMStateEntry.setDescription('An entry in the hgHgMStateTable.')
hgHgMAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgHgMAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
hgHgMOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgHgMOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
hgHgMUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgHgMUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
hgHgMOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12), )
if mibBuilder.loadTexts: hgHgMOperationalTable.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMOperationalTable.setDescription('The Operational group defines operational attributes associated with the HuntGroupMember component.')
hgHgMOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"), (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgHgMIndex"))
if mibBuilder.loadTexts: hgHgMOperationalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMOperationalEntry.setDescription('An entry in the hgHgMOperationalTable.')
hgHgMAvailability = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)).clone(4095)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hgHgMAvailability.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMAvailability.setDescription("This attribute indicates the current availability of the member. The higher the value, the more available the member is perceived to be. A value of 0 indicates the member is unavailable. A member must be considered 'available' by the hunt group in order to receive a call, regardless of the selection policy in use. The hunt group members report whether or not they are available to receive calls to the hunt group. Some services base their availability on unused logical channels, others on bandwidth or memory capacity. During initialization, the hunt group assumes all of its members are equally available and sets their availability value to the maximum of 4095. Similarly, a new hunt group member added to an existing hunt group has its availability value initialized to 4095. This ensures that members which have not reported their availability to the hunt group are tried in order to trigger the member to report its true availability. The availability of a member can change in the following ways: - Hunt group members can report their availability to the hunt group using a DPRS availability packet. - A network operator can temporarily change the value by the Set command. This change remains in effect until changed again by any of these ways. - The hunt group resets a member's availability to the maximum of 4095 if it has been 0 for at least 2.5 hours. This ensures that 'lost' availability information does not prevent a member from returning to service.")
hgHgMAvailabilityUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgHgMAvailabilityUpdates.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMAvailabilityUpdates.setDescription('This attribute counts the number of availability update packets received by the hunt group member. This counter wraps to 0 when it exceeds its maximum value.')
hgHgMCallsRefused = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hgHgMCallsRefused.setStatus('mandatory')
if mibBuilder.loadTexts: hgHgMCallsRefused.setDescription("This attribute counts the number of call packets which were returned to the hunt group by the member because it could not connect the call. If this counter increments frequently, it could indicate a problem with the member's reporting of its availability to the hunt group or an incompatibility in the call options. This counter wraps to 0 when it exceeds its maximum value.")
huntGroupGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 1))
huntGroupGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 1, 5))
huntGroupGroupBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 1, 5, 2))
huntGroupGroupBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 1, 5, 2, 2))
huntGroupCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 3))
huntGroupCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 3, 5))
huntGroupCapabilitiesBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 3, 5, 2))
huntGroupCapabilitiesBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 3, 5, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-HuntGroupMIB", hgAvailabilityUpdates=hgAvailabilityUpdates, hgProvTable=hgProvTable, hgStateTable=hgStateTable, huntGroupCapabilities=huntGroupCapabilities, hgRowStatus=hgRowStatus, hg=hg, hgIndex=hgIndex, hgOperationalTable=hgOperationalTable, huntGroupCapabilitiesBE01=huntGroupCapabilitiesBE01, hgAdminState=hgAdminState, hgHgMProvTable=hgHgMProvTable, huntGroupGroup=huntGroupGroup, hgStateEntry=hgStateEntry, hgCustomerIdentifier=hgCustomerIdentifier, hgNsapAddressTable=hgNsapAddressTable, hgHgMRowStatusTable=hgHgMRowStatusTable, hgRowStatusTable=hgRowStatusTable, hgHgMAvailability=hgHgMAvailability, hgHgMProvEntry=hgHgMProvEntry, hgHgMStateTable=hgHgMStateTable, hgComponentName=hgComponentName, hgBadPackets=hgBadPackets, huntGroupGroupBE01A=huntGroupGroupBE01A, hgHgMStateEntry=hgHgMStateEntry, hgHgMCallsRefused=hgHgMCallsRefused, hgRowStatusEntry=hgRowStatusEntry, hgHgM=hgHgM, hgMaxAddrLenExceeded=hgMaxAddrLenExceeded, hgHgMRowStatusEntry=hgHgMRowStatusEntry, hgHgMUsageState=hgHgMUsageState, hgLogicalProcessor=hgLogicalProcessor, hgFailedCalls=hgFailedCalls, hgAppendSuffixDigits=hgAppendSuffixDigits, hgMaxHuntAttempts=hgMaxHuntAttempts, hgHgMAddress=hgHgMAddress, hgHgMOperationalTable=hgHgMOperationalTable, huntGroupGroupBE01=huntGroupGroupBE01, hgHgMAvailabilityUpdates=hgHgMAvailabilityUpdates, hgOperationalState=hgOperationalState, huntGroupCapabilitiesBE=huntGroupCapabilitiesBE, hgHgMStorageType=hgHgMStorageType, hgHgMRowStatus=hgHgMRowStatus, hgHgMOperationalEntry=hgHgMOperationalEntry, hgAddress=hgAddress, hgOperationalEntry=hgOperationalEntry, huntGroupMIB=huntGroupMIB, hgHgMComponentName=hgHgMComponentName, hgNsapAddressEntry=hgNsapAddressEntry, hgSelectionPolicy=hgSelectionPolicy, hgHgMOperationalState=hgHgMOperationalState, hgCidDataEntry=hgCidDataEntry, hgHuntAttempts=hgHuntAttempts, hgStorageType=hgStorageType, hgHgMAdminState=hgHgMAdminState, hgUsageState=hgUsageState, hgCidDataTable=hgCidDataTable, huntGroupCapabilitiesBE01A=huntGroupCapabilitiesBE01A, hgHgMIndex=hgHgMIndex, huntGroupGroupBE=huntGroupGroupBE, hgInitialHuntAttempts=hgInitialHuntAttempts, hgProvEntry=hgProvEntry)
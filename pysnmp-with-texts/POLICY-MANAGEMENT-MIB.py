#
# PySNMP MIB module POLICY-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POLICY-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:41:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ModuleIdentity, TimeTicks, ObjectIdentity, Integer32, Unsigned32, Counter64, MibIdentifier, IpAddress, iso, NotificationType, experimental, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Integer32", "Unsigned32", "Counter64", "MibIdentifier", "IpAddress", "iso", "NotificationType", "experimental", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32")
DisplayString, RowStatus, TextualConvention, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "RowPointer")
policyMgt = ModuleIdentity((1, 3, 6, 1, 3, 107))
policyMgt.setRevisions(('2000-10-11 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: policyMgt.setRevisionsDescriptions(('The original version of this MIB, published as RFCXXXX.',))
if mibBuilder.loadTexts: policyMgt.setLastUpdated('200010111500Z')
if mibBuilder.loadTexts: policyMgt.setOrganization('IETF SNMP Configuration Working Group')
if mibBuilder.loadTexts: policyMgt.setContactInfo('Steve Waldbusser Phone: +1-650-948-6500 Fax: +1-650-745-0671 Email: waldbusser@nextbeacon.com Jon Saperia JDS Consulting, Inc. 174 Chapman St. Watertown MA 02472-3063 USA Phone: +1-617-744-1079 Fax: +1-617-249-0874 Email: saperia@jdscons.com Thippanna Hongal Riverstone Networks, Inc. 5200 Great America Parkway Santa Clara, CA, 95054 USA Phone: +1-408-878-6562 Fax: +1-408-878-6501 Email: hongal@riverstonenet.com')
if mibBuilder.loadTexts: policyMgt.setDescription('The MIB module for rule-based configuration of SNMP infrastructures.')
class UTF8String(TextualConvention, OctetString):
    description = 'An octet string containing information typically in human-readable form. To facilitate internationalization, this information is represented using the ISO/IEC IS 10646-1 character set, encoded as an octet string using the UTF-8 transformation format described in [RFC2279]. Since additional code points are added by amendments to the 10646 standard from time to time, implementations must be prepared to encounter any code point from 0x00000000 to 0x7fffffff. Byte sequences that do not correspond to the valid UTF-8 encoding of a code point or are outside this range are prohibited. The use of control codes should be avoided. When it is necessary to represent a newline, the control code sequence CR LF should be used. For code points not directly supported by user interface hardware or software, an alternative means of entry and display, such as hexadecimal, may be provided. For information encoded in 7-bit US-ASCII, the UTF-8 encoding is identical to the US-ASCII encoding. UTF-8 may require multiple bytes to represent a single character / code point; thus the length of this object in octets may be different from the number of characters encoded. Similarly, size constraints refer to the number of encoded octets, not the number of characters represented by an encoding. Note that when this TC is used for an object that is used or envisioned to be used as an index, then a SIZE restriction MUST be specified so that the number of sub-identifiers for any object instance does not exceed the limit of 128, as defined by [RFC1905]. Note that the size of an UTF8String object is measured in octets, not characters.'
    status = 'current'
    displayHint = '255a'

pmPolicyTable = MibTable((1, 3, 6, 1, 3, 107, 1), )
if mibBuilder.loadTexts: pmPolicyTable.setStatus('current')
if mibBuilder.loadTexts: pmPolicyTable.setDescription('The policy table. A policy is a pairing of a policyFilter and a policyAction which is used to apply the action to a selected set of elements.')
pmPolicyEntry = MibTableRow((1, 3, 6, 1, 3, 107, 1, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"))
if mibBuilder.loadTexts: pmPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: pmPolicyEntry.setDescription('An entry in the policy table.')
pmPolicyIndex = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: pmPolicyIndex.setStatus('current')
if mibBuilder.loadTexts: pmPolicyIndex.setDescription('A unique index for this policy entry.')
pmPolicyFilter = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 2), UTF8String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyFilter.setStatus('current')
if mibBuilder.loadTexts: pmPolicyFilter.setDescription('A policyFilter is an expression which results in a boolean value which represents whether or not an element is a member of a set of elements upon which an action is to be performed. The format of this expression is the policy expression language. Filter evaluation stops immediately when any error is detected without executing the policyAction. The policyFilter is evaluated for various elements. Any element for which the policyFilter returns any nonzero value will match the filter and will have the associated policyAction executed on that element.')
pmPolicyCalendar = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 3), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyCalendar.setStatus('current')
if mibBuilder.loadTexts: pmPolicyCalendar.setDescription('A pointer to an entry in the schedTable of the Scheduling MIB [20]. This policy is active when specified by the associated schedule entry. If the value of this object is 0.0, this policy is always active.')
pmPolicyAction = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 4), UTF8String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyAction.setStatus('current')
if mibBuilder.loadTexts: pmPolicyAction.setDescription('A pmPolicyAction is an operation performed on a set of elements. The format of this expression is the policy expression language. Action evaluation stops immediately when any error is detected.')
pmPolicyFilterMaxLatency = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 5), Unsigned32()).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyFilterMaxLatency.setStatus('current')
if mibBuilder.loadTexts: pmPolicyFilterMaxLatency.setDescription('Every element under the control of this agent is re-checked periodically to see if it is under control of this policy by re-running the filter expression for this policy. This object lets the manager control the maximum amount of time that may pass before an element is re-checked. In other words, in any given interval of this duration, all elements must be re-checked. Note that it is an implementation-dependent matter as to how the policy agent schedules the checking of various elements within this interval.')
pmPolicyActionMaxLatency = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 6), Unsigned32()).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyActionMaxLatency.setStatus('current')
if mibBuilder.loadTexts: pmPolicyActionMaxLatency.setDescription("Every element that matches this policy's filter and is therefore under control of this policy will have this policy's action executed periodically to ensure that the element remains in the state dictated by the policy. This object lets the manager control the maximum amount of time that may pass before an element has the action run on it. In other words, in any given interval of this duration, all elements under control of this policy must have the action run on them. Note that it is an implementation-dependent matter as to how the policy agent schedules the policy action on various elements within this interval.")
pmPolicyPrecedence = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyPrecedence.setStatus('current')
if mibBuilder.loadTexts: pmPolicyPrecedence.setDescription('The order in which policies on the local system are evaluated. A policy with a higher precedence value will be evaluated after a policy with a lower precedence. For example, a policy with a precedence value of 999 will be evaluated after a policy with a precedence value of 998. These values must be unique on the local policy system that realizes this module. The value for a particular policy should be the same across an administrative domain, though that is not mandatory. When the local policy system performs the evaluation in the pmPolicyFilter for the policy identified by this row it will also read the pmTrackingElementToPolicyStatus object for each object returned as a result of the policy evaluation. If that object is set to modified(3), then the pmPolicyAction shall not be taken on that element. The value of precedence(4), of pmTrackingElementToPolicyStatus is an indication that when an evaluation was performed by another policy, the pmTrackingElementToPolicyStatus was found to have a value of on(1) and that policy had a higher precedence value than the policy that initially set the value of the pmTrackingElementToPolicyStatus to on(1). In this event, the pmTrackingElementToPolicyPrecedence object shall have the value of the pmPolicyIndex for the policy with the higher precedence value entered. If the policy identified by this row of the pmPolicyTable has a higher precedence value than the value found in pmTrackingElementToPolicyPrecedence then the pmPolicyAction should be performed on the element and the pmTrackingElementToPolicyPrecedence object updated with the value of the pmPolicyIndex for this policy. The only exception to these rules is when the policy that has the higher precedence value in not currently running, i.e., the schedule is off.')
pmPolicyGroup = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 8), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyGroup.setStatus('current')
if mibBuilder.loadTexts: pmPolicyGroup.setDescription('An administratively assigned string that is used to group policies. Any combination is legal, the pmPolicyGroup object does not constrain precedence. That is precedence is evaluated independent of grouping though adminstrators might group related policies together for clarity.')
pmPolicyDescription = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 9), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyDescription.setStatus('current')
if mibBuilder.loadTexts: pmPolicyDescription.setDescription('A description of this rule and its significance, typically provided by a human.')
pmPolicyMatches = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 10), Gauge32()).setUnits('elements').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyMatches.setStatus('current')
if mibBuilder.loadTexts: pmPolicyMatches.setDescription('The number of elements that are currently matched by the associated pmPolicyFilter.')
pmPolicyExecutionErrors = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 11), Counter32()).setUnits('errors').setMaxAccess("readonly")
if mibBuilder.loadTexts: pmPolicyExecutionErrors.setStatus('current')
if mibBuilder.loadTexts: pmPolicyExecutionErrors.setDescription('The number of times execution of this policy has been terminated due to run-time errors.')
pmPolicyDebugging = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyDebugging.setStatus('current')
if mibBuilder.loadTexts: pmPolicyDebugging.setDescription('The status of debugging for this policy. If this is turned on(1), log entries will be created in the pmDebuggingTable for each run-time error that is experienced by this policy.')
pmPolicyStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyStatus.setStatus('current')
if mibBuilder.loadTexts: pmPolicyStatus.setDescription('The status of this pmPolicyEntry.')
pmElementTypeRegTable = MibTable((1, 3, 6, 1, 3, 107, 2), )
if mibBuilder.loadTexts: pmElementTypeRegTable.setStatus('current')
if mibBuilder.loadTexts: pmElementTypeRegTable.setDescription('A registration table for element types managed by this system.')
pmElementTypeRegEntry = MibTableRow((1, 3, 6, 1, 3, 107, 2, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmElementTypeRegIndex"))
if mibBuilder.loadTexts: pmElementTypeRegEntry.setStatus('current')
if mibBuilder.loadTexts: pmElementTypeRegEntry.setDescription('A registration of an element type.')
pmElementTypeRegIndex = MibTableColumn((1, 3, 6, 1, 3, 107, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: pmElementTypeRegIndex.setStatus('current')
if mibBuilder.loadTexts: pmElementTypeRegIndex.setDescription('A unique index for this entry.')
pmElementTypeRegOIDPrefix = MibTableColumn((1, 3, 6, 1, 3, 107, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmElementTypeRegOIDPrefix.setStatus('current')
if mibBuilder.loadTexts: pmElementTypeRegOIDPrefix.setDescription('An OBJECT IDENTIFIER subtree under which all instances of this element type may be found. This OBJECT IDENTIFIER should be specified up to, but not including, any index objects. The agent will discover all instances in the system that are members of the specified subtree. It will then execute policy filters (and potentially policy actions) for each instance discovered. Each invocation of the policy filter will be supplied with a parameter. This is derived by taking the last N sub-identifiers from the discovered instance, where N is: X = number of sub-identifiers in pmElementTypeRegOIDPrefix Y = number of sub-identifiers in discovered instance N = Y - X ')
pmElementTypeRegName = MibTableColumn((1, 3, 6, 1, 3, 107, 2, 1, 3), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmElementTypeRegName.setStatus('current')
if mibBuilder.loadTexts: pmElementTypeRegName.setDescription('A descriptive label for this registered type.')
pmElementTypeRegRowStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmElementTypeRegRowStatus.setStatus('current')
if mibBuilder.loadTexts: pmElementTypeRegRowStatus.setDescription('The status of this registration entry.')
pmRoleESTable = MibTable((1, 3, 6, 1, 3, 107, 3), )
if mibBuilder.loadTexts: pmRoleESTable.setStatus('current')
if mibBuilder.loadTexts: pmRoleESTable.setDescription('The role string table with element as the major index.')
pmRoleESEntry = MibTableRow((1, 3, 6, 1, 3, 107, 3, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmRoleESElement"), (0, "POLICY-MANAGEMENT-MIB", "pmRoleESString"))
if mibBuilder.loadTexts: pmRoleESEntry.setStatus('current')
if mibBuilder.loadTexts: pmRoleESEntry.setDescription('A role string entry associates a role string with an individual element.')
pmRoleESElement = MibTableColumn((1, 3, 6, 1, 3, 107, 3, 1, 1), RowPointer())
if mibBuilder.loadTexts: pmRoleESElement.setStatus('current')
if mibBuilder.loadTexts: pmRoleESElement.setDescription('The element to which this role string is associated. If the agent assigns new indexes in the MIB table to represent the same underlying element (re-indexing), the agent will modify this value to contain the new index for the underlying element.')
pmRoleESString = MibTableColumn((1, 3, 6, 1, 3, 107, 3, 1, 2), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: pmRoleESString.setStatus('current')
if mibBuilder.loadTexts: pmRoleESString.setDescription('The role string that is associated with an element through this table. A role string is an administratively specified characteristic of a managed element (for example, an interface). It is a selector for policy rules, to determine the applicability of the rule to a particular managed element.')
pmRoleESStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRoleESStatus.setStatus('current')
if mibBuilder.loadTexts: pmRoleESStatus.setDescription('The status of this role string.')
pmRoleSETable = MibTable((1, 3, 6, 1, 3, 107, 4), )
if mibBuilder.loadTexts: pmRoleSETable.setStatus('current')
if mibBuilder.loadTexts: pmRoleSETable.setDescription('A read-only version of the role string table with roleString as the major index. The purpose of this table is to make it easy to retrieve all elements that share a common string.')
pmRoleSEEntry = MibTableRow((1, 3, 6, 1, 3, 107, 4, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmRoleSEString"), (0, "POLICY-MANAGEMENT-MIB", "pmRoleSEElement"))
if mibBuilder.loadTexts: pmRoleSEEntry.setStatus('current')
if mibBuilder.loadTexts: pmRoleSEEntry.setDescription('A role string entry associates a role string with an individual element.')
pmRoleSEString = MibTableColumn((1, 3, 6, 1, 3, 107, 4, 1, 1), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: pmRoleSEString.setStatus('current')
if mibBuilder.loadTexts: pmRoleSEString.setDescription('The role string that is associated with an element through this table. A role string is an administratively specified characteristic of a managed element (for example, an interface). It is a selector for policy rules, to determine the applicability of the rule to a particular managed element.')
pmRoleSEElement = MibTableColumn((1, 3, 6, 1, 3, 107, 4, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRoleSEElement.setStatus('current')
if mibBuilder.loadTexts: pmRoleSEElement.setDescription('The element to which this role string is associated. If the agent assigns new indexes in the MIB table to represent the same underlying element (re-indexing), the agent will modify this value to contain the new index for the underlying element.')
pmCapabilitiesTable = MibTable((1, 3, 6, 1, 3, 107, 5), )
if mibBuilder.loadTexts: pmCapabilitiesTable.setStatus('current')
if mibBuilder.loadTexts: pmCapabilitiesTable.setDescription('The pmCapabilitiesTable contains a description of the inherent capabilities of the system.')
pmCapabilitiesEntry = MibTableRow((1, 3, 6, 1, 3, 107, 5, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmCapabilitiesIndex"))
if mibBuilder.loadTexts: pmCapabilitiesEntry.setStatus('current')
if mibBuilder.loadTexts: pmCapabilitiesEntry.setDescription('The description of a capability or limitation of a capability of the system. An entry will exist for each domain and mechanism specific ability the system has. In the case of a domain specific capability with no mechanism specific parameters, the pmCapabilitiesSubType and all other columns may be null. Entries will exist that contain values for the pmCapabilitiesRestrictOID, pmCapabilitiesRestrictType, pmCapabilitiesRestrictValue and pmCapabilitiesRestrictString objects only when an implementation is reporting a mechanism specific restriction. Multiple entries are possible when more than one restriction for a type or subtype are needed.')
pmCapabilitiesIndex = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: pmCapabilitiesIndex.setStatus('current')
if mibBuilder.loadTexts: pmCapabilitiesIndex.setDescription('A unique index for this entry.')
pmCapabilitiesType = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesType.setStatus('current')
if mibBuilder.loadTexts: pmCapabilitiesType.setDescription('The type of the capability represented by this entry. The IANA will publish the list of identifiers that are valid values for this object.')
pmCapabilitiesSubType = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesSubType.setStatus('current')
if mibBuilder.loadTexts: pmCapabilitiesSubType.setDescription('The sub type of capability is a pointer to a mechanism specific set of capabilities supporting a base technology. In the case of DIFFSERV, the OID value here would be the base OID of the Differentiated Services Policy MIB Module.')
pmCapabilitiesModificationOID = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesModificationOID.setStatus('current')
if mibBuilder.loadTexts: pmCapabilitiesModificationOID.setDescription('The OID of the object that is either not supported, supported with one or more limitations, or expanded by an implementation specific module. If this columnar object is other than null then there must be at least an entry in pmCapabilitiesModificationType. Note that this need not be a leaf node or scalar object. If an entire table is not supported, this value can be the base OID for the table.')
pmCapabilitiesModificationType = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unsupported", 0), ("restricted", 1), ("additional", 2), ("addvalue", 3), ("maxlimit", 4), ("minlimit", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesModificationType.setStatus('current')
if mibBuilder.loadTexts: pmCapabilitiesModificationType.setDescription('An unsupported value indicates that the OID in pmCapabilitiesModificationOID is not supported on this system. A value of 1 indicates that the OID is supported but with restricted values These constraints are described in the pmCapabilitiesModificationValue and pmCapabilitiesModificationString objects. A value of 2 indicates a vendor specific extension to a standard. The OID of the new object is pmCapabilitiesModificationOID. For some implementations, additional functions may be provided. addvalue indicates that this row of the table describes an additional value that the object can take. The specific value is in the pmCapabilitiesModificationValue. The values of 4 and 5 indicate restrictions or the removal of restrictions for the object identified.')
pmCapabilitiesModificationValue = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesModificationValue.setStatus('current')
if mibBuilder.loadTexts: pmCapabilitiesModificationValue.setDescription('If the value of pmCapabilitiesModificationType is 0, this object will be null since 0 indicates no support for the object at all. A value of 1 in the pmCapabilitiesModificationType will be further modified by a single integer value in this object that corresponds to enumerated integer values that are not supported by the system for the object that is identified in this row. This value can also represent the limit values in the pmCapabilitiesModificationType object.')
pmCapabilitiesModificationString = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesModificationString.setStatus('current')
if mibBuilder.loadTexts: pmCapabilitiesModificationString.setDescription('Any additional details or description or parameters needed.')
pmTrackingPolicyToElementTable = MibTable((1, 3, 6, 1, 3, 107, 6), )
if mibBuilder.loadTexts: pmTrackingPolicyToElementTable.setStatus('current')
if mibBuilder.loadTexts: pmTrackingPolicyToElementTable.setDescription('The pmTrackingPolicyToElementTable describes what elements are under control of a policy.')
pmTrackingPolicyToElementEntry = MibTableRow((1, 3, 6, 1, 3, 107, 6, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"), (0, "POLICY-MANAGEMENT-MIB", "pmTrackingPolicyToElementElement"))
if mibBuilder.loadTexts: pmTrackingPolicyToElementEntry.setStatus('current')
if mibBuilder.loadTexts: pmTrackingPolicyToElementEntry.setDescription('An entry in the pmTrackingPolicyToElementTable. The pmPolicyIndex in the index specifies the policy tracked by this entry.')
pmTrackingPolicyToElementElement = MibTableColumn((1, 3, 6, 1, 3, 107, 6, 1, 1), RowPointer())
if mibBuilder.loadTexts: pmTrackingPolicyToElementElement.setStatus('current')
if mibBuilder.loadTexts: pmTrackingPolicyToElementElement.setDescription('The element this policy is configuring.')
pmTrackingPolicyToElementStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTrackingPolicyToElementStatus.setStatus('current')
if mibBuilder.loadTexts: pmTrackingPolicyToElementStatus.setDescription("The status of this policy-element relationship. This value will be 1 if the associated policyFilter returned 1 for this element and if the calendar for the policy is active. Entries will only exist in this table if their status is on(1). Thus, on(1) is the only value of this object that can be retrieved. This object exists so that it can serve as the 'payload' in the varbind instead of the pmTrackingPolicyToElementElement object which is much longer and is already in the index (it would otherwise be duplicated).")
pmTrackingElementToPolicyTable = MibTable((1, 3, 6, 1, 3, 107, 7), )
if mibBuilder.loadTexts: pmTrackingElementToPolicyTable.setStatus('current')
if mibBuilder.loadTexts: pmTrackingElementToPolicyTable.setDescription('The pmTrackingElementToPolicyTable describes what policies are controlling an element.')
pmTrackingElementToPolicyEntry = MibTableRow((1, 3, 6, 1, 3, 107, 7, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmTrackingElementToPolicyElement"), (0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"))
if mibBuilder.loadTexts: pmTrackingElementToPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: pmTrackingElementToPolicyEntry.setDescription('An entry in the pmTrackingElementToPolicyTable. The pmPolicyIndex in the index specifies the policy tracked by this entry.')
pmTrackingElementToPolicyElement = MibTableColumn((1, 3, 6, 1, 3, 107, 7, 1, 1), RowPointer())
if mibBuilder.loadTexts: pmTrackingElementToPolicyElement.setStatus('current')
if mibBuilder.loadTexts: pmTrackingElementToPolicyElement.setDescription('The element this policy is configuring.')
pmTrackingElementToPolicyStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("forceOff", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTrackingElementToPolicyStatus.setStatus('current')
if mibBuilder.loadTexts: pmTrackingElementToPolicyStatus.setDescription('The status of this policy-element relationship. This value will be 1 if the associated policyFilter returned 1 for this element and if the calendar for the policy is active. Entries will not exist in this table if their status would be off(0). A policy can be forcibly disabled on a particular element by setting this value to forceOff(2). The agent should then act as if the policyFilter failed for this element. The forceOff(2) state will persist (even across reboots) until this value is set to on(1) by a management request. Even if the policyFilter later fails for this element, this value will stay in the forceOff(2) state.')
pmDebuggingTable = MibTable((1, 3, 6, 1, 3, 107, 8), )
if mibBuilder.loadTexts: pmDebuggingTable.setStatus('current')
if mibBuilder.loadTexts: pmDebuggingTable.setDescription('The pmDebuggingPolicyTable logs debugging messages when policies experience runtime errors.')
pmDebuggingEntry = MibTableRow((1, 3, 6, 1, 3, 107, 8, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"), (0, "POLICY-MANAGEMENT-MIB", "pmDebuggingElement"), (0, "POLICY-MANAGEMENT-MIB", "pmDebuggingLogIndex"))
if mibBuilder.loadTexts: pmDebuggingEntry.setStatus('current')
if mibBuilder.loadTexts: pmDebuggingEntry.setDescription('An entry in the pmDebuggingTable. The pmPolicyIndex in the index specifies the policy that encountered the error that led to this log entry.')
pmDebuggingElement = MibTableColumn((1, 3, 6, 1, 3, 107, 8, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmDebuggingElement.setStatus('current')
if mibBuilder.loadTexts: pmDebuggingElement.setDescription('The element the policy was executing on when it encountered the error that led to this log entry.')
pmDebuggingLogIndex = MibTableColumn((1, 3, 6, 1, 3, 107, 8, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmDebuggingLogIndex.setStatus('current')
if mibBuilder.loadTexts: pmDebuggingLogIndex.setDescription('A unique index for this log entry amongst other log entries for this policy/element combination.')
pmDebuggingMessage = MibTableColumn((1, 3, 6, 1, 3, 107, 8, 1, 3), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmDebuggingMessage.setStatus('current')
if mibBuilder.loadTexts: pmDebuggingMessage.setDescription('An error message generated by the expression runtime system.')
pmConformance = MibIdentifier((1, 3, 6, 1, 3, 107, 20))
pmCompliances = MibIdentifier((1, 3, 6, 1, 3, 107, 20, 1))
pmGroups = MibIdentifier((1, 3, 6, 1, 3, 107, 20, 2))
pmCompliance = ModuleCompliance((1, 3, 6, 1, 3, 107, 20, 1, 1)).setObjects(("POLICY-MANAGEMENT-MIB", "pmPolicyManagementGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmCompliance = pmCompliance.setStatus('current')
if mibBuilder.loadTexts: pmCompliance.setDescription('Describes the requirements for conformance to the Policy-Based Management MIB')
pmPolicyManagementGroup = ObjectGroup((1, 3, 6, 1, 3, 107, 20, 2, 1)).setObjects(("POLICY-MANAGEMENT-MIB", "pmPolicyFilter"), ("POLICY-MANAGEMENT-MIB", "pmPolicyCalendar"), ("POLICY-MANAGEMENT-MIB", "pmPolicyAction"), ("POLICY-MANAGEMENT-MIB", "pmPolicyFilterMaxLatency"), ("POLICY-MANAGEMENT-MIB", "pmPolicyActionMaxLatency"), ("POLICY-MANAGEMENT-MIB", "pmPolicyPrecedence"), ("POLICY-MANAGEMENT-MIB", "pmPolicyGroup"), ("POLICY-MANAGEMENT-MIB", "pmPolicyDescription"), ("POLICY-MANAGEMENT-MIB", "pmPolicyMatches"), ("POLICY-MANAGEMENT-MIB", "pmPolicyExecutionErrors"), ("POLICY-MANAGEMENT-MIB", "pmPolicyDebugging"), ("POLICY-MANAGEMENT-MIB", "pmPolicyStatus"), ("POLICY-MANAGEMENT-MIB", "pmElementTypeRegOIDPrefix"), ("POLICY-MANAGEMENT-MIB", "pmElementTypeRegName"), ("POLICY-MANAGEMENT-MIB", "pmElementTypeRegRowStatus"), ("POLICY-MANAGEMENT-MIB", "pmRoleESStatus"), ("POLICY-MANAGEMENT-MIB", "pmRoleSEElement"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesType"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesSubType"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationOID"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationType"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationValue"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationString"), ("POLICY-MANAGEMENT-MIB", "pmTrackingPolicyToElementStatus"), ("POLICY-MANAGEMENT-MIB", "pmTrackingElementToPolicyStatus"), ("POLICY-MANAGEMENT-MIB", "pmDebuggingElement"), ("POLICY-MANAGEMENT-MIB", "pmDebuggingLogIndex"), ("POLICY-MANAGEMENT-MIB", "pmDebuggingMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmPolicyManagementGroup = pmPolicyManagementGroup.setStatus('current')
if mibBuilder.loadTexts: pmPolicyManagementGroup.setDescription('Objects that allow for the creation and management of configuration policies.')
pmBaseFunctionLibrary = MibIdentifier((1, 3, 6, 1, 3, 107, 20, 2, 2))
mibBuilder.exportSymbols("POLICY-MANAGEMENT-MIB", pmCapabilitiesSubType=pmCapabilitiesSubType, pmTrackingElementToPolicyElement=pmTrackingElementToPolicyElement, pmRoleESStatus=pmRoleESStatus, pmGroups=pmGroups, pmTrackingPolicyToElementEntry=pmTrackingPolicyToElementEntry, pmCapabilitiesModificationType=pmCapabilitiesModificationType, pmDebuggingEntry=pmDebuggingEntry, pmPolicyActionMaxLatency=pmPolicyActionMaxLatency, pmRoleSEEntry=pmRoleSEEntry, pmRoleESString=pmRoleESString, pmBaseFunctionLibrary=pmBaseFunctionLibrary, pmPolicyGroup=pmPolicyGroup, pmTrackingElementToPolicyStatus=pmTrackingElementToPolicyStatus, pmRoleSEString=pmRoleSEString, pmRoleESElement=pmRoleESElement, pmElementTypeRegName=pmElementTypeRegName, pmCapabilitiesModificationValue=pmCapabilitiesModificationValue, pmTrackingPolicyToElementElement=pmTrackingPolicyToElementElement, pmDebuggingElement=pmDebuggingElement, pmDebuggingLogIndex=pmDebuggingLogIndex, pmPolicyEntry=pmPolicyEntry, pmRoleESTable=pmRoleESTable, pmTrackingElementToPolicyEntry=pmTrackingElementToPolicyEntry, pmCapabilitiesModificationOID=pmCapabilitiesModificationOID, pmPolicyAction=pmPolicyAction, pmCompliance=pmCompliance, pmElementTypeRegOIDPrefix=pmElementTypeRegOIDPrefix, policyMgt=policyMgt, pmPolicyExecutionErrors=pmPolicyExecutionErrors, pmPolicyIndex=pmPolicyIndex, pmCapabilitiesIndex=pmCapabilitiesIndex, pmCapabilitiesModificationString=pmCapabilitiesModificationString, pmRoleSETable=pmRoleSETable, pmTrackingElementToPolicyTable=pmTrackingElementToPolicyTable, pmPolicyFilterMaxLatency=pmPolicyFilterMaxLatency, pmPolicyMatches=pmPolicyMatches, pmPolicyStatus=pmPolicyStatus, pmElementTypeRegEntry=pmElementTypeRegEntry, pmRoleESEntry=pmRoleESEntry, pmPolicyFilter=pmPolicyFilter, pmElementTypeRegTable=pmElementTypeRegTable, pmTrackingPolicyToElementStatus=pmTrackingPolicyToElementStatus, pmPolicyDescription=pmPolicyDescription, pmTrackingPolicyToElementTable=pmTrackingPolicyToElementTable, pmCapabilitiesEntry=pmCapabilitiesEntry, pmPolicyCalendar=pmPolicyCalendar, pmConformance=pmConformance, pmPolicyTable=pmPolicyTable, pmPolicyPrecedence=pmPolicyPrecedence, pmCapabilitiesTable=pmCapabilitiesTable, pmCapabilitiesType=pmCapabilitiesType, pmCompliances=pmCompliances, pmDebuggingMessage=pmDebuggingMessage, pmRoleSEElement=pmRoleSEElement, pmPolicyManagementGroup=pmPolicyManagementGroup, PYSNMP_MODULE_ID=policyMgt, UTF8String=UTF8String, pmPolicyDebugging=pmPolicyDebugging, pmElementTypeRegIndex=pmElementTypeRegIndex, pmDebuggingTable=pmDebuggingTable, pmElementTypeRegRowStatus=pmElementTypeRegRowStatus)

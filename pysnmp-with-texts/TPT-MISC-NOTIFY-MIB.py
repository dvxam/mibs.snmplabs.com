#
# PySNMP MIB module TPT-MISC-NOTIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-MISC-NOTIFY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Counter64, iso, Counter32, NotificationType, TimeTicks, Unsigned32, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter64", "iso", "Counter32", "NotificationType", "TimeTicks", "Unsigned32", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
SslInspectedFlag, = mibBuilder.importSymbols("TPT-POLICY-MIB", "SslInspectedFlag")
tpt_tpa_objs, tpt_tpa_unkparams, tpt_tpa_eventsV2 = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs", "tpt-tpa-unkparams", "tpt-tpa-eventsV2")
tpt_misc_notify = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 2)).setLabel("tpt-misc-notify")
tpt_misc_notify.setRevisions(('2016-05-25 18:54', '2016-05-03 17:26', '2015-05-28 13:30', '2014-11-11 18:43',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_misc_notify.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.', 'Added emergency, alert, notice, info, and debug severity values to SystemLogSeverity.', 'Added SSL inspected flag parameter to quarantine notifications.', 'Added audit log notification and objects.',))
if mibBuilder.loadTexts: tpt_misc_notify.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_misc_notify.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_misc_notify.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_misc_notify.setDescription("Notification definitions that have no other place to call home. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
tptMiscNotifyDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 31), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptMiscNotifyDeviceID.setStatus('current')
if mibBuilder.loadTexts: tptMiscNotifyDeviceID.setDescription('The unique identifier of the device sending this notification.')
tptManagedNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 9)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"))
if mibBuilder.loadTexts: tptManagedNotify.setStatus('current')
if mibBuilder.loadTexts: tptManagedNotify.setDescription('Notification: Used to inform the management station that the device is now being managed by said management station.')
tptUnmanagedNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 10)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"))
if mibBuilder.loadTexts: tptUnmanagedNotify.setStatus('current')
if mibBuilder.loadTexts: tptUnmanagedNotify.setDescription('Notification: Used to inform the management station that the device is no longer being managed by said management station.')
class LogFileType(TextualConvention, Integer32):
    description = 'The type of the file that has rolled over.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("system", 1), ("alert", 2), ("block", 3), ("peer", 4), ("audit", 5), ("quarantine", 6))

tptRolloverNotifyFileType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 32), LogFileType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptRolloverNotifyFileType.setStatus('current')
if mibBuilder.loadTexts: tptRolloverNotifyFileType.setDescription('The type of the file that has rolled over.')
tptRolloverNotifyMaxFiles = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 33), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptRolloverNotifyMaxFiles.setStatus('deprecated')
if mibBuilder.loadTexts: tptRolloverNotifyMaxFiles.setDescription('The maximum number of files maintained for this log file type.')
tptRolloverNotifyNumFiles = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 34), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptRolloverNotifyNumFiles.setStatus('deprecated')
if mibBuilder.loadTexts: tptRolloverNotifyNumFiles.setDescription('The number of files that have rolled over.')
tptRolloverNotifyTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 35), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptRolloverNotifyTime.setStatus('current')
if mibBuilder.loadTexts: tptRolloverNotifyTime.setDescription('The rollover time of the most recent file pertaining to this notification (in seconds since January 1, 1970).')
tptRolloverNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 11)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptRolloverNotifyFileType"), ("TPT-MISC-NOTIFY-MIB", "tptRolloverNotifyTime"))
if mibBuilder.loadTexts: tptRolloverNotify.setStatus('current')
if mibBuilder.loadTexts: tptRolloverNotify.setDescription('Notification: Used to inform the management station that a log file has rolled over.')
class DiscoveryDelta(TextualConvention, Integer32):
    description = 'An indication of whether discovery results changed from the previous scan.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("changed", 1), ("unchanged", 2))

tptDiscoveryNotifyScanID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 42), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyScanID.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyScanID.setDescription('The unique identifier of the scan pertaining to this notification.')
tptDiscoveryNotifySegmentName = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 43), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifySegmentName.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifySegmentName.setDescription('The name of the scanned segment pertaining to this notification.')
tptDiscoveryNotifyScanRange = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 44), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyScanRange.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyScanRange.setDescription('The network address range requested in the scan pertaining to this notification.')
tptDiscoveryNotifyDelta = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 45), DiscoveryDelta()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyDelta.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyDelta.setDescription('An indication of whether discovery results changed from the previous scan. Undefined if this notification signifies the start of a scan.')
tptDiscoveryNotifyNewHosts = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 46), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyNewHosts.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyNewHosts.setDescription('The number of new hosts found by this scan (compared to the previous scan). Undefined if this notification signifies the start of a scan.')
tptDiscoveryNotifyChanged = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyChanged.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyChanged.setDescription('The number of hosts for which this scan found different results from the previous scan. Undefined if this notification signifies the start of a scan.')
tptDiscoveryNotifyUnchanged = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 48), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyUnchanged.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyUnchanged.setDescription('The number of existing hosts for which this scan found the same results (compared to the previous scan). Undefined if this notification signifies the start of a scan.')
tptDiscoveryNotifyNotFound = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 49), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyNotFound.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyNotFound.setDescription('The number of hosts found by the previous scan but not by this scan. Undefined if this notification signifies the start of a scan.')
tptDiscoveryNotifyUnknown = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 50), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyUnknown.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyUnknown.setDescription('The number of addresses scanned where no host was found and for which there was no previous scan data. Undefined if this notification signifies the start of a scan.')
tptDiscoveryNotifyStartTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 51), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyStartTime.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyStartTime.setDescription('The start time of the scan pertaining to this notification (in seconds since January 1, 1970).')
tptDiscoveryNotifyStopTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 52), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyStopTime.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyStopTime.setDescription('The stop time of the scan pertaining to this notification (in seconds since January 1, 1970). A zero value indicates that this notification signifies the start of a scan.')
tptDiscoveryNotifyErrorText = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 53), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyErrorText.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyErrorText.setDescription('If the current scan terminated abnormally, this string describes the error condition. Otherwise, an empty string.')
tptDiscoveryNotifySchedID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 56), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifySchedID.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifySchedID.setDescription('For a notification resulting from a scheduled scan, this value holds the scheduled scan identifier. Otherwise, this value is undefined.')
tptDiscoveryNotifyStartStop = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 12)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyScanID"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifySegmentName"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyScanRange"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyDelta"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyNewHosts"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyChanged"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyUnchanged"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyNotFound"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyUnknown"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyStartTime"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyStopTime"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyErrorText"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifySchedID"))
if mibBuilder.loadTexts: tptDiscoveryNotifyStartStop.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyStartStop.setDescription('Notification: Used to inform the management station that a network discovery scan has started or stopped.')
tptDiscoveryNotifyHostNetAddr = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 54), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyHostNetAddr.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyHostNetAddr.setDescription('The network address of the newly discovered host.')
tptDiscoveryNotifyHostDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 55), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptDiscoveryNotifyHostDeviceID.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyHostDeviceID.setDescription('The unique identifier of the newly discovered host.')
tptDiscoveryNotifyNewHost = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 13)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyHostNetAddr"), ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyHostDeviceID"))
if mibBuilder.loadTexts: tptDiscoveryNotifyNewHost.setStatus('obsolete')
if mibBuilder.loadTexts: tptDiscoveryNotifyNewHost.setDescription('Notification: Used to inform the management station that a previously unknown host was discovered by a scan.')
class SystemLogSeverity(TextualConvention, Integer32):
    description = 'An indication of the severity of a system log message.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("critical", 1), ("error", 2), ("emergency", 3), ("warning", 4), ("alert", 5), ("notice", 6), ("info", 7), ("debug", 8))

tptSystemLogNotifyText = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 92), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSystemLogNotifyText.setStatus('current')
if mibBuilder.loadTexts: tptSystemLogNotifyText.setDescription('The text of the message being logged.')
tptSystemLogNotifySequence = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 93), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSystemLogNotifySequence.setStatus('current')
if mibBuilder.loadTexts: tptSystemLogNotifySequence.setDescription('The log file entry sequence number corresponding to this notification.')
tptSystemLogNotifySeverity = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 94), SystemLogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSystemLogNotifySeverity.setStatus('current')
if mibBuilder.loadTexts: tptSystemLogNotifySeverity.setDescription('The severity of the attack for this notification.')
tptSystemLogNotifyTimeSec = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 95), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSystemLogNotifyTimeSec.setStatus('current')
if mibBuilder.loadTexts: tptSystemLogNotifyTimeSec.setDescription('The time this message was logged (in seconds since January 1, 1970).')
tptSystemLogNotifyTimeNano = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 96), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSystemLogNotifyTimeNano.setStatus('current')
if mibBuilder.loadTexts: tptSystemLogNotifyTimeNano.setDescription('The nanoseconds portion of tptSystemLogNotifyTimeSec.')
tptSystemLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 16)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifyText"), ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifySequence"), ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifySeverity"), ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifyTimeSec"), ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifyTimeNano"))
if mibBuilder.loadTexts: tptSystemLogNotify.setStatus('current')
if mibBuilder.loadTexts: tptSystemLogNotify.setDescription('Notification: Used to inform the management station that a critical, error, or warning message has been logged.')
class AddOrRemove(TextualConvention, Integer32):
    description = 'An indication of whether a host was added to or removed from the quarantine list.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("add", 1), ("remove", 2))

tptQuarantineNotifyHostNetAddr = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 132), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptQuarantineNotifyHostNetAddr.setStatus('current')
if mibBuilder.loadTexts: tptQuarantineNotifyHostNetAddr.setDescription('The network address of the host being quarantined (or removed).')
tptQuarantineNotifyHostNetAddrV6 = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 136), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptQuarantineNotifyHostNetAddrV6.setStatus('current')
if mibBuilder.loadTexts: tptQuarantineNotifyHostNetAddrV6.setDescription('The IPv6 network address of the host being quarantined (or removed).')
tptQuarantineNotifyReason = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 133), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptQuarantineNotifyReason.setStatus('current')
if mibBuilder.loadTexts: tptQuarantineNotifyReason.setDescription('The reason that a host was quarantined (undefined if action is remove).')
tptQuarantineNotifySegmentName = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 134), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptQuarantineNotifySegmentName.setStatus('current')
if mibBuilder.loadTexts: tptQuarantineNotifySegmentName.setDescription('A string of the format <slot>:<index> that uniquely identifies the segment pertaining to this notification.')
tptQuarantineNotifyAction = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 135), AddOrRemove()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptQuarantineNotifyAction.setStatus('current')
if mibBuilder.loadTexts: tptQuarantineNotifyAction.setDescription('Whether the host was added to or removed from the quarantine list.')
tptQuarantineNotifySslInspected = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 181), SslInspectedFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptQuarantineNotifySslInspected.setStatus('current')
if mibBuilder.loadTexts: tptQuarantineNotifySslInspected.setDescription('Flag indicating if this quarantine action was performed on an inspected SSL data stream.')
tptQuarantineNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 20)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifyHostNetAddr"), ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifyReason"), ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifySegmentName"), ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifyAction"), ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifyHostNetAddrV6"), ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifySslInspected"))
if mibBuilder.loadTexts: tptQuarantineNotify.setStatus('current')
if mibBuilder.loadTexts: tptQuarantineNotify.setDescription('Notification: Used to inform the management station that a host has been either added to or removed from the quarantine list.')
class CongestionThresholdPhase(TextualConvention, Integer32):
    description = 'The congestion threshold phase (entering, continuing, or exiting).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("entering", 1), ("continuing", 2), ("exiting", 3))

tptCongestionPacketLoss = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 153), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptCongestionPacketLoss.setStatus('current')
if mibBuilder.loadTexts: tptCongestionPacketLoss.setDescription('The current packet loss rate per thousand (percent * 10).')
tptCongestionNotifyPhase = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 154), CongestionThresholdPhase()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptCongestionNotifyPhase.setStatus('current')
if mibBuilder.loadTexts: tptCongestionNotifyPhase.setDescription('Whether entering, continuing, or exiting congestion threshold mode.')
tptCongestionThreshold = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 155), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptCongestionThreshold.setStatus('current')
if mibBuilder.loadTexts: tptCongestionThreshold.setDescription('The current packet loss threshold per thousand (percent * 10).')
tptTier3CongestionPacketLoss = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 156), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTier3CongestionPacketLoss.setStatus('current')
if mibBuilder.loadTexts: tptTier3CongestionPacketLoss.setDescription('The current tier3 packet loss rate per thousand (percent * 10).')
tptTier3CongestionNotifyPhase = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 157), CongestionThresholdPhase()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTier3CongestionNotifyPhase.setStatus('current')
if mibBuilder.loadTexts: tptTier3CongestionNotifyPhase.setDescription('Whether entering, continuing, or exiting tier3 congestion threshold mode.')
tptTier3CongestionThreshold = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 158), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTier3CongestionThreshold.setStatus('current')
if mibBuilder.loadTexts: tptTier3CongestionThreshold.setDescription('The current tier3 packet loss threshold per thousand (percent * 10).')
tptCongestionThresholdNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 25)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptCongestionNotifyPhase"), ("TPT-MISC-NOTIFY-MIB", "tptCongestionPacketLoss"), ("TPT-MISC-NOTIFY-MIB", "tptCongestionThreshold"))
if mibBuilder.loadTexts: tptCongestionThresholdNotify.setStatus('current')
if mibBuilder.loadTexts: tptCongestionThresholdNotify.setDescription('Notification: Used to inform the management station that the device-wide congestion has exceeded the configured congestion threshold.')
tptiTier3CongestionThresholdNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 26)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptTier3CongestionNotifyPhase"), ("TPT-MISC-NOTIFY-MIB", "tptTier3CongestionPacketLoss"), ("TPT-MISC-NOTIFY-MIB", "tptTier3CongestionThreshold"))
if mibBuilder.loadTexts: tptiTier3CongestionThresholdNotify.setStatus('current')
if mibBuilder.loadTexts: tptiTier3CongestionThresholdNotify.setDescription('Notification: Used to inform the management station that the tier3 congestion has exceeded the configured congestion threshold.')
tptAuditLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 60)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyTime"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyAccess"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyType"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyIpAddrType"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyIpAddr"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyCategory"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyResult"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyUser"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyMessage"))
if mibBuilder.loadTexts: tptAuditLogNotify.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotify.setDescription('Audit-log notification. ')
class AuditLogResult(TextualConvention, Integer32):
    description = 'The result of an audit check: success, or fail. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("success", 1), ("failed", 2))

class AuditLogCategory(TextualConvention, Integer32):
    description = 'The functional location of where an audit check was made and generated a log entry. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("undefined", 1), ("general", 2), ("login", 3), ("logout", 4), ("user", 5), ("time", 6), ("policy", 7), ("update", 8), ("boot", 9), ("report", 10), ("host", 11), ("cfg", 12), ("device", 13), ("sms", 14), ("server", 15), ("segment", 16), ("license", 17), ("ha", 18), ("monitor", 19), ("ipFilter", 20), ("connTable", 21), ("hostComm", 22), ("tse", 23), ("cf", 24))

tptAuditLogNotifyTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 170), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptAuditLogNotifyTime.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotifyTime.setDescription('The date and time when the entry was logged. ')
tptAuditLogNotifyAccess = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 171), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptAuditLogNotifyAccess.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotifyAccess.setDescription('The access level of the user initiating the audit check and generating the log. This is a bit field with the following mapping: 0x0 - normal 0x1 - operator 0x4 - administrator 0x8 - super-user ')
tptAuditLogNotifyType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 172), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptAuditLogNotifyType.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotifyType.setDescription('The interface source of the audit log action. ')
tptAuditLogNotifyIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 173), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptAuditLogNotifyIpAddrType.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotifyIpAddrType.setDescription('The type of IP address from which the user connected. ')
tptAuditLogNotifyIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 174), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptAuditLogNotifyIpAddr.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotifyIpAddr.setDescription('The IP address from which the user connected. ')
tptAuditLogNotifyCategory = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 175), AuditLogCategory()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptAuditLogNotifyCategory.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotifyCategory.setDescription('The functional area where the audit log was generated. ')
tptAuditLogNotifyResult = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 176), AuditLogResult()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptAuditLogNotifyResult.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotifyResult.setDescription('The result, pass or fail, of an audit check. ')
tptAuditLogNotifyUser = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 177), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptAuditLogNotifyUser.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotifyUser.setDescription('The user initiating the audit check and generating the log. ')
tptAuditLogNotifyMessage = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 178), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4096))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptAuditLogNotifyMessage.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogNotifyMessage.setDescription('A description of what configuration change was attempted (and possibly succeeded) by the user. ')
tptAuditLogCapacityNotifyPercent = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 201), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptAuditLogCapacityNotifyPercent.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogCapacityNotifyPercent.setDescription('The time of this notification (in seconds since January 1, 1970).')
tptAuditLogCapacityOrFailureNotifyTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 202), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptAuditLogCapacityOrFailureNotifyTime.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogCapacityOrFailureNotifyTime.setDescription('The time of this notification (in seconds since January 1, 1970).')
tptAuditLogCapacityNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 61)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptAuditLogCapacityNotifyPercent"), ("TPT-MISC-NOTIFY-MIB", "tptRolloverNotifyTime"))
if mibBuilder.loadTexts: tptAuditLogCapacityNotify.setStatus('current')
if mibBuilder.loadTexts: tptAuditLogCapacityNotify.setDescription('Notification: Used to inform the management station that audit log file size has reached more than 75 percent.')
tptLoggingFailureNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 62)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-MISC-NOTIFY-MIB", "tptRolloverNotifyTime"))
if mibBuilder.loadTexts: tptLoggingFailureNotify.setStatus('current')
if mibBuilder.loadTexts: tptLoggingFailureNotify.setDescription('Notification: Used to inform the management station that logging has failed.')
mibBuilder.exportSymbols("TPT-MISC-NOTIFY-MIB", tptCongestionPacketLoss=tptCongestionPacketLoss, tptRolloverNotifyMaxFiles=tptRolloverNotifyMaxFiles, AddOrRemove=AddOrRemove, tptTier3CongestionThreshold=tptTier3CongestionThreshold, tptQuarantineNotifyHostNetAddrV6=tptQuarantineNotifyHostNetAddrV6, tptQuarantineNotify=tptQuarantineNotify, tptDiscoveryNotifyHostNetAddr=tptDiscoveryNotifyHostNetAddr, tptAuditLogCapacityNotifyPercent=tptAuditLogCapacityNotifyPercent, SystemLogSeverity=SystemLogSeverity, tptDiscoveryNotifyUnchanged=tptDiscoveryNotifyUnchanged, AuditLogResult=AuditLogResult, tptRolloverNotifyNumFiles=tptRolloverNotifyNumFiles, tptUnmanagedNotify=tptUnmanagedNotify, tptQuarantineNotifyHostNetAddr=tptQuarantineNotifyHostNetAddr, tptDiscoveryNotifyNotFound=tptDiscoveryNotifyNotFound, tptDiscoveryNotifyStopTime=tptDiscoveryNotifyStopTime, tptDiscoveryNotifyNewHosts=tptDiscoveryNotifyNewHosts, tptCongestionNotifyPhase=tptCongestionNotifyPhase, tptDiscoveryNotifyStartTime=tptDiscoveryNotifyStartTime, tptAuditLogNotifyTime=tptAuditLogNotifyTime, tptDiscoveryNotifyHostDeviceID=tptDiscoveryNotifyHostDeviceID, tptLoggingFailureNotify=tptLoggingFailureNotify, tptRolloverNotifyFileType=tptRolloverNotifyFileType, tptDiscoveryNotifyUnknown=tptDiscoveryNotifyUnknown, tptQuarantineNotifyReason=tptQuarantineNotifyReason, tptTier3CongestionPacketLoss=tptTier3CongestionPacketLoss, PYSNMP_MODULE_ID=tpt_misc_notify, tptQuarantineNotifySegmentName=tptQuarantineNotifySegmentName, CongestionThresholdPhase=CongestionThresholdPhase, tptAuditLogNotifyIpAddrType=tptAuditLogNotifyIpAddrType, tptAuditLogCapacityNotify=tptAuditLogCapacityNotify, tptDiscoveryNotifyScanRange=tptDiscoveryNotifyScanRange, tptAuditLogNotifyResult=tptAuditLogNotifyResult, tptDiscoveryNotifyStartStop=tptDiscoveryNotifyStartStop, tptSystemLogNotifySequence=tptSystemLogNotifySequence, tptAuditLogCapacityOrFailureNotifyTime=tptAuditLogCapacityOrFailureNotifyTime, DiscoveryDelta=DiscoveryDelta, tptAuditLogNotifyIpAddr=tptAuditLogNotifyIpAddr, tptRolloverNotify=tptRolloverNotify, LogFileType=LogFileType, tptTier3CongestionNotifyPhase=tptTier3CongestionNotifyPhase, tptAuditLogNotifyCategory=tptAuditLogNotifyCategory, tptSystemLogNotifyText=tptSystemLogNotifyText, tptSystemLogNotifySeverity=tptSystemLogNotifySeverity, tptCongestionThreshold=tptCongestionThreshold, tptSystemLogNotifyTimeNano=tptSystemLogNotifyTimeNano, tptMiscNotifyDeviceID=tptMiscNotifyDeviceID, tpt_misc_notify=tpt_misc_notify, tptDiscoveryNotifyChanged=tptDiscoveryNotifyChanged, tptDiscoveryNotifyNewHost=tptDiscoveryNotifyNewHost, tptCongestionThresholdNotify=tptCongestionThresholdNotify, tptQuarantineNotifySslInspected=tptQuarantineNotifySslInspected, tptAuditLogNotifyMessage=tptAuditLogNotifyMessage, tptAuditLogNotifyType=tptAuditLogNotifyType, tptAuditLogNotify=tptAuditLogNotify, tptQuarantineNotifyAction=tptQuarantineNotifyAction, AuditLogCategory=AuditLogCategory, tptDiscoveryNotifyErrorText=tptDiscoveryNotifyErrorText, tptDiscoveryNotifySegmentName=tptDiscoveryNotifySegmentName, tptDiscoveryNotifyDelta=tptDiscoveryNotifyDelta, tptSystemLogNotifyTimeSec=tptSystemLogNotifyTimeSec, tptManagedNotify=tptManagedNotify, tptAuditLogNotifyAccess=tptAuditLogNotifyAccess, tptAuditLogNotifyUser=tptAuditLogNotifyUser, tptSystemLogNotify=tptSystemLogNotify, tptiTier3CongestionThresholdNotify=tptiTier3CongestionThresholdNotify, tptDiscoveryNotifyScanID=tptDiscoveryNotifyScanID, tptRolloverNotifyTime=tptRolloverNotifyTime, tptDiscoveryNotifySchedID=tptDiscoveryNotifySchedID)

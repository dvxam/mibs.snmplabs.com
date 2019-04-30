#
# PySNMP MIB module DLINK-3100-EMBWEB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-EMBWEB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:33:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, Bits, Counter64, Gauge32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, ObjectIdentity, Counter32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Bits", "Counter64", "Gauge32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "ObjectIdentity", "Counter32", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
rlEmbWeb = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66))
rlEmbWeb.setRevisions(('2006-07-03 00:00',))
if mibBuilder.loadTexts: rlEmbWeb.setLastUpdated('200607030000Z')
if mibBuilder.loadTexts: rlEmbWeb.setOrganization('Dlink, Inc.')
class RlEmbWebProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("http", 2), ("https", 3))

class RlEmbWebEnabled(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("false", 2), ("true", 3))

rlEmWebMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEmWebMibVersion.setStatus('current')
rlEmWebWebSite = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebWebSite.setStatus('current')
rlEmWebSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3), )
if mibBuilder.loadTexts: rlEmWebSecurityTable.setStatus('current')
rlEmWebSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1), ).setIndexNames((0, "DLINK-3100-EMBWEB-MIB", "rlEmWebSecurityUserName"))
if mibBuilder.loadTexts: rlEmWebSecurityEntry.setStatus('current')
rlEmWebSecurityUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebSecurityUserName.setStatus('current')
rlEmWebSecurityPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebSecurityPassword.setStatus('current')
rlEmWebSecurityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("readOnly", 2), ("readWrite", 3), ("super", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebSecurityAccess.setStatus('current')
rlEmWebSecurityIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebSecurityIpAddr.setStatus('current')
rlEmWebSecurityPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebSecurityPort.setStatus('current')
rlEmWebSecuritySnmpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ver1", 1), ("ver2", 2), ("ver3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebSecuritySnmpVersion.setStatus('current')
rlEmWebSecurityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebSecurityStatus.setStatus('current')
rlEmWebCloseTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebCloseTimeout.setStatus('current')
rlEmWebReceiveTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebReceiveTimeout.setStatus('current')
rlEmWebMaxIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebMaxIdleTimeout.setStatus('current')
rlEmWebSetEWSfilesStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("opened", 1), ("closed", 2))).clone('opened')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebSetEWSfilesStatus.setStatus('current')
rlEmbeddedWebApplied = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEmbeddedWebApplied.setStatus('current')
rlEmWebHttpPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebHttpPort.setStatus('current')
rlEmWebHttpEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebHttpEnable.setStatus('current')
rlEmWebHttpsPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebHttpsPort.setStatus('current')
rlEmWebHttpsEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebHttpsEnable.setStatus('current')
rlEmWebCertificateCountryName = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebCertificateCountryName.setStatus('current')
rlEmWebCertificateStateOrProvinceName = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebCertificateStateOrProvinceName.setStatus('current')
rlEmWebCertificateLocalityName = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebCertificateLocalityName.setStatus('current')
rlEmWebCertificateOrganizationName = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebCertificateOrganizationName.setStatus('current')
rlEmWebCertificateCommonName = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 19), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebCertificateCommonName.setStatus('current')
rlEmWebCertificateRegenerate = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noAction", 0), ("regenerateCertificate", 1), ("regenerateRsaKeyAndCertificate", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebCertificateRegenerate.setStatus('current')
rlEmWebRsaKeyLength = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 2048))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebRsaKeyLength.setStatus('current')
rlEmWebDebug = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebDebug.setStatus('current')
rlEmWebURL = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEmWebURL.setStatus('current')
rlEmWebDisplayNonPresentEntities = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEmWebDisplayNonPresentEntities.setStatus('current')
rlEmWebCertificateExists = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 25), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEmWebCertificateExists.setStatus('current')
rlEmWebHttpsActiveCertificateId = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 26), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebHttpsActiveCertificateId.setStatus('current')
rlEmWebExtraPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebExtraPort.setStatus('current')
rlEmWebExtraPortType = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("http", 0), ("https", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebExtraPortType.setStatus('current')
rlEmWebMaxHttpsIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebMaxHttpsIdleTimeout.setStatus('current')
rlEmWebServiceTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30), )
if mibBuilder.loadTexts: rlEmWebServiceTable.setStatus('current')
rlEmWebServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1), ).setIndexNames((0, "DLINK-3100-EMBWEB-MIB", "rlEmWebServiceId"))
if mibBuilder.loadTexts: rlEmWebServiceEntry.setStatus('current')
rlEmWebServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 1), Integer32())
if mibBuilder.loadTexts: rlEmWebServiceId.setStatus('current')
rlEmWebServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEmWebServiceName.setStatus('current')
rlEmWebServiceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 3), RlEmbWebEnabled().clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebServiceEnable.setStatus('current')
rlEmWebServicePort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebServicePort.setStatus('current')
rlEmWebServiceMaxUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEmWebServiceMaxUsers.setStatus('current')
rlEmWebServiceProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 6), RlEmbWebProtocol().clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebServiceProtocol.setStatus('current')
rlEmWebServiceCertificateId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 7), Integer32().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebServiceCertificateId.setStatus('current')
rlEmWebServiceMaxIdleTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932160)).clone(3932160)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEmWebServiceMaxIdleTimeOut.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-EMBWEB-MIB", rlEmWebExtraPort=rlEmWebExtraPort, rlEmWebSecurityUserName=rlEmWebSecurityUserName, rlEmWebCertificateOrganizationName=rlEmWebCertificateOrganizationName, rlEmWebServiceEnable=rlEmWebServiceEnable, rlEmWebSecurityPort=rlEmWebSecurityPort, rlEmWebServiceTable=rlEmWebServiceTable, rlEmWebServiceMaxUsers=rlEmWebServiceMaxUsers, rlEmWebReceiveTimeout=rlEmWebReceiveTimeout, RlEmbWebProtocol=RlEmbWebProtocol, rlEmWebExtraPortType=rlEmWebExtraPortType, rlEmWebCertificateExists=rlEmWebCertificateExists, rlEmWebCertificateCommonName=rlEmWebCertificateCommonName, rlEmWebHttpPort=rlEmWebHttpPort, rlEmWebServiceEntry=rlEmWebServiceEntry, rlEmWebMibVersion=rlEmWebMibVersion, rlEmWebCertificateStateOrProvinceName=rlEmWebCertificateStateOrProvinceName, rlEmWebServiceCertificateId=rlEmWebServiceCertificateId, rlEmWebSecuritySnmpVersion=rlEmWebSecuritySnmpVersion, rlEmWebCloseTimeout=rlEmWebCloseTimeout, rlEmWebCertificateCountryName=rlEmWebCertificateCountryName, rlEmWebServiceName=rlEmWebServiceName, rlEmWebServiceMaxIdleTimeOut=rlEmWebServiceMaxIdleTimeOut, PYSNMP_MODULE_ID=rlEmbWeb, rlEmWebSecurityAccess=rlEmWebSecurityAccess, rlEmWebSecurityTable=rlEmWebSecurityTable, rlEmWebServiceProtocol=rlEmWebServiceProtocol, rlEmWebRsaKeyLength=rlEmWebRsaKeyLength, rlEmWebDebug=rlEmWebDebug, rlEmWebURL=rlEmWebURL, rlEmWebServiceId=rlEmWebServiceId, rlEmWebSecurityStatus=rlEmWebSecurityStatus, RlEmbWebEnabled=RlEmbWebEnabled, rlEmWebWebSite=rlEmWebWebSite, rlEmbWeb=rlEmbWeb, rlEmWebCertificateLocalityName=rlEmWebCertificateLocalityName, rlEmWebMaxIdleTimeout=rlEmWebMaxIdleTimeout, rlEmWebHttpEnable=rlEmWebHttpEnable, rlEmWebServicePort=rlEmWebServicePort, rlEmWebSecurityEntry=rlEmWebSecurityEntry, rlEmWebCertificateRegenerate=rlEmWebCertificateRegenerate, rlEmWebSecurityPassword=rlEmWebSecurityPassword, rlEmWebHttpsActiveCertificateId=rlEmWebHttpsActiveCertificateId, rlEmWebSetEWSfilesStatus=rlEmWebSetEWSfilesStatus, rlEmWebMaxHttpsIdleTimeout=rlEmWebMaxHttpsIdleTimeout, rlEmWebSecurityIpAddr=rlEmWebSecurityIpAddr, rlEmbeddedWebApplied=rlEmbeddedWebApplied, rlEmWebDisplayNonPresentEntities=rlEmWebDisplayNonPresentEntities, rlEmWebHttpsPort=rlEmWebHttpsPort, rlEmWebHttpsEnable=rlEmWebHttpsEnable)

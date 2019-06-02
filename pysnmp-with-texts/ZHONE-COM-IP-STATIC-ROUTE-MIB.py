#
# PySNMP MIB module ZHONE-COM-IP-STATIC-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-IP-STATIC-ROUTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:47:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Gauge32, MibIdentifier, IpAddress, iso, Integer32, Bits, TimeTicks, Counter32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Gauge32", "MibIdentifier", "IpAddress", "iso", "Integer32", "Bits", "TimeTicks", "Counter32", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rdIndex, = mibBuilder.importSymbols("ZHONE-COM-IP-RD-MIB", "rdIndex")
zhoneIp, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneIp", "zhoneModules")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
comIpStaticRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 63))
comIpStaticRoute.setRevisions(('2006-07-14 15:50', '2005-04-29 14:10', '2000-09-12 10:23', '2000-09-29 16:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: comIpStaticRoute.setRevisionsDescriptions(('V01.00.02 - added staticRouteFallbackMatric, staticRoutePingInterval, and staticRoutePingFailMax.', 'V01.00.02 - Added staticRouteType.', 'V01.00.00 - Initial Release', 'V01.00.01 - Zhone keyword markup',))
if mibBuilder.loadTexts: comIpStaticRoute.setLastUpdated('200607141700Z')
if mibBuilder.loadTexts: comIpStaticRoute.setOrganization('Zhone Technologies, Inc.')
if mibBuilder.loadTexts: comIpStaticRoute.setContactInfo(' Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: comIpStaticRoute.setDescription('IP Static Route MIB IP Software Minneapolis, MN')
staticRoute = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13))
if mibBuilder.loadTexts: staticRoute.setStatus('current')
if mibBuilder.loadTexts: staticRoute.setDescription('The MIB module representing static routes in Zhone Technologies products. Static routes are user-defined routes that cause packets moving between a source and a destination to take a specified path. Static routes can be important if a router cannot build a route to a particular destination. They are also useful for specifying a gateway of last resort to which all unroutable packets will be sent.')
staticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1), )
if mibBuilder.loadTexts: staticRouteTable.setStatus('current')
if mibBuilder.loadTexts: staticRouteTable.setDescription("The Static Routes table contains static routes assigned to all interfaces. Each interface automatically gets one or more static routes upon interface initialization. More static routes are added as needed (e.g. default gateway). Rows are added by assigning staticRouteDest, staticRouteNetMask, staticRouteNextHop (or staticRouteIfNumber), and setting staticRouteRowStatus to 'createAndGo'. Rows are removed by setting staticRouteRowStatus to 'destroy'.")
staticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1), ).setIndexNames((0, "ZHONE-COM-IP-RD-MIB", "rdIndex"), (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteDest"), (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteNetMask"), (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteNextHop"), (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteIfNumber"), (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteType"))
if mibBuilder.loadTexts: staticRouteEntry.setStatus('current')
if mibBuilder.loadTexts: staticRouteEntry.setDescription('An entry in the Static Route table.')
staticRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: staticRouteDest.setStatus('current')
if mibBuilder.loadTexts: staticRouteDest.setDescription('The destination network or host IP address of the static route. A default gateway is one with a destination of 0.0.0.0 and netmask 0.0.0.0.')
staticRouteNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: staticRouteNetMask.setStatus('current')
if mibBuilder.loadTexts: staticRouteNetMask.setDescription('The destination IP network mask of the static route. A default gateway is one with a destination of 0.0.0.0 and netmask 0.0.0.0.')
staticRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 3), IpAddress())
if mibBuilder.loadTexts: staticRouteNextHop.setStatus('current')
if mibBuilder.loadTexts: staticRouteNextHop.setDescription('The IP address of the nexthop router of the static route. This may be 0.0.0.0 for static routes that use an interface number rather than a nexthop address, as in the case of a destination directly reachable via an interface requiring no intermediary system to act as a gateway.')
staticRouteIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 4), InterfaceIndexOrZero())
if mibBuilder.loadTexts: staticRouteIfNumber.setStatus('current')
if mibBuilder.loadTexts: staticRouteIfNumber.setDescription('The interface of the static route. This is for directly connected destinations (i.e. use this instead of staticRouteNextHop). Unnumbered point-to-point interfaces require this value to be valid. In general, this value must be valid if staticRouteNextHop is not valid. If staticRouteNextHop is valid, then this value must represent the interface named by the nexthop address. This index comes from ifIndex of RFC2233.')
staticRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 5), Unsigned32().clone(2147483647)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: staticRouteMetric.setStatus('current')
if mibBuilder.loadTexts: staticRouteMetric.setDescription('A dimensionless quantity chosen at the discretion of the provisioner for the purpose of comparing static routes. The meaning of this value when static routes are redistributed to other protocols is protocol-dependent, and the resulting value after redistribution is determined by the route-maps in use for that protocol. Lower numeric values for this number indicate more preferred routes.')
staticRouteEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: staticRouteEnable.setStatus('current')
if mibBuilder.loadTexts: staticRouteEnable.setDescription("An enumeration of the administrative state of the static route. The possible values are either 'disabled' or 'enabled', where the static route entry is not considered when making forwarding decisions for 'disabled', and is so for 'enabled'. The default is 'enabled'.")
staticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 7), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: staticRouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: staticRouteRowStatus.setDescription('The status of a static route entry.')
staticRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("destinationRoute", 1), ("sourceRoute", 2))))
if mibBuilder.loadTexts: staticRouteType.setStatus('current')
if mibBuilder.loadTexts: staticRouteType.setDescription('Determines if this entry is a traditional destination route or a source address based route. ')
staticRouteFallbackMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 9), Integer32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: staticRouteFallbackMetric.setStatus('current')
if mibBuilder.loadTexts: staticRouteFallbackMetric.setDescription("This object contains the fallback metric value for routes that are a part of a fallback route pair. Please refer to the Zhone Technologies User's Reference Manual for more information about fallback route pairs. The value of this object must be greater than both of the staticRouteMetrics of fallback route pair. ")
staticRoutePingInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: staticRoutePingInterval.setStatus('current')
if mibBuilder.loadTexts: staticRoutePingInterval.setDescription('This object defines the interval, in milliseconds, of succesive pings of the nexthop of an active fallback route pair. The minimum value is 500 milliseconds, and must be specified in increments of 100 milliseconds. ')
staticRoutePingFailMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: staticRoutePingFailMax.setStatus('current')
if mibBuilder.loadTexts: staticRoutePingFailMax.setDescription('This object contain the maximum number of times that the ping of the nexthop of an active route in a fallback route pair must fail, in a row, before this route is demoted to fallback and the other route in the fallback pair becomes the active route.')
mibBuilder.exportSymbols("ZHONE-COM-IP-STATIC-ROUTE-MIB", staticRouteDest=staticRouteDest, staticRouteEntry=staticRouteEntry, staticRouteType=staticRouteType, staticRouteEnable=staticRouteEnable, staticRouteMetric=staticRouteMetric, comIpStaticRoute=comIpStaticRoute, staticRouteNetMask=staticRouteNetMask, staticRouteFallbackMetric=staticRouteFallbackMetric, PYSNMP_MODULE_ID=comIpStaticRoute, staticRoutePingFailMax=staticRoutePingFailMax, staticRoute=staticRoute, staticRouteTable=staticRouteTable, staticRouteIfNumber=staticRouteIfNumber, staticRouteNextHop=staticRouteNextHop, staticRoutePingInterval=staticRoutePingInterval, staticRouteRowStatus=staticRouteRowStatus)
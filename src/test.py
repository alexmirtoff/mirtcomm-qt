#!/usr/bin/env python3.5

import netsnmp

session = netsnmp.Session( DestHost='192.168.0.254', Version=2, Community='home' )
vars = netsnmp.VarList( netsnmp.Varbind('.1.3.6.1.2.1.1.1.0') )
print( session.get(vars) )

#!/bin/env python 

import re

#p = re.compile('(\d+\.\d+\.\d+.\d+)\s+([\^b]+)\s*\#?\s*(?:mac\s*=\s*([\d\:]+))?')
p = re.compile('^(\d+\.\d+\.\d+.\d+)\s+([^\b\#\s]+)\s*\#?\s*(?:mac\s*=\s*([\w\:]+))?')

with open('/etc/dnsmasq.d/hosts') as f:
    for l in f.readlines():
        m = p.match(l.strip())
        if m:
            ip, name, mac =  m.groups()
            # dhcp-host=b8:27:eb:00:26:e2,rasp,192.168.1.134
            if mac:
                print "dhcp-host={},{},{}".format(mac.lower(), name, ip)
            else:
                print "dhcp-host={},{}".format(name, ip)

        
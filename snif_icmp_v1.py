from scapy.all import *



sniff(iface= 'enp0s3', prn=lambda x:x.summary(), filter='icmp')

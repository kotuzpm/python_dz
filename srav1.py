from scapy.all import *

def find_pkt(tcpdump):
    tcpdump = PcapReader(tcpdump)
    for pkt in tcpdump:
        if pkt[TCP].flags == 'S':
            return pkt

def pkt_compare(pkt1, pkt2, pkt3):
    L2 = list(pkt1.fields.keys())
    L3 = list(pkt1[IP].fields.keys())
    L4 = list(pkt1[TCP].fields.keys())
    for field in L2:
        if pkt1.fields.get(field) != pkt2.fields.get(field) or pkt1.fields.get(field) != pkt3.fields.get(field):
            print(f'layer 2 {field} 1: {pkt1.fields.get(field)} 2: {pkt2.fields.get(field)} 3: {pkt3.fields.get(field)} ')
    for field in L3:
        if pkt1[IP].fields.get(field) != pkt2[IP].fields.get(field) or pkt1[IP].fields.get(field) != pkt3[IP].fields.get(field):
            print(f'layer 3 {field} 1: {pkt1[IP].fields.get(field)} 2: {pkt2[IP].fields.get(field)} 3: {pkt3[IP].fields.get(field)} ')
    for field in L4:
        if pkt1[TCP].fields.get(field) != pkt2[TCP].fields.get(field) or pkt1[TCP].fields.get(field) != pkt3[TCP].fields.get(field):
            print(f'layer 4 {field} 1: {pkt1[TCP].fields.get(field)} 2: {pkt2[TCP].fields.get(field)} 3: {pkt3[TCP].fields.get(field)} ')


pkt1 = find_pkt('./pydevops/nmap_ssh.pcap')
pkt2 = find_pkt('./pydevops/ssh_connection_client.pcap')
pkt3 = find_pkt('./pydevops/ssh_normal.pcap')
pkt_compare(pkt1, pkt2, pkt3)
    

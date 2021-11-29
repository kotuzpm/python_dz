from scapy.all import *
def pkt_handler(pkt):
    if pkt.haslayer('TCP'):
        src = f'{pkt[IP].src}:{pkt[TCP].sport}'
        dst = f'{pkt[IP].dst}:{pkt[TCP].dport}'
        if pkt[TCP].flags == 'S':
            socket = (src, dst)
            tcp_socket.append(socket)

        res =[i for i in tcp_socket if (src in i) and (dst in i)]
        wrpcap(f'{res}.pcap', pkt, append = True)

global tcp_socket
tcp_socket = list()
sniff(iface= 'enp0s3', prn=pkt_handler, filter='port 80')

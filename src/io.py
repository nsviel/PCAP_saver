#---------------------------------------------
from src import param
from src import terminal
from scapy.all import *

import os
import time


def open_pcap(path):
    pcap = scapy.utils.rdpcap(path)
    return pcap

def get_nb_paquet(pcap):
    nb = 0
    for pkt in pcap:
        if pkt.haslayer(UDP):
            nb += 1
    return nb

def write_pcap_by_packet(path, packet):
    #If the file is more than 1 Gb save new pcap in file
    path_out = path + "file_" + str(param.cpt_file) + ".pcap"

    #get file size and convert it into Gb
    if os.path.exists(path_out):
        size = os.path.getsize(path_out) / 1000000000
    else:
        size = 0

    if size < 0.1:
        if(len(packet) == 1248):
            wrpcap(path_out, packet, append=True)
    else:
        param.cpt_file = param.cpt_file + 1
        filename = "file_" + str(param.cpt_file) + ".pcap"
        terminal.addLog("#", "100 Mo reached, new save file [\033[1;32m%s\033[0m]"% filename)

def write_pcap(pcap, path, is_append):
    #get file size and convert it into Gb
    if os.path.exists(path):
        size = os.path.getsize(path) / 1000000000
    else:
        size = 0

    #If the file is more than 1 Gb save new pcap in file
    if size < 1:
        for pkt in pcap:
            if pkt.haslayer(UDP):
                wrpcap(path, pkt, append=is_append)  #appends packet to output file
            else:
                pass

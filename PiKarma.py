# coding=utf-8

# Modulles
import sys
import time
import argparse
from termcolor import colored
from argparse import RawTextHelpFormatter
import commands
import netifaces
from scapy.all import *
from termcolor import colored
from scapy.sendrecv import sendp
from time import gmtime, strftime
from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap, Dot11Beacon, Dot11Elt, Dot11ProbeResp
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


banner_intro = """

██████╗ ██╗██╗  ██╗ █████╗ ██████╗ ███╗   ███╗ █████╗
██╔══██╗██║██║ ██╔╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗
██████╔╝██║█████╔╝ ███████║██████╔╝██╔████╔██║███████║
██╔═══╝ ██║██╔═██╗ ██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║
██║     ██║██║  ██╗██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝

------------------------------------------------------
"""


DESCRIPTION = """

Detects wireless network attacks performed by KARMA module

PiKarma Methods =

1 : Identify and log only KARMA Attack
2 : Identify, attack and log KARMA Module activities
--------------------------------------------------------------------
"""

parser = argparse.ArgumentParser('PiKarma', description=DESCRIPTION, formatter_class=RawTextHelpFormatter)
parser.add_argument('-pm','--pikarma-method', required=True, dest="attack_method", type=str, help="PiKARMA attack methods")
parser.add_argument('-i', '--interface',required=True, help="Interface (Monitor Mode)", type=str)
args = parser.parse_args()


def logging(log):
	with open("/var/log/pikarma.log", "a") as f:
		f.write(str(log)+"\n")
		f.flush()
		f.close()

def sniff_channel_hop(iface):
    for i in range(1, 14):
        os.system("iwconfig " + iface + " channel " + str(i))
        sniff(iface=iface, count=4, prn=air_scan)


def air_scan(pkt):
    """
    Scan all network with channel hopping
    Collected all ssid and mac address information
    :param pkt:  result of sniff function
    """
    if pkt.haslayer(Dot11ProbeResp):
        ssid, bssid = pkt.info, pkt.addr2
        info = "{}=*={}".format(bssid, ssid)
        if info not in info_list:
            info_list.append(info)


def pp_analysis(info_list, pp, pisavar_method):
    """
    Analysis air_scan result for pineAP Suite detection
    """
    for i in info_list:
        bssid, ssid= i.split("=*=")
        if bssid not in pp.keys():
            pp[bssid] = []
            pp[bssid].append(ssid)
        elif bssid in pp.keys() and ssid not in pp[bssid]:
            pp[bssid].append(ssid)

    """
    Detects KARMA Attack.
    """
    for v in pp.keys():
        if len(pp[v]) >= 2 and v not in blacklist:
            print colored("\033[1m[*] KARMA Attack activity detected.", 'magenta', attrs=['reverse', 'blink'])
            print "\033[1m[*] MAC Address : ", v
            print "\033[1m[*] FakeAP count: ", len(pp[v])
 	    log_time = time.strftime("%c")
            blacklist.append(v)
            if pikarma_method == "2":
                pp_deauth(blacklist)
                log = log_time, "||", v, " - ", len(pp[v]), " - Deauth Attack"
                logging(log)
            elif pikarma_method == "1":
                log = log_time, "||", v, " - ", len(pp[v])
                logging(log)
    time.sleep(3)
    return blacklist


def find_channel(clist, v):
    for i in range(0, len(clist)):
        if clist[i].haslayer(Dot11ProbeResp) and clist[i].addr2 == v:
            channel = ord(clist[i][Dot11Elt:3].info)
    return channel


def pp_deauth(blacklist):
    """
    Starts deauthentication attack for PineAP Suite.
    """
    attack_start = "[*] Attack has started for " + str(blacklist)
    print colored(attack_start, 'red', attrs=['reverse', 'blink'])
    time.sleep(2)
    channel = 1
    for target in blacklist:
        clist = sniff(iface=iface, count=50)
        channel = find_channel(clist, target)
        deauth = RadioTap() / Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=target.lower(), addr3=target.lower()) / Dot11Deauth()
        sendp(deauth, iface=iface, count=120, inter=.2, verbose=False)
        time.sleep(1)
    print colored("[*] Attack has completed..", 'green', attrs=['reverse', 'blink'])
    time.sleep(2)


if __name__ == '__main__':
    path = "/var/log/pikarma.log"
    iface = args.interface
    mode  = "Monitor"
    pikarma_method = args.attack_method
    os.system("reset")
    now = time.strftime("%c")
    print banner_intro
    print "Information about test:"
    print "----------"*5
    print "[*] Start time: ", now
    print "[*] Detects KARMA Attack activity and starts deauthentication attack \n    (for fake access points - WiFi Pineapple, FruityWifi, MANA) "
    print "------------"*7
    while True:
        time.sleep(10)
        channel = 0
        blacklist = []
        info_list = []
        pp = {}
        sniff_channel_hop(iface)
        blacklist = pp_analysis(info_list, pp, pikarma_method)
        time.sleep(2)
        if len(blacklist)!=0:
            print "--------"*5

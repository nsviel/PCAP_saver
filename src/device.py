#---------------------------------------------
from src import param
import pcapy


def get_device_to_sniff():
    ok = False
    while(ok == False):
        devices = get_all_device()
        for i in range(0, len(devices)):
            print("\033[1;32m%d\033[0m. %s"%(i, devices[i]))
        dev_nb = input("Device: ")
        if(dev_nb != ""):
            ok = True
            dev = get_device_from_number(dev_nb)
            param.dev = dev

def get_device_from_number(nb):
    devices = pcapy.findalldevs()
    for i in range(0, len(devices)):
        if(i == int(nb)):
            return devices[i]

def get_all_device():
    devices = pcapy.findalldevs()
    for d in devices :
        if(d == "any"):
            devices.remove("any")
        elif(d == "lo"):
            devices.remove("lo")
        elif(d == "docker0"):
            devices.remove("docker0")
        elif(d == "dbus-system"):
            devices.remove("dbus-system")
        elif(d == "dbus-session"):
            devices.remove("dbus-session")
        elif(d == "bluetooth0"):
            devices.remove("bluetooth0")
        elif(d == "bluetooth-monitor"):
            devices.remove("bluetooth-monitor")
        elif(d == "nflog"):
            devices.remove("nflog")
        elif(d == "nfqueue"):
            devices.remove("nfqueue")
    return devices

def check_if_device_exists(name):
    devices = get_all_device()
    exist = False
    for d in devices :
        if(d == name):
            exist = True
            break
    return exist

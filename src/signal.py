#---------------------------------------------
from src import terminal
from src import param

import socket
import platform
import signal
import os
import sys


def signal_handler(sig, frame):
    param.run_loop = False
    print("")

signal.signal(signal.SIGINT, signal_handler)

def system_clear():
    os.system('clear')

def check_for_root():
    if not os.geteuid() == 0:
        terminal.addLog("error", "Only root can run this script")
        sys.exit()

def system_information(prog_name):
    check_for_root()

    #Info
    program = prog_name
    ip = get_ip_adress()
    hostname = socket.gethostname()
    arch = platform.architecture()[0]
    core = platform.uname()[2]
    proc = platform.processor()
    python = platform.python_version()

    try:
        OS = platform.freedesktop_os_release()['PRETTY_NAME']
    except:
        OS = platform.system()

    #Header
    print("    : : \033[1;34m%s\033[0m : :    "% program)
    print("-----------------------")
    print('%-10s' '\033[1;34m%s\033[0m' % ("IP", ip))
    print('%-10s' '\033[1;34m%s\033[0m' % ("Hostname", hostname))
    print('%-10s' '\033[1;34m%s\033[0m, \033[1;34m%s\033[0m' % ("Arch", arch, proc))
    print('%-10s' '\033[1;34m%s\033[0m' % ("OS", OS))
    print('%-10s' '\033[1;34m%s\033[0m' % ("Core", core))
    print('%-10s' '\033[1;34m%s\033[0m' % ("Python", python))
    print("-----------------------")

def get_ip_adress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

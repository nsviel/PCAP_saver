#!/usr/bin/env python3
#---------------------------------------------
from src import capture
from src import signal
from src import device
from src import param

import time


signal.system_clear()
signal.system_information("PCAP Saver")
#-------------

device.get_device_to_sniff()
capture.start_thread()
while param.run_loop:
    time.sleep(0.1)
capture.stop_thread()

#-------------
print("-----------------------")
print("Program \033[1;34mclosed\033[0m")

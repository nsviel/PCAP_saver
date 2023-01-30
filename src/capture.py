#---------------------------------------------
from src import device
from src import io
from src import terminal
from src import param

import pcapy
import multiprocessing


def start_thread():
    param.thread_capture = multiprocessing.Process(target=start_capture, args=())
    param.thread_capture.start()

def stop_thread():
    param.thread_capture.terminate()

def start_capture():
    listener = pcapy.open_live(param.dev , 1248 , 1 , 0)
    terminal.addLog("#", "Capture start on \033[1;32m%s\033[0m"% param.dev)
    terminal.addLog("#", "File saved at \033[1;32m%s\033[0m ... "% param.path_out)
    while param.run_loop:
        (header, packet) = listener.next()
        io.write_pcap_by_packet(param.path_out, packet)

import sys, io

from AppContainer import runFlask
from subdomains import root_system, server_system
from subdomains.server_system import server_init
from system_monitor import runtime_monitor
from multiprocessing import Process, freeze_support

if __name__ == '__main__' and server_init.init():
    monitor=Process(target=runtime_monitor)
    monitor.start()
    freeze_support()
    runFlask()
    monitor.kill()

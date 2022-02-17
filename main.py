import sys, io

from AppContainer import runFlask
from subdomains import root_system, server_system
from subdomains.server_system import server_init, server_monitor
from multiprocessing import Process, freeze_support

if __name__ == '__main__' and server_init.init():
    monitor=Process(target=server_monitor.run)
    monitor.start()
    freeze_support()
    runFlask()
    monitor.kill()

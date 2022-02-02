from AppContainer import runFlask
from subdomains import root_system, server_system
from subdomains.server_system import server_init

if __name__ == '__main__' and server_init.init():
    runFlask()

import os
import platform
import time

import psutil

from gputil import GPUtil

while True:
    os.system('cls')
    print(platform.platform())
    print(platform.machine() + " " + platform.processor() +" CPU: " + str(psutil.cpu_percent()))
    print("CPU Frequency: " + str(int(psutil.cpu_freq().current)))
    print('RAM: ' + str(int(int(psutil.virtual_memory().total - psutil.virtual_memory().available))) + " B / " + str(int(psutil.virtual_memory().total)))
    print(GPUtil.showUtilization())
    time.sleep(1)

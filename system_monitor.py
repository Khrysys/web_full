import psutil, os, time
while True:
    os.system('cls')
    print("CPU: " + str(psutil.cpu_percent()))
    print("CPU Frequency: " + str(int(psutil.cpu_freq().current)))
    print('RAM: ' + str(int(int(psutil.virtual_memory().total - psutil.virtual_memory().available))) + " B / " + str(int(psutil.virtual_memory().total())))
    time.sleep(1)
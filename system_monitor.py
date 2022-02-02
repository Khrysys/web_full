import psutil, os, time
while True:
    os.system('cls')
    print("CPU: " + str(psutil.cpu_percent()))
    print("CPU Frequency: " + str(int(psutil.cpu_freq().current)))
    time.sleep(1)
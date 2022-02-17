import collections

import numpy as np
import psutil
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

length = 100

dsk_u = collections.deque(np.zeros(length))
ram_u = collections.deque(np.zeros(length))
cpu_f = collections.deque(np.zeros(length))
cpu_u = collections.deque(np.zeros(length))
x = np.zeros(length)

max_cpu = psutil.cpu_freq().max

fig, ((cpu_util, cpu_freq), (ram_util, dsk_util)) = plt.subplots(nrows=2, ncols=2)
fig.patch.set_facecolor('k')

cpu_util.xaxis.set_visible(False)
cpu_util.yaxis.set_visible(False)
cpu_freq.xaxis.set_visible(False)
cpu_freq.yaxis.set_visible(False)
ram_util.xaxis.set_visible(False)
ram_util.yaxis.set_visible(False)
dsk_util.xaxis.set_visible(False)
dsk_util.yaxis.set_visible(False)

def update(i):
    cpu_u.popleft()
    cpu_f.popleft()
    ram_u.popleft()
    dsk_u.popleft()

    cpu_u.append(psutil.cpu_percent())
    cpu_f.append(psutil.cpu_freq().current)
    ram_u.append(psutil.virtual_memory().percent)
    dsk_u.append(psutil.disk_usage('C:\\').percent)

    if cpu_u[-1] >= 75:
        cpu_util.set_facecolor('r')
    elif cpu_u[-1] >= 50:
        cpu_util.set_facecolor('y')
    else:
        cpu_util.set_facecolor('g')

    if cpu_f[-1] >= 3000:
        cpu_freq.set_facecolor('r')
    if cpu_f[-1] >= max_cpu:
        cpu_freq.set_facecolor('y')
    else:
        cpu_freq.set_facecolor('g')

    if ram_u[-1] >= 75:
        ram_util.set_facecolor('r')
    elif ram_u[-1] >= 50:
        ram_util.set_facecolor('y')
    else:
        ram_util.set_facecolor('g')
    
    if dsk_u[-1] >= 95:
        dsk_util.set_facecolor('r')
    elif dsk_u[-1] >= 75:
        dsk_util.set_facecolor('y')
    else:
        dsk_util.set_facecolor('g')

    cpu_util.cla()
    cpu_freq.cla()
    ram_util.cla()
    dsk_util.cla()

    cpu_util.plot(cpu_u)
    cpu_util.scatter(len(cpu_u)-1, cpu_u[-1])
    cpu_util.text(len(cpu_u)-1, cpu_u[-1]+2, "{}%".format(cpu_u[-1]), color='w')
    cpu_util.set_ylim(0, 100)

    cpu_freq.plot(cpu_f)
    cpu_freq.scatter(len(cpu_f)-1, cpu_f[-1])
    cpu_freq.text(len(cpu_f)-1, cpu_f[-1]+2, "{}MHz".format(cpu_f[-1]), color='w')
    cpu_freq.set_ylim(0, 4000)

    ram_util.plot(ram_u)
    ram_util.scatter(len(ram_u)-1, ram_u[-1])
    ram_util.text(len(ram_u)-1, ram_u[-1]+2, '{}%'.format(ram_u[-1]), color='w')
    ram_util.set_ylim(0, 100)

    dsk_util.plot(dsk_u)
    dsk_util.scatter(len(dsk_u)-1, dsk_u[-1])
    dsk_util.text(len(dsk_u)-1, dsk_u[-1]+2, '{}%'.format(dsk_u[-1]), color='w')
    dsk_util.set_ylim(0, 100)

    fig.savefig('subdomains/server_system/sv.png')


def run():
    ani = FuncAnimation(fig, update, interval=1000)

    plt.show()
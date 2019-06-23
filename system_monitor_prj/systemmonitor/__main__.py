#!/usr/bin/env python
import psutil
import time
import configparser
import json
import os
from datetime import datetime


class Systemmonitor:
    """Systemmonitor app ver.1"""

    cpuload = psutil.cpu_percent(interval=1, percpu=False)

    @staticmethod
    def output():
        print('CPU data has collected')


print(Systemmonitor.__doc__)

end = Systemmonitor()

discusage = disk_percent = psutil.disk_usage('/')[3]
totalvirtmem = psutil.virtual_memory().total
readcount = psutil.disk_io_counters()[0]
netinfo = psutil.net_io_counters().bytes_sent

conf = configparser.ConfigParser()
conf.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))

interval = conf.get('common', 'interval')
fileformat = conf.get('common', 'output')
quantity = conf.get('common', 'quantity')

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

file = open("syslog." + fileformat, "w")

for i in range(1, int(interval) + 1):
    if fileformat == "json":
        prints = json.dumps({
            "SNAPSHOT": str(i),
            "Timestamp": timestamp,
            "CPU_load_info,%": Systemmonitor.cpuload,
            "Memory_info": discusage,
            "Virtual_memory_info": totalvirtmem,
            "IO_info": readcount,
            "Network_info": netinfo
        }, indent=4)
        file.write(prints)
        time.sleep(int(interval))
    elif fileformat == "txt":
        prints = "SNAPSHOT :" + str(i) + " " + \
                 timestamp + ":" + \
                 "CPU_load_info,%:" + str(Systemmonitor.cpuload) + " " + \
                 "Memory_info:" + str(discusage) + " " + \
                 "Virtual_memory_info:" + str(totalvirtmem) + " " + \
                 "IO_info:" + str(readcount) + " " + \
                 "Network_info:" + str(netinfo) + "\n"
        file.write(prints)
        time.sleep(int(interval))

    end.output()

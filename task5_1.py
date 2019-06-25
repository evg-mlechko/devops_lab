import sys
import subprocess
import json
import yaml
import os
from pip._internal.operations import freeze


class Versions:
    """Info about the versions of python"""


li = []
file = open("syslog.json", "w")
m = os.environ['VIRTUAL_ENV'].split('/')
env = m[len(m) - 1]
k = subprocess.getoutput("which pip")
x = freeze.freeze()
for p in x:
    li.append(p)


def output():
    print('1. Python version is: ' + sys.version[:5])
    print('2. Using next virtual enviroment: ' + env)
    print('3. Python executable location is: ' + str(sys.executable))
    print('4. Pip location is: ' + k)
    print('5. Pythonpath location is: ' + sys.prefix)
    print('6. Pythonpath installed packages: ' + str(li))
    print('7. Site packages location is: ' + next(p for p in sys.path if 'site-packages' in p))


output()
prints = json.dumps({
    "Python version": str(sys.version[:5]),
    "In use virtual enviroment": str(sys.prefix),
    "Python executable location": str(sys.executable),
    "Pip location": k,
    "Pythonpath location": sys.prefix,
    "Pythonpath installed packages": str(li)
    }, indent=4)

file.write(prints)

data = dict(
    Python_version=str(sys.version[:5]),
    In_use_virtual_enviroment=str(sys.prefix),
    Python_executable_location=str(sys.executable),
    Pip_location=k,
    Pythonpath_location=sys.prefix,
    Pythonpath_installed_packages=str(li),
)

with open('data.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)


end = Versions()

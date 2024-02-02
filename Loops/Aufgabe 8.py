import subprocess
mac = subprocess.run(["cat /sys/class/net/enp3s0/address | tr -d '\n'"], shell=True, capture_output=True, text=True)
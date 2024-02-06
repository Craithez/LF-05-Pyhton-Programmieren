import psutil
hexset = psutil.net_if_addrs()
mac_address = hexset['Ethernet'][0].address
print(mac_address)

#kA wieso er es sich so schwer macht, psutil ist auf Linux und Windows mit den gleichen Befehlen bedienbar.
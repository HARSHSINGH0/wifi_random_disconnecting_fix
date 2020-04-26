import os
from time import sleep
import subprocess
import random

hosts = 'google.com'

def check_ping():
    
    host = hosts
    
    print(f"\t\n-========- Pinging {host} -========-")
    
    try:
        response = subprocess.check_output(
            ['ping', '-c', '1', host],
            stderr=subprocess.STDOUT,  # get all output
            universal_newlines=True  # return string not bytes
        )
        if 'Destination host unreachable' in response:
            print('Host Not Reachable')
            response = None
        else:
            response = 0
    except Exception:
    	response=None
    if response == 0:
        pingstatus = "active"
        print("\t\n-========- Network Active -========-")
    else:
        pingstatus = "inactive"
        print("\t\n-========- Network Error -========-")
        print("\nReconnecting...")
        os.system('netsh wlan connect name="Xiaomi_C3BF(PUT YOUR ROUTER NAME)"')
        sleep(8)
        
    if pingstatus == 'active':
        print("\nChecking again in 10 seconds")    
        sleep(10)

while True:
    check_ping()

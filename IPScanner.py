import os
from threading import Thread

def search(ip_address):
    commando = " ping -c 1 " + ip_address
    response = os.popen(commando).read() #string
    if "1 received "in response:
        print("Encontrado en : ", ip_address)
        print(commando)
 
for ip in range ( 1 , 255 ):
    current_ip = " 10.24.3." + str(ip)
    print(" Analizando la ip : ", current_ip )


# IP 10.24.3.17
# Gateway 10.24.3.254
# Mask 255.255.254.0
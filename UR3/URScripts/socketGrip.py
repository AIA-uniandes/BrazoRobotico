##
import socket
import time
import os

HOST = "157.253.197.57" #Robot IP
PORT = 30002

s_ur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_ur.connect((HOST, PORT))

##
#Lectura del archivo de Succión (Grip)
file = open(os.getcwd() + '\\vg_grip.txt',mode='r')
all_of_it0 = file.read()
file.close()

#Lectura del archivo de liberación
file = open(os.getcwd() + '\\vg_release.txt',mode='r')
all_of_it1 = file.read()
file.close()

## Ejecución del VG GRip
time.sleep(2)
s_ur.send(("set_digital_out(0,True)"+"\n"+all_of_it0).encode('utf8'))

## Ejecución del VG Release
time.sleep(1)
s_ur.send(("set_digital_out(0,True)"+"\n"+all_of_it1).encode('utf8'))

## Close
s_ur.close()



##


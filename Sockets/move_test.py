import socket
#import struct
import time

#Server creation	
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 31001))
serversocket.listen(5) #5 eingehende Verbindungen erlauben

HOST = "157.253.197.145"    # The remote host #Cambiar
PORT = 30002              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Obligatorio (https://www.zacobria.com/universal-robots-knowledge-base-tech-support-forum-hints-tips-cb2-cb3/index.php/ur-script-send-commands-from-host-pc-to-robot-via-socket-connection/)

s.connect((HOST, PORT))

s.send(("movej([-0.5, -0.94, 1.91, -0.90, 1.08, 3.90], a=1.0, v=0.3)" + "\n").encode("utf8"))
time.sleep(10)


s.send (("set_tool_voltage(24)" + "\n").encode("utf8"))
s.send (("set_digital_out(8,False)" + "\n").encode("utf8"))


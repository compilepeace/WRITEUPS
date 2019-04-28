import socket
import struct


host_ip = socket.gethostbyname('vortex.labs.overthewire.org')
port = 5842

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.connect((host_ip, port))

data = so.recv(1024)


print host_byte_order


for i in range(0, 4):
	payload += int(host_byte_order[i])


so.send(str(payload))
print payload

username = so.recv(1024)
password = so.recv(1024)

print username 
print password 

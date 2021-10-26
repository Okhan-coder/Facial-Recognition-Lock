import socket

port = 4210
#ip = "192.168.4.1"	# Default address of ESP
ip = "10.36.68.5"
#msg = bytes("Message to send","utf-8")
msg = "Message to send"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(msg , (ip, port))

print("test") 

import socket
import sys

def get_ports(address,min_port,max_port):
	found_ports=[]
	while min_port <= max_port:
		s=socket.socket()
		try:
			s.connect((address,min_port))
		except Exception as e:
			print('Error',e)
			min_port += 1
			continue
		else:
			found_ports.append(min_port)
			min_port += 1
			continue

	return found_ports






def main():
	target = input('What you want to scan?: ')
	address = socket.gethostbyname(target)
	min_port = input("Type Min Port :")
	max_port = input("Type Max Port : ")
	min_port=int(min_port)
	max_port=int(max_port)

	ports = get_ports(address, min_port, max_port)
	for p in ports:
		print(p)

main()



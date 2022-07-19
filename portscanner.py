#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
	found_ports = []
	while min_port <= max_port:
		s = socket.socket()
		try:
			s.connect((address, min_port))
		except Exception as e:
			print("Error occured", e)
			min_port += 1
			continue
		else:
			found_ports.append(min_port)
			min_port += 1
			continue

	return found_ports


def main():
	address = sys.argv[1]
	min_port = int(sys.argv[2])
	max_port = int(sys.argv[3])
	ports = get_accessible_ports(address, min_port, max_port)
	for p in ports:
		print(p)

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len() != 4:
		print('usage: python %s address min_port max_port' % [0])
	else:
		main()

# Fall 2016 CSci4211: Introduction to Computer Networks
# This program serves as the server of DNS query.
# Written in Python v3.

import sys, threading, os
from socket import *

def main():
	host = "localhost" # Hostname. It can be changed to anything you desire.
	port = 5001 # Port number.

	#create a socket object, SOCK_STREAM for TCP

	#bind socket to the current address on port 5001

	#Listen on the given socket maximum number of connections queued is 20
	

	monitor = threading.Thread(target=monitorQuit, args=[])
	monitor.start()

	print("Server is listening...")

	while 1:
		#blocked until a remote machine connects to the local port 5001
		connectionSock, addr = sSock.accept()
		server = threading.Thread(target=dnsQuery, args=[connectionSock, addr[0]])
		server.start()

def dnsQuery(connectionSock, srcAddress):

	hostName = connectionSock.recv(1024).decode() # Receive from client.

	DNS_Cache = "DNS_mapping.txt"
	open(DNS_Cache, "a") # Create if not existssxz

	#check the DNS_mapping.txt to see if the host name exists
	for line in open(DNS_Cache).read():
		if line.contains(hostName):
			result = "Local DNS:" + line.trim()
			connectionSock.send(result.encode())
	
	try:
		cSock = socket(AF_INET, SOCK_STREAM)
	except error as msg:
		cSock = None # Handle exception

	result = "Root DNS:" + hostName + cSock.getHostByName(hostName)
	with open(DNS_Cache, "a") as mapping:
		mapping.write(result)
	connectionSock.send(result.encode())


	#set local file cache to predetermined file.
        #create file if it doesn't exist 
        #if it does exist, read the file line by line to look for a
        #match with the query sent from the client
	#If no lines match, query the local machine DNS lookup to get the IP resolution
	#write the response in DNS_mapping.txt
	#print response to the terminal
	#send the response back to the client
	#Close the server socket.
   
	

def monitorQuit():
	while 1:
		sentence = input()
		if sentence == "exit":
			os.kill(os.getpid(),9)

main()

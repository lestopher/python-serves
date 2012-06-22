# simple illustration client/server pair; client program sends a string
# to server, which echoes it back to the client (in multiple copies),
# and the latter prints to the screen

import socket
import sys
# This is the client

# Create a socket

pySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server

host = sys.argv[1] # Server Address
port = int(sys.argv[2]) # Server Port

pySocket.connect((host, port))


# Read echo

i = 0

while (1):
  msg = pySocket.recv(4096) # Get message about username
  if msg == 'Please enter a username':
    print msg
 
    handle_name = raw_input()
    pySocket.send(handle_name)
  
  data = pySocket.recv(4096) # Read up to this many bytes
  if data:
    print data
    talk_to_me = raw_input()
    if talk_to_me == "exit()":
      break
    else:
      pySocket.send(talk_to_me)
  else:
    continue
    
  

#close the connection
pySocket.close()

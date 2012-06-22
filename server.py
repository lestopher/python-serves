
import signal
import socket
import sys

def signal_handler(signal, frame, conn):
  print 'Received interrupt from keyboard <ctrl+c>'
  conn.close()
  sys.exit(0)

# Function: get_username
# Parameters: conn (socket datatype), users (list datatype)
# Usage: prompts user for username and returns the username as a string
def get_username(conn, users):
  msg = 'Please enter a username'
  err = 'A user with that handle already exists' 

  while 1:
    conn.send(msg)
    username = conn.recv(100)

    # if it doesn't find username, it enqueues
    # else prompts for new username
    try:
      users.index(username)
      conn.send(err)
      continue
    except ValueError:
      return username

# Function: show_users
# Parmeters: users (list dattype)
# Usage: shows current users connected to server
def show_users(users):
  i = 0

  for i in len(users):
    print users[i]

  return
#
# Begin our "main"
#

signal.signal(signal.SIGINT, signal_handler)

# User list
users = []
# Create a socket
pySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '' # Doesn't need to be defined server side

# Associate socket with a port, it can be default 33333 or arg[1] on cmd line
if len(sys.argv) < 2:
  port = 33333
else:
  port = int(sys.argv[1])

pySocket.bind((host, port))

# Accept a call from the client
pySocket.listen(1)

# If we accept a connection, we prompt the user for a handle
conn, addr = pySocket.accept()
print 'client is at ', addr
# Prompt connected user for handle
username = get_username(conn, users)

print 'Client at', addr, 'is using handle', username
conn.send("Connected to server")
while 1:

  data = conn.recv(4096)

  if data == "disconnect()":
    break
  if data == "/showusers":
    show_users(users)
  else:
    data = "Received message: " + data
    conn.send(data)

# Close the connection
conn.close()
  

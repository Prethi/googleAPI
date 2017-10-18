#File Transfer - Server
 
import sys
import socket
import os
 
host = ''

# Create Socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Reuse address
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to address and port
server.bind((host,2525))

# Listen to client connection
server.listen(1)

print "Server Active"

filefound = 0
 
while True:
    try:
        # Accept connection from the client
        conn,address = server.accept()
        print 'Connection from client: ', address
    except:
        # Break if accept error
        print 'Accept error'
        break

    # Receive file name from client
    filename = conn.recv(1024)

    # Check for the file in directory
    for file in os.listdir("/Users/prethi/pre"):
        if file == filename:
            filefound = 1
            break
 
    if filefound == 0:
        print "'"+filename+"' Not Found On Server"
 
    else:
        print "File '"+filename+"' found"

        # Use rb(read binary format to open the file)
        fp = open("/Users/prethi/pre/"+filename,"rb")
        readbuff = fp.read(1024)
        i = 1
        while readbuff:
            # Send file data to the client
            print 'Sending data to client ', i
            conn.send(readbuff)
            readbuff = fp.read(1024)
            i = i + 1
        print "Sending Completed"
    break
 
conn.close()
server.close()

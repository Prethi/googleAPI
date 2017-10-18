#file Transfer - Client

import sys
import socket
import readline


def recvfile(client, filename):
    """ send file name and recvfile """

    print recvfile.__doc__

    sData = ""

    while True:
        print 'Sending file name to client'
        client.send(filename)

        print 'Receiving data from server'
        sData = client.recv(1024)
        #print 'sData: ', sData
        
        if sData == 'File not present':
            print 'File not present on the server'
            return True
        if sData == '':
            print 'No response from the server'
            return False

        print 'Open file with filename in write mode'
        fDownloadFile = open(filename,"wb")
        print 'Writing into file'
        while sData:
            print 'debug 1'
            fDownloadFile.write(sData)
            sData = client.recv(1024)
            print 'received data'
        print "Download Completed"
        return True

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1",2525))
    while True:
        #filename = raw_input("Enter Filename to download from server : ")
        #recvfile()
        userinput = raw_input("Enter Filename to download from server or just press enter to exit: ")
        if userinput != "":
            print 'userinput = ', userinput
            result = recvfile(client, userinput)
            if not result:
                print 'Terminating client'
                break
        else:
            client.send('Closing connection')
            print 'Closing connection'
            break
    client.close()

if __name__ == '__main__':
    main()


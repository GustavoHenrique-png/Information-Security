from distutils.log import error
import ipaddress
from socket import *

def honeyPot():
    ipAdress = ""
    port = 80

    try:
        getConnection = socket(AF_INET,SOCK_STREAM)
        getConnection.bind((ipAdress,port))
        getConnection.listen(10)
        while True:
            clientConnection,clientAdress = getConnection.accept()
            print(clientAdress[0])
            data = clientConnection.recv(1024)
            print(data.decode('utf-8'))
        
    except error as identifier:
        print("Error: " + identifier)
    except KeyboardInterrupt as ky:
        print("Error: " + ky)
    finally:
        getConnection.close()
    getConnection.close()

if __name__ == "__honeyPot__":
    honeyPot()
import socket

#lame code
#need to fix this

def init():
    try:
        socket.create_connection(("www.google.com", 80))
        isconnected = True
    except:
        isconnected = False

    return isconnected



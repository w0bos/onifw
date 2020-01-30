import os
import socket


def init():
    try:
        socket.create_connection(("www.google.com", 80))
        isconnected = True
    except:
        isconnected = False

    return isconnected



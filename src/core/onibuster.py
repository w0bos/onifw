#!/bin/python3

import requests
from sys import argv as args
import socket


'''
Main component of onibuster
@params
    rhost: target
    rport: port to use
    wordlist: dictionnary file
'''

def show_help():
    print("[!] - Wrong arguments")
    print("Usage: ./onimap [rhost] [rport] [wordlist]")


try:
    rhost = args[1]
    rport = args[2]
    dictf = args[3]
except IndexError:
    show_help()
    exit()

flag = 0
with open(dictf, encoding="utf-8", errors="ignore") as f:
    content = [line.rstrip('\n') for line in f]
    try:
        socket.create_connection((rhost, rport))
        print("[*] - Starting to look for directories...")
        for i in content:
            if i.startswith('#'):
                pass

            else :
                if len(i) > 1:
                    code = requests.get("http://"+rhost+"/"+i).status_code
                    if code in [200,300,301,307,308,401,403,407]:
                        print("[*] - {0} is a valid directory - Code {1}".format(i, code))
                        flag = 1
        if flag == 1:
            print("[*] - Done.")
        else:
            print("[!] - No directory found with the given wordlist")
    except:
        print("[!] - Host unreachable")
f.close()

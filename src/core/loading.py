from sys import stdout
from random import choice
from threading import Thread
from time import sleep
from socket import create_connection
#import setup


def init():
    try:
        create_connection(("www.google.com", 80))
        isconnected = True
    except:
        isconnected = False

    return isconnected

def loadingHack(importlib):
	chaine = "[*] -"+' Loading the framework'
	charspec = ")@€]£+-$>*.`X%{_/&\\#}[~!(?;^§<"

	while importlib.is_alive():
		chainehack = ""
		for c in chaine:
			chainehack += c
			r = choice(charspec) + choice(charspec) + choice(charspec)
			if len(chainehack + r) <= len(chaine):
				pass
			else:
				r = ""
			stdout.write('\r' + chainehack + r + "...")
			sleep(0.06)

def loadingUpper(importlib):
	string = " Loading the framework"
	string = list(string)
	nb = len(string)

	while importlib.is_alive():
		x = 0
		while x < nb:
			c = string[x]
			c = c.upper()
			string[x] = c
			stdout.write("\r[*] - " + ''.join(string) + '...')
			sleep(0.06)
			c = string[x]
			c = c.lower()
			string[x] = c
			x += 1


def thread_loading():
	num = choice([1,2])
	importlib = Thread(target = init)
	importlib.start()
	if num == 1:
		load = Thread(target = loadingHack(importlib))
	elif num == 2:
		load = Thread(target = loadingUpper(importlib))
	load.start()
	importlib.join()
	load.join()

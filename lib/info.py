#!/usr/bin/python

import sys
import os
import random
import configparser
import socket

import api.installer as instl

def clearScr():
    os.system('clear')

alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"

from getpass import getpass
from time import gmtime, strftime, sleep

installDir = os.path.dirname(os.path.abspath(__file__)) + '/../'
print(installDir)


toolDir = installDir + 'tools/'
logDir = installDir + 'log/'

class color:
    HEADER =    '\033[96m'
    IMPORTANT = '\033[35m'
    NOTICE =    '\033[32m'
    OKBLUE =    '\033[94m'
    OKGREEN =   '\033[92m'
    WARNING =   '\033[91m'
    RED =       '\033[31m'
    END =       '\033[0m'
    LOGGING =   '\033[93m'
    WHITE =     '\033[97m'


class nmap:
    def __init__(self):
        self.installDir = toolDir + "nmap"

        self.targetPrompt = color.LOGGING + "nmap > Enter Target IP/Subnet/Range/Host: " + color.WHITE

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))

    def install(self):
        instl.Installer(0, installDir, ["nmap"])

    def run(self):
        target = input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        print("   Nmap scan for: %s\n" % target)
        print("   1 - Simple Scan [-sV]")
        print("   2 - Port Scan [-Pn]")
        print("   3 - Operating System Detection [-A]\n")
        print("   99 - Return to information gathering menu \n")
        response = input(color.LOGGING + "nmap > " + color.WHITE)
        clearScr()
        logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("nmap -sV -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "2":
                os.system("nmap -Pn -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "3":
                os.system("nmap -A -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

class xsstrike:
    def __init__(self):
        self.installDir = toolDir + "xsstrike"
        if not self.installed():
            self.install()
            clearScr()
        response = input(color.LOGGING + "xsstrike > Enter a command (leave blank if unsure) :" + color.WHITE)
        self.run(response)
        

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["xsstrike"])

    def run(self, response):
        if not len(response):
            os.system("python %s/xsstrike.py -h" % (self.installDir))
        else :
            os.system("python %s/xsstrike.py %s" % (self.installDir, response))

class doork:
    def __init__(self):
        self.installDir = toolDir + "doork"

        if not self.installed():
            self.install()
            clearScr()

        target = input(color.LOGGING + "doork > Enter a Target: " + color.WHITE)
        self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["doork"])

    def run(self, target):
        if not "http://" in target:
            target = "http://" + target
        logPath = "logs/doork-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        try:
            os.system("python2 %s/doork.py -t %s -o %s" %
                      (self.installDir, target, logPath))
        except KeyboardInterrupt:
            pass

class crips:
    def __init__(self):
        self.installDir = toolDir + "crips"

        if not self.installed():
            self.install()
            clearScr()

        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir) or os.path.isdir("/usr/share/doc/Crips"))

    def install(self):
        instl.Installer(0, installDir, ["crips"])
        

    def run(self):
        try:
            os.system("python2 %s/crips.py" % self.installDir)
        except:
            pass

class wpscan:
    def __init__(self):
        self.installDir = toolDir + "wpscan"

        if not self.installed():
            self.install()
            clearScr()
        target = input(color.LOGGING + "wpscan > Enter a Target: " + color.WHITE)
        self.menu(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["wpscan"])

    def menu(self, target):
        print("   WPScan for: %s\n" % target)
        print("   1- Username Enumeration [--enumerate u]")
        print("   2 - Plugin Enumeration [--enumerate p]")
        print("   3 - All Enumeration Tools [--enumerate]\n")
        print("   r - Return to information gathering menu \n")
        response = input(color.LOGGING + "wpscan > " + color.WHITE)
        clearScr()
        logPath = "../../logs/wpscan-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        wpscanOptions = "--no-banner --random-agent --url %s" % target
        try:
            if response == "1":
                os.system(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate u --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "2":
                os.system(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate p --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "3":
                os.system(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "r":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

class setoolkit:
    def __init__(self):
        self.installDir = toolDir + "setoolkit"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isfile("/usr/bin/setoolkit"))

    def install(self):
        instl.Installer(0, installDir, ["settoolkit"])

    def run(self):
        os.system("sudo setoolkit")

class host2ip:
    def __init__(self):
        host = input(color.LOGGING + "host2ip > Enter a Host: " + color.WHITE)
        ip = socket.gethostbyname(host)
        print("[*] - %s has the IP of %s" % (host, ip))


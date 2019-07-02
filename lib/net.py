#!/usr/bin/python

import sys
import os

import api.installer as instl

def clearScr():
    os.system('clear')


alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"

installDir = os.path.dirname(os.path.abspath(__file__)) + '/../'



toolDir = installDir + 'tools/'
logDir = installDir + 'log/'


class apwps:
    def __init__(self):
        self.installDir = toolDir + "apwps"

        if not self.installed():
            self.install()
        clearScr()
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["apwps"])

    def run(self):
        os.system("python2 %s/autopixie.py" % self.installDir)

class snmp:
    def __init__(self):
        self.installDir = toolDir + "snmp"

        if not self.installed():
            self.install()
        clearScr()
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["snmp"])

    def run(self):
        target = input("Enter Target IP: ")
        os.system("python2 %s/snmpbrute.py -t %s" % (self.installDir,target))

class pyphi:
    def __init__(self):
        os.system("wget http://pastebin.com/raw/DDVqWp4Z --output-document=pypisher.py")
        clearScr()
        os.system("mv pypisher.py %spypisher.py" % (toolDir))
        os.system("python2 %spypisher.py" % (toolDir))

class stmp:
    def __init__(self):
        os.system("wget http://pastebin.com/raw/Nz1GzWDS --output-document=smtp.py")
        clearScr()
        os.system("mv smtp.py %ssmtp.py" % (toolDir))
        os.system("python2 %ssmtp.py" % (toolDir))

class ssltrip:
    def __init__(self):
        self.installDir = toolDir + "sslstrip"

        if not self.installed():
            self.install()
        clearScr()
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["ssltrip"])

    def run(self):
        target = input("Enter Target IP: ")
        os.system("python2 %s/sslstrip.py" % (self.installDir))


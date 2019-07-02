#!/usr/bin/python

import sys
import os

import api.installer as instl

def clearScr():
    os.system('clear')


alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"

installDir = os.path.dirname(os.path.abspath(__file__)) + '/../'

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

toolDir = installDir + 'tools/'
logDir = installDir + 'log/'

alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"

class cupp:
    
    def __init__(self):
        self.installDir = toolDir + "cupp"

        if not self.installed():
            self.install()
            clearScr()
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["cupp"])

    def run(self):
        os.system("python %s/cupp.py -i" % self.installDir)

class brutex:
    def __init__(self):
        self.installDir = toolDir + "brutex"

        if not self.installed():
            self.install()
        
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        if not os.path.isdir("/usr/share/brutex"):
            os.system("sudo mkdir /usr/share/brutex")
        instl.Installer(0, installDir, ["brutex"])

    def run(self):
        target = input(color.LOGGING + "BruteX > " + color.WHITE + "Enter Target IP: ")
        os.system("brutex %s" % target)

class leviathan:
    
    def __init__(self):
        self.installDir = toolDir + "leviathan"

        if not self.installed():
            self.install()
            clearScr()
        self.run()


    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["leviathan"])
    def run(self):
        os.system("python2 %s/leviathan.py -i" % self.installDir)
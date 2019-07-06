#!/usr/bin/python

import sys
import os

def clearScr():
    os.system('clear')

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

alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"

import api.installer as instl

installDir = os.path.dirname(os.path.abspath(__file__)) + '/../'

toolDir = installDir + 'tools/'
logDir = installDir + 'log/'


class nikto:
    def __init__(self):
        self.installDir = toolDir + "nikto"
        self.targetPrompt = color.IMPORTANT + "Nikto > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()
    def installed(self):
        return (os.path.isfile("%s/program/nikto.pl" % self.installDir))
    def install(self):
        instl.Installer(0, installDir, ["nikto"])
    def run(self):
        target = input(self.targetPrompt)
        self.menu(target)
    def menu(self, target):
        os.system("perl %s/program/nikto.pl -h %s" % (self.installDir, target))
               
class rscan:
    def __init__(self):
        self.installDir = toolDir + "rapidscan"
        if not self.installed():
            self.install()
        self.targetPrompt = color.LOGGING + "rscan > "  + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        target=input(self.targetPrompt)
        self.run(target)
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["rapidscan"])

    def run(self, target):
        os.system("python2 %s/rapidscan.py %s" % (self.installDir, target))

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

class arachni:
    def __init__(self):
        self.installDir = toolDir + "arachni"
        if not os.path.isdir(self.installDir):
            self.install()
        self.run()

    def install(self):
        instl.Installer(0, installDir, ["arachni"])

    def run(self):
        target = input(color.LOGGING + "Arachni > " + color.LOGGING + "Enter Target Hostname/URL: ")
        os.system("sudo arachni %s" %(target))

class sqlmap:
    def __init__(self):
        self.installDir = toolDir + "sqlmap"
        if not self.installed():
            self.install()
            self.run()
        else : self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["sqlmap"])


    def run(self):
        os.system("python2 %s/sqlmap.py --wizard" % (self.installDir))

class slowloris:
    def __init__(self):
        self.installDir = toolDir + "slowloris"
        self.targetPrompt = color.LOGGING + "slowloris > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            self.install()
        target = input(self.targetPrompt)
        self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["slowloris"])


    def run(self,target):
        os.system("python3 %s/slowloris.py %s" % (self.installDir, target))

class pwnloris:
    def __init__(self):
        self.installDir = toolDir + "pwnloris"
        self.targetPrompt = color.LOGGING + "pwnloris > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            self.install()
        target = input(self.targetPrompt)
        self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["pwnloris"])


    def run(self,target):
        os.system("python3 %s/pwnloris.py %s" % (self.installDir, target))

class atscan:
    def __init__(self):
        self.installDir = toolDir + "atscan"
        self.targetPrompt = color.LOGGING + "ATscan > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            self.install()

        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["atscan"])


    def run(self):
        os.system("perl %s/atscan.pl --interactive" % (self.installDir))

class hyde:
    def __init__(self):
        self.installDir = toolDir + "hyde"
        self.targetPrompt = color.LOGGING + "Hyde > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            self.install()
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        instl.Installer(0, installDir, ["hyde"])


    def run(self):
        os.system("python3 %s/hyde/main.py" % (self.installDir))

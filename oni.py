#!/usr/bin/env python

import configparser
import os
import random
import sys
import readline
import socket

#Api
import api.installer    as instl
import api.completer    as auto

#Libs
import lib.exploit      as ex
import lib.info         as ig
import lib.passw        as pwd
import lib.web          as web
import lib.net          as nt

def readcred():
    f = open("doc/Credits.txt")
    content = [line.rstrip('\n') for line in f]
    return content

def readvisual():
    f = open("doc/logo.txt")
    content = [line.rstrip('\n') for line in f]
    for i in content:
        print(i)

def readfile(file_dir):
    f = open(file_dir)
    content = [line.rstrip('\n') for line in f]
    return content

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
    #Text formatting
    BOLD =      '\033[1m'
    UNDER =     '\033[4m'

installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
configFile = installDir + "./settings.cfg"
config = configparser.ConfigParser()
config.read(configFile)

toolDir = installDir + config.get('onisettings', 'toolDir')
logDir = installDir + config.get('onisettings', 'logDir')
yes = config.get('onisettings', 'yes').split()

color_random = [color.HEADER, color.IMPORTANT, color.NOTICE, color.OKBLUE,
                color.OKGREEN, color.WARNING, color.RED, color.LOGGING]
random.shuffle(color_random)

onifw_title = color_random[0] + '''
 $$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$$\ $$\      $$\ 
$$  __$$\ $$$\  $$ |\_$$  _|$$  _____|$$ | $\  $$ |
$$ /  $$ |$$$$\ $$ |  $$ |  $$ |      $$ |$$$\ $$ |
$$ |  $$ |$$ $$\$$ |  $$ |  $$$$$\    $$ $$ $$\$$ |
$$ |  $$ |$$ \$$$$ |  $$ |  $$  __|   $$$$  _$$$$ |
$$ |  $$ |$$ |\$$$ |  $$ |  $$ |      $$$  / \$$$ |
 $$$$$$  |$$ | \$$ |$$$$$$\ $$ |      $$  /   \$$ |
 \______/ \__|  \__|\______|\__|      \__/     \__|\n                                                                           
'''

onifw_cmd = "onifw > "
version = "Version {%s}\n" % (config.get("onisettings","version"))

TaC = color.BOLD + color.WARNING + '''
    By using this framework you signify your acceptance that:   

    1.- You won't upload, download, distribute, transfer, any trademark,
        trade secret, copyrighted content, propietary or intellectual 
        property rights of any person;  

    2.- You won't use this tool for illegal or unethical purposes, including
        activities that give rise to criminal or civil liability;   

    3.- You won't use this tool in order to upload, download, distribute viruses,
        malwares, or any kind of malicious software;    

    4.- Under no event shall the author of onifw be responsible for any activities, 
        or misdeeds, made by using the framework.\n''' + color.END

def clearScr():
    os.system('clear')

def yesOrNo():
    return (input("Continue Y / N: ") in yes)

def check_connectivity():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        return False

def argeement():
    while not config.getboolean("onisettings", "agreement"):
        clearScr()
        print(TaC)
        agree = input(
            "You must agree to our terms and conditions first (Y/n) ").lower()
        if agree in yes:
            config.set('onisettings', 'agreement', '1')
        else:
            clearScr()
            print("You can't use onifw unless you accept terms of use")
            sys.exit(1)

def modhelp(msg):
    print(color.HEADER)
    print("%s framework help panel" % msg)
    print(color.NOTICE)
    print(color.BOLD + "    Command     Description" + color.END)
    print("    -------     -----------")
    print('''
    help        shows this panel
    list        list all %s tools
    return      leaves the %s module

    quit
        ''' % (msg.lower(), msg.lower()))
    print(color.WHITE)

def help():
    print(color.NOTICE + '''
    help                shows help
    info                starts info gathering module
    web                 starts the web module
    network             starts the network module
    exploit             starts the exploit module
    install             starts the installer, use install [package] if you
                        want to install specific packages

    show                misc
                        [logo] [title] [version] [credits]

    quit                quit program
        ''' + color.WHITE)

class onifw:

    def __init__(self):

        if not os.path.isdir(toolDir):  os.makedirs(toolDir)
        if not os.path.isdir(logDir):   os.makedirs(logDir)

        completer = auto.Autocomp(readfile("api/dict.txt"))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input(onifw_cmd + color.WHITE)
        
        
        if prompt == "help":            
            help()
            self.__init__()

        elif prompt == "quit":
            sys.exit(1)

        elif prompt == "clear":
            clearScr()
            self.__init__()

        elif prompt == "web":           
            webfw()
        
        elif prompt == "network":
            netfw()

        elif prompt == "info":
            infofw()

        elif prompt == "password":
            pwdfw()

        elif prompt == "exploit":
            expfw()
            
        elif prompt == "show title":
            print(onifw_title)
            self.__init__()

        elif prompt == "show logo":
            print(color.BOLD + color.IMPORTANT)
            readvisual()
            print(color.END + color.WHITE)
            self.__init__()
        
        elif prompt == "show version":
            print(color_random[random.randint(0,len(color_random)-1)])
            print(version)
            self.__init__()
            
        elif prompt == "show credits":
            print("All tools belong to their corresponding authors")
            out = readfile("doc/Credits.txt")
            print(color.BOLD + color.OKBLUE)
            for i in range(len(out)):
                print(out[i])
            print(color.END)
            print(color.OKGREEN + "Framework created by w0bos" + color.END + color.WHITE)
            self.__init__()
            
        # INSTALLER
        elif prompt[:7] == "install":

            if len(prompt) == 7:
                print(color.NOTICE)
                print("[*] - Usage : install [package] [-all]")
                print("      Multiple packages can be installed at once.")
                print("      Use [list] to see what packages are available")
                print(color.WHITE)
                self.__init__()
            if len(prompt) > 7:
                if prompt[8:12].lower() == "-all":
                    instl.Installer(0, installDir)
                    self.__init__()
                else :
                    tools = prompt[8:].split()
                    instl.Installer(0, installDir, tools)
                    self.__init__()

        elif prompt == "list" or prompt == "ls":
            instl.Installer(1, installDir)
            self.__init__()

        else:
            print(color.WARNING + "[!] - %s : unknown command" % prompt)
            self.__init__()



class webfw:
    def __init__(self):
        completer = auto.Autocomp(readfile("api/dict.txt"))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input("onifw.web > " + color.WHITE)

        if prompt == 'return':
            onifw()

        elif prompt == 'quit':
            sys.exit(0)

        elif prompt == "clear":
            clearScr()
            self.__init__()

        elif prompt == "list":
            self.showlist()

        elif prompt == "help":
            self.help()


        #Tools
        elif prompt == "nikto":
            web.nikto()
            self.__init__()

        elif prompt == "rapidscan":
            web.rscan()
            self.__init__()

        elif prompt == "brutex":
            web.brutex()
            self.__init__()

        elif prompt == "arachni":
            web.arachni()
            self.__init__()

        elif prompt == "sqlmap":
            web.sqlmap()
            self.__init__()

        elif prompt == "slowloris":
            web.slowloris()
            self.__init__()

        elif prompt == "pwnloris":
            web.pwnloris()
            self.__init__()

        elif prompt == "atscan":
            web.atscan()
            self.__init__()

        else:
            print(color.WARNING + "[!] - %s : unknown command" % prompt)
            self.__init__()

    def help(self):
        modhelp("Web")
        self.__init__()   

    def showlist(self):
        print(color.HEADER + "List of all web tools")
        print(color.NOTICE + '''
        nikto           
        rapidscan           
        brutex         
        arachni           
        sqlmap              
        slowloris           
        pwnloris            
        atscan              
        ''' + color.WHITE)
        self.__init__()

class netfw:
    def __init__(self):
        completer = auto.Autocomp(readfile("api/dict.txt"))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input("onifw.network > " + color.WHITE)

        if prompt == 'return':
            onifw()

        elif prompt == 'quit':
            sys.exit(0)

        elif prompt == "clear":
            clearScr()
            self.__init__()

        elif prompt == "list":
            self.showlist()

        elif prompt == "help":
            self.help()


        #Tools  
        elif prompt == "apwps":
            nt.apwps()
            self.__init__()

        elif prompt == "snmp":
            nt.snmp()
            self.__init__()
            
        elif prompt == "pyphi":
            nt.pyphi()
            self.__init__()
            
        elif prompt == "stmp":
            nt.stmp()
            self.__init__()
            
        elif prompt == "sslstrip":
            nt.ssltrip()
            self.__init__()

        else:
            print(color.WARNING + "[!] - %s : unknown command" % prompt)
            self.__init__() 

    def help(self):
        modhelp("Network")
        self.__init__()   

    def showlist(self):
        print(color.HEADER + "List of all network/wireless tools")
        print(color.NOTICE + '''
        apwps           
        snmp
        pyphi
        stmp
        sslstrip                    
        ''' + color.WHITE)
        self.__init__()

class infofw:
    def __init__(self):
        completer = auto.Autocomp(readfile("api/dict.txt"))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input("onifw.info > " + color.WHITE)

        if prompt == 'return':
            onifw()

        elif prompt == 'quit':
            sys.exit(0)

        elif prompt == "clear":
            clearScr()
            self.__init__()

        elif prompt == "list":
            self.showlist()

        elif prompt == "help":
            self.help()


        #Tools  
        elif prompt == "nmap":
            ig.nmap()
            self.__init__()

        elif prompt == "xsstrike":
            ig.xsstrike()
            self.__init__()

        elif prompt == "doork":
            ig.doork()
            self.__init__()

        elif prompt == "crips":
            ig.crips()
            self.__init__()

        elif prompt == "wpscan":
            ig.wpscan()
            self.__init__()

        elif prompt == "setoolkit":
            ig.setoolkit()
            self.__init__()

        elif prompt == "host2ip":
            ig.host2ip()
            self.__init__()

        else:
            print(color.WARNING + "[!] - %s : unknown command" % prompt)
            self.__init__() 

    def help(self):
        modhelp("Information")
        self.__init__()   

    def showlist(self):
        print(color.HEADER + "List of all information tools")
        print(color.NOTICE + '''
        nmap           
        xsstrike
        doork
        crips
        wpscan
        setoolkit
        host2ip                        
        ''' + color.WHITE)
        self.__init__()    

class pwdfw:
    def __init__(self):
        completer = auto.Autocomp(readfile("api/dict.txt"))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input("onifw.password > " + color.WHITE)

        if prompt == 'return':
            onifw()

        elif prompt == 'quit':
            sys.exit(0)

        elif prompt == "clear":
            clearScr()
            self.__init__()

        elif prompt == "list":
            self.showlist()

        elif prompt == "help":
            self.help()

        #Tools  
        elif prompt == "cupp":
            pwd.cupp()
            self.__init__()

        elif prompt == "brutex":
            pwd.brutex()
            self.__init__()

        elif prompt == "leviathan":
            pwd.leviathan()
            self.__init__()

        else:
            print(color.WARNING + "[!] - %s : unknown command" % prompt)
            self.__init__() 

    def help(self):
        modhelp("Password")
        self.__init__()   

    def showlist(self):
        print(color.HEADER + "List of all password tools")
        print(color.NOTICE + '''
        cupp           
        brutex
        leviathan                        
        ''' + color.WHITE)
        self.__init__()

class expfw:
    def __init__(self):
        completer = auto.Autocomp(readfile("api/dict.txt"))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input("onifw.exploit > " + color.WHITE)

        if prompt == 'return':
            onifw()

        elif prompt == 'quit':
            sys.exit(0)

        elif prompt == "clear":
            clearScr()
            self.__init__()

        elif prompt == "list":
            self.showlist()

        elif prompt == "help":
            self.help()

        #Tools  
        elif prompt == "microsploit":
            ex.microsploit()
            self.__init__()

        elif prompt == "poet":
            ex.poet()
            self.__init__()

        elif prompt == "weeman":
            ex.weeman()
            self.__init__()

        elif prompt == "sb0x" :
            ex.sb0x()
            self.__init__()

        elif prompt == "nxcrypt":
            ex.nxcrypt()
            self.__init__()

        elif prompt == "revsh":
            ex.revsh()
            self.__init__()

        else:
            print(color.WARNING + "[!] - %s : unknown command" % prompt)
            self.__init__() 

    def help(self):
        modhelp("Exploits")
        self.__init__()   

    def showlist(self):
        print(color.HEADER + "List of all exploit tools")
        print(color.NOTICE + '''
        microsploit           
        poet 
        weeman
        sb0x
        nxcrypt                        
        ''' + color.WHITE)
        self.__init__()


if __name__ == "__main__":
    try:
        argeement()
        clearScr()
        print(onifw_title + version + color.WHITE)
        print("[ ] - Checking connectivity...")
        if check_connectivity():
            print(color.OKGREEN + "[*] - Connected to a network")
        else :
            print(color.RED + "[!] - No connectivity!" + color.WHITE)
            print(color.RED + "[!] - Some tools might not work as intended" + color.WHITE)
        onifw()

    except KeyboardInterrupt:
        print("\n"+ color.LOGGING + "Leaving...\n" + color.WHITE)

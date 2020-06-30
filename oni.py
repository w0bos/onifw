#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Code shamelessly stolen from Manisso's fsociety framework
#Code shamelessly stolen from Lul3xploit's LittleBrother framework

### MODULES ###
import sys
import os
import readline
import random
import configparser
import subprocess


### IMPORTS ###
import core.completer as auto
import setup          as setup
import core.installer as instl
import core.custom    as cinstall
import core.launcher  as l
import core.updater   as up


### FROM ###
from core.loading import thread_loading
from core.gui import color as color



### DATA ###
installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
toolDir = installDir + 'tools/'
onifw_cmd = "onifw > "
with open("{}/api/version.txt".format(installDir)) as f:
    version = f.readlines()[0].rstrip("\n\r")
f.close()
pkg = ["microsploit", "poet","weeman","sb0x","nxcrypt",
        "nmap","xsstrike","doork","crips","wpscan","setoolkit","cupp",
        "brutex","leviathan","sslstrip","sqlmap","slowloris","pwnloris",
        "atscan","hyde","nikto","rapidscan","apwps","snmp","revsh","arachni","openssl"]


### PARAM ###
configFile = installDir + "./core/config.cfg"
config = configparser.ConfigParser()
config.read(configFile)

### Functions ###
def clearScr():
    os.system("cls||clear")

def readfile(file_dir):
    f = open(file_dir)
    content = [line.rstrip('\n') for line in f]
    return content

def del_cache(leave=0):
    os.system("rm -rf {}core/__pycache__".format(installDir))
    os.system("rm -rf {}./__pycache__".format(installDir))
    if leave==1:
        sys.exit(1)

def pkgmgrhelp():
    print(color.NOTICE)
    print("[*] - Usage : pkg [cmd] [package]")
    print("      Multiple packages can be installed at once.")
    print(
        "      Use the [list] commad to see what packages are available")
    print("      Flags:")
    print("      -a --all        install all packages")
    print("      -i --install    install named package")
    print("      -r --remove     remove package")
    print(
        "      -f --force      forces the removal (when installed in sudo)")
    print("      -c --custom     add custom package")
    print(color.WHITE)

### Class ###
class main:

    def __init__(self):

        if not os.path.isdir(toolDir):  os.makedirs(toolDir)

        completer = auto.Autocomp(readfile(installDir + "api/dict.txt"))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input(color.color_random[0]+onifw_cmd + color.END)

        cmd = prompt.split()

        if len(cmd)==0:
            self.__init__()

        elif cmd[0] == "quit":
            clearScr()
            print(color.BOLD + color.NOTICE + "[*] - Cleaning cache..." + color.END)
            print(color.BOLD + color.OKGREEN + "[*] - Leaving onifw..." + color.END)
            del_cache(1)     

        ### UTILS ###
        elif cmd[0] == "clean_cache":
            del_cache() 
        elif cmd[0] == "clear":
            clearScr()
        elif cmd[0] == "list" or cmd[0]=="ls":
            if len(cmd)==1:
                print(color.BOLD + color.HEADER + "List of installed tools" + color.END + color.LOGGING)
                os.system("ls %s/"%toolDir)
                print(color.END)
            elif cmd[1] == "-r" or cmd[1]=="recommended":
                instl.Installer(1, installDir)
        elif cmd[0]=="update":
            up.Updater(installDir)
            
            #print(color.NOTICE + "[*] - Feature not yet deployed" + color.END)
        elif cmd[0] == "help":
            print(color.NOTICE)
            with open("{}api/help.txt".format(installDir), 'r') as fin:
                print(color.color_random[0])
                print(fin.read())
                print(color.END)
                print(color.END + color.WHITE)
        elif cmd[0]=="uninstall":
            answer = input(
                color.WARNING + "[!] - Do you wish to remove onifw and all installed tools ?\n[y/N]").lower()
            if answer in ["y", "yes"]:
                subprocess.run("cd {} && ./uninstall".format(installDir), shell=True)
            else :
                print(color.LOGGING + "[*] - Aborting uninstall process.")
                self.__init__()

        ### MISC ###
        elif cmd[0] == "restore":
            instl.RestoreDict(installDir)
        elif cmd[0] == "show_version":
            print(color.color_random[random.randint(0,len(color.color_random)-1)])
            print(version)
        elif cmd[0] == "show_logo":
            print(color.HEADER)
            with open("{}api/logo.txt".format(installDir), 'r') as fin:
                print(color.color_random[0])
                print(fin.read())
                print(color.END)
                print(color.END + color.WHITE)
            fin.close()
        elif cmd[0]=="show_credits":
            with open("{}api/credits.txt".format(installDir), 'r') as fin:
                print(color.color_random[0])
                print(fin.read())
                print(color.END)
            fin.close()
        elif cmd[0]=="show_title":
            with open("{}api/logo_ascii.txt".format(installDir), 'r') as fin:
                print(color.color_random[0])
                print(fin.read())
                print(color.END)
            fin.close()
        elif cmd[0]=="show_agreement":
            with open("{}api/agreement.txt".format(installDir), 'r') as fin:
                print(color.BOLD + color.IMPORTANT)
                print(fin.read())
                print(color.END)
            fin.close()



        ### TOOL LAUNCH ###
        elif cmd[0] in pkg:
            e = cmd[0]
            if   e=="microsploit":l.microsploit()
            elif e=="poet":l.poet()
            elif e=="weeman":l.weeman()
            elif e=="sb0x":l.sb0x()
            elif e=="nxcrypt":l.nxcrypt()
            elif e=="revsh":l.revsh()
            elif e=="leviathen":l.leviathan()
            elif e=="brutetx":l.brutex()
            elif e=="cupp":l.cupp()
            elif e=="nmap":l.nmap()
            elif e=="xsstrike":l.xsstrike()
            elif e=="doork":l.doork()
            elif e=="crips":l.crips()
            elif e=="wpscan":l.wpscan()
            elif e=="setoolkit":l.setoolkit()
            elif e=="ipfinder":l.ipfind()
            elif e=="sslstrip":l.sslstrip()
            elif e=="stmp":l.stmp()
            elif e=="pyphi":l.pyphi()
            elif e=="snmp":l.snmp()
            elif e=="apwps":l.apwps()
            elif e=="atscan":l.atscan()
            elif e=="pwnloris":l.pwnloris()
            elif e=="slowloris":l.slowloris()
            elif e=="sqlmap":l.sqlmap()
            elif e=="arachni":l.arachni()
            elif e=="brutex":l.brutex()
            elif e=="rapidscan":l.rscan()
            elif e=="nikto":l.nikto()



        ### PACKAGE MANAGER ###
        elif cmd[0] == "pkg":
            if len(cmd)==1:
                pkgmgrhelp()
            else:         
                if "--all" in cmd or "-a" in cmd:
                    instl.Installer(0, installDir)
                elif "-c" in cmd or "--custom" in cmd:
                    cinstall.Main(installDir)
                elif "-r" in cmd or "--remove" in cmd:
                    instl.Uninstaller(installDir, cmd)
                elif "-rf" in cmd or "-fr" in cmd or ("--force" and "--remove") in cmd:
                    instl.Uninstaller(installDir, cmd, 1)
                elif "-i" in cmd or "--install" in cmd:
                    instl.User_install(installDir, cmd)
                elif "-h" in cmd or "--help" in cmd:
                    pkgmgrhelp()
                else :
                    tools = prompt[8:].split()
                    instl.Installer(0, installDir, tools)
    
        ### THROW NO CMD ###
        else:
            try:
                cmd = config.get('custom', str(prompt.rstrip('\n\r')))
                print(cmd)
                os.system(cmd)
            except:
                print(color.WARNING + "[!] - %s : unknown command" % cmd[0])
            

        self.__init__()

class custfw:
    print(color.IMPORTANT + "[!] - This feature may not work as intended")
    def __init__(self):
        completer = auto.Autocomp(readfile(installDir + "{}api/dict.txt".format(installDir)))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input(color.color_random[0] + "onifw.CUSTOM > " + color.WHITE)


        if prompt == "return":
            main()
        
        elif prompt == "list" or prompt=="ls":
            with open("{}api/ctools.txt".format(installDir), "r") as f:
                try:
                    lignes = [lines.rstrip('\n') for lines in f]
                    for i in lignes:
                        print(color.LOGGING + i)
                except:
                    print("[!] - There are no custom packages to display.")
            self.__init__()

        elif prompt =="clear":
            clearScr()
            self.__init__()
        
        elif prompt == "quit":
            sys.exit(1);
        
        else:
            try:
                cmd = config.get('custom', str(prompt))
                os.system(cmd)
                self.__init__()
            except configparser.Error:
                print(color.WARNING + "[!] - %s command not found.".format(prompt))
                self.__init__()



if __name__ == '__main__':
    try:
        clearScr()
        thread_loading()
        with open("{}api/logo_ascii.txt".format(installDir), 'r') as fin:
            print(color.color_random[0])
            print(fin.read())
            print(color.END)
        fin.close()
        print(color.color_random[0]+version)
        if setup.init(): #socket.create_connection(("www.google.com", 80)):
            print(color.OKGREEN + "\n[*] - Connected to a network")
        else :
            print(color.BOLD)
            print(color.RED + "[!] - No connectivity!" + color.WHITE)
            print(color.RED + "[!] - Some tools might not work as intended" + color.END)
        main()
    except KeyboardInterrupt:
        print("\n"+ color.LOGGING + color.BOLD)
        print("[*] - Keyboard interruption. Leaving onifw...\n" + color.WHITE)
        del_cache()

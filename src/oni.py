#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'''
    TODO 
        - Check if uninstaller works         

    DONE
        - ConfigHandler
        - CustomInstaller
        - Implement installer
        - Updater
        - GUI
        - Dictionnary handler
        - Loading
        - Load all tools installed in array 
'''







# Imports
import readline
import configparser
import subprocess
import random


# From
from os import system as cmd
from os import path as path
from os import makedirs as mkdir
from sys import exit as abort
from socket import create_connection

#File loading
import core.completer       as auto
import core.installer       as instl
import core.custom          as custom
import core.launcher        as launch
import core.updater         as update
import core.dict            as dictmgr
import core.confighandler   as cfghandler
from   core.loading         import thread_loading
from   core.gui             import color as color


# Data
installDir = path.dirname(path.abspath(__file__)) + '/'
toolDir = installDir + 'tools/'
onifw_cmd = "onifw > "



# Misc functions
def clearScr():
    cmd("cls||clear")


def readfile(file_dir):
    f = open(file_dir)
    content = [line.rstrip('\n') for line in f]
    return content


def del_cache(leave=0):
    
    if leave == 1:
        cmd("rm -rf {}core/__pycache__".format(installDir))
        cmd("rm -rf {}__pycache__".format(installDir))
        abort(1)
    else:
        cmd("rm -rf {}core/__pycache__".format(installDir))
        cmd("rm -rf {}__pycache__".format(installDir))



def pkgmgrhelp():
    print(color.NOTICE)
    print("[*] - Usage : pkg [cmd] [package]")
    print("      Multiple packages can be installed at once.")
    print("      Use the [list] commad to see what packages are available")
    print("      Flags:")
    print("      -a --all        install all packages")
    print("      -i --install    install named package")
    print("      -r --remove     remove package")
    print("      -f --force      forces the removal (when installed in sudo)")
    print("      -c --custom     add custom package")
    print(color.WHITE)



def loadtools():
    load_cmd = ['ls','{}'.format(toolDir)]
    output = subprocess.run(load_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
    #Clean output
    pkg_local=output.splitlines()
    return pkg_local


def loadconfig():
    cfghandler.ConfigOnstart(installDir)

def loadCustom(name):
    cfghandler.CustomTool(installDir, name)

# Class
class main:

    def __init__(self):
        #Check is path exists
        if not path.isdir(toolDir): mkdir(toolDir)
        completer = auto.Autocomp(readfile(installDir + "data/dict.txt"))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input(color.color_random[0]+onifw_cmd + color.END)
        
        # Ask input
        cmd = prompt.split()

        if len(cmd)==0:
            self.__init__()
            #loopback
        else:
            marg = cmd[0]
            #main argument


            # BASE COMMANDS
            # PASS
            if marg=="quit":
                clearScr()
                print(color.BOLD + color.NOTICE + "[*] - Cleaning cache..." + color.END)
                print(color.BOLD + color.OKGREEN + "[*] - Leaving onifw..." + color.END)
                del_cache(1)
            elif marg=="clean_cache":
                del_cache()
            elif marg=="clear":
                clearScr()
            elif marg=="list" or marg=="ls":
                if len(cmd)==1:
                    print(color.BOLD + color.HEADER +"List of installed tools" + color.END + color.LOGGING)
                    subprocess.run("ls {}tools/".format(installDir),shell=True)
                    print(color.END)
                elif cmd[1]=="-r" or cmd[1]=="--recommended":
                    instl.show_recommended()
                else:
                    print(color.WARNING + "[!] - %s : unknown command" % i for i in cmd)
            elif marg== "update":
                update.Updater(installDir)
            elif marg=="help":
                print(color.NOTICE)
                with open("{}data/help.txt".format(installDir), 'r') as fin:
                    print(color.color_random[0])
                    print(fin.read())
                    print(color.END + color.WHITE)
            elif marg=="uninstall":
                '''
                    MUST CHECK IF WORKING!!!
                '''
                answer = input(color.WARNING + "[!] - Do you wish to remove onifw and all installed tools ?\n[y/N]").lower()
                if answer.lower() in ["y", "yes"]:
                    subprocess.run("cd {} && ../uninstall".format(installDir), shell=True)
                    #subprocess.run("rm -rf $HOME/.onifw && sudo rm /usr/bin/local/onifw")
                else:
                    print(color.LOGGING + "[*] - Aborting uninstall process.")
                    self.__init__()
            

            # MISC
            # PASS
            elif marg == "show_version":
                print(color.color_random[random.randint(0, len(color.color_random)-1)])
                with open("{}data/version.txt".format(installDir)) as f:
                    version = f.readlines()[0].rstrip("\n\r")
                f.close()
                print("[*] - Installed version",version)
            elif marg == "show_logo":
                print(color.HEADER)
                with open("{}data/logo.txt".format(installDir), 'r') as fin:
                    print(color.color_random[0])
                    print(fin.read())
                    print(color.END)
                    print(color.END + color.WHITE)
                fin.close()
            elif marg == "show_credits":
                with open("{}data/credits.txt".format(installDir), 'r') as fin:
                    print(color.color_random[0])
                    print(fin.read())
                    print(color.END)
                fin.close()
            elif marg == "show_title":
                with open("{}data/logo_ascii.txt".format(installDir), 'r') as fin:
                    print(color.color_random[0])
                    print(fin.read())
                    print(color.END)
                fin.close()
            elif marg == "show_agreement":
                with open("{}data/agreement.txt".format(installDir), 'r') as fin:
                    print(color.BOLD + color.IMPORTANT)
                    print(fin.read())
                    print(color.END)
                fin.close()
            elif marg == "restore":
                dictmgr.restoreDict(installDir)


            # TOOL LAUNCHER
            elif marg in loadtools():
                # Add dictionnary to array on launch instead of hard coded one
                e = cmd[0]
                if e == "microsploit":  launch.microsploit()
                elif e == "poet":       launch.poet()
                elif e == "weeman":     launch.weeman()
                elif e == "sb0x":       launch.sb0x()
                elif e == "nxcrypt":    launch.nxcrypt()
                elif e == "revsh":      launch.revsh()
                elif e == "leviathen":  launch.leviathan()
                elif e == "brutetx":    launch.brutex()
                elif e == "cupp":       launch.cupp()
                elif e == "nmap":       launch.nmap()
                elif e == "xsstrike":   launch.xsstrike()
                elif e == "doork":      launch.doork()
                elif e == "crips":      launch.crips()
                elif e == "wpscan":     launch.wpscan()
                elif e == "setoolkit":  launch.setoolkit()
                elif e == "ipfinder":   launch.ipfind()
                elif e == "sslstrip":   launch.sslstrip()
                elif e == "stmp":       launch.stmp()
                elif e == "pyphi":      launch.pyphi()
                elif e == "snmp":       launch.snmp()
                elif e == "apwps":      launch.apwps()
                elif e == "atscan":     launch.atscan()
                elif e == "pwnloris":   launch.pwnloris()
                elif e == "slowloris":  launch.slowloris()
                elif e == "sqlmap":     launch.sqlmap()
                elif e == "arachni":    launch.arachni()
                elif e == "brutex":     launch.brutex()
                elif e == "rapidscan":  launch.rscan()
                elif e == "nikto":      launch.nikto()

                #Custom tool
                else:
                    try:
                        loadCustom(marg)
                    # Else throw command as unknown
                    except:
                        print(color.WARNING +
                              "[!] - %s : unknown command" % cmd[0])
            
            # Package managment
            elif marg == "pkg":
                if len(cmd) == 1:
                    pkgmgrhelp()
                else:
                    if "--all" in cmd or "-a" in cmd:
                        instl.Install(installDir)
                        #instl.Installer(0, installDir)
                    elif "-c" in cmd or "--custom" in cmd:
                        custom.Main(installDir)
                        #cinstall.Main(installDir)
                    elif "-r" in cmd or "--remove" in cmd:
                        #instl.Uninstaller(installDir, cmd)
                        instl.uninstall(installDir,cmd)
                    elif "-rf" in cmd or "-fr" in cmd or ("--force" and "--remove") in cmd:
                        #instl.Uninstaller(installDir, cmd, 1)
                        instl.uninstall(installDir, cmd,1)
                    elif "-i" in cmd or "--install" in cmd:
                        instl.User_install(installDir, cmd)
                    elif "-h" in cmd or "--help" in cmd:
                        pkgmgrhelp()
                    else:
                        tools = prompt.split(" ")[1:]
                        if not(len(tools)):
                            instl.Install(installDir)
                        else:
                            print(color.WARNING +"PackageManager[!] %s : unknown command" % tools)
                        #instl.Installer(0, installDir, tools)
            
            # Try custom package
            else:
                print(color.WARNING +"[!] - %s : unknown command" % cmd[0])
        
        #loopback while no command
        self.__init__()        


if __name__ == '__main__':
    try:
        clearScr()
        print(color.color_random[1])
        thread_loading()
        loadconfig()
        main()
    except KeyboardInterrupt:
        print("\n" + color.LOGGING + color.BOLD)
        print("[*] - Keyboard interruption. Leaving onifw...\n" + color.WHITE)
        del_cache()


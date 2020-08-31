#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    TODO:
        ! Commands
            - help [command] ==> Show more help

        * Configuration

        * Fix
            ! Some tools require modules (python pip)

        * Misc
            

    DONE:
        * Commands
            - myIP  -> Displays local and remote IP
            - shell -> Run a shell command
            - Add commands from dlab/plab
            - cd -> change current directory
            - onibuster -> starts a simple directory buster

        * Configuration
            - Complete log output of onifw in log/oni.log file

        * Fix
            - Fixed packages that didn't make make install
            - Fix logging when doing multiple argument input
            - Add more options to Nmap
            - IndexOutOfBonds when installing some packages
            - Fixed no arguments error that crash the framework
            - Fixed tools not compiling using the old installer
            - Fixed openssl install for revsh.

        * Misc
            - Edit cd command to work with path variables ($HOME, ~/, ../)
            - Add port configuration when using onimap
            - Simplify help command
            - Rewrote the package manager

'''

# From
from os import system as shell
from os import path
from os import makedirs as mkdir
from sys import exit as abort
from random import randint
from subprocess import run, PIPE
from readline import set_completer, parse_and_bind

#File loading
import core.completer       as auto
import core.packagemanager  as pacman
import core.custom          as custom
import core.launcher        as launch
import core.updater         as update
import core.dict            as dictmgr
import core.confighandler   as cfg
import core.logHandler      as logger
from   core.loading         import thread_loading
from   core.gui             import color
    
# Misc functions
def clearScr():
    shell("cls||clear")

def readfile(file_dir):
    f = open(file_dir)
    content = [line.rstrip('\n') for line in f]
    return content

def del_cache(leave=0):
    if leave == 1:
        shell("rm -rf {}core/__pycache__".format(installDir))
        shell("rm -rf {}__pycache__".format(installDir))
        abort(1)
    else:
        shell("rm -rf {}core/__pycache__".format(installDir))
        shell("rm -rf {}__pycache__".format(installDir))

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
    load_cmd = ['ls', '{}'.format(toolDir)]
    output = run(load_cmd, stdout=PIPE).stdout.decode('utf-8')
    #Clean output
    pkg_local = output.splitlines()
    return pkg_local

# Data
installDir = path.dirname(path.abspath(__file__)) + '/'
toolDir = installDir + 'tools/'
logDir = installDir + 'logs/'
onifw_cmd = cfg.check_prompt(installDir)
debug = cfg.check_value(installDir, "debug", False)

# Class
class main:

    def __init__(self):
        #Check is path exists
        if not path.isdir(toolDir): mkdir(toolDir)
        if not path.isdir(logDir): mkdir(logDir)
        completer = auto.Autocomp(readfile(installDir + "data/dict.txt"))
        set_completer(completer.complete)
        parse_and_bind('tab: complete')
        prompt = input(color.BOLD + color.color_random[0] + onifw_cmd + color.END)
        # Ask input
        cmd = prompt.split()
        #Add input to log if enables
        logger.LogHandler(installDir, logDir, cmd)

        if len(cmd) == 0:
            pass
            #loopback
        else:
            marg = cmd[0]
            # BASE COMMANDS
            # PASS
            if marg == "quit" or marg == "exit":
                clearScr()
                print(color.BOLD + color.NOTICE + "[*] - Cleaning cache..." + color.END)
                print(color.BOLD + color.OKGREEN + "[*] - Leaving onifw..." + color.END)
                del_cache(1)
            elif marg == "clean_cache":
                del_cache()
            elif marg == "clear":
                clearScr()
            elif marg == "list" or marg == "ls":
                if len(cmd) == 1:
                    print(color.BOLD + color.HEADER +"List of installed tools" + color.END + color.LOGGING)
                    run("ls {}tools/".format(installDir), shell=True)
                    print("myip  ipfinder  hashcheck  servicestatus  firewall  viewtraffic  netmanager  onimap  onibuster "+color.END)
                elif cmd[1] == "-r" or cmd[1] == "--recommended":
                    pacman.show_recommended()
                else:
                    print(color.WARNING + "ls[!] - %s : unknown command" % cmd[1])
                    #generator in print?
            elif marg == "update":
                update.Updater(installDir)
            elif marg in ["help", "?"]:
                if len(cmd) < 2:
                    with open("{}data/help.txt".format(installDir), 'r') as fin:
                        print(
                            color.NOTICE+color.color_random[0] + fin.read() + color.END + color.WHITE)
                else:
                    print(color.WARNING+"[-] - WIP"+color.END)
            elif marg == "uninstall":
                answer = input(color.WARNING + "[!] - Do you wish to remove onifw and all installed tools ?\n[y/N]").lower()
                if answer.lower() in ["y", "yes"]:
                    run("cd {} && . ../uninstall".format(installDir), shell=True)
                    #run("rm -rf $HOME/.onifw && sudo rm /usr/bin/local/onifw")
                else:
                    print(color.LOGGING + "[*] - Aborting uninstall process.")

            # MISC
            # PASS
            elif marg == "show_version":
                print(color.color_random[randint(0, len(color.color_random)-1)])
                with open("{}data/version.txt".format(installDir)) as f:
                    version = f.readlines()[0].rstrip("\n\r")
                f.close()
                print("[*] - Installed version", version)
            elif marg == "show_logo":
                print(color.HEADER)
                with open("{}data/logo.txt".format(installDir), 'r') as fin:
                    print(color.color_random[0])
                    print(fin.read())
                    print(color.END)
                    print(color.END + color.WHITE)
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
                if e == "microsploit":
                    launch.microsploit()
                elif e == "poet":
                    launch.poet()
                elif e == "weeman":
                    launch.weeman()
                elif e == "sb0x":
                    launch.sb0x()
                elif e == "nxcrypt":
                    launch.nxcrypt()
                elif e == "revsh":
                    launch.revsh()
                elif e == "leviathan":
                    launch.leviathan()
                elif e == "brutetx":
                    launch.brutex()
                elif e == "cupp":
                    launch.cupp()
                elif e == "nmap":
                    launch.nmap(installDir)
                elif e == "xsstrike":
                    launch.xsstrike()
                elif e == "doork":
                    launch.doork()
                elif e == "crips":
                    launch.crips()
                elif e == "wpscan":
                    launch.wpscan()
                elif e == "setoolkit":
                    launch.setoolkit()
                elif e == "sslstrip":
                    launch.sslstrip()
                elif e == "stmp":
                    launch.stmp()
                elif e == "pyphi":
                    launch.pyphi()
                elif e == "snmp":
                    launch.snmp()
                elif e == "apwps":
                    launch.apwps()
                elif e == "atscan":
                    launch.atscan()
                elif e == "pwnloris":
                    launch.pwnloris()
                elif e == "slowloris":
                    launch.slowloris()
                elif e == "sqlmap":
                    launch.sqlmap()
                elif e == "arachni":
                    launch.arachni()
                elif e == "brutex":
                    launch.brutex()
                elif e == "rapidscan":
                    launch.rscan()
                elif e == "nikto":
                    launch.nikto()
                #Custom tool
                else:
                    try:
                        cfg.CustomTool(installDir, marg)
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
                        pacman.Install(installDir)
                    elif "-c" in cmd or "--custom" in cmd:
                        custom.Main(installDir)
                    elif "-r" in cmd or "--remove" in cmd:
                        if len(cmd) > 2:
                            pacman.uninstall(installDir, cmd[2:])
                        else:
                            print("[!] - No arguments provided")
                    elif "-da" in cmd or "--delete-all" in cmd:
                        pacman.remove_all(installDir)
                    elif "-rf" in cmd or "-fr" in cmd or ("--force" and "--remove") in cmd:
                        if len(cmd) > 2:
                            pacman.uninstall(installDir, cmd, 1)
                        else:
                            print("[!] - No arguments provided")
                    elif "-i" in cmd or "--install" in cmd:
                        pacman.Install(installDir, cmd[2:])
                        #.User_install(installDir, cmd)
                    elif "-h" in cmd or "--help" in cmd:
                        pkgmgrhelp()
                    else:
                        if len(prompt.split(" ")[1:]) >= 1:
                            print(
                                color.WARNING + "PackageManager[!] %s : unknown command" % prompt.split(" ")[1:])

            # Default scripts
            elif marg == "ipfinder":
                launch.ipfind()
            elif marg == "bg":
                launch.bg()
            elif marg == "hashcheck":
                launch.hashcheck(logDir)
            elif marg == "servicestatus":
                launch.servicestatus(logDir)
            elif marg == "firewall":
                launch.firewall(logDir)
            elif marg == "viewtraffic":
                launch.viewtraffic(logDir)
            elif marg == "netmanager":
                launch.networkmanaged(logDir)
            elif marg == "onimap":
                launch.onimap(installDir, logDir)
            elif marg == "shell":
                launch.run_shell()
            elif marg == "onibuster":
                launch.onibuster(installDir, logDir)
            elif marg == "myip":
                launch.myip()
            elif marg == "cd":
                launch.cd(cmd)
            elif marg == "checkout":
                launch.checkout(cmd, installDir)
            elif marg == "status":
                launch.status(installDir)
            # Try custom package
            else:
                print(color.WARNING +"[!] - %s : unknown command" % cmd[0])

        #loopback while no command
        self.__init__()

if __name__ == '__main__':
    try:
        clearScr()
        if cfg.check_value(installDir, "show_loading", True):
            print(color.color_random[1])
            thread_loading()
        clearScr()
        cfg.ConfigOnstart(installDir)
        cfg.ConfigMisc(installDir)
        main()
    except KeyboardInterrupt:
        print("\n" + color.LOGGING + color.BOLD)
        print("[*] - Keyboard interruption. Leaving onifw...\n" + color.WHITE)
        if cfg.check_value(installDir, "delete_cache", True):
            del_cache()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    TODO:
        * Commands
            - help [command] ==> Show more help

        * Configuration
            - Add custom path for onirc file
            - Change default path for onirc :
                ==> $HOME/.onirc

        * Fix
            ! Some tools require modules (python pip)
            !

        * Misc
            ? Add session manager
            - Prepare for python 3.9 type hinting


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
            - Add display manager for messages
            - Add docstring (PEP8)

"""

# From
from os import path
from os import makedirs as mkdir
from sys import exit as leave
from random import randint
from subprocess import run
from readline import set_completer, parse_and_bind

#File loading
import core.completer       as auto
import core.packagemanager  as pacman
import core.custom          as custom
import core.updater         as update
import core.dict            as dictmgr
import core.confighandler   as cfg
import core.logHandler      as logger
import core.toolLauncher    as tl
from   core.loading         import thread_loading
from   core.gui             import color, logos
from   core.onilib          import clearScr, readfile, loadtools, del_cache, pkgmgrhelp, return_colored_prefix

installDir = path.dirname(path.abspath(__file__)) + '/'
toolDir = installDir + 'tools/'
logDir = installDir + 'logs/'
onifw_cmd = cfg.check_prompt(installDir)
debug = cfg.check_value(installDir, "debug", False)


class main:

    def __init__(self):
        if not path.isdir(toolDir): mkdir(toolDir)
        if not path.isdir(logDir): mkdir(logDir)
        completer = auto.Autocomp(readfile(installDir + "data/dict.txt"))
        set_completer(completer.complete)
        parse_and_bind('tab: complete')
        prompt = input(color.BOLD + color.color_random[0] + onifw_cmd + color.END)
        cmd = prompt.split()
        logger.LogHandler(installDir, logDir, cmd)
        if len(cmd) != 0:
            marg = cmd[0]

            if marg in ["quit", "exit"]:
                clearScr()
                print(return_colored_prefix("*") + "- Cleaning cache..." + color.END)
                print(return_colored_prefix("*") + "- Leaving onifw..." + color.END)
                del_cache(installDir)
                leave()
            elif marg == "clean_cache":
                del_cache(installDir)
            elif marg == "clear":
                clearScr()
            elif marg in ["list", "ls"]:
                if len(cmd) == 1:
                    print(color.BOLD + color.HEADER +"List of installed tools" + color.END + color.LOGGING)
                    run("ls {}tools/".format(installDir), shell=True)
                    print("myip  ipfinder  hashcheck  servicestatus  firewall  viewtraffic  netmanager  onimap  onibuster "+color.END)
                elif cmd[1] in ["-r", "--recommended"]:
                    pacman.show_recommended()
                else:
                    print(return_colored_prefix("!") + "- %s : unknown command" % cmd[1])
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
                answer = input(return_colored_prefix("!") + "- Do you wish to remove onifw and all installed tools ?\n[y/N]").lower()
                if answer.lower() in ["y", "yes"]:
                    run("cd {} && . ../uninstall".format(installDir), shell=True)
                else:
                    print(color.LOGGING + return_colored_prefix("*") + "- Aborting uninstall process.")
            elif marg == "show_version":
                print(color.color_random[randint(0, len(color.color_random)-1)])
                with open("{}data/version.txt".format(installDir)) as f:
                    version = f.readlines()[0].rstrip("\n\r")
                f.close()
                print(return_colored_prefix("*") + "- Installed version", version)
            elif marg == "show_title":
                print(color.color_random[2] + logos.ascii_art[0] + color.END)
                #with open("{}data/logo_ascii.txt".format(installDir), 'r') as fin:
                #    print(color.color_random[0])
                #    print(fin.read())
                #    print(color.END)
                #fin.close()
            elif marg == "show_agreement":
                with open("{}data/agreement.txt".format(installDir), 'r') as fin:
                    print(color.BOLD + color.IMPORTANT)
                    print(fin.read())
                    print(color.END)
                fin.close()
            elif marg == "restore":
                dictmgr.restoreDict(installDir)
            # TOOL LAUNCHER
            elif marg in loadtools(toolDir):
                e = cmd[0]
                if e == "microsploit":
                    tl.toolmanager("microsploit", "bash",
                                   False, False, "Microsploit")
                elif e == "poet":
                    tl.toolmanager("poet", "python2", False, False, "server")
                elif e == "weeman":
                    tl.toolmanager("weeman", "python2", False, True)
                elif e == "sb0x":
                    tl.toolmanager("sb0x", "python2", False, True)
                elif e == "nmap":
                    tl.nmap()
                elif e == "xsstrike":
                    tl.toolmanager("xsstrike", "python3", True,
                                   False, "", "-u", "--crawl -l 5 -t 10")
                elif e == "doork":
                    tl.doork()
                elif e == "crips":
                    tl.toolmanager("crips", "python2")
                elif e == "wpscan":
                    tl.wpscan()
                elif e == "setoolkit":
                    tl.setoolkit()
                elif e == "snmp":
                    tl.toolmanager("snmp", "python2", True,
                                   False, "snmpbrute", "-t")
                elif e == "apwps":
                    tl.toolmanager("apwps", "python2",
                                   False, False, "autopixie")
                elif e == "atscan":
                    tl.atscan()
                elif e == "rapidscan":
                    tl.toolmanager("rapidscan", "python2", True)
                elif e == "sqlmap":
                    tl.sqlmap()
                elif e == "ssltrip":
                    tl.toolmanager("ssltrip", "python2",
                                   True, False, "sslstrip")
                elif e == "cupp":
                    tl.toolmanager("cupp", "python3", False, False, "", "-i")
                elif e == "leviathan":
                    tl.toolmanager("leviathan", "python2",
                                   False, False, "", "-i")
                elif e == "nikto":
                    tl.toolmanager("nikto", "perl", True, False,
                                   "/program/nikto", "-h")
                elif e == "arachni":
                    tl.arachni()
                elif e == "slowloris":
                    tl.toolmanager("slowloris", "python3", True, False)
                
                # OLD INSTALLER
            #TOOLS THAT MUST BE COMPILED
                elif e == "revsh":
                    tl.revsh()
                elif e == "brutex":
                    tl.brutex()
                #Custom tool
                else:
                    try:
                        cfg.CustomTool(installDir, marg)
                    except:
                        print(return_colored_prefix("!") + "- %s : unknown command" % cmd[0])
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
                            print(return_colored_prefix("!") +
                                  " - No arguments provided")
                    elif "-da" in cmd or "--delete-all" in cmd:
                        pacman.remove_all(installDir)
                    elif "-rf" in cmd or "-fr" in cmd or ("--force" and "--remove") in cmd:
                        if len(cmd) > 2:
                            pacman.uninstall(installDir, cmd, 1)
                        else:
                            print(return_colored_prefix("!") +
                                  " - No arguments provided")
                    elif "-i" in cmd or "--install" in cmd:
                        pacman.Install(installDir, cmd[2:])
                        #.User_install(installDir, cmd)
                    elif "-h" in cmd or "--help" in cmd:
                        pkgmgrhelp()
                    else:
                        if len(prompt.split(" ")[1:]) >= 1:
                            print(return_colored_prefix(
                                "!") + "- %s : unknown command" % prompt.split(" ")[1:])

            # Default scripts
            elif marg == "ipfinder":
                tl.ipfind()
            elif marg == "bg":
                tl.bg()
            elif marg == "hashcheck":
                tl.hashcheck(logDir)
            elif marg == "servicestatus":
                tl.servicestatus(logDir)
            elif marg == "firewall":
                tl.firewall(logDir)
            elif marg == "viewtraffic":
                tl.viewtraffic(logDir)
            elif marg == "netmanager":
                tl.networkmanaged(logDir)
            elif marg == "onimap":
                tl.onimap(installDir, logDir)
            elif marg == "shell":
                tl.run_shell()
            elif marg == "onibuster":
                tl.onibuster(installDir, logDir)
            elif marg == "myip":
                tl.myip()
            elif marg == "cd":
                tl.cd(cmd)
            elif marg == "checkout":
                tl.checkout(cmd, installDir)
            elif marg == "status":
                tl.status(installDir)
            # Try custom package
            else:
                print(return_colored_prefix("!") + "- %s: unknown command" % cmd[0])
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
        print("\n" + color.LOGGING + color.BOLD +
              "[!] - Keyboard interruption. Leaving onifw...\n" + color.WHITE)
        if cfg.check_value(installDir, "delete_cache", True):
            del_cache(installDir)

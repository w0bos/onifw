#!/usr/bin/env python3

import os

version = "0.0.1"

def clearScr():
    os.system("clear||cls")

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


class Main:

    def __init__(self, installDir):
        self.installDir = installDir
        self.toolDir = installDir + 'tools/'
        self.logDir = installDir + 'logs/'
        print(color.WARNING)
        print("[!] - Custom tool installer.")
        print("This tool may not work properly and might break your current install of onifw.")
        print("[?] - What is the language of the tool?\n\r1 - Python2/3\n\r2 - C")
        ans = input("> ")
        if ans == "1":
            Pythonapp(self.installDir, self.toolDir)
        elif ans == "2":
            Capp(self.installDir, self.toolDir)
        else:
            print("[!] - Not yet implemented")


class Pythonapp:
    def __init__(self, installDir, toolDir):
        self.installDir, self.toolDir = installDir, toolDir
        link = input("Git repository of the tool (full link): ")
        name = input("Tool name: ")
        ver = input("Python version: ")
        cmds = input("Custom command (leave blank if unsure): ")
        issudo = input("Does the package needs root permissions? [y/N]")
        #Add question if script has a different name
        #g.e: main.py insttead of <projectname>.py
        temp = 0
        if not cmds:
            if issudo.lower() != "y":
                cmds = "python{0} {1}{2}/{2}.py".format(
                    ver, self.toolDir, name)
            else:
                cmds = "sudo python{0} {1}{2}/{2}.py".format(
                    ver, self.toolDir, name)
        try:
            os.system("git clone %s %s%s" % (link, self.toolDir, name))
            temp = 1
            # Must fix github login ?
        except:
            temp = -1
        if temp:
            with open("api/dict.txt", "a") as f:
                f.write(name + '\n')
                f.close()
            with open("api/ctools.txt", "a") as f:
                f.write(name + '\n')
                f.close()
            with open("core/config.cfg", "a") as f:
                f.write("{0} = {1}\n".format(name, cmds))
                f.close()
            print("[*] - You may need to restart onifw in order to use the custom tool.")


class Capp:
    def __init__(installDir, toolDir):
        self.installDir, self.toolDir = installDir, toolDir
        link = input("Git repository of the tool (full link): ")
        name = input("Tool name: ")
        nb_cmd = int(input("How many commands to build the tool?: "))
        try:
            os.system("git clone %s %s%s" % (link, self.toolDir, name))
            for i in range(nb_cmd):
                print("[*] - Current directory: %s" % os.system(pwd))
                cmd = input("Custom command: ")
                os.system(cmd)
        except:
            print("[!] - An unexpected error occurred!")

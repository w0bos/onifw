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
        print(color.BOLD + "[*] - Custom tool installer." + color.END)
        print("This tool may not work properly and might break your current install of onifw.")
        print("[?] - What is the language of the tool?\n\r1 - Python\n\r2 - C\n3 - Other")
        ans = input("> ")
        if ans == "1":
            Pythonapp(self.installDir, self.toolDir)
        elif ans == "2":
            Capp(self.installDir, self.toolDir)
        elif ans=="3":
            Otherapp(self.installDir, self.toolDir)    
        else:
            print("[!] - Not yet implemented")


class Pythonapp:
    def __init__(self, installDir, toolDir):
        self.installDir, self.toolDir = installDir, toolDir
        link = input("Git repository of the tool (full link): ")
        name = input("Tool name: ")
        ver = input("Python version: ")
        exe = input("Name of the file to launch (w/o extension): ")
        cmds = input("Custom command (leave blank if unsure): ")
        issudo = input("Does the package needs root permissions? [y/N]: ").lower()
        #Add question if script has a different name
        #g.e: main.py insttead of <projectname>.py
        temp = 0
        if not cmds:
            if issudo != "y":
                cmds = "python{0} {1}{2}/{3}.py".format(
                    ver, self.toolDir, name,exe)
            else:
                cmds = "sudo python{0} {1}{2}/{3}.py".format(
                    ver, self.toolDir, name,exe)
        try:
            os.system("git clone %s %s%s" % (link, self.toolDir, name))
            temp = 1
        except:
            temp = -1
        if temp:
            with open("{}api/dict.txt".format(self.installDir), "a") as f:
                f.write('\n' + name + '\n')
                f.close()
            with open("{}api/ctools.txt".format(self.installDir), "a") as f:
                f.write('\n' + name + '\n')
                f.close()
            with open("{}core/config.cfg".format(self.installDir), "a") as f:
                f.write("{0} = {1}\n".format(name, cmds))
                f.close()
            print("[*] - You may need to restart onifw in order to use the custom tool.")


class Capp:
    def __init__(self, installDir, toolDir):
        self.installDir, self.toolDir = installDir, toolDir
        link = input("Git repository of the tool (full link): ")
        name = input("Tool name: ")
        nb_cmd = int(input("How many commands to build the tool?: "))
        try:
            os.system("git clone %s %s%s" % (link, self.toolDir, name))
            for i in range(nb_cmd):
                print("[*] - Current directory: %s" % os.system("pwd"))
                cmd = input("Custom command: ")
                os.system(cmd)
            cmds = input("Launch command: ")
            with open("{}core/config.cfg".format(self.installDir), "a") as f:
                f.write("{0} = {1}\n".format(name, cmds))
                f.close()
            with open("{}api/dict.txt".format(self.installDir), "a") as f:
                f.write(name + '\n')
                f.close()
            with open("{}api/ctools.txt".format(self.installDir), "a") as f:
                f.write(name + '\n')
                f.close()
        except:
            print("[!] - An unexpected error occurred!")


class Otherapp:

    def __init__(self, installDir, toolDir):
        lang_dict = {
            "perl":     "perl",
            "ruby":     "ruby",
            "go":       "go", 
            "java-jar": "jar", 
            "java":     "java",
        }
        self.installDir, self.toolDir = installDir, toolDir
        print(color.OKBLUE + "Available languages:")
        for i in lang_dict.keys():
            print(i)
        print(color.END)
        lang = input("Select lang: ")
        link = input("Git repository of the tool (full link): ")
        name = input("Tool name: ")
        name_exe=input("Name of the main file (w/ entension): ")
        nb_cmd = int(input("How many commands to build the tool?: "))
        try:
            os.system("git clone %s %s%s" % (link, self.toolDir, name))
            for i in range(nb_cmd):
                print("[*] - Current directory: %s" % os.system("pwd"))
                cmd = input("Custom command: ")
                os.system(cmd)
            if lang=="java":
                cmds = "{0} = cd {1}{2} && {3}{4}".format(name, toolDir, name, lang_dict[lang], name_exe)
            else:
                cmds = "{0} = {1} {2}{3}{4}".format(name, lang_dict[lang], toolDir, name, name_exe)
            with open("{}core/config.cfg".format(self.installDir), "a") as f:
                f.write("{0} = {1}\n".format(name, cmds))
                f.close()
            with open("{}api/dict.txt".format(self.installDir), "a") as f:
                f.write(name + '\n')
                f.close()
            with open("{}api/ctools.txt".format(self.installDir), "a") as f:
                f.write(name + '\n')
                f.close()
            
        except:
            print("[!] - An unexpected error occurred!")

#!/usr/bin/env python3

import core.dict as dictmgr
from os import system as shell
from core.gui import color
from sys import exc_info as err
from core.errorHandler import ErrorHandler
from core.onilib import return_colored_prefix

version = "0.2"



class Main:

    def __init__(self, installDir):
        self.installDir = installDir
        self.toolDir = installDir + 'tools/'
        self.logDir = installDir + 'logs/'
        print(color.WARNING)
        print(return_colored_prefix(
            "*") + "- Custom tool installer." + color.END)
        print(color.OKBLUE + "Version {}".format(version) + color.END)
        print("The custom installer may not work properly and might break your current install of onifw.")
        print(return_colored_prefix(
            "?") + "- What is the language of the tool?\n\r1 - Python\n\r2 - C\n3 - Other\n\nq - Return")
        ans = input(color.OKBLUE + "PackageManager> ")
        if ans == "1":
            Pythonapp(self.installDir, self.toolDir)
        elif ans == "2":
            Capp(self.installDir, self.toolDir)
        elif ans == "3":
            Otherapp(self.installDir, self.toolDir)
        elif ans.lower()=="q":
            pass 
        else:
            print(return_colored_prefix(
                "!") + "- Not yet implemented")


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
                    ver, self.toolDir, name, exe)
            else:
                cmds = "sudo python{0} {1}{2}/{3}.py".format(
                    ver, self.toolDir, name, exe)
        try:
            shell("git clone %s %s%s" % (link, self.toolDir, name))
            temp = 1
        except:
            temp = -1
            ErrorHandler(err(), False)
        if temp:
            dictmgr.addWords(self.installDir, [name])
            dictmgr.addCustomWords(self.installDir, name)
            dictmgr.updateConfig(self.installDir, name, cmds)
            print(return_colored_prefix(
                "?") + "- You may need to restart onifw in order to use the custom tool.")


class Capp:
    def __init__(self, installDir, toolDir):
        self.installDir, self.toolDir = installDir, toolDir
        link = input("Git repository of the tool (full link): ")
        name = input("Tool name: ")
        nb_cmd = int(input("How many commands to build the tool?: "))
        try:
            shell("git clone %s %s %s" % (link, self.toolDir, name))
            for i in range(nb_cmd):
                print(return_colored_prefix(
                    "*") + "- Current directory: % s" % shell("pwd"))
                cmd = input("Custom command: ")
                shell(cmd)
            cmds = input("Launch command: ")
            dictmgr.addWords(self.installDir, name)
            dictmgr.addCustomWords(self.installDir, name)
            dictmgr.updateConfig(self.installDir, name, cmds)

        except:
            ErrorHandler(err(), False)


class Otherapp:
    """
    MUST IMPLEMENT SPECIAL CONFIG UPDATER IN DICTIONARY MANAGER
    """

    def __init__(self, installDir, toolDir):
        lang_dict = {
            "perl": "perl",
            "ruby": "ruby",
            "go": "go", 
            "java-jar": "jar", 
            "java": "java",
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
            shell("git clone %s %s%s" % (link, self.toolDir, name))
            for i in range(nb_cmd):
                print(return_colored_prefix(
                    "*") + "- Current directory: % s" % shell("pwd"))
                cmd = input("Custom command: ")
                shell(cmd)
            if lang == "java":
                cmds = "{0} = cd {1}{2} && {3}{4}".format(name, toolDir, name, lang_dict[lang], name_exe)
            else:
                cmds = "{0} = {1} {2}{3}{4}".format(name, lang_dict[lang], toolDir, name, name_exe)
            with open("{}onirc".format(self.installDir), "a") as f:
                f.write("{0} = {1}\n".format(name, cmds))
                f.close()
            with open("{}data/dict.txt".format(self.installDir), "a") as f:
                f.write(name + '\n')
                f.close()
            with open("{}data/ctools.txt".format(self.installDir), "a") as f:
                f.write(name + '\n')
                f.close()
        except:
            ErrorHandler(err(), False)

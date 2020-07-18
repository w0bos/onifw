import sys
import os
from sys import exit as abort
from os import system as cmd
from os import path as path
from os import makedirs as mkdir
from core.gui import color
from core.updater import Updater
from socket import create_connection
from configparser import ConfigParser
import readline


def check_connection():
    try:
        create_connection(("www.google.com", 80))
        isconnected = True
    except:
        isconnected = False
    return isconnected


def check_log_enabled(installDir):
    configFile = installDir + "onirc"
    parser = ConfigParser()
    parser.read(configFile)
    return parser.getboolean('config', 'save_session')

def check_custom_prompt(installDir):
    configFile = installDir + "onirc"
    parser = ConfigParser()
    parser.read(configFile)
    if parser.has_option("config", "prompt"):
        return str(parser.get("config","prompt"))+" "
    else:
        return "onifw > "

def debug_value(installDir):
    configFile = installDir + "onirc"
    parser = ConfigParser()
    parser.read(configFile)
    if parser.has_option("config", "debug"):
        return parser.getboolean("config","debug")
    else:
        return False

class ConfigOnstart:
    def __init__(self,installDir):
        self.installDir = installDir
        with open("{}data/version.txt".format(installDir)) as f:
            self.version = f.readlines()[0].rstrip("\n\r")
        f.close()
        self.configFile = installDir + "onirc"
        self.parser = ConfigParser()
        self.parser.read(self.configFile)
        self.startup()
    
    def startup(self):
        if self.parser.getboolean('config', 'show_ascii_art'):
            with open("{}data/logo_ascii.txt".format(self.installDir), 'r') as fin:
                print(color.color_random[0])
                print(fin.read())
                print(color.END)
            fin.close()
        if self.parser.getboolean('config', 'check_connectivity'):
            if check_connection():
                print(color.OKGREEN + "\n[*] - Connected to a network")
            else:
                print(color.BOLD)
                print(color.RED + "[!] - No connectivity!" + color.WHITE)
                print(color.RED + "[!] - Some tools might not work as intended" + color.END)
        if self.parser.getboolean('config', 'check_version'):
            Updater(self.installDir)
        if self.parser.getboolean('config', 'show_version'):
            print(color.color_random[0]+self.version)
        
        if self.parser.getboolean('config', 'show_options'):
            print(color.BOLD + color.LOGGING + "configuration:" + color.END)
            print("show_ascii_art: " + color.NOTICE      +str(self.parser.getboolean('config', 'show_ascii_art'))+ color.END)
            print("check_connectivity: " + color.NOTICE  +str(self.parser.getboolean('config', 'check_connectivity'))+ color.END)
            print("check_version: "       +color.NOTICE  +str(self.parser.getboolean('config', 'check_version'))+ color.END)
            print("show_version: "        +color.NOTICE  +str(self.parser.getboolean('config', 'show_version'))+ color.END)
            print("delete_cache_on_exit: "+color.NOTICE  +str(self.parser.getboolean('config', 'delete_cache_on_exit'))+color.END)
            print("remove_tools_on_exit: "+color.NOTICE  +str(self.parser.getboolean('config', 'remove_tools_on_exit'))+color.END)

class ConfigOnQuit:
    def __init__(self, installDir):
        self.installDir = installDir
        with open("{}data/version.txt".format(installDir)) as f:
            self.version = f.readlines()[0].rstrip("\n\r")
        f.close()
        self.configFile = installDir + "onirc"
        self.parser = ConfigParser()
        self.parser.read(self.configFile)
        self.onleave()

    def onleave(self):
        if self.parser.getboolean('config', 'delete_cache_on_exit'):
            cmd("rm -rf {}core/__pycache__".format(self.installDir))
            cmd("rm -rf {}__pycache__".format(self.installDir))
        if self.parser.getboolean('config', 'remove_tools_on_exit'):
            cmd("rm -rf {}/tools".format(self.installDir))



class CustomTool:
    def __init__(self,installDir,name):
        self.installDir = installDir
        with open("{}data/version.txt".format(installDir)) as f:
            self.version = f.readlines()[0].rstrip("\n\r")
        f.close()
        self.configFile = installDir + "onirc"
        self.parser = ConfigParser()
        self.parser.read(self.configFile)
        self.name = name
        self.custom()

    def custom(self):
        launch_cmd = self.parser.get('custom', self.name)
        cmd(launch_cmd)
        
class ConfigMisc:
    def __init__(self, installDir):
        self.installDir = installDir
        self.configFile = installDir + "onirc"
        self.logDir = installDir + "logs"
        self.parser = ConfigParser()
        self.parser.read(self.configFile)
        self.loadMisc()

    def loadMisc(self):
        if self.parser.getboolean('config', 'save_session'):
            if not path.isdir(self.logDir): mkdir(self.logDir)



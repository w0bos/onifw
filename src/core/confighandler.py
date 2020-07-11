import sys
import os
from sys import exit as abort
from os import system as cmd
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
        if self.parser.getboolean('startup', 'show_ascii_art'):
            with open("{}data/logo_ascii.txt".format(self.installDir), 'r') as fin:
                print(color.color_random[0])
                print(fin.read())
                print(color.END)
            fin.close()
        if self.parser.getboolean('startup', 'check_connectivity'):
            if check_connection():
                print(color.OKGREEN + "\n[*] - Connected to a network")
            else:
                print(color.BOLD)
                print(color.RED + "[!] - No connectivity!" + color.WHITE)
                print(color.RED + "[!] - Some tools might not work as intended" + color.END)
        if self.parser.getboolean('startup', 'check_version'):
            Updater(self.installDir)
        if self.parser.getboolean('startup', 'show_version'):
            print(color.color_random[0]+self.version)


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
        if self.parser.getboolean('onleave', 'delete_on_exit'):
            cmd("rm -rf {}core/__pycache__".format(self.installDir))
            cmd("rm -rf {}__pycache__".format(self.installDir))
        if self.parser.getboolean('onleave', 'remove_tools'):
            cmd("rm -rf {}/tools".format(self.installDir))

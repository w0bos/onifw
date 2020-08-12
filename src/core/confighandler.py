from os import system as cmd
from os import path
from os import makedirs as mkdir
from core.gui import color
from socket import create_connection
from configparser import ConfigParser


# Misc functions

def get_connection():
    try:
        create_connection(("www.google.com", 80))
        isconnected = True
    except:
        isconnected = False
    return isconnected


# Check values


def check_value(installDir,value,default):
    configFile = installDir + "onirc"
    parser = ConfigParser()
    parser.read(configFile)
    if parser.has_option('config', value):
        return parser.getboolean('config', value)
    else:
        return default


def check_prompt(installDir):
    configFile = installDir + "onirc"
    parser = ConfigParser()
    parser.read(configFile)
    if parser.has_option('config', 'prompt'):
        return str(parser.get('config', 'prompt'))+" "
    else:
        return "onifw > "



class ConfigOnstart:
    def __init__(self,installDir):
        self.installDir = installDir
        with open("{}data/version.txt".format(installDir)) as f:
            self.version = f.readlines()[0].rstrip("\n\r")
        f.close()
        self.startup()
    
    def startup(self):
        if check_value(self.installDir,"show_ascii_art",True):
            with open("{}data/logo_ascii.txt".format(self.installDir), 'r') as fin:
                print(color.color_random[1]+fin.read())
                print(color.END)
            fin.close()
        if check_value(self.installDir, "check_updates", False):
            from core.updater import Updater
            Updater(self.installDir)
        if check_value(self.installDir, "show_version", True):
            print(color.color_random[0]+"\t\tVersion: "+self.version)
        if check_value(self.installDir, "check_connectivity", True):
            if get_connection():
                print(color.OKGREEN + "\n[*] - Connected to a network")
            else:
                print(color.BOLD)
                print(color.RED + "[!] - No connectivity!" + color.WHITE)
                print(
                    color.RED + "[!] - Some tools might not work as intended" + color.END)
        if check_value(self.installDir, "show_options", False):
            print(color.BOLD + color.LOGGING + "configuration:" + color.END)
            print("show_ascii_art: "    +color.NOTICE  +str(check_value(self.installDir,"show_ascii_art",True))       + color.END)
            print("check_connectivity: "+color.NOTICE  +str(check_value(self.installDir,"check_connectivity",True))   + color.END)
            print("check_updates: "     +color.NOTICE  +str(check_value(self.installDir,"check_updates",False))       + color.END)
            print("show_version: "      +color.NOTICE  +str(check_value(self.installDir,"show_version",True))         + color.END)
            print("delete_cache: "      +color.NOTICE  +str(check_value(self.installDir,"delete_cache",True))         + color.END)
            print("remove_tools: "      +color.NOTICE  +str(check_value(self.installDir,"remove_tools",False))        + color.END)
            print("save_session: "      +color.NOTICE  +str(check_value(self.installDir,"save_session",False))        + color.END)
            print("debug: "             +color.NOTICE  +str(check_value(self.installDir,"debug",False))               + color.END)
            print("show_loading: "      +color.NOTICE  +str(check_value(self.installDir, "show_loading", True))       + color.END)
            print("prompt: "            +color.NOTICE  +str(check_prompt(self.installDir)) + color.END)


class ConfigOnQuit:
    def __init__(self, installDir):
        self.installDir = installDir
        with open("{}data/version.txt".format(installDir)) as f:
            self.version = f.readlines()[0].rstrip("\n\r")
        f.close()
        self.onleave()

    def onleave(self):
        if check_value(self.installDir,"delete_cache",True):
            cmd("rm -rf {}core/__pycache__".format(self.installDir))
            cmd("rm -rf {}__pycache__".format(self.installDir))
        if check_value(self.installDir,"remove_tools",False):
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
        self.logDir = installDir + "logs"
        self.loadMisc()

    def loadMisc(self):
        if check_value(self.installDir,"save_session",False):
            if not path.isdir(self.logDir): mkdir(self.logDir) # Make the dir
            if not path.isfile(self.logDir+"oni.log"): cmd("touch {}/oni.log".format(self.logDir))
        

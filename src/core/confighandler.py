from os import system as cmd
from os import path
from os import makedirs as mkdir
from core.gui import color, logos
import core.logHandler as logh
from configparser import ConfigParser
from core.onilib import check_prompt, check_value, get_connection, return_colored_prefix



class ConfigOnstart:
    def __init__(self, installDir):
        self.installDir = installDir
        with open("{}data/version.txt".format(installDir)) as f:
            self.version = f.readlines()[0].rstrip("\n\r")
        f.close()
        self.startup()

    def startup(self):
        if check_value(self.installDir, "custom_ascii", 0, False) != 0:
            with open("{}".format(check_value(self.installDir, "custom_ascii", 0, False)), "r") as fin:
                print(color.color_random[1] + fin.read())
                print(color.END)
            fin.close()
        else:
            if check_value(self.installDir, "show_ascii", True):
                #with open("{}data/logo_ascii.txt".format(self.installDir), 'r') as fin:
                #    print(color.color_random[1] + fin.read())
                #    print(color.END)
                #fin.close()
                print(color.color_random[1] + logos.ascii_art[0] + color.END)
        if check_value(self.installDir, "check_updates", False):
            from core.updater import Updater
            Updater(self.installDir)
        if check_value(self.installDir, "show_version", True):
            print(color.color_random[0] + "\t\tVersion: " + self.version)
        if check_value(self.installDir, "check_connectivity", True):
            if get_connection():
                print(return_colored_prefix("*") + "- Connected to a network")
            else:
                print(color.BOLD)
                print(return_colored_prefix("!") +
                      "- No connectivity!" + color.WHITE)
                print(return_colored_prefix("!") +
                      "- Some tools might not work as intended" + color.END)
        if check_value(self.installDir, "show_options", False):
            print(color.BOLD + color.LOGGING + "configuration:" + color.END)
            print("show_ascii: " + color.NOTICE + str(check_value(self.installDir, "show_ascii", True)) + color.END)
            print("custom_ascii: " + color.NOTICE + str(check_value(self.installDir, "custom_ascii", 0, True)) + color.END)
            print("check_connectivity: " + color.NOTICE + str(check_value(self.installDir, "check_connectivity", True)) + color.END)
            print("check_updates: " + color.NOTICE + str(check_value(self.installDir, "check_updates", False)) + color.END)
            print("show_version: " + color.NOTICE + str(check_value(self.installDir, "show_version", True)) + color.END)
            print("delete_cache: " + color.NOTICE + str(check_value(self.installDir, "delete_cache", True)) + color.END)
            print("remove_tools: " + color.NOTICE + str(check_value(self.installDir, "remove_tools", False)) + color.END)
            print("save_session: " + color.NOTICE + str(check_value(self.installDir, "save_session", False)) + color.END)
            print("debug: " + color.NOTICE + str(check_value(self.installDir, "debug", False)) + color.END)
            print("show_loading: " + color.NOTICE + str(check_value(self.installDir, "show_loading", True)) + color.END)
            print("prompt: " + color.NOTICE + str(check_prompt(self.installDir)) + color.END)


class ConfigOnQuit:
    def __init__(self, installDir):
        self.installDir = installDir
        with open("{}data/version.txt".format(installDir)) as f:
            self.version = f.readlines()[0].rstrip("\n\r")
        f.close()
        self.onleave()

    def onleave(self):
        if check_value(self.installDir, "delete_cache", True):
            cmd("rm -rf {}core/__pycache__".format(self.installDir))
            cmd("rm -rf {}__pycache__".format(self.installDir))
        if check_value(self.installDir, "remove_tools", False):
            cmd("rm -rf {}/tools".format(self.installDir))

class CustomTool:
    def __init__(self, installDir, name):
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
        self.logDir = installDir + "logs/"
        self.loadMisc()

    def loadMisc(self):
        if check_value(self.installDir, "save_session", False):
            if not path.isdir(self.logDir): mkdir(self.logDir) # Make the dir
            if not path.isfile(self.logDir + "oni.log"): cmd("touch {}/oni.log".format(self.logDir))
            logh.LogHandler(self.installDir, self.logDir, [], True)

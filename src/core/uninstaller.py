from sys import exit
from os import chdir, getcwd
from os import system as shell


class Uninstall:
    
    def __init__(self,installDir):
        self.installDir=installDir
        self.binDir = "/usr/local/bin/onifw"
        print("[*] - Looking for current install")
        try:
            os.chdir("$HOME")
            shell("rm -rf {}".format(self.installDir))
            shell("sudo rm {}".format(self.binDir))
            shell("pkkill -f oni.py")
        except:
            print("[*] - An unexpected error occurred")

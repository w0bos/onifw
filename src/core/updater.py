import os

import core.confighandler as cfg
from configparser import ConfigParser
from sys import exc_info as err
from packaging import version
from core.gui import color as color
import subprocess

class Updater:

    def __init__(self, installDir):
        self.installDir=installDir
        if not self.check_branch():
            try:
                with open("{}data/version.txt".format(installDir)) as f:
                    local_version = version.parse(f.readlines()[0].rstrip("\n\r"))
                f.close()
    
                if not os.path.isdir("{}/temp".format(installDir)):  os.makedirs("{}/temp".format(installDir))
                os.system("wget -q -O {}/temp/latest_version.txt https://raw.githubusercontent.com/w0bos/onifw/master/src/data/version.txt".format(installDir))
                with open("{}/temp/latest_version.txt".format(installDir)) as f:
                    latest_version = version.parse(f.readlines()[0].rstrip("\n\r"))
                f.close()
    
                if (latest_version>local_version):
                    ans = input(color.NOTICE + "[*] - A new version is available\nDo you wish to install the new update? [y/N] :" + color.END)
                    if ans.lower() in ["yes","y"]:
                        # Won't wipe old install
                        os.system("cd {} && git pull".format(installDir))
                        #os.system("{}../install.sh".format(installDir))
                    else:
                        print("[*] - Update aborted")
    
                elif (latest_version==local_version) :
                    print(color.OKGREEN + "[*] - You're already running the latest version of onifw" + color.END)
                elif (latest_version<local_version):
                    print(color.IMPORTANT + "[+] - You are running an alpha version of onifw" + color.END)
                else:
                    print(color.WARNING + "[!] - Unknown error" + color.END)
    
                os.system("rm -rf {}/temp".format(installDir))
            except:
                print("[!] - An unexpected error occurred! Please try again")
                if cfg.check_value(installDir,"debug",False):
                    print(err())

    def check_branch(self):
        curr_branch = subprocess.check_output("cd {} && git branch --show-current".format(self.installDir), shell=True).decode("utf-8").strip('\n')
        if curr_branch == "dev":
            print("[!] - Currently working on the dev branch. Updates can only be done while in the master branch\n[!] - Use checkout master to switch to the master branch")
            return True

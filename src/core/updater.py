from os import makedirs as mkdir
from os import path
from core.gui import color
from os import system as shell
from core.errorHandler import ErrorHandler
from sys import exc_info as err
from packaging import version
from subprocess import check_output



class Updater:

    def __init__(self, installDir):
        self.installDir=installDir
        if self.check_branch():
            try:
                with open("{}data/version.txt".format(installDir)) as f:
                    local_version = version.parse(f.readlines()[0].rstrip("\n\r"))
                f.close()
    
                latest_version = check_output(
                    "curl -s https://raw.githubusercontent.com/w0bos/onifw/master/src/data/version.txt", shell=True).decode("utf-8").strip('\r\n')
                #if not path.isdir("{}/temp".format(installDir)):  mkdir("{}/temp".format(installDir))
                #shell("wget -q -O {}/temp/latest_version.txt https://raw.githubusercontent.com/w0bos/onifw/master/src/data/version.txt".format(installDir))
                #with open("{}/temp/latest_version.txt".format(installDir)) as f:
                #    latest_version = version.parse(f.readlines()[0].rstrip("\n\r"))
                #f.close()
                late = version.parse(latest_version)
                if (late>local_version):
                    ans = input(color.NOTICE + "[*] - A new version is available\nDo you wish to install the new update? [y/N] :" + color.END)
                    if ans.lower() in ["yes","y"]:
                        # Won't wipe old install
                        shell("cd {} && git pull".format(installDir))
                    else:
                        print("[*] - Update aborted")
    
                elif (late==local_version) :
                    print(color.OKGREEN + "[*] - You're already running the latest version of onifw" + color.END)
                elif (late<local_version):
                    print(color.BOLD + color.IMPORTANT + "[+] - You are running an alpha version of onifw" + color.END)
                else:
                    print(color.WARNING + "[!] - Unknown error" + color.END)
    
                shell("rm -rf {}/temp".format(installDir))
            except:
                ErrorHandler(err(), False, True)
                #print("[!] - An unexpected error occurred! Please try again")
                #if cfg.check_value(installDir,"debug",False):
                #    print(err())    

    def check_branch(self):
        curr_branch = check_output("cd {} && git branch --show-current".format(self.installDir), shell=True).decode("utf-8").strip('\n')
        if curr_branch == "dev":
            print(color.HEADER + "[!] - Currently working on the dev branch. Updates can only be done while in the master branch")
            print("[!] - Use the checkout command to switch to the master branch"+color.END)
            return True

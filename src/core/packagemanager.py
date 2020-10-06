#!/usr/bin/env python

from os import system as shell
from sys import exc_info as err

import core.dict as dictmgr
from core.errorHandler import ErrorHandler
from core.gui import color
from core.onilib import readfile
from core.onilib import abort, uninstall, remove_all

# Dict to stop using absolute values
pkg = {
    "microsploit"  :   "https://github.com/Screetsec/Microsploit",
    "poet"         :   "https://github.com/mossberg/poet",
    "weeman"       :   "https://github.com/samyoyo/weeman",
    "sb0x"         :   "https://github.com/lostcitizen/sb0x-project",
    "nmap"         :   "https://github.com/nmap/nmap",
    "xsstrike"     :   "https://github.com/UltimateHackers/XSStrike.git",
    "doork"        :   "https://github.com/AeonDave/doork.git",
    "crips"        :   "https://github.com/Manisso/Crips.git",
    "wpscan"       :   "https://github.com/wpscanteam/wpscan.git",
    "setoolkit"    :   "https://github.com/trustedsec/social-engineer-toolkit.git",
    "cupp"         :   "https://github.com/Mebus/cupp.git",
    "brutex"       :   "https://github.com/1N3/BruteX.git",
    "leviathan"    :   "https://github.com/tearsecurity/leviathan",
    "ssltrip"      :   "https://github.com/arnolix/ssltrip",
    "sqlmap"       :   "https://github.com/sqlmapproject/sqlmap",
    "slowloris"    :   "https://github.com/gkbrk/slowloris",
    "atscan"       :   "https://github.com/AlisamTechnology/ATSCAN",
    "nikto"        :   "https://github.com/sullo/nikto",
    "rapidscan"    :   "https://github.com/skavngr/rapidscan",
    "apwps"        :   "https://github.com/nxxxu/AutoPixieWps",
    "snmp"         :   "https://github.com/SECFORCE/SNMP-Brute",
    "revsh"        :   "https://github.com/emptymonkey/revsh",
    "arachni"      :   "https://github.com/Arachni/arachni.git"
}


def show_recommended():
    """
    Displays the list of recommended packages\n
    \nArguments:\n
    packages : Required (dict)
    """
    print("\033[32m" + "Recommended packages\n" + "\033[93m")
    keys = [i for i in pkg.keys()]
    for i in range(0, len(keys), 2):
        if i < len(keys)-1:
            print("%-15s" "%s" % (keys[i], keys[i+1]))
        else:
            print("%s" % (keys[i]))
    print("\033[97m")


class Install:
    def __init__(self, installDir, args=[], force=False):
        self.toolDir = installDir + 'tools/'
        self.installDir = installDir
        self.args = args
        if len(args)<1:
            if force:
                self.install_all()
            else:
                ans = input(
                    color.IMPORTANT +
                    "[*] - Installation process can be quite long.\nProceed anyways?\n[y/N] : " 
                    + color.END).lower()
                if ans in ["y", "yes"]:
                    self.install_all()
        else:
            self.install_some()

    def install_all(self):
        wordlist=[]
        for i in pkg:
            temp_install_dir = self.toolDir+i
            if i in ["crips", "arachni", "brutex", "revsh", "nmap"]:
                self.build_tools(i,temp_install_dir)
            else:
                print(color.LOGGING + "[+] - Installing " +
                      color.NOTICE+"{}".format(i)+"...")
                shell("git clone -q {0} {1}".format(pkg[i], temp_install_dir))
                wordlist.append(i)
        self.add_words(wordlist)

    def install_some(self):
        tempDir = []
        
        for i in range(len(self.args)):
            tree = self.installDir + "tools/" + self.args[i]
            tempDir.append(tree)

        for i in range(len(self.args)):
            target=self.args[i]
            if target in ["crips", "arachni", "brutex", "revsh", "nmap"]:
                self.build_tools(target, tempDir[i])
            else:
                # target is package
                if target in pkg:
                    print(color.LOGGING + "[+] - Installing " +
                          color.NOTICE+"{}".format(target)+color.LOGGING+"...")
                    shell("git clone -q {0} {1}".format(pkg[target], tempDir[i]))
                else:
                    print(color.RED+"[*] - Unkown package. Please retry or use the custom package installer"+color.END)

        self.add_words(self.args)
        
    def build_tools(self, target, tempDir):
        print(color.LOGGING + "[+] - Installing "+color.NOTICE+"{}".format(target)+color.LOGGING+"...")
        if target == "crips":
            shell("git clone -q %s %s" % (pkg[target], tempDir))
            shell("sudo chmod +x %s/install.sh" % (tempDir))
            shell("sudo %s/install.sh" % (tempDir))

        elif target == "arachni":
            shell("git clone -q %s %s" % (pkg[target], tempDir))
            shell("cd %s/ && bundle install" % (tempDir))

        elif target == "brutex":
            shell("sudo git clone -q %s %s && cd %s && ./install.sh" % (pkg[target], tempDir, tempDir))

        elif target == "revsh":
            #Configure OPENSSL
            print(color.OKBLUE+"[+] - Configuring openssl for revsh..."+color.END)
            shell("git clone -q %s %s" %
                  ("https://github.com/openssl/openssl", self.toolDir+"openssl"))
            shell("cd {0} && ./config no-shared -static && make && make test".format(self.toolDir+"openssl"))
            shell("git clone -q %s %s" % (pkg[target], tempDir))
            shell("cd %s/ && make && make install" % (tempDir))

        elif target == "nmap":
            shell("git clone -q %s %s && cd %s/ && ./configure && make && make install" %
                  (pkg[target], tempDir, tempDir))

    def install_dependencies(self, targetDir, target):
        """
        Install dependecies with pip
        """
        tool_req_file = targetDir + "requiremets.txt"
        try:
            shell("sudo pip install -r {}".format(tool_req_file))
        except:
            ErrorHandler(err(), False, True)



    def add_words(self, wordList=[]):
        print(color.OKGREEN+"[*] - Done."+color.END)
        if not(len(wordList)):
            for i in pkg:
                wordList.append(i)
        dictmgr.addWords(self.installDir, wordList)

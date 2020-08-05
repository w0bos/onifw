#!/usr/bin/env python

import core.dict as dictmgr
import core.confighandler as cfg

from os import system as shell
from core.gui import color
from configparser import ConfigParser
from sys import exc_info as err


# Dict to stop using absolute values
pkg = {
    "microsploit"  :   "https://github.com/Screetsec/Microsploit",
    "poet"         :   "https://github.com/mossberg/poet",
    "weeman"       :   "https://github.com/samyoyo/weeman",
    "sb0x"         :   "https://github.com/lostcitizen/sb0x-project",
    "nxcrypt"      :   "https://github.com/Hadi999/NXcrypt",
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
    "hyde"         :   "https://github.com/hyde/hyde",
    "nikto"        :   "https://github.com/sullo/nikto",
    "rapidscan"    :   "https://github.com/skavngr/rapidscan",
    "apwps"        :   "https://github.com/nxxxu/AutoPixieWps",
    "snmp"         :   "https://github.com/SECFORCE/SNMP-Brute",
    "revsh"        :   "https://github.com/emptymonkey/revsh",
    "arachni"      :   "https://github.com/Arachni/arachni.git"
}

scripts = [
    ["pypisher",        "http://pastebin.com/raw/DDVqWp4Z"],
    ["smtp",            "http://pastebin.com/raw/Nz1GzWDS"]
]


def load_debug(installDir):
    return cfg.debug_value(installDir)

def show_recommended():
    print("\033[32m" + "Recommended packages\n" + "\033[93m")
    keys = [i for i in pkg.keys()]
    for i in range(0,len(keys),2):
        if i<len(keys)-1:
            print("%-15s" "%s" % (keys[i], keys[i+1]))
        else:
            print("%s" % (keys[i]))
    print("\033[97m")


def abort():
    input(color.LOGGING +
          "[*] - Installation canceled, press [return] to go back" + color.WHITE)


def uninstall(installDir, cmd, root=0):
    print("[*] - Removing folder")
    if not root:
        shell("rm -rf {0}tools/{1}".format(installDir, cmd[2]))
    else:
        shell("sudo rm -rf {0}tools/{1}".format(installDir, cmd[2]))
    print("[*] - Cleaning dictionnary...")
    f = open("{}data/dict.txt".format(installDir))
    out = []
    for line in f:
        if not cmd[2] in line:
            out.append(line)
    f.close()
    f = open("{}data/dict.txt".format(installDir), 'w')
    f.writelines(out)
    f.close()

class Install:
    def __init__(self, installDir, args=[]):
        self.toolDir = installDir + 'tools/'
        self.installDir = installDir
        self.args = args
        if len(args)<1:
            self.install_all()
        else:
            self.install_some()

    def install_all(self):
        ans = input(
            #color.IMPORTANT 
            "[*] - Installation process can be quite long.\nProceed anyways?\n [y/N] : " ).lower()
            #+ color.WHITE).lower()
        if ans in ["y", "yes"]:
            for i in pkg:
                temp_install_dir = self.toolDir+i

                if i in ["crips", "arachni", "brutex", "revsh", "nmap"]:
                    self.build_tools(i,temp_install_dir)
                else:
                    print("[+] - Installing {}...".format(pkg[i]))
                    shell("git clone -q {0} {1}".format(pkg[i], temp_install_dir))

            for i in range(len(scripts)):
                print("[+] - Installing {}...".format(scripts[i][0]))
                shell("wget -q %s --output-document=%s.py" %
                      (scripts[i][1], scripts[i][0]))
                shell("mv %s.py %s%s.py" % (
                    scripts[i][0], temp_install_dir, scripts[i][0]))

            self.add_words()

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
                    print("[+] - Installing {}...".format(target))
                    shell("git clone -q {0} {1}".format(pkg[target], tempDir[i]))
                # target is script
                elif target in scripts:
                    shell("wget %s --output-document=%s.py" %
                          (scripts[i][1], scripts[i][0]))
                    shell("mv %s.py %s%s.py" % (
                        scripts[i][0], tempDir, scripts[i][0]))
                else:
                    print("[*] - Unkown package. Please retry or use the custom package installer")

        self.add_words(self.args)
        
    def build_tools(self, target, tempDir):

        print("[+] - Installing {}...".format(target))
        if target == "crips":
            shell("git clone -q %s %s" % (pkg[target], tempDir))
            shell("sudo chmod +x %s/install.sh" % (tempDir))
            shell("sudo %s/install.sh" % (tempDir))

        elif target == "arachni":
            shell("git clone -q %s %s" % (pkg[target], tempDir))
            shell("cd %s/ && bundle install" % (tempDir))

        elif target == "brutex":
            shell("sudo mkdir /usr/share/brutex")
            shell("git clone -q %s %s" % (pkg[target], tempDir))

        elif target == "revsh":
            #Configure OPENSSL
            print("[+] - Configuring openssl for revsh...")
            shell("git clone -q %s %s" %
                  ("https://github.com/openssl/openssl", self.toolDir+"openssl"))
            shell("cd {0} && ./config no-shared -static && make && make test".format(self.toolDir+"openssl"))
            shell("git clone -q %s %s" % (pkg[target], tempDir))
            shell("cd %s/ && make && make install" % (tempDir))

        elif target == "nmap":
            shell("git clone %s %s && cd %s/ && ./configure && make && make install" %
                  (pkg[target], tempDir, tempDir))

    def add_words(self, wordList=[]):
        print("[*] - Done.")
        if not(len(wordList)):
            for i in pkg:
                wordList.append(i)
        dictmgr.addWords(self.installDir, wordList)

Install("/home/scandion/Documents/Git/w0bos/onifw/src/", ["nikto", "revsh"])

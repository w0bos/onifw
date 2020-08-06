#!/usr/bin/env python

import os
import core.dict as dictmgr
from os import system as shell
from core.gui import color
import core.confighandler as cfg
from configparser import ConfigParser
from sys import exc_info as err


def load_debug(installDir):
    return cfg.debug_value(installDir)

pkg = [
    ["microsploit",     "https://github.com/Screetsec/Microsploit"],
    ["poet",            "https://github.com/mossberg/poet"],
    ["weeman",          "https://github.com/samyoyo/weeman"],
    ["sb0x",            "https://github.com/lostcitizen/sb0x-project"],
    ["nxcrypt",         "https://github.com/Hadi999/NXcrypt"],
    ["nmap",            "https://github.com/nmap/nmap"],
    ["xsstrike",        "https://github.com/UltimateHackers/XSStrike.git"],
    ["doork",           "https://github.com/AeonDave/doork.git"],
    ["crips",           "https://github.com/Manisso/Crips.git"],
    ["wpscan",          "https://github.com/wpscanteam/wpscan.git"],
    ["setoolkit",       "https://github.com/trustedsec/social-engineer-toolkit.git"],
    ["cupp",            "https://github.com/Mebus/cupp.git"],
    ["brutex",          "https://github.com/1N3/BruteX.git"],
    ["leviathan",       "https://github.com/tearsecurity/leviathan"],
    ["ssltrip",        "https://github.com/arnolix/ssltrip"],
    ["sqlmap",          "https://github.com/sqlmapproject/sqlmap"],
    ["slowloris",       "https://github.com/gkbrk/slowloris"],
    ["atscan",          "https://github.com/AlisamTechnology/ATSCAN"],
    ["hyde",            "https://github.com/hyde/hyde"],
    ["nikto",           "https://github.com/sullo/nikto"],
    ["rapidscan",       "https://github.com/skavngr/rapidscan"],
    ["apwps",           "https://github.com/nxxxu/AutoPixieWps"],
    ["snmp",            "https://github.com/SECFORCE/SNMP-Brute"],
    ["revsh",           "https://github.com/emptymonkey/revsh"],
    ["arachni",         "https://github.com/Arachni/arachni.git"]
]
scripts = [
    ["pypisher",        "http://pastebin.com/raw/DDVqWp4Z"],
    ["smtp",            "http://pastebin.com/raw/Nz1GzWDS"]
]


def show_recommended():
    print("\033[32m" + "Recommended packages\n" + "\033[93m")
    for i in range(0, len(pkg), 2):
         if i < len(pkg)-1:
             print("%-15s" "%s" % (pkg[i][0], pkg[i+1][0]))
         else:
             print("%s" % (pkg[i][0]))
    print("\033[32m" + "\nRecommended scripts\n" + "\033[93m")
    for i in range(len(scripts)):
        print("%s" % scripts[i][0])
    # customz = 2
    print("\033[97m")


def abort():
    input(color.LOGGING +
          "[*] - Installation canceled, press [return] to go back" + color.WHITE)


def uninstall(installDir,cmd,root=0):
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
    def __init__(self, installDir, pack=[]):

        self.toolDir = installDir + 'tools/'
        self.installDir = installDir
        # /g/ humor 
        # self.defaultDir = installDir

        #if not len(pack):
        #    self.install_all()
        #else:
        #    self.install_some(pack)
        self.install_all()

    def install_all(self):
        ans = input(
                color.IMPORTANT + "[*] - Installation process can be quite long.\nProceed anyways?\n [y/N] : " + color.WHITE).lower()
        if ans == "y":
            for i in range(len(pkg)):
                tempDir = self.toolDir + pkg[i][0]
                # PASS
                if pkg[i][0] == "crips":
                    shell("git clone %s %s" %
                              (pkg[i][1], tempDir))
                    shell("sudo chmod +x %s/install.sh" %
                              (tempDir))
                    shell("sudo %s/./install.sh" %
                              (tempDir))
                # PASS
                # !!! User MUST check dependencies
                elif pkg[i][0] == "arachni":
                    shell("git clone %s %s" %
                              (pkg[i][1], tempDir))
                    shell("cd %s/ && bundle install" %
                              (tempDir))
                elif pkg[i][0] == "brutex":
                    shell("sudo mkdir /usr/share/brutex")
                    shell("git clone %s %s" %
                              (pkg[i][1], tempDir))
                elif pkg[i][0] == "revsh":
                    shell("git clone %s %s" %
                              (pkg[i][1], tempDir))
                    shell("cd %s/ && make && make install" %
                              (tempDir))

                # ERROR ON BUILD
                elif pkg[i][0] == "nmap":
                    shell("git clone %s %s && cd %s/ && ./configure && make && make install" %
                              (pkg[i][1], tempDir, tempDir))
                else:                            
                    shell("git clone %s %s" %
                              (pkg[i][1], tempDir))

            for i in range(len(scripts)):
                shell("wget %s --output-document=%s.py" %
                          (scripts[i][1], scripts[i][0]))
                shell("mv %s.py %s%s.py" % (
                    scripts[i][0], tempDir, scripts[i][0]))
            #Generate all wordlist
            wordList = []
            for i in range(len(pkg)):
                wordList.append(pkg[i][0])
            dictmgr.addWords(self.installDir,wordList)
        else:
            abort()


    #   IS THE SAME AS USERINSTALL?
    def install_some(self,pack):
        for i in pack:
            for j in range(len(pkg)):
                if i == pkg[j][0]:
                    try:
                        self.installDir = self.toolDir + pkg[j][0]
                        tempDir = self.toolDir + pkg[j][0]
                        if not (i in ("crips", "arachni","revsh","nmap")):
                            shell("git clone %s %s" %
                                  (pkg[j][1], tempDir))
                        else:
                            if i == "crips":
                                shell("git clone %s %s" % (
                                    pkg[j][1], tempDir))
                                shell(
                                    "sudo chmod +x %s/install.sh" % (tempDir))
                                shell("sudo %s/./install.sh" %
                                      (tempDir))
                            elif i == "arachni":
                                shell("git clone %s %s" % (
                                    pkg[j][1], tempDir))
                                shell(
                                    "cd %s/ && bundle install" % (tempDir))
                            elif i == "revsh":
                                shell("git clone %s %s" % (
                                    pkg[j][1], tempDir))
                                shell(
                                    "cd %s/ && make && make install" % (tempDir))
                            elif i == "nmap":
                                shell("git clone %s %s && cd %s/ && ./configure && make && make install" % (
                                    pkg[j][1], tempDir, tempDir))
                    except:
                        print(color.NOTICE + "[!] - An error occurred" + color.WHITE)
                        if cfg.check_value(self.installDir, "debug", False):
                            print(err())

'''
DONT USE PKG[<value>], PKG[<var>] instead
'''
class User_install:

    def __init__(self, installDir, cmd):
        self.target = cmd[2:]
        self.absDir = installDir
        self.installDir = []
        for i in range(len(self.target)):
            tree = installDir + "tools/" + self.target[i]
            self.installDir.append(tree)
        self.bugpkg = ["arachni", "crips", "brutex", "revsh", "nmap"]
        self.install()

    def install(self):
        for i in range(len(self.target)):
            if self.target[i] in scripts:
                for i in range(len(scripts)):
                    if self.target[i] == scripts[i][0]:
                        shell("wget %s --output-document=%s.py" %
                                  (scripts[i][1], scripts[i][0]))
            elif not (self.target[i] in self.bugpkg):
                for i in range(len(self.target)):
                    for j in range(len(pkg)):
                        if self.target[i] == pkg[j][0]:
                            print("[*] - Installing %s" % (self.target[i]))
                            shell("git clone %s %s" %
                                      (pkg[j][1], self.installDir[i]))
            else:
                if self.target[i] == "crips":
                    shell("git clone %s %s" %
                              (pkg[8][1], self.installDir[i]))
                    shell("sudo chmod +x %s/install.sh" %
                              (self.installDir[i]))
                    shell("sudo %s/./install.sh" % (self.installDir[i]))
                elif self.target[i] == "arachni":
                    shell("git clone %s %s" %
                              (pkg[24][1], self.installDir[i]))
                    shell("cd %s/ && bundle install" %
                              (self.installDir[i]))
                elif self.target[i] == "brutex":
                    shell("sudo mkdir /usr/share/brutex")
                    shell("git clone %s %s" %
                              (pkg[12][1], self.installDir[i]))
                elif self.target[i] == "revsh":
                    shell("git clone %s %s" %
                              (pkg[23][1], self.installDir[i]))
                    shell("cd %s/ && make && make install" %
                              (self.installDir[i]))
                elif self.target[i] == "nmap":
                    shell("git clone %s %s && cd %s/ && ./configure" %
                              (pkg[5][1], self.installDir[i], self.installDir[i]))
                    shell("git clone %s %s && cd %s/ && ./configure" %
                          ("https://github.com/openssl/openssl", self.absDir+"tools/openssl", self.absDir+"tools/openssl"))
                    shell("cd %s/ && sudo make && make install" %
                              self.installDir[i])
                    # shell("sudo make install")
            wordList = []
            for i in self.target:
                wordList.append(i)
            print(wordList)
            dictmgr.addWords(self.absDir,wordList)

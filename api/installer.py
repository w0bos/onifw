#!/usr/bin/env python

import os

def clearScr():
    os.system('clear')

class color:
    HEADER =    '\033[96m'
    IMPORTANT = '\033[35m'
    NOTICE =    '\033[32m'
    OKBLUE =    '\033[94m'
    OKGREEN =   '\033[92m'
    WARNING =   '\033[91m'
    RED =       '\033[31m'
    END =       '\033[0m'
    LOGGING =   '\033[93m'
    WHITE =     '\033[97m'

class Installer:
    def __init__(self, show, installDir, pack=[]):
        
        self.toolDir = installDir + 'tools/'
        self.logDir = installDir + 'log/'
        clearScr()

        self.pkg = [
            ["microsploit",     "https://github.com/Screetsec/Microsploit"],
            ["poet",            "https://github.com/mossberg/poet"],
            ["weeman",          "https://github.com/samyoyo/weeman"],
            ["sb0x",            "https://github.com/lostcitizen/sb0x-project"],
            ["nxcrypt",         "https://github.com/Hadi999/NXcrypt"],
            ["nmap",            "https://github.com/nmap/nmap.git"],
            ["xsstrike",        "https://github.com/UltimateHackers/XSStrike.git"],
            ["doork",           "https://github.com/AeonDave/doork.git"],
            ["crips",           "https://github.com/Manisso/Crips.git"],
            ["wpscan",          "https://github.com/wpscanteam/wpscan.git"],
            ["setoolkit",       "https://github.com/trustedsec/social-engineer-toolkit.git"],
            ["cupp",            "https://github.com/Mebus/cupp.git"],
            ["brutex",          "https://github.com/1N3/BruteX.git"],
            ["leviathan",       "https://github.com/tearsecurity/leviathan"],
            ["sslstrip",        "https://github.com/arnolix/ssltrip"],
            ["sqlmap",          "https://github.com/sqlmapproject/sqlmap"],
            ["slowloris",       "https://github.com/gkbrk/slowloris"],
            ["pwnloris",        "https://github.com/h0ussni/pwnloris"],
            ["atscan",          "https://github.com/AlisamTechnology/ATSCAN"],
            ["hyde",            "https://github.com/hyde/hyde"],
            ["nikto",           "https://github.com/sullo/nikto"],
            ["rapidscan",       "https://github.com/skavngr/rapidscan"],
            ["apwps",           "https://github.com/nxxxu/AutoPixieWps"],
            ["snmp",            "https://github.com/SECFORCE/SNMP-Brute"],
            ["revsh",           "https://github.com/emptymonkey/revsh"],
            ["arachni",         "https://github.com/Arachni/arachni.git"],
            ["openssl",         "https://github.com/openssl/openssl.git"],
        ]
        self.scripts = [
            ["pypisher",        "http://pastebin.com/raw/DDVqWp4Z"],
            ["smtp",            "http://pastebin.com/raw/Nz1GzWDS"]
        ]

        if show == 0:
            if not len(pack):
                ans = input(color.IMPORTANT + "[*] - Installation process can be quite long.\nProceed anyways?\n [Y/N] : " + color.WHITE)
                if ans.lower() == "y":            
                    for i in range(len(self.pkg)):
                        self.installDir = self.toolDir + self.pkg[i][0]

                        if self.pkg[i][0] == "Crips":
                            clearScr()
                            os.system("git clone %s %s" % (self.pkg[i][1], self.installDir))
                            os.system("sudo chmod +x %s/install.sh" % (self.installDir))
                            os.system("sudo %s/./install.sh" % (self.installDir))

                        elif self.pkg[i][0] == "arachni":
                            clearScr()
                            os.system("git clone %s %s" % (self.pkg[i][1], self.installDir))
                            os.system("cd %s/ && bundle install" % (self.installDir))

                        elif self.pkg[i][0] == "openssl":
                            clearScr()
                            os.system("git clone %s %s" %(self.pkg[i][1], self.installDir))
                            os.system("cd %s/ && ./config no-shared -static && make && make test && sudo make install" % self.installDir)
                        
                        elif self.pkg[i][0] == "brutex":
                            clearScr()
                            os.system("sudo mkdir /usr/share/brutex")
                            os.system("git clone %s %s" % (self.pkg[i][1],self.installDir))

                        elif self.pkg[i][0] == "revsh":
                            clearScr()
                            os.system("git clone %s %s" %(self.pkg[i][1], self.installDir))
                            os.system("cd %s/ && make && make install" % (self.installDir))       

                        else:
                            clearScr()
                            os.system("git clone %s %s" % (self.pkg[i][1], self.installDir))

                    for i in range(len(self.scripts)):
                        os.system("wget %s --output-document=%s.py" % (self.scripts[i][1], self.scripts[i][0]))
                        os.system("mv %s.py %s%s.py" % (self.scripts[i][0], self.toolDir, self.scripts[i][0]))

                    self.completed()

                else:
                    self.aborted()

            elif len(pack):
                for i in pack:
                    for j in range(len(self.pkg)):
                        if i==self.pkg[j][0]:
                            try :
                                self.installDir = self.toolDir + self.pkg[j][0]
                                if not (i in ("crips", "arachni", "openssl", "revsh")):
                                    os.system("git clone %s %s" % (self.pkg[j][1], self.installDir))
                                else :
                                    if i == "crips":
                                        os.system("git clone %s %s" % (self.pkg[j][1], self.installDir))
                                        os.system("sudo chmod +x %s/install.sh" % (self.installDir))
                                        os.system("sudo %s/./install.sh" % (self.installDir))  
                                    elif i == "arachni":
                                        os.system("git clone %s %s" % (self.pkg[j][1], self.installDir))
                                        os.system("cd %s/ && bundle install" % (self.installDir)) 
                                    elif i == "openssl":
                                        os.system("git clone %s %s" %(self.pkg[j][1], self.installDir))
                                        os.system("cd %s/ && ./config no-shared -static && make && make test && sudo make install" % self.installDir)
                                    elif i == "revsh":
                                        os.system("git clone %s %s" %(self.pkg[j][1], self.installDir))
                                        os.system("cd %s/ && make && make install" % (self.installDir))
                            except os.isdir(self.toolDir + self.pkg[j][0]):
                                print(color.NOTICE + "[!] - Already installed" + color.WHITE)

        if show == 1:
            print("\033[32m" + "Packages\n" + "\033[93m")
            for i in range(0,len(self.pkg),2):
                if i<len(self.pkg)-1:
                    print("%-15s" "%s" % (self.pkg[i][0], self.pkg[i+1][0]))
                else:
                    print("%s" % (self.pkg[i][0]))
                
            print("\033[32m" + "\nScripts\n" + "\033[93m")
            for i in range(len(self.scripts)):
                print("%s" % self.scripts[i][0])
            print("\033[97m")    

    def completed(self):
        input(color.LOGGING + "[*] - Installation completed, press [return] to go back" + color.WHITE)


    def aborted(self):
        input(color.LOGGING + "[*] - Installation canceled, press [return] to go back" + color.WHITE)


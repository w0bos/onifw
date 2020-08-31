#!/usr/bin/python

import os
import socket

from core.errorHandler import ErrorHandler
from sys import exc_info as err
from os import makedirs as mkdir
from os import path, chdir, getcwd
from os import system as shell
from core.gui import color
from requests import get
from getpass import getuser
from time import gmtime, strftime
from subprocess import check_output
from socket import gethostname, gethostbyname

def clearScr():
    shell('cls||clear')


alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"

installDir = os.path.dirname(os.path.abspath(__file__)) + '/../'
toolDir = installDir + 'tools/'


### CLASS ###
class microsploit:
    def __init__(self):
        self.installDir = toolDir + "microsploit"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        shell("bash %s/Microsploit" % (self.installDir))

class poet:
    def __init__(self):
        self.installDir = toolDir + "poet"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        shell("python2 %s/server.py" % (self.installDir))

class weeman:
    def __init__(self):
        self.installDir = toolDir + "weeman"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        shell("cd %s/ && python2 weeman.py" % (self.installDir))

class sb0x:
    def __init__(self):
        self.installDir = toolDir + "sb0x"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))


    def run(self):
        shell("cd %s/ && python2 %s/sb0x.py" % (self.installDir, self.installDir))

class nxcrypt:
    def __init__(self):
        self.installDir = toolDir + "nxcrypt"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))


    def run(self):
        shell("sudo python2 %s/NXcrypt.py --help" % (self.installDir))

class revsh:
    def __init__(self):
        self.installDir = toolDir + "revsh"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))


    def run(self):
        shell("chmod +x %s/revsh.c" % self.installDir)
        shell("cd %s/ && %s/revsh" % (self.installDir, self.installDir))

class nmap:
    def __init__(self, installDir):
        self.installDir = toolDir + "nmap"
        self.normalDir = installDir
        self.targetPrompt = color.LOGGING + "nmap >  " + color.WHITE

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")

        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))

    def run(self):
        print("[?] - Enter target IP/Subnet/Range/Host")
        target = input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        print("   Nmap scan for: %s\n" % target)
        print("   1 - Ping scan         [-sP]")
        print("   2 - Syn scan          [-sS]")
        print("   3 - UDP scan          [-sU]")
        print("   4 - Version detection [-sV]")
        print("   5 - OS detection      [-O]")
        print("   6 - Aggressive scan   [-A]")
        print("   7 - Scan for vulns    [--script vuln]")
        print("   c - Custom")
        print("   99 - Return \n")
        response = input(color.LOGGING + "nmap > " + color.WHITE)
        clearScr()
        logPath = "{}logs/nmap-".format(self.normalDir) + strftime("%H:%M:%S", gmtime())
        try:
            if response == "1":
                shell("nmap -sP -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "2":
                shell("nmap -sS -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "3":
                shell("nmap -sU -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "4":
                shell("nmap -sV -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "5":
                shell("sudo nmap -O -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "6":
                shell("nmap -A -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "7":
                shell("nmap --script vuln -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "c":
                flags = input("Which options: ")
                shell("nmap %s -oN %s %s" % (flags, logPath, target))
                response = input(continuePrompt)
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

class xsstrike:
    def __init__(self):
        self.installDir = toolDir + "xsstrike"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
            clearScr()
        else:
            print("[?] - Enter a command: (leave blank if unsure)")
            response = input(color.LOGGING + "xsstrike > " + color.WHITE)
            self.run(response)
        

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self, response):
        if not len(response):
            shell("python3 %s/xsstrike.py -h" % (self.installDir))
        else :
            shell("python3 %s/xsstrike.py %s" % (self.installDir, response))

class doork:
    def __init__(self):
        self.installDir = toolDir + "doork"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
            clearScr()
        else:
            print("[?] - Enter a target")
            target = input(color.LOGGING + "doork > " + color.WHITE)
            self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self, target):
        if not "http://" in target:
            target = "http://" + target
        logPath = "logs/doork-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        try:
            shell("python2 %s/doork.py -t %s -o %s" %
                      (self.installDir, target, logPath))
        except KeyboardInterrupt:
            pass

class crips:
    def __init__(self):
        self.installDir = toolDir + "crips"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")

        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir) or os.path.isdir("/usr/share/doc/Crips"))

    def run(self):
        try:
            shell("python2 %s/crips.py" % self.installDir)
        except:
            pass

class wpscan:
    def __init__(self):
        self.installDir = toolDir + "wpscan"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            print("[?] - Enter a target")
            target = input(color.LOGGING + "wpscan > " + color.WHITE)
            self.menu(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def menu(self, target):
        print("   WPScan for: %s\n" % target)
        print("   1- Username Enumeration [--enumerate u]")
        print("   2 - Plugin Enumeration [--enumerate p]")
        print("   3 - All Enumeration Tools [--enumerate]\n")
        print("   r - Return to information gathering menu \n")
        response = input(color.LOGGING + "wpscan > " + color.WHITE)
        clearScr()
        logPath = "../../logs/wpscan-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        wpscanOptions = "--no-banner --random-agent --url %s" % target
        try:
            if response == "1":
                shell(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate u --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "2":
                shell(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate p --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "3":
                shell(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "r":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

class setoolkit:
    def __init__(self):
        self.installDir = toolDir + "setoolkit"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        print("%ssetoolkit/setoolkit" % toolDir)
        print(os.path.isfile("%s/setoolkit/setoolkit" % (toolDir)))
        return (os.path.isfile("%s/setoolkit/setoolkit" % (toolDir)))

    def run(self):
        shell("sudo %ssetoolkit/setoolkit" % (toolDir))

class apwps:
    def __init__(self):
        self.installDir = toolDir + "apwps"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:   
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        shell("python2 %s/autopixie.py" % self.installDir)

class snmp:
    def __init__(self):
        self.installDir = toolDir + "snmp"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        target = input("Enter Target IP: ")
        shell("python2 %s/snmpbrute.py -t %s" % (self.installDir,target))


class sslstrip:
    def __init__(self):
        self.installDir = toolDir + "sslstrip"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        target = input("[?] - Enter Target IP: ")
        shell("python2 %s/sslstrip.py %s" % (self.installDir, target))

class cupp:
    
    def __init__(self):
        self.installDir = toolDir + "cupp"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        shell("python3 %s/cupp.py -i" % self.installDir)

class brutex:
    def __init__(self):
        self.installDir = toolDir + "brutex"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        print("[?] - Enter target IP")
        target = input(color.LOGGING + "BruteX > " + color.WHITE)
        shell("brutex %s" % target)

class leviathan:
    
    def __init__(self):
        self.installDir = toolDir + "leviathan"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        shell("python2 %s/leviathan.py -i" % self.installDir)

class nikto:
    def __init__(self):
        self.installDir = toolDir + "nikto"
        self.targetPrompt = color.IMPORTANT + "Nikto > " + color.WHITE
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()
    def installed(self):
        return (os.path.isfile("%s/program/nikto.pl" % self.installDir))

    def run(self):
        print("[?] - Enter Target IP/Subnet/Range/Host")
        target = input(self.targetPrompt)
        self.menu(target)
    def menu(self, target):
        shell("perl %s/program/nikto.pl -h %s" % (self.installDir, target))
               
class rscan:
    def __init__(self):
        self.installDir = toolDir + "rapidscan"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            self.targetPrompt = color.LOGGING + "rscan > "  + color.WHITE
            print("[?] - Enter target ip/subnet/range/host")
            target=input(self.targetPrompt)
            self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self, target):
        shell("python2 %s/rapidscan.py %s" % (self.installDir, target))

class arachni:
    def __init__(self):
        self.installDir = toolDir + "arachni"
        if not os.path.isdir(self.installDir):
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            self.run()

    def run(self):
        print("[?] - Enter target")
        target = input(color.LOGGING + "Arachni > " + color.LOGGING)
        shell("sudo arachni %s" %(target))

class sqlmap:
    def __init__(self):
        self.installDir = toolDir + "sqlmap"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else : self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        shell("python2 %s/sqlmap.py --wizard" % (self.installDir))

class slowloris:
    def __init__(self):
        self.installDir = toolDir + "slowloris"
        self.targetPrompt = color.LOGGING + "slowloris > " + color.WHITE
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            print("[?] - Enter Target IP/Subnet/Range/Host: ")
            target = input(self.targetPrompt)
            self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self,target):
        shell("python3 %s/slowloris.py %s" % (self.installDir, target))

class pwnloris:
    def __init__(self):
        self.installDir = toolDir + "pwnloris"
        self.targetPrompt = color.LOGGING + "pwnloris > " + color.WHITE
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            print("[?] - Enter Target IP/Subnet/Range/Host: ")
            target = input(self.targetPrompt)
            self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self,target):
        shell("python3 %s/pwnloris.py %s" % (self.installDir, target))

class atscan:
    def __init__(self):
        self.installDir = toolDir + "atscan"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        shell("perl %s/atscan.pl --interactive" % (self.installDir))

class hyde:
    def __init__(self):
        self.installDir = toolDir + "hyde"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        shell("python3 %s/hyde/main.py" % (self.installDir))




"""

CUSTOM

"""


# Default 

class ipfind:
    def __init__(self):
        print("[?] - Enter URL")
        host = input(color.NOTICE +
                     "onifw/IPfinder > "+ color.WHITE)
        ip = socket.gethostbyname(host)
        print("[*] - The IP of %s is: %s" % (host, ip))

class hashcheck:
    def __init__(self,logDir):
        filepath=input(color.LOGGING+"[?] - Enter path of file: ")
        print("Hash checker")
        print("1 - MD5")
        print("2 - sha1")
        print("3 - sha224")
        print("4 - sha256")
        print("99 - exit")
        hashtype = input(color.NOTICE + "onifw/hashcheck > " + color.END)
        if hashtype=="1":
            shell("md5sum {}".format(filepath))
        elif hashtype == "2":
            shell("sha1sum {}".format(filepath))
        elif hashtype=="3":
            shell("sha224sum {}".format(filepath))
        elif hashtype == "4":
            shell("sha256sum {}".format(filepath))

class servicestatus:
    def __init__(self,logDir):
        self.logDir=logDir
        if not path.isdir(self.logDir):mkdir(self.logDir)  # Make folder
        print(color.LOGGING)
        shell("ps -ef > {}/services.out".format(self.logDir))
        print(color.END + color.NOTICE + "[*] - Log saved in the .onifw/src/logs/ dir" + color.END)


class firewall:
    def __init__(self,logDir):
        self.logDir = logDir
        if not path.isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print(color.LOGGING)
        print("FIREWALL SETUP")
        print("1 - Export firewall current setup")
        print("2 - Edit firewall table")
        print("3 - Apply iptable")
        print("99 - exit")
        print(color.END)
        choice = input(color.NOTICE + "onifw/firewallconfig > " + color.END)
        if choice == "1":
            shell("iptables-save > {}/firewall.out".format(self.logDir))
        elif choice == "2":
            shell("iptables-save > {}/firewall.out".format(self.logDir))
            shell("vi {}/firewall.out".format(logDir))
        if choice == "3":
            shell("iptables-restore < {}/firewall.out".format(self.logDir))


class viewtraffic:
    def __init__(self,logDir):
        self.logDir = logDir
        if not path.isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print("TRAFFIC ANALYSIS")
        print("1 - Tcpdump")
        print("2 - Tshark")
        choice = input(color.NOTICE + "onifw/trafficanalyzer> " + color.END)
        if choice == "1":
            shell("sudo tcpdump -A -vv > {}/tcpdump.out".format(self.logDir))
        elif choice == "2":
            shell("sudo tcpdump -w {}/tshark.pcap".format(self.logDir))


class networkmanaged:
    def __init__(self,logDir):
        self.logDir = logDir
        if not path.isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print("wireless monitoring")
        print("1 - Enable monitoring mode")
        print("2 - Disable monitoring mode")
        print("99 - Exit ")
        ans = input(color.NOTICE+"onifw/netmanager > "+color.END)
        if ans == "1":
            inter_name = input("interface name: ")
            try:
                shell("sudo iwconfig {} down".format(inter_name))
                shell("sudo iwconfig {} mode monitor".format(inter_name))
                shell("sudo iwconfig {} up".format(inter_name))
            except:
                print(
                    color.IMPORTANT+"[!] - An error occurred, check if iwconfig is installed and the name of the interface"+color.END)
        elif ans == "2":
            inter_name = input("interface name: ")
            try:
                shell("sudo iwconfig {} down".format(inter_name))
                shell("sudo iwconfig {} mode managed".format(inter_name))
                shell("sudo iwconfig {} up".format(inter_name))
            except:
               ErrorHandler(err(),False) 


class onimap:
    def __init__(self,installDir,logDir):
        self.logDir = logDir
        self.installDir = installDir
        print("[?] - Which target to scan")
        target = input(color.NOTICE + "onifw/onimap > " + color.END)
        shell("python3 {0}core/onimap.py {1}".format(self.installDir,target))


class onibuster:
    def __init__(self, installDir, logDir):
        self.logDir = logDir
        self.installDir = installDir
        print("[?] - Set target")
        rhost = input("target > ")
        print("[?] - Set port (default:80)")
        port = input("port > ")
        if len(port) < 1:
            port = 80
        print("[?] - Which dictionnary file to use")
        dictf = input("dictionnary > ")
        shell("python3 {0}/core/onibuster.py {1} {2} {3}".format(installDir, rhost, port, dictf))

class bg:
    def __init__(self):
       sh = check_output("echo $SHELL", shell=True).decode("utf-8").rstrip("\r\n")
       shell("python -c 'from pty import spawn; spawn(\"%s\")'" % sh)

class run_shell:
    def __init__(self):
        print(color.LOGGING+"[*] - Opening shell prompt")
        shell_cmd=input(color.NOTICE+"shell$ "+color.END)
        shell(shell_cmd)

class myip:
    def __init__(self):
        print(color.NOTICE + "Local IP: {}".format(gethostbyname(gethostname())))
        print("Remote IP: {}".format(get("https://api.ipify.org").text) + color.END)

class cd:
    def __init__(self, cmd):
        flag = True
        if len(cmd) > 1:
            value = cmd[1]
            if cmd[1][0] == "$":
                value = check_output("echo {}".format(cmd[1]), shell=True).decode("utf-8").strip('\n')
                flag = False
            try:
                print(color.OKBLUE+"[+] - Changing current directory...")
                if flag:
                    chdir("/home/{}".format(getuser()) + "/" + value)
                else:
                    chdir(value)
                print(color.LOGGING+"[*] - Current directory: " +
                      color.NOTICE + getcwd() + color.END)
            except:
                ErrorHandler(err(), False)

class checkout:
    def __init__(self, cmd, installDir):
        if len(cmd) > 1:
            if cmd[1] == "dev":
                ans = input(
                    "[!] - Switching to the dev branch might break onifw.\n[?] - Continue? [y/N]: ")
                if ans.lower() in ["y", "yes"]:
                    shell("cd {} && git checkout dev".format(installDir))
                    print(
                        "[*] - Done.\n[*] - Restart onifw for changes to take effect")
            if cmd[1] == "master":
                ans = input(
                    "[!] - Switching to the master branch might break onifw.\n[?] - Continue? [y/N]: ")
                if ans.lower() in ["y", "yes"]:
                    shell("cd {} && git checkout master".format(installDir))
                    print(
                        "[*] - Done.\n[*] - Restart onifw for changes to take effect")
        else:
            print("[!] - No branch provided :: Usage: git checkout [branch]")
            print("[!] - Branches available : master / dev")


class status:
    def __init__(self, installDir):
        curr_branch = check_output("cd {} && git branch --show-current".format(
            installDir), shell=True).decode("utf-8").strip('\n')
        version = ""
        with open("{}data/version.txt".format(installDir)) as f:
            version = color.NOTICE + \
                f.readlines()[0].rstrip("\n\r") + color.END
        f.close()
        latest_version = check_output(
            "curl -s https://raw.githubusercontent.com/w0bos/onifw/master/src/data/version.txt", shell=True).decode("utf-8").strip('\n')
        header = color.NOTICE + "[+]" + color.HEADER
        print(header + " - onifw {0}{1}{2} on {3}{4}{5} branch".format(
            color.NOTICE, version, color.HEADER, color.IMPORTANT, curr_branch, color.HEADER))
        print(header + " - Latest version : {0}{1}".format(color.OKBLUE,latest_version))
        print(header + " - Installation location: {}".format(installDir)+color.END)
        if curr_branch == "dev":
            print(header + " - Status : "+color.BOLD +color.RED+"unstable"+color.END)

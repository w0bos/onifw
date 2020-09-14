#!/usr/bin/python


from os import system, chdir, getcwd
from os.path import isdir, dirname, abspath
from os import makedirs as mkdir
from core.gui import color
from subprocess import check_output
from socket import gethostbyname, gethostname
from requests.api import get
from getpass import getuser
from sys import exc_info as err
from time import gmtime, strftime
from core.errorHandler import ErrorHandler
from core.onilib import clearScr


installDir = dirname(abspath(__file__)) + '/../'
toolDir = installDir + 'tools/'
continuePrompt = "\nClick [Return] to continue"


extensions = {
    "python":   ".py",
    "ruby":     ".rb",
    "shell":    ".sh",
    "perl":     ".pl",
    "bash":     ""
}

class toolmanager:
    def __init__(self, tool_name, lang="", need_args=False, change_dir=False, exe_name="", pre_cmd="", post_cmd="", sudo=False):
        self.tool_name = tool_name
        self.lang = lang
        self.installDir = toolDir + self.tool_name
        self.prefix = self.lang
        self.arg=""
        if not isdir(self.installDir):
            print(color.IMPORTANT +
                  "[!] - Tool not installed or not located in the tool/ directory" +
                  color.END)
            return
        for i in extensions:
            if i in self.lang:
                self.extension = extensions[i]     
        if need_args:
            print(color.LOGGING +
                  "[?] - Please specify a target" + color.END)
            self.arg = str(
                input(color.HEADER + "onifw[{}]: ".format(self.tool_name) + color.END))
        if len(pre_cmd) > 1:
            self.extension += " " + pre_cmd
        if len(post_cmd) > 1:
            self.arg += " " + post_cmd
        if len(exe_name) > 1:
            self.exe_name = exe_name
        else:
            self.exe_name = self.tool_name
        if sudo:
            self.prefix = "sudo " + self.prefix
        self.cmd = "{0} {1}/{2}{3}".format(self.prefix, self.installDir, self.exe_name, self.extension)
        if change_dir:
            self.cmd = "cd {0} && {1}".format(self.installDir, self.cmd)
        if not len(self.arg)<1:
            self.cmd += " " + self.arg
        try:
            system(self.cmd)
        except:
            ErrorHandler(err(), False)



class doork:
    def __init__(self):
        self.installDir = toolDir + "doork"

        if not self.installed():
            print(
                "[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
            clearScr()
        else:
            print("[?] - Enter a target")
            target = input(color.LOGGING + "doork > " + color.WHITE)
            self.run(target)

    def installed(self):
        return (isdir(self.installDir))

    def run(self, target):
        if not "http://" in target:
            target = "http://" + target
        logPath = "logs/doork-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        try:
            system("python2 %s/doork.py -t %s -o %s" %
                  (self.installDir, target, logPath))
        except KeyboardInterrupt:
            pass

class nxcrypt:
    def __init__(self):
        self.installDir = toolDir + "nxcrypt"
        if not self.installed():
            print(
                "[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (isdir(self.installDir))

    def run(self):
        system("sudo python2 %s/NXcrypt.py --help" % (self.installDir))


class revsh:
    def __init__(self):
        self.installDir = toolDir + "revsh"
        if not self.installed():
            print("[*] - Tool not installed.")
            print("[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (isdir(self.installDir))

    def run(self):
        system("chmod +x %s/revsh.c" % self.installDir)
        system("cd %s/ && %s/revsh" % (self.installDir, self.installDir))


class brutex:
    def __init__(self):
        self.installDir = toolDir + "brutex"

        if not self.installed():
            print(
                "[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (isdir(self.installDir))

    def run(self):
        print("[?] - Enter target IP")
        target = input(color.LOGGING + "BruteX > " + color.WHITE)
        system("brutex %s" % target)




# CUSTOM #


class arachni:
    def __init__(self):
        self.installDir = toolDir + "arachni"
        if not isdir(self.installDir):
            print(
                "[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            self.run()

    def run(self):
        print("[?] - Enter target")
        target = input(color.LOGGING + "Arachni > " + color.LOGGING)
        system("sudo arachni %s" % (target))

class setoolkit:
    def __init__(self):
        self.installDir = toolDir + "setoolkit"

        system("cd %s/ && sudo ./setoolkit" % (self.installDir))

class sqlmap:
    def __init__(self):
        self.installDir = toolDir + "sqlmap"
        system("python2 %s/sqlmap.py --wizard" % (self.installDir))

class atscan:
    def __init__(self):
        self.installDir = toolDir + "atscan"
        system("perl %s/atscan.pl --interactive" % (self.installDir))

class nmap:
    def __init__(self):
        self.installDir = toolDir + "nmap"
        self.normalDir = installDir
        self.targetPrompt = color.LOGGING + "nmap >  " + color.WHITE
        clearScr()
        self.run()

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
        logPath = "{}logs/nmap-".format(self.normalDir) + \
            strftime("%H:%M:%S", gmtime())
        try:
            if response == "1":
                system("nmap -sP -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "2":
                system("nmap -sS -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "3":
                system("nmap -sU -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "4":
                system("nmap -sV -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "5":
                system("sudo nmap -O -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "6":
                system("nmap -A -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "7":
                system("nmap --script vuln -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "c":
                flags = input("Which options: ")
                system("nmap %s -oN %s %s" % (flags, logPath, target))
                response = input(continuePrompt)
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

class wpscan:
    def __init__(self):
        self.installDir = toolDir + "wpscan"
        print("[?] - Enter a target")
        target = input(color.LOGGING + "wpscan > " + color.WHITE)
        self.menu(target)

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
                system(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate u --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "2":
                system(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate p --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "3":
                system(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)


##########################
#        CUSTOM          #
##########################


class ipfind:
    def __init__(self):
        print("[?] - Enter URL")
        host = input(color.NOTICE +
                     "onifw/IPfinder > " + color.WHITE)
        ip = gethostbyname(host)
        print("[*] - The IP of %s is: %s" % (host, ip))

class hashcheck:
    def __init__(self, logDir):
        filepath = input(color.LOGGING+"[?] - Enter path of file: ")
        print("Hash checker")
        print("1 - MD5")
        print("2 - sha1")
        print("3 - sha224")
        print("4 - sha256")
        print("99 - exit")
        hashtype = input(color.NOTICE + "onifw/hashcheck > " + color.END)
        if hashtype == "1":
            system("md5sum {}".format(filepath))
        elif hashtype == "2":
            system("sha1sum {}".format(filepath))
        elif hashtype == "3":
            system("sha224sum {}".format(filepath))
        elif hashtype == "4":
            system("sha256sum {}".format(filepath))

class servicestatus:
    def __init__(self, logDir):
        self.logDir = logDir
        if not isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print(color.LOGGING)
        system("ps -ef > {}/services.out".format(self.logDir))
        print(color.END + color.NOTICE +
              "[*] - Log saved in the .onifw/src/logs/ dir" + color.END)

class firewall:
    def __init__(self, logDir):
        self.logDir = logDir
        if not isdir(self.logDir):
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
            system("iptables-save > {}/firewall.out".format(self.logDir))
        elif choice == "2":
            system("iptables-save > {}/firewall.out".format(self.logDir))
            system("vi {}/firewall.out".format(logDir))
        if choice == "3":
            system("iptables-restore < {}/firewall.out".format(self.logDir))

class viewtraffic:
    def __init__(self, logDir):
        self.logDir = logDir
        if not isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print("TRAFFIC ANALYSIS")
        print("1 - Tcpdump")
        print("2 - Tshark")
        choice = input(color.NOTICE + "onifw/trafficanalyzer> " + color.END)
        if choice == "1":
            system("sudo tcpdump -A -vv > {}/tcpdump.out".format(self.logDir))
        elif choice == "2":
            system("sudo tcpdump -w {}/tshark.pcap".format(self.logDir))

class networkmanaged:
    def __init__(self, logDir):
        self.logDir = logDir
        if not isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print("wireless monitoring")
        print("1 - Enable monitoring mode")
        print("2 - Disable monitoring mode")
        print("99 - Exit ")
        ans = input(color.NOTICE+"onifw/netmanager > "+color.END)
        if ans == "1":
            inter_name = input("interface name: ")
            try:
                system("sudo iwconfig {} down".format(inter_name))
                system("sudo iwconfig {} mode monitor".format(inter_name))
                system("sudo iwconfig {} up".format(inter_name))
            except:
                print(
                    color.IMPORTANT+"[!] - An error occurred, check if iwconfig is installed and the name of the interface"+color.END)
        elif ans == "2":
            inter_name = input("interface name: ")
            try:
                system("sudo iwconfig {} down".format(inter_name))
                system("sudo iwconfig {} mode managed".format(inter_name))
                system("sudo iwconfig {} up".format(inter_name))
            except:
                print(
                    color.IMPORTANT+"[!] - An error occurred, check if iwconfig is installed and the name of the interface"+color.END)

class onimap:
    def __init__(self, installDir, logDir):
        self.logDir = logDir
        self.installDir = installDir
        print("[?] - Which target to scan")
        target = input(color.NOTICE + "onifw/onimap > " + color.END)
        system("python3 {0}core/onimap.py {1}".format(self.installDir, target))

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
        system(
            "python3 {0}/core/onibuster.py {1} {2} {3}".format(installDir, rhost, port, dictf))

class bg:
    def __init__(self):
       sh = check_output("echo $SHELL", shell=True).decode(
           "utf-8").rstrip("\r\n")
       system("python -c 'from pty import spawn; spawn(\"%s\")'" % sh)

class run_shell:
    def __init__(self):
        print(color.LOGGING+"[*] - Opening system prompt")
        system_cmd = input(color.OKBLUE+"shell$ "+color.END)
        system(system_cmd)

class myip:
    def __init__(self):
        print(color.NOTICE + "Local IP: {}".format(gethostbyname(gethostname())))
        print("Remote IP: {}".format(
            get("https://api.ipify.org").text) + color.END)

class cd:
    def __init__(self, cmd):
        flag = True
        if len(cmd) > 1:
            value = cmd[1]
            if cmd[1][0] == "$":
                value = check_output("echo {}".format(
                    cmd[1]), shell=True).decode("utf-8").strip('\n')
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
                print("[!] - And unexpected error occurred")

class checkout:
    def __init__(self, cmd, installDir):
        if len(cmd) > 1:
            if cmd[1] == "dev":
                ans = input(
                    "[!] - Switching to the dev branch might break onifw.\n[?] - Continue? [y/N]: ")
                if ans.lower() in ["y", "yes"]:
                    system("cd {} && git checkout dev".format(installDir))
                    print(
                        "[*] - Done.\n[*] - Restart onifw for changes to take effect")
            if cmd[1] == "master":
                ans = input(
                    "[!] - Switching to the master branch might break onifw.\n[?] - Continue? [y/N]: ")
                if ans.lower() in ["y", "yes"]:
                    system("cd {} && git checkout master".format(installDir))
                    print(
                        "[*] - Done.\n[*] - Restart onifw for changes to take effect")
        else:
            print("[!] - No branch provided :: Usage: git checkout [branch]")
            print("[!] - Branches available : master / dev")

class status:
    def __init__(self, installDir):
        curr_branch = check_output("cd {} && git branch --show-current".format(installDir), shell=True).decode("utf-8").strip('\n')
        version = ""
        with open("{}data/version.txt".format(installDir)) as f:
            version = f.readlines()[0].rstrip("\n\r")
        f.close()
        if curr_branch == "dev":
            print(color.NOTICE + "[+]" + color.HEADER +
                  " - onifw {0} on {1} branch".format(version, curr_branch) + color.END)
            print(color.NOTICE + "[+]" + color.HEADER +
                  " - Installation location: {}".format(installDir) + color.END)

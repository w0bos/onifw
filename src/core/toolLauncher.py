#!/usr/bin/python


from os import system, path, chdir, getcwd
from os import makedirs as mkdir

from core.gui import color
from subprocess import check_output
from socket import gethostbyname, gethostname
from requests.api import get
from getpass import getuser

def clearScr():
    system("cls||clear")

installDir = path.dirname(path.abspath(__file__)) + '/../'
toolDir = installDir + 'tools/'



class toolmanager:
    def __init__(self, cmd=[]):
        pass

##########################
#        CUSTOM
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
        if not path.isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print(color.LOGGING)
        system("ps -ef > {}/services.out".format(self.logDir))
        print(color.END + color.NOTICE +
              "[*] - Log saved in the .onifw/src/logs/ dir" + color.END)


class firewall:
    def __init__(self, logDir):
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
            system("iptables-save > {}/firewall.out".format(self.logDir))
        elif choice == "2":
            system("iptables-save > {}/firewall.out".format(self.logDir))
            system("vi {}/firewall.out".format(logDir))
        if choice == "3":
            system("iptables-restore < {}/firewall.out".format(self.logDir))


class viewtraffic:
    def __init__(self, logDir):
        self.logDir = logDir
        if not path.isdir(self.logDir):
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
       sh = check_output("echo $system", system=True).decode(
           "utf-8").rstrip("\r\n")
       system("python -c 'from pty import spawn; spawn(\"%s\")'" % sh)


class run_system:
    def __init__(self):
        print(color.LOGGING+"[*] - Opening system prompt")
        system_cmd = input(color.NOTICE+"system$ "+color.END)
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
                    cmd[1]), system=True).decode("utf-8").strip('\n')
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
        curr_branch = check_output("cd {} && git branch --show-current".format(
            installDir), system=True).decode("utf-8").strip('\n')
        version = ""
        with open("{}data/version.txt".format(installDir)) as f:
            version = f.readlines()[0].rstrip("\n\r")
        f.close()
        if curr_branch == "dev":
            print(color.NOTICE + "[+]" + color.HEADER +
                  " - onifw {0} on {1} branch".format(version, curr_branch) + color.END)
            print(color.NOTICE + "[+]" + color.HEADER +
                  " - Installation location: {}".format(installDir) + color.END)

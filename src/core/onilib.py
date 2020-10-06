from os import system, getpid
from subprocess import PIPE, check_output, run
from socket import create_connection
from configparser import ConfigParser
from core.gui import color


"""
COMMON FUNCTIONS
"""
def clearScr():
    """
    clear the terminal
    """
    system("cls||clear")


def readfile(file_dir):
    """
    Returns the content of a file in an array.
    \nArguments:\n
    file_dir : Required (str)
    """
    f = open(file_dir)
    content = [line.rstrip('\n') for line in f]
    return content




"""
ONI.PY FUNCTIONS
"""

def pkgmgrhelp():
    """
    Displays the help message of the
    package manager
    """
    print(color.NOTICE + "[*] - Usage : pkg [cmd] [package]\n")
    print("Multiple packages can be installed at once.")
    print("Use the [list] commad to see what packages are available")
    print("Flags:")
    print("-a --all             install all packages")
    print("-i --install         install named package")
    print("-r --remove          remove package")
    print("-da --delete-all     removes all installed packages")
    print("-f --force           forces the removal (when installed in sudo)")
    print("-c --custom          add custom package")
    print(color.WHITE)


def loadtools(toolDir):
    """
    Returns an array of elements in the toolDir
    directory.
    \nArguments:\n
    toolDir : Required (str)
    """
    load_cmd = ['ls', '{}'.format(toolDir)]
    output = run(load_cmd, stdout=PIPE, check=True).stdout.decode('utf-8')
    pkg_local = output.splitlines()
    return pkg_local

def del_cache(installDir):
    """
    Remove __pycache__/ folders of onifw.
    If leave==True then it will exit the framework
    \nArguments:\n
    installDir : Required (str)
    """
    system("rm -rf {}core/__pycache__".format(installDir))
    system("rm -rf {}__pycache__".format(installDir))


"""
CONFIGHANDLER.PY FUNCTIONS
"""


def get_connection():
    """
    Returns True if it can connect to 
    google.com
    """
    try:
        create_connection(("www.google.com", 80))
        isconnected = True
    except:
        isconnected = False
    return isconnected


def check_value(installDir, value, default, boolean=True):
    """
    Check the value of a given item and compare it to
    the value stored in the configfile
    \nArguments:\n
    installDir    : Required (str)
    value         : Required (str)
    default       : Required (str)
    boolean       : Optional (bool)
    """
    configFile = installDir + "onirc"
    parser = ConfigParser()
    parser.read(configFile)
    if boolean:
        if parser.has_option('config', value):
            return parser.getboolean('config', value)
        else:
            return default
    else:
        if parser.has_option('config', value):
            return parser.get('config', value)
        else:
            return default


def check_prompt(installDir):
    """
    Check the value of th prompt and handles it\n
    \nArguments:\n
    installDir : Required (str)
    """
    configFile = installDir + "onirc"
    parser = ConfigParser()
    parser.read(configFile)
    if parser.has_option('config', 'prompt'):
        return str(parser.get('config', 'prompt'))+" "
    else:
        return "onifw > "

"""
Updater functions
"""


def check_branch(installDir):
    """
    Checks the name of the current branch
    \nArguments:\n
    installDir : Required (str)
    """
    curr_branch = check_output("cd {} && git branch --show-current".format(
        installDir), shell=True).decode("utf-8").strip('\n')
    if curr_branch == "dev":
        print(
            color.HEADER + "[!] - Currently working on the dev branch. Updates can only be done while in the master branch")
        print(
            "[!] - Use the checkout command to switch to the master branch"+color.END)
        return True




"""
PACMAN FUNCTIONS
"""

def abort():
    """
    Displays the install cancel message
    """
    input(color.LOGGING +
          "[*] - Installation canceled, press [return] to go back" + color.WHITE)


def uninstall(installDir, cmd, root=0):
    """
    Uninstall a package
    \nArguments:\n
    installDir  : Required (str)
    cmd         : Required (Array(str))
    root        : Optional (int)
    """
    print("[*] - Removing folder")
    if root == 0:
        for i in cmd:
            system("rm -rf {0}tools/{1}".format(installDir, i))
    else:
        for i in cmd:
            system("sudo rm -rf {0}tools/{1}".format(installDir, i))
    print(color.LOGGING+"[*] - Cleaning dictionnary..."+color.END)
    f = open("{}data/dict.txt".format(installDir))
    out = []
    for line in f:
        for i in cmd:
            if not i in line:
                out.append(line)
    f.close()
    f = open("{}data/dict.txt".format(installDir), 'w')
    f.writelines(out)
    f.close()


def remove_all(installDir, root=1):
    """
    Delete all installed packages
    \nArguments:\n
    installDir  : Required (str)
    root        : Optional (int)
    """
    toolDir = installDir + 'tools/'
    # To avoid errors
    if root == 1:
        system("sudo rm -rf {}*".format(toolDir))
    else:
        system("rm -rf {}*".format(toolDir))

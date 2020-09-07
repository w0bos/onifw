from os import system
from subprocess import PIPE, run
from socket import create_connection
from configparser import ConfigParser



"""
COMMON FUNCTIONS
"""
def clearScr():
    """
    clearscreen
    """
    system("cls||clear")


def readfile(file_dir):
    """ readfile(file_dir:str)

    Returns the content of a file in an array.
    """
    f = open(file_dir)
    content = [line.rstrip('\n') for line in f]
    return content

"""
ONI.PY FUNCTIONS
"""

def loadtools(toolDir):
    """loadtools(toolDir:str)

        Returns an array of elements in the toolDir
        directory.
    """
    load_cmd = ['ls', '{}'.format(toolDir)]
    output = run(load_cmd, stdout=PIPE).stdout.decode('utf-8')
    pkg_local = output.splitlines()
    return pkg_local

def del_cache(installDir):
    """delete_cache(installDir, leave=False)

    Remove __pycache__/ folders of onifw.
    If leave==True then it will exit the framework
    """
    system("rm -rf {}core/__pycache__".format(installDir))
    system("rm -rf {}__pycache__".format(installDir))


"""
CONFIGHANDLER.PY FUNCTIONS  
"""


def get_connection():
    """get_connection()

    Returns a boolean. True if it can connect to 
    google.com
    """
    try:
        create_connection(("www.google.com", 80))
        isconnected = True
    except:
        isconnected = False
    return isconnected


def check_value(installDir, value, default, boolean=True):
    """check_value(installDir, value, default, boolean=True)

    Check the value of a given item and compare it to
    the value stored in the configfile
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
    """check_prompt(installDir)

    Check the value of th prompt and handles it
    """
    configFile = installDir + "onirc"
    parser = ConfigParser()
    parser.read(configFile)
    if parser.has_option('config', 'prompt'):
        return str(parser.get('config', 'prompt'))+" "
    else:
        return "onifw > "


#!/usr/bin/env python

from core.gui import color
from sys import exc_info as err
from core.errorHandler import ErrorHandler
from core.onilib import return_colored_prefix

def addWords(installDir, wordList):
    """
    Add words to dictionnary file
    \nArguments:\n
    installDir  : Required (str)
    wordList    : Required Array(str)
    """
    print(return_colored_prefix("*") + "- Adding dictionnary words...")
    try:
        with open("{}data/dict.txt".format(installDir), "a") as f:
            for i in range(len(wordList)):
                f.write(wordList[i] + "\n")
        f.close()
        print(return_colored_prefix("*") + "- Done.")
    except:
        ErrorHandler(err(), False)


def restoreDict(installDir):
    """
    Restore default dictionnary file
    \nArguments:\n
    installDir  : Required (str)
    """
    print(return_colored_prefix("*") + "- Restoring dictionnary to default...")
    try:
        f = open("{}data/dict.txt".format(installDir))
        out = []
        default = False
        for line in f:
            temp = str(line).rstrip('\n\r')
            if temp == "update":
                default = True
                out.append(temp)
            if default == False:
                out.append(line)
        f.close()

        f = open("{}data/dict.txt".format(installDir), 'w')
        out.append("\n")
        f.writelines(out)
        f.close()
    except:
        ErrorHandler(err(), False)


def updateConfig(installDir, name, command):
    """
    Add launch command to the onirc file
    \nArguments:\n
    installDir  : Required (str)
    name        : Required (str)
    command     : Required (str)
    """
    print(return_colored_prefix("*") + "- Updating configuration...")
    try:
        with open("{}onirc".format(installDir), "a") as f:
            f.write("{0} = {1}\n".format(name, command))
        f.close()
        print(return_colored_prefix("*") + "- Done.")
    except:
        print(color.LOGGING + "[!] - Unexpected error: ")
        ErrorHandler(err(), False)
    
def addCustomWords(installDir, name):
    """
    Add words to the custom dictionnary
    Arguments:
    name        : Required (str)
    installDir  : Required (str)
    """
    print(return_colored_prefix("*") + "- Adding custom words...")
    try:
        with open("{}data/ctools.txt".format(installDir), "a") as f:
            f.write(name + "\n")
        f.close()
        print(return_colored_prefix("*") + "- Done.")
    except:
        ErrorHandler(err(), False)

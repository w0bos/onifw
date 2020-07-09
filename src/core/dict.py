#!/usr/bin/env python

from core.gui import color
from sys import exc_info as einfo




def addWords(installDir,wordList):
    """Add words to dictionnary file
    
    Arguments:
        - wordList : Array of strings containing words to add
    """
    print("[*] - Adding dictionnary words...")
    try:
        with open("{}data/dict.txt".format(installDir), "a") as f:
            for i in range(len(wordList)):
                f.write(wordList[i] + "\n")
        f.close()
        print("[*] - Done.")
    except:
        print(color.LOGGING + "[!] - Unexpected error: ", einfo()[0])


def restoreDict(installDir):
    """Restore default dictionnary file
    """
    print("[*] - Restoring dictionnary to default...")
    print(installDir)
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
        print(color.LOGGING + "[!] - Unexpected error: ", einfo()[0])

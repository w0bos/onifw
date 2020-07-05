#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import readline
import configparser
import subprocess
import random

# From
from os import system as cmd
from os import path as path
from os import makedirs as mkdir
from sys import exit as abort

#File loading
import core.completer as auto
import core.installer as instl
import core.custom    as custom
import core.launcher  as launch
import core.updater   as update
import setup          as setup
from   core.loading   import thread_loading
from   core.gui       import color as color

# Data
installDir = path.dirname(path.abspath(__file__)) + '/'
toolDir = installDir + 'tools/'
onifw_cmd = "onifw > "
with open("{}/api/version.txt".format(installDir)) as f:
    version = f.readlines()[0].rstrip("\n\r")
f.close()


# Configuration files
configFile = installDir + "./core/config.cfg"
config = configparser.ConfigParser()
config.read(configFile)

# Misc functions
def clearScr():
    cmd("cls||clear")


def readfile(file_dir):
    f = open(file_dir)
    content = [line.rstrip('\n') for line in f]
    return content


def del_cache(leave=0):
    cmd("rm -rf {}core/__pycache__".format(installDir))
    cmd("rm -rf {}./__pycache__".format(installDir))
    if leave == 1:
        abort(1)


def pkgmgrhelp():
    print(color.NOTICE)
    print("[*] - Usage : pkg [cmd] [package]")
    print("      Multiple packages can be installed at once.")
    print("      Use the [list] commad to see what packages are available")
    print("      Flags:")
    print("      -a --all        install all packages")
    print("      -i --install    install named package")
    print("      -r --remove     remove package")
    print("      -f --force      forces the removal (when installed in sudo)")
    print("      -c --custom     add custom package")
    print(color.WHITE)

# Class
class main:

    def __init__(self):
        #Check is path exists
        if not path.isdir(toolDir): mkdir(toolDir)

        completer = auto.Autocomp(readfile(installDir + "data/dict.txt"))
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        prompt = input(color.color_random[0]+onifw_cmd + color.END)
        # Ask input
        cmd = prompt.split()



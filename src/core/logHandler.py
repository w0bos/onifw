import readline
import subprocess

import core.completer as auto
import core.dict as dictmgr
import core.confighandler as cfghandler

from core.gui import color

class logHandler:
    def __init__(self, installDir, logDir):
        self.logDir = logDir
        self.installDir = installDir

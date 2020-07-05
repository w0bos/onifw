import sys
import os
from os import system as cmd
import readline
import configparser

'''
    Objective:
        - Allow user configuration
        - syntax
                    `edit` [item] [value]

'''


class ConfigHandler:
    def __init__(self,configfile):
        self.config = configfile

    def showBanner(self):
        #Banner 
        pass

    def edit_config(self):
        pass

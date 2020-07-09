import sys
import os
from os import system as cmd
import readline
import configparser




class ConfigHandler:
    def __init__(self,configfile):
        self.config = configfile


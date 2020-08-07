import unittest
import core

from core import confighandler as cfg
from os import path

installDir = path.dirname(path.abspath(__file__)) + '/'

class testConfigHandler(unittest.TestCase):


    def test_show_version(self):
        self.assertFalse(cfg.check_value(installDir,"show_version",False))
        self.assertTrue(cfg.check_value(installDir, "show_version", True))

    def test_check_prompt(self):
        self.assertEqual(cfg.check_prompt(installDir),"onifw > ")


if __name__=="__main__":
    unittest.main()

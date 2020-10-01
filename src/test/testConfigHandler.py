import unittest

from core import confighandler as cfg
from os import path

installDir = path.dirname(path.abspath(__file__)) + '/'

class testConfigHandler(unittest.TestCase):


    def test_show_version(self):
        self.assertFalse(cfg.check_value(installDir,"show_version",False))
        self.assertTrue(cfg.check_value(installDir, "show_version", True))

    @unittest.expectedFailure
    def test_wrong_show_version(self):
        self.assertFalse(cfg.check_value(installDir))

    def test_check_prompt(self):
        self.assertEqual(cfg.check_prompt(installDir), "onifw > ")

    @unittest.expectedFailure
    def test_wrong_check_prompt(self):
        self.assertEqual(cfg.check_prompt(installDir), True)

    # Check values
    def test_check_values(self):
        self.assertFalse(cfg.check_value(installDir, "none", False))
        self.assertTrue(cfg.check_value(installDir, "show_ascii_art", True))

    @unittest.expectedFailure
    def test_wrong_check_values(self):
        self.assertTrue(cfg.check_value(installDir, "none"))

    """
        Check ==> add custom launch script 
    """


if __name__=="__main__":
    unittest.main()

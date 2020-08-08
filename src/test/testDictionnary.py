import unittest
import core.dict as dmgr
from os import path
from time import sleep
installDir = path.dirname(path.abspath(__file__)) + '/../'


class testConfigHandler(unittest.TestCase):

    def test_restore_dict(self):
        default=[]
        restored=[]
        with open("test/default_dict.txt","r") as f:
            for line in f:
                default.append(str(line).rstrip("\n\r"))
        f.close()
        dmgr.restoreDict(installDir)
        with open("data/dict.txt", "r") as f:
            for line in f:
                restored.append(str(line).rstrip("\n\r"))
        f.close()
        self.assertEqual(default,restored)

    def test_add_word(self):
        dmgr.restoreDict(installDir)
        wordlist = ["test"]
        dmgr.addWords(installDir,wordlist)
        default = []
        edited = []
        with open("test/default_dict.txt", "r") as f:
            for line in f:
                default.append(str(line).rstrip("\n\r"))
        f.close()
        default.append("test")
        with open("data/dict.txt", "r") as f:
            for line in f:
                edited.append(str(line).rstrip("\n\r"))
        f.close()
        self.assertEqual(default, edited)





if __name__ == "__main__":
    unittest.main()

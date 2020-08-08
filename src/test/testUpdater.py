import unittest
from core import updater as up
from os import path, system
from subprocess import check_output


installDir = path.dirname(path.abspath(__file__)) + '/../'
toolDir = installDir+"tools/"



class testConfigHandler(unittest.TestCase):


    def test_branch_disabled(self):
        current = check_output("cd {} && git branch --show-current".format(installDir), shell=True).decode("utf-8").strip('\n')
        if current=="dev":
            #self.assertEqual(up.Updater(installDir), "[!] - Currently working on the dev branch. Updates can only be done while in the master branch\n[!] - Use checkout master to switch to the master branch")
            # function returns boolean
            self.assertTrue(up.Updater(installDir))
        else:
            self.assertNotEqual(current,"dev")
    
    


if __name__ == "__main__":
    unittest.main()

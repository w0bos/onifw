import unittest
import core.packagemanager as pacman
import core.dict as dmgr
from os import path, system
from time import sleep
from os import path
installDir = path.dirname(path.abspath(__file__)) + '/../'
toolDir = installDir+"tools/"

def cleanup():
    pacman.remove_all(installDir)
    dmgr.restoreDict(installDir)
    sleep(0.1)

class testConfigHandler(unittest.TestCase):

    # Must find a way to implement this fast
    #def test_install_all(self):
    #    pacman.Install(installDir,[],True)

    def test_install_one(self):
        pacman.Install(installDir, ["rapidscan"])
        cleanup()

    def test_install_two(self):
        pacman.Install(installDir, ["hyde","poet"])
        cleanup()

    def test_install_script(self):
        pacman.Install(installDir, ["smtp"])
        cleanup()

    def test_install_scripts(self):
        pacman.Install(installDir, ["smtp","pypisher"])
        cleanup()
    
    def test_install_script_and_tool(self):
        pacman.Install(installDir, ["rapidscan","smtp"])
        cleanup()

    def test_install_builds_single(self):
        pacman.Install(installDir, ["brutex"])
    
    #def test_install_builds_multiple(self):
    #    pacman.Install(installDir, ["brutex", "nmap"])

    def test_remove_one(self):
        pacman.Install(installDir, ["rapidscan","nikto"])
        pacman.uninstall(installDir, ["rapidscan"])
        testDir = toolDir+"rapidscan"
        localDir = toolDir+"nikto"
        self.assertFalse(path.isdir(testDir))
        self.assertTrue(path.isdir(localDir))
        cleanup()

    def test_remove_all(self):
        pacman.Install(installDir, ["rapidscan", "nikto"])
        pacman.remove_all(installDir,0)
        testDir = toolDir+"rapidscan"
        localDir = toolDir+"nikto"
        self.assertFalse(path.isdir(testDir))
        self.assertFalse(path.isdir(localDir))
        self.assertTrue(path.isdir(toolDir))
        cleanup()

    


if __name__ == "__main__":
    cleanup()
    unittest.main()
    

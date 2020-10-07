from os import system as shell
from subprocess import check_output
from sys import exc_info as err

from packaging import version

from core.errorHandler import ErrorHandler
from core.gui import color
from core.onilib import check_branch, return_colored_prefix


class Updater:
    """
    The update manager class of onifw

    Arguments: None
    """
    def __init__(self, installDir):
        self.installDir = installDir
        if not check_branch(installDir):
            try:
                with open("{}data/version.txt".format(installDir)) as f:
                    local_version = version.parse(
                        f.readlines()[0].rstrip("\n\r"))
                f.close()

                latest_version = check_output(
                    "curl -s https://raw.githubusercontent.com/w0bos/onifw/master/src/data/version.txt", shell=True).decode("utf-8").strip('\r\n')
                late = version.parse(latest_version)
                if late > local_version:
                    ans = input(return_colored_prefix(
                        "*") + "- A new version is available\nDo you wish to install the new update? [y/N] :" + color.END)
                    if ans.lower() in ["yes", "y"]:
                        # Won't wipe old install
                        shell("cd {} && git pull".format(installDir))
                    else:
                        print(return_colored_prefix("*") + "- Update aborted")

                elif late == local_version:
                    print(return_colored_prefix(
                        "*") + "- You're already running the latest version of onifw" + color.END)
                elif late < local_version:
                    print(return_colored_prefix(
                        "*") + "- You are running an alpha version of onifw" + color.END)
                else:
                    ErrorHandler(err(), False, True)

                shell("rm -rf {}/temp".format(installDir))
            except:
                ErrorHandler(err(), False, True)

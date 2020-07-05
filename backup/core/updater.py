import os

from packaging import version



from core.gui import color as color

class Updater:

    def __init__(self, installDir):
        try:
            with open("{}/api/version.txt".format(installDir)) as f:
                local_version = version.parse(f.readlines()[0].rstrip("\n\r"))
            f.close()

            if not os.path.isdir("{}/temp".format(installDir)):  os.makedirs("{}/temp".format(installDir))
            os.system("wget -q -O {}/temp/latest_version.txt https://raw.githubusercontent.com/w0bos/onifw/master/api/version.txt".format(installDir))
            with open("{}/temp/latest_version.txt".format(installDir)) as f:
                latest_version = version.parse(f.readlines()[0].rstrip("\n\r"))
            f.close()

            if (latest_version>local_version):
                ans = input(color.NOTICE + "[*] - A new version is available\nDo you wish to install the new update? [y/N] :" + color.END)
                if ans.lower() !="y":
                    print("[*] - Update aborted")

                elif ans.lower()=="y":
                    os.system("{}/install.sh")

            elif (latest_version==local_version) :
                print(color.OKGREEN + "[*] - You're already running the latest version of onifw" + color.END)
            elif (latest_version<local_version):
                print(color.IMPORTANT + "[*] - You are running an alpha version of onifw" + color.END)
            else:
                print(color.WARNING + "[!] - Unknown error" + color.END)

            os.system("rm -rf {}/temp".format(installDir))
        except:
            print("[!] - An unexpected error occurred! Please try again")

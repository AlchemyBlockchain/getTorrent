import subprocess, pathlib, os, distro, shutil
from PIL import ImageGrab

screenshot_dir = f"{pathlib.Path.home()}/.uni/metabot/.tmp"


def setup():
    os.makedirs(screenshot_dir, exist_ok=True)
    installOpenshot()


def takeScreenshot():
    screenshot = ImageGrab.grab()
    screenshot.show()


def openInCrop(file):
    subprocess.call(["xdg-open", f"{screenshot_dir}/{file}"])


def installOpenshot():
    """ # To Do: replace with `getpass` to make secure
    sch: https://www.google.com/search?q=python+subprocess+as+sudo
    Works: https://stackoverflow.com/questions/567542/running-a-command-as-a-super-user-from-a-python-script

    Alt:
    https://www.reddit.com/r/learnprogramming/comments/cpxt24/running_passwordprotected_sudo_commands_with/
    """
    password = "u"

    if shutil.which("openshot-qt") == "None":
        if distro.name() == "Ubuntu":
            # Works!
            subprocess.call(f"echo {password} | sudo -S apt install -y openshot-qt", shell=True)


if __name__ == '__main__':
    setup()
    takeScreenshot()

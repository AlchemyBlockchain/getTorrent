import subprocess, pathlib, os, distro, shutil
from PIL import ImageGrab

screenshot_dir = f"{pathlib.Path.home()}/.uni/metabot/.tmp"


def setup():
    os.makedirs(screenshot_dir, exist_ok=True)
    installOpenshot()


def takeScreenshot():
    def X11():
        """
        https://nitratine.net/blog/post/how-to-take-a-screenshot-in-python-using-pil/
        """
        screenshot = ImageGrab.grab()
        screenshot.show()

    def Wayland():
        """
        # Favorite: https://github.com/ponty/pyscreenshot
        >[Wayland](https://github.com/ponty/pyscreenshot#wayland)
        >Wayland is supported with these setups:
        >
        >1. using D-Bus (org.freedesktop.portal.Screenshot) on any desktop with xdg-desktop-portal.
        >2. using D-Bus (org.gnome.Shell.Screenshot) on GNOME.
        >3. using Grim on any Wayland compositor with wlr-screencopy-unstable-v1 support. (GNOME:no, KDE:no, Sway:yes)
        >If both Wayland and X are available then Wayland is preferred because Xwayland can not be used for screenshot. Rules for decision:
        >
        >1. use X if DISPLAY variable exists and XDG_SESSION_TYPE variable != "wayland"
        >2. use Wayland if 1. is not successful

        # D-Bus
        Discuss:
        - https://stackoverflow.com/questions/72216896/how-can-i-get-a-screenshot-on-wayland-with-pure-python

        # Other
        sch: https://www.google.com/search?q=python+take+screenshot+wayland
        
        Discuss.issue:
        - https://github.com/python-pillow/Pillow/issues/6312
        """
        print("Help")


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

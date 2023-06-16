import subprocess, pathlib, os, distro, time

screenshot_dir = f"{pathlib.Path.home()}/.uni/metabot/.tmp"

def setup():
    os.makedirs(screenshot_dir)

def openInCrop(file):
    subprocess.call(["xdg-open", f"{screenshot_dir}/{file}"])

def installOpenshot():
    """https://www.google.com/search?q=python+subprocess+as+sudo
    https://www.reddit.com/r/learnprogramming/comments/cpxt24/running_passwordprotected_sudo_commands_with/
    https://stackoverflow.com/questions/3172470/actual-meaning-of-shell-true-in-subprocess
    """

    if distro.name() == "Ubuntu":
        print("Installing")

        output = subprocess.call(['echo', 'u', '|', 'sudo', '-S', 'apt', 'install', 'openshot'], shell=True)
        # subprocess.call('echo u | sudo -S apt install openshot', shell=True)

        time.sleep(1.4)
        print(output)


if __name__ == '__main__':
    installOpenshot()



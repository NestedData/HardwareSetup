import os
import Utils
import shutil


USER_PATH = os.path.expanduser('~')

TEAMVIEWER_PACKAGE_NAME = "teamviewer_linux_x64.deb"
TEAMVIEWER_PACKAGE_PATH = os.path.join(USER_PATH, TEAMVIEWER_PACKAGE_NAME)
TEAMVIEWER_URL = "http://download.teamviewer.com/download/{package_name}".format(
    package_name=TEAMVIEWER_PACKAGE_NAME
)
GOOGLE_CHROME_PACKAGE_NAME = "google-chrome-stable_current_amd64.deb"
GOOGLE_CHROME_PACKAGE_PATH = os.path.join(USER_PATH, GOOGLE_CHROME_PACKAGE_NAME)
STARTUP_DESKTOP_SCRIPT_PATH = os.path.join(USER_PATH, "Desktop/Start-Drizzle.sh")
AUTORUN_SCRIPT_PATH = os.path.join(USER_PATH, ".config/autostart")
AUTORUN_SCRIPT_NAME = os.path.join(AUTORUN_SCRIPT_PATH, "drizzle.desktop")
SCREEN_LOCKER = "/etc/xdg/autostart/light-locker.desktop"
UPDATE_NOTIFIER = "/etc/xdg/autostart/update-notifier.desktop"
TEAMVIEWER_CONF_PATH = "~/.config/teamviewer9/config/client.conf"
GRUB_PATH = "/etc/default/grub"

def install_chromium():
    Utils.install_apt_packages("chromium-browser")


def install_chrome():
    # Install Chrome dependencies
    Utils.install_apt_packages(["libxss1", "libappindicator1", "libindicator7"])
    CHROME_URL_TEMPLATE = "https://dl.google.com/linux/direct/{package_name}"
    CHROME_URL = CHROME_URL_TEMPLATE.format(
        package_name=GOOGLE_CHROME_PACKAGE_NAME
    )
    # download chrome's debian package
    Utils.download_file(GOOGLE_CHROME_PACKAGE_PATH, CHROME_URL)
    # install the chrome package
    # NOTE: changed to GOOGLE_CHROME_PACKAGE_PATH so that it works from any directory, not only if this
    # script is run from the same location as the chrome binary is downloaded
    Utils.install_debian_package_binary(GOOGLE_CHROME_PACKAGE_PATH)
    # remove the google deb package that was downloaded and installed already
    # TODO: maybe os.remove()? http://stackoverflow.com/questions/6996603/how-do-i-delete-a-file-or-folder-in-python
    os.system("sudo rm -rf {path}".format(
        path=GOOGLE_CHROME_PACKAGE_PATH
    ))


# hides mouse cursor if the mouse isn't moving
def install_unclutter():
    Utils.install_apt_packages("unclutter")

def install_teamviewer():
    Utils.download_file(TEAMVIEWER_PACKAGE_PATH, TEAMVIEWER_URL)
	Utils.install_debian_package_binary(TEAMVIEWER_PACKAGE_PATH)

def disable_teamviewer_popup():
	conf = "[int32] ShowTaskbarInfoOnMinimize = 0"
	Utils.write_file(TEAMVIEWER_CONF_PATH, conf)

def set_grub_recordFail_timeout():
	grub_append = "GRUB_RECORDFAIL_TIMEOUT=2"
	Utils.write_file(GRUB_PATH, grub_append, mode='a')

def update_grub():
	os.system("sudo apt-get update-grub")

# installs/removes
def install_software():
    try:
        install_chromium()
        # install_chrome()
        # hides mouse cursor if the mouse isn't moving
        install_unclutter()
        install_teamviewer()
        # configure teamviewer
        disable_teamviewer_popup()
        # configure grub
        set_grub_recordFail_timeout()
        update_grub()
    except OSError as oserr:
        if oserr:
            raise


def cleanup():
    # disable some startup stuff
    Utils.remove_file(SCREEN_LOCKER)
    Utils.remove_file(UPDATE_NOTIFIER)

install_software()
cleanup()







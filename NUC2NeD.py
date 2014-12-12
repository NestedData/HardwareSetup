import os
import Utils
import shutil


USER_PATH = os.path.expanduser('~')

TEAMVIEWER_PACKAGE_NAME = "teamviewer_linux_x64.deb"
TEAMVIEWER_PACKAGE_PATH = os.path.join(USER_PATH, TEAMVIEWER_PACKAGE_NAME)
TEAMVIEWER_URL = "http://download.teamviewer.com/download/{package_name}".format(
    package_name=TEAMVIEWER_PACKAGE_NAME
)
TEAMVIEWER_CONF_PATH = "~/.config/teamviewer9/config/client.conf"
NODEJS_REP="https://deb.nodesource.com/setup"
GOOGLE_CHROME_PACKAGE_NAME = "google-chrome-stable_current_amd64.deb"
GOOGLE_CHROME_PACKAGE_PATH = os.path.join(USER_PATH, GOOGLE_CHROME_PACKAGE_NAME)
STARTUP_DESKTOP_SCRIPT_PATH = os.path.join(USER_PATH, "Desktop/Start-Drizzle.sh")
AUTORUN_SCRIPT_PATH = os.path.join(USER_PATH, ".config/autostart")
AUTORUN_SCRIPT_NAME = os.path.join(AUTORUN_SCRIPT_PATH, "drizzle.desktop")
POWER_MANAGER = "/etc/xdg/autostart/xfce4-power-manager.desktop"
UPDATE_NOTIFIER = "/etc/xdg/autostart/update-notifier.desktop"
HW_UPDATOR = "/etc/xdg/autostart/jockey-gtk.desktop"

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
	Utils.remove_file(GOOGLE_CHROME_PACKAGE_PATH)
	

# hides mouse cursor if the mouse isn't moving
def install_unclutter():
    Utils.install_apt_packages("unclutter")

def install_teamviewer():
	Utils.download_file(TEAMVIEWER_PACKAGE_PATH, TEAMVIEWER_URL)
	Utils.install_debian_package_binary(TEAMVIEWER_PACKAGE_PATH)
	
def install_nodejs():
	# get node.js rep
	os.system("curl -sL {NODEJS_REP} | sudo bash -".format(
		NODEJS_REP=NODEJS_REP
		))
	Utils.install_apt_packages("nodejs")
	os.system("sudo npm install -g n")

def disable_teamviewer_popup():
	conf = "[int32] ShowTaskbarInfoOnMinimize = 0"
	Utils.write_file(TEAMVIEWER_CONF_PATH, conf)

# installs/removes
def install_software():
    try:
    	install_nodejs()
        #install_chromium()
        # install_chrome()
        # hides mouse cursor if the mouse isn't moving
        install_unclutter()
        install_teamviewer()
        # configure teamviewer
        # disable_teamviewer_popup()
    except OSError as oserr:
        if oserr:
            raise


def cleanup():
    # disable some startup stuff
    Utils.remove_file(POWER_MANAGER)
    Utils.remove_file(UPDATE_NOTIFIER)
    Utils.remove_file(HW_UPDATOR)

install_software()
cleanup()
os.system("sudo python grub_setup.py")







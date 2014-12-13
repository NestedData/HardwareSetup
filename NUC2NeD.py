import os
import Utils
import shutil


USER_PATH = os.path.expanduser('~')

TEAMVIEWER_PACKAGE_NAME = "teamviewer_linux_x64.deb"
TEAMVIEWER_PACKAGE_PATH = os.path.join(USER_PATH, TEAMVIEWER_PACKAGE_NAME)
TEAMVIEWER_URL = "http://download.teamviewer.com/download/{package_name}".format(
    package_name=TEAMVIEWER_PACKAGE_NAME
)
TEAMVIEWER_PATH = USER_PATH + "/.config/teamviewer10"
TEAMVIEWER_CONF_PATH = TEAMVIEWER_PATH + "/client.conf"
TEAMVIEWER_CONF = "\n[int32] ShowTaskbarInfoOnMinimize = 0"
NODEJS_REP="https://deb.nodesource.com/setup"
GOOGLE_CHROME_PACKAGE_NAME = "google-chrome-stable_current_amd64.deb"
GOOGLE_CHROME_PACKAGE_PATH = os.path.join(USER_PATH, GOOGLE_CHROME_PACKAGE_NAME)
STARTUP_DESKTOP_SCRIPT_PATH = os.path.join(USER_PATH, "Desktop/Start-Drizzle.sh")
AUTORUN_SCRIPT_PATH = os.path.join(USER_PATH, ".config/autostart")
AUTORUN_SCRIPT_NAME = os.path.join(AUTORUN_SCRIPT_PATH, "drizzle.desktop")
POWER_MANAGER = "/etc/xdg/autostart/xfce4-power-manager.desktop"
UPDATE_NOTIFIER = "/etc/xdg/autostart/update-notifier.desktop"
HW_UPDATOR = "/etc/xdg/autostart/jockey-gtk.desktop"

######### Installs

def install_chromium():
    Utils.install_apt_packages("chromium-browser")


def install_chrome():
    # Install Chrome dependencies
    Utils.install_apt_packages(["libxss1", "libappindicator1", "libindicator7"])
    CHROME_URL_TEMPLATE = "https://dl.google.com/linux/direct/{package_name}"
    CHROME_URL = CHROME_URL_TEMPLATE.format(
    package_name=GOOGLE_CHROME_PACKAGE_NAME
    )
    # download chrome's debian package and install it
    Utils.download_install_deb(CHROME_URL, GOOGLE_CHROME_PACKAGE_PATH)    

# hides mouse cursor if the mouse isn't moving
def install_unclutter():
    Utils.install_apt_packages("unclutter")

def configure_unclutter():
    os.system("unclutter -idle 0.01 -root&")

def install_teamviewer():
    Utils.download_install_deb(TEAMVIEWER_PACKAGE_PATH, TEAMVIEWER_URL)
    Utils.copy_and_backup_original("copyFiles/teamviewer10", TEAMVIEWER_PATH)
    # Create initial files
    os.system("cp -rp copyFiles/teamviewer10 {path}".format(path=TEAMVIEWER_PATH))
    
def disable_teamviewer_popup():
    Utils.write_file(TEAMVIEWER_CONF_PATH, TEAMVIEWER_CONF, 'a')

def install_nodejs():
    # get node.js rep
    os.system("curl -sL {NODEJS_REP} | sudo bash -".format(
        NODEJS_REP=NODEJS_REP
        ))
    Utils.install_apt_packages("nodejs")
    os.system("sudo npm install -g n")

######### Startup Scripts
# make desktop script to open chromium
def chromium_startup_script_template():
    school_name = raw_input("What is the schools name?") or "Mississippi State University"
    school_name = Utils.slugify(school_name)
    SCHOOL_STREAMER_URL = "http://socialdrizzle.com/{school_name}/s/jumbotron".format(
        school_name=school_name
    )
    script_lines = [
        "#!/bin/bash\n",
        "chromium-browser --kiosk {url}".format(url=SCHOOL_STREAMER_URL),
    ]
    return '\n'.join(script_lines)

# write the file that will cause start-drizzle.sh to be run on startup
def write_autostart_script():
    # creates ~/.config/autostart/directory 
    if not os.path.exists(AUTORUN_SCRIPT_PATH):   
        os.makedirs(AUTORUN_SCRIPT_PATH)
    # creates drizzle.desktop
    Utils.write_file(AUTORUN_SCRIPT_NAME, autostart_script_template())

# write the file that will be run at startup
def write_chromium_startup_script():
    # creates Start-Drizzle.sh on Desktop
    Utils.write_file(STARTUP_DESKTOP_SCRIPT_PATH, chromium_startup_script_template())
    # change permissions to execute
    os.chmod(STARTUP_DESKTOP_SCRIPT_PATH, 0755)

# template for startup script
def autostart_script_template():
    script_lines = [
        "[Desktop Entry]\n",
        "Type=Application",
        "Exec="+STARTUP_DESKTOP_SCRIPT_PATH
    ]
    return '\n'.join(script_lines)

######### Finishing up

def cleanup():
    # disable some startup stuff
    Utils.remove_file(POWER_MANAGER)
    Utils.remove_file(UPDATE_NOTIFIER)
    Utils.remove_file(HW_UPDATOR)

def run_linux_adjustments():
    os.system("sudo python grub_setup.py")
    os.system("sudo python killDPMS.py")

# installs/removes
def install_software():
    try:
    	install_nodejs()
        #install_chromium()
        # install_chrome()
        # hides mouse cursor if the mouse isn't moving
        install_unclutter()
        install_teamviewer()
        print "done"
        # configure teamviewer
        # disable_teamviewer_popup()
    except OSError as oserr:
        if oserr:
            raise

# makes the necessary files for autostart
def make_startup_files():
    try:
        write_chromium_startup_script()
        write_autostart_script()
    except OSError as oserr:
        if oserr:
            raise 


install_software()
cleanup()
make_startup_files()
run_linux_adjustments()
configure_unclutter()



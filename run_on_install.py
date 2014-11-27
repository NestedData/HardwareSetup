import os

GOOGLE_CHROME_PACKAGE_NAME = "google-chrome-stable_current_amd64.deb"
GOOGLE_CHROME_PACKAGE_PATH = os.path.expanduser("~")+"/"+GOOGLE_CHROME_PACKAGE_NAME
SCHOOL_STREAMER_URL = "http://socialdrizzle.com/univeristy-of-alabama-at-birmingham/s/jumbotron"
STARTUP_DESKTOP_SCRIPT_PATH = os.path.expanduser("~")+"/Desktop/Start-Drizzle.sh"
AUTORUN_SCRIPT_PATH = os.path.expanduser("~")+"/.config/autostart/directory"
AUTORUN_SCRIPT_NAME = AUTORUN_SCRIPT_PATH+"/drizzle.desktop"

# installs/removes
def install_software():
    try:
        # install chromium
        os.system("sudo apt-get install chromium-browser")
        # Install Chrome dependencies
        os.system("sudo apt-get install libxss1 libappindicator1 libindicator7")
        # download chrome's debian package
        os.system("wget -O "+GOOGLE_CHROME_PACKAGE_PATH+" https://dl.google.com/linux/direct/$GOOGLE_CHROME_PACKAGE_NAME")
        # install the chrome package
        os.system("sudo dpkg -i "+GOOGLE_CHROME_PACKAGE_NAME)
        # remove the google deb package that was downloaded and installed already
        os.system("sudo rm -rf "+GOOGLE_CHROME_PACKAGE_PATH)
    except OSError as oserr:
        if oserr:
            raise 

# makes the necessary files for autostart
def make_startup_files():
    try:
        # creates Start-Drizzle.sh on Desktop
        startup_desktop = open(STARTUP_DESKTOP_SCRIPT_PATH, "w")
        # writes script to run on startup
        startup_desktop.write("#!/bin/bash\nchromium-browser --kiosk " + SCHOOL_STREAMER_URL)
        # change permissions to exicute
        os.system("chmod 755 "+STARTUP_DESKTOP_SCRIPT_PATH)

        # creates ~/.config/autostart/directory 
        os.makedirs(AUTORUN_SCRIPT_PATH)
        # creates drizzle.desktop
        startup_config = open(AUTORUN_SCRIPT_NAME, "w")
        # writes script for running autostart
        startup_config.write("[Desktop Entry]\n\nType=Application\n\nExec="+STARTUP_DESKTOP_SCRIPT_PATH)
        
    except OSError as oserr:
        if oserr:
            raise 
    

install_software()

make_startup_files()

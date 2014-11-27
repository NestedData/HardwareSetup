# NOTE: if we're going to use python for this let's give up on making it look like a
#       bash script. Instead, lets grab python by the jewels and make it bend to our whims.
#       os.system should be removed as much as possible. replace them with python tools
#       that do what the bash tool we're running does. Otherwise, we should just go back to
#       bash so we have easy access to pipes and redirects.
import os
from slugify import slugify


USER_PATH = os.path.expanduser('~')

school_name = raw_input("What is the schools name?") or "University of Alabama at Birmingham"
school_name = slugify(school_name)

GOOGLE_CHROME_PACKAGE_NAME = "google-chrome-stable_current_amd64.deb"
GOOGLE_CHROME_PACKAGE_PATH = os.path.join(USER_PATH, GOOGLE_CHROME_PACKAGE_NAME)
SCHOOL_STREAMER_URL = "http://socialdrizzle.com/"+school_name+"/s/jumbotron"
STARTUP_DESKTOP_SCRIPT_PATH = os.path.join(USER_PATH, "Desktop/Start-Drizzle.sh")
AUTORUN_SCRIPT_PATH = os.path.join(USER_PATH, ".config/autostart")
AUTORUN_SCRIPT_NAME = os.path.join(AUTORUN_SCRIPT_PATH, "drizzle.desktop")

print SCHOOL_STREAMER_URL
def install_debian_package_binary(package_path):
    os.system("sudo dpkg -i {package_path}".format(**{
        package_path: package_path
    }))

def install_chromium():
    os.system("sudo apt-get install chromium-browser")

# NOTE: TBH at this point you should probably use urllib or something
# other than spawning a system call to download this file.
# http://stackoverflow.com/questions/2467609/using-wget-via-python
def wget(target_path, source_url):
    os.system("wget -O {target_path} {source_url}".format(**{
        'target_path': target_path,
        'source_url': source_url
    }))

def install_chrome():
    # Install Chrome dependencies
    os.system("sudo apt-get install libxss1 libappindicator1 libindicator7")
    CHROME_URL = "https://dl.google.com/linux/direct/{package_name}".format(**{
        'package_name': GOOGLE_CHROME_PACKAGE_NAME
    })
    # download chrome's debian package
    wget(GOOGLE_CHROME_PACKAGE_PATH, CHROME_URL)
    # install the chrome package
    # NOTE: changed to GOOGLE_CHROME_PACKAGE_PATH so that it works from any directory, not only if this
    # script is run from the same location as the chrome binary is downloaded
    install_debian_package_binary(GOOGLE_CHROME_PACKAGE_PATH)
    # remove the google deb package that was downloaded and installed already
    # TODO: maybe os.remove()? http://stackoverflow.com/questions/6996603/how-do-i-delete-a-file-or-folder-in-python
    os.system("sudo rm -rf "+GOOGLE_CHROME_PACKAGE_PATH)

def chromium_startup_script_template():
    script_lines = [
        "#!/bin/bash\n",
        "chromium-browser --kiosk " + SCHOOL_STREAMER_URL,
    ]
    return '\n'.join(script_lines)

def write_chromium_startup_script():
    # creates Start-Drizzle.sh on Desktop
    file_handle = open(STARTUP_DESKTOP_SCRIPT_PATH, "w")
    # writes script to run on startup
    file_handle.write(chromium_startup_script_template())
    # change permissions to execute
    os.system("chmod 755 "+STARTUP_DESKTOP_SCRIPT_PATH)


def autostart_script_template():
    script_lines = [
        "[Desktop Entry]\n",
        "Type=Application",
        "Exec="+STARTUP_DESKTOP_SCRIPT_PATH
    ]
    return '\n'.join(script_lines)
def write_autostart_script():
    # creates ~/.config/autostart/directory 
    os.makedirs(AUTORUN_SCRIPT_PATH)
    # creates drizzle.desktop
    startup_config = open(AUTORUN_SCRIPT_NAME, "w")
    # writes script for running autostart
    startup_config.write(autostart_script_template())

# installs/removes
def install_software():
    try:
        install_chromium()
        install_chrome()
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

make_startup_files()

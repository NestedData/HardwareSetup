import os
import Utils
import shutil
import socket

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

# write the file that will be run at startup
def write_chromium_startup_script():
    # creates Start-Drizzle.sh on Desktop
    Utils.write_file(STARTUP_DESKTOP_SCRIPT_PATH, chromium_startup_script_template())
    # change permissions to execute
    os.chmod(STARTUP_DESKTOP_SCRIPT_PATH, 0755)


def autostart_script_template():
    script_lines = [
        "[Desktop Entry]\n",
        "Type=Application",
        "Exec="+STARTUP_DESKTOP_SCRIPT_PATH
    ]
    return '\n'.join(script_lines)

# write the file that will cause start-drizzle.sh to be run on startup
def write_autostart_script():
    # creates ~/.config/autostart/directory 
    if not os.path.exists(AUTORUN_SCRIPT_PATH):   
        os.makedirs(AUTORUN_SCRIPT_PATH)
    # creates drizzle.desktop
    Utils.write_file(AUTORUN_SCRIPT_NAME, autostart_script_template())


def configure_unclutter():    
    os.system("unclutter -idle 0.01 -root")


# makes the necessary files for autostart
def make_startup_files():
    try:
        write_chromium_startup_script()
        write_autostart_script()
    except OSError as oserr:
        if oserr:
            raise 

def change_hostname():
    HOSTNAME_PATH = "/etc/hostname"
    HOSTS_PATH = "/etc/hosts"
    old_hostname = socket.gethostname()
    new_hostname = raw_input("What is this NeD's name?") or socket.gethostname()
    os.chmod(HOSTNAME_PATH, 0666)
    Utils.write_file(HOSTNAME_PATH, new_hostname, true)
    #### read every line of HOSTS_PATH until old_hostname is found then
    #### replace it with new_hostname
    # change hostname immediatly (uncomment after the rest of the function is done)
    # os.system("sudo hostname {hostname}".format(hostname=new_hostname))
    ############################

make_startup_files()
configure_unclutter()

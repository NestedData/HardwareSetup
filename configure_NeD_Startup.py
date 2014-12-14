import os
import Utils

USER_PATH = os.path.expanduser('~')

STARTUP_DESKTOP_SCRIPT_PATH = os.path.join(USER_PATH, "Desktop/Start-Drizzle.sh")
AUTORUN_SCRIPT_PATH = os.path.join(USER_PATH, ".config/autostart")
AUTORUN_SCRIPT_NAME = os.path.join(AUTORUN_SCRIPT_PATH, "drizzle.desktop")
POWER_MANAGER = "/etc/xdg/autostart/xfce4-power-manager.desktop"
UPDATE_NOTIFIER = "/etc/xdg/autostart/update-notifier.desktop"
HW_UPDATOR = "/etc/xdg/autostart/jockey-gtk.desktop"

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
        "unclutter -idle 0.01 -root &",
        "sleep 6",
        'wmctrl -r "Computers & Contacts" -b toggle,shaded',
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

# require sudo
def remove_startup_services():
    # disable some default startup stuff
    Utils.remove_file(POWER_MANAGER)
    Utils.remove_file(UPDATE_NOTIFIER)
    Utils.remove_file(HW_UPDATOR)
    print "Removed unnecessary startup services."



# makes the necessary files for autostart
def make_startup_files():
    try:
        write_chromium_startup_script()
        write_autostart_script()
        print "Finished writing startup files."
    except OSError as oserr:
        if oserr:
            raise 


remove_startup_services()
make_startup_files()

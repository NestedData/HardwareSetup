import os
import Utils
import shutil

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
    

make_startup_files()
configure_unclutter()

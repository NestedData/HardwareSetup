import os
import shutil

DPMS_PATH = "/etc/X11/"

if not os.path.exists(DPMS_PATH):   
	os.makedirs(DPMS_PATH)
	DPMS_PATH = DPMS_PATH + "xorg.conf.d"
shutil.copyfile(DPMS_PATH, "xorg.conf.d")
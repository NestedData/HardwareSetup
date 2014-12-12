import os
import shutil

DPMS_PATH = "/etc/X11/"

if not os.path.exists(DPMS_PATH):   
	os.makedirs(DPMS_PATH)
	
shutil.copyfile("xorg.conf.d", DPMS_PATH)
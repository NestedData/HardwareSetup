import os
import shutil

DPMS_PATH = "/etc/X11/xorg.conf.d"

shutil.copyfile(DPMS_PATH, "xorg.conf.d")
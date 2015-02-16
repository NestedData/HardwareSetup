#!/usr/bin/env bash

# make backup folder
mkdir backup_logo

# make backup of logo
sudo cp /lib/plymouth/themes/lubuntu-logo/lubuntu_logo.png backup_logo
# make backup of on dot
sudo cp /lib/plymouth/themes/lubuntu-logo/progress_dot_on.png backup_logo
# make backup of off dot
sudo cp /lib/plymouth/themes/lubuntu-logo/progress_dot_off.png backup_logo
# replace old logo with new KICK ASS LOGO
sudo cp IMG/lubuntu_logo.png /lib/plymouth/themes/lubuntu-logo/lubuntu_logo.png
# replace old logo with new BLUE KICK ASS RAIN DROPS
sudo cp IMG/progress_dot_on.png /lib/plymouth/themes/lubuntu-logo/progress_dot_on.png
# replace old logo with new BLUE KICK ASS RAIN DROPS
sudo cp IMG/progress_dot_off.png /lib/plymouth/themes/lubuntu-logo/progress_dot_off.png

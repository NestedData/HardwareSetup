#! /bin/sh

# Configure Grub
sudo python grub_setup.py
# AKA: 
# sudo cat GRUB_RECORDFAIL_TIMEOUT=2 >> /etc/default/grub
# sudo update-grub

# Configure power management
sudo python killDPMS.py
# AKA:
# sudo mkdir -p /etc/X11
# sudo cp copyFiles/xorg.conf.g /etc/X11/

# Install pip
sudo apt-get install -y python-pip
# Install our python requirements
sudo pip install -r requirements.txt

# Make it a a NeD
sudo python NUC2NeD.py

teamviewer
xfce4-power-manager
xscreensaver-demo

# configure teamviewer to not popup on startup
echo '\n[int32] ShowTaskbarInfoOnMinimize = 0' >> ~/.config/teamviewer10/client.conf

# TODO: disable teamviewer popup on remote login
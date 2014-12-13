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

echo "Downloading and installing teamviewer."
wget http://download.teamviewer.com/download/teamviewer_amd64.deb
sudo dpkg -i teamviewer_amd64.deb
sudo apt-get install -fy
sudo dpkg -i teamviewer_amd64.deb
echo "Launching teamviewer. Please accept the license, configure it, and exit the application to continue."
teamviewer
echo "Configure power." 
xfce4-power-manager-settings
echo "Disable screensaver."
xscreensaver-demo

# configure teamviewer to not popup on startup
echo "[int32] ShowTaskbarInfoOnMinimize = 0" >> ~/.config/teamviewer10/client.conf

# TODO: disable teamviewer popup on remote login
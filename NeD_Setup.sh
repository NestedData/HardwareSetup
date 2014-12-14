#! /bin/sh

NODEJS_REP="https://deb.nodesource.com/setup"
GRUB_PATH = "/etc/default/grub"
GRUB_APPEND = "GRUB_RECORDFAIL_TIMEOUT=2"
DPMS_PATH = "/etc/X11/"
INSTALL_CONF_PATH="copyFiles/xorg.conf.d"

######### Install software
sudo apt-get update

echo "Downloading and installing teamviewer."
wget http://download.teamviewer.com/download/teamviewer_amd64.deb
sudo dpkg -i teamviewer_amd64.deb
sudo apt-get install -fy
sudo dpkg -i teamviewer_amd64.deb
echo "Successfully installed Teamviewer."

# Get node.js repository
curl -sL $NODEJS_REP | sudo bash -

# # Install pip 
sudo apt-get install -y python-pip 
# Install our python requirements
sudo pip install -r requirements.txt

# Install node.js
sudo apt-get install -y nodejs
# Install n
sudo npm install -g n
echo "Successfully installed NodeJS."

#install windows manager control (hides teamviewer)
sudo apt-get install -y wmctrl

# Install unclutter (hides mouse)
sudo apt-get install -y unclutter
echo "Finished installing software."

# Modify grub to auto boot int os
sudo cat $GRUB_APPEND >> $GRUB_PATH
sudo update-grub

# Mondify xorg.conf.d in /etc/X11 if dir does not exist make it
if [ ! -d "$DPMS_PATH" ]; then
	sudo mkdir -p DPMS_PATH
fi
sudo cp -p INSTALL_CONF_PATH DPMS_PATH

########## Launch apps that need to be modified manually

echo "Launching teamviewer. Please accept the license, configure it, and exit the application to continue."
teamviewer
echo "Configure power." 
xfce4-power-manager-settings
echo "Disable screensaver."
xscreensaver-demo

######### Write startup files and remove unwanted startup items 
# Make it a NeD
sudo python configure_NeD_Startup.py



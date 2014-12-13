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
python NUC2NeD.py

#!/bin/sh

#installs/removes
sudo apt-get install chromium-browser
sudo apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb

sudo rm -rf ~/Desktop/google*

# adds Start-Drizzle.sh to Desktop to open on boot
echo "#!/bin/bash \n
chromium-browser --kiosk ‘http://socialdrizzle.com/univeristy-of-alabama-at-birmingham/s/jumbotron’" > ~/Desktop/Start-Drizzle.sh

chmod 755 Start-Drizzle.sh

# set autostart to desktop file
mkdir -p ~/.config/autostart/directory/
echo "[Desktop Entry]
Type=Application
Exec=/home/{computer_name(ex:drizzle2-desktop)}/Start-Drizzle.sh" > ~/.config/autostart/directory/drizzle.desktop

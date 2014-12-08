# Setup

1. Install lubuntu 14.04
2. Open terminal
3. Execute "bash run.sh"
4. Set all energy settings to never
	Menu -> Preferences -> Light Locker Settings
		both sliders = Never
		enable LL = OFF
	Menu -> Preferences -> Power Manager
		General
			when pwr btn pressed = shutdown
		On AC
			Actions: slider = never
			Monitor: both sliders = never
		Extended
			uncheck lock screen
5. Configure TeamViewer
	Autostart on boot
	Disable windows on boot 
6. Reboot into NeD_base

#####################################################

To upgrade from NeD_base to NeD_XXX#
### TODO.........
Navigate to http://socialdrizzle.com/sign-in
6. Enter Email and Password

# Developers

To freeze pip requirements

`pip freeze > requirements.txt` from within the root of the hardwaresetup repo while in the appropriate virtualenv


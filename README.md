# Create `NeD_XXX###`

1. Install lubuntu 12.04

	`Your Name: Social Drizzle`

	`Computer Name: NeD_XXX###`
	
	`User Name: socialdrizzle `
	
	`Password: S9@rx4L`
	
2. Go to and download

	`https://github.com/NestedData/HardwareSetup`
	
3. Open terminal execute 

	`cd ~/Downloads/HardwareSetup && sudo bash run.sh`
	
4. Set all energy settings to never

	Menu -> Preferences -> Screen Saver
	
		Mode -> Disable Screen Saver
		
	Menu -> Preferences -> Power Manager
	
		General
		
			when pwr btn pressed = shutdown
			
		On AC
		
			Actions: slider = never
			
			Monitor: both sliders = never
			
		Extended
		
			uncheck lock screen
			
5. Configure TeamViewer

	Extras -> options
	
		check `Start teamviewer with system`
	
	
6.Navigate to http://socialdrizzle.com/sign-in

	sign in as NeD's user
7. Reboot into NeD_base



# Developers

To freeze pip requirements

`pip freeze > requirements.txt` from within the root of the hardwaresetup repo while in the appropriate virtualenv


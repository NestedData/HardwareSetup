# Create `NeD_XXX###`

1. Install lubuntu 12.04

	`Your Name: SocialDrizzle`

	`Computer Name: NeD_XXX###`
	
	`User Name: socialdrizzle `
	
	`Password: S9@rx4L`
	
2. Go to, download, and extract to `~`

	`https://github.com/NestedData/HardwareSetup`
	
3. Open terminal execute 

	`cd HardwareSetup && sudo bash run.sh`
	
# While that is running
	
Set all energy settings to never
	
	Menu -> Preferences -> Screen Saver
	
		Mode -> Disable Screen Saver
		
	Menu -> Preferences -> Power Manager
	
		General
		
			when pwr btn pressed = shutdown
			
			uncheck boxes
			
		On AC
		
			Actions: slider = never
			
			Monitor: both sliders = never
			
		Extended
		
			uncheck lock screen

Navigate to [http://socialdrizzle.com/sign-in]

	sign in as NeD's user
	
				
Configure TeamViewer

	Extras -> options
	
		check `Start teamviewer with system`
	
	
# When Finished

Reboot into NeD_base



# Developers

To freeze pip requirements

`pip freeze > requirements.txt` from within the root of the hardwaresetup repo while in the appropriate virtualenv


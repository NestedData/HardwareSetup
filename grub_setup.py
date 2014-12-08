import os
import Utils

GRUB_PATH = "/etc/default/grub"

def set_grub_recordFail_timeout():
	grub_append = "GRUB_RECORDFAIL_TIMEOUT=2"
	#os.system("sudo cat grub_append >> GRUB_PATH".format(
	#grub_append=grub_append,
	#GRUB_PATH=GRUB_PATH
	#))
	#os.chmod(GRUB_PATH, 0666)
	Utils.write_file(GRUB_PATH, grub_append, mode='a')

def update_grub():
	os.system("sudo update-grub")

# configure grub
set_grub_recordFail_timeout()
update_grub()
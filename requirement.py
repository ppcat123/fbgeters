import subprocess

def download_requirements():
    # Get user input for the shell command
    shell_command = input("Enter the shell command to download requirements: ")

    try:
        # Use subprocess to run the user-provided shell command
        subprocess.check_call(shell_command, shell=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing the command: {str(e)}")

if __name__ == "__main__":
    download_requirements()

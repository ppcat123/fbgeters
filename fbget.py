#!/usr/bin/env python3
import sys
import time
import subprocess

# ANSI escape codes for colors and formatting
GREEN = '\033[92m'
BOLD = '\033[1m'
END = '\033[0m'

def main():
    name = input(f"{BOLD}Enter your name:{END} ")
    print(f"Hello, {GREEN}{name}{END}! {BOLD}Welcome to Shell Design{END}.")
    
    # Add a 5-second delay
    print(f"Waiting for 5 seconds...")
    time.sleep(5)
    
    # Execute fbgetter.py
    try:
        subprocess.run(["python3", "fbgetter.py"])  # Adjust the command as needed
    except Exception as e:
        print(f"Error executing fbgetter.py: {e}")
    
if __name__ == "__main__":
    main()

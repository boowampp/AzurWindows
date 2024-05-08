import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display menu options
def display_menu():
    clear_screen()
    print(Fore.GREEN + r"""
                             __          ___           _                   
     /\                     \ \        / (_)         | |                  
    /  \    _____   _ _ __   \ \  /\  / / _ _ __   __| | _____      _____ 
   / /\ \  |_  / | | | '__|   \ \/  \/ / | | '_ \ / _` |/ _ \ \ /\ / / __|
  / ____ \  / /| |_| | |       \  /\  /  | | | | | (_| | (_) \ V  V /\__ \
 /_/    \_\/___|\__,_|_|        \/  \/   |_|_| |_|\__,_|\___/ \_/\_/ |___/
                                                                          
                                                                          
    """ + Style.RESET_ALL)
    print("1. Activate")
    print("2. Contact")
    print("3. Quit")

# Function to activate
def activate():
    print("Activating...")
    subprocess.run(["powershell", "-Command", "irm https://massgrave.dev/get | iex"])

# Function to display contact information
def display_contact():
    print("Contact me on Discord: boowamp", end='')

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Activate option
            activate()
            input("Press Enter to continue...")
        elif choice == '2':
            # Contact option
            display_contact()
            input("Press Enter to continue...")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
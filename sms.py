import os
import sys
import time
import requests

# ANSI Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def print_logo():
    logo = f"""
{RED}
   ______ ____  _____  _    _          _____   
  |  ____/ __ \\|  __ \\| |  | |   /\\   |  __ \\  
  | |__ | |  | | |__) | |__| |  /  \\  | |  | | 
  |  __|| |  | |  _  /|  __  | / /\\ \\ | |  | | 
  | |   | |__| | | \\ \\| |  | |/ ____ \\| |__| | 
  |_|    \\____/|_|  \\_\\_|  |_/_/    \\_\\_____/  
{RESET}
"""
    print(logo)

def open_social_link(choice):
    links = {
        '1': "https://facebook.com/forhadhasan995",
        '2': "https://github.com/Forhadj",
        '3': "https://t.me/f_forhad",
        '4': "https://youtube.com/@forhad2.00"
    }
    if choice in links:
        print(f"{CYAN}Opening link: {links[choice]}{RESET}")
        if sys.platform.startswith('linux') or sys.platform == 'darwin':
            os.system(f"xdg-open {links[choice]} 2>/dev/null")
        elif sys.platform.startswith('win'):
            os.system(f"start {links[choice]}")
        else:
            print(f"{RED}Cannot open links on this platform.{RESET}")
        time.sleep(1)
    else:
        print(f"{RED}Invalid option!{RESET}")

def send_sms(phone_number):
    """
    Example SMS bombing function using a fake API endpoint.
    Replace this with your actual SMS API or method.
    """
    url = "https://example-sms-api.com/send"  # Replace with your real API URL
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    payload = {
        "phone": phone_number,
        "message": "This is a test SMS bombing message"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"{GREEN}SMS sent successfully to {phone_number}{RESET}")
            return True
        else:
            print(f"{RED}Failed to send SMS to {phone_number}. Status: {response.status_code}{RESET}")
            return False
    except Exception as e:
        print(f"{RED}Error sending SMS: {e}{RESET}")
        return False

def start_sms_bombing():
    print(f"{CYAN}Enter the target phone number (with country code, e.g. +8801XXXXXXXXX):{RESET}")
    phone = input("Phone number: ").strip()
    if not phone.startswith('+'):
        print(f"{RED}Please include the country code, e.g. +8801XXXXXXXXX{RESET}")
        return
    print(f"{CYAN}How many SMS do you want to send?{RESET}")
    try:
        count = int(input("Count: "))
    except:
        print(f"{RED}Invalid number.{RESET}")
        return

    print(f"{GREEN}Starting SMS bombing to {phone} with {count} messages...{RESET}")

    for i in range(count):
        print(f"Sending SMS {i+1} of {count}...")
        success = send_sms(phone)
        time.sleep(1)  # Adjust delay as per your API limits
        if not success:
            print(f"{RED}Stopping bombing due to failure.{RESET}")
            break

    print(f"{GREEN}SMS bombing process finished.{RESET}")

def main_menu():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print_logo()
        print(f"{CYAN}Select an option from the menu:{RESET}")
        print(f"{GREEN}1.{RESET} Start SMS Bombing")
        print(f"{GREEN}2.{RESET} Open Social Links")
        print(f"{GREEN}0.{RESET} Exit")

        choice = input("Your choice: ").strip()

        if choice == '1':
            start_sms_bombing()
        elif choice == '2':
            print(f"{CYAN}Social Links:{RESET}")
            print(f"{GREEN}1.{RESET} Facebook")
            print(f"{GREEN}2.{RESET} GitHub")
            print(f"{GREEN}3.{RESET} Telegram")
            print(f"{GREEN}4.{RESET} YouTube")
            print(f"{GREEN}0.{RESET} Back to Main Menu")

            link_choice = input("Which link do you want to open? ").strip()
            if link_choice == '0':
                continue
            else:
                open_social_link(link_choice)
            input("Press Enter to return to main menu...")
        elif choice == '0':
            print(f"{RED}Exiting... Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice, try again.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}Interrupted! Exiting...{RESET}")
        sys.exit()

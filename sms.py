import os
import time

def show_logo():
    print("""
  ______ ____  _____  _    _          _____   
 |  ____/ __ \|  __ \| |  | |   /\   |  __ \  
 | |__ | |  | | |__) | |__| |  /  \  | |  | | 
 |  __|| |  | |  _  /|  __  | / /\ \ | |  | | 
 | |   | |__| | | \ \| |  | |/ ____ \| |__| | 
 |_|    \____/|_|  \_\_|  |_/_/    \_\_____/  
    """)

def menu():
    print("""
1. Facebook: https://facebook.com/forhadhasan995
2. GitHub: https://github.com/Forhadj
3. Telegram: https://t.me/f_forhad
4. YouTube: https://youtube.com/@forhad2.00?si=vmV-oUKHLF3ZCTnu
0. Exit
""")

def open_link(choice):
    if choice == '1':
        os.system("xdg-open https://facebook.com/forhadhasan995")
    elif choice == '2':
        os.system("xdg-open https://github.com/Forhadj")
    elif choice == '3':
        os.system("xdg-open https://t.me/f_forhad")
    elif choice == '4':
        os.system("xdg-open https://youtube.com/@forhad2.00?si=vmV-oUKHLF3ZCTnu")
    elif choice == '0':
        print("Exiting...")
        exit()
    else:
        print("Please select a valid option.")

def sms_bomb(number, count):
    print(f"Starting to send {count} SMS messages to {number}...")
    for i in range(count):
        # Add your SMS API or sending logic here
        print(f"SMS sent: {i+1}")
        time.sleep(1)
    print("SMS bombing finished.")

def main():
    show_logo()
    while True:
        print("\nSelect an option from the menu:")
        print("1. Start SMS Bombing")
        print("2. Open Social Links")
        print("0. Exit")
        choice = input("Your choice: ")
        if choice == '1':
            number = input("Enter the phone number to send SMS: ")
            count = int(input("How many SMS do you want to send? "))
            sms_bomb(number, count)
        elif choice == '2':
            menu()
            opt = input("Which link do you want to open? ")
            open_link(opt)
        elif choice == '0':
            print("Thanks for using the tool!")
            break
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main()

import time
import os

def clear_screen():
    # Clear the terminal screen (works for Unix-like systems)
    os.system('clear' if os.name == 'posix' else 'cls')

def display_title():
    title = """
╦╔╗╔╔═╗╔╦╗╔═╗╔═╗╦═╗╔═╗╔╦╗  ╔═╗╔═╗╔═╗╔╦╗╦ ╦╔═╗╦═╗╔═╗
║║║║╚═╗ ║ ╠═╣║ ╦╠╦╝╠═╣║║║  ╚═╗║ ║╠╣  ║ ║║║╠═╣╠╦╝║╣ 
╩╝╚╝╚═╝ ╩ ╩ ╩╚═╝╩╚═╩ ╩╩ ╩  ╚═╝╚═╝╚   ╩ ╚╩╝╩ ╩╩╚═╚═╝ 
- ENTER USERNAME TO GRAB ACCOUNT                                                                                        
    """
    print(title)

def get_username():
    while True:
        username = input("Enter Username: ")
        if 6 <= len(username) <= 30:
            return username
        else:
            print("-- Username must be between 6 and 30 characters. --")

def loading_animation(username):
    print(f"Loading {username}..")
    time.sleep(15)

def main():
    while True:
        clear_screen()
        display_title()
        username = get_username()
        loading_animation(username)

        # Print the result
        print("----------------")
        print(f"Username: {username}")
        print("Login: springneedham14@aol.com:gub7F*FGQ6jrDZ&xY7HZ")
        print("---")
        print(f"Private Messages Access ✅")
        print(f"Deleted Photos Access ✅")
        print("---")
        print(f"Completed: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("----------------")

        choice = input("Press 'Enter' to regenerate or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            break

if __name__ == "__main__":
    main()

from colorama import init, Fore, Style

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f"{Fore.RED}User not found{Style.RESET_ALL}")
        except ValueError:
            return f"{Fore.MAGENTA}Enter the argument for the command.{Style.RESET_ALL}"
        except IndexError:
            return f"{Fore.MAGENTA}Enter the argument for the command.{Style.RESET_ALL}"
        except Exception as err:
            print(f"An unexpected error occurred: {err}")

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"{Fore.GREEN}Contact added.{Style.RESET_ALL}"

@input_error
def change_contact(args, contacts):
    name, phone = args
    if (name in contacts):
        contacts[name] = phone
        return f"{Fore.GREEN}Contact changed.{Style.RESET_ALL}"
    else:
        raise KeyError
        
    

@input_error
def phone_user(args, contacts):
    [name] = args
    
    phone = contacts.get(name)

    if phone:
      return f"{name}: {phone}"
    else:
        return f"{Fore.RED}Not found phone{Style.RESET_ALL}"
    
@input_error
def all_users(contacts):
    for name, phone in contacts.items():
        print(f"{Fore.CYAN}Name: {Fore.YELLOW}{name}, {Fore.CYAN}Phone: {Fore.YELLOW}{phone}{Style.RESET_ALL}") 

def main():
    init()

    contacts = {}

    print(f"{Fore.MAGENTA}Welcome to the assistant bot!{Style.RESET_ALL}")
    while True:
        user_input = input(f"{Fore.BLUE}Enter a command: {Style.RESET_ALL}")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print(f"{Fore.MAGENTA}Good bye!{Style.RESET_ALL}")
            break
        elif command == "hello":
            print(f"{Fore.MAGENTA}How can I help you?{Style.RESET_ALL}")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_user(args, contacts))
        elif command == "all":
            all_users(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

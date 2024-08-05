def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid input format. Please provide the necessary arguments."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args):
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all_contacts(args):
    if not contacts:
        return "No contacts found."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    commands = {
        "add": add_contact,
        "phone": get_contact,
        "all": show_all_contacts,
    }

    while True:
        command_input = input("Enter a command: ").strip().lower()
        if command_input in commands:
            args_input = input("Enter the argument for the command: ").strip().split()
            print(commands[command_input](args_input))
        elif command_input == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()

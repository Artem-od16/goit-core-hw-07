from classes import AddressBook, Record
from functions import parse_input


def main():
    book = AddressBook()
    methods = {
        "add": Record.add_phone,
        "change": Record.edit_phone,
        "phone": Record.find_phone,
        "all": AddressBook.show_all,
        "delete-phone": Record.remove_phone,
        "delete-contact": Record.remove_contact,
        "add-birthday": Record.add_birthday,
        "show-birthday": Record.find_birthday,
        "birthdays": Record.birthdays,
    }

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(methods["add"](args, book))

        elif command == "change":
            print(methods["change"](args, book))

        elif command == "phone":
            print(methods["phone"](args, book))

        elif command == "delete-phone":
            print(methods["delete-phone"](args, book))

        elif command == "all":
            for name, record in book.data.items():
                print(record)

        elif command == "add-birthday":
            print(methods["add-birthday"](args, book))

        elif command == "show-birthday":
            print(methods["show-birthday"](args, book))

        elif command == "birthdays":
            print(methods["birthdays"](args, book))

        elif command == "delete-contact":
            print(methods["delete-contact"](args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

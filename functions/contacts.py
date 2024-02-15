from .decorators import input_error


@input_error
def add_contact(args, book):
    name, phone = args
    if name.isalpha() and phone.isdigit():
        book[name] = phone
        return "Contact added."
    else:
        return "Contact cannot be added. Name  must consist of letters and phone must consist of numbers."


@input_error
def change_contact(args, book):
    name, phone = args
    if name in book:
        if phone.isdigit():
            book[name] = phone
            return "Contact updated."
        else:
            return "Contact cannot be updated. Phone must consist of numbers."
    else:
        return "Contact not found."


@input_error
def show_contact(args, book):
    name = args[0]
    return book[name]


@input_error
def show_all(book):
    if book:
        for name, phone in book.items():
            if name != "" and phone != "":
                print(f"Name - {name}, phone - {phone}")
            else:
                continue
    else:
        return "No book."

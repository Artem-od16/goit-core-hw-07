from .decorators import input_error
from .general.get_upcoming_birthdays import get_upcoming_birthdays


@input_error
def add_birthday(args, book):
    date = args[0]
    book["birthday"] = date
    return "Birthday added."


@input_error
def show_birthday(args, book):
    date = args[0]
    return book[date]


@input_error
def birthdays(book):
    if len(book) != 0:
        get_upcoming_birthdays(book)

    else:
        return "No contacts."

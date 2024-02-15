from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not args:
            return "Invalid command. Provide arguments."
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return str(ve)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."

    return inner

from datetime import datetime, timedelta

current_datetime = datetime.now()
current_year = current_datetime.year


def get_upcoming_birthdays(users: list):
    upcoming_birthdays = []

    if not users:
        return "No birthdays yet."

    for person in users:
        date = person.birthday
        datetime_object = datetime.strptime(date, "%Y.%m.%d")
        day = datetime_object.weekday()

        if day == 6:
            day_interval = timedelta(days=2)
            datetime_object = datetime_object + day_interval
        elif day == 7:
            day_interval = timedelta(days=1)
            datetime_object = datetime_object + day_interval

        target_day = datetime_object.day

        # Calculate the number of days until the next birthday
        days_until_birthday = (datetime_object - current_datetime).days

        # Check if the birthday is within the next week
        if 0 <= days_until_birthday <= 7:
            date = str(current_year) + date[4:8] + str(target_day)

        person.congratulation_date = date
        upcoming_birthdays.append(person)

    return f'List of users to be congratulated by day in the coming week - {[person.congratulation_date for person in upcoming_birthdays]}'
from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Підготовка структури даних для зберігання імен по днях тижня
    birthdays_per_week = defaultdict(list)

    # Отримання поточної дати
    today = datetime.today().date()

    # Перебір користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Оцінка дати на цей рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Порівняння з поточною датою
        delta_days = (birthday_this_year - today).days

        # Визначення дня тижня
        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
            # Вихідні переносимо на понеділок
            if day_of_week in ['Saturday','Sunday']:
                day_of_week = 'Monday'

            birthdays_per_week[day_of_week].append(name)

    # Виведення результату
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

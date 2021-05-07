import datetime

months = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь",
]

today = datetime.datetime.today()
today_month = months[today.month-1]
today_day = str(today.day)

after_21_days = datetime.date(today.year, today.month, today.day) + datetime.timedelta(days=21)
after_month = months[after_21_days.month-1]
after_day = str(after_21_days.day)
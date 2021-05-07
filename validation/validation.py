import re

from aiogram import types

def proccess_validate_name(message: types.Message)->bool:
    match = re.findall("^[А-ЯЁA-Zа-яёa-z-]{2,20}$", message.text)
    if match:
        return False
    return True


def proccess_validate_month(message: types.Message)->bool:
    months = [
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь",
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
    ]
    if message.text not in months:
        return True
    return False


def proccess_validate_day(message: types.Message)->bool:
    if message.text.isdigit() and int(message.text) <= 31:
        return False
    return True


def proccess_validate_date(date: str)->"bool|list":
    match = date.split(".")
    if len(match) == 3:
        day = match[0]
        month = match[1]
        year = match[2]
        if day.isdigit() and month.isdigit() and year.isdigit:
            if int(day) < 1 or int(day) > 31:
                return False
            if int(month) < 1 or int(month) > 12:
                return False
            if len(year) != 4 or int(year[0:3]) != 202:
                return False
        return [day, month, year]
    else:
        return False


def proccess_validate_new_event(message)->"bool|list":
    matchx = re.findall("^\/new (.*) \"(.*)\" \"(.*)\"", message.text)
    match = re.findall("^\/new (.*) «(.*)» «(.*)»", message.text)
    if matchx == [] and match == []:
        return False
    elif matchx != []:
        return list(matchx[0])
    elif match != []:
        return list(match[0])


def proccess_validate_phone(message):
    match = re.findall(r"^\+375[0-9]{9}", message)
    if match:
        return False
    return True
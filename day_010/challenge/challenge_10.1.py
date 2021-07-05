# 10.1 Days in Month


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month <= 0:
        return "Invalid month entered"
    elif is_leap_year(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]


# 🚨 Do NOT change any of the code below
input_year = int(input("Enter a year: "))
input_month = int(input("Enter a month: "))
days = days_in_month(input_year, input_month)
print(days)

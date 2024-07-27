
def is_leap_year (year):
    leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
        else:
            leap_year = True
    return leap_year

def get_amount_days (month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        amount_days = 31
    elif month in {4, 6, 9, 11}:
        amount_days = 30
    else:
        if leap_year:
            amount_days = 29
        else:
            amount_days = 28
    return amount_days


total_amount_days = 1
n = 0

for year in range(1900, 2001):
    leap_year = is_leap_year(year)

    for month in range(1, 13):
        amount_days = get_amount_days(month)
        total_amount_days += amount_days

        if total_amount_days % 7 == 0:
            if year != 1900:
                n +=1

print(n)
import re

stringDates = '10/01/2010abc31/02/2020def31/04/2021hij60/55/2119klm29/02/2025nop29/02/2400'

dateRegex = re.compile(r'''
    (([0-2][0-9]|3[0-1])  # Day
    /
    (0[1-9]|1[0-2])           # Month
    /
    ([1-2][0-9]{3}) )               # Year
''', re.VERBOSE)


print(dateRegex.findall(stringDates))

def isValidDate(dates):
    for group in dateRegex.findall(dates):
        print(group[0])
        day = int(group[1])
        month = int(group[2])
        year = int(group[3])

        if month in [4, 6, 9, 11] and day > 30:
            print('Invalid Date - April, June, Sept. and Nov. have 30 days')
        elif month == 2 and year % 400 == 0 and day <= 29:
            print('Valid Date')
        elif month == 2 and year % 4 != 0 and not year % 100 == 0 and day > 29:
            print('Invalid Date - Leap Years have 29 days in February ' + str(year))
        elif month == 2 and day > 28:
            print('Invalid Date - February has 28 days in ' + str(year))
        elif day > 31:
            print('Invalid Date - More than 31 days')
        else:
            print('Valid Date')

isValidDate(stringDates)

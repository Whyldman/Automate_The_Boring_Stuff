import re

dates = '10/01/2010abc31/01/2020def31/04/2021hij60/55/2119'

dateRegex = re.compile(r'''
    (([0-2][0-9])|(3[0-1])) # Day
    //
    ((0[1-9])|(1[0-2]))     # Month
    //
    ([1-2][0-9]{3}) # Year
''', re.VERBOSE)

print(dateRegex.findall(dates))

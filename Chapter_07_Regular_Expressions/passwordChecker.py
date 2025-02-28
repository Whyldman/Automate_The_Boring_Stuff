short = 'abc123'
lower = 'abcdefg12'
upper = 'ABCDEFG1'
noNumber = 'abcDEFghi'
password = 'Password1'

import re

def passwordChecker(password):
    hasUpper = re.compile(r'[A-Z]')
    hasLower = re.compile(r'[a-z]')
    hasNumber = re.compile(r'\d')

    if hasUpper.search(password) is None:
        print('Needs Uppercase Letter')
    if hasLower.search(password) is None:
        print('Needs Lowercase Letter')
    if hasNumber.search(password) is None:
        print('Needs a number')
    if len(password) < 8:
        print("Password needs to be at least 8 characters")
    if len(password) >= 8 and hasUpper.search(password) is not None and hasLower.search(password) is not None and hasNumber.search(password) is not None:
        print('Password Accepted')

passwordChecker(short)
passwordChecker(upper)
passwordChecker(lower)
passwordChecker(noNumber)
passwordChecker(password)
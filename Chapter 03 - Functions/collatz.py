import time
def collatz(number):
    if number % 2 == 0:
        print(str(number) + ' divided by 2 and floored is ' + str(number // 2))
        return number // 2
    elif number % 2 == 1:
        print(str(number) + ' times 3 plus 1 is ' + str(3 * number + 1))
        return 3 * number + 1


print('Give me an integer.')

try:
    input_integer = int(input())
except ValueError:
    print("That's not a number")

while input_integer != 1:
    print('Working on the next step in the Collatz sequence')
    time.sleep(0.5)
    input_integer = collatz(input_integer)


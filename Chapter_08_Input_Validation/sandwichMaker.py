import pyinputplus as pyip

bread = pyip.inputMenu(choices = ['white', 'wheat', 'sourdough'],
                  prompt = 'What type of bread would you like?\n')

protein = pyip.inputMenu(choices=['chicken', 'turkey', 'ham', 'tofu'],
                         prompt='What type of protein?\n')

wantsCheese = pyip.inputYesNo("Do you want cheese?\n")

if wantsCheese == "yes":
    cheese = pyip.inputMenu(choices=['cheddar', 'Swiss', 'mozzarella'],
                             prompt='What type of cheese?\n')
else:
    cheese = 'none'

wantsMayo = pyip.inputYesNo("Do you want mayo?\n")
wantsMustard = pyip.inputYesNo("Do you want mustard?\n")
wantsLettuce = pyip.inputYesNo("Do you want lettuce?\n")
wantsTomato = pyip.inputYesNo("Do you want tomato?\n")

if wantsMayo == "yes":
    mayo = 1
else:
    mayo = 0

if wantsMustard == "yes":
    mustard = 1
else:
    mustard = 0

if wantsLettuce == "yes":
    lettuce = 1
else:
    lettuce = 0

if wantsTomato == "yes":
    tomato = 1
else:
    tomato = 0

prices = {
    'breads': {
        'white': 2,
        'wheat': 2,
        'sourdough':3
    },
    'proteins': {
        'chicken': 3,
        'turkey': 4,
        'ham': 2,
        'tofu': 3
    },
    'cheeses': {
        'none': 0,
        'cheddar': 1,
        'Swiss': 1,
        'mozzarella': 1
    },
    'mayo': .5,
    'mustard': .5,
    'lettuce': .5,
    'tomato': 1
}

price = (prices['breads'][bread] +
         prices['proteins'][protein] +
         prices['cheeses'][cheese] +
         (prices['mayo'] * mayo) +
         (prices['mustard'] * mustard) +
         (prices['lettuce'] * lettuce) +
         (prices['tomato']) * tomato)


print(f"That'll be ${price}, please.")

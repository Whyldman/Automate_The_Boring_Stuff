import pyinputplus as pyip

bread = pyip.inputMenu(choices = ['white', 'wheat', 'sourdough'],
                  prompt = 'What type of bread would you like?\n')

protein = pyip.inputMenu(choices=['chicken', 'turkey', 'ham', 'tofu'],
                         prompt='What type of protein?\n')

wantsCheese = pyip.inputYesNo("Do you want cheese?")

if wantsCheese == "yes":
    cheese = pyip.inputMenu(choices=['cheddar', 'Swiss', 'mozzarella'],
                             prompt='What type of cheese?\n')
else:
    cheese = 'none'

wantsMayo = pyip.inputYesNo("Do you want mayo?\n")
wantsMustard = pyip.inputYesNo("Do you want mustard?\n")
wantsLettuce = pyip.inputYesNo("Do you want lettuce?\n")
wantsTomato = pyip.inputYesNo("Do you want tomato?\n")

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
         prices['mayo'] +
         prices['mustard'] +
         prices['lettuce'] +
         prices['tomato'])


print(f"That'll be ${price}, please.")

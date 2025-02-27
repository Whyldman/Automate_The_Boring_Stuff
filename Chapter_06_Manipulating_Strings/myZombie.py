import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # High Risk:
        # brains = 0
        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']
        #
        #     if random.randint(1,10) > 2:
        #         diceRollResults = zombiedice.roll() # roll again
        #     else:
        #         break

        # Randomly decide from 1 to 4 rolls unless 2 shotguns are rolled
        shotguns = 0
        rolls = 0
        max_rolls = random.randint(1,4)
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns == 2:
                break
            elif rolls < max_rolls:
                diceRollResults = zombiedice.roll()  # roll again
                rolls += 1
            else:
                break


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='Unpredictable Low Risk'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)

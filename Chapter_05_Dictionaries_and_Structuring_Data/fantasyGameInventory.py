stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print("  " + str(v) + " " + k)
    print("Total number of items: " + str(item_total))

dragonLoot = ['gold coin', 'dagger', 'gold coin',  'gold coin', 'ruby']

def addToInventory(inventory, added_items):
    for i in range(len(added_items)):
        item = added_items[i]
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1

displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)

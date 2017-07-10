stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(' - Torch ' + str(displayInventory(stuff, 'torch')))
        print("Total number of items: " + str(item_total))

displayInventory(stuff)

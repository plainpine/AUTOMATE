'''
Chapter 5 Dictionaries and Structuring Data

Fantasy Game Inventory

You are creating a fantasy video game. The data structure to model the
player’s inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value
detailing how many of that item the player has. For example, the dictionary
value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.


List to Dictionary Function for Fantasy Game Inventory

Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot.
The addToInventory() function should return a dictionary that represents the
updated inventory.

'''

stuff = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}

inv = {'金貨': 42, 'ロープ': 1}
dragonLoot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']

def displayInventory(inventory):
    print("持ち物リスト:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v

    print("アイテム総数: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

displayInventory(stuff)

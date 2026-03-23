"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    
    inventory = {}
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
 
    return inventory




def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
        
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items: #遍历库存
        if inventory.get(item, 0) > 0:
            inventory[item] -= 1 #如果大于0，取出并减一
                                                     #否则保持不变
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, None) #移除字典里的这个物品，如果没这个物品返回空值
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    result = []
    
    # 2. 遍歷字典裡的每一組「鍵」和「值」
    for name, count in inventory.items():
        # 3. 只有數量大於 0 的才要
        if count > 0:
            result.append((name, count))
    return result
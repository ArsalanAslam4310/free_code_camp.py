
def display_inventory(inventory):
    print('inventory:')
    item_total=0

    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

dictionary ={'rope':1,'torch':6,'gold_coins':42,'dagger':1,'arrow':12}
display_inventory(dictionary)

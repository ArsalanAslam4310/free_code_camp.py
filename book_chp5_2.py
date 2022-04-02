from hsxbz import display_inventory

def add_to_inventory(inventory,add_items):
    sum =0

    for value in add_items:
        inventory.setdefault(value,0)
        inventory[value]+=1
    return inventory


inv={'gold_coin':42,'rope':1}
dragon_loot=['gold_coin', 'dagger','gold_coin','gold_coin','ruby','rope']
add_to_inventory(inv,dragon_loot)
display_inventory(inv)

      

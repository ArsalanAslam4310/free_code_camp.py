def total_brought(guests,item):
    num_brought=0
    for k, v in guests.items():
        num_brought += v.get(item,0)
    return num_brought

all_guest={'alice':{'apples':5,'banana':12},
            'bob':{'ham_sandwiches':3, 'apples':2},
            'carol':{'cups':3,'apple pies':1}}
print('number of thing being brought:')
print(' - apples ' + str(total_brought(all_guest,'apples')))
print(' - cups ' + str(total_brought(all_guest, 'cups')))
print(' - cakes ' + str(total_brought(all_guest, 'cakes')))
print(' - ham_sandwiches ' + str(total_brought(all_guest, 'ham_sandwiches')))
print(' - apple pies  ' + str(total_brought(all_guest, 'apple pies')))
print(' - banana ' + str(total_brought(all_guest, 'banana')))

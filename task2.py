import random

def generate_list(begin, end, quantity):
    list = []
    for i in range(quantity):
        list.append(round(random.uniform(begin, end), 2))
    return list

def get_winner_list(list1, list2):
    list = []
    length1 = len(list1)
    length2 = len(list2)
    min_len = length1
    if length2 < min_len:
        min_len = length2
    for i in range(min_len):
        if list1[i] > list2[i]:
            list.append(list1[i])
        else:
            list.append(list2[i])
    return list

band1 = []
band2 = []
winners = []
band1 = generate_list(5, 10, 20)
print(band1)
band2 = generate_list(5, 10, 20)
print(band2)
winners = get_winner_list(band1, band2)
print(winners)
# Реализуйте алгоритм перемешивания списка

import random

def get_list(num, lft, rght):
    return [random.randint(lft, rght) for i in range(num)]

def shuffle_list(lst):
    return random.shuffle(lst)

num = 5
lft = -30
rght = 30

mylist = get_list(num, lft, rght)
print(mylist)
shuffle_list(mylist)
print(mylist)
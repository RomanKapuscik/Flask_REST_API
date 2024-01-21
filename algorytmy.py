import json
import time
import numpy as np

with open('imiona.json') as f:
    data = json.load(f)


#   zadanie 2
def find_name_json(name: str) -> str:
    start = time.time()
    lines = 0
    for x in data['data']:
        lines += 1
        if x[11] == name.upper():
            print(x, f'\nLiczba lini kodu: {lines}')
            break
    end = time.time()
    total = end - start
    return 'Wyszukiwanie JSON czas: ' + str(total)


# print(find_name_json('Julian'))


# zadanie 3
def create_hispanic_names_list() -> list:
    hispanic_names = list()
    for x in data['data']:
        if x[10] == "HISPANIC":
            hispanic_names.append(x[11])
    return hispanic_names


def find_name_list(name: str) -> str:
    hispanic_names = create_hispanic_names_list()
    start = time.time()
    for x in hispanic_names:
        if x == name.upper():
            print(x)
            break
    end = time.time()
    total = end - start
    return 'Wyszukiwanie list czas: ' + str(total)


#   zadanie 4
def find_name_set(name: str) -> str:
    hispanic_names = create_hispanic_names_list()
    for x in data['data']:
        if x[10] == "HISPANIC":
            hispanic_names.append(x[11])

    hispanic_names_set = set(hispanic_names)

    start = time.time()
    for x in hispanic_names_set:
        if x == name.upper():
            print(x)
            break
    end = time.time()
    total = end - start
    return 'Wyszukiwanie set czas: ' + str(total)


def buble_sort(data):
    n = len(data)
    while n > 0:
        for x in range(n - 1):
            if data[x] > data[x + 1]:
                data[x], data[x + 1] = data[x + 1], data[x]
        n -= 1
    return data


def generatot_liczb_losowych(n: int):
    return np.random.rand(n, 1)


number_of_random = 100
liczby_losowe = generatot_liczb_losowych(number_of_random)

# print(type(list(buble_sort(liczby_losowe))))




# start = time.time()
# print(buble_sort(hispanic_names))
# end = time.time()
# print(end - start)

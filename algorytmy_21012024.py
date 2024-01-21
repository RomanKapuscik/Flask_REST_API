import json
from typing import List

with open('friends.json') as f:
    data = json.load(f)

def find_friends_json(name1, name2):
    for x in data['who_know_who']:
        if name1 == x:
            # print(data['who_know_who'][name1])
            if name2 in data['who_know_who'][name1]:
                return True
            return False


# print(find_friends_json('Mikolaj', 'Kamil'))

def find_who_has_things(thing):
    for x in data['who_has_what']:
        if x == thing:
             return data['who_has_what'][thing]


def does_he_has_it(name, thing):
    return name in find_who_has_things(thing)

def looking_for_thing_with_friends(name: str, item):
    people_wit_the_thing = []
    for person in find_who_has_things(item):
        if find_friends_json(person, name):
            people_wit_the_thing.append(person)

    if people_wit_the_thing:
        return people_wit_the_thing

    for person in find_who_has_things(item):
        for x in data['who_know_who'][person]:
            if find_friends_json(x, name):
                return x, person


def looking_for_things_with_friends(name: str, items: List[str]):
    result = dict()
    for item in items:
        result[item] = [looking_for_thing_with_friends(name, item)]
    return result


print(looking_for_things_with_friends('Magda', ['kamera', 'statyw']))
# print(looking_for_things_with_friends('Magda', 'statyw'))
# print(looking_for_things_with_friends('Daniel', 'statyw'))

# print(does_he_has_it('Magda', 'kamera'))



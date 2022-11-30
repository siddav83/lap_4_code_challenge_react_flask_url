import random

def short_url_creator():
    random_index = ""
    array = [1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"] 
    for num in range(0,6):
        random_index += str(random.choice(array))
    return random_index     
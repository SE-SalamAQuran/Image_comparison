import json
from key_generator.key_generator import generate

#This file generates mock api keys

key = generate(seed = 990)
print(key.get_key())  

key_custom = generate(5, '-', 3, 3, type_of_value = 'hex', capital = 'none', extras = ['%', '&', '^'], seed = 42).get_key()
print(key_custom)  

key_custom_2 = generate(2, ['-', ':'], 3, 10, type_of_value = 'char', capital = 'mix', seed = 17).get_key()
print(key_custom_2)  

keys = {}

f = open("keys.json", 'r')
# returns JSON object as  a dictionary 
data = json.load(f) 
print(data['secret_keys'])
keys['secret_keys'] = data['secret_keys']

if key.get_key() in data:
    print("Key Duplication")
    exit()
else:
    keys['secret_keys'].append({
        "key": key.get_key()
    }) 
    keys['secret_keys'].append({
        "key": key_custom
    })
    keys['secret_keys'].append({
        "key": key_custom_2
    })
    
with open("keys.json", 'w') as outfile:
    json.dump(keys, outfile)


def validate_key(input_key):
    if input_key not in keys['secret_keys']:
        return False
    else:
        return True

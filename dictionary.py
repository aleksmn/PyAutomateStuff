##myCat.keys() # dict_keys(['size', 'color'])
##myCat.values() # dict_values(['fat', 'gray'])
##list(myCat.keys()) # ['size', 'color']

import pprint
message = 'It was a bright cold day in April, and the clack'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

#text = pprint.pformat(count)
#pprint.pprint(count)

# Sort Dictionary

sorted_count_by_key = {k: v for k, v in sorted(count.items(), key=lambda item: item[0])}
sorted_count_by_value = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}
print(sorted_count_by_key)
print(sorted_count_by_value)

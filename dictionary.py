myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

#keys(), values(), items() -- Dictionary Methods

message = 'It was a bright cold day in April, and th clocks were strinking 13'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1
    
print(count)

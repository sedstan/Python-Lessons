message = 'It was a bright cold day in April, and the clock was striking thriteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

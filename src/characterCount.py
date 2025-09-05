message = 'It was a bright cold day in April,' \
          'and the clocks were striking thirteen.'
count = {}
for character in message:
   count.setdefault(character, 0) # ①
   count[character] = count[character] + 1 # ②
print(count)

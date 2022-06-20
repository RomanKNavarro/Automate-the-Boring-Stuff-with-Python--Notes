# characterCount.py (without 'pprint' module)


# This program counts the number of times a character is used in a string using the setdefault() method.

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:                       # This iterates over every character in the string
    count.setdefault(character, 0)              # The setdefault() method will add the characters to the 'count' dictionary, as well as the number of times they appear.
    count[character] = count[character] + 1     # this expression will add 1 to the value of a character for every time it appears in the string.

print(count)                                    # prints the list.





# The same program as the previous, but the 'pprint' module is imported. This will cause the dictionary to be printed vertically, resulting in an easier-to-read display.
print()



import pprint
message = 'It was a bright cold day in April,and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
companies = [{'BIGDIG':{'gold': 0}}, {'BULK_METALS':{'copper': 0}}, {'MINERAL':{'marble': 0}}]

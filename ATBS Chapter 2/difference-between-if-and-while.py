# swordfish.py

print('swordfish.py:')
print()

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue  # 'continue' means to reloop if "name != 'Joe'" is true, not to continue with the rest of the code
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':  # if password is not swordfish, the program will reloop from the beginning
        break
print('Access granted')

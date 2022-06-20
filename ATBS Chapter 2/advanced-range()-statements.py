# advanced range() arguments
print('advanced range() arguments:')
print()

for i in range(12, 16):  # counts from 12 up to the numbers inbetween 16
    print(i)

print()
for i in range(0, 10, 2):  # The third number is called the 'step argument'. It determines by how much each iteriation is increased.
    print(i)               # In this case, each iteriation will go up by 2. So, the sequance would be '2, 4, 6, 8'

print()
for i in range(5, -1, -1):  # range() also counts down with negative numbers
    print(i)

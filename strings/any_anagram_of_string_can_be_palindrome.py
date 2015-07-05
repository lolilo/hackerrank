string = raw_input()
 
found = True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
d = {}
for char in string:
    if d.get(char):
        d[char] += 1
    else:
        d[char] = 1

even_count = 0
odd_count = 0
for char in d.keys():
    if d[char] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if odd_count > 1: # I don't even need even_count, actually.
    found = False

if not found:
    print("NO")
else:
    print("YES")

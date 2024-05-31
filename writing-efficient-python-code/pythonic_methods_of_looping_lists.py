names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
i = 0
new_list = []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
    
# Print the list using a non-pythonic approach
print(new_list)

# Print the list pythonically by looping over the contents of names 
# without using an index variable.
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)

# Use a list comprehension:
best_list = [name for name in names if len(name) >= 6]
print(best_list)
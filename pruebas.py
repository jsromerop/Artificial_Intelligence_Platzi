numbers = range(10)

new_dict_for = {}

for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2

print(new_dict_for)

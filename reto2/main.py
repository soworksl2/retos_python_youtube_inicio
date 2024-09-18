my_input = [5, 3, 1, 2, 4]

my_input_ordered = sorted(my_input)

output = []

take_minor = True
while len(my_input_ordered) > 0:
    if take_minor:
        value = my_input_ordered.pop(0)
    else:
        value = my_input_ordered.pop(-1)

    output.append(value)
    take_minor = not take_minor

print(output)

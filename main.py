def check_numbers(numbers):
    new_list = []
    for i in numbers:
        if i > 0:
            new_list.append(i)
        else:
            new_list.append(0)
    return new_list

print(check_numbers([5, 3, -5, 3, -7, -3, 1, -8]))

#[5, 3, 0, 3, 0, 0, 1, 0]

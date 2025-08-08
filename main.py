set_one = {1, 3, 2, 5, 4}
set_two = {5, 4, 1, 6, 3}

# The onion operation creates a new set that combines unique values from both sets.
print(set_one | set_two)

# The intersection operation creates a new set with unique values that only exist in both sets.
print(set_one & set_two)

# The difference operation creates a new set with unique values that only exist in the first set.
print(set_one - set_two)
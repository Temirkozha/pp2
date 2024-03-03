def all_true(tup):
    return all(tup)

my_tup = (True, True, True, True)
print("All elements of the my_tup are true:", all_true(my_tup))

my_tup = (True, False)
print("All elements of the my_tup are true:", all_true(my_tup))

my_tup = (False, False, False)
print("All elements of the my_tup are true:", all_true(my_tup))
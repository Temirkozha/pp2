def count(my_str):
    upper_count = sum(1 for char in my_str if char.isupper())
    lower_count = sum(1 for char in my_str if char.islower())
    return upper_count, lower_count

inp_str = str(input())
upper, lower = count(inp_str)
print("Count upper case:", upper)
print("Count lower case:", lower)
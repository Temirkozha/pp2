from functools import reduce

def myltp(num):
    res = reduce(lambda x, y: x * y, num)
    return res

num_list = [2, 11, 1, 2]
print("My List:", num_list)
print("Result:", myltp(num_list))
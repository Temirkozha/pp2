def Pol(my_str):
    my_str = my_str.lower()
    my_str = my_str.replace(" ", "")
    return my_str == my_str[::-1]

my_str = str(input())
if Pol(my_str):
    print("This string is polindrom")
else:
    print("This string is not polindrom")
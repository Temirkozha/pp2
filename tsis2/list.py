#1
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#2
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#3
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#4
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#6
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#7
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#8
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#9
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#10
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#11
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#12
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#13
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

        
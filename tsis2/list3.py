#1
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#2
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#4
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#5
newlist = [x for x in fruits if x != "apple"]

#6
newlist = [x for x in range(10)]

#7
newlist = [x for x in range(10) if x < 5]

#8
newlist = [x.upper() for x in fruits]

#9
newlist = ['hello' for x in fruits]

#10
newlist = [x if x != "banana" else "orange" for x in fruits]  
#1
def myfunction():
  pass

#2
def my_function(x, /):
  print(x)

my_function(3)

#3
def my_function(x):
  print(x)

my_function(x = 3)

#4

def my_function(*, x):
  print(x)

my_function(x = 3)

#5
def my_function(x):
  print(x)

my_function(3)

#6
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#7
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


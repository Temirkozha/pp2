"""
x = куры, y = кролики
2x + 4y = legs
x + y = heads
"""
def solve(numheads, numlegs):
    for i in range(numheads + 1):
        y = numheads - 1
        if 2 * x + 4 * y == numlegs:
            return x, y
    return None

x = int(input())
y = int(input())
res1 = solve(x, y)
print(res1)

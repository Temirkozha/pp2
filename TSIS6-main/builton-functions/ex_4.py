import math
import time

def calc(num, millisec):
    time.sleep(millisec / 1000)
    square = math.sqrt(num)
    print(f"Square root of {num} after {millisec} milliseconds is {square}")

num = int(input())
millisec = int(input())

calc(num, millisec)
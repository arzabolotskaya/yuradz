
import math
print("Входные данные: ")
a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2 
v = p * (p-a) * (p-b) * (p-c)
s = math.sqrt(v)
print(s)

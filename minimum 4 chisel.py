def min4(a, b, c, d):
    x = min(a, b)
    y = min(c, d)
    m = min(x, y)
    
    return m
    
print("Входные данные:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))

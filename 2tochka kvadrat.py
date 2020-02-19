def IsPointInSquare(x, y):
    return (-1 < x < 1)&(-1 < y < 1)

print("Входные данные: ")
a = float(input())
b = float(input())

if IsPointInSquare == True:
    print("YES")
else:
    print("NO)

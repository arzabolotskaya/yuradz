
def  IsPointInCircle(x, y, xc, yc, r):
    
    return (x - xc)**2 + (y - yc)**2 < r**2

print("Входные данные: ")
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

if IsPointInCircle(x, y, xc, yc, r) == False:
    print("NO")
else:
    print("YES")

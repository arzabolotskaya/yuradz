
def  IsPrime(n):      
    return ((n%n)==0)


print("Входные данные: ")
n = int(input())
if IsPrime(n) == True:
    print("YES")
else:
    print("NO")

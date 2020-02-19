def summ(a, b):
    if(b==0):
        return a
    else:
        return(1+summ(a,b-1))

print("Входные данные: ")
a = int(input())
b = int(input())
print(summ(a, b))

def  MinDivisor(n):
    mdlist = []
    for i in range(2, n+1):
        if n%i==0:
            mdlist.append(i)
    mdlist.sort()
        
    return mdlist[0]

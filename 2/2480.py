#주사위
a,b,c=map(int, input().split())
M=int()
if a==b :
    if b==c :     
        M=10000+(a*1000)
        print(M)
    else :
        M=1000+(a*100)
        print(M)
else :
    if a==c or b==c: 
        M=1000+(c*100)
        print(M)
    else :
        M=max(a,b,c)*100
        print(M)

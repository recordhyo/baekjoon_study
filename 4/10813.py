N,M=map(int, input().split())
li = list(range(1,N+1))
temp = int

for _ in range(M) :
    i,j = map(int,input().split())
    temp=li[i-1]
    li[i-1]=li[j-1]
    li[j-1]=temp
for x in range(N) :
    print(li[x],'',end="")
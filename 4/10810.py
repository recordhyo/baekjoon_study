#바구니에 공넣기 
N,M=map(int, input().split())
li = [0]*N

for _ in range(M) :
    x,y,z = map(int,input().split())
    for i in range(x,y+1) :
        li[i-1]=z
for i in range(N) :
    print(li[i],'',end="")

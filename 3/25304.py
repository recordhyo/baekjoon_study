#영수증계산
M=int(input())
n=int(input())
for i in range(n) :
    a,b=map(int,input().split())
    M=M-(a*b)
if M==0 :
    print("Yes")
else :
    print("No")

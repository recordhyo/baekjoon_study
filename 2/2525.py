#오븐시계
H,M=map(int, input().split())
T=int(input())
A=M+T

if A<60 : print(H,A)
else :
    H=H+(A//60)
    if H>=24 : print(H-24,A%60)
    else : print(H,(A%60))

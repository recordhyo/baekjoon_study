#알람시계 45분일찍 맞추기
H,M=map(int, input().split())
if M>=45 :
    print(H, M-45)
else :
    if H==0 : print("23", 60+(M-45))
    else : print(H-1, 60+(M-45))

li1 = list(range(1,31))
li2 = [0]*28
for i in range(28) :
    li2[i] = int(input())
    
for j in range(30) :
    if li2.count(li1[j])==0 :
        print(li1[j])
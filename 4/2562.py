li = list(range(9))
for i in range(9):
    li[i] = int(input())
    
print(max(li))

for i in range(9) :
    if max(li) ==li[i] :
        print(i+1)
    else :
        continue
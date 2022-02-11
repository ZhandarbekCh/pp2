jp=input().split()
l=[]
for i in range (len(jp)):
    l.append(int(jp[i]))
max_jp=0
for i in range (len(jp)):
    if max_jp>=i:
        if l[i]+i>=len(jp)-1:
            print(1)
            exit()
        elif l[i]+i>max_jp:
            max_jp=l[i]+i
    else:
        break
if max_jp<len(jp)-1:
    print(0)
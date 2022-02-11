d = dict() 
max = 0 

for i in range(int(input())): 
    a = list(map(str, input().split())) 

    if a[0] not in d: 
         d[a[0]] = int(a[1]) 

    else: 
        d[a[0]] += int(a[1]) 

for b in d.values(): 

    if b > max: 
        max = b 
        
for i, j in sorted(d.items()): 
    if j == max: 
        print(i, 'is lucky!') 

    else: 
        print(f'{i} has to receive {max-j} tenge')
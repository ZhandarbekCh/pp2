data = [] 

for i in range(10**5): 
    a = input().split() 
    if a[0] == '0': 
        break 

    data.append(a) 
data.sort(key = lambda x : (x[2], x[1], x[0])) 

for i in data: 
    print(*i)
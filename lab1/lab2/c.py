a = int(input()) 
b = [[0 for i in range(a)] for j in range(a)] 

for i in range(a): 
    for j in range(a): 
        if i == j: 
            b[i][j] = i*j 
        elif i == 0: 
            b[i][j] = j 
        elif j == 0: 
            b[i][j] = i 

for i in range(a): 
    for j in range(a): 
        print(b[i][j], end=' ') 
        
    print()
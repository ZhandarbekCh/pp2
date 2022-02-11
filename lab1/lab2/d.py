a = int(input()) 
b = [['.' for i in range(a)] for j in range(a)] 

if a % 2 == 1: 
    for i in range(a): 
        for j in range(a): 
            if i+j+1 >= a: 
                b[i][j] = '#' 
else: 
    for i in range(a): 
        for j in range(a): 
            if j - i <= 0: 
                b[i][j] = '#' 
                
for i in range(a): 
    for j in range(a): 
        print(b[i][j], end='') 
    print()
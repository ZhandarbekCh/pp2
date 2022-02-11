x = input().split() 
for i in range(len(x)): 
    for j in range(len(x[i])): 
        if x[i][j] in '?.,!-;:"' or x[i][j] in "'": 
            x[i] = x[i].replace(x[i][j], '') 
print(len(set(x)), *sorted(set(x)), sep='\n')
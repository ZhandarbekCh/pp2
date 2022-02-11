n =int(input())

for i in range(len(n)):
    for j in range(len(n[i])):

        if n[i][j] in '?.,!-;:"' or n[i][j] in "'":
            n[i] = n[i].replace(n[i][j], '')
            
print(len(set(n)), *sorted(set(n)), sep='\n')
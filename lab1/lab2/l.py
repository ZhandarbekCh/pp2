n, stack, cl, op = input(), [], '})]', '{([' 
for i in n:

    if i in op: 
        stack.append(i) 

    elif i in cl: 
        pos = cl.index(i) 

        if len(stack) != 0 and stack[len(stack) - 1] == op[pos]: 
            stack.pop() 

        else: 
            print('No') 
            exit(0) 
            
if len(stack) == 0: 
    print('Yes') 
else: 
    print('No')
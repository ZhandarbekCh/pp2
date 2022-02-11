def strong (a): 
    upp, low, digit = False, False, False 
    for i in a: 
        if ord(i) >= 48 and ord(i) <= 57: 
            digit = True 
        elif ord(i) >= 65 and ord(i) <= 90: 
            upp = True 
        elif ord(i) >= 97 and ord(i) <= 122: 
            low = True 
    return upp and low and digit 
b, cnt = [], 0 
for i in range(int(input())): 
    a = input() 
    if strong(a) and a not in b: 
        cnt += 1 
        b.append(a) 
print(cnt, *sorted(b), sep='\n')
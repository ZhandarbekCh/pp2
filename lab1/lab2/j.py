def strong(b):
    upper, lower, digit = False, False, False
    for i in b:
        if ord(i) >= 48 and ord(i) <= 57:
            digit = True
        elif ord(i) >= 65 and ord(i) <= 90:
            upper = True
        elif ord(i) >= 97 and ord(i) <= 122:
            lower = True
        return upper and lower and digit
a, count = [], 0
for i in range(int(input())):
    b = input()

    if strong(b) and b not in a:
        count +=1
        a.append(b)
print(count, *sorted(a), sep='\n')
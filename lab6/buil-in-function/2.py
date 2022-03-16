t = input()
up = 0
low = 0
for i in t:
    if ord(i) >= 65 and ord(i) <= 90:
        up+=1
    elif ord(i) >= 97 and ord(i) <= 122:
        low+=1
print(up, low)
        

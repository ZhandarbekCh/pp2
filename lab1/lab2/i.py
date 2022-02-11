n, b, b1 = int(input()), [], []
for i in range(n):
    
    a = list(input().split())
    x = int(a[0])

    if len(a) == 1:
        b1.append(b[0])
        b.pop(0)

    if x == 1:
        b.append(a[1])
print(*b1)
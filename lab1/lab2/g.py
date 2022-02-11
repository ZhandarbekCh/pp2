dem, hun, amount = dict(), dict(), 0

for i in range(int(input())):
    d=list(input().split())

    if d[1] not in dem:
        dem[d[1]] = 1

    else:
        dem[d[1]] +=1

for i in range(int(input())):
    h=list(input().split())

    if h[1] not in hun:
        hun[h[1]] = int(h[2])

    else:
        hun[h[1]] += int(h[2])
        
for i in dem.keys():

    if i in hun.keys():
        dem[i] -= hun[i]

    if dem[i] > 0:
        amount += dem[i]

print("Demons left:", amount)

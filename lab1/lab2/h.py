def closest_point(point):
    global x, y
    return (x - point[0])**2+(y - point[1])**2

x, y = map(int, input().split())
coords = []

for _ in range(int(input())):
    coords.append(tuple(map(int, input().split())))
coords.sort(key=closest_point)

for i in coords:
    print(*i)
def solve(numheads, numlegs):
    for rabhead in range(numheads):
        chicken=numheads-rabhead
        if (chicken*2+rabhead*4==numlegs):
            print(chicken, rabhead)
            break

x=input().split()
solve(int(x[0]), int(x[1]))

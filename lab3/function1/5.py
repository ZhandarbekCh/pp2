def perm(s):
    import itertools 
    perm_set = itertools.permutations(s) 
    for val in perm_set: 
        print(val)
    

s = input()
perm(s)


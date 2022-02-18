from re import L


def unique_list(l):
  x = []
  for a in l:
    if int(a) not in x:
      x.append(int(a))
  return x

l=(input().split())
print(unique_list(l))

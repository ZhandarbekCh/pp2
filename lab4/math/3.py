from math import floor, tan, pi
n_of_s=int(input("Input number of sides: "))
l=float(input("Input the length of a side: "))
area=floor(n_of_s * (l**2)/(4 * tan(pi / n_of_s)))
print("The area of the polygon is:",area)

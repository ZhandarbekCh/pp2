t = input()
s = t[::-1]
if hash(t) == hash(s):
    print("It is polindrome")
else:
    print("It is not palindrome")

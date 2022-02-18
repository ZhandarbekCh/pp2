def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
    return False
x=int(input())
nums=[]
for i in range(x):
    y=int(input())
    nums.append(y)
if (spy_game(nums)):
    print("True")
else:
    print("False")

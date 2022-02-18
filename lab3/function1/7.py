def has__33(nums):
    for i in range(len(nums)-1):
        if (nums[i]==3 and nums[i+1]==3):
            return True
    return False


x=int(input())
nums=[]
for i in range(x):
    y=int(input())
    nums.append(y)
if (has__33(nums)):
    print("True")
else:
    print("False")

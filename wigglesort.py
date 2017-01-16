def wiggle_sort(nums):
    if nums==None or len(nums)<=1:
        return nums
    
    startSmaller=True
    
    for i in range(0, len(nums)-1):
        if startSmaller:
            if nums[i]>=nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        else:
            if nums[i]<=nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        startSmaller = (not startSmaller)
        
    return nums

def wiggleSort(nums):
    for i in range(len(nums)):
        nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)
    return nums

def wiggleSort2(nums):
    for i in range(1, len(nums)):
        if (i % 2) ^ (nums[i] > nums[i - 1]):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums
    
if __name__ == "__main__":
    nums = []
    nums.append(1)
    nums.append(5)
    nums.append(1)
    nums.append(1)
    nums.append(6)
    nums.append(4)
    print(wiggle_sort(nums))
    print(wiggleSort(nums))
    print(wiggleSort2(nums))

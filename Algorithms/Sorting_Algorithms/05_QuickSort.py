def quick_sort(nums, low, high):
    if low < high:
        mid = partition(nums, low, high)

        quick_sort(nums, low, mid -1)
        quick_sort(nums, mid + 1, high)



def partition(nums, low, high):
    pivot = high
    i = low - 1
    for j in range(low, high):
        if nums[j] < nums[pivot]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        
    nums[i+1], nums[high] = nums[high] , nums[i+1]

    return i+1

nums = [3,1,6,7,2,-7,8]
n = len(nums) -1
quick_sort(nums, 0,n) # it's an in place sorting algorithm
print(nums)

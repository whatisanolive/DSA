# Brute Force
def bubble_sort_slow(nums):
    n = len(nums)
    for i in range(n):
        for j in range(1, n - i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums

nums = [3,1,6,7,2,-7,8]
print(bubble_sort_slow(nums))

# time - O(n^2) always
# space = O(1)



# Optimal 
def bubble_sort(nums):
    if not nums:
        return "Empty list"
    

    n = len(nums)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                nums[i-1] , nums[i] = nums[i] , nums[i-1]
                flag = True

    return nums



nums2 = [3,1,6,7,2,-7,8]
print(bubble_sort(nums2))

# time - O(n^2) worst case
# time - O(n) best case
# space = O(1)
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


arr = [3,1,6,7,2,-7,8]
print(bubble_sort(arr))

# time - O(n^2)
# space = O(1)
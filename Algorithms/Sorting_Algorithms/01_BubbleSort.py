# Brute Force
def bubble_sort_slow(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

arr = [3,1,6,7,2,-7,8]
print(bubble_sort_slow(arr))

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



arr2 = [3,1,6,7,2,-7,8]
print(bubble_sort(arr2))

# time - O(n^2) worst case
# time - O(n) best case
# space = O(1)
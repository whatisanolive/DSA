#time - O(n^2) , always
#space = O(1) , in-place

def insertion_sort_slow(nums):
    n = len(nums)

    for i in range(1,n):
        for j in range(i,0,-1):

            if nums[j-1] > nums[j]:
                nums[j-1] , nums[j] = nums[j] , nums[j-1]
            

    return nums

nums = [3,1,6,7,2,-7,8]
print(insertion_sort_slow(nums))



#time - O(n^2), worst case
#time = O(n), best case
#space = O(1) , in-place

def insertion_sort(nums):
    n = len(nums)

    for i in range(1,n):
        for j in range(i,0,-1):
            print("in loop")
            if nums[j-1] > nums[j]:
                nums[j-1] , nums[j] = nums[j] , nums[j-1]
            else:
                break

    return nums




nums = [3,1,6,7,2,-7,8]
print(insertion_sort(nums))

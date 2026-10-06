# selection sort works by iterating through the entire list 'i' and keep another iteration 'j', which runs from i to end of the list. We consider the smallest element as 'i' and compare it to all the elements on the right side usning the inner loop. change the smallest_index as needed and finally after the end of inner loop we swap the i and smallest_element

# Time - O(n^2)
# Space = O(1)

def selection_sort(nums):
    n = len(nums)

    for i in range( n):
        smallest_index = i

        for j in range(i,n):

            if nums[j] < nums[smallest_index]:
                smallest_index = j

        nums[smallest_index], nums[i] = nums[i], nums[smallest_index]

    return nums

nums = [3,1,6,7,2,-7,8]
print(selection_sort(nums))
# In merge sort we:

# Divide the array into two (equal) halves (divide)
# Recursively sort the two halves
# Merge the two halves to form a sorted array (conquer)

# Time - O(nlogn)

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    
    mid = len(nums)//2

    left_sorted = merge_sort(nums[:mid])

    right_sorted = merge_sort(nums[mid:])

    sorted_nums = merge(left_sorted,right_sorted)

    return sorted_nums



def merge(first, second):
    i,j=0,0
    res = []
    while i < len(first) and j < len(second):
        if first[i] > second[j]:
            res.append(second[j])
            j+=1
        else:
            res.append(first[i])
            i += 1

    res.extend(first[i:])
    res.extend(second[j:])

    return res


nums = [3,1,6,7,2,2,-7,8]
print(merge_sort(nums))



# merge_sort() divides the input array into two halves, calls itself on each half, and then merges the two sorted halves back together in order.

# The merge() function merges two already sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each only have one element. Those single element lists will be merged into a sorted list of length two, and we can build from there.

# Stable: Merge sort is a stable sort which means that values with duplicate keys in the original list will be in the same order in the sorted list.

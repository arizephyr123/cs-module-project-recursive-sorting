# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [] #[0] * elements
    # Your code here

    left.sort()
    right.sort()
    # track index in merged_arr
    i = 0 
    # for i in range(elements):
    
    #     # compare left-most of each arr
    for el in range(elements):
        while left and right:
            
            if left[0] <= right[0]:
                print(left,  right,  merged_arr, i, el)
                merged_arr.insert(i, left.pop(0))
                # iterate to next index in merged_arr
                i+=1
            if left[0] > right[0]:
                print(left,  right,  merged_arr, i, el)
                merged_arr.insert(i, right.pop(0))
                i+=1

        else:
            while right != None:
                print(left,  right,  merged_arr, i, (elements))
                merged_arr.insert(i, right.pop(0))
                i+=1
            while left != None:
                print(left,  right,  merged_arr, i, (elements))
                merged_arr.insert(i, left.pop(0))
                i+=1
            
    return merged_arr

print(merge([6, 2], [4, 1]))

'''
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    for i in range(len(arr)):


    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
'''
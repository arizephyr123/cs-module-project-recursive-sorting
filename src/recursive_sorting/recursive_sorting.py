# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [0] * elements
    # Your code here

    m = 0 # inital index of merged_arr
    l = 0 # inital index of left
    r = 0 # inital index of right
    print("====in merge", left, right)
    #while index of sub-array less than length
    ## compare at index if left, right
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            print(left,  right,  merged_arr, m)
            # print(f'left: {l}/{len(left)}\nright:{r}/{len(right)}')
            merged_arr[m] = left[l]
            # iterate to next index in left and merged
            l+=1
            m+=1
        # else:
        elif left[l] > right[r]:
            print(left,  right,  merged_arr, m)
            print(f'left: {l}/{len(left)}\nright:{r}/{len(right)}')
            merged_arr[m] = right[r]
            r += 1
            m+=1

    # while r < len(right) :
    while l == len(left) and r < len(right):
        print(left,  right,  merged_arr, m)
        print(f'left: {l}/{len(left)}\nright:{r}/{len(right)}')
        merged_arr[m] = right[r]
        # merged_arr[m:] = right[r:]

        r+=1
        m+=1
    # while l < len(left) :
    while r == len(right) and l < len(left):
        print(left,  right,  merged_arr, m)
        print(f'left: {l}/{len(left)}\nright:{r}/{len(right)}')
        merged_arr[m] = left[l]
        # merged_arr[m:] = left[l:]
        l+=1
        m+=1
    
    print("===merge done", merged_arr)
    return merged_arr
    '''

def merge( arrA, arrB ):
    # given 2 sorted arrays,
    # return a new combined array
    merged_arr = []
    # TO-DO
    i = 0
    j = 0
    # perform the actions thru both arrays
    while i < len(arrA) and j < len(arrB):
        # compare the two vlues, choose the smaller one
        if arrB[j] >= arrA[i]:
            merged_arr.append(arrA[i])
            i+=1
        # if not true, merge value from second array (because it is smaller)
        else:
            merged_arr.append(arrB[j])
            j+=1
    # Whichever array remains as the last one, 
    # the remaining values will be pushed into the merged array.

    return merged_arr  + arrA[i:] + arrB[j:]
'''

# print("merge test 2, 2",merge([1, 44],[5, 33]))
# print("merge test 1, 1",merge([1],[33]))
# print("merge test 1, empty",merge([1],[]))
# print('merge test empty empty', merge([], []))
# print('merge test', merge([8], [2, 9]))
# print('merge test', merge([8], [2, 4]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid_index = len(arr) //2
    left = arr[0:mid_index]
    right = arr[mid_index:]

    print("in Merge_sort",len(arr), mid_index,left, right)
    return merge(merge_sort(left),merge_sort(right))

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print("final return -->",merge_sort(arr1))

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start_2nd_half = mid +1
    print('merge_in_place',  )

    if arr[mid] <= arr[start_2nd_half]:
        return arr


    while (start <= mid and start_2nd_half <= end):
        if arr[start] <= arr[start_2nd_half]:
            start += 1
    else:
        value = arr[start_2nd_half]
        index = start_2nd_half
        while(index != start):
            arr[index] = index[i-1]
            index -= 1
        
        arr[start] = value

        start += 1
        mid += 1
        start_2nd_half += 1

    return arr


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print()
# print(merge_in_place([2, 4, 6, 8, 4, 5, 1], 0, 3, 6))


def merge_sort_in_place(arr, l, r):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid_index = len(arr) //2
    left_start = arr[0]
    left_end = arr[mid_index]
    right_start = arr[mid_index + 1]
    right_end = arr[-1]

    if left_end - left_start > 1:
        merge_sort_in_place(arr[left_start:left_end], left_start, left_end)
        return merge_in_place(arr[left_start:left_end], left_start, mid_index, left_end)

    elif right_end - right_start > 1:
        merge_sort_in_place(arr[right_start:right_end], right_start, right_end)
        return merge_in_place(arr[right_start:right_end], right_start, right_end)

    # return merge_in_place()



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

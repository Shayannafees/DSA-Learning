################################
################################
#dividing a list into 2 halves
def split_list(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return left,right

arr = [6,3,5,8]
left, right = split_list(arr) # type: ignore

print('left: ', left)
print('right: ', right)


################################
################################

#merge 2 sorted lists into 1 merged list
def merge_sorted_list(left, right):
    
    merged = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

left = [1,3,19]
right = [2,7,11]

print(merge_sorted_list(left,right))

################################
################################

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left, right = split_list(arr) #splitting the list/array
    sorted_left = merge_sort(left) # type: ignore # recursively sort left half
    sorted_right = merge_sort(right) # type: ignore # recursively sort left half
    return merge_sorted_list(sorted_left, sorted_right) #Merge


arr = [6,3,8,5,2,7,4,1]
sorted_arr = merge_sort(arr)
print("Sorted: ", sorted_arr)
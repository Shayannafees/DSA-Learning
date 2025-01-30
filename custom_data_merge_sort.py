def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key)
    merge_sort(right, key)

    i,j,k = 0,0,0

    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

arr = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 22}
]

s = merge_sort(arr, 'age')
print(s)

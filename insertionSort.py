# def insertionSort(arr):
#     for i in range(1,len(arr)):
#         j = i

#         while arr[j - 1] > arr[j] and j > 0:
#             arr[j-1], arr[j] = arr[j], arr[j-1]
#             print("swapped",arr[j-1], 'and', arr[j] ) 
#             print(arr)
#             j -= 1


# arr = [2,6,5,1,3,4]
# insertionSort(arr)
# print(arr)

def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i

        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]

            j -= 1

s = [3,4,7,122,543,0]
insertionSort(s)
print(s)
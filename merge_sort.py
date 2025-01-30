# def merge_sort(arr):
#     if len(arr) > 1:
#         left = arr[:len(arr)//2]            #start to mid of array
#         right = arr[len(arr)//2:]           #mid to end of array

#         #recursion
#         merge_sort(left)
#         merge_sort(right)

#         #merge
#         i,j = 0,0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1 
        
#         #putting remaining elements from left
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1
        
#         #puting remaining elems from right
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1


# arr = [3,5,56,78,23,90,56,34,76,34,53,21]
# merge_sort(arr)
# print(arr)



############
############
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        #merge
        
        i,j,k = 0,0,0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
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
    def sortLL(self):
        pass

arr = [4,2,7,1]
merge_sort(arr)
print(arr)


# def merge_sort(arr):
#     print("Khali",arr)
#     # if len(arr) < 1:
#     #     print("Hi")
#     #     return arr

#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]

#     print('left: ',left)
#     print('right: ',right)
#     print(len(arr))
#     print(mid)

#     merge_sort(left)
#     merge_sort(right)


#     i,j,k = 0,0,0
    
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
        
#         k += 1
    
#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1
    
#     while j < len(right):
#         arr[k] = right[j]
#         j += 1 
#         k += 1

    
# A = [3,65,78,1,43,54,23]
# merge_sort(A)
# print(A)
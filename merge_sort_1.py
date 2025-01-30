def MergeSort(series):
    print("Khali",series)
    if len(series) <= 1:        #added = sign now
        return series

    if len(series) > 1:
        mid = len(series)//2
        left = series[:mid]
        right = series[mid:]
    
        # print('left: ',left)
        # print('right: ',right)
        # print(len(series))
        # print(mid)
    
        MergeSort(left)
        MergeSort(right)
    
        i,j,k = 0,0,0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                series[k] = left[i]
                i += 1
            else:
                series[k] = right[j]
                j += 1          #j incrementation was missed, now fixed 
            k += 1
        
        while i < len(left):
            series[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            series[k] = right[j]
            j += 1 
            k += 1
    


s = [11,13,7,5,3,31]
MergeSort(s)
print("Final Sorted Array: ",s)
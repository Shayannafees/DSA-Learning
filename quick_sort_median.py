def Partition (A, l, h):
    mid = (l+h)//2
    pivot = A[mid]
    print("Pivot: ", pivot)
    i,j = l,h

    while i < j:
        while pivot > A[i]:
            i += 1

        while pivot < A[j]:
            j -= 1
        
        if i < j:
            A[i], A[j] = A[j], A[i]
            print("inner while: ",s)
        
    pivot, A[j] = A[j], pivot
    # print("Outside While: ", s)

    return j

def QuickSort(A,l,h):
    if l < h:
        shayan = Partition(A,l,h)
        QuickSort(A,l,shayan-1)
        QuickSort(A,shayan+1,h)



s = [11,13,7,5,31]
QuickSort(s,0,len(s)-1)
print("Final Sorted Array: ",s)



def Partition (A, l, h):
    pivot = A[l]
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
        QuickSort(A,l,shayan)
        QuickSort(A,shayan+1,h)



s = [1,2,4,6,8,9,13,15,30,35,57]
QuickSort(s,0,len(s)-1)
print("Final Sorted Array: ",s)



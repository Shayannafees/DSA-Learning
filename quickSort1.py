def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    
    length = len(sequence)

    pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for i in sequence:
        if i < pivot:
            items_lower.append(i)
        else:
            items_greater.append(i)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([56,45,2,6,3567,34,753,8,9,0]))
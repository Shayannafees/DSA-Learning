arr = [2,3,1,2,4,3]
target = 7
positive_infinity = float('inf')


def minSubArray(arr, target):

    low, high = 0,0
    current_Sum = 0
    minLenWindow = positive_infinity

    while high < len(arr):
        current_Sum += arr[high]
        high += 1
        print(high)
        
        while current_Sum >= target:
            currWindowSize = high - low
            minLenWindow = min(minLenWindow, currWindowSize)

            current_Sum -= arr[low]
            low += 1

    return minLenWindow 

print(minSubArray(arr,target))
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

l = [3,2,9,6,4,5,11,6,7]
print(bubbleSort(l))

def selectionSort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
                arr[i], arr[minIndex] =  arr[minIndex], arr[i]
    return arr

l = [2,4,1,5,6,8,7,19,11]
print(selectionSort(l))
            

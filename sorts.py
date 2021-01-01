import random
import time
def bubbleSort(array):
    #time complexity o(n^2)
    arr = array.copy()
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                sorted = False
    return arr

def merge(arr1, arr2):
    arr = []
    arr1index = 0
    arr2index = 0
    lastChanged1 = False
    while arr1index < len(arr1) and arr2index < len(arr2):
        if arr1[arr1index] < arr2[arr2index]:
            arr.append(arr1[arr1index])
            arr1index += 1
            lastChanged1 = True
        else:
            arr.append(arr2[arr2index])
            arr2index += 1
            lastChanged1 = False
    if lastChanged1:
        arr += arr2[arr2index:]
    else:
        arr += arr1[arr1index:]
    return arr

def mergeSort(array):
    arrays = [[i] for i in array]
    while len(arrays) > 1:
        newArrays = []
        for i in range(len(arrays)//2):
            newArrays.append(merge(arrays[i*2], arrays[1+(i*2)]))
        if(len(arrays) & 1):
            newArrays.append(arrays[-1])
        arrays = newArrays
    return arrays[0]





arr1 = list(range(10, 0, -1))
arr2 = [random.randrange(0,100) for i in range(10)]

print(bubbleSort(arr1))
print(bubbleSort(arr2))


print(mergeSort(arr1))
print(mergeSort(arr2))



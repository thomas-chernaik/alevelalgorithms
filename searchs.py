import random
def linear(list, item):
    for index, i in enumerate(list):
        if item == i:
            return index

    return None
def binary(list, item):
    start = 0
    end = len(list)-1
    midpoint = 1
    while start != end:
        midpoint = (start+end)//2
        if list[midpoint] == item:
            return midpoint
        if list[midpoint] < item:
            start = midpoint+1
        else: #if list[midpoint] > item
            end = midpoint-1
    midpoint = (start + end) // 2
    if list[midpoint] == item:
        return midpoint
    return None
listyList = [random.randrange(0,1000) for i in range(1000)]
listyList.sort()

output = linear(listyList, 50)
if output:
    print("found at index with linear")
    print(output)
    print(listyList[output])

output = binary(listyList, 50)
if output:
    print("found at index with binary")
    print(output)
    print(listyList[output])
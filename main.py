import random
import time

def searchLinary(array: list, findNumber: int):
    """O(n)"""

    for i in range(len(array)):
        if array[i] == findNumber:
            return i
    else:
        return "Элемент отсутствует в списке"

def searchBinary(array: list, findNumber: int):
    """O(log2(n))"""

    lengthArray = len(array)
    beginArray = 0
    endArray = lengthArray - 1

    while True:
        center = (endArray - beginArray) // 2 + beginArray
        if beginArray == center:
            return "Элемент отсутствует в списке"
        if array[center] == findNumber:
            return center
        elif array[center] > findNumber:
            endArray = center
        else:
            beginArray = center

def sortBubble(array: list):
    """O(n^2)"""

    for j in range(len(array) - 1):
        for i in range(1, len(array), 1):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
    return array

def sortShake(array:list):
    """O(n^2)"""

    lengthArray = len(array)
    beginArray = 1
    endArray = lengthArray - 1

    while (beginArray < (lengthArray)):
        beginArray += 1
        for i in range(beginArray - 1, endArray, 1):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
        endArray -= 1
        for i in range(endArray + 1, beginArray - 2, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]

    return array

def sortChoise(array:list):
    """O(n^2)"""

    ind = 0
    while ind < len(array)-1:
        min_ = array[ind]
        for i in range(ind, len(array), 1):
            if min_ > array[i]:
                min_ = array[i]
                array[ind], array[i] = array[i], array[ind]
        ind += 1

    return array

def sortInsertion(array:list):
    """O(n^2)"""

    for i in range(1, len(array), 1):
        j = i
        while (j > 0) and (array[j-1]>array[j]):
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array
    
def sortMerge(array:list):
    """O(n*log(n))"""
    if (len(array) > 1):
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        sortMerge(lefthalf)
        sortMerge(righthalf)

        i = 0
        j = 0
        k = 0

        while (i < len(lefthalf)) and (j < len(righthalf)):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1
        
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1
        
    return array

def main():
    findNumber = int(input("Какое число найти: "))
    __value = 10000
    array = [random.randint(0, 1500) for i in range(__value)]
    # print(array,"\n")
    tic = time.time()
    # sortMerge(array)
    # print(sortMerge(array))
    
    findNumberIndex = searchLinary(sortMerge(array), findNumber)
    toc = time.time()
    print("\n{:.10f}\n".format(toc - tic))
    print("Элемент под индексом ", findNumberIndex)


main()


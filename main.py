import random
import time

def searchLinary(array: list, findNumber: int):
    for i in range(len(array)):
        if array[i] == findNumber:
            return i
    else:
        return "Элемент отсутствует в списке"

def searchBinary(array: list, findNumber: int):
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

def sortQuick(array: list):
    for j in range(len(array) - 1):
        for i in range(1, len(array), 1):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
    return array


def main():
    findNumber = int(input("Какое число найти: "))
    __value = 1500
    array = [random.randint(0, 1500) for i in range(__value)]
    # print(sortArray(array))
    findNumberIndex = searchLinary(sortArray(array), findNumber)
    print("Элемент под индексом ", findNumberIndex)

tic = time.time()
main()
toc = time.time()
print("\n{:.6f}".format(toc - tic))

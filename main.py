import random
import time

def searchInArray(array: list, findNumber: int):
    lengthArray = len(array)
    beginArray = 0
    endArray = lengthArray - 1
    while True:
        center = (endArray - beginArray) // 2 + beginArray
        # print("\n\n", beginArray, " ", center, " ", endArray)
        if beginArray == center:
            return "Элемент отсутствует в списке"
        if array[center] == findNumber:
            return center
        elif array[center] > findNumber:
            endArray = center
        # print(array[center], " > ", findNumber)
        else:
            beginArray = center
        # print(array[center], " < ", findNumber)


def sortArray(array: list):
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
    findNumberIndex = searchInArray(searchInArray(array), findNumber)
    print("Элемент под индексом ", findNumberIndex)

tic = time.time()
main()
toc = time.time()
print("\n{:.6f}".format(toc - tic))

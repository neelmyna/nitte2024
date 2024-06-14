def bubbleSort(array):
    for i in range(len(array)-1):
        arraySorted = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                arraySorted = False
        if arraySorted:
            return
numbers = '19  23  7  2  5  11  3  17  29'
array = [int(item) for item in numbers.split()]
bubbleSort(array)
print('Unsorted Array is', numbers)
numbers = ' '.join([str(item) for item in array])
print('Sorted Array is', numbers)

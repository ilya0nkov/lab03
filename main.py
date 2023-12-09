def bubble_sort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array
'''
# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print("Отсортированный массив:", array)
'''
if __name__ == "__main__":
    array = []
    n = int(input('Enter N\n'))
    for i in range(n):
        number = int(input('Enter number\n'))
        array.append(number)
    array = bubble_sort(array)
    print("Sorted array:", array)
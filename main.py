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


if __name__ == "__main__":
    mode = int(input("Enter 1 if you want a direct order"
                     "else if you want reverse order enter 2\n"))

    array = []
    n = int(input('Enter N\n'))
    for i in range(n):
        number = int(input('Enter number\n'))
        array.append(number)
    array = bubble_sort(array)

    if mode == 1:
        print("Sorted array:", array)
    else:
        print("Sorted array:", array[::-1])

